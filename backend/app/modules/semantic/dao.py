"""语义模型数据访问层。"""

import uuid
from typing import Any

import sqlalchemy as sa
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.semantic.models import SemanticObject, SemanticProperty, DataMapping
from app.modules.datasets.models import Dataset, DatasetField


# ═══════════════════════════════════════════════════════
# SemanticObject
# ═══════════════════════════════════════════════════════

async def semantic_object_list(
    db: AsyncSession,
    *,
    keyword: str | None = None,
    object_type: str | None = None,
    domain: str | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[SemanticObject], int]:
    query = select(SemanticObject)
    if keyword:
        query = query.filter(
            SemanticObject.name.ilike(f"%{keyword}%")
            | SemanticObject.code.ilike(f"%{keyword}%")
            | SemanticObject.description.ilike(f"%{keyword}%")
        )
    if object_type:
        query = query.filter(SemanticObject.object_type == object_type)
    if domain:
        query = query.filter(SemanticObject.domain == domain)
    if status:
        query = query.filter(SemanticObject.status == status)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(SemanticObject.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def semantic_object_get_by_id(
    db: AsyncSession, object_id: uuid.UUID,
) -> SemanticObject | None:
    return await db.get(SemanticObject, object_id)


async def semantic_object_get_by_code(
    db: AsyncSession, code: str,
) -> SemanticObject | None:
    result = await db.execute(
        select(SemanticObject).where(SemanticObject.code == code)
    )
    return result.scalar_one_or_none()


async def semantic_object_insert(db: AsyncSession, obj: SemanticObject) -> SemanticObject:
    db.add(obj)
    await db.flush()
    return obj


async def semantic_object_update(db: AsyncSession, obj: SemanticObject) -> SemanticObject:
    await db.flush()
    return obj


# ═══════════════════════════════════════════════════════
# SemanticProperty
# ═══════════════════════════════════════════════════════

async def semantic_property_list(
    db: AsyncSession,
    *,
    semantic_object_id: uuid.UUID | None = None,
    property_type: str | None = None,
    page: int | None = None,
    page_size: int | None = None,
) -> tuple[list[dict], int]:
    """Return properties as list[dict] with object_name and has_mapping resolved."""
    sp = SemanticProperty
    # Build query with JOIN to semantic_objects
    query = (
        select(
            sp.id,
            sp.semantic_object_id,
            sp.name,
            sp.code,
            sp.description,
            sp.property_type,
            sp.data_type,
            sp.is_required,
            sp.is_sensitive,
            sp.ordinal_position,
            sp.status,
            sp.created_at,
            sp.updated_at,
            SemanticObject.name.label("_object_name"),
        )
        .select_from(sp)
        .join(SemanticObject, SemanticObject.id == sp.semantic_object_id, isouter=False)
    )
    if semantic_object_id:
        query = query.filter(sp.semantic_object_id == semantic_object_id)
    if property_type:
        query = query.filter(sp.property_type == property_type)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(sp.ordinal_position, sp.name)
    if page is not None and page_size is not None:
        query = query.offset((page - 1) * page_size).limit(page_size)

    result = await db.execute(query)
    rows = result.all()

    # Collect property IDs to check for mappings
    prop_ids = [row[0] for row in rows]
    mapping_check: set[uuid.UUID] = set()
    if prop_ids:
        map_result = await db.execute(
            select(DataMapping.semantic_property_id).where(
                DataMapping.semantic_property_id.in_(prop_ids)
            )
        )
        mapping_check = {r[0] for r in map_result if r[0]}

    items = []
    for row in rows:
        prop_id = row[0]
        items.append({
            "id": prop_id,
            "semantic_object_id": row[1],
            "name": row[2],
            "code": row[3],
            "description": row[4],
            "property_type": row[5],
            "data_type": row[6],
            "is_required": bool(row[7]),
            "is_sensitive": bool(row[8]),
            "ordinal_position": row[9],
            "status": row[10],
            "created_at": row[11],
            "updated_at": row[12],
            "object_name": row[13],
            "has_mapping": prop_id in mapping_check,
        })
    return items, total


async def semantic_property_get_by_id(
    db: AsyncSession, prop_id: uuid.UUID,
) -> SemanticProperty | None:
    return await db.get(SemanticProperty, prop_id)


async def semantic_property_insert(db: AsyncSession, prop: SemanticProperty) -> SemanticProperty:
    db.add(prop)
    await db.flush()
    return prop


async def semantic_property_update_values(
    db: AsyncSession, prop: SemanticProperty, values: dict[str, Any],
) -> SemanticProperty:
    for k, v in values.items():
        if v is not None:
            setattr(prop, k, v)
    await db.flush()
    return prop


async def semantic_property_delete(db: AsyncSession, prop: SemanticProperty) -> None:
    await db.delete(prop)
    await db.flush()


# ═══════════════════════════════════════════════════════
# DataMapping
# ═══════════════════════════════════════════════════════

async def data_mapping_list(
    db: AsyncSession,
    *,
    mapping_type: str | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[dict], int]:
    """Return mappings as list[dict] with target_name resolved from datasets/dataset_fields."""
    dm = DataMapping
    select_cols = [
        dm.id, dm.mapping_type, dm.semantic_object_id, dm.semantic_property_id,
        dm.semantic_relation_id, dm.target_type, dm.target_id,
        dm.transform_rule, dm.confidence, dm.status,
        dm.created_by, dm.confirmed_by, dm.created_at, dm.updated_at,
    ]
    query = select(*select_cols)
    if mapping_type:
        query = query.filter(dm.mapping_type == mapping_type)
    if status:
        query = query.filter(dm.status == status)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(dm.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    rows = result.all()

    # Collect object/property IDs for name resolution
    obj_ids = {r[2] for r in rows if r[2]}
    prop_ids = {r[3] for r in rows if r[3]}

    obj_names: dict[uuid.UUID, str] = {}
    if obj_ids:
        obj_result = await db.execute(
            select(SemanticObject.id, SemanticObject.name).where(
                SemanticObject.id.in_(obj_ids)
            )
        )
        obj_names = {row[0]: row[1] for row in obj_result}

    prop_names: dict[uuid.UUID, str] = {}
    if prop_ids:
        prop_result = await db.execute(
            select(SemanticProperty.id, SemanticProperty.name).where(
                SemanticProperty.id.in_(prop_ids)
            )
        )
        prop_names = {row[0]: row[1] for row in prop_result}

    # Resolve target_name from datasets / dataset_fields
    dataset_ids = {r[6] for r in rows if r[4] == "dataset"}
    field_ids = {r[6] for r in rows if r[4] == "dataset_field"}

    dataset_names: dict[uuid.UUID, str] = {}
    if dataset_ids:
        ds_result = await db.execute(
            select(Dataset.id, Dataset.name).where(Dataset.id.in_(dataset_ids))
        )
        dataset_names = {row[0]: row[1] for row in ds_result}

    field_info: dict[uuid.UUID, dict] = {}
    if field_ids:
        f_result = await db.execute(
            select(DatasetField.id, DatasetField.field_name, DatasetField.dataset_id)
            .where(DatasetField.id.in_(field_ids))
        )
        for row in f_result:
            field_info[row[0]] = {"field_name": row[1], "dataset_id": row[2]}

    # Resolve dataset names for fields
    field_dataset_ids = {v["dataset_id"] for v in field_info.values() if v.get("dataset_id")}
    field_dataset_names: dict[uuid.UUID, str] = {}
    if field_dataset_ids:
        fds_result = await db.execute(
            select(Dataset.id, Dataset.name).where(Dataset.id.in_(field_dataset_ids))
        )
        field_dataset_names = {row[0]: row[1] for row in fds_result}

    items: list[dict] = []
    for row in rows:
        ttype = row[5]   # target_type is index 5
        tid = row[6]     # target_id is index 6
        target_name = None
        target_table = None
        if ttype == "dataset":
            target_name = dataset_names.get(tid)
        elif ttype == "dataset_field":
            fi = field_info.get(tid, {})
            target_name = fi.get("field_name")
            if fi.get("dataset_id"):
                target_table = field_dataset_names.get(fi["dataset_id"])

        items.append({
            "id": row[0],
            "mapping_type": row[1],
            "semantic_object_id": row[2],
            "semantic_property_id": row[3],
            "semantic_relation_id": row[4],
            "target_type": row[5],
            "target_id": row[6],
            "transform_rule": row[7],
            "confidence": row[8],
            "status": row[9],
            "created_by": row[10],
            "confirmed_by": row[11],
            "created_at": row[12],
            "updated_at": row[13],
            "semantic_object_name": obj_names.get(row[2]),
            "semantic_property_name": prop_names.get(row[3]),
            "target_name": target_name,
            "target_table": target_table,
        })
    return items, total


async def data_mapping_get_by_id(
    db: AsyncSession, mapping_id: uuid.UUID,
) -> DataMapping | None:
    return await db.get(DataMapping, mapping_id)


async def data_mapping_insert(db: AsyncSession, mapping: DataMapping) -> DataMapping:
    db.add(mapping)
    await db.flush()
    return mapping


async def data_mapping_update_values(
    db: AsyncSession, mapping: DataMapping, values: dict[str, Any],
) -> DataMapping:
    for k, v in values.items():
        if v is not None:
            setattr(mapping, k, v)
    await db.flush()
    return mapping


async def data_mapping_delete(db: AsyncSession, mapping: DataMapping) -> None:
    await db.delete(mapping)
    await db.flush()


# ═══════════════════════════════════════════════════════
# Stats
# ═══════════════════════════════════════════════════════

async def semantic_get_stats(db: AsyncSession) -> dict:
    # Total objects
    total_objects = (await db.execute(
        select(func.count()).select_from(SemanticObject)
    )).scalar_one()

    # Active objects
    active_objects = (await db.execute(
        select(func.count()).select_from(SemanticObject).where(
            SemanticObject.status == "active"
        )
    )).scalar_one()

    # Total properties
    total_properties = (await db.execute(
        select(func.count()).select_from(SemanticProperty)
    )).scalar_one()

    # Total mappings
    total_mappings = (await db.execute(
        select(func.count()).select_from(DataMapping)
    )).scalar_one()

    # Confirmed mappings
    confirmed_mappings = (await db.execute(
        select(func.count()).select_from(DataMapping).where(
            DataMapping.status == "confirmed"
        )
    )).scalar_one()

    # Group by object_type
    type_result = await db.execute(
        select(
            SemanticObject.object_type,
            func.count(SemanticObject.id),
        ).group_by(SemanticObject.object_type)
    )
    by_object_type = [{"type": row[0], "count": row[1]} for row in type_result]

    # Group by status
    status_result = await db.execute(
        select(
            SemanticObject.status,
            func.count(SemanticObject.id),
        ).group_by(SemanticObject.status)
    )
    by_status = [{"status": row[0], "count": row[1]} for row in status_result]

    return {
        "total_objects": total_objects,
        "active_objects": active_objects,
        "total_properties": total_properties,
        "total_mappings": total_mappings,
        "confirmed_mappings": confirmed_mappings,
        "by_object_type": by_object_type,
        "by_status": by_status,
    }
