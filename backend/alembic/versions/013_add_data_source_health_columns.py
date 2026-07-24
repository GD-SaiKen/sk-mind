"""add source_category / connection_status / last_health_check_at to data_sources

Revision ID: 013
Revises: 012
Create Date: 2026-07-24

Reason: DataSource ORM model added three columns for health-check and
source-category tracking, but the actual DB table was missing them.
"""

from typing import Sequence, Union

from alembic import op

revision: str = "013"
down_revision: Union[str, None] = "012"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    for col_name, pg_type in [
        ("source_category", "VARCHAR(20)"),
        ("connection_status", "VARCHAR(50)"),
        ("last_health_check_at", "TIMESTAMPTZ"),
    ]:
        op.execute(f"""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM information_schema.columns
                    WHERE table_name = 'data_sources'
                      AND column_name = '{col_name}'
                ) THEN
                    ALTER TABLE data_sources ADD COLUMN {col_name} {pg_type};
                END IF;
            END $$;
        """)


def downgrade() -> None:
    for col_name in [
        "last_health_check_at",
        "connection_status",
        "source_category",
    ]:
        op.execute(f"""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 FROM information_schema.columns
                    WHERE table_name = 'data_sources'
                      AND column_name = '{col_name}'
                ) THEN
                    ALTER TABLE data_sources DROP COLUMN {col_name};
                END IF;
            END $$;
        """)
