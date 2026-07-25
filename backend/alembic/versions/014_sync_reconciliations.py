"""create sync_reconciliations + sync_schema_changes audit tables

Revision ID: 014
Revises: 013
Create Date: 2026-07-25

Reason: 同步引擎优化方案（08-d2a 对标）Phase 1 P0 —— 为对账机制（L1/L2/L3）
和 Schema 漂移检测提供审计存储：
  - sync_reconciliations：每次对账结果（API 总量 vs DB 行数 + 差异分级）
  - sync_schema_changes：API 返回新字段时自动加列的审计记录

采用裸 SQL `CREATE TABLE IF NOT EXISTS`（幂等可重复执行），并使用
DB 侧 `DEFAULT gen_random_uuid()` 主键默认值，以便引擎用裸 SQL INSERT
时无需显式提供 id（见 B1.2 _check_schema_drift / B1.3 reconcile_l1）。
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers
revision: str = "014"
down_revision: Union[str, None] = "013"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # gen_random_uuid() 在 PG13+ 为内置；老版本来自 pgcrypto，保险起见确保扩展存在
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    # ── sync_reconciliations（对账记录） ──────────────────────────
    op.execute("""
        CREATE TABLE IF NOT EXISTS sync_reconciliations (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            data_source_id  UUID NOT NULL,
            interface_name  VARCHAR(200) NOT NULL,
            batch_id        UUID,
            check_level     VARCHAR(10) NOT NULL,
            api_total       INTEGER,
            db_count        INTEGER,
            diff_count      INTEGER,
            diff_ratio      NUMERIC(6,4),
            status          VARCHAR(20) NOT NULL,
            detail          JSONB,
            checked_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_sync_recon_ds "
        "ON sync_reconciliations(data_source_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_sync_recon_iface "
        "ON sync_reconciliations(interface_name)"
    )

    # ── sync_schema_changes（Schema 漂移审计） ────────────────────
    op.execute("""
        CREATE TABLE IF NOT EXISTS sync_schema_changes (
            id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            table_name  VARCHAR(500) NOT NULL,
            change_type VARCHAR(20) NOT NULL,
            column_name TEXT NOT NULL,
            detail      JSONB,
            detected_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_sync_schema_changes_table "
        "ON sync_schema_changes(table_name)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_sync_schema_changes_detected "
        "ON sync_schema_changes(detected_at)"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS idx_sync_schema_changes_detected")
    op.execute("DROP INDEX IF EXISTS idx_sync_schema_changes_table")
    op.execute("DROP TABLE IF EXISTS sync_schema_changes")

    op.execute("DROP INDEX IF EXISTS idx_sync_recon_iface")
    op.execute("DROP INDEX IF EXISTS idx_sync_recon_ds")
    op.execute("DROP TABLE IF EXISTS sync_reconciliations")
