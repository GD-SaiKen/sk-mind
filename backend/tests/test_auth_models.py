"""auth 模块模型测试 — 验证用户、角色、权限的 CRUD 和关联。"""

import uuid

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.models import (
    AuditLog,
    Department,
    Permission,
    Role,
    RolePermission,
    User,
    UserRole,
)
from app.core.security import hash_password, verify_password


class TestUserModel:
    """User 模型测试。"""

    async def test_create_user(self, db_session: AsyncSession):
        """创建用户并验证字段。"""
        user = User(
            username="testuser",
            email="test@example.com",
            hashed_password=hash_password("secret123"),
            display_name="Test User",
        )
        db_session.add(user)
        await db_session.flush()

        assert user.id is not None
        assert user.username == "testuser"
        assert user.is_active is True
        assert user.is_superuser is False
        assert user.created_at is not None

    async def test_unique_username(self, db_session: AsyncSession):
        """用户名唯一约束。"""
        u1 = User(
            username="sameuser",
            email="a@example.com",
            hashed_password="hash",
            display_name="A",
        )
        u2 = User(
            username="sameuser",
            email="b@example.com",
            hashed_password="hash",
            display_name="B",
        )
        db_session.add_all([u1, u2])
        with pytest.raises(Exception):
            await db_session.flush()

    async def test_password_hashing(self, db_session: AsyncSession):
        """密码哈希与验证。"""
        plain = "my-password-123"
        hashed = hash_password(plain)
        assert verify_password(plain, hashed) is True
        assert verify_password("wrong", hashed) is False

    async def test_user_role_association(self, db_session: AsyncSession):
        """用户-角色关联。"""
        user = User(
            username="roleuser",
            email="role@example.com",
            hashed_password="hash",
            display_name="Role User",
        )
        role = Role(name="数据分析师", code="data_analyst")
        db_session.add_all([user, role])
        await db_session.flush()

        ur = UserRole(user_id=user.id, role_id=role.id)
        db_session.add(ur)
        await db_session.flush()

        # 重新加载验证
        await db_session.refresh(user, ["roles"])
        assert len(user.roles) == 1
        assert user.roles[0].role_id == role.id

    async def test_department_tree(self, db_session: AsyncSession):
        """部门自引用层级。"""
        root = Department(name="总公司", code="HQ")
        child = Department(name="技术部", code="TECH", parent_id=None)
        db_session.add_all([root, child])
        await db_session.flush()

        child.parent_id = root.id
        await db_session.flush()
        await db_session.refresh(child, ["parent"])

        assert child.parent is not None
        assert child.parent.name == "总公司"


class TestRolePermission:
    """角色-权限测试。"""

    async def test_role_with_permissions(self, db_session: AsyncSession):
        """角色关联权限。"""
        role = Role(name="管理员", code="admin")
        perm = Permission(
            name="查看数据源",
            code="data_source:read",
            resource="data_source",
            action="read",
        )
        db_session.add_all([role, perm])
        await db_session.flush()

        rp = RolePermission(role_id=role.id, permission_id=perm.id)
        db_session.add(rp)
        await db_session.flush()

        # 查询验证
        await db_session.refresh(role, ["permissions"])
        assert len(role.permissions) == 1
        assert role.permissions[0].code == "data_source:read"


class TestAuditLog:
    """审计日志测试。"""

    async def test_create_audit_log(self, db_session: AsyncSession):
        """写入审计日志。"""
        log = AuditLog(
            username="admin",
            action="login",
            resource="auth",
            detail="User admin logged in",
            ip_address="127.0.0.1",
        )
        db_session.add(log)
        await db_session.flush()

        assert log.id is not None
        assert log.action == "login"
        assert log.created_at is not None
