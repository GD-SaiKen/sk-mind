"""add missing JSONB columns to mes_andon_api_controller

Revision ID: 008
Revises: 007
Create Date: 2026-07-21
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = '008'
down_revision: Union[str, None] = '007'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add 4 missing JSONB columns discovered during end-to-end testing."""
    cols = [
        ("finish_url_list", "处理结果图片/视频列表 array<UrlAndTypeDTO>"),
        ("supplement_url_list", "补充图片/视频列表 array<UrlAndTypeDTO>"),
        ("andon_record_log_list", "安灯日志 array<AndonRecordLog>"),
        ("andon_oa_process_info_list", "安灯OA流程信息 array<AndonOaProcessInfo>"),
    ]
    for col_name, _ in cols:
        op.execute(
            f"ALTER TABLE raw.mes_andon_api_controller "
            f"ADD COLUMN IF NOT EXISTS {col_name} JSONB"
        )


def downgrade() -> None:
    cols = [
        "finish_url_list",
        "supplement_url_list",
        "andon_record_log_list",
        "andon_oa_process_info_list",
    ]
    for col_name in cols:
        op.execute(
            f"ALTER TABLE raw.mes_andon_api_controller "
            f"DROP COLUMN IF EXISTS {col_name}"
        )
