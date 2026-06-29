"""数据库引擎与会话管理 — SQLAlchemy async。"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, Uuid, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DB_ECHO,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """所有 ORM 模型的基类。"""
    pass


def _utcnow() -> datetime:
    """返回当前 UTC 时间 — 同时用于 Python 端 default 和 onupdate。"""
    return datetime.now(timezone.utc)


class TimestampMixin:
    """公共时间戳字段混入（兼容 PostgreSQL 和 SQLite）。"""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=_utcnow,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=_utcnow,
        onupdate=_utcnow,
        nullable=False,
    )


class UUIDPrimaryKeyMixin:
    """UUID 主键混入。"""

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )


async def get_db() -> AsyncSession:  # type: ignore[misc]
    """FastAPI 依赖注入：获取一个异步数据库会话。"""
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
