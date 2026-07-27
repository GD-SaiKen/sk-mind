"""隔离区查询 / 统计 / 重试 / 忽略 服务（B2.6）。

- 列表、统计用同步 Session 直接查 ``sync_quarantine``（经 ``ingestion_batches`` 关联 task）。
- 重试：取出 ``raw_json``（已是 ColumnMapper 映射后的 DB 列格式），复用真实同步的
  ``StageWriter.write`` 单行 upsert 回 raw 表 —— 与正常同步同一写入路径，保证列/跟踪列一致。
- 忽略：置 ``status='ignored'``。
"""

import logging
import uuid
from datetime import datetime, timezone

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.models import IngestionBatch, IngestionTask, Quarantine
from app.modules.ingestion.stage_writer import StageWriter
from app.modules.ingestion.engines.api_sync_engine import load_config

logger = logging.getLogger(__name__)


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _load_interface_config(task: IngestionTask, interface_name: str) -> dict | None:
    """从 task.config.configPath 加载 YAML，按 interface_name 找到接口定义。"""
    cfg = task.config or {} if task else {}
    config_path = cfg.get("configPath") or cfg.get("config_path")
    if not config_path:
        return None
    try:
        full_cfg = load_config(config_path)
    except Exception as e:  # noqa: BLE001
        logger.warning("隔离区重试：加载数据源配置失败 %s: %s", config_path, e)
        return None
    for iface in (full_cfg.get("interfaces") or []):
        if iface.get("name") == interface_name:
            return iface
    return None


def _threshold_pct(task: IngestionTask) -> float:
    """从任务关联的 YAML 接口配置中取最小阈值（最敏感），默认 5%。"""
    cfg = task.config or {} if task else {}
    config_path = cfg.get("configPath") or cfg.get("config_path")
    if not config_path:
        return 5.0
    try:
        full_cfg = load_config(config_path)
    except Exception:  # noqa: BLE001
        return 5.0
    vals: list[float] = []
    for iface in (full_cfg.get("interfaces") or []):
        t = (iface.get("quarantine") or {}).get("threshold_pct")
        if t is None:
            t = (iface.get("reconciliation") or {}).get("threshold_pct")
        if t is not None:
            vals.append(float(t))
    return min(vals) if vals else 5.0


def list_quarantine(
    db: Session,
    task_id: uuid.UUID,
    status: str | None = None,
    interface_name: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[dict], int]:
    """分页列出某任务的隔离记录（经 batch 关联 task_id）。"""
    where = ["b.task_id = :task_id"]
    params: dict = {"task_id": str(task_id)}
    if status:
        where.append("q.status = :status")
        params["status"] = status
    if interface_name:
        where.append("q.interface_name = :iface")
        params["iface"] = interface_name
    where_sql = " AND ".join(where)

    total = db.execute(
        text(
            f"SELECT count(*) FROM sync_quarantine q "
            f"JOIN ingestion_batches b ON b.id = q.batch_id "
            f"WHERE {where_sql}"
        ),
        params,
    ).scalar_one()

    params["limit"] = page_size
    params["offset"] = (page - 1) * page_size
    rows = db.execute(
        text(
            f"SELECT q.* FROM sync_quarantine q "
            f"JOIN ingestion_batches b ON b.id = q.batch_id "
            f"WHERE {where_sql} "
            f"ORDER BY q.created_at DESC LIMIT :limit OFFSET :offset"
        ),
        params,
    ).mappings().all()

    items = []
    for r in rows:
        d = dict(r)
        d["rawJson"] = d.pop("raw_json", None)
        d["batchId"] = d.pop("batch_id")
        d["dataSourceId"] = d.pop("data_source_id")
        d["interfaceName"] = d.pop("interface_name")
        d["pkValue"] = d.pop("pk_value")
        d["rejectionReason"] = d.pop("rejection_reason")
        d["retriedAt"] = d.pop("retried_at")
        d["resolvedAt"] = d.pop("resolved_at")
        d["createdAt"] = d.pop("created_at")
        # JSONB 经驱动返回已是 dict；顺便把 _quality_flags 等一并透明返回
        items.append(d)
    return items, total


