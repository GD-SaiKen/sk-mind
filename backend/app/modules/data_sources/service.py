"""DataSource module service layer."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.data_sources.dao import get_by_id


async def check_connection(
    source_id: uuid.UUID,
    db: AsyncSession,
) -> dict:
    """Check DataSource connectivity and persist the result.

    For database sources: placeholder (bridge not yet ready).
    For API sources: issues a HEAD request to the health endpoint.

    Returns {"source_id": str, "connection_status": str}.
    """
    source = await get_by_id(db, source_id)
    if not source:
        raise ValueError(f"DataSource not found: {source_id}")

    is_healthy = False
    try:
        if (source.source_category or source.source_type) == "database":
            # Placeholder: SQL Server bridge not yet configured
            # Will be replaced with BridgeAdapter.health_check() once bridge is ready
            is_healthy = False
        elif (source.source_category or "") == "api":
            import httpx
            config = source  # connector_config is on a separate table; skip for now
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.head("http://placeholder/health")
                is_healthy = resp.status_code < 500
    except Exception:
        is_healthy = False

    source.connection_status = "healthy" if is_healthy else "unhealthy"
    source.last_health_check_at = datetime.now(timezone.utc)
    await db.commit()

    return {
        "source_id": str(source_id),
        "connection_status": source.connection_status,
    }
