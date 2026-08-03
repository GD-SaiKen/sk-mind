"""graph 模块路由 — 业务关系边生成、查询、确认、统计。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.graph import dao
from app.modules.graph.schemas import (
    EdgeGenerateResponse,
    GraphEdgeListResponse,
    GraphEdgeResponse,
    GraphPath,
    GraphPathEdge,
    GraphQueryResponse,
    GraphStatsResponse,
)
from app.modules.graph.service import generate_edges_for_relation
from app.modules.semantic.dao import (
    semantic_object_get_by_code,
    semantic_relation_get_by_code,
)
from app.modules.semantic.loader import get_loader

router = APIRouter(prefix="/graph", tags=["graph"])

_DUMP_OPTS = {"by_alias": True}


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


@router.post("/edges/generate")
async def generate_edges(
    relation_code: str = Query(..., alias="relationCode"),
    source: str = Query("mes", max_length=50),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """按关系定义从 serving 视图生成实例边。"""
    try:
        loader = get_loader(source)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail=f"Source '{source}' not found")

    rel_def = loader.get_relation(relation_code)
    if rel_def is None:
        raise HTTPException(
            status_code=404,
            detail=f"Relation '{relation_code}' not found in source '{source}'",
        )

    # 关系必须已同步到 DB（YAML → semantic_relations）
    db_rel = await semantic_relation_get_by_code(db, relation_code)
    if db_rel is None:
        raise HTTPException(
            status_code=400,
            detail=f"Relation '{relation_code}' 未同步到数据库，请先 reload",
        )

    subject_obj = await semantic_object_get_by_code(
        db, f"{source}.{rel_def.get('subject')}"
    )
    object_obj = await semantic_object_get_by_code(
        db, f"{source}.{rel_def.get('object')}"
    )
    if subject_obj is None or object_obj is None:
        raise HTTPException(
            status_code=400,
            detail=f"Relation '{relation_code}' 的主体/客体对象未同步到数据库",
        )

    try:
        generated = await generate_edges_for_relation(
            db,
            relation_code=relation_code,
            source=source,
            relation_id=db_rel.id,
            subject_object_id=subject_obj.id,
            object_object_id=object_obj.id,
        )
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return _ok(
        EdgeGenerateResponse(
            relation_code=relation_code,
            generated=generated,
        ).model_dump(**_DUMP_OPTS),
        msg=f"生成 {generated} 条边",
    )


@router.get("/edges")
async def list_edges(
    keyword: str | None = Query(None),
    relation_code: str | None = Query(None, alias="relationCode"),
    status: str | None = Query(None),
    generated_by: str | None = Query(None, alias="generatedBy"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.edge_list(
        db,
        keyword=keyword,
        relation_code=relation_code,
        status=status,
        generated_by=generated_by,
        page=page,
        page_size=page_size,
    )
    return _ok(
        GraphEdgeListResponse(
            items=[GraphEdgeResponse(**i) for i in items],
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.get("/edges/{edge_id}")
async def get_edge(
    edge_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = await dao.edge_detail(db, edge_id)
    if item is None:
        raise HTTPException(status_code=404, detail="关系边不存在")
    return _ok(GraphEdgeResponse(**item).model_dump(**_DUMP_OPTS))


@router.post("/edges/{edge_id}/confirm")
async def confirm_edge(
    edge_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = await dao.edge_get_by_id(db, edge_id)
    if not edge:
        raise HTTPException(status_code=404, detail="关系边不存在")
    await dao.edge_update_status(
        db, edge, "confirmed", confirmed_by=current_user.display_name
    )
    await db.commit()
    item = await dao.edge_detail(db, edge_id)
    return _ok(
        GraphEdgeResponse(**item).model_dump(**_DUMP_OPTS),
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
    await dao.edge_update_status(db, edge, "rejected")
    await db.commit()
    return _ok(msg="已拒绝")


@router.post("/edges/{edge_id}/insufficient")
async def insufficient_edge(
    edge_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    edge = await dao.edge_get_by_id(db, edge_id)
    if not edge:
        raise HTTPException(status_code=404, detail="关系边不存在")
    await dao.edge_update_status(db, edge, "insufficient")
    await db.commit()
    return _ok(msg="已标记信息不足")


@router.get("/stats")
async def get_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stats = await dao.graph_stats(db)
    return _ok(GraphStatsResponse(**stats).model_dump(**_DUMP_OPTS))


@router.get("/query")
async def query_graph(
    type: str | None = Query(None),
    id: str | None = Query(None),
    relation_code: str | None = Query(None, alias="relationCode"),
    hops: int = Query(2, ge=1, le=3),
    min_confidence: float = Query(0.0, ge=0.0, le=1.0, alias="minConfidence"),
    confirmed_only: bool = Query(False, alias="confirmedOnly"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """关系路径查询（BFS，hops 1-3）。"""
    paths = await dao.graph_query(
        db,
        object_type=type,
        entity_id=id,
        relation_code=relation_code,
        hops=hops,
        min_confidence=min_confidence,
        confirmed_only=confirmed_only,
    )
    return _ok(
        GraphQueryResponse(
            paths=[
                GraphPath(edges=[GraphPathEdge(**e) for e in path])
                for path in paths
            ],
            hops=hops,
            total=len(paths),
        ).model_dump(**_DUMP_OPTS)
    )
