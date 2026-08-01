"""Ingestion 模块路由层 — 接入任务管理 + 数据浏览。"""

import asyncio
import json
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from decimal import Decimal
from pydantic import BaseModel
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
    QuickFillRequest,
    TimeRangeResponse,
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


class PreviewCronRequest(BaseModel):
    cronExpression: str = ""


@task_router.post("/preview-cron")
async def preview_cron(body: PreviewCronRequest):
    """Cron 表达式预览：返回合法性、下次执行时间、描述（B2.3 / F2.1 用）。"""
    from app.modules.ingestion.scheduler import _normalize_cron
    from apscheduler.triggers.cron import CronTrigger
    from datetime import datetime as _dt

    expr = (body.cronExpression or "").strip()
    if not expr:
        return _ok({"isValid": False, "nextRun": None, "description": None})
    try:
        trigger = CronTrigger.from_crontab(_normalize_cron(expr))
        nxt = trigger.get_next_fire_time(None, _dt.now(timezone.utc))
        return _ok({
            "isValid": True,
            "nextRun": nxt.isoformat() if nxt else None,
            "description": str(trigger),
        })
    except Exception:
        return _ok({"isValid": False, "nextRun": None, "description": None})


def _enqueue(task_id, batch_id, task_name, timeout=60):
    """将同步任务入队 RQ，返回 job_id。"""
    from app.core.queue import redis_conn
    from rq import Queue
    queue = Queue("ingestion", connection=redis_conn)
    job = queue.enqueue(
        "app.modules.ingestion.tasks.sync_tasks.run_echo_sync",
        str(task_id), str(batch_id), task_name, job_timeout=timeout,
    )
    return job.id


def _enqueue_api_sync(
    task_id, batch_id, config_path="", interfaces=None,
    data_source_id=None, timeout=7200,
):
    """Enqueue API full sync task to RQ.

    Args:
        task_id: IngestionTask UUID.
        batch_id: Pre-created IngestionBatch UUID.
        config_path: Optional YAML config path (provides interfaces).
        interfaces: Optional list of interface names to sync.
        data_source_id: DataSource UUID — used to load DB connection config.
        timeout: RQ job timeout.
    """
    from app.core.queue import redis_conn
    from rq import Queue
    queue = Queue("ingestion", connection=redis_conn)
    job = queue.enqueue(
        "app.modules.ingestion.tasks.sync_tasks.run_api_full_sync",
        str(task_id), str(batch_id), config_path or "", interfaces,
        str(data_source_id) if data_source_id else None,
        job_timeout=timeout,
    )
    return job.id


def _recent_start(config: dict | None, default_days: int = 30) -> datetime:
    """从任务 config 解析默认拉取起始时间。"""
    days = config.get("default_recent_days", default_days) if config else default_days
    return datetime.now(timezone.utc) - timedelta(days=days)


# ═══════════════════════════════════════════
# 接入任务 CRUD
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
    # B2.2：新建任务默认 active，调度器 60s 轮询才会注册 cron 任务。
    # （model 默认 status="draft"，若留 draft 调度器永不注册 → 定时任务不生效）
    # 删除 disable→disabled、disable_task→paused、enable_task→active 均保持联动。
    task.status = "active"
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


# ═══════════════════════════════════════════
# 隔离区（B2.6）
# ═══════════════════════════════════════════

@task_router.get("/{task_id}/quarantine")
async def list_quarantine_endpoint(
    task_id: uuid.UUID,
    status: str | None = Query(None),
    interfaceName: str | None = Query(None),
    page: int = Query(1, ge=1),
    pageSize: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
):
    """隔离区记录列表（分页 + 状态/接口筛选）。"""
    from app.modules.ingestion.quarantine_service import list_quarantine
    from app.modules.ingestion.services.sync_database import SyncSessionLocal

    def _run():
        s = SyncSessionLocal()
        try:
            return list_quarantine(s, task_id, status, interfaceName, page, pageSize)
        finally:
            s.close()

    items, total = await asyncio.to_thread(_run)
    return _paginated(items, total, page, pageSize)


@task_router.get("/{task_id}/quarantine/stats")
async def quarantine_stats_endpoint(
    task_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
):
    """隔离区统计：总数/待处理/已修复/已忽略/隔离率/阈值/熔断触发。"""
    from app.modules.ingestion.quarantine_service import get_stats
    from app.modules.ingestion.services.sync_database import SyncSessionLocal

    def _run():
        s = SyncSessionLocal()
        try:
            return get_stats(s, task_id)
        finally:
            s.close()

    return _ok(await asyncio.to_thread(_run))


