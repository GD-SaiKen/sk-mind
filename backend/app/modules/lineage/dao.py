"""Lineage 模块数据访问层。"""

import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.lineage.models import DataLineage


async def edge_list_all(
    db: AsyncSession,
    keyword: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[DataLineage], int]:
    query = select(DataLineage)
    if keyword:
        query = query.filter(
            DataLineage.source_name.ilike(f"%{keyword}%")
            | DataLineage.target_name.ilike(f"%{keyword}%")
            | DataLineage.description.ilike(f"%{keyword}%")
        )

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(DataLineage.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def edge_get_by_id(db: AsyncSession, edge_id: uuid.UUID) -> DataLineage | None:
    return await db.get(DataLineage, edge_id)


async def edge_insert(db: AsyncSession, edge: DataLineage) -> DataLineage:
    db.add(edge)
    await db.flush()
    return edge


async def edge_update(db: AsyncSession, edge: DataLineage) -> DataLineage:
    await db.flush()
    return edge
