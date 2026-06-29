"""Auth 模块 Pydantic schemas — 请求/响应模型。"""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# ── 用户 ─────────────────────────────────────
class UserCreate(BaseModel):
    """创建用户请求。"""

    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)
    display_name: str = Field(..., min_length=1, max_length=100)
    department_id: Optional[uuid.UUID] = None


class UserUpdate(BaseModel):
    """更新用户请求。"""

    email: Optional[EmailStr] = None
    display_name: Optional[str] = Field(None, min_length=1, max_length=100)
    department_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    """用户响应（不含密码）。"""

    id: uuid.UUID
    username: str
    email: str
    display_name: str
    department_id: Optional[uuid.UUID] = None
    is_active: bool
    is_superuser: bool
    last_login_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserListResponse(BaseModel):
    """用户列表响应。"""

    items: list[UserResponse]
    total: int


# ── 认证 ─────────────────────────────────────
class LoginRequest(BaseModel):
    """登录请求。"""

    username: str
    password: str


class TokenResponse(BaseModel):
    """JWT Token 响应。"""

    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenRefreshRequest(BaseModel):
    """Token 刷新请求。"""

    access_token: str


# ── 角色 ─────────────────────────────────────
class RoleCreate(BaseModel):
    """创建角色请求。"""

    name: str = Field(..., min_length=1, max_length=100)
    code: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None


class RoleResponse(BaseModel):
    """角色响应。"""

    id: uuid.UUID
    name: str
    code: str
    description: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ── 权限 ─────────────────────────────────────
class PermissionCreate(BaseModel):
    """创建权限请求。"""

    name: str = Field(..., min_length=1, max_length=100)
    code: str = Field(..., min_length=1, max_length=100)
    resource: str = Field(..., min_length=1, max_length=100)
    action: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None


class PermissionResponse(BaseModel):
    """权限响应。"""

    id: uuid.UUID
    name: str
    code: str
    resource: str
    action: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


# ── 审计 ─────────────────────────────────────
class AuditLogResponse(BaseModel):
    """审计日志响应。"""

    id: uuid.UUID
    user_id: Optional[uuid.UUID] = None
    username: Optional[str] = None
    action: str
    resource: str
    resource_id: Optional[str] = None
    detail: Optional[str] = None
    ip_address: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class AuditLogListResponse(BaseModel):
    """审计日志列表响应。"""

    items: list[AuditLogResponse]
    total: int
