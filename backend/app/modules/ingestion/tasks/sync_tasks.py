"""RQ Worker task entry points for the sync engine.

Corresponds to: 04-???????? .

New entry points for sync engine v2:
- run_sync_task: unified pipeline (Fetcher -> SchemaManager -> Validator -> RawWriter)

Legacy entry points kept for backward compat:
- run_full_sync: database full sync
- run_api_pull: API pull sync
- run_echo_sync: mock sync for testing
"""

import logging
import os
import uuid
from pathlib import Path

from rq import get_current_job

# Load .env for RQ worker process (env vars needed by sync engine connectors)
_env_path = Path(__file__).resolve().parents[4] / ".env"
if _env_path.exists():
    try:
        from dotenv import load_dotenv
        load_dotenv(_env_path)
    except ImportError:
        pass

from app.modules.ingestion.services.sync_service import SyncService

logger = logging.getLogger(__name__)


# --- Sync engine v2 entry point ---


def run_sync_task(task_id: str):
    """Execute a single SyncTask through the unified sync pipeline.

    This is the primary entry point for sync engine v2.
    It replaces the old run_full_sync / run_api_pull split.

    Args:
        task_id: Task ID (UUID string).
    """
    job = get_current_job()
    task_uuid = uuid.UUID(task_id)

    try:
        service = SyncService()
        result = service.execute_task(task_id=task_uuid, rq_job=job)
        logger.info("Sync complete: task=%s result=%s", task_id[:8], result)

    except Exception as e:
        logger.exception("Sync failed: task=%s", task_id)
        raise


# --- Legacy entry points (kept for backward compatibility) ---


def run_full_sync(
    task_id: str,
    source_object_name: str,
    connector_config: dict,
    raw_table_name: str,
):
    """Legacy: execute database full sync via direct connector.

    Args:
        task_id: Task ID (UUID string).
        source_object_name: Source table name.
        connector_config: Connector config dict.
        raw_table_name: Target raw table name.
    """
    job = get_current_job()
    task_uuid = uuid.UUID(task_id)

    try:
        from app.modules.ingestion.services.connector_service import ConnectorService
        from app.modules.ingestion.services.sync_database import get_sync_db

        connector = ConnectorService.create_sqlserver(connector_config)
        connector.connect()

        # Use the legacy SyncService method
        from app.modules.ingestion.services.sync_service import _LegacySyncService
        service = _LegacySyncService()
        result = service.execute_full_sync(
            task_id=task_uuid,
            source_object_name=source_object_name,
            connector=connector,
            raw_table_name=raw_table_name,
            rq_job=job,
        )
        logger.info("Full sync complete: %s", result)

    except Exception as e:
        logger.exception("Full sync failed: task=%s, table=%s", task_id, source_object_name)
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
    """Legacy: execute API pull sync.

    Args:
        task_id: Task ID (UUID string).
        endpoint: API endpoint.
        method: HTTP method.
        body: Request body template.
        source_system: Source system identifier.
        connector_config: Connector config dict.
        page_size: Records per page.
        max_pages: Maximum pages to fetch.
    """
    job = get_current_job()
    task_uuid = uuid.UUID(task_id)

    try:
        from app.modules.ingestion.services.connector_service import ConnectorService
        from app.modules.ingestion.services.sync_service import _LegacySyncService

        connector = ConnectorService.create_api(connector_config)
        connector.connect()

        service = _LegacySyncService()
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
        logger.info("API pull complete: %s", result)

    except Exception as e:
        logger.exception("API pull failed: task=%s, endpoint=%s", task_id, endpoint)
        raise
    finally:
        if "connector" in locals():
            connector.disconnect()


