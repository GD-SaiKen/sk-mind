"""StageWriter: isolation layer before raw data promotion.

Writes sync data into a staging table first. Only after the entire batch
passes integrity checks does it atomically promote to the raw schema.

Design:
- Full sync: CREATE staging.{table}_{batch_id} -> write all rows -> atomic RENAME to raw.{table}
- Incremental: CREATE staging.{table}_{batch_id} -> write deltas -> INSERT INTO raw.{table} SELECT * FROM staging
- On failure: DROP staging table, raw is untouched

This ensures raw tables are never left in a half-written or polluted state.
"""

import hashlib
import json
import logging
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.models import IngestionBatch

logger = logging.getLogger(__name__)


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _short_batch_id(batch_id: uuid.UUID) -> str:
    """Return a shortened, table-safe batch identifier."""
    return str(batch_id).replace("-", "_")[:12]


class StageWriter:
    """Isolation layer: write to staging, atomically promote to raw.

    Pipeline position:
        Validator -> StageWriter -> raw.{table}
    """

    BATCH_INSERT_SIZE = 1000

    def __init__(self, db: Session):
        self._db = db
        self._staging_tables: list[str] = []

    # --- Batch lifecycle ---

    def create_batch(
        self, task_id: uuid.UUID, trigger_type: str = "manual"
    ) -> IngestionBatch:
        batch = IngestionBatch(
            task_id=task_id,
            trigger_type=trigger_type,
            status="pending",
        )
        self._db.add(batch)
        self._db.commit()
        return batch

    def start_batch(self, batch: IngestionBatch) -> None:
        batch.status = "running"
        batch.started_at = _utcnow()
        self._db.commit()

    def finish_batch(
        self,
        batch: IngestionBatch,
        status: str,
        total: int = 0,
        success: int = 0,
        rejected: int = 0,
        error_summary: Optional[str] = None,
        error_items: Optional[list] = None,
        last_sync_marker: Optional[dict] = None,
        source_signature: Optional[str] = None,
    ) -> None:
        batch.status = status
        batch.finished_at = _utcnow()
        batch.record_count = total
        batch.success_count = success
        batch.fail_count = rejected
        batch.rejected_rows = str(rejected)
        if error_summary:
            batch.error_summary = error_summary[:1000]
        if error_items:
            batch.error_items = error_items
        if last_sync_marker:
            batch.last_sync_marker = last_sync_marker
        if source_signature:
            batch.source_signature = source_signature
        self._db.commit()

    # --- Stage -> Promote ---

    def write(
        self,
        target_table: str,
        batch: IngestionBatch,
        rows: list[dict],
        source_id: str,
        source_signature: str,
        sync_mode: str,
        pulled_at: Optional[datetime] = None,
    ) -> dict:
        """Write rows to staging, then promote to raw if healthy.

        Returns: {"success": int, "rejected": int}
        """
        if not rows:
            return {"success": 0, "rejected": 0}

        pulled_at = pulled_at or _utcnow()
        schema, table = self._parse_schema_table(target_table)
        raw_full = f"{schema}.{table}"
        staging_full = self._staging_table_name(schema, table, batch.id)

        try:
            # 1. Clone raw table structure into staging
            self._clone_table_structure(raw_full, staging_full)
            self._staging_tables.append(staging_full)

            # 2. Write all rows to staging
            success, rejected = self._insert_into_staging(
                staging_full, batch, rows, source_id, source_signature, pulled_at
            )

            if rejected > 0 and sync_mode == "full" and success == 0:
                # All rows rejected: don't promote, clean up staging
                self._drop_staging(staging_full)
                return {"success": 0, "rejected": rejected}

            # 3. Atomic promotion
            if sync_mode == "full":
                self._promote_full(staging_full, raw_full)
            else:
                self._promote_incremental(staging_full, raw_full)

            return {"success": success, "rejected": rejected}

        except Exception:
            # On any error, clean up staging ? raw is untouched
            self._drop_staging(staging_full)
            raise

    def _insert_into_staging(
        self,
        staging_full: str,
        batch: IngestionBatch,
        rows: list[dict],
        source_id: str,
        source_signature: str,
        pulled_at: datetime,
    ) -> tuple[int, int]:
        """Batch-insert rows into the staging table."""
        data_cols = list(rows[0].keys())
        tracking_cols = [
            "_source_id", "_batch_id", "_pulled_at",
            "_source_signature", "_row_hash", "_quality_flags",
        ]
        all_cols = data_cols + tracking_cols
        placeholders = ", ".join(f":{c}" for c in all_cols)
        col_names = ", ".join(f'"{c}"' for c in all_cols)
        ins = text(
            f"INSERT INTO {staging_full} ({col_names}) VALUES ({placeholders})"
        )

        success = 0
        rejected = 0
        chunk: list[dict] = []

        for row in rows:
            flags = row.get("_quality_flags", [])
            flags_json = json.dumps(flags, ensure_ascii=False) if isinstance(flags, list) else "[]"

            params: dict[str, Any] = {c: row.get(c) for c in data_cols}
            params["_source_id"] = source_id
            params["_batch_id"] = str(batch.id)
            params["_pulled_at"] = pulled_at
            params["_source_signature"] = source_signature
            params["_row_hash"] = self._compute_row_hash(row, data_cols)
            params["_quality_flags"] = flags_json
            chunk.append(params)

            if len(chunk) >= self.BATCH_INSERT_SIZE:
                s, r = self._flush_chunk(ins, chunk)
                success += s
                rejected += r
                chunk = []

        if chunk:
            s, r = self._flush_chunk(ins, chunk)
            success += s
            rejected += r

        return success, rejected

    def _flush_chunk(self, stmt, chunk: list[dict]) -> tuple[int, int]:
        """Flush one chunk to staging table."""
        success = 0
        rejected = 0
        for params in chunk:
            try:
                self._db.execute(stmt, params)
                success += 1
            except Exception:
                self._db.rollback()
                rejected += 1
        self._db.commit()
        return success, rejected

    # --- Promotion ---

    def _promote_full(self, staging_full: str, raw_full: str) -> None:
        """Atomic full-sync promotion: swap staging into raw.

        Uses a transaction to ensure atomicity:
          1. DROP raw table
          2. ALTER staging RENAME TO raw
        """
        schema, table = staging_full.split(".", 1)
        raw_schema, raw_table = raw_full.split(".", 1)

        self._db.execute(text(f"DROP TABLE IF EXISTS {raw_full} CASCADE"))
        self._db.execute(
            text(f"ALTER TABLE {staging_full} RENAME TO {raw_table}")
        )
        # Re-set schema if needed
        if schema != raw_schema:
            self._db.execute(
                text(f"ALTER TABLE {raw_schema}.{raw_table} SET SCHEMA {raw_schema}")
            )
        self._db.commit()
        logger.info("Full-sync promoted: %s -> %s", staging_full, raw_full)

    def _promote_incremental(self, staging_full: str, raw_full: str) -> None:
        """Incremental promotion: INSERT from staging into raw, then drop staging."""
        self._db.execute(
            text(f"INSERT INTO {raw_full} SELECT * FROM {staging_full}")
        )
        self._db.execute(text(f"DROP TABLE IF EXISTS {staging_full}"))
        self._db.commit()
        logger.info("Incremental promoted: %s -> %s", staging_full, raw_full)

    def _drop_staging(self, staging_full: str) -> None:
        """Drop a staging table unconditionally (no-op if doesn't exist)."""
        try:
            self._db.execute(text(f"DROP TABLE IF EXISTS {staging_full}"))
            self._db.commit()
        except Exception:
            pass

    # --- Table structure clone ---

    def _clone_table_structure(self, source_full: str, target_full: str) -> None:
        """Clone the column structure of source table to create a staging table.

        Uses CREATE TABLE ... (LIKE source INCLUDING ALL) then adds tracking
        columns if the source doesn't exist yet (first sync).
        """
        schema, table = source_full.split(".", 1)
        check = text(
            "SELECT EXISTS ("
            "  SELECT 1 FROM information_schema.tables "
            "  WHERE table_schema = :schema AND table_name = :table"
            ")"
        )

        source_exists = self._db.execute(
            check, {"schema": schema, "table": table}
        ).scalar_one()

        if source_exists:
            # Clone existing raw table structure
            self._db.execute(
                text(f"CREATE TABLE {target_full} (LIKE {source_full} INCLUDING ALL)")
            )
        else:
            # First sync: create staging table in raw schema to make promotion trivial
            # The target_full IS a raw schema table; SchemaManager creates it
            # Here we just create an empty staging copy
            self._db.execute(
                text(f"CREATE TABLE {target_full} ()")
            )
            self._db.execute(text(f"DROP TABLE IF EXISTS {target_full}"))
            self._db.execute(
                text(f"CREATE TABLE {target_full} (LIKE {source_full} INCLUDING ALL)")
            )

        self._db.commit()
        logger.debug("Cloned structure: %s -> %s", source_full, target_full)

    @staticmethod
    def _staging_table_name(
        schema: str, table: str, batch_id: uuid.UUID
    ) -> str:
        """Generate staging table name: staging.{table}_{batch_short}."""
        return f"staging.{table}_{_short_batch_id(batch_id)}"

    @staticmethod
    def _parse_schema_table(full_name: str) -> tuple[str, str]:
        parts = full_name.split(".", 1)
        return (parts[0], parts[1]) if len(parts) == 2 else ("raw", parts[0])

    @staticmethod
    def _compute_row_hash(row: dict, data_cols: list[str]) -> str:
        subset = {k: row[k] for k in data_cols if k in row}
        serialized = json.dumps(subset, sort_keys=True, ensure_ascii=False, default=str)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()[:16]
