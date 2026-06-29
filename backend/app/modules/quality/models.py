"""数据质量规则、检查执行与问题记录 ORM 模型。

对应 PRD：非空、唯一、枚举、范围、格式检查和质量问题。
"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy import JSON as JSONB, Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin, _utcnow


class QualityRule(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """质量规则定义。"""

    __tablename__ = "quality_rules"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 规则类型
    rule_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True
    )  # not_null / unique / enum / range / format / freshness / completeness

    # 作用范围
    dataset_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("datasets.id"), nullable=True, index=True
    )
    field_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("dataset_fields.id"), nullable=True, index=True
    )

    # 规则参数 (JSONB)
    rule_params: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    # 状态
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    severity: Mapped[str] = mapped_column(
        String(20), default="warning", nullable=False
    )  # info / warning / error / critical

    def __repr__(self) -> str:
        return f"<QualityRule {self.name}>"


class QualityRun(Base, UUIDPrimaryKeyMixin):
    """质量检查执行记录。"""

    __tablename__ = "quality_runs"

    # 触发信息
    triggered_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    trigger_type: Mapped[str] = mapped_column(
        String(20), default="manual", nullable=False
    )  # manual / scheduled / on_ingestion

    # 执行范围
    rule_ids: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON
    dataset_ids: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON

    # 时间
    started_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    finished_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    # 统计
    total_rules: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    passed_rules: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    failed_rules: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    total_issues: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    status: Mapped[str] = mapped_column(
        String(20), default="running", nullable=False
    )  # running / completed / failed

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow, nullable=False, index=True
    )

    def __repr__(self) -> str:
        return f"<QualityRun {self.id}>"


class QualityIssue(Base, UUIDPrimaryKeyMixin):
    """质量问题记录。"""

    __tablename__ = "quality_issues"

    quality_run_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("quality_runs.id"), nullable=False, index=True
    )
    rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("quality_rules.id"), nullable=False, index=True
    )

    # 问题位置
    dataset_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("datasets.id"), nullable=True, index=True
    )
    field_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("dataset_fields.id"), nullable=True, index=True
    )
    batch_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("ingestion_batches.id"), nullable=True
    )

    # 问题详情
    issue_type: Mapped[str] = mapped_column(String(50), nullable=False)
    severity: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # info / warning / error / critical
    issue_message: Mapped[str] = mapped_column(Text, nullable=False)

    # 样例数据
    sample_value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sample_row: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # 影响范围
    affected_record_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # 处理状态
    status: Mapped[str] = mapped_column(
        String(20), default="open", nullable=False
    )  # open / acknowledged / resolved / ignored

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_utcnow, nullable=False, index=True
    )

    def __repr__(self) -> str:
        return f"<QualityIssue {self.issue_type}>"
