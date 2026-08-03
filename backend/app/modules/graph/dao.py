"""业务关系图谱数据访问层。"""

import uuid
from typing import Any

import sqlalchemy as sa
from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.graph.models import BusinessGraphEdge
from app.modules.semantic.models import SemanticObject, SemanticRelation


# ═══════════════════════════════════════════════════════
# 边列表 / 详情
# ═══════════════════════════════════════════════════════

async def edge_list(
    db: AsyncSession,
    *,
    keyword: str | None = None,
    relation_code: str | None = None,
    status: str | None = None,
    generated_by: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[dict], int]:
    """返回边为 list[dict]，带关系名/对象名。"""
    e = BusinessGraphEdge
    query = (
        select(
            e.id,
            e.relation_id,
            e.from_object_id,
            e.from_entity_id,
            e.to_object_id,
            e.to_entity_id,
            e.edge_properties,
            e.source_dataset,
            e.generated_by,
            e.confidence,
            e.status,
            e.confirmed_by,
            e.confirmed_at,
            e.valid_from,
            e.valid_to,
            e.created_at,
            e.updated_at,
            SemanticRelation.name.label("_relation_name"),
            SemanticRelation.code.label("_relation_code"),
            SemanticObject.name.label("_from_object_name"),
        )
        .select_from(e)
        .join(SemanticRelation, SemanticRelation.id == e.relation_id)
        .join(SemanticObject, SemanticObject.id == e.from_object_id)
    )
    if keyword:
        query = query.filter(
            e.from_entity_id.ilike(f"%{keyword}%")
            | e.to_entity_id.ilike(f"%{keyword}%")
        )
    if relation_code:
        query = query.filter(SemanticRelation.code == relation_code)
    if status:
        query = query.filter(e.status == status)
    if generated_by:
        query = query.filter(e.generated_by == generated_by)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(e.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    rows = result.all()

    # 解析 to_object_name
    to_obj_ids = {row[4] for row in rows}
    to_names: dict[uuid.UUID, str] = {}
    if to_obj_ids:
        to_result = await db.execute(
            select(SemanticObject.id, SemanticObject.name).where(
                SemanticObject.id.in_(to_obj_ids)
            )
        )
        to_names = {row[0]: row[1] for row in to_result}

    items = []
    for row in rows:
        items.append({
            "id": row[0],
            "relation_id": row[1],
            "from_object_id": row[2],
            "from_entity_id": row[3],
            "to_object_id": row[4],
            "to_entity_id": row[5],
            "edge_properties": row[6],
            "source_dataset": row[7],
            "generated_by": row[8],
            "confidence": float(row[9]) if row[9] is not None else 0.0,
            "status": row[10],
            "confirmed_by": row[11],
            "confirmed_at": row[12],
            "valid_from": row[13],
            "valid_to": row[14],
            "created_at": row[15],
            "updated_at": row[16],
            "relation_name": row[17],
            "relation_code": row[18],
            "from_object_name": row[19],
            "to_object_name": to_names.get(row[4]),
        })
    return items, total


async def edge_get_by_id(
    db: AsyncSession, edge_id: uuid.UUID,
) -> BusinessGraphEdge | None:
    return await db.get(BusinessGraphEdge, edge_id)


async def edge_detail(
    db: AsyncSession, edge_id: uuid.UUID,
) -> dict | None:
    """返回单条边的完整 dict（含关系名/对象名），不存在返回 None。"""
    e = BusinessGraphEdge
    result = await db.execute(
        select(
            e.id,
            e.relation_id,
            e.from_object_id,
            e.from_entity_id,
            e.to_object_id,
            e.to_entity_id,
            e.edge_properties,
            e.source_dataset,
            e.generated_by,
            e.confidence,
            e.status,
            e.confirmed_by,
            e.confirmed_at,
            e.valid_from,
            e.valid_to,
            e.created_at,
            e.updated_at,
            SemanticRelation.name.label("_relation_name"),
            SemanticRelation.code.label("_relation_code"),
            SemanticObject.name.label("_from_object_name"),
        )
        .select_from(e)
        .join(SemanticRelation, SemanticRelation.id == e.relation_id)
        .join(SemanticObject, SemanticObject.id == e.from_object_id)
        .where(e.id == edge_id)
    )
    row = result.first()
    if row is None:
        return None

    to_obj = await db.get(SemanticObject, row[4])
    return {
        "id": row[0],
        "relation_id": row[1],
        "from_object_id": row[2],
        "from_entity_id": row[3],
        "to_object_id": row[4],
        "to_entity_id": row[5],
        "edge_properties": row[6],
        "source_dataset": row[7],
        "generated_by": row[8],
        "confidence": float(row[9]) if row[9] is not None else 0.0,
        "status": row[10],
        "confirmed_by": row[11],
        "confirmed_at": row[12],
        "valid_from": row[13],
        "valid_to": row[14],
        "created_at": row[15],
        "updated_at": row[16],
        "relation_name": row[17],
        "relation_code": row[18],
        "from_object_name": row[19],
        "to_object_name": to_obj.name if to_obj else None,
    }


async def edge_update_status(
    db: AsyncSession,
    edge: BusinessGraphEdge,
    status: str,
    confirmed_by: str | None = None,
) -> BusinessGraphEdge:
    edge.status = status
    if confirmed_by is not None:
        edge.confirmed_by = confirmed_by
        from datetime import datetime

        edge.confirmed_at = datetime.now()
    await db.flush()
    return edge


# ═══════════════════════════════════════════════════════
# Stats
# ═══════════════════════════════════════════════════════

async def graph_stats(db: AsyncSession) -> dict:
    e = BusinessGraphEdge
    total = (await db.execute(
        select(func.count()).select_from(e)
    )).scalar_one()
    confirmed = (await db.execute(
        select(func.count()).select_from(e).where(e.status == "confirmed")
    )).scalar_one()
    pending = (await db.execute(
        select(func.count()).select_from(e).where(e.status == "pending")
    )).scalar_one()
    ai_generated = (await db.execute(
        select(func.count()).select_from(e).where(e.generated_by == "ai")
    )).scalar_one()
    return {
        "total_edges": total,
        "confirmed_count": confirmed,
        "ai_generated_count": ai_generated,
        "pending_count": pending,
        "confirm_rate": round(confirmed / total * 100, 2) if total else 0.0,
    }


# ═══════════════════════════════════════════════════════
# 路径查询（简化 BFS，hops ≤ 3）
# ═══════════════════════════════════════════════════════

async def graph_query(
    db: AsyncSession,
    *,
    object_type: str | None = None,
    entity_id: str | None = None,
    relation_code: str | None = None,
    hops: int = 2,
    min_confidence: float = 0.0,
    confirmed_only: bool = False,
) -> list[list[dict]]:
    """BFS 查询关系路径，返回路径列表（每条路径为 edge dict 列表）。"""
    e = BusinessGraphEdge
    query = (
        select(e, SemanticRelation.code.label("_rel_code"),
               SemanticRelation.name.label("_rel_name"),
               SemanticObject.name.label("_from_name"))
        .select_from(e)
        .join(SemanticRelation, SemanticRelation.id == e.relation_id)
        .join(SemanticObject, SemanticObject.id == e.from_object_id)
    )
    if relation_code:
        query = query.filter(SemanticRelation.code == relation_code)
    if confirmed_only:
        query = query.filter(e.status == "confirmed")
    if min_confidence > 0:
        query = query.filter(e.confidence >= min_confidence)

    result = await db.execute(query)
    rows = result.all()

    # 组装为 dict
    edges = []
    for row in rows:
        edge = row[0]
        edges.append({
            "id": edge.id,
            "relation_id": edge.relation_id,
            "from_object_id": edge.from_object_id,
            "from_entity_id": edge.from_entity_id,
            "to_object_id": edge.to_object_id,
            "to_entity_id": edge.to_entity_id,
            "relation_code": row[1],
            "relation_name": row[2],
            "from_object_name": row[3],
            "confidence": float(edge.confidence) if edge.confidence is not None else 0.0,
            "status": edge.status,
        })

    # 对象 id → object code 映射（用于 from_type/to_type）
    obj_ids = {edge["from_object_id"] for edge in edges} | {
        edge["to_object_id"] for edge in edges
    }
    obj_names: dict[uuid.UUID, str] = {}
    if obj_ids:
        obj_result = await db.execute(
            select(SemanticObject.id, SemanticObject.code).where(
                SemanticObject.id.in_(obj_ids)
            )
        )
        obj_names = {row[0]: row[1] for row in obj_result}

    # 起点过滤：对象类型（按 code 后段匹配）+ 可选实体 id
    start_edge_ids: set[uuid.UUID] = set()
    for edge in edges:
        code = obj_names.get(edge["from_object_id"], "")
        obj_key = code.split(".", 1)[-1] if "." in code else code
        if object_type and obj_key != object_type:
            continue
        if entity_id and edge["from_entity_id"] != entity_id:
            continue
        start_edge_ids.add(edge["id"])

    if not start_edge_ids:
        return []

    paths: list[list[dict]] = []
    by_id = {edge["id"]: edge for edge in edges}
    adjacency: dict[uuid.UUID, list[dict]] = {}
    for edge in edges:
        adjacency.setdefault(edge["to_object_id"], []).append(edge)

    # 简化：从起点边出发，逐层扩展（同方向 to 扩展）
    frontier: list[list[dict]] = [[by_id[i]] for i in start_edge_ids]
    visited_paths: set[tuple[uuid.UUID, ...]] = set()

    for _ in range(hops):
        next_frontier: list[list[dict]] = []
        for path in frontier:
            key = tuple(e["id"] for e in path)
            if key in visited_paths:
                continue
            visited_paths.add(key)
            paths.append(path)
            last = path[-1]
            for nxt in adjacency.get(last["to_object_id"], []):
                if nxt["id"] in {e["id"] for e in path}:
                    continue
                next_frontier.append(path + [nxt])
        frontier = next_frontier
        if not frontier:
            break

    # 转成对外结构（from_type/to_type 用对象 code 后段）
    result_paths = []
    for path in paths:
        out_edges = []
        for edge in path:
            from_code = obj_names.get(edge["from_object_id"], "")
            to_code = obj_names.get(edge["to_object_id"], "")
            out_edges.append({
                "from_type": from_code.split(".", 1)[-1] if "." in from_code else from_code,
                "from_id": edge["from_entity_id"],
                "relation_code": edge["relation_code"],
                "relation_name": edge["relation_name"],
                "to_type": to_code.split(".", 1)[-1] if "." in to_code else to_code,
                "to_id": edge["to_entity_id"],
                "confidence": edge["confidence"],
                "status": edge["status"],
            })
        result_paths.append(out_edges)
    return result_paths
