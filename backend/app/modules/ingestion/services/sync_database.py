"""同步数据库会话（sync — RQ Worker 使用）。

RQ Worker 运行在独立进程中，使用同步 SQLAlchemy 引擎。
与 async API 层隔离，避免事件循环冲突。
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# RQ Worker 专用同步引擎
sync_engine = create_engine(
    settings.DATABASE_URL_SYNC,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
)

SyncSessionLocal = sessionmaker(
    bind=sync_engine,
    autocommit=False,
    autoflush=False,
)


def get_sync_db() -> Session:
    """创建同步数据库会话。"""
    return SyncSessionLocal()
