"""Auth 模块业务服务 — 用户、角色、权限 CRUD 和认证逻辑。"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, hash_password, verify_password
from app.modules.auth.models import (
    AuditLog,
    Department,
    Permission,
    Role,
    RolePermission,
    User,
    UserRole,
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
    """创建新用户。"""
    user = User(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password),
        display_name=data.display_name,
        department_id=data.department_id,
    )
    db.add(user)
    await db.flush()
    await db.refresh(user)
    return user


async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> Optional[User]:
    """按 ID 查询用户。"""
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_user_by_username(db: AsyncSession, username: str) -> Optional[User]:
    """按用户名查询用户。"""
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    """按邮箱查询用户。"""
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def list_users(
    db: AsyncSession, skip: int = 0, limit: int = 50
) -> tuple[list[User], int]:
    """分页查询用户列表。"""
    count_q = await db.execute(select(func.count(User.id)))
    total = count_q.scalar() or 0

    q = select(User).offset(skip).limit(limit).order_by(User.created_at.desc())
    result = await db.execute(q)
    return list(result.scalars().all()), total


async def update_user(
    db: AsyncSession, user: User, data: UserUpdate
) -> User:
    """更新用户信息。"""
    if data.email is not None:
        user.email = data.email
    if data.display_name is not None:
        user.display_name = data.display_name
    if data.department_id is not None:
        user.department_id = data.department_id
    if data.is_active is not None:
        user.is_active = data.is_active

    await db.flush()
    await db.refresh(user)
    return user


async def authenticate_user(
    db: AsyncSession, username: str, password: str
) -> Optional[User]:
    """验证用户名密码，返回用户或 None。"""
    user = await get_user_by_username(db, username)
    if user is None or not user.is_active:
        return None
    if not verify_password(password, user.hashed_password):
        return None

    # 更新登录时间
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
    db.add(role)
    await db.flush()
    await db.refresh(role)
    return role


async def list_roles(db: AsyncSession) -> list[Role]:
    """查询所有角色。"""
    result = await db.execute(select(Role).order_by(Role.created_at.desc()))
    return list(result.scalars().all())


async def assign_role_to_user(
    db: AsyncSession, user_id: uuid.UUID, role_id: uuid.UUID
) -> UserRole:
    """为用户分配角色。"""
    ur = UserRole(user_id=user_id, role_id=role_id)
    db.add(ur)
    await db.flush()
    return ur


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
    db.add(perm)
    await db.flush()
    await db.refresh(perm)
    return perm


async def list_permissions(db: AsyncSession) -> list[Permission]:
    """查询所有权限点。"""
    result = await db.execute(select(Permission).order_by(Permission.resource))
    return list(result.scalars().all())


async def assign_permission_to_role(
    db: AsyncSession, role_id: uuid.UUID, permission_id: uuid.UUID
) -> RolePermission:
    """为角色分配权限。"""
    rp = RolePermission(role_id=role_id, permission_id=permission_id)
    db.add(rp)
    await db.flush()
    return rp


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
    db.add(log)
    await db.flush()
    return log


async def list_audit_logs(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 50,
    user_id: Optional[uuid.UUID] = None,
    action: Optional[str] = None,
    resource: Optional[str] = None,
) -> tuple[list[AuditLog], int]:
    """分页查询审计日志，支持按用户、操作、资源筛选。"""
    conditions = []
    if user_id:
        conditions.append(AuditLog.user_id == user_id)
    if action:
        conditions.append(AuditLog.action == action)
    if resource:
        conditions.append(AuditLog.resource == resource)

    count_q = select(func.count(AuditLog.id))
    if conditions:
        count_q = count_q.where(*conditions)
    total_result = await db.execute(count_q)
    total = total_result.scalar() or 0

    q = select(AuditLog).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit)
    if conditions:
        q = q.where(*conditions)
    result = await db.execute(q)
    return list(result.scalars().all()), total
