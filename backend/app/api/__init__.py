"""API 路由聚合 — 汇总所有业务模块路由（三层架构：router → service → dao）。"""

from fastapi import APIRouter

from app.modules.auth.router import router as auth_router
from app.modules.ingestion.router import task_router, browse_router
from app.modules.ingestion.api.sse import sse_router
from app.modules.ingestion.api.control import control_router
from app.modules.data_sources.router import router as data_sources_router
from app.modules.datasets.router import router as datasets_router
from app.modules.catalog.router import router as catalog_router
from app.modules.lineage.router import router as lineage_router
from app.modules.quality.router import router as quality_router
from app.modules.semantic.router import router as semantic_router
from app.modules.agent.router import router as agent_router
from app.modules.graph.router import router as graph_router

router = APIRouter()

# ── 注册业务路由 ─────────────────────────────
router.include_router(auth_router)
router.include_router(task_router)
router.include_router(sse_router, prefix="/ingestion-tasks")
router.include_router(control_router, prefix="/ingestion-tasks")
router.include_router(browse_router)
router.include_router(data_sources_router)
router.include_router(datasets_router)
router.include_router(catalog_router)
router.include_router(lineage_router)
router.include_router(quality_router)
router.include_router(semantic_router)
router.include_router(agent_router)
router.include_router(graph_router)

# 当前阶段提供一个简单的状态接口验证前后端联通
@router.get("/status", tags=["system"])
async def api_status() -> dict:
    """API 聚合状态检查。"""
    return {
        "status": "ok",
        "modules": [
            "auth",
            "data_sources",
            "ingestion",
            "catalog",
            "quality",
            "datasets",
            "lineage",
            "semantic",
        ],
    }
