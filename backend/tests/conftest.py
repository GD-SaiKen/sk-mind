"""pytest 配置文件 — 提供异步数据库会话和 HTTP 测试客户端 fixtures。"""

import asyncio
import sqlite3
import uuid as _uuid
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import event, StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# 将 backend 加入 Python path
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))  # tests/ for direct conftest imports

from app.core.database import Base, get_db

# ── 导入所有模型（必须在 app.main 之前以确保 metadata 完整）──
import app.modules.auth.models  # noqa: F401
import app.modules.data_sources.models  # noqa: F401
import app.modules.ingestion.models  # noqa: F401
import app.modules.datasets.models  # noqa: F401
import app.modules.quality.models  # noqa: F401
import app.modules.lineage.models  # noqa: F401
import app.modules.semantic.models  # noqa: F401
import app.modules.graph.models  # noqa: F401

# ── FastAPI app（在模型之后导入避免循环引用）────
import app.main  # noqa: F401
fastapi_app = app.main.app

# ── 测试用 SQLite 内存数据库 ────────────────
TEST_DATABASE_URL = "sqlite+aiosqlite://"

# 注册 UUID → hex 适配器（无连字符），SQLAlchemy Uuid(as_uuid=True) 在 SQLite 中存为 CHAR(32)
sqlite3.register_adapter(_uuid.UUID, lambda u: u.hex)


@pytest.fixture(scope="session")
def event_loop():
    """创建 session 级别的事件循环。"""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """每个测试独立的数据库会话，自动建表 + 回滚。"""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        echo=False,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    # 建表
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with session_factory() as session:
        yield session
        await session.rollback()

    # 清理
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """FastAPI TestClient — 异步 HTTP 客户端。"""

    async def override_get_db():
        yield db_session

    fastapi_app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    fastapi_app.dependency_overrides.clear()


# ── T11: 认证 fixture ──────────────────────────────────────

@pytest_asyncio.fixture(scope="function")
async def auth_headers(client: AsyncClient) -> dict[str, str]:
    """注册测试用户 → 登录 → 返回 Authorization 头。"""
    await client.post("/api/auth/register", json={
        "username": "t11_tester",
        "email": "t11@test.internal",
        "password": "testpass123",
        "display_name": "T11 Tester",
    })
    resp = await client.post("/api/auth/login", json={
        "username": "t11_tester",
        "password": "testpass123",
    })
    assert resp.status_code == 200, resp.text
    token = resp.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


# ── T11: 测试数据源工厂 ──────────────────────────────────────

async def create_test_datasource(client, auth_headers, suffix=""):
    """创建一个测试用数据源，返回其 id。"""
    resp = await client.post(
        "/api/data-sources",
        json={
            "name": f"T11-MES{suffix}",
            "code": f"t11_mes_{suffix.replace('-', '_')}" if suffix else "t11_mes",
            "description": "T11 单元测试-制造执行系统",
            "source_type": "mes",
            "access_method": "api_pull",
            "sensitivity_level": "internal",
        },
        headers=auth_headers,
    )
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]["id"]


# ── T11: 测试数据集工厂 ──────────────────────────────────────

async def create_test_dataset(client, auth_headers, source_id, **overrides):
    """创建一个测试用 Dataset 记录，返回完整响应 data。"""
    payload = {
        "name": "测试工单表",
        "code": "raw.mes_t11_workorder",
        "description": "T11 测试用工单数据",
        "data_layer": "raw",
        "data_source_id": str(source_id),
        "status": "active",
        "business_domain": "工单域",
    }
    payload.update(overrides)
    resp = await client.post(
        "/api/datasets",
        json=payload,
        headers=auth_headers,
    )
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]


async def create_test_field(
    db_session: AsyncSession, dataset_id: str, **overrides,
):
    """在数据库中直接插入一条 DatasetField 记录，返回 ORM 对象。"""
    import uuid as _uuid
    from app.modules.datasets.models import Dataset, DatasetField
    ds = await db_session.get(Dataset, _uuid.UUID(dataset_id))
    if not ds:
        raise RuntimeError(f"Dataset {dataset_id} not found")
    defaults = dict(
        field_name="woid",
        data_type="varchar",
        is_nullable=False,
        ordinal_position=1,
        is_primary_key=True,
        source_column="woid",
        sensitivity_level="internal",
    )
    defaults.update(overrides)
    field = DatasetField(dataset_id=ds.id, **defaults)
    db_session.add(field)
    await db_session.flush()
    await db_session.refresh(field)
    return field
