"""添加同步追踪字段 — last_sync_at / sync_mode。

Revision ID: 002
Revises: 001
Create Date: 2026-07-13
"""

from typing import Sequence, Union
from alembic import op
from sqlalchemy import Column, String, DateTime

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("ingestion_tasks", Column("sync_mode", String(20), server_default="full", nullable=False))
    op.add_column("ingestion_tasks", Column("last_sync_at", DateTime(timezone=True), nullable=True))
    op.add_column("ingestion_tasks", Column("last_sync_status", String(20), nullable=True))


def downgrade() -> None:
    op.drop_column("ingestion_tasks", "last_sync_status")
    op.drop_column("ingestion_tasks", "last_sync_at")
    op.drop_column("ingestion_tasks", "sync_mode")
