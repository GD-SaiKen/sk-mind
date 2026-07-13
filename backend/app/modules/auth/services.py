"""Auth 模块业务服务 — 用户、角色、权限 CRUD 和认证逻辑。"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, hash_password, verify_password
from app.modules.auth import dao
from app.modules.auth.models import (
    AuditLog,
    Permission,
    Role,
    User,
)
from app.modules.auth.schemas import (
    PermissionCreate,
    RoleCreate,
    UserCreate,
    UserUpdate,
)


# ═══════════════════════════════════════════
# 用户服务
# ═══════════════════════════════════════════

async def create_user(db: AsyncSession, data: UserCreate) -> User:
    """创建新用户（含密码哈希）。"""
    user = User(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password),
        display_name=data.display_name,
        department_id=data.department_id,
    )
    return await dao.user_insert(db, user)


# 委托 DAO 的纯查询
get_user_by_id = dao.user_get_by_id
get_user_by_username = dao.user_get_by_username
get_user_by_email = dao.user_get_by_email
list_users = dao.user_list


async def update_user(db: AsyncSession, user: User, data: UserUpdate) -> User:
    """更新用户信息。"""
    if data.email is not None:
        user.email = data.email
    if data.display_name is not None:
        user.display_name = data.display_name
    if data.department_id is not None:
        user.department_id = data.department_id
    if data.is_active is not None:
        user.is_active = data.is_active
    return await dao.user_update(db, user)


async def authenticate_user(
    db: AsyncSession, username: str, password: str
) -> Optional[User]:
    """验证用户名密码，返回用户或 None。"""
    user = await dao.user_get_by_username(db, username)
    if user is None or not user.is_active:
        return None
    if not verify_password(password, user.hashed_password):
        return None

    user.last_login_at = datetime.now(timezone.utc)
    await db.flush()
    return user


def create_user_token(user: User) -> str:
    """为用户签发 JWT token。"""
    return create_access_token(subject=str(user.id))


# ═══════════════════════════════════════════
# 角色服务
# ═══════════════════════════════════════════

async def create_role(db: AsyncSession, data: RoleCreate) -> Role:
    """创建角色。"""
    role = Role(name=data.name, code=data.code, description=data.description)
    return await dao.role_insert(db, role)


list_roles = dao.role_list
assign_role_to_user = dao.user_role_insert


# ═══════════════════════════════════════════
# 权限服务
# ═══════════════════════════════════════════

async def create_permission(db: AsyncSession, data: PermissionCreate) -> Permission:
    """创建权限点。"""
    perm = Permission(
        name=data.name,
        code=data.code,
        resource=data.resource,
        action=data.action,
        description=data.description,
    )
    return await dao.permission_insert(db, perm)


list_permissions = dao.permission_list
assign_permission_to_role = dao.role_permission_insert


# ═══════════════════════════════════════════
# 审计服务
# ═══════════════════════════════════════════

async def write_audit_log(
    db: AsyncSession,
    action: str,
    resource: str,
    user_id: Optional[uuid.UUID] = None,
    username: Optional[str] = None,
    resource_id: Optional[str] = None,
    detail: Optional[str] = None,
    ip_address: Optional[str] = None,
) -> AuditLog:
    """写入审计日志。"""
    log = AuditLog(
        user_id=user_id,
        username=username,
        action=action,
        resource=resource,
        resource_id=resource_id,
        detail=detail,
        ip_address=ip_address,
    )
    return await dao.audit_log_insert(db, log)


list_audit_logs = dao.audit_log_list
