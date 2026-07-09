"""Ingestion task API routes."""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.ingestion.models import IngestionBatch
from app.modules.ingestion.schemas.ingestion_task import (
    BatchProgressResponse,
    ImportErrorResponse,
    IngestionBatchResponse,
    IngestionTaskCreate,
    IngestionTaskResponse,
    IngestionTaskUpdate,
)
from app.modules.ingestion.services.task_service import TaskService

router = APIRouter(prefix="/ingestion-tasks", tags=["ingestion"])


def _dump(model):
    return model.model_dump(mode="json", by_alias=True)


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


def _paginated(items, total, page, page_size):
    return _ok({"items": items, "total": total, "page": page, "pageSize": page_size}, msg="OK")


@router.get("")
async def list_tasks(
    keyword: str | None = Query(None),
    status: str | None = Query(None),
    data_source_id: uuid.UUID | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(db)
    items, total = await service.list_tasks(keyword=keyword, status=status, data_source_id=data_source_id, page=page, page_size=page_size)
    return _paginated([_dump(IngestionTaskResponse.model_validate(i)) for i in items], total, page, page_size)


@router.post("", status_code=201)
async def create_task(data: IngestionTaskCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    task = await service.create(data)
    return _ok(_dump(IngestionTaskResponse.model_validate(task)), msg="task created")


@router.get("/{task_id}")
async def get_task(task_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    task = await service.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    return _ok(_dump(IngestionTaskResponse.model_validate(task)))


@router.put("/{task_id}")
async def update_task(task_id: uuid.UUID, data: IngestionTaskUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    task = await service.update(task_id, data)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    return _ok(_dump(IngestionTaskResponse.model_validate(task)), msg="task updated")


@router.delete("/{task_id}")
async def delete_task(task_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    if not await service.delete(task_id):
        raise HTTPException(status_code=404, detail="not found")
    return _ok(msg="task disabled")


@router.post("/{task_id}/enable")
async def enable_task(task_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    if not await service.enable(task_id):
        raise HTTPException(status_code=404, detail="not found")
    return _ok(msg="task enabled")


@router.post("/{task_id}/disable")
async def disable_task(task_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    if not await service.disable(task_id):
        raise HTTPException(status_code=404, detail="not found")
    return _ok(msg="task disabled")


@router.get("/{task_id}/batches")
async def list_batches(task_id: uuid.UUID, status: str | None = Query(None), page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    items, total = await service.list_batches(task_id=task_id, status=status, page=page, page_size=page_size)
    return _paginated([_dump(IngestionBatchResponse.model_validate(i)) for i in items], total, page, page_size)


@router.get("/batches/{batch_id}")
async def get_batch(batch_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    batch = await service.get_batch_by_id(batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="not found")
    return _ok(_dump(IngestionBatchResponse.model_validate(batch)))


@router.get("/batches/{batch_id}/progress")
async def get_batch_progress(batch_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    batch = await service.get_batch_by_id(batch_id)
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
    return _ok(_dump(BatchProgressResponse(batchId=str(batch.id), status=batch.status, progress=progress, step=step, lastHeartbeat=batch.started_at)))


@router.get("/batches/{batch_id}/errors")
async def list_batch_errors(batch_id: uuid.UUID, error_level: str | None = Query(None), page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    items, total = await service.list_errors(batch_id=batch_id, error_level=error_level, page=page, page_size=page_size)
    return _paginated([_dump(ImportErrorResponse.model_validate(i)) for i in items], total, page, page_size)


@router.post("/{task_id}/execute")
async def execute_task(task_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    task = await service.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="not found")
    if task.status == "disabled":
        raise HTTPException(status_code=400, detail="task disabled")

    batch = IngestionBatch(task_id=task.id, trigger_type="manual", status="pending", triggered_by=str(current_user.id))
    db.add(batch)
    await db.flush()

    try:
        from app.core.queue import redis_conn
        from rq import Queue
        queue = Queue("ingestion", connection=redis_conn)
        job = queue.enqueue("app.modules.ingestion.tasks.sync_tasks.run_echo_sync", str(task.id), str(batch.id), task.name, job_timeout=60)
        batch.status = "running"
        batch.started_at = datetime.now(timezone.utc)
        await db.flush()
        return _ok({"batchId": str(batch.id), "jobId": job.id}, msg="task submitted")
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await db.flush()
        raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")


@router.post("/batches/{batch_id}/retry")
async def retry_batch(batch_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = TaskService(db)
    old = await service.get_batch_by_id(batch_id)
    if not old:
        raise HTTPException(status_code=404, detail="not found")
    task = await service.get_by_id(old.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    batch = IngestionBatch(task_id=task.id, trigger_type="retry", status="pending", triggered_by=str(current_user.id))
    db.add(batch)
    await db.flush()

    try:
        from app.core.queue import redis_conn
        from rq import Queue
        queue = Queue("ingestion", connection=redis_conn)
        job = queue.enqueue("app.modules.ingestion.tasks.sync_tasks.run_echo_sync", str(task.id), str(batch.id), f"{task.name} (retry)", job_timeout=60)
        batch.status = "running"
        batch.started_at = datetime.now(timezone.utc)
        await db.flush()
        return _ok({"batchId": str(batch.id), "jobId": job.id, "retryFrom": str(batch_id)}, msg="retry submitted")
    except Exception as e:
        batch.status = "failed"
        batch.error_summary = f"enqueue failed: {e}"
        await db.flush()
        raise HTTPException(status_code=500, detail=f"RQ enqueue failed: {e}")
