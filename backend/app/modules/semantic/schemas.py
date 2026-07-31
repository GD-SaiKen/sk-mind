"""语义模型 Pydantic schemas。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import Field

from app.core.schemas import CamelModel


# ═══════════════════════════════════════════════════════
# SemanticObject
# ═══════════════════════════════════════════════════════

class SemanticObjectCreate(CamelModel):
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=100)
    description: Optional[str] = None
    object_type: str = Field(..., max_length=50)
    domain: Optional[str] = Field(None, max_length=100)
    status: str = "draft"


class SemanticObjectUpdate(CamelModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    object_type: Optional[str] = Field(None, max_length=50)
    domain: Optional[str] = Field(None, max_length=100)
    status: Optional[str] = None


class SemanticObjectResponse(CamelModel):
    id: uuid.UUID
    name: str
    code: str
    description: Optional[str] = None
    object_type: str
    domain: Optional[str] = None
    status: str
    property_count: int = 0
    mapping_count: int = 0
    created_at: datetime
    updated_at: datetime


class SemanticObjectListResponse(CamelModel):
    items: list[SemanticObjectResponse]
    total: int
    page: int = 1
    page_size: int = 20


# ═══════════════════════════════════════════════════════
# SemanticProperty
# ═══════════════════════════════════════════════════════

class SemanticPropertyCreate(CamelModel):
    semantic_object_id: uuid.UUID
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=100)
    description: Optional[str] = None
    property_type: str = Field(..., max_length=50)
    data_type: str = Field(..., max_length=50)
    is_required: bool = False
    is_sensitive: bool = False
    ordinal_position: int = 0
    status: str = "draft"


class SemanticPropertyUpdate(CamelModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    property_type: Optional[str] = Field(None, max_length=50)
    data_type: Optional[str] = Field(None, max_length=50)
    is_required: Optional[bool] = None
    is_sensitive: Optional[bool] = None
    ordinal_position: Optional[int] = None
    status: Optional[str] = None


class SemanticPropertyResponse(CamelModel):
    id: uuid.UUID
    semantic_object_id: uuid.UUID
    name: str
    code: str
    description: Optional[str] = None
    property_type: str
    data_type: str
    is_required: bool
    is_sensitive: bool
    ordinal_position: int
    status: str
    object_name: Optional[str] = None
    has_mapping: bool = False
    created_at: datetime
    updated_at: datetime


class SemanticPropertyListResponse(CamelModel):
    items: list[SemanticPropertyResponse]
    total: int


# ═══════════════════════════════════════════════════════
# DataMapping
# ═══════════════════════════════════════════════════════

class DataMappingCreate(CamelModel):
    mapping_type: str = Field(..., max_length=20)
    semantic_object_id: Optional[uuid.UUID] = None
    semantic_property_id: Optional[uuid.UUID] = None
    semantic_relation_id: Optional[uuid.UUID] = None
    target_type: str = Field(..., max_length=30)
    target_id: uuid.UUID
    transform_rule: Optional[str] = None
    confidence: str = "medium"
    status: str = "unconfirmed"
    created_by: Optional[str] = Field(None, max_length=100)


class DataMappingUpdate(CamelModel):
    mapping_type: Optional[str] = Field(None, max_length=20)
    target_type: Optional[str] = Field(None, max_length=30)
    target_id: Optional[uuid.UUID] = None
    transform_rule: Optional[str] = None
    confidence: Optional[str] = None
    status: Optional[str] = None
    confirmed_by: Optional[str] = Field(None, max_length=100)


class DataMappingResponse(CamelModel):
    id: uuid.UUID
    mapping_type: str
    semantic_object_id: Optional[uuid.UUID] = None
    semantic_property_id: Optional[uuid.UUID] = None
    semantic_relation_id: Optional[uuid.UUID] = None
    target_type: str
    target_id: uuid.UUID
    transform_rule: Optional[str] = None
    confidence: str
    status: str
    created_by: Optional[str] = None
    confirmed_by: Optional[str] = None
    semantic_object_name: Optional[str] = None
    semantic_property_name: Optional[str] = None
    target_name: Optional[str] = None
    target_table: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class DataMappingListResponse(CamelModel):
    items: list[DataMappingResponse]
    total: int
    page: int = 1
    page_size: int = 20


# ═══════════════════════════════════════════════════════
# Stats
# ═══════════════════════════════════════════════════════

class SemanticStatsResponse(CamelModel):
    total_objects: int = 0
    active_objects: int = 0
    total_properties: int = 0
    total_mappings: int = 0
    confirmed_mappings: int = 0
    by_object_type: list[dict] = []
    by_status: list[dict] = []