@task_router.post("/quarantine/{qid}/retry")
async def retry_quarantine_endpoint(
    qid: uuid.UUID,
    current_user: User = Depends(get_current_user),
):
    """重试单条隔离记录：raw_json 经 StageWriter 单行写回 raw 表。"""
    from app.modules.ingestion.quarantine_service import retry_quarantine
    from app.modules.ingestion.services.sync_database import SyncSessionLocal

    def _run():
        s = SyncSessionLocal()
        try:
            return retry_quarantine(s, qid)
        finally:
            s.close()

    return _ok(await asyncio.to_thread(_run))


@task_router.post("/quarantine/{qid}/ignore")
async def ignore_quarantine_endpoint(
    qid: uuid.UUID,
    current_user: User = Depends(get_current_user),
):
    """忽略单条隔离记录：status='ignored'。"""
    from app.modules.ingestion.quarantine_service import ignore_quarantine
    from app.modules.ingestion.services.sync_database import SyncSessionLocal

    def _run():
        s = SyncSessionLocal()
        try:
            return ignore_quarantine(s, qid)
        finally:
            s.close()

    return _ok(await asyncio.to_thread(_run))


# ═══════════════════════════════════════════
# 批次查询
# ═══════════════════════════════════════════

@task_router.get("/{task_id}/batches")
async def list_batches(
    task_id: uuid.UUID,
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
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
        progress, step = -1, "同步中..."
    elif batch.status in ("success", "partial_success"):
        progress, step = 100, "完成"
    elif batch.status == "failed":
        progress, step = 100, f"失败: {batch.error_summary or ''}"
    else:
        progress, step = 0, "等待中"
    return _ok(_dump(BatchProgressResponse(
        batchId=str(batch.id), status=batch.status,
        progress=progress, step=step, lastHeartbeat=batch.started_at,
    )))


@task_router.get("/batches/{batch_id}/stream")
async def stream_batch_progress(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    """SSE endpoint that pushes batch progress updates in real-time."""
    async def event_generator():
        import app.modules.ingestion.dao as ingestion_dao
        dao = ingestion_dao
        for _ in range(360):  # max 6 min (360 × 1s)
            db.expire_all()  # clear identity map so we see worker's committed updates
            batch = await dao.batch_get_by_id(db, batch_id)
            if not batch:
                break

            # Use progress_step from the worker if available, otherwise default
            if batch.status == "running":
                step = batch.progress_step or "同步中..."
                pct = -1
            elif batch.status in ("success", "partial_success"):
                pct, step = 100, "完成"
            elif batch.status == "failed":
                pct, step = 100, f"失败: {batch.error_summary or ''}"
            elif batch.status == "cancelled":
                pct, step = 0, "已取消"
            else:
                pct, step = 0, "等待中"

            data = json.dumps({
                "pct": pct,
                "step": step,
                "status": batch.status,
                "startedAt": batch.started_at.isoformat() if batch.started_at else None,
                "recordCount": batch.record_count or 0,
                "successCount": batch.success_count or 0,
                "failCount": batch.fail_count or 0,
                "skipCount": batch.skip_count or 0,
                "sourceSignature": batch.source_signature or "",
            })
            yield f"data: {data}\n\n"

            if batch.status in ("success", "partial_success", "failed", "cancelled"):
                break

            await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


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


# ═══════════════════════════════════════════
# 同步触发
# ═══════════════════════════════════════════

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
        status="running", started_at=datetime.now(timezone.utc),
        triggered_by=str(current_user.id),
    )
    await dao.batch_insert(db, batch)
    await db.commit()  # commit before enqueue so worker can see the batch

    # 根据 access_method 选择同步引擎
    # config JSON keys may be camelCase (from frontend) or snake_case
    _cfg = (task.config or {})
    access_method = _cfg.get("accessMethod") or _cfg.get("access_method") or ""
    if access_method in ("api", "api_pull"):
        config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
        interfaces = _cfg.get("interfaces")
        # config_path 和 data_source_id 至少有一个：YAML 提供 interfaces，DB 提供 connection
        if not config_path and not task.data_source_id:
            raise HTTPException(
                status_code=400,
                detail="API sync requires config_path or data_source_id with DB connection config",
            )
        try:
            job_id = _enqueue_api_sync(
                task.id, batch.id, config_path, interfaces,
                data_source_id=task.data_source_id,
            )
        except Exception as e:
            batch.status = "failed"
            batch.error_summary = f"enqueue failed: {e}"
            await dao.batch_update(db, batch)
            await db.commit()
            raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")
    else:
        try:
            job_id = _enqueue(task.id, batch.id, task.name)
        except Exception as e:
            batch.status = "failed"
            batch.error_summary = f"enqueue failed: {e}"
            await dao.batch_update(db, batch)
            await db.commit()
            raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")

    return _ok({"batchId": str(batch.id), "jobId": job_id}, msg="task submitted")


@task_router.post("/{task_id}/soft-delete-check")
async def soft_delete_check(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """触发软删除检测（B3.2）：作为 RQ 任务异步执行，结果写回 task.config.softDeleteLast。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    if task.status == "disabled":
        raise HTTPException(status_code=400, detail="task disabled")

    _cfg = (task.config or {})
    config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
    if not config_path and not task.data_source_id:
        raise HTTPException(
            status_code=400,
            detail="soft-delete check requires config_path or data_source_id",
        )
    try:
        from app.core.queue import redis_conn
        from rq import Queue

        queue = Queue("ingestion", connection=redis_conn)
        job = queue.enqueue(
            "app.modules.ingestion.tasks.sync_tasks.run_soft_delete_check",
            str(task.id),
            config_path,
            str(task.data_source_id) if task.data_source_id else None,
            job_timeout=7200,
        )
        return _ok({"jobId": job.id, "taskId": str(task.id)}, msg="soft-delete check submitted")
    except Exception as e:
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
        status="running", started_at=datetime.now(timezone.utc),
        triggered_by=str(current_user.id),
    )
    await dao.batch_insert(db, batch)
    await db.commit()  # commit before enqueue so worker can see the batch

    try:
        _cfg = (task.config or {})
        access_method = _cfg.get("accessMethod") or _cfg.get("access_method") or ""
        if access_method in ("api", "api_pull"):
            config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
            interfaces = _cfg.get("interfaces")
            job_id = _enqueue_api_sync(
                task.id, batch.id, config_path, interfaces,
                data_source_id=task.data_source_id,
            )
        else:
            job_id = _enqueue(task.id, batch.id, f"{task.name} (retry)")
        return _ok(
            {"batchId": str(batch.id), "jobId": job_id, "retryFrom": str(batch_id)},
            msg="retry submitted",
        )
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await dao.batch_update(db, batch)
        await db.commit()
        raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")


# ═══════════════════════════════════════════
# 全量回溯 / 近期快补（目标1：保证所有源数据落入 Raw 层）
# ═══════════════════════════════════════════

@task_router.post("/{task_id}/backfill")
async def backfill_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """全量同步：拉取所有历史数据，保证 Raw 层有完整数据。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")

    batch = IngestionBatch(
        task_id=task.id, trigger_type="backfill",
        status="running", started_at=datetime.now(timezone.utc),
        triggered_by=str(current_user.id),
    )
    await dao.batch_insert(db, batch)
    await db.commit()  # commit before enqueue so worker can see the batch

    try:
        # 根据 access_method 选择同步引擎（与 execute_task 一致）
        _cfg = (task.config or {})
        access_method = _cfg.get("accessMethod") or _cfg.get("access_method") or ""
        if access_method in ("api", "api_pull"):
            config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
            interfaces = _cfg.get("interfaces")
            job_id = _enqueue_api_sync(
                task.id, batch.id, config_path, interfaces,
                data_source_id=task.data_source_id, timeout=7200,
            )
        else:
            job_id = _enqueue(task.id, batch.id, f"{task.name} (backfill)", timeout=7200)
        return _ok({
            "batchId": str(batch.id), "jobId": job_id,
        }, msg="全量同步已提交")
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await dao.batch_update(db, batch)
        await db.commit()
        raise HTTPException(status_code=500, detail=str(e))


@task_router.post("/{task_id}/quick-fill")
async def quick_fill_task(
    task_id: uuid.UUID,
    data: QuickFillRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """近期快补：指定起止时间拉取数据，用于补漏（如接口故障导致缺失几天数据）。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")

    batch = IngestionBatch(
        task_id=task.id, trigger_type="quick_fill",
        status="running", started_at=datetime.now(timezone.utc),
        triggered_by=str(current_user.id),
    )
    await dao.batch_insert(db, batch)
    await db.commit()  # commit before enqueue so worker can see the batch

    try:
        _cfg = (task.config or {})
        access_method = _cfg.get("accessMethod") or _cfg.get("access_method") or ""
        if access_method in ("api", "api_pull"):
            config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
            interfaces = _cfg.get("interfaces")
            job_id = _enqueue_api_sync(
                task.id, batch.id, config_path, interfaces,
                data_source_id=task.data_source_id, timeout=3600,
            )
        else:
            job_id = _enqueue(
                task.id, batch.id,
                f"{task.name} (quick-fill {data.start_time.date()}→{data.end_time.date()})",
                timeout=3600,
            )
        return _ok({
            "batchId": str(batch.id), "jobId": job_id,
            "startTime": data.start_time.isoformat(),
            "endTime": data.end_time.isoformat(),
        }, msg="快补任务已提交")
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await dao.batch_update(db, batch)
        await db.commit()
        raise HTTPException(status_code=500, detail=str(e))


@task_router.get("/{task_id}/time-range")
async def get_time_range(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """查询建议的同步时间范围（仅预览，不触发同步）。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")

    now = datetime.now(timezone.utc)

    return _ok(_dump(TimeRangeResponse(
        sync_mode=task.sync_mode,
        last_sync_at=task.last_sync_at,
        suggested_start=now,
        suggested_end=now,
        schedule_cron=task.cron_expression,
        schedule_description=_cron_desc(task.cron_expression) if task.cron_expression else "未配置定时",
    )))


def _cron_desc(expr: str) -> str:
    """简单 Cron 转中文描述。"""
    parts = expr.strip().split()
    if len(parts) != 5:
        return expr
    minute, hour, dom, month, dow = parts
    if dom == "*" and month == "*":
        if dow == "*":
            return f"每天 {hour}:{minute.zfill(2)} 执行"
        return f"每周{dow} {hour}:{minute.zfill(2)} 执行"
    return expr


# ═══════════════════════════════════════════
# 同步引擎优化 Phase 1：对账 / Schema 漂移审计 API (B1.4)
# 约定：API 一律 camelCase（项目 CamelModel 规范），但本组端点直接走裸 SQL，
# 故在返回前手动将 snake_case 列名转 camelCase，并序列化 UUID/Decimal/DateTime。
# ═══════════════════════════════════════════

def _snake_to_camel(key: str) -> str:
    head, *tail = key.split("_")
    return head + "".join(w.title() for w in tail)


def _row_to_camel(row) -> dict:
    """将裸 SQL 行（RowMapping / dict）转为 camelCase、JSON 安全的 dict。"""
    out: dict = {}
    for k, v in dict(row).items():
        if isinstance(v, uuid.UUID):
            v = str(v)
        elif isinstance(v, Decimal):
            v = float(v)
        elif isinstance(v, datetime):
            v = v.isoformat()
        out[_snake_to_camel(k)] = v
    return out


class ReconcileRequest(BaseModel):
    level: str = "L1"  # L1 / L2 / L3


class RepairRequest(BaseModel):
    segment: str | None = None


async def _resolve_ds_code(db: AsyncSession, data_source_id) -> str | None:
    """根据 data_source_id 取数据源 code，用于 Schema 变更按 raw.{code}_ 前缀做作用域过滤。"""
    if not data_source_id:
        return None
    try:
        row = await db.execute(
            text("SELECT code FROM data_sources WHERE id = :ds"),
            {"ds": str(data_source_id)},
        )
        return row.scalar_one_or_none()
    except Exception:
        return None


@task_router.get("/{task_id}/schema-changes")
async def list_schema_changes(
    task_id: uuid.UUID,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Schema 变更审计列表（best-effort 按数据源 raw 表前缀过滤）。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")

    # sync_schema_changes 表无 task/data_source 字段，仅以 table_name 记录；
    # 用数据源 code 前缀 best-effort 收敛到本任务所属数据源的 raw 表。
    code = await _resolve_ds_code(db, task.data_source_id)
    where = ""
    params: dict = {}
    if code:
        # raw 表前缀为 raw.{code小写}_，但 data_sources.code 可能大写，
        # 用 ILIKE 消除大小写不匹配（如 code='MES' 但表为 raw.mes_*）
        where = "WHERE table_name ILIKE :pat"
        params["pat"] = f"raw.{code}_%"

    total = (await db.execute(
        text(f"SELECT count(*) FROM sync_schema_changes {where}"), params
    )).scalar_one()

    offset = (page - 1) * page_size
    result = await db.execute(
        text(
            f"SELECT id, table_name, change_type, column_name, detail, detected_at "
            f"FROM sync_schema_changes {where} "
            f"ORDER BY detected_at DESC LIMIT :lim OFFSET :off"
        ),
        {**params, "lim": page_size, "off": offset},
    )
    items = [_row_to_camel(r) for r in result.mappings().all()]
    return _paginated(items, total, page, page_size)


@task_router.get("/{task_id}/reconciliations")
async def list_reconciliations(
    task_id: uuid.UUID,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """对账记录列表（按数据源过滤，含 L1/L2/L3）。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    if not task.data_source_id:
        return _paginated([], 0, page, page_size)

    ds = str(task.data_source_id)
    total = (await db.execute(
        text("SELECT count(*) FROM sync_reconciliations WHERE data_source_id = :ds"),
        {"ds": ds},
    )).scalar_one()

    offset = (page - 1) * page_size
    result = await db.execute(
        text(
            "SELECT id, data_source_id, interface_name, batch_id, check_level, "
            "api_total, db_count, pulled_count, diff_count, diff_ratio, status, "
            "sync_mode, detail, checked_at "
            "FROM sync_reconciliations WHERE data_source_id = :ds "
            "ORDER BY checked_at DESC LIMIT :lim OFFSET :off"
        ),
        {"ds": ds, "lim": page_size, "off": offset},
    )
    items = [_row_to_camel(r) for r in result.mappings().all()]
    return _paginated(items, total, page, page_size)


@task_router.get("/reconciliations/{recon_id}")
async def get_reconciliation(
    recon_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """对账详情（含 detail 分段，L1 暂无分段）。"""
    row = await db.execute(
        text(
            "SELECT id, data_source_id, interface_name, batch_id, check_level, "
            "api_total, db_count, pulled_count, diff_count, diff_ratio, status, "
            "sync_mode, detail, checked_at "
            "FROM sync_reconciliations WHERE id = :id"
        ),
        {"id": str(recon_id)},
    )
    rec = row.mappings().first()
    if not rec:
        raise HTTPException(status_code=404, detail="not found")
    return _ok(_row_to_camel(rec))


@task_router.post("/{task_id}/reconcile")
async def trigger_reconcile(
    task_id: uuid.UUID,
    body: ReconcileRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """触发对账。L1 = 重新跑一次同步（同步引擎内部已含 L1 轻量对账）；L2/L3 深度对账后续实现。"""
    task = await dao.task_get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    level = (body.level or "L1").upper()

    if level == "L1":
        batch = IngestionBatch(
            task_id=task.id, trigger_type="manual",
            status="running", started_at=datetime.now(timezone.utc),
            triggered_by=str(current_user.id),
        )
        await dao.batch_insert(db, batch)
        await db.commit()  # commit before enqueue so worker can see the batch

        _cfg = (task.config or {})
        access_method = _cfg.get("accessMethod") or _cfg.get("access_method") or ""
        try:
            if access_method in ("api", "api_pull"):
                config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
                interfaces = _cfg.get("interfaces")
                if not config_path and not task.data_source_id:
                    raise HTTPException(status_code=400, detail="API sync requires config_path or data_source_id")
                job_id = _enqueue_api_sync(
                    task.id, batch.id, config_path, interfaces,
                    data_source_id=task.data_source_id,
                )
            else:
                job_id = _enqueue(task.id, batch.id, task.name)
        except Exception as e:
            batch.status = "failed"
            batch.error_summary = f"enqueue failed: {e}"
            await dao.batch_update(db, batch)
            await db.commit()
            raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")
        return _ok(
            {"id": str(batch.id), "batchId": str(batch.id), "jobId": job_id, "level": level},
            msg="L1 对账已触发（重新同步）",
        )

    # L2 / L3 尚未实现
    return _ok(
        {"supported": False, "level": level, "message": "L2/L3 深度对账尚未实现"},
        msg="not supported yet",
    )


@task_router.post("/reconciliations/{recon_id}/repair")
async def repair_reconciliation(
    recon_id: uuid.UUID,
    body: RepairRequest | None = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """修复不一致段（L2/L3 分段修复，尚未实现）。"""
    return _ok(
        {"supported": False, "reconId": str(recon_id), "message": "L2/L3 修复尚未实现"},
        msg="not supported yet",
    )


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
