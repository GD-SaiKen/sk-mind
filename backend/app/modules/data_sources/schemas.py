"""DataSource 模块 Pydantic schemas。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, Field

from app.core.schemas import CamelModel


class DataSourceCreate(CamelModel):
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=100)
    source_type: str = Field(..., max_length=50)
    access_method: str = Field(..., max_length=50)
    description: Optional[str] = None
    owner_name: Optional[str] = Field(None, max_length=100)
    owner_dept: Optional[str] = Field(None, max_length=100)
    contact_info: Optional[str] = Field(None, max_length=200)
    sensitivity_level: str = "internal"


class DataSourceUpdate(CamelModel):
    name: Optional[str] = Field(None, max_length=200)
    source_type: Optional[str] = Field(None, max_length=50)
    access_method: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = None
    owner_name: Optional[str] = Field(None, max_length=100)
    owner_dept: Optional[str] = Field(None, max_length=100)
    contact_info: Optional[str] = Field(None, max_length=200)
    sensitivity_level: Optional[str] = None
    status: Optional[str] = None


class DataSourceResponse(CamelModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    code: str
    source_type: str
    access_method: str
    description: Optional[str] = None
    owner_name: Optional[str] = None
    owner_dept: Optional[str] = None
    contact_info: Optional[str] = None
    sensitivity_level: str
    status: str
    is_agent_accessible: bool = False
    created_at: datetime
    updated_at: datetime


class DataSourceListResponse(CamelModel):
    items: list[DataSourceResponse]
    total: int
