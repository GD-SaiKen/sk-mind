"""Alembic 迁移环境配置 — 从 app.core.config 读取数据库 URL。"""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core.config import settings

# Alembic Config 对象，提供 .ini 中的值
config = context.config

# 设置日志
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 从应用配置覆盖数据库 URL（支持环境变量）
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL_SYNC)

# ── 导入所有模型的 Base metadata ──────────────────
from app.core.database import Base

# 导入所有模型模块，使 Base.metadata 包含所有表
import app.modules.auth.models  # noqa: F401
import app.modules.data_sources.models  # noqa: F401
import app.modules.ingestion.models  # noqa: F401
import app.modules.datasets.models  # noqa: F401
import app.modules.quality.models  # noqa: F401
import app.modules.lineage.models  # noqa: F401

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """以 'offline' 模式运行迁移（生成 SQL 脚本）。"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """以 'online' 模式运行迁移（直接连接数据库）。"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
