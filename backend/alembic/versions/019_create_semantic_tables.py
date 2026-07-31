"""create semantic_objects, semantic_properties, data_mappings tables

Revision ID: 019
Revises: 018
Create Date: 2026-07-29

Phase 1: 语义模型 — 业务对象、对象属性、数据映射三张核心表。
"""

from typing import Sequence, Union

from alembic import op

revision: str = "019"
down_revision: Union[str, None] = "018"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── 1. semantic_objects ──
    op.execute("""
        CREATE TABLE IF NOT EXISTS semantic_objects (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(200) NOT NULL,
            code VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            object_type VARCHAR(50) NOT NULL,
            domain VARCHAR(100),
            status VARCHAR(20) NOT NULL DEFAULT 'draft',
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_semantic_objects_code ON semantic_objects(code)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_semantic_objects_object_type ON semantic_objects(object_type)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_semantic_objects_status ON semantic_objects(status)")

    # ── 2. semantic_properties ──
    op.execute("""
        CREATE TABLE IF NOT EXISTS semantic_properties (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            semantic_object_id UUID NOT NULL
                REFERENCES semantic_objects(id) ON DELETE CASCADE,
            name VARCHAR(200) NOT NULL,
            code VARCHAR(100) NOT NULL,
            property_type VARCHAR(50) NOT NULL,
            data_type VARCHAR(50) NOT NULL,
            description TEXT,
            is_required BOOLEAN NOT NULL DEFAULT FALSE,
            is_sensitive BOOLEAN NOT NULL DEFAULT FALSE,
            status VARCHAR(20) NOT NULL DEFAULT 'draft',
            ordinal_position INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_semantic_properties_object_id ON semantic_properties(semantic_object_id)")

    # ── 3. data_mappings ──
    op.execute("""
        CREATE TABLE IF NOT EXISTS data_mappings (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            mapping_type VARCHAR(20) NOT NULL,
            semantic_object_id UUID
                REFERENCES semantic_objects(id) ON DELETE SET NULL,
            semantic_property_id UUID
                REFERENCES semantic_properties(id) ON DELETE SET NULL,
            semantic_relation_id UUID,
            target_type VARCHAR(30) NOT NULL,
            target_id UUID NOT NULL,
            transform_rule TEXT,
            confidence VARCHAR(10) NOT NULL DEFAULT 'medium',
            status VARCHAR(20) NOT NULL DEFAULT 'unconfirmed',
            created_by VARCHAR(100),
            confirmed_by VARCHAR(100),
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_data_mappings_object_id ON data_mappings(semantic_object_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_data_mappings_property_id ON data_mappings(semantic_property_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_data_mappings_type ON data_mappings(mapping_type)")


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS data_mappings CASCADE")
    op.execute("DROP TABLE IF EXISTS semantic_properties CASCADE")
    op.execute("DROP TABLE IF EXISTS semantic_objects CASCADE")
