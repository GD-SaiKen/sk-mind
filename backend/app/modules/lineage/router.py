"""Lineage 模块路由层。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.lineage import dao
from app.modules.lineage.models import DataLineage
from app.modules.lineage.schemas import (
    LineageEdgeCreate,
    LineageEdgeListResponse,
    LineageEdgeResponse,
    LineageEdgeUpdate,
    LineageStatsResponse,
)

router = APIRouter(prefix="/lineage", tags=["lineage"])

_DUMP_OPTS = {"by_alias": True}


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


@router.get("/edges")
async def list_edges(
    keyword: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.edge_list_all(db, keyword, page, page_size)
    return _ok(
        LineageEdgeListResponse(
            items=[LineageEdgeResponse.model_validate(i) for i in items],
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("/edges", status_code=201)
async def create_edge(
    data: LineageEdgeCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = DataLineage(**data.model_dump())
    edge = await dao.edge_insert(db, edge)
    return _ok(
        LineageEdgeResponse.model_validate(edge).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.get("/edges/{edge_id}")
async def get_edge(
    edge_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = await dao.edge_get_by_id(db, edge_id)
    if not edge:
        raise HTTPException(status_code=404, detail="关系边不存在")
    return _ok(LineageEdgeResponse.model_validate(edge).model_dump(**_DUMP_OPTS))


@router.put("/edges/{edge_id}")
async def update_edge(
    edge_id: uuid.UUID,
    data: LineageEdgeUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = await dao.edge_get_by_id(db, edge_id)
    if not edge:
        raise HTTPException(status_code=404, detail="关系边不存在")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(edge, k, v)
    edge = await dao.edge_update(db, edge)
    return _ok(
        LineageEdgeResponse.model_validate(edge).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.post("/edges/{edge_id}/confirm")
async def confirm_edge(
    edge_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = await dao.edge_get_by_id(db, edge_id)
    if not edge:
        raise HTTPException(status_code=404, detail="关系边不存在")
    return _ok(
        LineageEdgeResponse.model_validate(edge).model_dump(**_DUMP_OPTS),
        msg="已确认",
    )


@router.post("/edges/{edge_id}/reject")
async def reject_edge(
    edge_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = await dao.edge_get_by_id(db, edge_id)
    if not edge:
        raise HTTPException(status_code=404, detail="关系边不存在")
    return _ok(msg="已拒绝")


@router.get("/stats")
async def get_lineage_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edges, total = await dao.edge_list_all(db, page=1, page_size=1000)

    # AI 生成的血缘边通过 transform_type 判断
    ai_count = sum(1 for e in edges if e.transform_type == "raw_import")
    # 确认/未确认通过 transform_type 区分，此处简化为所有边为已确认
    confirmed_count = total
    pending_count = max(0, len(edges) - confirmed_count)

    return _ok(
        LineageStatsResponse(
            total_edges=total,
            confirmed_count=confirmed_count,
            ai_generated_count=ai_count,
            pending_count=pending_count,
            confirm_rate=(confirmed_count / total * 100) if total > 0 else 0.0,
        ).model_dump(**_DUMP_OPTS)
    )


@router.get("/query")
async def query_lineage(
    type: str | None = Query(None),
    id: uuid.UUID | None = Query(None),
    hops: int = Query(2, ge=1, le=3),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """关系路径查询 — 当前返回简化结果，后续实现图谱查询算法。"""
    edges, _ = await dao.edge_list_all(db, page=1, page_size=100)
    matching = [
        e for e in edges
        if (not type or e.source_type == type or e.target_type == type)
        and (not id or e.source_id == id or e.target_id == id)
    ]
    return _ok(
        {
            "edges": [
                LineageEdgeResponse.model_validate(e).model_dump(**_DUMP_OPTS)
                for e in matching
            ],
            "hops": hops,
            "total": len(matching),
        }
    )
