"""fix: add source_category to ingestion_tasks (was missing in 003)

Revision ID: 007
Revises: 006
Create Date: 2026-07-21
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = '007'
down_revision: Union[str, None] = '006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("ingestion_tasks", sa.Column("source_category", sa.String(20), nullable=True))


def downgrade() -> None:
    op.drop_column("ingestion_tasks", "source_category")
