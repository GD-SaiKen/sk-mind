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
    """RQ 任务：模拟同步（验证端到端链路）。

    不做真实数据同步，只是模拟一个耗时的批量写入操作，
    用于验证：创建任务 → 提交执行 → Worker 拉取 → 批次更新 的完整链路。
    """
    import time
    import uuid as _uuid

    logger.info("Echo 同步开始: task_id=%s, batch_id=%s, task_name=%s", task_id, batch_id, task_name)

    # 模拟耗时的同步操作
    time.sleep(2)

    # 更新批次状态为成功
    from app.modules.ingestion.services.sync_database import get_sync_db
    db = get_sync_db()
    try:
        from app.modules.ingestion.models import IngestionBatch as IB
        batch = db.get(IB, _uuid.UUID(batch_id))
        if batch:
            batch.status = "success"
            batch.record_count = 100
            batch.success_count = 100
            batch.fail_count = 0
            batch.finished_at = __import__("datetime").datetime.now(
                __import__("datetime").timezone.utc
            )
            db.commit()
            logger.info("Echo 同步完成: batch_id=%s", batch_id)
    finally:
        db.close()
