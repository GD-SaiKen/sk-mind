"""Ingestion 模块数据访问层 — 纯数据库 CRUD 操作。"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.ingestion.models import (
    ImportError,
    IngestionBatch,
    IngestionTask,
)


# ═══════════════════════════════════════════
# 任务 CRUD
# ═══════════════════════════════════════════

async def task_list(
    db: AsyncSession,
    keyword: str | None = None,
    status: str | None = None,
    data_source_id: uuid.UUID | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[IngestionTask], int]:
    query = select(IngestionTask)
    if keyword:
        query = query.filter(IngestionTask.name.ilike(f"%{keyword}%"))
    if status:
        query = query.filter(IngestionTask.status == status)
    if data_source_id:
        query = query.filter(IngestionTask.data_source_id == data_source_id)

    count_query = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_query)).scalar_one()

    query = query.order_by(IngestionTask.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def task_get_by_id(db: AsyncSession, task_id: uuid.UUID) -> IngestionTask | None:
    return await db.get(IngestionTask, task_id)


async def task_insert(db: AsyncSession, task: IngestionTask) -> IngestionTask:
    db.add(task)
    await db.flush()
    return task


async def task_update(db: AsyncSession, task: IngestionTask) -> IngestionTask:
    await db.flush()
    return task


async def task_update_sync_status(
    db: AsyncSession,
    task: IngestionTask,
    status: str,
    sync_at: datetime | None = None,
) -> IngestionTask:
    """更新任务的同步追踪字段。"""
    task.last_sync_status = status
    task.last_sync_at = sync_at or datetime.now(timezone.utc)
    await db.flush()
    return task


# ═══════════════════════════════════════════
# 批次 CRUD
# ═══════════════════════════════════════════

async def batch_list(
    db: AsyncSession,
    task_id: uuid.UUID | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[IngestionBatch], int]:
    query = select(IngestionBatch)
    if task_id:
        query = query.filter(IngestionBatch.task_id == task_id)
    if status:
        query = query.filter(IngestionBatch.status == status)

    count_query = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_query)).scalar_one()

    query = query.order_by(IngestionBatch.created_at.desc(), IngestionBatch.id.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def batch_get_by_id(db: AsyncSession, batch_id: uuid.UUID) -> IngestionBatch | None:
    return await db.get(IngestionBatch, batch_id)


async def batch_insert(db: AsyncSession, batch: IngestionBatch) -> IngestionBatch:
    db.add(batch)
    await db.flush()
    return batch


async def batch_update(db: AsyncSession, batch: IngestionBatch) -> IngestionBatch:
    await db.flush()
    return batch


# ═══════════════════════════════════════════
# 错误清单
# ═══════════════════════════════════════════

async def error_list(
    db: AsyncSession,
    batch_id: uuid.UUID | None = None,
    error_level: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[ImportError], int]:
    query = select(ImportError)
    if batch_id:
        query = query.filter(ImportError.batch_id == batch_id)
    if error_level:
        query = query.filter(ImportError.error_level == error_level)

    count_query = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_query)).scalar_one()

    query = query.order_by(ImportError.created_at.asc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def error_insert(db: AsyncSession, error: ImportError) -> ImportError:
    db.add(error)
    await db.flush()
    return error
