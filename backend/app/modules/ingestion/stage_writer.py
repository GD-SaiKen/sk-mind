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
        self,
        task_id: uuid.UUID,
        trigger_type: str = "manual",
        triggered_by: str | None = None,
        parent_id: uuid.UUID | None = None,
    ) -> IngestionBatch:
        batch = IngestionBatch(
            task_id=task_id,
            trigger_type=trigger_type,
            triggered_by=triggered_by,
            parent_id=parent_id,
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
        skip: int = 0,
        pulled: int = 0,
    ) -> None:
        batch.status = status
        batch.finished_at = _utcnow()
        # 拉取行数 = 真实从 API 拉取的行数（由引擎透传），无则回退到 success
        batch.record_count = pulled or total
        # 写入行数 = 实际变更（新增 + 更新），不是"交给 writer 的行数"
        batch.success_count = success
        batch.fail_count = rejected
        # 跳过行数 = 已存在且内容未变、被 upsert 跳过写入的行
        batch.skip_count = skip
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
        pk_fields: Optional[list[str]] = None,
    ) -> dict:
        """Write rows to staging, then promote to raw if healthy.

        Returns a truthful accounting of what actually happened to the raw
        table (NOT just how many rows were handed to the writer):

            {
              "success":   int,  # 实际变更行数 = inserted + updated（写入行数）
              "rejected":  int,  # staging 写入被拒（逐行异常）
              "inserted": int,  # 新增行（raw 中原本无此 PK）
              "updated":  int,   # 已存在且内容有变化的行（upsert 覆盖）
              "unchanged":int,   # 已存在且内容完全相同，被跳过（未写入）
            }
        """
        if not rows:
            return {
                "success": 0, "rejected": 0,
                "inserted": 0, "updated": 0, "unchanged": 0,
            }

        pulled_at = pulled_at or _utcnow()
        schema, table = self._parse_schema_table(target_table)
        raw_full = f"{schema}.{table}"
        staging_full = self._staging_table_name(schema, table, batch.id)

        try:
            # 1. Clone raw table structure into staging
            self._clone_table_structure(raw_full, staging_full)
            self._staging_tables.append(staging_full)

            # 2. Write all rows to staging
            staging_success, rejected = self._insert_into_staging(
                staging_full, batch, rows, source_id, source_signature, pulled_at,
                pk_fields=pk_fields,
            )

            if rejected > 0 and sync_mode == "full" and staging_success == 0:
                # All rows rejected: don't promote, clean up staging
                self._drop_staging(staging_full)
                return {
                    "success": 0, "rejected": rejected,
                    "inserted": 0, "updated": 0, "unchanged": 0,
                }

            # 3. Atomic promotion — count what actually landed in raw
            if sync_mode == "upsert" and pk_fields:
                inserted, updated = self._promote_upsert(staging_full, raw_full, pk_fields)
                # 跳过的行 = staging 中既未新增也未更新的行（已存在且内容完全一致）
                unchanged = staging_success - inserted - updated
                if unchanged < 0:
                    unchanged = 0
            elif sync_mode == "full":
                self._promote_full(staging_full, raw_full)
                inserted, updated, unchanged = staging_success, 0, 0
            else:
                self._promote_incremental(staging_full, raw_full)
                inserted, updated, unchanged = staging_success, 0, 0

            return {
                "success": inserted + updated,
                "rejected": rejected,
                "inserted": inserted,
                "updated": updated,
                "unchanged": unchanged,
            }

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
        pk_fields: Optional[list[str]] = None,
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
                s, r = self._flush_chunk(ins, chunk, pk_fields)
                success += s
                rejected += r
                chunk = []

        if chunk:
            s, r = self._flush_chunk(ins, chunk, pk_fields)
            success += s
            rejected += r

        return success, rejected

    def _flush_chunk(self, stmt, chunk: list[dict], pk_fields=None) -> tuple[int, int]:
        """Flush one chunk to staging table. 逐行写入失败的行写入隔离区（write_error）。"""
        success = 0
        rejected = 0
        for params in chunk:
            try:
                self._db.execute(stmt, params)
                success += 1
            except Exception:
                self._db.rollback()
                rejected += 1
                self._quarantine_row(params, pk_fields)
        self._db.commit()
        return success, rejected

    def _quarantine_row(self, params: dict, pk_fields=None) -> None:
        """把 staging 写入失败的行写入 sync_quarantine（reason=write_error）。

        params 含数据列 + 跟踪列（_source_id/_batch_id/_source_signature 等）。
        异常不中断主流程。
        """
        try:
            _tracking = {
                "_source_id", "_batch_id", "_source_signature",
                "_pulled_at", "_row_hash", "_quality_flags",
            }
            raw = {k: v for k, v in params.items() if k not in _tracking}
            pk_value = (
                "|".join(
                    str(params.get(p)) for p in (pk_fields or [])
                    if params.get(p) is not None
                ) or None
            )
            self._db.execute(text(
                """
                INSERT INTO sync_quarantine
                  (id, batch_id, data_source_id, interface_name, pk_value,
                   rejection_reason, raw_json, status, created_at)
                VALUES
                  (gen_random_uuid(), :batch_id, :ds, :iface, :pk,
                   'write_error', :raw, 'pending', now())
                """
            ), {
                "batch_id": params.get("_batch_id"),
                "ds": params.get("_source_id"),
                "iface": params.get("_source_signature"),
                "pk": pk_value,
                "raw": json.dumps(raw, ensure_ascii=False, default=str),
            })
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            logger.warning("隔离区(write_error)写入失败: %s", e)

    # --- Promotion ---

    def _promote_full(self, staging_full: str, raw_full: str) -> None:
        """Atomic full-sync promotion: swap staging into raw.

        Uses a transaction to ensure atomicity:
          1. DROP raw table
          2. ALTER staging SET SCHEMA + RENAME TO raw
        """
        raw_schema, raw_table = raw_full.split(".", 1)

        self._db.execute(text(f"DROP TABLE IF EXISTS {raw_full} CASCADE"))
        # Move staging to raw schema and rename in one step
        self._db.execute(
            text(f"ALTER TABLE {staging_full} SET SCHEMA {raw_schema}")
        )
        self._db.execute(
            text(f"ALTER TABLE {raw_schema}.{staging_full.split('.', 1)[1]} RENAME TO {raw_table}")
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

    def _promote_upsert(
        self, staging_full: str, raw_full: str, pk_fields: list[str]
    ) -> tuple[int, int]:
        """Upsert promotion: INSERT staging into raw with ON CONFLICT DO UPDATE.

        Conflicts on pk_fields -> update business + tracking columns.
        Excludes ``_raw_id`` (preserves original PK) and ``_ingested_at``
        (preserves original ingestion timestamp).

        Rows whose PK already exists in raw with the SAME ``_row_hash`` are
        byte-identical to what was synced before, so they are EXCLUDED from
        the INSERT entirely (never touched). This keeps the "written" metric
        honest: only genuinely new or changed rows count as written.

        Returns ``(inserted, updated)`` — split via PostgreSQL's
        ``RETURNING (xmax = 0) AS is_insert`` idiom (a freshly inserted row
        has xmax = 0; an ON CONFLICT-updated row has xmax = current xid).
        """
        cols = self._get_columns(raw_full)
        conflict_cols = set(pk_fields)
        set_cols = [
            c for c in cols
            if c not in conflict_cols and c not in ("_raw_id", "_ingested_at")
        ]

        col_list = ", ".join(f'"{c}"' for c in cols)
        set_clause = ", ".join(f'"{c}" = EXCLUDED."{c}"' for c in set_cols)
        conflict_target = ", ".join(f'"{c}"' for c in pk_fields)
        pk_equal = " AND ".join(f'r."{c}" = s."{c}"' for c in pk_fields)

        # Only skip unchanged rows when both tables carry _row_hash (new-style
        # raw tables). Legacy tables without _row_hash fall back to a plain
        # upsert where every staged row is treated as inserted/updated.
        skip_unchanged = "_row_hash" in cols
        if skip_unchanged:
            where_unchanged = (
                f"WHERE NOT EXISTS ("
                f"  SELECT 1 FROM {raw_full} r"
                f"  WHERE {pk_equal} AND r.\"_row_hash\" = s.\"_row_hash\""
                f")"
            )
        else:
            where_unchanged = ""

        sql = (
            f"INSERT INTO {raw_full} ({col_list}) "
            f"SELECT {col_list} FROM {staging_full} s "
            f"{where_unchanged} "
            f"ON CONFLICT ({conflict_target}) DO UPDATE SET {set_clause} "
            f"RETURNING (xmax = 0) AS is_insert"
        )
        result = self._db.execute(text(sql))

        inserted = 0
        updated = 0
        for row in result:
            if row[0]:
                inserted += 1
            else:
                updated += 1

        self._db.execute(text(f"DROP TABLE IF EXISTS {staging_full}"))
        self._db.commit()
        logger.info(
            "Upsert promoted: %s -> %s (conflict on %s): inserted=%d updated=%d",
            staging_full, raw_full, conflict_target, inserted, updated,
        )
        return inserted, updated

    def _get_columns(self, full_table: str) -> list[str]:
        """Return ordered column names from information_schema."""
        schema, table = full_table.split(".", 1)
        result = self._db.execute(
            text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_schema = :schema AND table_name = :table "
                "ORDER BY ordinal_position"
            ),
            {"schema": schema, "table": table},
        )
        return [r.column_name for r in result]

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
            # Raw table doesn't exist — caller must have created it via
            # SchemaManager or ApiSyncEngine._ensure_raw_table before write().
            raise RuntimeError(
                f"Raw table {source_full} does not exist. "
                f"Ensure SchemaManager or _ensure_raw_table creates it before write()."
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
