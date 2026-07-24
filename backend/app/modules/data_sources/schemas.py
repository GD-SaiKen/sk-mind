"""DataSource 模块 Pydantic schemas。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import Field

from app.core.schemas import CamelModel


class ConnectionConfigSchema(CamelModel):
    """数据源连接配置。

    API 拉取场景存 base_url / 鉴权方式 / 凭据等；
    数据库同步场景后续扩展 host / port / database 等。
    凭据当前明文存于 extra_config JSON，后续迁移到加密存储。
    """

    # ── API 通用 ──
    base_url: Optional[str] = Field(None, description="API 基础路径")
    auth_type: Optional[str] = Field(
        None, description="鉴权方式：none/bearer/basic/api_key/dual_key/session"
    )
    auth_header_name: Optional[str] = Field(None, description="鉴权 Header 名")
    auth_credentials: Optional[str] = Field(None, description="凭据/密钥")
    auth_header_name_2: Optional[str] = Field(None, description="第二鉴权 Header 名（dual_key）")
    auth_credentials_2: Optional[str] = Field(None, description="第二凭据（dual_key）")
    qps_limit: Optional[int] = Field(None, description="QPS 限制")
    timeout: Optional[int] = Field(None, description="超时秒数")
    ssl_verify: Optional[bool] = Field(None, description="是否验证 SSL 证书")
    records_path: Optional[str] = Field(None, description="响应记录列表路径")
    total_path: Optional[str] = Field(None, description="响应总数路径")


class DataSourceCreate(CamelModel):
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=100)
    source_type: str = Field(..., max_length=50)
    access_method: str = Field(..., max_length=50)
    description: Optional[str] = None
    business_owner: Optional[str] = Field(None, max_length=100)
    owner_dept: Optional[str] = Field(None, max_length=100)
    tech_owner: Optional[str] = Field(None, max_length=200)
    sensitivity_level: str = "internal"
    connection_config: Optional[ConnectionConfigSchema] = None


class DataSourceUpdate(CamelModel):
    name: Optional[str] = Field(None, max_length=200)
    source_type: Optional[str] = Field(None, max_length=50)
    access_method: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = None
    business_owner: Optional[str] = Field(None, max_length=100)
    owner_dept: Optional[str] = Field(None, max_length=100)
    tech_owner: Optional[str] = Field(None, max_length=200)
    sensitivity_level: Optional[str] = None
    status: Optional[str] = None
    connection_config: Optional[ConnectionConfigSchema] = None


class DataSourceResponse(CamelModel):

    id: uuid.UUID
    name: str
    code: str
    source_type: str
    access_method: str
    description: Optional[str] = None
    business_owner: Optional[str] = None
    owner_dept: Optional[str] = None
    tech_owner: Optional[str] = None
    sensitivity_level: str
    status: str
    is_agent_accessible: bool = False
    source_category: Optional[str] = None
    connection_status: Optional[str] = None
    last_health_check_at: Optional[datetime] = None
    task_count: int = 0
    last_sync_at: Optional[datetime] = None
    connection_config: Optional[ConnectionConfigSchema] = None
    created_at: datetime
    updated_at: datetime


class DataSourceListResponse(CamelModel):
    items: list[DataSourceResponse]
    total: int


class InterfaceItem(CamelModel):
    """Single API interface entry returned by GET /data-sources/{id}/interfaces."""
    name: str
    endpoint: str
    method: str = "POST"
    target_table: str = ""
    order: int = 0
    is_time_based: bool = True
    pk_fields: list[str] = []
