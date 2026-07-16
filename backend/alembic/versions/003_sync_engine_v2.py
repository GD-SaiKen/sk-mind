"""sync engine v2: extend ingestion/data_sources models, init raw/clean/serving schemas.

Revision ID: 003
Revises: 002
Create Date: 2026-07-16
"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB

revision: str = "003"
down_revision: Union[str, None] = "002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- PostgreSQL schemas ---
    op.execute("CREATE SCHEMA IF NOT EXISTS raw")
    op.execute("CREATE SCHEMA IF NOT EXISTS clean")
    op.execute("CREATE SCHEMA IF NOT EXISTS serving")
    op.execute("CREATE SCHEMA IF NOT EXISTS staging")

    # --- IngestionTask ---
    op.add_column("ingestion_tasks", Column("fetch_config", JSONB, nullable=True))
    op.add_column("ingestion_tasks", Column("column_rules", JSONB, nullable=True))
    op.add_column("ingestion_tasks", Column("last_sync_marker", JSONB, nullable=True))
    op.add_column("ingestion_tasks", Column("target_table", String(200), nullable=True))

    # --- IngestionBatch ---
    op.add_column("ingestion_batches", Column("rejected_rows", String(50), nullable=True))
    op.add_column("ingestion_batches", Column("last_sync_marker", JSONB, nullable=True))
    op.add_column("ingestion_batches", Column("error_items", JSONB, nullable=True))
    op.add_column("ingestion_batches", Column("source_signature", String(500), nullable=True))

    # --- DataSource ---
    op.add_column("data_sources", Column("source_category", String(20), nullable=True))
    op.add_column("data_sources", Column("connection_status", String(20), nullable=True))
    op.add_column("data_sources", Column("last_health_check_at", DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    op.drop_column("data_sources", "last_health_check_at")
    op.drop_column("data_sources", "connection_status")
    op.drop_column("data_sources", "source_category")

    op.drop_column("ingestion_batches", "source_signature")
    op.drop_column("ingestion_batches", "error_items")
    op.drop_column("ingestion_batches", "last_sync_marker")
    op.drop_column("ingestion_batches", "rejected_rows")

    op.drop_column("ingestion_tasks", "target_table")
    op.drop_column("ingestion_tasks", "last_sync_marker")
    op.drop_column("ingestion_tasks", "column_rules")
    op.drop_column("ingestion_tasks", "fetch_config")

    op.execute("DROP SCHEMA IF EXISTS serving CASCADE")
    op.execute("DROP SCHEMA IF EXISTS clean CASCADE")
    op.execute("DROP SCHEMA IF EXISTS staging CASCADE")
    op.execute("DROP SCHEMA IF EXISTS raw CASCADE")
