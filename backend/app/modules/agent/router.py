"""Agent 模块路由 — 提供 YAML 语义模型查询和热重载端点。

业务逻辑已提取到 handlers.py，供 REST 和 MCP 路由器复用。
"""

import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user
from app.core.database import get_db
from app.modules.auth.models import User
from app.modules.agent.handlers import (
    handle_catalog,
    handle_query_graph,
    handle_query_metrics,
    handle_query_objects,
    handle_query_relations,
    handle_reload,
)
from app.modules.agent.schemas import (
    QueryObjectsRequest,
    QueryMetricsRequest,
    QueryObjectsResponse,
    QueryMetricsResponse,
    QueryRelationsRequest,
    QueryRelationsResponse,
    RelationItem,
    QueryGraphRequest,
    QueryGraphResponse,
    GraphPathItem,
    GraphPathEdgeItem,
    CatalogObject,
    CatalogMetric,
    CatalogResponse,
)

router = APIRouter(prefix="/agent", tags=["agent"])
logger = logging.getLogger("sk-mind")


# ── Helpers ──────────────────────────────────────────────


def _raise_http_from_error(e: Exception) -> None:
    """将 handler 异常转换为 HTTP 异常。"""
    if isinstance(e, ValueError):
        raise HTTPException(status_code=400, detail=str(e))
    if isinstance(e, RuntimeError):
        raise HTTPException(status_code=500, detail=str(e))
    raise HTTPException(status_code=500, detail=str(e))


# ── POST /api/agent/query_objects ─────────────────────────


@router.post("/query_objects", response_model=QueryObjectsResponse)
async def query_objects(
    body: QueryObjectsRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """根据 YAML 定义的 object 查询 serving 视图数据。"""
    try:
        result = await handle_query_objects(
            db=db,
            source=body.source,
            object_name=body.object_name,
            filters=body.filters,
            order_by=body.order_by,
            limit=body.limit,
        )
    except Exception as e:
        _raise_http_from_error(e)

    return QueryObjectsResponse(
        columns=result["columns"],
        rows=result["rows"],
        total=result["total"],
    )


# ── POST /api/agent/query_metrics ─────────────────────────


@router.post("/query_metrics", response_model=QueryMetricsResponse)
async def query_metrics(
    body: QueryMetricsRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """根据 YAML 定义的 metric 执行聚合查询。"""
    try:
        result = await handle_query_metrics(
            db=db,
            source=body.source,
            metric_name=body.metric_name,
            group_by=body.group_by,
            dimensions=body.dimensions,
            filters=body.filters,
            limit=body.limit,
        )
    except Exception as e:
        _raise_http_from_error(e)

    return QueryMetricsResponse(
        metric_name=result["metric_name"],
        columns=result["columns"],
        rows=result["rows"],
        total=result["total"],
    )


# ── POST /api/agent/query_relations ─────────────────────


@router.post("/query_relations", response_model=QueryRelationsResponse)
async def query_relations(
    body: QueryRelationsRequest,
    current_user: User = Depends(get_current_user),
):
    """根据 YAML 定义返回语义关系目录（类型层）。"""
    try:
        result = handle_query_relations(
            source=body.source,
            relation_type=body.relation_type,
            subject_object=body.subject_object,
            object_object=body.object_object,
            agent_enabled_only=body.agent_enabled_only,
        )
    except Exception as e:
        _raise_http_from_error(e)

    items = [
        RelationItem(
            code=r["code"],
            name=r["name"],
            relation_type=r["relation_type"],
            subject_object=r["subject_object"],
            object_object=r["object_object"],
            cardinality=r["cardinality"],
            join_mechanism=r.get("join_mechanism"),
            description=r.get("description"),
            agent_enabled=r["agent_enabled"],
        )
        for r in result["relations"]
    ]
    return QueryRelationsResponse(
        source=result["source"],
        relations=items,
        total=result["total"],
    )


# ── POST /api/agent/query_graph ──────────────────────────


@router.post("/query_graph", response_model=QueryGraphResponse)
async def query_graph(
    body: QueryGraphRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """查询业务关系图谱中的实例路径（1-3 跳）。"""
    try:
        result = await handle_query_graph(
            db=db,
            source=body.source,
            object_type=body.object_type,
            entity_id=body.entity_id,
            relation_code=body.relation_code,
            hops=body.hops,
            min_confidence=body.min_confidence,
            confirmed_only=body.confirmed_only,
        )
    except Exception as e:
        _raise_http_from_error(e)

    return QueryGraphResponse(
        source=result["source"],
        paths=[
            GraphPathItem(
                edges=[GraphPathEdgeItem(**e) for e in path["edges"]]
            )
            for path in result["paths"]
        ],
        hops=result["hops"],
        total=result["total"],
    )


# ── GET /api/agent/catalog ────────────────────────────────


@router.get("/catalog", response_model=CatalogResponse)
async def get_catalog(
    source: str = Query(default="mes", max_length=50),
    current_user: User = Depends(get_current_user),
):
    """列出指定 source 的所有业务对象和指标。"""
    try:
        result = handle_catalog(source=source)
    except Exception as e:
        _raise_http_from_error(e)

    return CatalogResponse(
        source=result["source"],
        objects=[
            CatalogObject(
                name=obj["name"],
                display_name=obj["display_name"],
                description=obj["description"],
            )
            for obj in result["objects"]
        ],
        metrics=[
            CatalogMetric(
                name=m["name"],
                display_name=m["display_name"],
                description=m["description"],
                source_object=m["source_object"],
            )
            for m in result["metrics"]
        ],
    )


# ── POST /api/agent/reload ────────────────────────────────


@router.post("/reload")
async def reload_semantic(
    source: str = Query(default="mes", max_length=50),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """热重载 YAML 配置并同步到 DB 缓存。"""
    try:
        result = await handle_reload(db=db, source=source)
    except Exception as e:
        _raise_http_from_error(e)

    return result
