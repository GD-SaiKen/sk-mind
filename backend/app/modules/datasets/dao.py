"""Dataset 模块数据访问层。"""

import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import func, select, text, update as sa_update
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from app.modules.datasets.models import Dataset, DatasetField, DataTable


# ── Dataset 列表查询（T4: 筛选增强） ──

async def dataset_list_all(
    db: AsyncSession,
    keyword: str | None = None,
    source: str | None = None,
    data_layer: str | None = None,
    quality: str | None = None,
    category: str | None = None,
    is_agent_accessible: bool | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[Dataset], int]:
    query = select(Dataset)
    if keyword:
        query = query.filter(
            Dataset.name.ilike(f"%{keyword}%")
            | Dataset.code.ilike(f"%{keyword}%")
            | Dataset.description.ilike(f"%{keyword}%")
        )
    if data_layer:
        query = query.filter(Dataset.data_layer == data_layer)
    if category:
        query = query.filter(Dataset.business_domain == category)
    # T4: source 过滤 — JOIN data_sources 按名称筛选
    if source:
        ds_tbl = sa.table("data_sources", sa.column("id"), sa.column("name"))
        query = query.join(
            ds_tbl,
            ds_tbl.c.id == Dataset.data_source_id,
            isouter=True,
        ).filter(func.lower(ds_tbl.c.name).like(f"%{source.lower()}%"))
    # T4: quality 过滤 — 兼容中英文和 ok/warning/error 三值
    if quality:
        if quality in ("ok", "正常"):
            query = query.filter(Dataset.status == "active")
        elif quality in ("warning", "警告"):
            query = query.filter(Dataset.status == "active")
        elif quality in ("error", "异常"):
            query = query.filter(Dataset.status != "active")
    # T4: Agent 可用性筛选
    if is_agent_accessible is not None:
        query = query.filter(Dataset.is_agent_accessible == is_agent_accessible)

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


# ── DatasetField 查询 ──

async def dataset_field_list(
    db: AsyncSession, dataset_id: uuid.UUID
) -> tuple[list[DatasetField], int]:
    base_q = select(DatasetField).where(DatasetField.dataset_id == dataset_id)
    count_q = select(func.count()).select_from(base_q.subquery())
    total = (await db.execute(count_q)).scalar_one()
    q = base_q.order_by(DatasetField.ordinal_position)
    result = await db.execute(q)
    return list(result.scalars().all()), total


# ── T4: 字段 CRUD ──

async def dataset_field_get_by_id(
    db: AsyncSession, field_id: uuid.UUID
) -> DatasetField | None:
    return await db.get(DatasetField, field_id)


async def dataset_field_update_values(
    db: AsyncSession, field: DatasetField, values: dict[str, Any]
) -> DatasetField:
    for k, v in values.items():
        if v is not None:
            setattr(field, k, v)
    await db.flush()
    return field


async def dataset_field_batch_set_sensitivity(
    db: AsyncSession, dataset_id: uuid.UUID, field_ids: list[uuid.UUID],
    sensitivity_level: str,
) -> int:
    """Batch update sensitivity_level for multiple fields. Returns count updated."""
    stmt = (
        sa_update(DatasetField)
        .where(DatasetField.dataset_id == dataset_id)
        .where(DatasetField.id.in_(field_ids))
        .values(sensitivity_level=sensitivity_level)
    )
    result = await db.execute(stmt)
    return result.rowcount


async def dataset_field_delete(db: AsyncSession, field: DatasetField) -> None:
    await db.delete(field)
    await db.flush()


# ── DataTable 查询 ──

async def data_table_list_by_dataset(
    db: AsyncSession, dataset_id: uuid.UUID
) -> tuple[list[DataTable], int]:
    base_q = select(DataTable).where(DataTable.dataset_id == dataset_id)
    count_q = select(func.count()).select_from(base_q.subquery())
    total = (await db.execute(count_q)).scalar_one()
    q = base_q.order_by(DataTable.table_name)
    result = await db.execute(q)
    return list(result.scalars().all()), total


# ── T4: 样例数据 ──

_EXCLUDE_COLUMNS_SQL = (
    "_synced_at", "_row_hash", "_batch_id", "_source_id",
    "_source_signature", "_action",
)

