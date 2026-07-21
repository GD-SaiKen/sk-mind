"""Convert date/timestamp columns from TIMESTAMPTZ to BIGINT for raw millis storage

Revision ID: 010
Revises: 009
Create Date: 2026-07-21

Principle: Raw layer stores API values as-is — no type conversion.
MES API returns Java-millis integers for date fields, so columns
should be BIGINT, not TIMESTAMPTZ. The Clean layer will convert
these to proper datetime types.
"""
from typing import Sequence, Union
from alembic import op

revision: str = '010'
down_revision: Union[str, None] = '009'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


CONVERSIONS = {
    "raw.mes_andon_api_controller": [
        "create_date", "receive_date", "finish_date",
    ],
    "raw.mes_filter_workorder": [
        "create_time", "end_time", "start_time", "require_end_time",
        "estimated_start_time", "estimated_end_time", "actual_complete_time", "close_time",
    ],
    "raw.mes_select_procedures_report_data_by_time": ["create_time", "approver_time"],
    "raw.mes_select_workorder_report_data_by_time": ["create_time", "approver_time"],
    "raw.mes_select_workorder_task_action_statistics": [
        "start_time", "end_time", "mould_start_time", "mould_end_time",
        "start_mould_time", "end_mould_time",
    ],
    "raw.mes_select_oee_report": ["start_time", "end_time", "sim_date"],
    "raw.mes_query_craft_hours": ["create_time", "update_time"],
    "raw.mes_select_error_report": [
        "shift_start_date", "shift_end_date", "wait_start_time", "wait_end_time",
        "update_time", "work_date",
    ],
    "raw.mes_get_trilight_summary_duration_time": ["start_time", "end_time"],
    "raw.mes_get_trilight_current_color": ["update_date"],
    "raw.mes_get_trilight_current_color_list": ["update_date"],
    "raw.mes_select_complish_report": ["work_date"],
}


def upgrade():
    for tbl, cols in CONVERSIONS.items():
        for col in cols:
            op.execute(
                f"ALTER TABLE {tbl} ALTER COLUMN {col} TYPE BIGINT "
                f"USING (CASE WHEN {col} IS NULL THEN NULL "
                f"ELSE EXTRACT(EPOCH FROM {col}) * 1000::BIGINT END)"
            )


def downgrade():
    for tbl, cols in CONVERSIONS.items():
        for col in cols:
            op.execute(
                f"ALTER TABLE {tbl} ALTER COLUMN {col} TYPE TIMESTAMPTZ "
                f"USING (CASE WHEN {col} IS NULL THEN NULL "
                f"ELSE TO_TIMESTAMP({col} / 1000.0) END)"
            )
