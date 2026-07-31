"""Agent 模块路由 — 提供 YAML 语义模型查询和热重载端点。"""

import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user
from app.core.database import get_db
from app.modules.auth.models import User
from app.modules.agent.schemas import (
    QueryObjectsRequest,
    QueryMetricsRequest,
    QueryObjectsResponse,
    QueryMetricsResponse,
    CatalogObject,
    CatalogMetric,
    CatalogResponse,
)
from app.modules.semantic.loader import get_loader
from app.modules.semantic.mapper import ObjectQueryMapper, MetricQueryMapper

router = APIRouter(prefix="/agent", tags=["agent"])
logger = logging.getLogger("sk-mind")


# ── Helper ────────────────────────────────────────────────


def _rows_to_dict(columns: list[str], rows: list) -> list[dict]:
    """将原生 SQL 行列表转为 dict 列表。"""
    return [dict(zip(columns, row)) for row in rows]


# ── POST /api/agent/query_objects ─────────────────────────


@router.post("/query_objects", response_model=QueryObjectsResponse)
async def query_objects(
    body: QueryObjectsRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """根据 YAML 定义的 object 查询 serving 视图数据。"""
    try:
        loader = get_loader(body.source)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail=f"Source '{body.source}' not found")

    obj_def = loader.get_object(body.object_name)
    if obj_def is None:
        raise HTTPException(
            status_code=404, detail=f"Object '{body.object_name}' not found in source '{body.source}'"
        )

    mapper = ObjectQueryMapper(obj_def)
    sql, params = mapper.build_query(
        filters=body.filters,
        order_by=body.order_by,
        limit=body.limit,
    )

    try:
        result = await db.execute(text(sql), params)
        rows = result.fetchall()
        columns = list(result.keys())
    except Exception as e:
        logger.exception("Query objects failed: %s", sql)
        raise HTTPException(status_code=500, detail=str(e))

    return QueryObjectsResponse(
        columns=columns,
        rows=_rows_to_dict(columns, rows),
        total=len(rows),
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
        loader = get_loader(body.source)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail=f"Source '{body.source}' not found")

    metric_def = loader.get_metric(body.metric_name)
    if metric_def is None:
        raise HTTPException(
            status_code=404, detail=f"Metric '{body.metric_name}' not found in source '{body.source}'"
        )

    source_obj_name = metric_def.get("source_object", "")
    obj_def = loader.get_object(source_obj_name)
    if obj_def is None:
        raise HTTPException(
            status_code=404, detail=f"Source object '{source_obj_name}' not found for metric '{body.metric_name}'"
        )

    mapper = MetricQueryMapper(metric_def, obj_def)
    sql, params = mapper.build_query(
        group_by=body.group_by,
        dimensions=body.dimensions,
        filters=body.filters,
        limit=body.limit,
    )

    try:
        result = await db.execute(text(sql), params)
        rows = result.fetchall()
        columns = list(result.keys())
    except Exception as e:
        logger.exception("Query metrics failed: %s", sql)
        raise HTTPException(status_code=500, detail=str(e))

    return QueryMetricsResponse(
        metric_name=body.metric_name,
        columns=columns,
        rows=_rows_to_dict(columns, rows),
        total=len(rows),
    )


# ── GET /api/agent/catalog ────────────────────────────────


@router.get("/catalog", response_model=CatalogResponse)
async def get_catalog(
    source: str = Query(default="mes", max_length=50),
    current_user: User = Depends(get_current_user),
):
    """列出指定 source 的所有业务对象和指标。"""
    try:
        loader = get_loader(source)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail=f"Source '{source}' not found")

    catalog = loader.get_catalog()
    objects = loader.list_objects()
    metrics = loader.list_metrics()

    return CatalogResponse(
        source=source,
        objects=[
            CatalogObject(
                name=obj.get("object", ""),
                display_name=obj.get("display_name", ""),
                description=obj.get("description", ""),
            )
            for obj in objects
        ],
        metrics=[
            CatalogMetric(
                name=m.get("metric", ""),
                display_name=m.get("display_name", ""),
                description=m.get("description", ""),
                source_object=m.get("source_object", ""),
            )
            for m in metrics
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
        loader = get_loader(source)
        loader.reload()
        await loader.load_all_async(db, force=True)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail=f"Source '{source}' not found")
    except Exception as e:
        logger.exception("Reload failed for source '%s'", source)
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "source": source,
        "objects_loaded": len(loader.list_objects()),
        "metrics_loaded": len(loader.list_metrics()),
        "status": "reloaded",
    }
