"""add sync_watermarks table

Revision ID: 005
Revises: 003_sync_engine_v2
Create Date: 2026-07-20
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers — keep auto-generated values
revision: str = '005'
down_revision: Union[str, None] = '003'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'sync_watermarks',
        sa.Column('id', sa.Uuid(), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('data_source_id', sa.Uuid(), nullable=False),
        sa.Column('interface_name', sa.String(128), nullable=False),
        sa.Column('last_synced_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.UniqueConstraint('data_source_id', 'interface_name', name='uq_watermark_ds_iface'),
    )


def downgrade() -> None:
    op.drop_table('sync_watermarks')
