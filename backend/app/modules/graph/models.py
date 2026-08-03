"""业务关系图谱 ORM 模型 — 实例层关系边。

与 semantic_relations（类型层）配套：semantic_relations 定义「对象类型之间
允许存在什么关系」，business_graph_edges 记录「具体对象实例之间实际存在的
关系边」。
"""

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy import JSON as SqlJSON
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin


class BusinessGraphEdge(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """业务关系边 — 对象实例之间的实际关系。"""

    __tablename__ = "business_graph_edges"
    __table_args__ = (
        UniqueConstraint(
            "relation_id",
            "from_object_id",
            "from_entity_id",
            "to_object_id",
            "to_entity_id",
            name="uq_graph_edge",
        ),
    )

    relation_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("semantic_relations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    from_object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("semantic_objects.id"),
        nullable=False,
        index=True,
    )
    from_entity_id: Mapped[str] = mapped_column(String(200), nullable=False)

    to_object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("semantic_objects.id"),
        nullable=False,
        index=True,
    )
    to_entity_id: Mapped[str] = mapped_column(String(200), nullable=False)

    edge_properties: Mapped[Optional[dict]] = mapped_column(
        SqlJSON, nullable=True
    )
    source_dataset: Mapped[Optional[str]] = mapped_column(
        String(300), nullable=True
    )

    generated_by: Mapped[str] = mapped_column(
        String(20), default="system", nullable=False
    )  # system / mapping_rule / ai / manual
    confidence: Mapped[float] = mapped_column(
        Numeric(3, 2), default=0.90, nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False, index=True
    )  # pending / confirmed / rejected / insufficient

    confirmed_by: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True
    )
    confirmed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    valid_from: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    valid_to: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"<BusinessGraphEdge {self.from_entity_id}->{self.to_entity_id}>"
