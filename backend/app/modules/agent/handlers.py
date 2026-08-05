"""Agent 共享查询逻辑 — 从 router.py 提取，供 REST 和 MCP 路由器复用。"""

import logging
from typing import Any, Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.semantic.loader import get_loader
from app.modules.semantic.mapper import ObjectQueryMapper, MetricQueryMapper
from app.modules.graph.dao import graph_query

logger = logging.getLogger("sk-mind")


def _rows_to_dict(columns: list[str], rows: list) -> list[dict]:
    """将原生 SQL 行列表转为 dict 列表。"""
    return [dict(zip(columns, row)) for row in rows]


async def handle_query_objects(
    db: AsyncSession,
    source: str = "mes",
    object_name: Optional[str] = None,
    filters: Optional[dict[str, Any]] = None,
    order_by: Optional[str] = None,
    limit: int = 100,
) -> dict[str, Any]:
    """根据 YAML 定义的 object 查询 serving 视图数据。"""
    try:
        loader = get_loader(source)
    except FileNotFoundError:
        raise ValueError(f"Source '{source}' not found")

    # 不传 object_name 时返回对象目录
    if not object_name:
        objects = loader.list_objects()
        return {
            "columns": ["object", "display_name", "description", "domain"],
            "rows": [
                {
                    "object": obj.get("object", ""),
                    "display_name": obj.get("display_name", ""),
                    "description": obj.get("description", ""),
                    "domain": obj.get("domain", ""),
                }
                for obj in objects
            ],
            "total": len(objects),
        }

    obj_def = loader.get_object(object_name)
    if obj_def is None:
        raise ValueError(f"Object '{object_name}' not found in source '{source}'")

    mapper = ObjectQueryMapper(obj_def)
    sql, params = mapper.build_query(
        filters=filters,
        order_by=order_by,
        limit=limit,
    )

    try:
        result = await db.execute(text(sql), params)
        rows = result.fetchall()
        columns = list(result.keys())
    except Exception as e:
        logger.exception("Query objects failed: %s", sql)
        raise RuntimeError(str(e))

    return {
        "columns": columns,
        "rows": _rows_to_dict(columns, rows),
        "total": len(rows),
    }


async def handle_query_metrics(
    db: AsyncSession,
    source: str = "mes",
    metric_name: Optional[str] = None,
    group_by: Optional[list[str]] = None,
    dimensions: Optional[list[str]] = None,
    filters: Optional[dict[str, Any]] = None,
    limit: int = 50,
) -> dict[str, Any]:
    """根据 YAML 定义的 metric 执行聚合查询。"""
    try:
        loader = get_loader(source)
    except FileNotFoundError:
        raise ValueError(f"Source '{source}' not found")

    # 不传 metric_name 时返回指标目录
    if not metric_name:
        metrics = loader.list_metrics()
        return {
            "metric_name": "",
            "columns": ["metric", "display_name", "description", "source_object", "category"],
            "rows": [
                {
                    "metric": m.get("metric", ""),
                    "display_name": m.get("display_name", ""),
                    "description": m.get("description", ""),
                    "source_object": m.get("source_object", ""),
                    "category": m.get("category", ""),
                }
                for m in metrics
            ],
            "total": len(metrics),
        }

    metric_def = loader.get_metric(metric_name)
    if metric_def is None:
        raise ValueError(f"Metric '{metric_name}' not found in source '{source}'")

    source_obj_name = metric_def.get("source_object", "")
    obj_def = loader.get_object(source_obj_name)
    if obj_def is None:
        raise ValueError(
            f"Source object '{source_obj_name}' not found for metric '{metric_name}'"
        )

    mapper = MetricQueryMapper(metric_def, obj_def)
    sql, params = mapper.build_query(
        group_by=group_by,
        dimensions=dimensions,
        filters=filters,
        limit=limit,
    )

    try:
        result = await db.execute(text(sql), params)
        rows = result.fetchall()
        columns = list(result.keys())
    except Exception as e:
        logger.exception("Query metrics failed: %s", sql)
        raise RuntimeError(str(e))

    return {
        "metric_name": metric_name,
        "columns": columns,
        "rows": _rows_to_dict(columns, rows),
        "total": len(rows),
    }


