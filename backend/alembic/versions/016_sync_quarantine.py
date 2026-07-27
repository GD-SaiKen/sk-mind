"""create sync_quarantine table (B2.4 隔离区)

Revision ID: 016
Revises: 015
Create Date: 2026-07-27

Reason: 同步引擎优化 Phase 2 — 隔离区机制。被 _validate_rows（null_pk /
dup_in_batch）与 stage_writer（write_error）拒绝的坏数据行不再丢弃，写入
sync_quarantine 表，可追溯、可重试（B2.6 提供重试/忽略 API）。
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers
revision: str = "016"
down_revision: Union[str, None] = "015"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS sync_quarantine (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            batch_id        UUID NOT NULL,
            data_source_id  UUID NOT NULL,
            interface_name  VARCHAR(200) NOT NULL,
            pk_value        TEXT,
            rejection_reason VARCHAR(100) NOT NULL,
            raw_json        JSONB NOT NULL,
            status          VARCHAR(20) NOT NULL DEFAULT 'pending',
            retried_at      TIMESTAMPTZ,
            resolved_at     TIMESTAMPTZ,
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_quarantine_batch ON sync_quarantine(batch_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_quarantine_status ON sync_quarantine(status)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_quarantine_iface ON sync_quarantine(interface_name)"
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS sync_quarantine")
