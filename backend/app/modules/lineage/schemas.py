"""Lineage 模块 Pydantic schemas。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, Field

from app.core.schemas import CamelModel


class LineageEdgeCreate(CamelModel):
    source_type: str = Field(..., max_length=50)
    source_id: uuid.UUID
    source_name: str = Field(..., max_length=300)
    target_type: str = Field(..., max_length=50)
    target_id: uuid.UUID
    target_name: str = Field(..., max_length=300)
    transform_type: str = Field(..., max_length=50)
    transform_rule: Optional[str] = None
    ingestion_task_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    description: Optional[str] = None


class LineageEdgeUpdate(CamelModel):
    source_name: Optional[str] = Field(None, max_length=300)
    target_name: Optional[str] = Field(None, max_length=300)
    transform_type: Optional[str] = Field(None, max_length=50)
    transform_rule: Optional[str] = None
    description: Optional[str] = None


class LineageEdgeResponse(CamelModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    source_type: str
    source_id: uuid.UUID
    source_name: str
    target_type: str
    target_id: uuid.UUID
    target_name: str
    transform_type: str
    transform_rule: Optional[str] = None
    ingestion_task_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class LineageEdgeListResponse(CamelModel):
    items: list[LineageEdgeResponse]
    total: int
    page: int = 1
    page_size: int = 20


class LineageStatsResponse(CamelModel):
    total_edges: int
    confirmed_count: int
    ai_generated_count: int
    pending_count: int
    confirm_rate: float