def run_echo_sync(task_id: str, batch_id: str, task_name: str):
    """Legacy: mock sync for testing connectivity and flow."""
    import json
    import time
    import random
    import uuid as _uuid

    job = get_current_job()

    # Data source validation
    task_uuid = _uuid.UUID(task_id)
    from app.modules.ingestion.services.sync_database import get_sync_db
    _db = get_sync_db()
    try:
        from app.modules.ingestion.models import IngestionTask as IT
        from app.modules.data_sources.models import DataSource
        _task = _db.get(IT, task_uuid)
        if _task and _task.data_source_id:
            _ds = _db.get(DataSource, _task.data_source_id)
            ds_name = _ds.name if _ds else "?????"
        else:
            ds_name = None
    finally:
        _db.close()

    if not ds_name:
        _fail_batch(batch_id, "???????????????????? ERP/MES/SRM", task_id[:8])
        return

    logger.info("Sync start: task=%s batch=%s ds=%s", task_id[:8], batch_id[:8], ds_name)

    # Redis pub/sub
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
        if not _pubsub:
            return False
        msg = _pubsub.get_message()
        while msg:
            if msg["type"] == "message" and msg["data"] == b"cancel":
                return True
            msg = _pubsub.get_message()
        return False

    stages = [
        (0, 20, "?????..."),
        (20, 40, "?????..."),
        (40, 70, "?????..."),
        (70, 90, "?? Raw ?..."),
        (90, 100, "??"),
    ]

    total_rows = random.randint(5000, 50000)
    fail_rows = random.randint(0, 3)
    retry_count = 0
    max_retries = 3
    cancelled = False
    failed = False

    for pct_start, pct_end, step in stages:
        time.sleep(random.uniform(0.8, 1.5))
        if _cancelled():
            cancelled = True
            _pub(pct_start, f"??? ({step})", "cancelled")
            break

        if random.random() < 0.15 and retry_count < max_retries:
            retry_count += 1
            _pub(pct_start, f"{step} ???? {retry_count}/{max_retries} ???...", "running")
            time.sleep(1.5)
            if retry_count >= max_retries and random.random() < 0.5:
                failed = True
                _pub(pct_start, f"{step} ???????", "failed")
                break

        _pub(pct_end, f"{step} ({pct_end}%%)")

    # Update batch
    db2 = get_sync_db()
    try:
        from app.modules.ingestion.models import IngestionBatch as IB
        from datetime import datetime as dt, timezone

        batch = db2.get(IB, _uuid.UUID(batch_id))
        if batch:
            if cancelled:
                batch.status = "cancelled"
                batch.finished_at = dt.now(timezone.utc)
                batch.error_summary = "??????"
            elif failed:
                batch.status = "failed"
                batch.finished_at = dt.now(timezone.utc)
                batch.error_summary = f"?? {max_retries} ?????"
                _pub(0, "?????????", "failed")
            else:
                batch.status = "success" if fail_rows == 0 else "partial_success"
                batch.record_count = total_rows
                batch.success_count = total_rows - fail_rows
                batch.fail_count = fail_rows
                batch.finished_at = dt.now(timezone.utc)
                if fail_rows > 0:
                    batch.error_summary = f"{fail_rows} ?????????"
                _pub(100, "????" if fail_rows == 0 else f"?? ({fail_rows} ???)", "success")
            db2.commit()
            logger.info("Sync %s: batch=%s",
                "cancelled" if cancelled else ("failed" if failed else "complete"),
                batch_id[:8])
    finally:
        db2.close()
        if _pubsub:
            _pubsub.unsubscribe(_ctrl_channel)
            _pubsub.close()


def _fail_batch(batch_id: str, reason: str, task_short: str = ""):
    """Mark batch as failed and push SSE failure event."""
    import json as _j
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

    logger.warning("Pre-flight failure: batch=%s %s", batch_id[:8] if batch_id else '-', reason)


