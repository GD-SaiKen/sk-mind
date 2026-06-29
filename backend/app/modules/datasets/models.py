"""数据集、字段与数据表 ORM 模型。

对应 PRD：Raw/Clean/Serving 数据集、字段元数据、数据表登记。
"""

import uuid
from typing import Optional

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Dataset(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """数据集 — 表示 Raw、Clean 或 Serving 层数据资产。"""

    __tablename__ = "datasets"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 数据分层
    data_layer: Mapped[str] = mapped_column(
        String(20), nullable=False, index=True
    )  # raw / clean / serving

    # 来源
    data_source_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("data_sources.id"), nullable=True
    )
    source_object_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("source_objects.id"), nullable=True
    )
    generated_by_task_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_tasks.id"), nullable=True
    )
    last_batch_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_batches.id"), nullable=True
    )

    # 元信息
    record_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    field_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # 业务信息
    business_domain: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    owner_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    tags: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON

    # 权限与状态
    sensitivity_level: Mapped[str] = mapped_column(
        String(20), default="internal", nullable=False
    )  # public / internal / sensitive / high_sensitive
    is_agent_accessible: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False, index=True
    )  # draft / active / archived

    def __repr__(self) -> str:
        return f"<Dataset {self.name}>"


class DatasetField(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """数据集字段元数据。"""

    __tablename__ = "dataset_fields"

    dataset_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("datasets.id"), nullable=False, index=True
    )

    # 字段基础信息
    field_name: Mapped[str] = mapped_column(String(200), nullable=False)
    field_alias: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 类型信息
    data_type: Mapped[str] = mapped_column(String(50), nullable=False)
    field_length: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_nullable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # 排序
    ordinal_position: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # 敏感等级
    sensitivity_level: Mapped[str] = mapped_column(
        String(20), default="internal", nullable=False
    )

    # 质量状态
    quality_status: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True
    )  # ok / warning / error / unknown

    # 样例值 (JSON)
    sample_values: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<DatasetField {self.field_name}>"


class DataTable(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """物理表或视图登记。"""

    __tablename__ = "data_tables"

    dataset_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("datasets.id"), nullable=True, index=True
    )

    schema_name: Mapped[str] = mapped_column(String(100), nullable=False)
    table_name: Mapped[str] = mapped_column(String(200), nullable=False)
    table_type: Mapped[str] = mapped_column(
        String(20), default="table", nullable=False
    )  # table / view / materialized_view
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    row_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    data_size_bytes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"<DataTable {self.schema_name}.{self.table_name}>"