def get_stats(db: Session, task_id: uuid.UUID) -> dict:
    """隔离区统计：总数/待处理/已修复/已忽略/隔离率/阈值/熔断触发。"""
    rows = db.execute(
        text(
            "SELECT q.status, count(*) AS c FROM sync_quarantine q "
            "JOIN ingestion_batches b ON b.id = q.batch_id "
            "WHERE b.task_id = :task_id GROUP BY q.status"
        ),
        {"task_id": str(task_id)},
    ).mappings().all()

    counts = {r["status"]: r["c"] for r in rows}
    pending = counts.get("pending", 0)
    resolved = counts.get("resolved", 0)
    ignored = counts.get("ignored", 0)
    total = pending + resolved + ignored

    quarantine_rate = round((pending / total) * 100, 2) if total > 0 else 0.0

    task = db.get(IngestionTask, task_id)
    threshold = _threshold_pct(task) if task else 5.0
    circuit_breaker = quarantine_rate >= threshold

    return {
        "total": total,
        "pending": pending,
        "resolved": resolved,
        "ignored": ignored,
        "quarantineRate": quarantine_rate,
        "threshold": threshold,
        "circuitBreakerTriggered": circuit_breaker,
    }


def retry_quarantine(db: Session, qid: uuid.UUID) -> dict:
    """重试单条隔离记录：raw_json 经 StageWriter 单行写回 raw 表。

    成功 → status='resolved' + resolved_at；失败/写入 0 行 → 仍 'pending' + retried_at。
    """
    q = db.get(Quarantine, qid)
    if q is None:
        return {"success": False, "message": "隔离记录不存在"}

    batch = db.get(IngestionBatch, q.batch_id)
    task = db.get(IngestionTask, batch.task_id) if batch else None
    iface = _load_interface_config(task, q.interface_name) if task else None
    if iface is None:
        return {"success": False, "message": f"无法定位接口配置: {q.interface_name}"}

    target_table = iface["target_table"]
    pk_fields = iface.get("pk_fields") or []
    raw = q.raw_json  # dict，已是 DB 列格式（snake_case）
    if not isinstance(raw, dict):
        return {"success": False, "message": "raw_json 格式非法"}

    has_pk = bool(pk_fields) and all(raw.get(p) not in (None, "") for p in pk_fields)
    sync_mode = "upsert" if has_pk else "insert"

    # 用原始 batch_id 作 staging 命名（staging 表在 promote 后被 DROP，不会冲突）
    b = IngestionBatch(
        id=q.batch_id, task_id=task.id, trigger_type="manual", status="pending"
    )
    writer = StageWriter(db)
    try:
        result = writer.write(
            target_table=target_table,
            batch=b,
            rows=[raw],
            source_id=str(q.data_source_id),
            source_signature=q.interface_name,
            sync_mode=sync_mode,
            pk_fields=pk_fields or None,
        )
        if result.get("success", 0) > 0:
            q.status = "resolved"
            q.resolved_at = _utcnow()
            db.commit()
            return {
                "success": True,
                "status": "resolved",
                "result": result,
            }
        # 写入 0 行（如 null_pk 行 upsert 无命中）：保持 pending，记录重试时间
        q.retried_at = _utcnow()
        db.commit()
        return {
            "success": False,
            "status": "pending",
            "message": "写入 0 行（可能该行为 null_pk，无法 upsert）",
            "result": result,
        }
    except Exception as e:  # noqa: BLE001
        db.rollback()
        q.retried_at = _utcnow()
        db.commit()
        logger.warning("隔离区重试失败 id=%s: %s", qid, e)
        return {"success": False, "status": "pending", "message": str(e)}


def ignore_quarantine(db: Session, qid: uuid.UUID) -> dict:
    """忽略单条隔离记录：status='ignored'。"""
    q = db.get(Quarantine, qid)
    if q is None:
        return {"success": False, "message": "隔离记录不存在"}
    q.status = "ignored"
    db.commit()
    return {"success": True, "status": "ignored"}
