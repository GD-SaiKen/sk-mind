"""Auth API 路由 — 登录、注册、Token 刷新、用户管理。"""

import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_superuser, get_current_user
from app.modules.auth.models import User
from app.modules.auth.schemas import (
    AuditLogListResponse,
    AuditLogResponse,
    LoginRequest,
    PermissionCreate,
    PermissionResponse,
    RoleCreate,
    RoleResponse,
    TokenResponse,
    UserCreate,
    UserListResponse,
    UserResponse,
    UserUpdate,
)
from app.modules.auth import services as auth_svc

router = APIRouter(prefix="/auth", tags=["auth"])


# ── 认证接口 ─────────────────────────────────

@router.post("/login", response_model=TokenResponse)
async def login(
    request: Request,
    data: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    """用户登录，返回 JWT token。"""
    user = await auth_svc.authenticate_user(db, data.username, data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )

    token = auth_svc.create_user_token(user)

    # 审计日志
    await auth_svc.write_audit_log(
        db,
        action="login",
        resource="auth",
        user_id=user.id,
        username=user.username,
        detail=f"User {user.username} logged in",
        ip_address=request.client.host if request.client else None,
    )

    return TokenResponse(
        access_token=token,
        user=UserResponse.model_validate(user),
    )


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    request: Request,
    data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    """注册新用户。"""
    # 检查用户名和邮箱唯一性
    existing_user = await auth_svc.get_user_by_username(db, data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="用户名已存在",
        )
    existing_email = await auth_svc.get_user_by_email(db, data.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="邮箱已被注册",
        )

    user = await auth_svc.create_user(db, data)

    await auth_svc.write_audit_log(
        db,
        action="register",
        resource="auth",
        user_id=user.id,
        username=user.username,
        detail=f"User {user.username} registered",
        ip_address=request.client.host if request.client else None,
    )

    return UserResponse.model_validate(user)


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    current_user: User = Depends(get_current_user),
):
    """刷新 JWT token。"""
    token = auth_svc.create_user_token(current_user)
    return TokenResponse(
        access_token=token,
        user=UserResponse.model_validate(current_user),
    )


@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: User = Depends(get_current_user),
):
    """获取当前登录用户信息。"""
    return UserResponse.model_validate(current_user)


# ── 用户管理接口（管理员）───────────────────

@router.get("/users", response_model=UserListResponse)
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """查询用户列表（管理员）。"""
    users, total = await auth_svc.list_users(db, skip, limit)
    return UserListResponse(
        items=[UserResponse.model_validate(u) for u in users],
        total=total,
    )


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """查询单个用户（管理员）。"""
    user = await auth_svc.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    return UserResponse.model_validate(user)


@router.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: uuid.UUID,
    data: UserUpdate,
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """更新用户信息（管理员）。"""
    user = await auth_svc.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    user = await auth_svc.update_user(db, user, data)
    return UserResponse.model_validate(user)


# ── 角色管理接口（管理员）───────────────────

@router.post("/roles", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
async def create_role(
    data: RoleCreate,
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """创建角色（管理员）。"""
    role = await auth_svc.create_role(db, data)
    return RoleResponse.model_validate(role)


@router.get("/roles", response_model=list[RoleResponse])
async def list_roles(
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """查询角色列表（管理员）。"""
    roles = await auth_svc.list_roles(db)
    return [RoleResponse.model_validate(r) for r in roles]


@router.post("/roles/{role_id}/users/{user_id}", status_code=status.HTTP_201_CREATED)
async def assign_role(
    role_id: uuid.UUID,
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """为用户分配角色（管理员）。"""
    await auth_svc.assign_role_to_user(db, user_id, role_id)
    return {"detail": "角色分配成功"}


# ── 权限管理接口（管理员）───────────────────

@router.post("/permissions", response_model=PermissionResponse, status_code=status.HTTP_201_CREATED)
async def create_permission(
    data: PermissionCreate,
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """创建权限点（管理员）。"""
    perm = await auth_svc.create_permission(db, data)
    return PermissionResponse.model_validate(perm)


@router.get("/permissions", response_model=list[PermissionResponse])
async def list_permissions(
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """查询权限列表（管理员）。"""
    perms = await auth_svc.list_permissions(db)
    return [PermissionResponse.model_validate(p) for p in perms]


# ── 审计日志接口（管理员）───────────────────

@router.get("/audit-logs", response_model=AuditLogListResponse)
async def list_audit_logs(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    user_id: Optional[uuid.UUID] = None,
    action: Optional[str] = None,
    resource: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    _superuser: User = Depends(get_current_superuser),
):
    """查询审计日志（管理员）。"""
    logs, total = await auth_svc.list_audit_logs(
        db, skip=skip, limit=limit, user_id=user_id, action=action, resource=resource
    )
    return AuditLogListResponse(
        items=[AuditLogResponse.model_validate(l) for l in logs],
        total=total,
    )
