"""Ingestion API 包。"""

from app.modules.ingestion.api.ingestion_tasks import router as ingestion_tasks_router

__all__ = ["ingestion_tasks_router"]
