"""RQ Worker 任务入口。

对应策略文档：04-同步引擎技术实现 §4。
"""

import logging
import uuid

from rq import get_current_job

from app.modules.ingestion.services.connector_service import ConnectorService
from app.modules.ingestion.services.sync_service import SyncService

logger = logging.getLogger(__name__)


def run_full_sync(
    task_id: str,
    source_object_name: str,
    connector_config: dict,
    raw_table_name: str,
):
    """RQ 任务：执行数据库全量同步。

    Args:
        task_id: 任务 ID（UUID 字符串）。
        source_object_name: 源表名。
        connector_config: 连接器配置字典。
        raw_table_name: 目标 Raw 表名。
    """
    job = get_current_job()
    task_uuid = uuid.UUID(task_id)

    try:
        connector = ConnectorService.create_sqlserver(connector_config)
        connector.connect()

        service = SyncService()
        result = service.execute_full_sync(
            task_id=task_uuid,
            source_object_name=source_object_name,
            connector=connector,
            raw_table_name=raw_table_name,
            rq_job=job,
        )
        logger.info("全量同步完成: %s", result)

    except Exception as e:
        logger.exception("全量同步失败: task=%s, table=%s", task_id, source_object_name)
        raise
    finally:
        if "connector" in locals():
            connector.disconnect()


def run_api_pull(
    task_id: str,
    endpoint: str,
    method: str,
    body: dict | None,
    source_system: str,
    connector_config: dict,
    page_size: int = 100,
    max_pages: int | None = None,
):
    """RQ 任务：执行 API 拉取同步。

    Args:
        task_id: 任务 ID（UUID 字符串）。
        endpoint: API 端点。
        method: HTTP 方法。
        body: 请求体模板。
        source_system: 来源系统标识。
        connector_config: API 连接器配置字典。
        page_size: 每页数量。
        max_pages: 最大页数。
    """
    job = get_current_job()
    task_uuid = uuid.UUID(task_id)

    try:
        connector = ConnectorService.create_api(connector_config)
        connector.connect()

        service = SyncService()
        result = service.execute_api_pull(
            task_id=task_uuid,
            endpoint=endpoint,
            method=method,
            body=body,
            source_system=source_system,
            connector=connector,
            page_size=page_size,
            max_pages=max_pages,
            rq_job=job,
        )
        logger.info("API 拉取完成: %s", result)

    except Exception as e:
        logger.exception("API 拉取失败: task=%s, endpoint=%s", task_id, endpoint)
        raise
    finally:
        if "connector" in locals():
            connector.disconnect()


