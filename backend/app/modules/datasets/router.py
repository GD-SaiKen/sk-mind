"""Dataset 模块路由层。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.datasets import dao
from app.modules.datasets.models import Dataset
from app.modules.datasets.schemas import (
    DataTableListResponse,
    DataTableResponse,
    DatasetCreate,
    DatasetFieldListResponse,
    DatasetFieldResponse,
    DatasetListResponse,
    DatasetResponse,
    DatasetUpdate,
)

router = APIRouter(prefix="/datasets", tags=["datasets"])

_DUMP_OPTS = {"by_alias": True}


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


@router.get("")
async def list_datasets(
    keyword: str | None = Query(None),
    source: str | None = Query(None),
    data_layer: str | None = Query(None),
    quality: str | None = Query(None),
    category: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.dataset_list_all(
        db, keyword, source, data_layer, quality, category, page, page_size
    )
    return _ok(
        DatasetListResponse(
            items=[DatasetResponse.model_validate(i) for i in items],
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