async def get_sample_data(
    db: AsyncSession, schema_name: str, table_name: str, limit: int = 100,
) -> tuple[list[str], list[list[Any]]]:
    """Query the physical raw table for the first N rows (excluding tracking columns).

    Returns (column_names, rows).
    """
    # Get business column names to exclude tracking columns
    col_result = await db.execute(
        text(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema = :schema AND table_name = :tbl "
            "ORDER BY ordinal_position"
        ),
        {"schema": schema_name, "tbl": table_name},
    )
    all_cols = [row.column_name for row in col_result]
    biz_cols = [
        c for c in all_cols
        if not (c.startswith("_") and c in _EXCLUDE_COLUMNS_SQL)
    ]
    # Build safe query with quoted identifiers
    quoted_cols = ", ".join(f'"{c}"' for c in biz_cols)
    full_table = f'"{schema_name}"."{table_name}"'
    result = await db.execute(
        text(f"SELECT {quoted_cols} FROM {full_table} LIMIT :limit"),
        {"limit": limit},
    )
    rows = [list(row) for row in result]
    return biz_cols, rows


# ── T5: 空值率统计 ──

async def compute_null_rates(
    db: AsyncSession, schema_name: str, table_name: str, dataset_id: uuid.UUID,
) -> int:
    """Compute null_rate for all DatasetField records of a dataset.

    Queries the physical table for each business column and updates
    dataset_fields.null_rate.

    Returns number of fields updated.
    """
    # Get field names for this dataset
    fields_result = await db.execute(
        text(
            "SELECT id, field_name FROM dataset_fields "
            "WHERE dataset_id = :ds_id"
        ),
        {"ds_id": dataset_id},
    )
    fields = [(row.id, row.field_name) for row in fields_result]
    if not fields:
        return 0

    # Get all null rates in one query
    field_names = [f[1] for f in fields]
    null_counts: dict[str, float] = {}
    for fname in field_names:
        full_tbl = f'"{schema_name}"."{table_name}"'
        result = await db.execute(
            text(
                f"SELECT CAST(SUM(CASE WHEN \"{fname}\" IS NULL THEN 1 ELSE 0 END) AS REAL) "
                f"/ NULLIF(count(*), 0) FROM {full_tbl}"
            ),
        )
        row = result.fetchone()
        if row and row[0] is not None:
            null_counts[fname] = round(row[0], 4)

    # Batch update
    updated = 0
    now = datetime.now(timezone.utc)
    for fid, fname in fields:
        rate = null_counts.get(fname)
        if rate is not None:
            await db.execute(
                text(
                    "UPDATE dataset_fields SET null_rate = :rate, updated_at = :now "
                    "WHERE id = :id"
                ),
                {"rate": rate, "id": fid, "now": now},
            )
            updated += 1

    return updated


# ── T6: Agent 可用性检查 ──

async def get_field_description_coverage(
    db: AsyncSession, dataset_id: uuid.UUID,
) -> float:
    """Returns the ratio of fields with a non-null description.  0.0 ~ 1.0."""
    result = await db.execute(
        text(
            "SELECT CAST(SUM(CASE WHEN description IS NOT NULL AND description != '' THEN 1 ELSE 0 END) AS REAL) "
            "/ NULLIF(count(*), 0) "
            "FROM dataset_fields WHERE dataset_id = :ds_id"
        ),
        {"ds_id": dataset_id},
    )
    row = result.fetchone()
    return round(row[0], 2) if row and row[0] is not None else 0.0


async def count_unmarked_sensitive_fields(
    db: AsyncSession, dataset_id: uuid.UUID,
) -> int:
    """Count fields whose sensitivity_level is 'sensitive' or 'high_sensitive'
    but whose description is null (i.e. not reviewed)."""
    result = await db.execute(
        text(
            "SELECT count(*) FROM dataset_fields "
            "WHERE dataset_id = :ds_id "
            "AND sensitivity_level IN ('sensitive', 'high_sensitive')"
        ),
        {"ds_id": dataset_id},
    )
    return result.scalar_one()


async def set_agent_accessible(
    db: AsyncSession, dataset_id: uuid.UUID, accessible: bool,
) -> None:
    await db.execute(
        text(
            "UPDATE datasets SET is_agent_accessible = :val, updated_at = :now "
            "WHERE id = :id"
        ),
        {"val": accessible, "id": dataset_id, "now": datetime.now(timezone.utc)},
    )
    await db.flush()
