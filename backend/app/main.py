"""FastAPI 应用入口 — 创建 app、注册路由、配置中间件。"""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """应用生命周期：启动时初始化日志和调度器，关闭时清理连接。"""
    setup_logging(settings.LOG_LEVEL)

    # uvicorn 自己的日志不要被 root handler 接管，保持原生彩色
    for name in ("uvicorn", "uvicorn.access", "uvicorn.error"):
        logging.getLogger(name).propagate = False
    from app.core.database import engine
    from app.modules.ingestion.scheduler import start_scheduler, shutdown_scheduler

    try:
        start_scheduler()
    except Exception:
        logging.getLogger("sk-mind").warning("调度器启动失败（可能是 Redis 未就绪），定时任务不可用")

    try:
        from app.core.database import async_session_factory
        from app.modules.semantic.loader import get_loader
        async with async_session_factory() as db:
            loader = get_loader("mes")
            await loader.load_all_async(db)
    except Exception:
        logging.getLogger("sk-mind").warning("YAML 语义模型启动同步失败")

    yield
    shutdown_scheduler()
    await engine.dispose()


# ── 注册所有 ORM 模型（确保 FK 关系可解析）───
import app.modules.auth.models          # noqa: F401
import app.modules.data_sources.models  # noqa: F401
import app.modules.datasets.models      # noqa: F401
import app.modules.ingestion.models     # noqa: F401
import app.modules.lineage.models       # noqa: F401
import app.modules.quality.models       # noqa: F401
import app.modules.semantic.models    # noqa: F401

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# ── CORS ──────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── 全局异常处理 ──────────────────────────────
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """兜底异常处理，避免内部错误直接泄露给前端。"""
    logger = logging.getLogger("sk-mind")
    logger.exception("Unhandled exception on %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


# ── Health check ──────────────────────────────
@app.get("/api/health", tags=["system"])
async def health_check() -> dict:
    """健康检查接口。"""
    return {"status": "ok", "version": settings.APP_VERSION}


# ── 注册业务路由 ─────────────────────────────
from app.api import router as api_router
app.include_router(api_router, prefix="/api")
