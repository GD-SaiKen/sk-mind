"""Dataset 模块路由层。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.datasets import dao
from app.modules.datasets import service
from app.modules.datasets.models import Dataset
from app.modules.datasets.schemas import (
    AgentCheckResponse,
    DataTableListResponse,
    DataTableResponse,
    DatasetCreate,
    DatasetFieldBatchUpdate,
    DatasetFieldListResponse,
    DatasetFieldResponse,
    DatasetFieldUpdate,
    DatasetListResponse,
    DatasetResponse,
    DatasetUpdate,
    NullRateResult,
)

router = APIRouter(prefix="/datasets", tags=["datasets"])

_DUMP_OPTS = {"by_alias": True}


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


# ═══════════════════════════════════════
# Dataset CRUD
# ═══════════════════════════════════════

@router.get("")
async def list_datasets(
    keyword: str | None = Query(None),
    source: str | None = Query(None),
    data_layer: str | None = Query(None),
    quality: str | None = Query(None),
    category: str | None = Query(None),
    is_agent_accessible: bool | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.dataset_list_all(
        db, keyword, source, data_layer, quality, category,
        is_agent_accessible, page, page_size,
    )

    # ── Enrich: source_name + quality_status ──
    ds_ids = [i.data_source_id for i in items if i.data_source_id]
    source_names: dict[uuid.UUID, str] = {}
    if ds_ids:
        _ds_rows = await db.execute(
            select(text("id, name")).select_from(text("data_sources")).where(
                text("id = ANY(:ids)")
            ),
            {"ids": ds_ids},
        )
        source_names = {row[0]: row[1] for row in _ds_rows}

    response_items = []
    for ds in items:
        d = DatasetResponse.model_validate(ds)
        if ds.data_source_id:
            d.source_name = source_names.get(ds.data_source_id)
        d.quality_status = "ok" if ds.status == "active" else ("error" if ds.status == "archived" else "warning")
        response_items.append(d)

    return _ok(
        DatasetListResponse(
            items=response_items,
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("", status_code=201)
async def create_dataset(
    data: DatasetCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = Dataset(**data.model_dump())
    ds = await dao.dataset_insert(db, ds)
    return _ok(
        DatasetResponse.model_validate(ds).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.get("/{ds_id}")
async def get_dataset(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.dataset_get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据集不存在")
    return _ok(DatasetResponse.model_validate(ds).model_dump(**_DUMP_OPTS))


@router.put("/{ds_id}")
async def update_dataset(
    ds_id: uuid.UUID,
    data: DatasetUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.dataset_get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据集不存在")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(ds, k, v)
    ds = await dao.dataset_update(db, ds)
    return _ok(
        DatasetResponse.model_validate(ds).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.delete("/{ds_id}")
async def delete_dataset(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.dataset_get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据集不存在")
    ds.status = "archived"
    await dao.dataset_update(db, ds)
    return _ok(msg="已归档")


# ═══════════════════════════════════════
# DatasetField CRUD (T4)
# ═══════════════════════════════════════

@router.get("/{ds_id}/fields")
async def get_dataset_fields(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.dataset_field_list(db, ds_id)
    return _ok(
        DatasetFieldListResponse(
            items=[DatasetFieldResponse.model_validate(i) for i in items],
            total=total,
        ).model_dump(**_DUMP_OPTS)
    )


@router.put("/{ds_id}/fields/{field_id}")
async def update_field(
    ds_id: uuid.UUID,
    field_id: uuid.UUID,
    data: DatasetFieldUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    field = await dao.dataset_field_get_by_id(db, field_id)
    if not field or field.dataset_id != ds_id:
        raise HTTPException(status_code=404, detail="字段不存在")
    field = await dao.dataset_field_update_values(
        db, field, data.model_dump(exclude_unset=True),
    )
    return _ok(
        DatasetFieldResponse.model_validate(field).model_dump(**_DUMP_OPTS),
        msg="字段更新成功",
    )


@router.put("/{ds_id}/fields/batch")
async def batch_update_fields(
    ds_id: uuid.UUID,
    data: DatasetFieldBatchUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """批量更新字段，目前支持批量修改 sensitivity_level。"""
    if not data.field_ids:
        raise HTTPException(status_code=400, detail="field_ids 不能为空")
    updated = await dao.dataset_field_batch_set_sensitivity(
        db, ds_id, data.field_ids, data.sensitivity_level,
    )
    return _ok({"updated": updated}, msg="批量更新成功")


@router.delete("/{ds_id}/fields/{field_id}")
async def delete_field(
    ds_id: uuid.UUID,
    field_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    field = await dao.dataset_field_get_by_id(db, field_id)
    if not field or field.dataset_id != ds_id:
        raise HTTPException(status_code=404, detail="字段不存在")
    await dao.dataset_field_delete(db, field)
    return _ok(msg="字段已删除")


# ═══════════════════════════════════════
# DataTable
# ═══════════════════════════════════════

@router.get("/{ds_id}/tables")
async def get_dataset_tables(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.data_table_list_by_dataset(db, ds_id)
    return _ok(
        DataTableListResponse(
            items=[DataTableResponse.model_validate(i) for i in items],
            total=total,
        ).model_dump(**_DUMP_OPTS)
    )


# ═══════════════════════════════════════
# Sample Data (T4)
# ═══════════════════════════════════════

@router.get("/{ds_id}/sample-data")
async def get_sample_data(
    ds_id: uuid.UUID,
    limit: int = Query(100, ge=1, le=500),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.dataset_get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据集不存在")
    tables, _ = await dao.data_table_list_by_dataset(db, ds_id)
    if not tables:
        return _ok({"columns": [], "rows": [], "total": 0}, msg="无关联物理表")
    dt = tables[0]
    columns, rows = await dao.get_sample_data(
        db, dt.schema_name, dt.table_name, limit,
    )
    return _ok({"columns": columns, "rows": rows, "total": len(rows)})


# ═══════════════════════════════════════
# Null Rate (T5)
# ═══════════════════════════════════════

@router.post("/{ds_id}/compute-null-rates")
async def compute_null_rates(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.dataset_get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据集不存在")
    updated = await service.compute_null_rates_for_dataset(db, ds)
    return _ok({"updated": updated}, msg="空值率计算完成")


# ═══════════════════════════════════════
# Agent Check (T6)
# ═══════════════════════════════════════

@router.post("/{ds_id}/check-agent")
async def check_agent_availability(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.dataset_get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据集不存在")
    result = await service.check_agent_availability(db, ds)
    return _ok(AgentCheckResponse(**result).model_dump(**_DUMP_OPTS))
