"""Auth API 集成测试 — 登录、注册、Token 校验。"""

import pytest
from httpx import AsyncClient


class TestAuthAPI:
    """认证 API 集成测试。"""

    async def test_health_check(self, client: AsyncClient):
        """健康检查接口应返回 200。"""
        resp = await client.get("/api/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"

    async def test_api_status(self, client: AsyncClient):
        """API 状态接口应列出所有模块。"""
        resp = await client.get("/api/status")
        assert resp.status_code == 200
        data = resp.json()
        assert "auth" in data["modules"]

    async def test_register_user(self, client: AsyncClient):
        """注册新用户。"""
        resp = await client.post("/api/auth/register", json={
            "username": "newuser",
            "email": "new@example.com",
            "password": "secret123",
            "display_name": "New User",
        })
        assert resp.status_code == 201
        data = resp.json()
        assert data["username"] == "newuser"
        assert "hashed_password" not in data

    async def test_register_duplicate_username(self, client: AsyncClient):
        """重复用户名应返回 409。"""
        # 先注册一个用户
        await client.post("/api/auth/register", json={
            "username": "dupuser",
            "email": "dup1@example.com",
            "password": "secret123",
            "display_name": "Dup User",
        })
        # 再注册同名用户
        resp = await client.post("/api/auth/register", json={
            "username": "dupuser",
            "email": "dup2@example.com",
            "password": "secret123",
            "display_name": "Dup User 2",
        })
        assert resp.status_code == 409

    async def test_login_success(self, client: AsyncClient):
        """登录成功应返回 Token 和用户信息。"""
        # 注册
        await client.post("/api/auth/register", json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "mypassword",
            "display_name": "Login User",
        })
        # 登录
        resp = await client.post("/api/auth/login", json={
            "username": "loginuser",
            "password": "mypassword",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["username"] == "loginuser"

    async def test_login_wrong_password(self, client: AsyncClient):
        """错误密码应返回 401。"""
        # 注册
        await client.post("/api/auth/register", json={
            "username": "wrongpw",
            "email": "wrongpw@example.com",
            "password": "correct",
            "display_name": "Wrong PW User",
        })
        # 错误密码登录
        resp = await client.post("/api/auth/login", json={
            "username": "wrongpw",
            "password": "wrong",
        })
        assert resp.status_code == 401

    async def test_get_me_requires_auth(self, client: AsyncClient):
        """未登录访问 /me 应返回 401。"""
        resp = await client.get("/api/auth/me")
        assert resp.status_code == 401

    async def test_get_me_with_token(self, client: AsyncClient):
        """带 Token 访问 /me 应返回用户信息。"""
        # 注册
        await client.post("/api/auth/register", json={
            "username": "meuser",
            "email": "me@example.com",
            "password": "secret123",
            "display_name": "Me User",
        })
        # 登录
        login_resp = await client.post("/api/auth/login", json={
            "username": "meuser",
            "password": "secret123",
        })
        token = login_resp.json()["access_token"]

        # 访问 me
        resp = await client.get("/api/auth/me", headers={
            "Authorization": f"Bearer {token}",
        })
        assert resp.status_code == 200
        assert resp.json()["username"] == "meuser"
