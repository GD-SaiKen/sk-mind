"""Agent 模块 Pydantic schemas。"""

from typing import Any, Optional

from pydantic import Field

from app.core.schemas import CamelModel


class QueryObjectsRequest(CamelModel):
    source: str = Field(default="mes", max_length=50)
    object_name: str = Field(..., max_length=100)
    filters: Optional[dict[str, Any]] = None
    order_by: Optional[str] = None
    limit: int = Field(default=100, ge=1, le=10000)


class QueryMetricsRequest(CamelModel):
    source: str = Field(default="mes", max_length=50)
    metric_name: str = Field(..., max_length=100)
    group_by: Optional[list[str]] = None
    dimensions: Optional[list[str]] = None
    filters: Optional[dict[str, Any]] = None
    limit: int = Field(default=50, ge=1, le=10000)


class QueryObjectsResponse(CamelModel):
    columns: list[str]
    rows: list[dict[str, Any]]
    total: int


class QueryMetricsResponse(CamelModel):
    metric_name: str
    columns: list[str]
    rows: list[dict[str, Any]]
    total: int


class QueryRelationsRequest(CamelModel):
    source: str = Field(default="mes", max_length=50)
    relation_type: Optional[str] = Field(None, max_length=50)
    subject_object: Optional[str] = Field(None, max_length=100)
    object_object: Optional[str] = Field(None, max_length=100)
    agent_enabled_only: bool = False


class RelationItem(CamelModel):
    code: str
    name: str
    relation_type: str
    subject_object: str
    object_object: str
    cardinality: str
    join_mechanism: Optional[str] = None
    description: Optional[str] = None
    agent_enabled: bool


class QueryRelationsResponse(CamelModel):
    source: str
    relations: list[RelationItem]
    total: int


class QueryGraphRequest(CamelModel):
    source: str = Field(default="mes", max_length=50)
    object_type: Optional[str] = Field(None, max_length=100)
    entity_id: Optional[str] = Field(None, max_length=200)
    relation_code: Optional[str] = Field(None, max_length=100)
    hops: int = Field(default=2, ge=1, le=3)
    min_confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    confirmed_only: bool = False


class GraphPathEdgeItem(CamelModel):
    from_type: str
    from_id: str
    relation_code: str
    relation_name: str
    to_type: str
    to_id: str
    confidence: float
    status: str


class GraphPathItem(CamelModel):
    edges: list[GraphPathEdgeItem]


class QueryGraphResponse(CamelModel):
    source: str
    paths: list[GraphPathItem]
    hops: int
    total: int


class CatalogObject(CamelModel):
    name: str
    display_name: str
    description: str


class CatalogMetric(CamelModel):
    name: str
    display_name: str
    description: str
    source_object: str


class CatalogResponse(CamelModel):
    source: str
    objects: list[CatalogObject]
    metrics: list[CatalogMetric]
