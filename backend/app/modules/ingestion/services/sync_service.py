"""Sync orchestration service (RQ Worker side) --- Fetcher -> SchemaManager -> Validator -> RawWriter pipeline.

Corresponds to the design doc: 2026-07-16-??????-design .
"""

import hashlib
import json
import logging
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy.orm import Session

from app.modules.ingestion.fetchers.base import (
    BaseFetcher, SyncConfig, FetcherMeta,
)
from app.modules.ingestion.fetchers.bridge_adapter import (
    BridgeAdapter, BridgeCommand, PlaceholderBridgeAdapter,
)
from app.modules.ingestion.models import IngestionBatch, IngestionTask
from app.modules.ingestion.stage_writer import StageWriter
from app.modules.ingestion.schema_manager import SchemaManager
from app.modules.ingestion.validator import ColumnRule, ValidationLevel, Validator
from app.modules.ingestion.services.sync_database import get_sync_db

logger = logging.getLogger(__name__)


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class SyncService:
    """Unified sync pipeline: Fetcher -> SchemaManager -> Validator -> RawWriter.

    Runs inside an RQ Worker; all database operations use a sync Session.
    """

    def __init__(self, db: Optional[Session] = None):
        self._db = db or get_sync_db()
        self._schema_mgr = SchemaManager(self._db)
        self._writer = StageWriter(self._db)

    # --- Public entry point ---

    def execute_task(
        self,
        task_id: uuid.UUID,
        rq_job=None,
    ) -> dict:
        """Execute a single SyncTask through the full pipeline.

        Steps:
        1. Load task + create batch
        2. Build Fetcher + SyncConfig
        3. Fetcher.fetch() -> streaming row iterator + metadata
        4. SchemaManager ensure/comparison
        5. Validator per-row: L1 REJECT / L2 WARN / PASS
        6. RawWriter batch write with tracking columns
        7. Write-back last_sync_marker + update batch status
        """
        # 1. Load task
        task = self._db.get(IngestionTask, task_id)
        if not task:
            raise ValueError(f"Task not found: {task_id}")

        batch = self._writer.create_batch(task_id, "manual")
        self._writer.start_batch(batch)
        self._update_progress(rq_job, 0, f"Starting: {task.name}")

        total_success = 0
        total_rejected = 0
        error_items: list[dict] = []

        try:
            # 2. Build Fetcher
            fetcher = self._build_fetcher(task)
            config = self._build_sync_config(task)

            # 3. Fetch
            self._update_progress(rq_job, 10, "Fetching data...")
            rows, meta = fetcher.fetch(config)
            self._update_progress(
                rq_job, 30, f"Fetched {meta.total_rows or '?'} rows"
            )

            # 4. Schema management
            self._update_progress(rq_job, 40, "Managing schema...")
            schema, table = self._parse_schema_table(task.target_table or "raw.default")
            self._schema_mgr.ensure_table(
                schema, table,
                source_id=str(task.data_source_id),
                columns=self._columns_from_meta(meta),
            )

            # Check for structural changes (skip on first run)
            changes = self._schema_mgr.check_schema(
                schema, table,
                columns=self._columns_from_meta(meta),
            )
            if changes:
                msg = f"Schema change detected: {len(changes)} columns changed"
                self._writer.finish_batch(
                    batch, "failed", error_summary=msg,
                )
                return {"status": "failed", "reason": "schema_changed", "changes": len(changes)}

            # 5. Validate rows
            self._update_progress(rq_job, 50, "Validating rows...")
            rules = self._build_column_rules(task)
            validator = Validator(rules)
            validated_rows: list[dict] = []

            row_count = 0
            for row in rows:
                row_count += 1
                result = validator.validate(row)
                if result.level == ValidationLevel.REJECT:
                    total_rejected += 1
                    error_items.append({
                        "row_index": row_count,
                        "source_signature": meta.source_signature,
                        "error_type": "L1_reject",
                        "error_message": "; ".join(result.errors),
                    })
                else:
                    mapped = dict(result.mapped_row)
                    mapped["_quality_flags"] = result.quality_flags
                    validated_rows.append(mapped)
                    total_success += 1

                if row_count % 5000 == 0:
                    self._update_progress(
                        rq_job,
                        50 + min(30, int(row_count / max(meta.total_rows or 1, 1) * 30)),
                        f"Validated {row_count} rows",
                    )

            # 6. Write to staging -> atomic promote to raw
            self._update_progress(rq_job, 80, "Writing to staging layer...")
            write_result = self._writer.write(
                table_name=f"{schema}.{table}",
                batch=batch,
                rows=validated_rows,
                source_id=str(task.data_source_id),
                source_signature=meta.source_signature,
                sync_mode=config.sync_mode,
                pulled_at=meta.pulled_at,
            )
            total_success = write_result["success"]
            total_rejected += write_result["rejected"]

            # 7. Determine last_sync_marker
            last_marker = self._compute_sync_marker(config, rows)

            # 8. Finish batch
            final_status = (
                "success" if total_rejected == 0 else "partial_success"
            )
            self._writer.finish_batch(
                batch,
                status=final_status,
                total=total_success + total_rejected,
                success=total_success,
                rejected=total_rejected,
                error_items=error_items if error_items else None,
                last_sync_marker=last_marker,
                source_signature=meta.source_signature,
            )

            self._update_progress(rq_job, 100, "Sync complete")
            return {
                "status": final_status,
                "total": total_success + total_rejected,
                "success": total_success,
                "rejected": total_rejected,
            }

        except Exception as e:
            logger.exception("Sync failed for task %s", task_id)
            self._writer.finish_batch(
                batch,
                status="failed",
                error_summary=str(e)[:1000],
                error_items=error_items if error_items else None,
            )
            raise

    # --- Fetcher factory ---

    def _build_fetcher(self, task: IngestionTask) -> BaseFetcher:
        """Build the appropriate Fetcher based on task configuration."""
        from app.modules.ingestion.fetchers.bridge_adapter import BridgeAdapter

        category = task.source_category or "database"

        # For now, SQL Server is the only DB type and uses bridge mode
        if category == "database":
            return _BridgeFetcher(
                adapter=PlaceholderBridgeAdapter(
                    bridge_url=(task.fetch_config or {}).get("bridge_url", "")
                )
            )
        else:
            raise ValueError(f"Unsupported source_category: {category}")

    def _build_sync_config(self, task: IngestionTask) -> SyncConfig:
        """Build SyncConfig from the task's fetch_config."""
        fc = task.fetch_config or {}
        return SyncConfig(
            source_type=task.source_category or "database",
            sync_mode=task.sync_mode or "full",
            source_sql=fc.get("source_sql"),
            table_name=fc.get("table_name") or task.target_table,
            timestamp_column=fc.get("timestamp_column"),
            cursor_column=fc.get("cursor_column"),
            batch_size=fc.get("batch_size", 1000),
            last_sync_marker=task.last_sync_marker,
            bridge_url=fc.get("bridge_url"),
            schema=fc.get("schema", "dbo"),
        )

    def _build_column_rules(self, task: IngestionTask) -> list[ColumnRule]:
        """Build ColumnRule list from the task's column_rules config."""
        cr = task.column_rules or []
        return [ColumnRule(**rule) for rule in cr]

    @staticmethod
    def _columns_from_meta(meta: FetcherMeta) -> list[dict]:
        """Convert FetcherMeta.columns to the format SchemaManager expects."""
        return [
            {"name": c, "data_type": "nvarchar", "is_nullable": True}
            for c in meta.columns
        ]

    @staticmethod
    def _compute_sync_marker(
        config: SyncConfig, rows: list[dict],
    ) -> Optional[dict]:
        """Compute the last_sync_marker from the pulled data."""
        if config.sync_mode == "timestamp" and config.timestamp_column:
            values = [
                row.get(config.timestamp_column)
                for row in rows
                if row.get(config.timestamp_column) is not None
            ]
            if values:
                return {"last_timestamp": str(max(values))}
        elif config.sync_mode == "cursor" and config.cursor_column:
            values = [
                row.get(config.cursor_column)
                for row in rows
                if row.get(config.cursor_column) is not None
            ]
            if values:
                return {"last_cursor_id": max(values)}
        return None

    @staticmethod
    def _parse_schema_table(full_name: str) -> tuple[str, str]:
        parts = full_name.split(".", 1)
        if len(parts) == 2:
            return parts[0], parts[1]
        return "raw", parts[0]

    @staticmethod
    def _update_progress(rq_job, progress: int, step: str) -> None:
        if rq_job:
            rq_job.meta["progress"] = progress
            rq_job.meta["step"] = step
            rq_job.save_meta()


