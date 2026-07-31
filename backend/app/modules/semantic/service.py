"""语义模型服务层 — 业务编排。

Phase 1 中 service 层较薄，主要用于为后续业务逻辑
（如自动锚定、批量映射）预留扩展点。
"""

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.datasets.models import Dataset, DatasetField


async def resolve_target_name(
    db: AsyncSession,
    target_type: str,
    target_id: uuid.UUID,
) -> str | None:
    """Resolve the display name for a mapping target_id."""
    if target_type == "dataset":
        ds = await db.get(Dataset, target_id)
        return ds.name if ds else None
    elif target_type == "dataset_field":
        field = await db.get(DatasetField, target_id)
        return field.field_name if field else None
    return None
