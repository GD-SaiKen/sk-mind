"""create semantic_relations + business_graph_edges tables

Revision ID: 022
Revises: 021
Create Date: 2026-08-03

Phase 2: 语义模型对象关系 — 类型层 semantic_relations（对象间关系定义）
+ 实例层 business_graph_edges（具体对象实例间的关系边）。
"""

from typing import Sequence, Union

from alembic import op

revision: str = "022"
down_revision: Union[str, None] = "021"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── 1. semantic_relations — 类型层：对象间关系定义 ──
    op.execute("""
        CREATE TABLE IF NOT EXISTS semantic_relations (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(200) NOT NULL,
            code VARCHAR(100) NOT NULL UNIQUE,
            relation_type VARCHAR(50) NOT NULL,
            subject_object_id UUID NOT NULL
                REFERENCES semantic_objects(id) ON DELETE CASCADE,
            object_object_id UUID NOT NULL
                REFERENCES semantic_objects(id) ON DELETE CASCADE,
            cardinality VARCHAR(10) NOT NULL,
            join_mechanism TEXT,
            description TEXT,
            agent_enabled BOOLEAN NOT NULL DEFAULT TRUE,
            status VARCHAR(20) NOT NULL DEFAULT 'draft',
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_semantic_relations_code"
        " ON semantic_relations(code)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_semantic_relations_subject"
        " ON semantic_relations(subject_object_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_semantic_relations_object"
        " ON semantic_relations(object_object_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_semantic_relations_relation_type"
        " ON semantic_relations(relation_type)"
    )

    # ── 2. business_graph_edges — 实例层：对象实例间关系边 ──
    op.execute("""
        CREATE TABLE IF NOT EXISTS business_graph_edges (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            relation_id UUID NOT NULL
                REFERENCES semantic_relations(id) ON DELETE CASCADE,
            from_object_id UUID NOT NULL
                REFERENCES semantic_objects(id),
            from_entity_id VARCHAR(200) NOT NULL,
            to_object_id UUID NOT NULL
                REFERENCES semantic_objects(id),
            to_entity_id VARCHAR(200) NOT NULL,
            edge_properties JSONB,
            source_dataset VARCHAR(300),
            generated_by VARCHAR(20) NOT NULL DEFAULT 'system',
            confidence DECIMAL(3,2) NOT NULL DEFAULT 0.90,
            status VARCHAR(20) NOT NULL DEFAULT 'pending',
            confirmed_by VARCHAR(100),
            confirmed_at TIMESTAMPTZ,
            valid_from TIMESTAMPTZ,
            valid_to TIMESTAMPTZ,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT uq_graph_edge
                UNIQUE (relation_id, from_object_id, from_entity_id,
                        to_object_id, to_entity_id)
        )
    """)
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_business_graph_edges_relation_id"
        " ON business_graph_edges(relation_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_business_graph_edges_from"
        " ON business_graph_edges(from_object_id, from_entity_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_business_graph_edges_to"
        " ON business_graph_edges(to_object_id, to_entity_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_business_graph_edges_status"
        " ON business_graph_edges(status)"
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS business_graph_edges CASCADE")
    op.execute("DROP TABLE IF EXISTS semantic_relations CASCADE")