# --- Internal bridge-based Fetcher ---

class _BridgeFetcher(BaseFetcher):
    """Fetcher that delegates to a BridgeAdapter for SQL Server access.

    This is an internal implementation. It is replaced once the real bridge
    script is ready (Phase B).
    """

    def __init__(self, adapter: BridgeAdapter):
        self._adapter = adapter

    def fetch(self, config: SyncConfig) -> tuple[list[dict], FetcherMeta]:
        cmd = BridgeCommand(
            source_sql=config.source_sql or f"SELECT * FROM {config.table_name}",
            sync_mode=config.sync_mode,
            batch_size=config.batch_size,
            timestamp_column=config.timestamp_column,
            cursor_column=config.cursor_column,
            last_sync_marker=config.last_sync_marker,
            schema=config.schema,
        )
        rows = self._adapter.execute(cmd)
        columns = list(rows[0].keys()) if rows else []
        meta = FetcherMeta(
            total_rows=len(rows),
            columns=columns,
            source_signature=(
                f"sqlserver://{getattr(self._adapter, '_bridge_url', 'placeholder')}"
                f"/{config.schema or 'dbo'}.{config.table_name}"
            ),
            pulled_at=_utcnow(),
        )
        return rows, meta

    def test_connection(self, config: SyncConfig) -> bool:
        return self._adapter.health_check()


