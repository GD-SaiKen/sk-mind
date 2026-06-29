"""数据库初始化 Seed 脚本 — 创建默认管理员、角色和权限。

用法：
    python -m app.seed
"""

import asyncio
import sys
from pathlib import Path

# 确保 backend 在 path 中
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_factory, Base, engine
from app.modules.auth.models import Permission, Role, RolePermission, User, UserRole
from app.core.security import hash_password

# 导入所有模型以确保建表
import app.modules.auth.models  # noqa: F401
import app.modules.data_sources.models  # noqa: F401
import app.modules.ingestion.models  # noqa: F401
import app.modules.datasets.models  # noqa: F401
import app.modules.quality.models  # noqa: F401
import app.modules.lineage.models  # noqa: F401


async def create_tables():
    """创建所有表（如果不存在）。"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表已就绪")


async def seed_admin_user(db: AsyncSession) -> User:
    """创建默认管理员用户。"""
    existing = await db.execute(select(User).where(User.username == "admin"))
    if existing.scalar_one_or_none():
        print("⏭️  管理员用户已存在，跳过")
        return existing.scalar_one()

    admin = User(
        username="admin",
        email="admin@skmind.local",
        hashed_password=hash_password("admin123"),
        display_name="系统管理员",
        is_superuser=True,
    )
    db.add(admin)
    await db.flush()
    await db.refresh(admin)
    print(f"✅ 管理员用户已创建: admin / admin123")
    return admin


async def seed_roles(db: AsyncSession) -> dict[str, Role]:
    """创建默认角色。"""
    roles_def = [
        {"name": "系统管理员", "code": "admin", "description": "拥有全部权限"},
        {"name": "数据管理员", "code": "data_admin", "description": "管理数据源、接入任务和数据目录"},
        {"name": "数据分析师", "code": "analyst", "description": "查询数据目录、质量和指标"},
        {"name": "普通用户", "code": "viewer", "description": "只读查看数据"},
    ]

    roles = {}
    for rd in roles_def:
        existing = await db.execute(select(Role).where(Role.code == rd["code"]))
        if existing.scalar_one_or_none():
            roles[rd["code"]] = existing.scalar_one()
            continue

        role = Role(**rd)
        db.add(role)
        await db.flush()
        await db.refresh(role)
        roles[rd["code"]] = role
        print(f"✅ 角色已创建: {role.name}")

    return roles


async def seed_permissions(db: AsyncSession) -> dict[str, Permission]:
    """创建默认权限点。"""
    perms_def = [
        # 数据源
        {"name": "查看数据源", "code": "data_source:read", "resource": "data_source", "action": "read"},
        {"name": "创建数据源", "code": "data_source:create", "resource": "data_source", "action": "create"},
        {"name": "编辑数据源", "code": "data_source:update", "resource": "data_source", "action": "update"},
        {"name": "删除数据源", "code": "data_source:delete", "resource": "data_source", "action": "delete"},
        # 接入任务
        {"name": "查看接入任务", "code": "ingestion:read", "resource": "ingestion", "action": "read"},
        {"name": "创建接入任务", "code": "ingestion:create", "resource": "ingestion", "action": "create"},
        {"name": "执行接入任务", "code": "ingestion:execute", "resource": "ingestion", "action": "execute"},
        # 数据目录
        {"name": "查看数据目录", "code": "catalog:read", "resource": "catalog", "action": "read"},
        # 数据质量
        {"name": "查看质量结果", "code": "quality:read", "resource": "quality", "action": "read"},
        {"name": "管理质量规则", "code": "quality:manage", "resource": "quality", "action": "manage"},
        # 用户管理
        {"name": "管理用户", "code": "user:manage", "resource": "user", "action": "manage"},
        {"name": "管理角色", "code": "role:manage", "resource": "role", "action": "manage"},
        # 审计
        {"name": "查看审计日志", "code": "audit:read", "resource": "audit", "action": "read"},
    ]

    perms = {}
    for pd in perms_def:
        existing = await db.execute(select(Permission).where(Permission.code == pd["code"]))
        if existing.scalar_one_or_none():
            perms[pd["code"]] = existing.scalar_one()
            continue

        perm = Permission(**pd)
        db.add(perm)
        await db.flush()
        await db.refresh(perm)
        perms[pd["code"]] = perm

    print(f"✅ {len(perms_def)} 个权限点已就绪")
    return perms


async def seed_role_permissions(
    db: AsyncSession,
    roles: dict[str, Role],
    perms: dict[str, Permission],
):
    """为角色分配默认权限。"""
    mapping = {
        "admin": list(perms.keys()),
        "data_admin": [
            "data_source:read", "data_source:create", "data_source:update", "data_source:delete",
            "ingestion:read", "ingestion:create", "ingestion:execute",
            "catalog:read", "quality:read", "quality:manage",
            "audit:read",
        ],
        "analyst": [
            "data_source:read", "ingestion:read",
            "catalog:read", "quality:read",
        ],
        "viewer": [
            "data_source:read", "catalog:read", "quality:read",
        ],
    }

    for role_code, perm_codes in mapping.items():
        role = roles[role_code]
        for pc in perm_codes:
            existing = await db.execute(
                select(RolePermission).where(
                    RolePermission.role_id == role.id,
                    RolePermission.permission_id == perms[pc].id,
                )
            )
            if existing.scalar_one_or_none():
                continue
            rp = RolePermission(role_id=role.id, permission_id=perms[pc].id)
            db.add(rp)

    print("✅ 角色权限已分配")


async def seed_admin_role(db: AsyncSession, admin_user: User, roles: dict[str, Role]):
    """为管理员用户分配 admin 角色。"""
    existing = await db.execute(
        select(UserRole).where(
            UserRole.user_id == admin_user.id,
            UserRole.role_id == roles["admin"].id,
        )
    )
    if existing.scalar_one_or_none():
        print("⏭️  管理员角色已分配，跳过")
        return

    ur = UserRole(user_id=admin_user.id, role_id=roles["admin"].id)
    db.add(ur)
    print("✅ 管理员角色已分配")


async def main():
    """执行 seed。"""
    print("🌱 开始数据库初始化...\n")

    await create_tables()

    async with async_session_factory() as db:
        try:
            admin = await seed_admin_user(db)
            roles = await seed_roles(db)
            perms = await seed_permissions(db)
            await seed_role_permissions(db, roles, perms)
            await seed_admin_role(db, admin, roles)
            await db.commit()
            print("\n🎉 数据库初始化完成！")
            print("   默认管理员: admin / admin123")
        except Exception:
            await db.rollback()
            raise


if __name__ == "__main__":
    asyncio.run(main())
