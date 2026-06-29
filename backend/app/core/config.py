"""应用配置 — 通过 pydantic-settings 从环境变量 / .env 加载。"""

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """全平台配置，所有值均可通过环境变量覆盖（前缀 SKMIND_）。"""

    model_config = SettingsConfigDict(
        env_prefix="SKMIND_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ── 应用 ──────────────────────────────────
    APP_NAME: str = "sk-mind"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    # ── 数据库 ────────────────────────────────
    DATABASE_URL: str = "postgresql+asyncpg://skmind:skmind@localhost:5432/skmind"
    DATABASE_URL_SYNC: str = "postgresql+psycopg2://skmind:skmind@localhost:5432/skmind"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 5
    DB_ECHO: bool = False

    # ── Redis ─────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── JWT / Auth ────────────────────────────
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480

    # ── 文件 ──────────────────────────────────
    DATA_DIR: Path = Path("/data")          # 生产环境挂载目录
    UPLOAD_DIR: Path = Path("/data/uploads")
    MAX_UPLOAD_SIZE_MB: int = 100

    # ── LLM ───────────────────────────────────
    LLM_PROVIDER: Literal["local", "openai", "disabled"] = "disabled"
    LLM_API_KEY: str = ""
    LLM_BASE_URL: str = ""

    # ── 安全 ──────────────────────────────────
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]


settings = Settings()
