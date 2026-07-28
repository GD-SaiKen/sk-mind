"""Catalog 模块数据访问层。

全部查询基于已有 datasets / dataset_fields / data_sources 表，
不建独立表，纯 JOIN 聚合。
"""

from typing import Optional

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.datasets.models import Dataset, DatasetField
from app.modules.data_sources.models import DataSource


# ── 数据集目录列表 ──

async def catalog_list_datasets(
    db: AsyncSession,
    *,
    keyword: Optional[str] = None,
    source: Optional[str] = None,
    domain: Optional[str] = None,
    is_agent_accessible: Optional[bool] = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[dict], int]:
    """数据集目录 — 业务视角 JOIN 查询。"""
    query = (
        sa.select(
            Dataset.id,
            Dataset.name,
            Dataset.code,
            Dataset.description,
            Dataset.data_layer,
            Dataset.business_domain,
            Dataset.updated_at,
            sa.case(
                (Dataset.status == "active", "ok"),
                (Dataset.status == "archived", "error"),
                else_="warning",
            ).label("quality_status"),
            Dataset.sensitivity_level.label("permission_level"),
            Dataset.is_agent_accessible,
            Dataset.record_count,
            Dataset.field_count,
            DataSource.name.label("source_name"),
        )
        .outerjoin(DataSource, Dataset.data_source_id == DataSource.id)
        .where(Dataset.status != "archived")
    )

    if keyword:
        query = query.where(
            Dataset.name.ilike(f"%{keyword}%")
            | Dataset.code.ilike(f"%{keyword}%")
            | Dataset.description.ilike(f"%{keyword}%")
        )
    if source:
        query = query.where(DataSource.name.ilike(f"%{source}%"))
    if domain:
        query = query.where(Dataset.business_domain == domain)
    if is_agent_accessible is not None:
        query = query.where(Dataset.is_agent_accessible == is_agent_accessible)

    # Count
    count_q = sa.select(sa.func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(Dataset.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)

    items = [dict(row._mapping) for row in result]
    return items, total


# ── 字段目录（跨数据集搜索）──

async def catalog_search_fields(
    db: AsyncSession,
    *,
    keyword: Optional[str] = None,
    dataset_id: Optional[str] = None,
    data_type: Optional[str] = None,
    is_sensitive: Optional[bool] = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[dict], int]:
    """字段目录 — 跨数据集搜索字段名/别名/描述。"""
    query = (
        sa.select(
            DatasetField.id,
            DatasetField.field_name,
            DatasetField.field_alias,
            DatasetField.description,
            DatasetField.data_type,
            DatasetField.is_primary_key,
            sa.case(
                (DatasetField.sensitivity_level.in_(["sensitive", "high_sensitive"]), True),
                else_=False,
            ).label("is_sensitive"),
            DatasetField.sensitivity_level,
            DatasetField.null_rate,
            Dataset.name.label("dataset_name"),
            Dataset.id.label("dataset_id"),
        )
        .join(Dataset, DatasetField.dataset_id == Dataset.id)
        .where(Dataset.status == "active")
    )

    if keyword:
        query = query.where(
            DatasetField.field_name.ilike(f"%{keyword}%")
            | DatasetField.field_alias.ilike(f"%{keyword}%")
            | DatasetField.description.ilike(f"%{keyword}%")
        )
    if dataset_id:
        query = query.where(DatasetField.dataset_id == dataset_id)
    if data_type:
        query = query.where(DatasetField.data_type == data_type)
    if is_sensitive is not None:
        if is_sensitive:
            query = query.where(
                DatasetField.sensitivity_level.in_(["sensitive", "high_sensitive"])
            )
        else:
            query = query.where(
                DatasetField.sensitivity_level.notin_(["sensitive", "high_sensitive"])
            )

    count_q = sa.select(sa.func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(DatasetField.ordinal_position)
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)

    items = [dict(row._mapping) for row in result]
    return items, total


# ── 统计 ──

async def catalog_get_stats(db: AsyncSession) -> dict:
    """数据目录首页统计卡片。"""
    base = sa.select(Dataset).where(Dataset.status == "active")

    total = (await db.execute(
        sa.select(sa.func.count()).select_from(base.subquery())
    )).scalar_one()

    quality_ok = (await db.execute(
        sa.select(sa.func.count()).select_from(
            sa.select(Dataset).where(Dataset.status == "active").subquery()
        )
    )).scalar_one()

    agent_accessible = (await db.execute(
        sa.select(sa.func.count()).select_from(
            sa.select(Dataset).where(
                Dataset.status == "active", Dataset.is_agent_accessible == True
            ).subquery()
        )
    )).scalar_one()

    # By domain
    domain_rows = await db.execute(
        sa.select(
            Dataset.business_domain,
            sa.func.count().label("cnt"),
        )
        .where(Dataset.status == "active", Dataset.business_domain.isnot(None))
        .group_by(Dataset.business_domain)
        .order_by(sa.func.count().desc())
    )
    by_domain = [{"domain": row.business_domain, "count": row.cnt} for row in domain_rows]

    return {
        "total": total,
        "quality_ok": quality_ok,
        "quality_warning": 0,  # placeholder until quality module is fully integrated
        "agent_accessible": agent_accessible,
        "by_domain": by_domain,
    }
