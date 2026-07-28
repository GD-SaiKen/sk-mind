"""Catalog 模块服务层 — 组装聚合查询结果。"""

import uuid
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.catalog import dao
from app.modules.catalog.schemas import CatalogDatasetDetail, CatalogFieldItem
from app.modules.datasets.models import Dataset, DatasetField
from app.modules.data_sources.models import DataSource
import sqlalchemy as sa


async def get_dataset_detail(
    db: AsyncSession,
    ds_id: uuid.UUID,
) -> Optional[dict]:
    """组装数据集业务详情。

    与 datasets 模块 detail 的区别：
    - 不展示样例数据、空值率等技术信息
    - 增加：Agent 使用限制、敏感字段列表、来源信息
    """
    ds = await db.get(Dataset, ds_id)
    if not ds:
        return None

    # Source name
    source_name: Optional[str] = None
    if ds.data_source_id:
        src = await db.get(DataSource, ds.data_source_id)
        source_name = src.name if src else None

    # Fields — 业务视角
    fields_result = await db.execute(
        sa.select(DatasetField)
        .where(DatasetField.dataset_id == ds_id)
        .order_by(DatasetField.ordinal_position)
    )
    field_rows = fields_result.scalars().all()

    field_items = []
    for f in field_rows:
        item = CatalogFieldItem(
            id=f.id,
            field_name=f.field_name,
            field_alias=f.field_alias,
            description=f.description,
            data_type=f.data_type,
            is_primary_key=f.is_primary_key,
            is_sensitive=f.sensitivity_level in ("sensitive", "high_sensitive"),
            sensitivity_level=f.sensitivity_level,
            null_rate=f.null_rate,
            dataset_name=ds.name,
            dataset_id=ds.id,
        )
        field_items.append(item)

    detail = CatalogDatasetDetail(
        id=ds.id,
        name=ds.name,
        display_name=ds.name,
        code=ds.code,
        description=ds.description,
        source_name=source_name,
        data_layer=ds.data_layer,
        business_domain=ds.business_domain,
        updated_at=ds.updated_at,
        quality_status="ok" if ds.status == "active" else ("error" if ds.status == "archived" else "warning"),
        permission_level=ds.sensitivity_level,
        is_agent_accessible=ds.is_agent_accessible,
        agent_accessible_reason=ds.agent_unavailable_reason,
        record_count=ds.record_count,
        field_count=ds.field_count,
        fields=field_items,
        sensitive_fields=[f for f in field_items if f.is_sensitive],
    )
    return detail.model_dump(by_alias=True)
