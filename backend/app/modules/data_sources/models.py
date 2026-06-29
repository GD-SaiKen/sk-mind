"""数据源管理 ORM 模型。

对应 PRD：数据源登记、连接配置、负责人、敏感等级和状态管理。
"""

import uuid
from typing import Optional

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, UUIDPrimaryKeyMixin


class DataSource(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """数据源登记。"""

    __tablename__ = "data_sources"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 数据源类型
    source_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True
    )  # excel / csv / database / api / shared_folder

    # 接入方式
    access_method: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # file_upload / directory_scan / db_sync / api_pull

    # 负责人
    owner_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    owner_dept: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    contact_info: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # 敏感等级
    sensitivity_level: Mapped[str] = mapped_column(
        String(20), default="internal", nullable=False
    )  # public / internal / sensitive / high_sensitive

    # 状态
    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False, index=True
    )  # draft / active / paused / archived

    # 权限
    is_agent_accessible: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # 标签
    tags: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON array as text

    def __repr__(self) -> str:
        return f"<DataSource {self.name}>"


class SourceObject(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """来源对象 — 数据源中的具体表、文件、接口。"""

    __tablename__ = "source_objects"

    data_source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("data_sources.id"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    object_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # table / view / file / api_endpoint / sheet
    object_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    schema_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    row_count_estimate: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def __repr__(self) -> str:
        return f"<SourceObject {self.name}>"


class ConnectorConfig(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """连接配置 — 加密保存凭据摘要。"""

    __tablename__ = "connector_configs"

    data_source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("data_sources.id"), nullable=False, index=True
    )
    config_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # db_connection / file_path / api_config
    host: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    port: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    database_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    username: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    # 凭据只保存加密引用摘要，不保存明文
    credential_ref: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    extra_config: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON
    is_validated: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"<ConnectorConfig for {self.data_source_id}>"