def run_api_full_sync(
    task_id: str,
    batch_id: str,
    config_path: str = "",
    interfaces: list[str] | None = None,
    data_source_id: str | None = None,
):
    """Execute API sync via ApiSyncEngine.

    Sync strategy per interface:
    - First sync (no watermark): full pull — paginate all data, no date params.
    - Incremental (watermark exists, is_time_based=True): pull only recent data
      via API date params (start = watermark - replay_days, end = now).
    - Non-time-based interfaces: always full pull.

    Config resolution priority:
    1. If ``config_path`` points to a valid YAML → load YAML (provides interfaces).
    2. If ``data_source_id`` is provided → load DB ``ConnectorConfig``
       (overrides YAML ``connection`` 段).
    3. Merge: DB connection + YAML interfaces; if only one source, use it alone.
    4. If neither exists → error.

    Args:
        task_id: IngestionTask UUID.
        batch_id: Pre-created IngestionBatch UUID (from the router).
        config_path: Optional absolute path to data source YAML config.
        interfaces: optional list of interface names to sync (syncs all if None).
        data_source_id: Optional DataSource UUID — used to load DB connection config.
    """
    import os as _os
    import uuid as _uuid
    from datetime import datetime, timezone
    from pathlib import Path as _Path
    from app.modules.ingestion.engines.api_sync_engine import ApiSyncEngine, load_config
    from app.modules.ingestion.models import IngestionBatch, IngestionTask
    from app.modules.ingestion.services.sync_database import get_sync_db
    from app.modules.ingestion.services.connector_service import build_engine_config
    from app.modules.data_sources.models import DataSource  # register FK table for commit

    task_uuid = _uuid.UUID(task_id)
    batch_uuid = _uuid.UUID(batch_id)

    db = get_sync_db()
    batch = None
    task = None
    try:
        task = db.get(IngestionTask, task_uuid)
        batch = db.get(IngestionBatch, batch_uuid)
        if not task:
            logger.error("Task not found: %s", task_id)
            return
        if not batch:
            logger.error("Batch not found: %s", batch_id)
            return

        # ── Config resolution: YAML (interfaces) + DB (connection) ──

        # Resolve config_path relative to the backend root (parents[4]),
        # NOT the RQ worker's CWD which may be the project root.
        _backend_root = _Path(__file__).resolve().parents[4]

        # 1. Try YAML — provides interfaces + default connection
        yaml_config = None
        if config_path:
            _actual_path = config_path
            # If relative path doesn't resolve from CWD, try from backend root
            if not _os.path.exists(_actual_path):
                _from_backend = _backend_root / config_path
                if _os.path.exists(_from_backend):
                    _actual_path = str(_from_backend)
                    logger.info(
                        "Config path resolved (backend root): %s → %s",
                        config_path, _actual_path,
                    )
            # Case-insensitive filename lookup as fallback
            if not _os.path.exists(_actual_path):
                _dir = _Path(_actual_path).parent
                _filename = _Path(_actual_path).name.lower()
                # Also try from backend root
                if not _os.path.isdir(_dir):
                    _dir_b = _backend_root / _dir
                    if _os.path.isdir(_dir_b):
                        _dir = _dir_b
                if _os.path.isdir(_dir):
                    for _entry in _os.listdir(_dir):
                        if _entry.lower() == _filename:
                            _actual_path = str(_Path(_dir) / _entry)
                            logger.info(
                                "Config path resolved (case-insensitive): %s → %s",
                                config_path, _actual_path,
                            )
                            break
            if _os.path.exists(_actual_path):
                yaml_config = load_config(_actual_path)
                logger.info(
                    "Loaded YAML config: %s (%d interfaces)",
                    _actual_path, len(yaml_config.get("interfaces", [])),
                )

        # 2. Try DB ConnectorConfig — overrides YAML connection
        db_config = None
        _ds_str = data_source_id or (str(task.data_source_id) if task.data_source_id else None)
        if _ds_str:
            try:
                db_config = build_engine_config(db, _uuid.UUID(_ds_str))
            except Exception:
                logger.warning(
                    "Failed to load DB config for source %s", _ds_str, exc_info=True,
                )

        # 3. Merge
        if yaml_config and db_config:
            yaml_config["connection"] = {
                **yaml_config.get("connection", {}),
                **db_config["connection"],
            }
            config = yaml_config
            logger.info("Merged config: YAML interfaces + DB connection override")
        elif yaml_config:
            config = yaml_config
            logger.info("Using YAML-only config (no DB config found)")
        elif db_config:
            config = db_config
            logger.info("Using DB-only config (no YAML — interfaces empty)")
        else:
            raise RuntimeError(
                f"No config available: config_path={config_path!r} not found "
                f"and no DB config for data_source_id={data_source_id}"
            )

        ds_sync_id = task.data_source_id or task_uuid

        engine = ApiSyncEngine(config, db)
        logger.info("Syncing all data for task %s", task_id[:8])
        result = engine.sync_all(
            task_id=task_uuid,
            data_source_id=ds_sync_id,
            interfaces=interfaces,
            batch=batch,
        )

        # Update the router's batch with final stats
        total_success = sum(v["success"] for v in result.values())
        total_rejected = sum(v["rejected"] for v in result.values())
        batch.record_count = total_success + total_rejected
        batch.success_count = total_success
        batch.fail_count = total_rejected
        batch.status = "success" if total_rejected == 0 else "partial_success"
        batch.finished_at = datetime.now(timezone.utc)

        # Update task tracking
        task.last_sync_at = datetime.now(timezone.utc)
        task.last_sync_status = batch.status
        db.commit()

        logger.info("API full sync done: %s (batch %s)", {k: v["success"] for k, v in result.items()}, batch_id[:8])
    except Exception:
        logger.exception("API full sync failed: task=%s batch=%s", task_id[:8], batch_id[:8])
        try:
            db.rollback()  # reset failed transaction before touching expired attrs
        except Exception:
            pass
        # Re-query fresh instances after rollback (old objects are expired)
        try:
            _fresh_batch = db.get(IngestionBatch, batch_uuid)
            if _fresh_batch:
                _fresh_batch.status = "failed"
                _fresh_batch.finished_at = datetime.now(timezone.utc)
        except Exception:
            logger.warning("Failed to update batch status to 'failed'", exc_info=True)
        try:
            _fresh_task = db.get(IngestionTask, task_uuid)
            if _fresh_task:
                _fresh_task.last_sync_status = "failed"
        except Exception:
            logger.warning("Failed to update task last_sync_status", exc_info=True)
        try:
            db.commit()
        except Exception:
            logger.warning("Failed to commit failure status", exc_info=True)
        raise
    finally:
        db.close()
