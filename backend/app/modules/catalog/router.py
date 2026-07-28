"""Catalog 模块路由层 — 数据目录（业务视角）。

所有查询基于 datasets + dataset_fields + data_sources JOIN，
不建独立表。
"""

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.catalog import dao, service
from app.modules.catalog.schemas import (
    CatalogDatasetItem,
    CatalogDatasetListResponse,
    CatalogFieldItem,
    CatalogFieldListResponse,
    CatalogStatsResponse,
)

router = APIRouter(prefix="/catalog", tags=["catalog"])

_DUMP_OPTS = {"by_alias": True, "exclude_none": False}


# ── 数据集目录列表 ──

@router.get("/datasets")
async def list_datasets(
    keyword: str | None = Query(None, description="搜索名称/描述"),
    source: str | None = Query(None, description="来源系统名称"),
    domain: str | None = Query(None, description="业务域"),
    is_agent_accessible: bool | None = Query(None, alias="isAgentAccessible"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.catalog_list_datasets(
        db,
        keyword=keyword,
        source=source,
        domain=domain,
        is_agent_accessible=is_agent_accessible,
        page=page,
        page_size=page_size,
    )
    resp_items = [CatalogDatasetItem(**item) for item in items]
    return {
        "code": 0,
        "data": CatalogDatasetListResponse(
            items=resp_items, total=total, page=page, page_size=page_size,
        ).model_dump(**_DUMP_OPTS),
    }


# ── 字段目录（跨数据集搜索）──

@router.get("/fields")
async def search_fields(
    keyword: str | None = Query(None),
    dataset_id: str | None = Query(None, alias="datasetId"),
    data_type: str | None = Query(None, alias="dataType"),
    is_sensitive: bool | None = Query(None, alias="isSensitive"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.catalog_search_fields(
        db,
        keyword=keyword,
        dataset_id=dataset_id,
        data_type=data_type,
        is_sensitive=is_sensitive,
        page=page,
        page_size=page_size,
    )
    resp_items = [CatalogFieldItem(**item) for item in items]
    return {
        "code": 0,
        "data": CatalogFieldListResponse(
            items=resp_items, total=total, page=page, page_size=page_size,
        ).model_dump(**_DUMP_OPTS),
    }


# ── 统计 ──

@router.get("/stats")
async def get_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stats = await dao.catalog_get_stats(db)
    return {
        "code": 0,
        "data": CatalogStatsResponse(**stats).model_dump(**_DUMP_OPTS),
    }


# ── 数据集详情（业务视角）──

@router.get("/datasets/{ds_id}")
async def get_dataset_detail(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    detail = await service.get_dataset_detail(db, ds_id)
    if not detail:
        return {"code": 404, "message": "dataset not found"}
    return {"code": 0, "data": detail}