# --- Legacy SyncService (kept for backward compat with existing RQ workers) ---

class _LegacySyncService:
    """Legacy sync service for existing connector-based sync flows.

    Used by run_full_sync / run_api_pull legacy entry points.
    Will be removed after all tasks migrate to sync engine v2.
    """

    def __init__(self):
        from app.modules.ingestion.services.sync_database import get_sync_db
        self._db = get_sync_db()

    def execute_full_sync(
        self,
        task_id,
        source_object_name,
        connector,
        raw_table_name,
        rq_job=None,
    ) -> dict:
        import hashlib, json
        from datetime import datetime, timezone
        from sqlalchemy import text
        from app.modules.ingestion.models import IngestionBatch, ImportError

        def _now():
            return datetime.now(timezone.utc)

        batch = IngestionBatch(task_id=task_id, trigger_type="manual", status="pending")
        self._db.add(batch)
        self._db.commit()

        batch.status = "running"
        batch.started_at = _now()
        self._db.commit()

        try:
            columns = connector.fetch_schema(source_object_name)
            from app.modules.ingestion.connectors.sqlserver import SqlServerConnector

            schema, tbl = self._parse(raw_table_name)
            check = text(
                "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema=:s AND table_name=:t)"
            )
            exists = self._db.execute(check, {"s": schema, "t": tbl}).scalar_one()
            if not exists:
                col_defs = []
                for c in columns:
                    pg = SqlServerConnector.TYPE_MAP.get(c.data_type.lower().split("(")[0].strip(), "TEXT")
                    col_defs.append(f'    "{c.name}" {pg}{"" if c.is_nullable else " NOT NULL"}')
                tracking = [
                    '    "_batch_id" VARCHAR(64) NOT NULL',
                    '    "_source_system" VARCHAR(64) NOT NULL',
                    '    "_source_object" VARCHAR(256) NOT NULL',
                    '    "_source_row_hash" VARCHAR(64) NOT NULL',
                    '    "_ingested_at" TIMESTAMPTZ NOT NULL DEFAULT NOW()',
                ]
                ddl = f"CREATE TABLE {raw_table_name} ("
                ddl += ",\n".join(col_defs + tracking)
                ddl += "\n)"
                self._db.execute(text(ddl))
                self._db.execute(text(ddl))
                self._db.commit()

            total = connector.count_rows(source_object_name)
            batch_sz = min(10000, max(1000, total // 10)) if total > 0 else 1000
            offset = 0
            success = 0
            failed = 0

            def _hash(d):
                s = json.dumps(d, sort_keys=True, ensure_ascii=False, default=str)
                return hashlib.sha256(s.encode()).hexdigest()[:16]

            while offset < total:
                rows = list(connector.fetch_data(source_object_name, offset=offset, limit=batch_sz))
                for row in rows:
                    try:
                        rec = dict(row)
                        rec["_batch_id"] = str(batch.id)
                        rec["_source_system"] = "ERP_E10"
                        rec["_source_object"] = source_object_name
                        rec["_source_row_hash"] = _hash(rec)
                        rec["_ingested_at"] = _now()

                        cols = ", ".join(f'"{k}"' for k in rec)
                        vals = ", ".join(f":{k}" for k in rec)
                        self._db.execute(text(f"INSERT INTO {raw_table_name} ({cols}) VALUES ({vals})"), rec)
                        success += 1
                    except Exception as e:
                        failed += 1
                self._db.commit()
                offset += batch_sz

            batch.record_count = total
            batch.success_count = success
            batch.fail_count = failed
            batch.status = "success" if failed == 0 else "partial_success"
            batch.finished_at = _now()
            self._db.commit()
            return {"total": total, "success": success, "failed": failed}

        except Exception:
            batch.status = "failed"
            batch.finished_at = _now()
            self._db.commit()
            raise

    def execute_api_pull(
        self, task_id, endpoint, method, body, source_system, connector,
        page_size=100, max_pages=None, rq_job=None,
    ) -> dict:
        import json as _j
        from datetime import datetime, timezone
        from sqlalchemy import text
        from app.modules.ingestion.models import IngestionBatch, ImportError

        def _now():
            return datetime.now(timezone.utc)

        batch = IngestionBatch(task_id=task_id, trigger_type="manual", status="pending")
        self._db.add(batch)
        self._db.commit()

        batch.status = "running"
        batch.started_at = _now()
        self._db.commit()

        try:
            success = 0
            failed = 0

            for page_records in connector.fetch_all_pages(
                endpoint, method=method, body=body, page_size=page_size, max_pages=max_pages,
            ):
                if not isinstance(page_records, list):
                    page_records = [page_records]
                for record in page_records:
                    if not isinstance(record, dict):
                        failed += 1
                        continue
                    try:
                        table_name = f"raw.{source_system.lower()}_{endpoint}"
                        schema, tbl = self._parse(table_name)
                        check = text(
                            "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema=:s AND table_name=:t)"
                        )
                        exists = self._db.execute(check, {"s": schema, "t": tbl}).scalar_one()
                        if not exists:
                            ddl = text(
                                f"CREATE TABLE {table_name} ("
                                "  _raw_id BIGSERIAL PRIMARY KEY,"
                                "  _batch_id VARCHAR(64) NOT NULL,"
                                "  _source_system VARCHAR(64) NOT NULL,"
                                "  _source_object VARCHAR(256) NOT NULL,"
                                "  _source_row_hash VARCHAR(64) NOT NULL,"
                                "  _api_url VARCHAR(512) NOT NULL,"
                                "  _api_request_params JSONB,"
                                "  _api_response_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),"
                                "  _ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),"
                                "  payload JSONB NOT NULL"
                                ")"
                            )
                            self._db.execute(ddl)
                            self._db.commit()
                        import hashlib
                        h = hashlib.sha256(_j.dumps(record, sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()[:16]
                        self._db.execute(text(
                            f"INSERT INTO {table_name} "
                            "(_batch_id, _source_system, _source_object, _source_row_hash, _api_url, _api_request_params, _api_response_at, _ingested_at, payload) "
                            "VALUES (:bid, :ss, :so, :h, :url, :rp, :at, :now, :p) "
                            "ON CONFLICT (_batch_id, _source_row_hash) DO NOTHING"
                        ), {
                            "bid": str(batch.id), "ss": source_system, "so": endpoint,
                            "h": h, "url": endpoint,
                            "rp": _j.dumps(body or {}), "at": _now(), "now": _now(),
                            "p": _j.dumps(record, ensure_ascii=False)
                        })
                        success += 1
                    except Exception:
                        failed += 1
                self._db.commit()

            total = success + failed
            batch.record_count = total
            batch.success_count = success
            batch.fail_count = failed
            batch.status = "success" if failed == 0 else "partial_success"
            batch.finished_at = _now()
            self._db.commit()
            return {"total": total, "success": success, "failed": failed}
        except Exception:
            batch.status = "failed"
            batch.finished_at = _now()
            self._db.commit()
            raise

    @staticmethod
    def _parse(full: str):
        p = full.split(".", 1)
        return (p[0], p[1]) if len(p) == 2 else ("raw", p[0])
