"""add null_rate to dataset_fields and agent_unavailable_reason to datasets (T5+T6)

Revision ID: 018
Revises: 017
Create Date: 2026-07-28

T5: dataset_fields.null_rate — null 值占比统计
T6: datasets.agent_unavailable_reason — Agent 可用性检查不通过原因
"""

from typing import Sequence, Union

from alembic import op

revision: str = "018"
down_revision: Union[str, None] = "017"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE dataset_fields
        ADD COLUMN IF NOT EXISTS null_rate FLOAT
        """
    )
    op.execute(
        """
        ALTER TABLE datasets
        ADD COLUMN IF NOT EXISTS agent_unavailable_reason TEXT
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE dataset_fields
        DROP COLUMN IF EXISTS null_rate
        """
    )
    op.execute(
        """
        ALTER TABLE datasets
        DROP COLUMN IF EXISTS agent_unavailable_reason
        """
    )
