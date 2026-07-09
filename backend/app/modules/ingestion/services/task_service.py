"""接入任务 CRUD 服务（async — FastAPI 层使用）。"""

import uuid
from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.ingestion.models import (
    ImportError,
    IngestionBatch,
    IngestionTask,
)
from app.modules.ingestion.schemas.ingestion_task import (
    IngestionTaskCreate,
    IngestionTaskUpdate,
)


class TaskService:
    """接入任务管理服务（async）。"""

    def __init__(self, db: AsyncSession):
        self.db = db

    # ── 任务 CRUD ─────────────────────────

    async def list_tasks(
        self,
        keyword: str | None = None,
        status: str | None = None,
        data_source_id: uuid.UUID | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> tuple[list[IngestionTask], int]:
        """分页查询任务列表。"""
        query = select(IngestionTask)

        if keyword:
            query = query.filter(
                IngestionTask.name.ilike(f"%{keyword}%")
            )
        if status:
            query = query.filter(IngestionTask.status == status)
        if data_source_id:
            query = query.filter(IngestionTask.data_source_id == data_source_id)

        # 总数
        count_query = select(func.count()).select_from(query.subquery())
        total = (await self.db.execute(count_query)).scalar_one()

        # 分页
        query = query.order_by(IngestionTask.updated_at.desc())
        query = query.offset((page - 1) * page_size).limit(page_size)
        result = await self.db.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def get_by_id(self, task_id: uuid.UUID) -> IngestionTask | None:
        """按 ID 查询任务。"""
        return await self.db.get(IngestionTask, task_id)

    async def create(self, data: IngestionTaskCreate) -> IngestionTask:
        """创建任务。"""
        task = IngestionTask(**data.model_dump())
        self.db.add(task)
        await self.db.flush()
        return task

    async def update(
        self, task_id: uuid.UUID, data: IngestionTaskUpdate
    ) -> IngestionTask | None:
        """更新任务配置。"""
        task = await self.get_by_id(task_id)
        if not task:
            return None
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)
        await self.db.flush()
        return task

    async def delete(self, task_id: uuid.UUID) -> bool:
        """软删除任务（设为 disabled）。"""
        task = await self.get_by_id(task_id)
        if not task:
            return False
        task.status = "disabled"
        await self.db.flush()
        return True

    async def enable(self, task_id: uuid.UUID) -> IngestionTask | None:
        """启用任务。"""
        task = await self.get_by_id(task_id)
        if not task:
            return None
        task.status = "active"
        await self.db.flush()
        return task

    async def disable(self, task_id: uuid.UUID) -> IngestionTask | None:
        """停用任务。"""
        task = await self.get_by_id(task_id)
        if not task:
            return None
        task.status = "paused"
        await self.db.flush()
        return task

    # ── 批次查询 ─────────────────────────

    async def list_batches(
        self,
        task_id: uuid.UUID | None = None,
        status: str | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> tuple[list[IngestionBatch], int]:
        """分页查询批次列表。"""
        query = select(IngestionBatch)

        if task_id:
            query = query.filter(IngestionBatch.task_id == task_id)
        if status:
            query = query.filter(IngestionBatch.status == status)

        count_query = select(func.count()).select_from(query.subquery())
        total = (await self.db.execute(count_query)).scalar_one()

        query = query.order_by(IngestionBatch.created_at.desc())
        query = query.offset((page - 1) * page_size).limit(page_size)
        result = await self.db.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def get_batch_by_id(
        self, batch_id: uuid.UUID
    ) -> IngestionBatch | None:
        """按 ID 查询批次。"""
        return await self.db.get(IngestionBatch, batch_id)

    async def list_errors(
        self,
        batch_id: uuid.UUID | None = None,
        error_level: str | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> tuple[list[ImportError], int]:
        """分页查询错误清单。"""
        query = select(ImportError)

        if batch_id:
            query = query.filter(ImportError.batch_id == batch_id)
        if error_level:
            query = query.filter(ImportError.error_level == error_level)

        count_query = select(func.count()).select_from(query.subquery())
        total = (await self.db.execute(count_query)).scalar_one()

        query = query.order_by(ImportError.created_at.asc())
        query = query.offset((page - 1) * page_size).limit(page_size)
        result = await self.db.execute(query)
        items = list(result.scalars().all())

        return items, total
