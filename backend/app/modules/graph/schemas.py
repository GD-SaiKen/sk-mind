"""graph 模块 Pydantic schemas — 业务关系边。"""

import uuid
from datetime import datetime
from typing import Any, Optional

from pydantic import Field

from app.core.schemas import CamelModel


class GraphEdgeResponse(CamelModel):
    id: uuid.UUID
    relation_id: uuid.UUID
    from_object_id: uuid.UUID
    from_entity_id: str
    to_object_id: uuid.UUID
    to_entity_id: str
    edge_properties: Optional[dict[str, Any]] = None
    source_dataset: Optional[str] = None
    generated_by: str
    confidence: float
    status: str
    confirmed_by: Optional[str] = None
    confirmed_at: Optional[datetime] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    relation_name: Optional[str] = None
    relation_code: Optional[str] = None
    from_object_name: Optional[str] = None
    to_object_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class GraphEdgeListResponse(CamelModel):
    items: list[GraphEdgeResponse]
    total: int
    page: int = 1
    page_size: int = 20


class GraphStatsResponse(CamelModel):
    total_edges: int = 0
    confirmed_count: int = 0
    ai_generated_count: int = 0
    pending_count: int = 0
    confirm_rate: float = 0.0


class GraphPathEdge(CamelModel):
    from_type: str
    from_id: str
    relation_code: str
    relation_name: str
    to_type: str
    to_id: str
    confidence: float
    status: str


class GraphPath(CamelModel):
    edges: list[GraphPathEdge]


class GraphQueryResponse(CamelModel):
    paths: list[GraphPath]
    hops: int
    total: int


class EdgeGenerateResponse(CamelModel):
    relation_code: str
    generated: int = 0
