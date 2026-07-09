"""接入任务 Schemas — Pydantic 请求/响应模型。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


def _to_camel(snake: str) -> str:
    """snake_case → camelCase"""
    parts = snake.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class CamelModel(BaseModel):
    """自动将 snake_case 字段转为 camelCase 别名的基础模型。"""
    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,  # 允许同时使用 snake_case 和 camelCase
    )


# ── 请求 ─────────────────────────────────────

class IngestionTaskCreate(CamelModel):
    """创建接入任务请求。"""

    name: str = Field(..., max_length=200, description="任务名称")
    code: str = Field(..., max_length=100, description="任务编码（唯一）")
    data_source_id: uuid.UUID = Field(..., description="关联数据源 ID")
    source_object_id: Optional[uuid.UUID] = Field(None, description="关联来源对象 ID")
    target_layer: str = Field("raw", description="目标层级 raw/clean/serving")
    schedule_type: str = Field("manual", description="调度方式 manual/cron/on_demand")
    cron_expression: Optional[str] = Field(None, max_length=50, description="Cron 表达式")
    config: Optional[dict] = Field(None, description="任务配置 JSON")
    description: Optional[str] = Field(None, description="任务描述")


class IngestionTaskUpdate(CamelModel):
    """更新接入任务请求。"""

    name: Optional[str] = Field(None, max_length=200, description="任务名称")
    target_layer: Optional[str] = Field(None, description="目标层级")
    schedule_type: Optional[str] = Field(None, description="调度方式")
    cron_expression: Optional[str] = Field(None, max_length=50, description="Cron 表达式")
    config: Optional[dict] = Field(None, description="任务配置 JSON")
    description: Optional[str] = Field(None, description="任务描述")


# ── 响应 ─────────────────────────────────────

class IngestionTaskResponse(CamelModel):
    """接入任务响应。"""

    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    id: uuid.UUID
    name: str
    code: str
    data_source_id: uuid.UUID
    source_object_id: Optional[uuid.UUID] = None
    target_layer: str
    schedule_type: str
    cron_expression: Optional[str] = None
    status: str
    config: Optional[dict] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class IngestionBatchResponse(CamelModel):
    """接入批次响应。"""

    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    id: uuid.UUID
    task_id: uuid.UUID
    triggered_by: Optional[str] = None
    trigger_type: str
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    file_count: int
    record_count: int
    success_count: int
    fail_count: int
    skip_count: int
    status: str
    affected_datasets: Optional[str] = None
    error_summary: Optional[str] = None
    created_at: datetime


class BatchProgressResponse(CamelModel):
    """批次实时进度响应。"""

    batchId: str
    status: str
    progress: int = Field(..., ge=0, le=100, description="进度百分比 0-100")
    step: str = Field("", description="当前步骤描述")
    lastHeartbeat: Optional[datetime] = None


class ImportErrorResponse(CamelModel):
    """导入错误响应。"""

    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    id: uuid.UUID
    batch_id: uuid.UUID
    error_level: str
    sheet_name: Optional[str] = None
    row_number: Optional[int] = None
    field_name: Optional[str] = None
    error_type: str
    error_message: str
    raw_value: Optional[str] = None
    created_at: datetime
