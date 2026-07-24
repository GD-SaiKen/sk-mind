"""Convert remaining TIMESTAMPTZ/DATE business columns to raw-friendly types

Revision ID: 011
Revises: 010
Create Date: 2026-07-21

Converts:
  - String-date TIMESTAMPTZ -> TEXT (task_start_time, task_end_time, use_time)
  - DATE columns -> TEXT (work_date, production_date, first_date, receive_date)
The _pulled_at / _ingested_at tracking columns remain as TIMESTAMP — those
are engine-managed, not from API responses.
"""
from typing import Sequence, Union
from alembic import op

revision: str = '011'
down_revision: Union[str, None] = '010'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


TEXT_CONVERSIONS = {
    # API returns string datetime -> TEXT
    "raw.mes_select_procedures_report_data_by_time": [
        "task_start_time", "task_end_time", "work_date",
    ],
    "raw.mes_select_workorder_report_data_by_time": [
        "task_start_time", "task_end_time", "work_date",
    ],
    "raw.mes_select_task_use_material": ["use_time"],
    # DATE columns from machine detail API
    "raw.mes_get_machine_detail_by_id": [
        "first_date", "production_date", "receive_date",
    ],
}


def upgrade():
    for tbl, cols in TEXT_CONVERSIONS.items():
        schema, tname = tbl.split(".")
        for col in cols:
            op.execute(f"""
                DO $$
                DECLARE
                    _type text;
                BEGIN
                    SELECT data_type INTO _type
                    FROM information_schema.columns
                    WHERE table_schema = '{schema}'
                      AND table_name   = '{tname}'
                      AND column_name  = '{col}';
                    IF _type IS NOT NULL AND _type NOT IN ('text', 'character varying') THEN
                        ALTER TABLE {tbl} ALTER COLUMN {col} TYPE TEXT;
                    END IF;
                END $$;
            """)


def downgrade():
    for tbl, cols in TEXT_CONVERSIONS.items():
        schema, tname = tbl.split(".")
        for col in cols:
            op.execute(f"""
                DO $$
                DECLARE
                    _type text;
                BEGIN
                    SELECT data_type INTO _type
                    FROM information_schema.columns
                    WHERE table_schema = '{schema}'
                      AND table_name   = '{tname}'
                      AND column_name  = '{col}';
                    IF _type IS NOT NULL AND _type IN ('text', 'character varying') THEN
                        ALTER TABLE {tbl} ALTER COLUMN {col} TYPE TIMESTAMPTZ
                        USING (CASE WHEN {col} IS NULL THEN NULL ELSE {col}::TIMESTAMPTZ END);
                    END IF;
                END $$;
            """)
