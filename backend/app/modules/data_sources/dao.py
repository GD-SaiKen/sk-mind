"""DataSource 模块数据访问层。"""

import uuid
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.data_sources.models import DataSource


async def list_all(
    db: AsyncSession,
    keyword: str | None = None,
    source_type: str | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[DataSource], int]:
    query = select(DataSource)
    if keyword:
        query = query.filter(DataSource.name.ilike(f"%{keyword}%"))
    if source_type:
        query = query.filter(DataSource.source_type == source_type)
    if status:
        query = query.filter(DataSource.status == status)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(DataSource.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def get_by_id(db: AsyncSession, ds_id: uuid.UUID) -> DataSource | None:
    return await db.get(DataSource, ds_id)


async def insert(db: AsyncSession, ds: DataSource) -> DataSource:
    db.add(ds)
    await db.flush()
    return ds


async def update(db: AsyncSession, ds: DataSource) -> DataSource:
    await db.flush()
    return ds
