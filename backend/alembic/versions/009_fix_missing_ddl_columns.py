"""add missing DDL columns discovered via API field comparison

Revision ID: 009
Revises: 008
Create Date: 2026-07-21

Changes:
  1. raw.mes_select_procedures_report_data_by_time: add compensate_hours NUMERIC
  2. raw.mes_select_workorder_report_data_by_time: add compensate_hours NUMERIC
  3. raw.mes_select_workorder_task_action_statistics: rename product_specifications -> product_specification_qties
  4. raw.mes_select_oee_report: add oee_users JSONB
  5. raw.mes_query_craft_hours: add procedure_name JSONB (API returns singular procedure_name as list)
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = '009'
down_revision: Union[str, None] = '008'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1-2. compensate_hours for procedure/workorder report tables
    for tbl in [
        "raw.mes_select_procedures_report_data_by_time",
        "raw.mes_select_workorder_report_data_by_time",
    ]:
        op.execute(f"ALTER TABLE {tbl} ADD COLUMN IF NOT EXISTS compensate_hours NUMERIC")

    # 3. Rename product_specifications -> product_specification_qties
    op.execute("""
        ALTER TABLE raw.mes_select_workorder_task_action_statistics
        RENAME COLUMN product_specifications TO product_specification_qties
    """)

    # 4. oee_users for OEE report
    op.execute(
        "ALTER TABLE raw.mes_select_oee_report ADD COLUMN IF NOT EXISTS oee_users JSONB"
    )

    # 5. procedure_name for craft hours (API returns singular field as list)
    op.execute(
        "ALTER TABLE raw.mes_query_craft_hours ADD COLUMN IF NOT EXISTS procedure_name JSONB"
    )


def downgrade() -> None:
    for tbl in [
        "raw.mes_select_procedures_report_data_by_time",
        "raw.mes_select_workorder_report_data_by_time",
    ]:
        op.execute(f"ALTER TABLE {tbl} DROP COLUMN IF EXISTS compensate_hours")

    op.execute("""
        ALTER TABLE raw.mes_select_workorder_task_action_statistics
        RENAME COLUMN product_specification_qties TO product_specifications
    """)

    op.execute("ALTER TABLE raw.mes_select_oee_report DROP COLUMN IF EXISTS oee_users")
    op.execute("ALTER TABLE raw.mes_query_craft_hours DROP COLUMN IF EXISTS procedure_name")
