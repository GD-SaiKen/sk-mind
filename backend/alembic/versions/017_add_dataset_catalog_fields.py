"""add is_primary_key and source_column to dataset_fields (T1)

Revision ID: 017
Revises: 016
Create Date: 2026-07-28

T1 聚焦任务：为 dataset_fields 表增加两个字段，供 T2 同步自动登记时使用。
- is_primary_key: 标记该字段来自 YAML pk_fields，upsert 的 ON CONFLICT 列
- source_column: raw 表物理列名即源字段名，对 raw 层两者相同，对 clean/serving 层追溯来源有用
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers
revision: str = "017"
down_revision: Union[str, None] = "016"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE dataset_fields
        ADD COLUMN IF NOT EXISTS is_primary_key BOOLEAN NOT NULL DEFAULT FALSE
        """
    )
    op.execute(
        """
        ALTER TABLE dataset_fields
        ADD COLUMN IF NOT EXISTS source_column VARCHAR(200)
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE dataset_fields
        DROP COLUMN IF EXISTS is_primary_key
        """
    )
    op.execute(
        """
        ALTER TABLE dataset_fields
        DROP COLUMN IF EXISTS source_column
        """
    )
