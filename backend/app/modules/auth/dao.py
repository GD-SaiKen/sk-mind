"""Auth 模块数据访问层 — 纯数据库 CRUD 操作，不含业务逻辑。"""

import uuid
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.models import (
    AuditLog,
    Permission,
    Role,
    RolePermission,
    User,
    UserRole,
)


# ═══════════════════════════════════════════
# 用户
# ═══════════════════════════════════════════

async def user_get_by_id(db: AsyncSession, user_id: uuid.UUID) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def user_get_by_username(db: AsyncSession, username: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()


async def user_get_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def user_list(
    db: AsyncSession, skip: int = 0, limit: int = 50
) -> tuple[list[User], int]:
    total_q = await db.execute(select(func.count(User.id)))
    total = total_q.scalar() or 0
    q = select(User).offset(skip).limit(limit).order_by(User.created_at.desc())
    result = await db.execute(q)
    return list(result.scalars().all()), total


async def user_insert(db: AsyncSession, user: User) -> User:
    db.add(user)
    await db.flush()
    await db.refresh(user)
    return user


async def user_update(db: AsyncSession, user: User) -> User:
    await db.flush()
    await db.refresh(user)
    return user


# ═══════════════════════════════════════════
# 角色
# ═══════════════════════════════════════════

async def role_insert(db: AsyncSession, role: Role) -> Role:
    db.add(role)
    await db.flush()
    await db.refresh(role)
    return role


async def role_list(db: AsyncSession) -> list[Role]:
    result = await db.execute(select(Role).order_by(Role.created_at.desc()))
    return list(result.scalars().all())


async def user_role_insert(db: AsyncSession, user_id: uuid.UUID, role_id: uuid.UUID) -> UserRole:
    ur = UserRole(user_id=user_id, role_id=role_id)
    db.add(ur)
    await db.flush()
    return ur


# ═══════════════════════════════════════════
# 权限
# ═══════════════════════════════════════════

async def permission_insert(db: AsyncSession, perm: Permission) -> Permission:
    db.add(perm)
    await db.flush()
    await db.refresh(perm)
    return perm


async def permission_list(db: AsyncSession) -> list[Permission]:
    result = await db.execute(select(Permission).order_by(Permission.resource))
    return list(result.scalars().all())


async def role_permission_insert(
    db: AsyncSession, role_id: uuid.UUID, permission_id: uuid.UUID
) -> RolePermission:
    rp = RolePermission(role_id=role_id, permission_id=permission_id)
    db.add(rp)
    await db.flush()
    return rp


# ═══════════════════════════════════════════
# 审计日志
# ═══════════════════════════════════════════

async def audit_log_insert(db: AsyncSession, log: AuditLog) -> AuditLog:
    db.add(log)
    await db.flush()
    return log


async def audit_log_list(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 50,
    user_id: Optional[uuid.UUID] = None,
    action: Optional[str] = None,
    resource: Optional[str] = None,
) -> tuple[list[AuditLog], int]:
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
