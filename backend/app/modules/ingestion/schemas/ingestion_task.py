"""接入任务 Schemas — Pydantic 请求/响应模型。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import Field

from app.core.schemas import CamelModel


# ── 请求 ─────────────────────────────────────

class IngestionTaskCreate(CamelModel):
    """创建接入任务请求。"""

    name: str = Field(..., max_length=200, description="任务名称")
    code: str = Field(..., max_length=100, description="任务编码（唯一）")
    data_source_id: uuid.UUID = Field(..., description="关联数据源 ID")
    source_object_id: Optional[uuid.UUID] = Field(None, description="关联来源对象 ID")
    target_layer: str = Field("raw", description="目标层级 raw/clean/serving")
    sync_mode: str = Field("full", description="同步模式 full/incremental")
    schedule_type: str = Field("manual", description="调度方式 manual/cron/on_demand")
    cron_expression: Optional[str] = Field(None, max_length=50, description="Cron 表达式")
    config: Optional[dict] = Field(None, description="任务配置 JSON")
    description: Optional[str] = Field(None, description="任务描述")


class IngestionTaskUpdate(CamelModel):
    """更新接入任务请求。"""

    name: Optional[str] = Field(None, max_length=200, description="任务名称")
    target_layer: Optional[str] = Field(None, description="目标层级")
    sync_mode: Optional[str] = Field(None, description="同步模式 full/incremental")
    schedule_type: Optional[str] = Field(None, description="调度方式")
    cron_expression: Optional[str] = Field(None, max_length=50, description="Cron 表达式")
    config: Optional[dict] = Field(None, description="任务配置 JSON")
    description: Optional[str] = Field(None, description="任务描述")


# ── 响应 ─────────────────────────────────────

class IngestionTaskResponse(CamelModel):
    """接入任务响应。"""

    id: uuid.UUID
    name: str
    code: str
    data_source_id: uuid.UUID
    source_object_id: Optional[uuid.UUID] = None
    target_layer: str
    sync_mode: str
    schedule_type: str
    cron_expression: Optional[str] = None
    last_sync_at: Optional[datetime] = None
    last_sync_status: Optional[str] = None
    status: str
    config: Optional[dict] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class IngestionBatchResponse(CamelModel):
    """接入批次响应。"""

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
    progress_step: Optional[str] = None
    source_signature: Optional[str] = None
    rejected_rows: Optional[str] = None
    created_at: datetime


class BatchProgressResponse(CamelModel):
    """批次实时进度响应。"""

    batchId: str
    status: str
    progress: int = Field(..., ge=-1, le=100, description="进度百分比 -1=未知, 0-100=已知")
    step: str = Field("", description="当前步骤描述")
    lastHeartbeat: Optional[datetime] = None


class ImportErrorResponse(CamelModel):
    """导入错误响应。"""

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


# ── 时间范围 / 快补 ───────────────────────────

class QuickFillRequest(CamelModel):
    """近期快补请求 — 指定起止时间拉取数据。"""

    start_time: datetime = Field(..., description="开始时间（含）")
    end_time: datetime = Field(..., description="结束时间（含）")


class TimeRangeResponse(CamelModel):
    """时间范围预览响应 — 展示建议的同步范围，不触发同步。"""

    sync_mode: str
    last_sync_at: Optional[datetime] = None
    suggested_start: Optional[datetime] = None
    suggested_end: Optional[datetime] = None
    next_scheduled_run: Optional[datetime] = None
    schedule_cron: Optional[str] = None
    schedule_description: Optional[str] = None


# ── 隔离区（B2.6）─────────────────────────────

class QuarantineResponse(CamelModel):
    """隔离区单条记录响应。"""

    id: uuid.UUID
    batchId: uuid.UUID
    dataSourceId: uuid.UUID
    interfaceName: str
    pkValue: Optional[str] = None
    rejectionReason: str
    rawJson: dict
    status: str
    retriedAt: Optional[datetime] = None
    resolvedAt: Optional[datetime] = None
    createdAt: datetime


class QuarantineStatsResponse(CamelModel):
    """隔离区统计响应。"""

    total: int
    pending: int
    resolved: int
    ignored: int
    quarantineRate: float
    threshold: float
    circuitBreakerTriggered: bool
