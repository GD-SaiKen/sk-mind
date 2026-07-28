"""Dataset auto-registration after sync (T2).

After ApiSyncEngine successfully writes data to a raw table, this module
auto-creates/updates Dataset, DatasetField, and DataTable records so that
the "数据表" and "数据目录" modules can discover the new data.

Design principles:
- Failure must NOT block the sync main flow — all exceptions are caught.
- Uses raw SQL (via sync Session.execute) — consistent with how the sync
  engine writes to quarantine, schema_changes, etc.
- Idempotent: Dataset.code = target_table provides upsert uniqueness.
- DatasetField: only INSERT new columns on incremental sync; never
  delete or overwrite manually-edited fields.
"""

import logging
import uuid
from typing import Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

# Columns that should NOT be registered as DatasetField (sync engine internals)
_EXCLUDE_COLUMNS = {
    "_synced_at", "_row_hash", "_batch_id", "_source_id",
    "_source_signature", "_action",
}


class DatasetRegistrar:
    """Auto-register Dataset/DatasetField/DataTable after successful sync.

    Called from within ``ApiSyncEngine._sync_interface`` after watermark save.
    Uses the sync engine's synchronous ``Session``.
    """

    def __init__(self, db: Session):
        self._db = db

    # ── public API ────────────────────────────

    def register(
        self,
        *,
        target_table: str,
        data_source_id: uuid.UUID,
        task_id: uuid.UUID,
        batch_id: uuid.UUID,
        pk_fields: list[str],
        pulled: int,
        domain: Optional[str] = None,
        data_source_name: Optional[str] = None,
    ) -> Optional[str]:
        """Register or update dataset metadata after a sync completes.

        Called once per interface after successful write + watermark save.

        Args:
            target_table: Full table name, e.g. "raw.mes_filter_workorder".
            data_source_id: DataSource UUID.
            task_id: IngestionTask UUID.
            batch_id: IngestionBatch UUID.
            pk_fields: YAML pk_fields list (used to mark DatasetField.is_primary_key).
            pulled: Number of rows pulled from API.
            domain: Business domain parsed from YAML comments, e.g. "工单域".
            data_source_name: Human-readable data source name.

        Returns:
            dataset_id as string if successful, None on failure.
        """
        try:
            schema, table = target_table.split(".", 1)
        except ValueError:
            logger.warning("Invalid target_table format: %s", target_table)
            return None

        try:
            dataset_id = self._upsert_dataset(
                code=target_table,
                name=data_source_name or target_table,
                data_source_id=data_source_id,
                task_id=task_id,
                batch_id=batch_id,
                record_count=pulled,
                business_domain=domain,
                schema=schema,
                table=table,
            )

            if not dataset_id:
                return None

            self._upsert_data_table(
                dataset_id=dataset_id,
                schema_name=schema,
                table_name=table,
                row_count=pulled,
            )

            self._sync_fields(
                dataset_id=dataset_id,
                schema=schema,
                table=table,
                pk_fields=pk_fields,
            )

            logger.info(
                "Dataset auto-registered: code=%s dataset_id=%s domain=%s",
                target_table, dataset_id, domain or "-",
            )
            return dataset_id

        except Exception:
            logger.warning(
                "DatasetRegistrar failed for %s (non-fatal)", target_table, exc_info=True,
            )
            try:
                self._db.rollback()
            except Exception:
                pass
            return None

    # ── domain parsing (static) ────────────────

    @staticmethod
    def parse_domains_from_yaml(yaml_path: str) -> dict[str, str]:
        """Parse business domain comments from a YAML config file.

        Scans lines for ``# ── 工单域 ──`` patterns and maps them to
        the interface names that follow.

        Returns:
            {"filterWorkorder": "工单域", "andonList": "安灯域", ...}
        """
        import re

        domain_map: dict[str, str] = {}
        current_domain: Optional[str] = None
        # Matches:  # ── 工单域 ──
        domain_pattern = re.compile(r"^\s*#\s*──\s*(.+?)\s*──\s*$")
        # Matches:    - name: filterWorkorder
        name_pattern = re.compile(r"^\s*-\s+name:\s*(\S+)")

        try:
            with open(yaml_path, encoding="utf-8") as f:
                for line in f:
                    dm = domain_pattern.match(line)
                    if dm:
                        current_domain = dm.group(1).strip()
                        continue

                    nm = name_pattern.match(line)
                    if nm and current_domain:
                        domain_map[nm.group(1)] = current_domain
        except Exception:
            logger.warning("Failed to parse business domains from %s", yaml_path, exc_info=True)

        return domain_map

    # ── internal helpers ───────────────────────

    def _upsert_dataset(
        self,
        code: str,
        name: str,
        data_source_id: uuid.UUID,
        task_id: uuid.UUID,
        batch_id: uuid.UUID,
        record_count: int,
        business_domain: Optional[str],
        schema: str,
        table: str,
    ) -> Optional[str]:
        """Upsert a Dataset record by unique code. Returns dataset_id or None."""
        # Check existing to know if we're creating or updating
        existing = self._db.execute(
            text("SELECT id FROM datasets WHERE code = :code"),
            {"code": code},
        ).scalar_one_or_none()

        # Count actual rows in the physical table (fallback to API pulled count)
        try:
            actual_count = self._db.execute(
                text(f"SELECT count(*) FROM {schema}.\"{table}\"")
            ).scalar()
        except Exception:
            actual_count = record_count

        # Count physical columns (excluding tracking columns)
        field_count = self._count_business_columns(schema, table)

        if existing:
            dataset_id = str(existing)
            self._db.execute(
                text(
                    """
                    UPDATE datasets SET
                        record_count = :record_count,
                        field_count = :field_count,
                        last_batch_id = :batch_id,
                        updated_at = now()
                    WHERE id = :id
                    """
                ),
                {
                    "record_count": actual_count,
                    "field_count": field_count,
                    "batch_id": str(batch_id),
                    "id": existing,
                },
            )
            self._db.commit()
            return dataset_id

        # First time — INSERT with all fields
        dataset_id = str(uuid.uuid4())
        self._db.execute(
            text(
                """
                INSERT INTO datasets (
                    id, name, code, data_layer, data_source_id,
                    generated_by_task_id, last_batch_id,
                    record_count, field_count, business_domain,
                    status, sensitivity_level, is_agent_accessible,
                    created_at, updated_at
                ) VALUES (
                    :id, :name, :code, :data_layer, :data_source_id,
                    :task_id, :batch_id,
                    :record_count, :field_count, :business_domain,
                    :status, :sensitivity_level, :is_agent_accessible,
                    now(), now()
                )
                """
            ),
            {
                "id": uuid.UUID(dataset_id),
                "name": name,
                "code": code,
                "data_layer": "raw",
                "data_source_id": str(data_source_id),
                "task_id": str(task_id),
                "batch_id": str(batch_id),
                "record_count": actual_count,
                "field_count": field_count,
                "business_domain": business_domain,
                "status": "active",
                "sensitivity_level": "internal",
                "is_agent_accessible": False,
            },
        )
        self._db.commit()
        return dataset_id

    def _upsert_data_table(
        self,
        dataset_id: str,
        schema_name: str,
        table_name: str,
        row_count: int,
    ) -> None:
        """Insert or update a DataTable record."""
        existing = self._db.execute(
            text(
                "SELECT id FROM data_tables "
                "WHERE dataset_id = :ds_id "
                "AND schema_name = :schema AND table_name = :tbl"
            ),
            {
                "ds_id": uuid.UUID(dataset_id),
                "schema": schema_name,
                "tbl": table_name,
            },
        ).scalar_one_or_none()

        if existing:
            self._db.execute(
                text(
                    "UPDATE data_tables SET row_count = :cnt, updated_at = now() "
                    "WHERE id = :id"
                ),
                {"cnt": row_count, "id": existing},
            )
        else:
            self._db.execute(
                text(
                    """
                    INSERT INTO data_tables (
                        id, dataset_id, schema_name, table_name,
                        table_type, row_count, created_at, updated_at
                    ) VALUES (
                        :id, :ds_id, :schema, :tbl,
                        'table', :cnt, now(), now()
                    )
                    """
                ),
                {
                    "id": uuid.uuid4(),
                    "ds_id": uuid.UUID(dataset_id),
                    "schema": schema_name,
                    "tbl": table_name,
                    "cnt": row_count,
                },
            )
        self._db.commit()

    def _sync_fields(
        self,
        dataset_id: str,
        schema: str,
        table: str,
        pk_fields: list[str],
    ) -> None:
        """Sync DatasetField records: add new columns, keep existing untouched."""
        # Get existing field names (case-insensitive to avoid dupes)
        existing = self._db.execute(
            text(
                "SELECT LOWER(field_name) FROM dataset_fields "
                "WHERE dataset_id = :ds_id"
            ),
            {"ds_id": uuid.UUID(dataset_id)},
        )
        existing_names: set[str] = {row[0] for row in existing}

        # Get physical columns from information_schema
        phys_cols = self._db.execute(
            text(
                "SELECT column_name, data_type, is_nullable, ordinal_position, "
                "character_maximum_length "
                "FROM information_schema.columns "
                "WHERE table_schema = :schema AND table_name = :tbl "
                "ORDER BY ordinal_position"
            ),
            {"schema": schema, "tbl": table},
        ).fetchall()

        inserted = 0
        for col in phys_cols:
            col_name = col.column_name
            # Skip tracking columns
            if col_name.startswith("_") and col_name in _EXCLUDE_COLUMNS:
                continue

            if col_name.lower() in existing_names:
                continue  # already registered — don't touch

            self._db.execute(
                text(
                    """
                    INSERT INTO dataset_fields (
                        id, dataset_id, field_name, data_type,
                        field_length, is_nullable, ordinal_position,
                        is_primary_key, source_column,
                        sensitivity_level, quality_status,
                        created_at, updated_at
                    ) VALUES (
                        :id, :ds_id, :name, :dtype,
                        :length, :nullable, :ordinal,
                        :is_pk, :src_col,
                        :sensitivity, :quality,
                        now(), now()
                    )
                    """
                ),
                {
                    "id": uuid.uuid4(),
                    "ds_id": uuid.UUID(dataset_id),
                    "name": col_name,
                    "dtype": self._normalize_data_type(col.data_type),
                    "length": col.character_maximum_length
                    if hasattr(col, "character_maximum_length") else None,
                    "nullable": col.is_nullable == "YES",
                    "ordinal": col.ordinal_position,
                    "is_pk": col_name in pk_fields,
                    "src_col": col_name,  # raw layer: source = physical column
                    "sensitivity": "internal",
                    "quality": None,
                },
            )
            inserted += 1

        if inserted > 0:
            self._db.commit()
            logger.info(
                "DatasetField: added %d new columns for dataset %s", inserted, dataset_id[:8]
            )

        # Update field_count if new fields were added
        if inserted > 0:
            new_total = len(existing_names) + inserted
            self._db.execute(
                text(
                    "UPDATE datasets SET field_count = :cnt, updated_at = now() "
                    "WHERE id = :id"
                ),
                {"cnt": new_total, "id": uuid.UUID(dataset_id)},
            )
            self._db.commit()

    def _count_business_columns(self, schema: str, table: str) -> int:
        """Count business columns (excluding tracking) in a physical table."""
        result = self._db.execute(
            text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_schema = :schema AND table_name = :tbl"
            ),
            {"schema": schema, "tbl": table},
        )
        return sum(
            1 for row in result
            if not (row.column_name.startswith("_")
                    and row.column_name in _EXCLUDE_COLUMNS)
        )

    @staticmethod
    def _normalize_data_type(pg_type: str) -> str:
        """Shorten PostgreSQL type names to common labels."""
        _map = {
            "character varying": "varchar",
            "character": "char",
            "double precision": "float8",
            "timestamp without time zone": "timestamp",
            "timestamp with time zone": "timestamptz",
            "time without time zone": "time",
            "time with time zone": "timetz",
        }
        return _map.get(pg_type, pg_type)
