"""Dataset 模块数据访问层。"""

import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.datasets.models import Dataset, DatasetField, DataTable


async def dataset_list_all(
    db: AsyncSession,
    keyword: str | None = None,
    source: str | None = None,
    data_layer: str | None = None,
    quality: str | None = None,
    category: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[Dataset], int]:
    query = select(Dataset)
    if keyword:
        query = query.filter(
            Dataset.name.ilike(f"%{keyword}%") | Dataset.code.ilike(f"%{keyword}%")
        )
    if data_layer:
        query = query.filter(Dataset.data_layer == data_layer)
    if category:
        query = query.filter(Dataset.business_domain == category)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(Dataset.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def dataset_get_by_id(db: AsyncSession, ds_id: uuid.UUID) -> Dataset | None:
    return await db.get(Dataset, ds_id)


async def dataset_insert(db: AsyncSession, ds: Dataset) -> Dataset:
    db.add(ds)
    await db.flush()
    return ds


async def dataset_update(db: AsyncSession, ds: Dataset) -> Dataset:
    await db.flush()
    return ds


async def dataset_field_list(
    db: AsyncSession, dataset_id: uuid.UUID
) -> tuple[list[DatasetField], int]:
    base_q = select(DatasetField).where(DatasetField.dataset_id == dataset_id)
    count_q = select(func.count()).select_from(base_q.subquery())
    total = (await db.execute(count_q)).scalar_one()
    q = base_q.order_by(DatasetField.ordinal_position)
    result = await db.execute(q)
    return list(result.scalars().all()), total


async def data_table_list_by_dataset(
    db: AsyncSession, dataset_id: uuid.UUID
) -> tuple[list[DataTable], int]:
    base_q = select(DataTable).where(DataTable.dataset_id == dataset_id)
    count_q = select(func.count()).select_from(base_q.subquery())
    total = (await db.execute(count_q)).scalar_one()
    q = base_q.order_by(DataTable.table_name)
    result = await db.execute(q)
    return list(result.scalars().all()), total
