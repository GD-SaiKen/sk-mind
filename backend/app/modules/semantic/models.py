"""语义模型 ORM 模型 — 业务对象、对象属性、数据映射、语义关系。

Phase 1 覆盖 3 种元模型类型：
- semantic_objects → 业务对象
- semantic_properties → 对象属性
- data_mappings → 数据映射

Phase 2 新增：
- semantic_relations → 语义关系（类型层，对象间关系定义）
"""

import uuid
from typing import Optional

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin


class SemanticObject(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """业务对象定义 — 对应前端「业务对象」Tab。"""

    __tablename__ = "semantic_objects"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    object_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True
    )  # master_data / transaction / resource / process / event_state / metric / rule / data

    domain: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False, index=True
    )  # draft / active / archived

    def __repr__(self) -> str:
        return f"<SemanticObject {self.name}>"


class SemanticProperty(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """对象属性定义 — 对应前端「对象属性」Tab。"""

    __tablename__ = "semantic_properties"

    semantic_object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("semantic_objects.id"), nullable=False, index=True
    )

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    property_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # identifier / descriptive / status / temporal / measure / metric

    data_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # STRING / INTEGER / DECIMAL / DATE / DATETIME / BOOLEAN

    is_required: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_sensitive: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    ordinal_position: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False
    )  # draft / active / archived

    def __repr__(self) -> str:
        return f"<SemanticProperty {self.name}>"


class DataMapping(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """语义→数据资产映射 — 对应前端「数据映射」Tab。"""

    __tablename__ = "data_mappings"

    mapping_type: Mapped[str] = mapped_column(
        String(20), nullable=False, index=True
    )  # object / field / relation / metric

    semantic_object_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("semantic_objects.id"), nullable=True, index=True
    )
    semantic_property_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("semantic_properties.id"), nullable=True, index=True
    )
    semantic_relation_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), nullable=True
    )  # FK placeholder for Phase 2 semantic_relations

    target_type: Mapped[str] = mapped_column(
        String(30), nullable=False
    )  # dataset / dataset_field / data_source

    target_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False
    )

    transform_rule: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    confidence: Mapped[str] = mapped_column(
        String(10), default="medium", nullable=False
    )  # high / medium / low

    status: Mapped[str] = mapped_column(
        String(20), default="unconfirmed", nullable=False
    )  # confirmed / unconfirmed

    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    confirmed_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    def __repr__(self) -> str:
        return f"<DataMapping {self.mapping_type}>"


class SemanticRelation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """语义关系定义 — 类型层：业务对象之间的关系模板。"""

    __tablename__ = "semantic_relations"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
    relation_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True
    )  # structural / transactional / resource / process / responsibility / financial / quality / event

    subject_object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("semantic_objects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    object_object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("semantic_objects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    cardinality: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # 1:1 / 1:N / N:1 / N:M
    join_mechanism: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    agent_enabled: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False
    )  # draft / active / archived

    def __repr__(self) -> str:
        return f"<SemanticRelation {self.code}>"
