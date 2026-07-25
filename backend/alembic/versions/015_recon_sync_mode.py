"""add sync_mode + pulled_count to sync_reconciliations

Revision ID: 015
Revises: 014
Create Date: 2026-07-25

Reason: 同步引擎优化 — L1 对账按同步模式分作用域（见 B1.3 修正）。
原来增量同步把「API 窗口总量」与「整张 raw 表累计行数」对比，产生无意义的
负差异率（-5000%），且 `diff<=0 -> pass` 规则会掩盖增量窗口内的真实丢数。

- sync_mode: 该次对账的同步模式（full / incremental），用于前端区分作用域。
- pulled_count: 增量模式下与 api_total 对比的「本批实际拉取行数」；
  全量模式为 0（对比基准是整表，用 db_count）。
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers
revision: str = "015"
down_revision: Union[str, None] = "014"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE sync_reconciliations "
        "ADD COLUMN IF NOT EXISTS sync_mode VARCHAR(16) NOT NULL DEFAULT 'full'"
    )
    op.execute(
        "ALTER TABLE sync_reconciliations "
        "ADD COLUMN IF NOT EXISTS pulled_count INTEGER NOT NULL DEFAULT 0"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_sync_recon_mode "
        "ON sync_reconciliations(sync_mode)"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS idx_sync_recon_mode")
    op.execute("ALTER TABLE sync_reconciliations DROP COLUMN IF EXISTS pulled_count")
    op.execute("ALTER TABLE sync_reconciliations DROP COLUMN IF EXISTS sync_mode")