def handle_query_relations(
    source: str = "mes",
    relation_type: Optional[str] = None,
    subject_object: Optional[str] = None,
    object_object: Optional[str] = None,
    agent_enabled_only: bool = False,
) -> dict[str, Any]:
    """根据 YAML 定义返回语义关系目录（类型层）。"""
    try:
        loader = get_loader(source)
    except FileNotFoundError:
        raise ValueError(f"Source '{source}' not found")

    relations = loader.list_relations()
    if relation_type:
        relations = [r for r in relations if r.get("relation_type") == relation_type]
    if subject_object:
        relations = [r for r in relations if r.get("subject") == subject_object]
    if object_object:
        relations = [r for r in relations if r.get("object") == object_object]
    if agent_enabled_only:
        relations = [r for r in relations if r.get("agent_enabled", True)]

    items = [
        {
            "code": r["code"],
            "name": r.get("name", r["code"]),
            "relation_type": r.get("relation_type", ""),
            "subject_object": r.get("subject", ""),
            "object_object": r.get("object", ""),
            "cardinality": r.get("cardinality", "1:N"),
            "join_mechanism": r.get("join_mechanism"),
            "description": r.get("description"),
            "agent_enabled": r.get("agent_enabled", True),
        }
        for r in relations
    ]
    return {
        "source": source,
        "relations": items,
        "total": len(items),
    }


async def handle_query_graph(
    db: AsyncSession,
    source: str = "mes",
    object_type: Optional[str] = None,
    entity_id: Optional[str] = None,
    relation_code: Optional[str] = None,
    hops: int = 2,
    min_confidence: float = 0.0,
    confirmed_only: bool = False,
) -> dict[str, Any]:
    """查询业务关系图谱中的实例路径（1-3 跳）。"""
    try:
        paths = await graph_query(
            db,
            object_type=object_type,
            entity_id=entity_id,
            relation_code=relation_code,
            hops=hops,
            min_confidence=min_confidence,
            confirmed_only=confirmed_only,
        )
    except Exception as e:
        logger.exception("Graph query failed")
        raise RuntimeError(str(e))

    return {
        "source": source,
        "paths": [{"edges": [dict(e) for e in path]} for path in paths],
        "hops": hops,
        "total": len(paths),
    }


def handle_catalog(source: str = "mes") -> dict[str, Any]:
    """列出指定 source 的所有业务对象和指标。"""
    try:
        loader = get_loader(source)
    except FileNotFoundError:
        raise ValueError(f"Source '{source}' not found")

    objects = loader.list_objects()
    metrics = loader.list_metrics()

    return {
        "source": source,
        "objects": [
            {
                "name": obj.get("object", ""),
                "display_name": obj.get("display_name", ""),
                "description": obj.get("description", ""),
            }
            for obj in objects
        ],
        "metrics": [
            {
                "name": m.get("metric", ""),
                "display_name": m.get("display_name", ""),
                "description": m.get("description", ""),
                "source_object": m.get("source_object", ""),
            }
            for m in metrics
        ],
    }


async def handle_reload(db: AsyncSession, source: str = "mes") -> dict[str, Any]:
    """热重载 YAML 配置并同步到 DB 缓存。"""
    try:
        loader = get_loader(source)
        loader.reload()
        await loader.load_all_async(db, force=True)
    except FileNotFoundError:
        raise ValueError(f"Source '{source}' not found")
    except Exception as e:
        logger.exception("Reload failed for source '%s'", source)
        raise RuntimeError(str(e))

    return {
        "source": source,
        "objects_loaded": len(loader.list_objects()),
        "metrics_loaded": len(loader.list_metrics()),
        "status": "reloaded",
    }
