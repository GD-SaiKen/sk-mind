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
