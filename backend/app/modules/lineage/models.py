"""数据血缘 ORM 模型。

对应 PRD：来源到 Raw/Clean/Serving 层的链路追踪。
"""

import uuid
from typing import Optional

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin


class DataLineage(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """血缘边 — 记录数据从来源到目标数据集的流转链路。"""

    __tablename__ = "data_lineage"

    # 来源
    source_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # data_source / dataset / file / api
    source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True
    )
    source_name: Mapped[str] = mapped_column(String(300), nullable=False)

    # 目标
    target_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # dataset / dataset_field / metric / semantic_object
    target_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True
    )
    target_name: Mapped[str] = mapped_column(String(300), nullable=False)

    # 转换
    transform_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # raw_import / clean / serving / field_mapping
    transform_rule: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关联任务和批次
    ingestion_task_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_tasks.id"), nullable=True
    )
    batch_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_batches.id"), nullable=True, index=True
    )

    # 描述
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<DataLineage {self.source_name} -> {self.target_name}>"
