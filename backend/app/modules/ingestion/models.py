"""接入任务、批次与错误清单 ORM 模型。

对应 PRD：接入任务配置、执行批次、文件资产、错误清单和状态流转。
"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy import JSON as JSONB, Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin, _utcnow


class IngestionTask(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """接入任务 — 配置数据读取、清洗、写入规则。"""

    __tablename__ = "ingestion_tasks"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)

    data_source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("data_sources.id"), nullable=False, index=True
    )
    source_object_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("source_objects.id"), nullable=True
    )

    # 目标层级
    target_layer: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # raw / clean / serving

    # 调度策略
    schedule_type: Mapped[str] = mapped_column(
        String(20), default="manual", nullable=False
    )  # manual / cron / on_demand
    cron_expression: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    # 状态
    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False, index=True
    )  # draft / active / paused / disabled

    # 配置参数 (JSONB)
    config: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<IngestionTask {self.name}>"


class IngestionBatch(Base, UUIDPrimaryKeyMixin):
    """接入批次 — 每次任务执行记录。"""

    __tablename__ = "ingestion_batches"

    task_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_tasks.id"), nullable=False, index=True
    )

    # 执行信息
    triggered_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    trigger_type: Mapped[str] = mapped_column(
        String(20), default="manual", nullable=False
    )  # manual / scheduled / retry

    # 时间
    started_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    finished_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    # 数据量统计
    file_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    record_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    success_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    fail_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    skip_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # 状态
    status: Mapped[str] = mapped_column(
        String(30), default="pending", nullable=False, index=True
    )  # pending / running / success / partial_success / failed / canceled

    # 影响范围
    affected_datasets: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON

    error_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow, nullable=False, index=True
    )

    def __repr__(self) -> str:
        return f"<IngestionBatch {self.id} task={self.task_id}>"


class FileAsset(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """文件资产 — 目录扫描或上传的文件元数据。"""

    __tablename__ = "file_assets"

    data_source_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("data_sources.id"), nullable=True, index=True
    )
    ingestion_task_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_tasks.id"), nullable=True, index=True
    )
    batch_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_batches.id"), nullable=True, index=True
    )

    # 文件元数据
    file_name: Mapped[str] = mapped_column(String(500), nullable=False)
    file_path: Mapped[str] = mapped_column(String(1000), nullable=False)
    file_size: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    file_hash: Mapped[Optional[str]] = mapped_column(String(128), nullable=True, index=True)
    file_mtime: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    # 模板信息
    template_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    sheet_names: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON

    # 处理状态
    status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False
    )  # pending / parsing / parsed / failed / skipped

    row_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<FileAsset {self.file_name}>"


class ImportError(Base, UUIDPrimaryKeyMixin):
    """导入错误 — 文件级、行级、字段级错误明细。"""

    __tablename__ = "import_errors"

    batch_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_batches.id"), nullable=False, index=True
    )
    file_asset_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("file_assets.id"), nullable=True, index=True
    )

    # 错误位置
    error_level: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # file / row / field / structure
    sheet_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    row_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    field_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # 错误详情
    error_type: Mapped[str] = mapped_column(String(100), nullable=False)
    error_message: Mapped[str] = mapped_column(Text, nullable=False)
    raw_value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow, nullable=False, index=True
    )

    def __repr__(self) -> str:
        return f"<ImportError {self.error_type} at {self.error_level}>"
