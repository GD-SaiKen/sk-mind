"""SchemaManager: manages the lifecycle of raw-layer physical tables.

Responsibilities:
- First-time sync: auto CREATE TABLE with tracking columns + indexes
- Subsequent sync: compare structures and reject if source columns changed
- SQL Server -> PostgreSQL type mapping
"""

from dataclasses import dataclass, field
from typing import Optional
import logging

from sqlalchemy import text
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

# --- SQL Server -> PostgreSQL type mapping ---
SQLSERVER_TYPE_MAP: dict[str, str] = {
    "nvarchar": "text",
    "varchar": "text",
    "text": "text",
    "nchar": "text",
    "char": "text",
    "ntext": "text",
    "int": "bigint",
    "bigint": "bigint",
    "smallint": "bigint",
    "tinyint": "bigint",
    "decimal": "numeric",
    "numeric": "numeric",
    "money": "numeric",
    "smallmoney": "numeric",
    "float": "double precision",
    "real": "double precision",
    "datetime": "timestamp",
    "datetime2": "timestamp",
    "smalldatetime": "timestamp",
    "date": "date",
    "time": "time",
    "datetimeoffset": "timestamptz",
    "bit": "boolean",
    "uniqueidentifier": "uuid",
    "varbinary": "bytea",
    "image": "bytea",
}

# --- Standard tracking columns prepended to every raw table ---
TRACKING_COLUMNS: list[tuple[str, str]] = [
    ("_raw_id", "UUID PRIMARY KEY DEFAULT gen_random_uuid()"),
    ("_source_id", "UUID NOT NULL"),
    ("_batch_id", "UUID NOT NULL"),
    ("_pulled_at", "TIMESTAMP NOT NULL"),
    ("_source_signature", "TEXT"),
    ("_row_hash", "TEXT"),
    ("_quality_flags", "JSONB DEFAULT '[]'"),
    ("_ingested_at", "TIMESTAMP DEFAULT now()"),
]

_INDEX_COLUMNS = ["_batch_id", "_pulled_at", "_row_hash"]


@dataclass
class SchemaChange:
    """Describes a detected schema difference between source and target."""
    change_type: str  # "added" | "removed" | "type_changed"
    column_name: str
    old_definition: Optional[str] = None
    new_definition: Optional[str] = None


class SchemaManager:
    """Manages the lifecycle of raw schema physical tables."""

    def __init__(self, db: Session):
        self._db = db

    # --- CREATE ---

    def ensure_table(
        self,
        schema: str,
        table: str,
        source_id: str,
        columns: list[dict],
    ) -> None:
        """Create the raw table if it does not exist.

        Each column dict: {"name": str, "data_type": str, "is_nullable": bool}
        data_type should be the SQL Server native type name (e.g. "nvarchar", "int").
        """
        full_name = f"{schema}.{table}"
        if self._table_exists(schema, table):
            return

        col_defs: list[str] = []
        for c in columns:
            base_type = c["data_type"].lower().split("(")[0].strip()
            pg_type = SQLSERVER_TYPE_MAP.get(base_type, "text")
            nullable = "" if c.get("is_nullable", True) else " NOT NULL"
            col_defs.append(f'    "{c["name"]}" {pg_type}{nullable}')

        for name, typedef in TRACKING_COLUMNS:
            col_defs.append(f'    "{name}" {typedef}')

        ddl = f"CREATE TABLE {full_name} (\n" + ",\n".join(col_defs) + "\n)"
        self._db.execute(text(ddl))
        self._db.commit()

        # Create indexes
        for idx_col in _INDEX_COLUMNS:
            idx_name = f"idx_{table}_{idx_col}"
            idx_sql = text(
                f"CREATE INDEX IF NOT EXISTS {idx_name} ON {full_name} ({idx_col})"
            )
            self._db.execute(idx_sql)
        self._db.commit()

        logger.info("Created raw table %s with %d data columns", full_name, len(columns))

    # --- COMPARE ---

    def check_schema(
        self, schema: str, table: str, expected: list[dict]
    ) -> list[SchemaChange]:
        """Compare the existing table against expected columns.

        Returns a list of SchemaChange; empty list means structures match.
        Caller should reject the sync if any changes are detected.
        """
        existing_cols = self._get_table_columns(schema, table)
        existing_names = {c["name"] for c in existing_cols}
        expected_names = {c["name"] for c in expected}

        changes: list[SchemaChange] = []

        # Detected additions
        for name in expected_names - existing_names:
            changes.append(SchemaChange(
                change_type="added",
                column_name=name,
                new_definition=name,
            ))

        # Detected removals
        for name in existing_names - expected_names:
            changes.append(SchemaChange(
                change_type="removed",
                column_name=name,
                old_definition=name,
            ))

        # Detected type changes
        for ec in existing_cols:
            if ec["name"] in expected_names:
                for xc in expected:
                    if xc["name"] == ec["name"]:
                        base_type = xc["data_type"].lower().split("(")[0].strip()
                        expected_pg = SQLSERVER_TYPE_MAP.get(base_type, "text")
                        if ec["data_type"] != expected_pg:
                            changes.append(SchemaChange(
                                change_type="type_changed",
                                column_name=ec["name"],
                                old_definition=ec["data_type"],
                                new_definition=expected_pg,
                            ))

        return changes

    # --- INTERNAL ---

    def _table_exists(self, schema: str, table: str) -> bool:
        check = text(
            "SELECT EXISTS ("
            "  SELECT 1 FROM information_schema.tables "
            "  WHERE table_schema = :schema AND table_name = :table"
            ")"
        )
        result = self._db.execute(check, {"schema": schema, "table": table})
        return result.scalar_one()

    def _get_table_columns(self, schema: str, table: str) -> list[dict]:
        """Return column definitions from PostgreSQL, excluding tracking columns."""
        sql = text(
            "SELECT column_name, data_type FROM information_schema.columns "
            "WHERE table_schema = :schema AND table_name = :table "
            "AND column_name NOT LIKE '_\\_%' ESCAPE '\\' "
            "ORDER BY ordinal_position"
        )
        result = self._db.execute(sql, {"schema": schema, "table": table})
        return [{"name": row.column_name, "data_type": row.data_type} for row in result]
