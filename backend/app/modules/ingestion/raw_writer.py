"""RawWriter: writes validated rows into raw schema physical tables with batch lifecycle.

Responsibilities:
- Batch lifecycle management (create / update / finalise)
- Batch INSERT with automatic tracking-column population
- Full-sync: TRUNCATE + INSERT; Incremental: INSERT with row-hash dedup
"""

import hashlib
import json
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.models import IngestionBatch


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class RawWriter:
    """Writes rows into raw schema tables and manages batch lifecycle."""

    BATCH_INSERT_SIZE = 1000

    def __init__(self, db: Session):
        self._db = db

    # --- Batch lifecycle ---

    def create_batch(
        self,
        task_id: uuid.UUID,
        trigger_type: str = "manual",
    ) -> IngestionBatch:
        """Create a new execution batch in 'pending' status."""
        batch = IngestionBatch(
            task_id=task_id,
            trigger_type=trigger_type,
            status="pending",
        )
        self._db.add(batch)
        self._db.commit()
        return batch

    def start_batch(self, batch: IngestionBatch) -> None:
        """Transition batch to 'running'."""
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
        """Finalise batch with statistics and status."""
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

    # --- Write ---

    def write(
        self,
        table_name: str,
        batch: IngestionBatch,
        rows: list[dict],
        source_id: str,
        source_signature: str,
        sync_mode: str,
        pulled_at: Optional[datetime] = None,
        hash_exclude_fields: Optional[list[str]] = None,
    ) -> dict:
        """Write a batch of rows to the raw table.

        Full sync: TRUNCATE then INSERT.
        Incremental: INSERT with dedup via ON CONFLICT based on _row_hash.
        Returns: {"success": int, "rejected": int}.
        """
        if not rows:
            return {"success": 0, "rejected": 0}

        pulled_at = pulled_at or _utcnow()

        # Full sync: truncate first
        if sync_mode == "full":
            self._db.execute(text(f"TRUNCATE TABLE {table_name}"))
            self._db.commit()

        success = 0
        rejected = 0

        for i in range(0, len(rows), self.BATCH_INSERT_SIZE):
            chunk = rows[i : i + self.BATCH_INSERT_SIZE]
            s, r = self._insert_chunk(
                table_name, batch, chunk, source_id,
                source_signature, pulled_at, sync_mode, hash_exclude_fields,
            )
            success += s
            rejected += r

        return {"success": success, "rejected": rejected}

    def _insert_chunk(
        self,
        table_name: str,
        batch: IngestionBatch,
        rows: list[dict],
        source_id: str,
        source_signature: str,
        pulled_at: datetime,
        sync_mode: str,
        hash_exclude_fields: Optional[list[str]] = None,
    ) -> tuple[int, int]:
        """Insert a chunk of up to BATCH_INSERT_SIZE rows."""
        if not rows:
            return 0, 0

        data_cols = list(rows[0].keys())
        tracking_cols = [
            "_source_id", "_batch_id", "_pulled_at",
            "_source_signature", "_row_hash", "_quality_flags",
        ]
        all_cols = data_cols + tracking_cols

        placeholders = ", ".join(f":{c}" for c in all_cols)
        col_names = ", ".join(f'"{c}"' for c in all_cols)

        ins = text(
            f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"
        )

        success = 0
        rejected = 0

        for row in rows:
            quality_flags = row.get("_quality_flags", [])
            if isinstance(quality_flags, list):
                quality_flags_json = json.dumps(quality_flags, ensure_ascii=False)
            else:
                quality_flags_json = "[]"

            params: dict[str, Any] = {c: row.get(c) for c in data_cols}
            params["_source_id"] = source_id
            params["_batch_id"] = str(batch.id)
            params["_pulled_at"] = pulled_at
            params["_source_signature"] = source_signature
            params["_row_hash"] = self._compute_row_hash(row, data_cols, hash_exclude_fields)
            params["_quality_flags"] = quality_flags_json

            try:
                self._db.execute(ins, params)
                success += 1
            except Exception:
                self._db.rollback()
                rejected += 1

        self._db.commit()
        return success, rejected

    @staticmethod
    def _compute_row_hash(
        row: dict, data_cols: list[str], exclude_cols: Optional[list[str]] = None
    ) -> str:
        """SHA-256 hash of business columns, excluding tracking + ``exclude_cols``.

        ``exclude_cols`` lets an interface drop volatile tracking fields (e.g.
        ``update_time``) from the dedup hash so a server-side timestamp refresh
        does not masquerade as a real business change.
        """
        subset = {
            k: row[k]
            for k in data_cols
            if k in row and (not exclude_cols or k not in exclude_cols)
        }
        serialized = json.dumps(subset, sort_keys=True, ensure_ascii=False, default=str)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()[:16]
