"""API 路由聚合 — 汇总所有业务模块路由。"""

from fastapi import APIRouter

from app.api.auth import router as auth_router

router = APIRouter()

# ── 注册业务路由 ─────────────────────────────
router.include_router(auth_router)

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
        ],
    }
