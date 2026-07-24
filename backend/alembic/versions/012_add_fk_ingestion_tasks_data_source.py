"""fix: 为 ingestion_tasks.data_source_id 添加外键约束

Revision ID: 012
Revises: 011
Create Date: 2026-07-24

此前 data_source_id 是普通 UUID 列，无引用完整性保护。
本次添加 ForeignKey 约束确保每个接入任务必须关联一个有效的数据源。
"""

from typing import Sequence, Union

from alembic import op

revision: str = "012"
down_revision: Union[str, None] = "011"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """添加 foreign key 约束：ingestion_tasks.data_source_id -> data_sources.id"""
    op.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM information_schema.table_constraints
                WHERE constraint_name = 'fk_ingestion_tasks_data_source_id'
            ) THEN
                ALTER TABLE ingestion_tasks
                ADD CONSTRAINT fk_ingestion_tasks_data_source_id
                FOREIGN KEY (data_source_id) REFERENCES data_sources(id);
            END IF;
        END $$;
    """)


def downgrade() -> None:
    """回退：删除外键约束"""
    op.execute("""
        DO $$
        BEGIN
            IF EXISTS (
                SELECT 1 FROM information_schema.table_constraints
                WHERE constraint_name = 'fk_ingestion_tasks_data_source_id'
            ) THEN
                ALTER TABLE ingestion_tasks
                DROP CONSTRAINT fk_ingestion_tasks_data_source_id;
            END IF;
        END $$;
    """)
