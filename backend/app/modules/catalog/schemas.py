"""Catalog 模块 Pydantic schemas。

数据目录 = 数据表元数据的业务投影。不建独立表，全通过 JOIN
datasets + dataset_fields + data_sources 组装。
"""

import uuid
from datetime import datetime
from typing import Optional

from app.core.schemas import CamelModel


# ── 列表 ──

class CatalogDatasetItem(CamelModel):
    """数据目录列表项 — 业务视角。"""

    id: uuid.UUID
    name: str
    display_name: Optional[str] = None
    code: str
    description: Optional[str] = None
    source_name: Optional[str] = None
    data_layer: str
    business_domain: Optional[str] = None
    updated_at: datetime
    quality_status: Optional[str] = None  # ok / warning / error
    permission_level: str = "internal"  # public / internal / sensitive / high_sensitive
    is_agent_accessible: bool = False
    record_count: Optional[int] = None
    field_count: Optional[int] = None


class CatalogDatasetListResponse(CamelModel):
    items: list[CatalogDatasetItem]
    total: int
    page: int = 1
    page_size: int = 20


# ── 字段目录 ──

class CatalogFieldItem(CamelModel):
    """字段目录列表项 — 跨数据集搜索。"""

    id: uuid.UUID
    field_name: str
    field_alias: Optional[str] = None
    description: Optional[str] = None
    data_type: str
    is_primary_key: bool = False
    is_sensitive: bool = False
    sensitivity_level: str = "internal"
    null_rate: Optional[float] = None
    dataset_name: str
    dataset_id: uuid.UUID


class CatalogFieldListResponse(CamelModel):
    items: list[CatalogFieldItem]
    total: int
    page: int = 1
    page_size: int = 20


# ── 详情 ──

class CatalogDatasetDetail(CatalogDatasetItem):
    """数据集详情 — 业务视角。"""

    agent_accessible_reason: Optional[str] = None
    fields: list[CatalogFieldItem] = []
    sensitive_fields: list[CatalogFieldItem] = []


# ── 统计 ──

class CatalogStatsResponse(CamelModel):
    total: int = 0
    quality_ok: int = 0
    quality_warning: int = 0
    agent_accessible: int = 0
    by_domain: list[dict] = []  # [{"domain": "工单域", "count": 9}, ...]
