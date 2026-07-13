"""Ingestion 模块路由层 — 接入任务管理 + 数据浏览。"""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.ingestion import dao
from app.modules.ingestion.models import IngestionBatch, IngestionTask
from app.modules.ingestion.schemas.ingestion_task import (
    BatchProgressResponse,
    ImportErrorResponse,
    IngestionBatchResponse,
    IngestionTaskCreate,
    IngestionTaskResponse,
    IngestionTaskUpdate,
)

# ── 两个子路由 ──────────────────────────────

task_router = APIRouter(prefix="/ingestion-tasks", tags=["ingestion"])
browse_router = APIRouter(prefix="/data-browse", tags=["data-browse"])


def _dump(model):
    return model.model_dump(mode="json", by_alias=True)


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


def _paginated(items, total, page, page_size):
    return _ok({"items": items, "total": total, "page": page, "pageSize": page_size}, msg="OK")


# ═══════════════════════════════════════════
# 接入任务
# ═══════════════════════════════════════════

@task_router.get("")
async def list_tasks(
    keyword: str | None = Query(None),
    status: str | None = Query(None),
    data_source_id: uuid.UUID | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.task_list(
        db, keyword=keyword, status=status,
        data_source_id=data_source_id, page=page, page_size=page_size,
    )
    return _paginated(
        [_dump(IngestionTaskResponse.model_validate(i)) for i in items],
        total, page, page_size,
    )


@task_router.post("", status_code=201)
async def create_task(
    data: IngestionTaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = IngestionTask(**data.model_dump())
    task = await dao.task_insert(db, task)
    return _ok(_dump(IngestionTaskResponse.model_validate(task)), msg="task created")


@task_router.get("/{task_id}")
async def get_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    return _ok(_dump(IngestionTaskResponse.model_validate(task)))


@task_router.put("/{task_id}")
async def update_task(
    task_id: uuid.UUID,
    data: IngestionTaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    task = await dao.task_update(db, task)
    return _ok(_dump(IngestionTaskResponse.model_validate(task)), msg="task updated")


@task_router.delete("/{task_id}")
async def delete_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    task.status = "disabled"
    await dao.task_update(db, task)
    return _ok(msg="task disabled")


@task_router.post("/{task_id}/enable")
async def enable_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    task.status = "active"
    await dao.task_update(db, task)
    return _ok(msg="task enabled")


@task_router.post("/{task_id}/disable")
async def disable_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    task.status = "paused"
    await dao.task_update(db, task)
    return _ok(msg="task disabled")


@task_router.get("/{task_id}/batches")
async def list_batches(
    task_id: uuid.UUID,
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.batch_list(
        db, task_id=task_id, status=status, page=page, page_size=page_size,
    )
    return _paginated(
        [_dump(IngestionBatchResponse.model_validate(i)) for i in items],
        total, page, page_size,
    )


@task_router.get("/batches/{batch_id}")
async def get_batch(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    batch = await dao.batch_get_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="not found")
    return _ok(_dump(IngestionBatchResponse.model_validate(batch)))


@task_router.get("/batches/{batch_id}/progress")
async def get_batch_progress(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    batch = await dao.batch_get_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="not found")
    if batch.status == "running":
        progress, step = -1, "running..."
    elif batch.status in ("success", "partial_success"):
        progress, step = 100, "done"
    elif batch.status == "failed":
        progress, step = 100, f"failed: {batch.error_summary or ''}"
    else:
        progress, step = 0, "pending"
    return _ok(_dump(BatchProgressResponse(
        batchId=str(batch.id), status=batch.status,
        progress=progress, step=step, lastHeartbeat=batch.started_at,
    )))


@task_router.get("/batches/{batch_id}/errors")
async def list_batch_errors(
    batch_id: uuid.UUID,
    error_level: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.error_list(
        db, batch_id=batch_id, error_level=error_level, page=page, page_size=page_size,
    )
    return _paginated(
        [_dump(ImportErrorResponse.model_validate(i)) for i in items],
        total, page, page_size,
    )


@task_router.post("/{task_id}/execute")
async def execute_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    if task.status == "disabled":
        raise HTTPException(status_code=400, detail="task disabled")

    batch = IngestionBatch(
        task_id=task.id, trigger_type="manual",
        status="pending", triggered_by=str(current_user.id),
    )
    await dao.batch_insert(db, batch)

    try:
        from app.core.queue import redis_conn
        from rq import Queue
        queue = Queue("ingestion", connection=redis_conn)
        job = queue.enqueue(
            "app.modules.ingestion.tasks.sync_tasks.run_echo_sync",
            str(task.id), str(batch.id), task.name, job_timeout=60,
        )
        batch.status = "running"
        batch.started_at = datetime.now(timezone.utc)
        await dao.batch_update(db, batch)
        return _ok({"batchId": str(batch.id), "jobId": job.id}, msg="task submitted")
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await dao.batch_update(db, batch)
        raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")


@task_router.post("/batches/{batch_id}/retry")
async def retry_batch(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    old = await dao.batch_get_by_id(db, batch_id)
    if not old:
        raise HTTPException(status_code=404, detail="not found")
    task = await dao.task_get_by_id(db, old.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    batch = IngestionBatch(
        task_id=task.id, trigger_type="retry",
        status="pending", triggered_by=str(current_user.id),
    )
    await dao.batch_insert(db, batch)

    try:
        from app.core.queue import redis_conn
        from rq import Queue
        queue = Queue("ingestion", connection=redis_conn)
        job = queue.enqueue(
            "app.modules.ingestion.tasks.sync_tasks.run_echo_sync",
            str(task.id), str(batch.id), f"{task.name} (retry)", job_timeout=60,
        )
        batch.status = "running"
        batch.started_at = datetime.now(timezone.utc)
        await dao.batch_update(db, batch)
        return _ok(
            {"batchId": str(batch.id), "jobId": job.id, "retryFrom": str(batch_id)},
            msg="retry submitted",
        )
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await dao.batch_update(db, batch)
        raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")


# ═══════════════════════════════════════════
# 数据浏览
# ═══════════════════════════════════════════

@browse_router.get("/tables")
async def list_tables(
    schema: str = Query("raw"),
    system: str = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """列出 raw schema 下的表及行数。"""
    if system:
        sql = text(
            "SELECT t.table_name,"
            "  (SELECT count(*) FROM information_schema.columns"
            "   WHERE table_schema=:schema AND table_name=t.table_name) as col_count"
            " FROM information_schema.tables t"
            " WHERE t.table_schema = :schema AND t.table_name LIKE :pat"
        )
        params = {"schema": schema, "pat": f"{system}_%"}
    else:
        sql = text(
            "SELECT t.table_name,"
            "  (SELECT count(*) FROM information_schema.columns"
            "   WHERE table_schema='raw' AND table_name=t.table_name) as col_count"
            " FROM information_schema.tables t"
            " WHERE t.table_schema = :schema"
        )
        params = {"schema": schema}

    result = await db.execute(sql, params)
    tables = []
    for row in result:
        table_name = row.table_name
        count_result = await db.execute(text(f"SELECT count(*) FROM {schema}.{table_name}"))
        count = count_result.scalar_one()
        tables.append({"table_name": table_name, "row_count": count})
    return {"code": 0, "message": "success", "msg": "OK", "data": tables}


@browse_router.get("/sample")
async def get_sample(
    table: str = Query(...),
    limit: int = Query(20, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """获取指定表的抽样数据（仅 payload 展开）。"""
    schema, tbl = table.split(".", 1) if "." in table else ("raw", table)
    try:
        result = await db.execute(
            text(f"SELECT payload FROM {schema}.{tbl} ORDER BY _ingested_at DESC LIMIT :lim"),
            {"lim": limit},
        )
        rows = []
        for row in result:
            payload = row.payload
            if isinstance(payload, str):
                import json
                payload = json.loads(payload)
            rows.append(payload)
        return {"code": 0, "message": "success", "msg": "OK", "data": rows}
    except Exception as e:
        return {"code": 0, "message": "success", "msg": "OK", "data": [], "error": str(e)}