def run_echo_sync(task_id: str, batch_id: str, task_name: str):
    """RQ 任务：模拟同步 — 验证数据源可用后执行模拟流程。"""
    import json
    import time
    import random
    import uuid as _uuid

    job = get_current_job()

    # ── 数据源验证 ─────────────────────────
    task_uuid = _uuid.UUID(task_id)
    from app.modules.ingestion.services.sync_database import get_sync_db
    _db = get_sync_db()
    try:
        from app.modules.ingestion.models import IngestionTask as IT
        from app.modules.data_sources.models import DataSource
        _task = _db.get(IT, task_uuid)
        if _task and _task.data_source_id:
            _ds = _db.get(DataSource, _task.data_source_id)
            ds_name = _ds.name if _ds else "未知数据源"
        else:
            ds_name = None
    finally:
        _db.close()

    # 没有数据源 → 直接失败（不跑模拟）
    if not ds_name:
        _fail_batch(batch_id, "未配置数据源，请先在「数据源管理」中登记 ERP/MES/SRM", task_id[:8])
        return

    logger.info("同步开始: task=%s batch=%s ds=%s", task_id[:8] if task_id else '-', batch_id[:8], ds_name)

    # Redis pub/sub 通道（用于 SSE 推送 + 取消信号）
    try:
        from app.core.queue import redis_conn as _redis
        _channel = f"batch:{batch_id}:progress"
        _ctrl_channel = f"batch:{batch_id}:control"
        _pubsub = _redis.pubsub()
        _pubsub.subscribe(_ctrl_channel)
    except Exception:
        _redis = None
        _channel = None
        _ctrl_channel = None
        _pubsub = None

    def _pub(pct: int, step: str, status: str = "running"):
        """同时写入 job.meta 和 Redis pub/sub。"""
        if job:
            job.meta["progress"] = pct
            job.meta["step"] = step
            job.save_meta()
        if _redis:
            try:
                _redis.publish(_channel, json.dumps({"pct": pct, "step": step, "status": status}))
            except Exception:
                pass

    def _cancelled() -> bool:
        """检查是否收到取消信号。"""
        if not _pubsub:
            return False
        msg = _pubsub.get_message()
        while msg:
            if msg["type"] == "message" and msg["data"] == b"cancel":
                return True
            msg = _pubsub.get_message()
        return False

    stages = [
        (0, 20, "连接数据源..."),
        (20, 40, "获取表结构..."),
        (40, 70, "拉取数据中..."),
        (70, 90, "写入 Raw 层..."),
        (90, 100, "完成"),
    ]

    total_rows = random.randint(5000, 50000)
    fail_rows = random.randint(0, 3)  # 模拟少量格式异常行（跳过不写入）
    retry_count = 0
    max_retries = 3
    cancelled = False
    failed = False

    for pct_start, pct_end, step in stages:
        time.sleep(random.uniform(0.8, 1.5))
        if _cancelled():
            cancelled = True
            _pub(pct_start, f"已取消 ({step})", "cancelled")
            break

        # 模拟偶尔的阶段性失败 → 自动重试
        if random.random() < 0.15 and retry_count < max_retries:
            retry_count += 1
            _pub(pct_start, f"{step} 失败，第 {retry_count}/{max_retries} 次重试...", "running")
            time.sleep(1.5)
            if retry_count >= max_retries and random.random() < 0.5:
                failed = True
                _pub(pct_start, f"{step} 重试耗尽，中止", "failed")
                break

        _pub(pct_end, f"{step} ({pct_end}%%)")

    # 更新批次状态
    from app.modules.ingestion.services.sync_database import get_sync_db
    db = get_sync_db()
    try:
        from app.modules.ingestion.models import IngestionBatch as IB
        from datetime import datetime as dt, timezone

        batch = db.get(IB, _uuid.UUID(batch_id))
        if batch:
            if cancelled:
                batch.status = "cancelled"
                batch.finished_at = dt.now(timezone.utc)
                batch.error_summary = "用户手动取消"
            elif failed:
                batch.status = "failed"
                batch.finished_at = dt.now(timezone.utc)
                batch.error_summary = f"重试 {max_retries} 次后仍失败"
                _pub(0, "重试耗尽，任务失败", "failed")
            else:
                batch.status = "success" if fail_rows == 0 else "partial_success"
                batch.record_count = total_rows
                batch.success_count = total_rows - fail_rows
                batch.fail_count = fail_rows
                batch.finished_at = dt.now(timezone.utc)
                if fail_rows > 0:
                    batch.error_summary = f"{fail_rows} 行格式异常，已跳过"
                _pub(100, "同步完成" if fail_rows == 0 else f"完成 ({fail_rows} 行跳过)", "success")
            db.commit()
            logger.info("同步%s: batch=%s", "已取消" if cancelled else "失败" if failed else "完成", batch_id[:8])
    finally:
        db.close()
        if _pubsub:
            _pubsub.unsubscribe(_ctrl_channel)
            _pubsub.close()


def _fail_batch(batch_id: str, reason: str, task_short: str = ""):
    """标记批次失败并推送 SSE 失败事件（用于前置校验失败）。"""
    import json as _j, logging as _log
    import uuid as _uuid
    from app.modules.ingestion.services.sync_database import get_sync_db as _gsdb
    from app.modules.ingestion.models import IngestionBatch as IB
    from datetime import datetime as dt, timezone

    _db = _gsdb()
    try:
        b = _db.get(IB, _uuid.UUID(batch_id))
        if b:
            b.status = "failed"
            b.finished_at = dt.now(timezone.utc)
            b.error_summary = reason
            _db.commit()
    finally:
        _db.close()

    try:
        from app.core.queue import redis_conn as _r
        _r.publish(f"batch:{batch_id}:progress", _j.dumps({"pct": 0, "step": reason, "status": "failed"}))
    except Exception:
        pass

    _log.getLogger(__name__).warning("前置失败: batch=%s %s", batch_id[:8] if batch_id else '-', reason)
