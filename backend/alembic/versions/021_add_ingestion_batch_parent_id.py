"""add parent_id to ingestion_batches for explicit parent-child grouping

Revision ID: 021
Revises: 020
Create Date: 2026-08-01

多接口任务一次运行会产生一个「(汇总)」父批次 + 各接口子批次。此前前端只能靠
``source_signature='(汇总)'`` 哨兵 + 时间连续归组来推断父子，在「同一分钟多次
运行交错 / 双 (汇总) 同秒」时会把所有子接口塞进最后一个 (汇总)，导致执行记录
树形父子关系错乱。本迁移新增 parent_id（自引用 FK）显式记录子接口批次归属的
父批次，后端在创建子批次时回填，前端按 parent_id 精确分组。
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "021"
down_revision: Union[str, None] = "020"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "ingestion_batches",
        sa.Column("parent_id", sa.UUID(as_uuid=True), nullable=True),
    )
    op.create_index(
        "ix_ingestion_batches_parent_id", "ingestion_batches", ["parent_id"]
    )
    op.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM information_schema.table_constraints
                WHERE constraint_name = 'fk_ingestion_batches_parent_id'
            ) THEN
                ALTER TABLE ingestion_batches
                ADD CONSTRAINT fk_ingestion_batches_parent_id
                FOREIGN KEY (parent_id) REFERENCES ingestion_batches(id);
            END IF;
        END $$;
        """
    )


def downgrade() -> None:
    op.execute(
        "ALTER TABLE ingestion_batches DROP CONSTRAINT IF EXISTS fk_ingestion_batches_parent_id"
    )
    op.drop_index("ix_ingestion_batches_parent_id", table_name="ingestion_batches")
    op.drop_column("ingestion_batches", "parent_id")
