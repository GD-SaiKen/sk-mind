"""Dataset 模块 Pydantic schemas。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import Field

from app.core.schemas import CamelModel


class DatasetCreate(CamelModel):
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=100)
    description: Optional[str] = None
    data_layer: str = Field(..., max_length=20)
    data_source_id: Optional[uuid.UUID] = None
    source_object_id: Optional[uuid.UUID] = None
    generated_by_task_id: Optional[uuid.UUID] = None
    last_batch_id: Optional[uuid.UUID] = None
    record_count: Optional[int] = None
    field_count: Optional[int] = None
    business_domain: Optional[str] = Field(None, max_length=100)
    owner_name: Optional[str] = Field(None, max_length=100)
    tags: Optional[str] = None
    sensitivity_level: str = "internal"
    is_agent_accessible: bool = False
    status: str = "draft"


class DatasetUpdate(CamelModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    data_layer: Optional[str] = Field(None, max_length=20)
    data_source_id: Optional[uuid.UUID] = None
    record_count: Optional[int] = None
    field_count: Optional[int] = None
    business_domain: Optional[str] = Field(None, max_length=100)
    owner_name: Optional[str] = Field(None, max_length=100)
    tags: Optional[str] = None
    sensitivity_level: Optional[str] = None
    is_agent_accessible: Optional[bool] = None
    status: Optional[str] = None


class DatasetResponse(CamelModel):

    id: uuid.UUID
    name: str
    code: str
    description: Optional[str] = None
    data_layer: str
    data_source_id: Optional[uuid.UUID] = None
    source_object_id: Optional[uuid.UUID] = None
    generated_by_task_id: Optional[uuid.UUID] = None
    last_batch_id: Optional[uuid.UUID] = None
    record_count: Optional[int] = None
    field_count: Optional[int] = None
    business_domain: Optional[str] = None
    owner_name: Optional[str] = None
    tags: Optional[str] = None
    sensitivity_level: str
    is_agent_accessible: bool
    agent_unavailable_reason: Optional[str] = None  # T6
    status: str
    source_name: Optional[str] = None  # derived from JOIN data_sources
    quality_status: Optional[str] = None  # ok / warning / error
    created_at: datetime
    updated_at: datetime


class DatasetListResponse(CamelModel):
    items: list[DatasetResponse]
    total: int
    page: int = 1
    page_size: int = 20


class DatasetFieldResponse(CamelModel):

    id: uuid.UUID
    dataset_id: uuid.UUID
    field_name: str
    field_alias: Optional[str] = None
    description: Optional[str] = None
    data_type: str
    field_length: Optional[int] = None
    is_nullable: bool
    ordinal_position: int
    sensitivity_level: str
    quality_status: Optional[str] = None
    is_primary_key: bool = False
    source_column: Optional[str] = None
    null_rate: Optional[float] = None  # T5
    sample_values: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class DatasetFieldListResponse(CamelModel):
    items: list[DatasetFieldResponse]
    total: int


class DataTableResponse(CamelModel):

    id: uuid.UUID
    dataset_id: Optional[uuid.UUID] = None
    schema_name: str
    table_name: str
    table_type: str
    description: Optional[str] = None
    row_count: Optional[int] = None
    data_size_bytes: Optional[int] = None
    created_at: datetime
    updated_at: datetime


class DataTableListResponse(CamelModel):
    items: list[DataTableResponse]
    total: int


# ── T4: 字段编辑/批量打标 ──

class DatasetFieldUpdate(CamelModel):
    """编辑单个字段的元数据。"""
    field_alias: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    sensitivity_level: Optional[str] = None  # internal / sensitive / high_sensitive


class DatasetFieldBatchUpdate(CamelModel):
    """批量更新字段元数据。"""
    field_ids: list[uuid.UUID]
    sensitivity_level: Optional[str] = None  # 批量修改敏感等级


# ── T5: 空值率统计 ──

class NullRateResult(CamelModel):
    field_name: str
    null_rate: Optional[float] = None  # 0.0 ~ 1.0


# ── T6: Agent 可用性检查 ──

class AgentCheckResponse(CamelModel):
    """Agent 可用性检查结果。"""
    passed: bool  # 是否通过所有检查
    reasons: list[str] = []  # 不通过的原因列表
    field_description_coverage: float = 0.0  # 字段说明覆盖率
    unmarked_sensitive_count: int = 0  # 未标记的敏感字段数
