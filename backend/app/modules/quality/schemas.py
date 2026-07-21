"""Quality 模块 Pydantic schemas。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, Field

from app.core.schemas import CamelModel


class QualityRuleCreate(CamelModel):
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=100)
    description: Optional[str] = None
    rule_type: str = Field(..., max_length=50)
    dataset_id: Optional[uuid.UUID] = None
    field_id: Optional[uuid.UUID] = None
    rule_params: Optional[dict] = None
    is_enabled: bool = True
    severity: str = "warning"


class QualityRuleUpdate(CamelModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    rule_type: Optional[str] = Field(None, max_length=50)
    dataset_id: Optional[uuid.UUID] = None
    field_id: Optional[uuid.UUID] = None
    rule_params: Optional[dict] = None
    is_enabled: Optional[bool] = None
    severity: Optional[str] = None


class QualityRuleResponse(CamelModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    code: str
    description: Optional[str] = None
    rule_type: str
    dataset_id: Optional[uuid.UUID] = None
    field_id: Optional[uuid.UUID] = None
    rule_params: Optional[dict] = None
    is_enabled: bool
    severity: str
    created_at: datetime
    updated_at: datetime


class QualityRuleListResponse(CamelModel):
    items: list[QualityRuleResponse]
    total: int
    page: int = 1
    page_size: int = 20


class QualityRunResponse(CamelModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    triggered_by: Optional[str] = None
    trigger_type: str
    rule_ids: Optional[str] = None
    dataset_ids: Optional[str] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    total_rules: int
    passed_rules: int
    failed_rules: int
    total_issues: int
    status: str
    created_at: datetime


class QualityRunListResponse(CamelModel):
    items: list[QualityRunResponse]
    total: int
    page: int = 1
    page_size: int = 20


class QualityIssueResponse(CamelModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    quality_run_id: uuid.UUID
    rule_id: uuid.UUID
    dataset_id: Optional[uuid.UUID] = None
    field_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    issue_type: str
    severity: str
    issue_message: str
    sample_value: Optional[str] = None
    sample_row: Optional[int] = None
    affected_record_count: Optional[int] = None
    status: str
    created_at: datetime


class QualityIssueListResponse(CamelModel):
    items: list[QualityIssueResponse]
    total: int
    page: int = 1
    page_size: int = 20


class QualityIssueStatusUpdate(CamelModel):
    status: str = Field(...)


class QualityStatsResponse(CamelModel):
    total_rules: int
    enabled_rules: int
    passed_count: int
    warning_count: int
    error_count: int
    pass_rate: float
    open_issues: int
