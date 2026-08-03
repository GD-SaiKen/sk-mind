"""业务关系边生成服务 — 从 serving 视图按关系定义实例化边。"""

import logging
import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.semantic.loader import get_loader

logger = logging.getLogger("sk-mind")


def _parse_join_fields(join_mechanism: str) -> list[list[str]]:
    """解析 join_mechanism 为字段列表。

    支持:
    - "machine_no" → ["machine_no"]
    - "workorder_no + procedure_no" → AND 复合
    - "mid / machine_no" → 取第一个在两边都存在者
    """
    result = []
    for group in join_mechanism.split("+"):
        alts = [f.strip() for f in group.split("/") if f.strip()]
        result.append(alts)  # 每个位置保留备选列表
    return result


async def generate_edges_for_relation(
    db: AsyncSession,
    *,
    relation_code: str,
    source: str = "mes",
    relation_id: uuid.UUID | None = None,
    subject_object_id: uuid.UUID | None = None,
    object_object_id: uuid.UUID | None = None,
) -> int:
    """按关系定义从 serving 视图生成实例边，返回新生成数量。"""
    if not relation_id or not subject_object_id or not object_object_id:
        raise ValueError(
            f"relation '{relation_code}' missing DB ids — 关系未同步到数据库"
        )

    loader = get_loader(source)
    rel_def = loader.get_relation(relation_code)
    if rel_def is None:
        raise KeyError(f"relation '{relation_code}' not found in source '{source}'")

    subject_def = loader.get_object(rel_def["subject"])
    object_def = loader.get_object(rel_def["object"])
    if subject_def is None or object_def is None:
        raise ValueError(
            f"relation '{relation_code}' references missing object"
        )

    # 解析 serving 表与 field_map
    subj_binding = (subject_def.get("bindings") or [{}])[0]
    obj_binding = (object_def.get("bindings") or [{}])[0]
    subj_table = (subj_binding.get("tables") or [{}])[0]
    obj_table = (obj_binding.get("tables") or [{}])[0]
    subj_schema = subj_table.get("schema", "serving")
    obj_schema = obj_table.get("schema", "serving")
    subj_tbl = subj_table.get("table", "")
    obj_tbl = obj_table.get("table", "")
    if not subj_tbl or not obj_tbl:
        raise ValueError(f"relation '{relation_code}' missing serving table")

    subj_fm = subj_binding.get("field_map", {})
    obj_fm = obj_binding.get("field_map", {})

    # 主体/客体 key（from_entity / to_entity）
    subj_key = (subject_def.get("keys") or [""])[0]
    obj_key = (object_def.get("keys") or [""])[0]
    if not subj_key or not obj_key:
        raise ValueError(f"relation '{relation_code}' missing object key")
    subj_key_col = subj_fm.get(subj_key, subj_key)
    obj_key_col = obj_fm.get(obj_key, obj_key)

    # join 字段解析
    join_groups = _parse_join_fields(rel_def.get("join_mechanism", ""))
    join_clauses = []
    for group in join_groups:
        chosen = next(
            (f for f in group if f in subj_fm and f in obj_fm),
            None,
        )
        if chosen is None:
            raise ValueError(
                f"relation '{relation_code}' join field {group} not in both field maps"
            )
        subj_col = subj_fm.get(chosen, chosen)
        obj_col = obj_fm.get(chosen, chosen)
        join_clauses.append(f"s.{subj_col} = o.{obj_col}")

    if not join_clauses:
        raise ValueError(f"relation '{relation_code}' has empty join_mechanism")

    join_sql = " AND ".join(join_clauses)
    source_dataset = f"{subj_schema}.{subj_tbl} ↔ {obj_schema}.{obj_tbl}"

    # id 与时间戳：显式生成，兼容 PostgreSQL（gen_random_uuid）与 SQLite 测试库
    dialect = db.bind.dialect.name if db.bind is not None else "postgresql"
    if dialect == "sqlite":
        id_expr = "lower(hex(randomblob(16)))"
        now_expr = "datetime('now')"
        conflict_clause = "OR IGNORE"
        insert_keyword = "INSERT OR IGNORE"
    else:
        id_expr = "gen_random_uuid()"
        now_expr = "NOW()"
        conflict_clause = ""
        insert_keyword = "INSERT"

    sql = f"""
        {insert_keyword} INTO business_graph_edges
            (relation_id, from_object_id, from_entity_id,
             to_object_id, to_entity_id,
             source_dataset, generated_by, confidence, status,
             id, created_at, updated_at)
        SELECT
            :relation_id, :from_object_id, s.{subj_key_col},
            :to_object_id, o.{obj_key_col},
            :source_dataset, 'system', 0.95, 'pending',
            {id_expr}, {now_expr}, {now_expr}
        FROM {subj_schema}.{subj_tbl} s
        JOIN {obj_schema}.{obj_tbl} o ON {join_sql}
        WHERE s.{subj_key_col} IS NOT NULL
          AND o.{obj_key_col} IS NOT NULL
    """
    if dialect != "sqlite":
        sql += "\n        ON CONFLICT ON CONSTRAINT uq_graph_edge DO NOTHING"

    try:
        result = await db.execute(
            text(sql),
            {
                "relation_id": relation_id,
                "from_object_id": subject_object_id,
                "to_object_id": object_object_id,
                "source_dataset": source_dataset,
            },
        )
        await db.commit()
        return result.rowcount or 0
    except Exception:
        await db.rollback()
        logger.exception("Edge generation failed for relation '%s'", relation_code)
        raise
