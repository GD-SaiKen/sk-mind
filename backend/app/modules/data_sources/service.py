"""DataSource module service layer."""

import json
import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.data_sources.dao import get_by_id, get_connection_config


def _build_auth_headers(conn: dict) -> dict:
    """从 connection 配置构建鉴权 Header（与 HttpxApiConnector.connect() 对齐）。"""
    headers: dict = {}
    auth_type = conn.get("auth_type", "none")
    cred = conn.get("auth_credentials")
    cred_2 = conn.get("auth_credentials_2")
    header_name = conn.get("auth_header_name", "Authorization")
    header_name_2 = conn.get("auth_header_name_2", "")

    if auth_type == "bearer" and cred:
        headers[header_name] = f"Bearer {cred}"
    elif auth_type == "basic" and cred:
        headers[header_name] = f"Basic {cred}"
    elif auth_type == "api_key" and cred:
        headers[header_name] = cred
    elif auth_type == "dual_key" and cred and cred_2:
        headers[header_name] = cred
        headers[header_name_2] = cred_2

    return headers


async def check_connection(
    source_id: uuid.UUID,
    db: AsyncSession,
) -> dict:
    """Check DataSource connectivity and persist the result.

    For database sources: placeholder (bridge not yet ready).
    For API sources: uses DB ConnectorConfig to issue a HEAD request
    to the configured base_url.

    Returns {"source_id": str, "connection_status": str}.
    """
    source = await get_by_id(db, source_id)
    if not source:
        raise ValueError(f"DataSource not found: {source_id}")

    is_healthy = False
    detail = ""
    try:
        if (source.source_category or source.source_type) == "database":
            # Placeholder: SQL Server bridge not yet configured
            is_healthy = False
            detail = "数据库连接检测尚未实现"
        elif (source.source_category or "") == "api":
            # 从 DB ConnectorConfig 读取连接配置
            cfg = await get_connection_config(db, source_id)
            if not cfg or not cfg.extra_config:
                is_healthy = False
                detail = "未找到连接配置（请在编辑页配置 API 连接信息）"
            else:
                conn = json.loads(cfg.extra_config)
                base_url = conn.get("base_url")
                if not base_url:
                    is_healthy = False
                    detail = "连接配置缺少 base_url"
                else:
                    import httpx
                    headers = _build_auth_headers(conn)
                    ssl_verify = conn.get("ssl_verify", True)
                    timeout = conn.get("timeout", 10)
                    async with httpx.AsyncClient(
                        timeout=timeout, verify=ssl_verify, follow_redirects=True,
                    ) as client:
                        resp = await client.head(base_url, headers=headers)
                        # 2xx / 3xx / 4xx 都算"能连上"（鉴权错误也算连通）
                        is_healthy = resp.status_code < 500
                        detail = f"HTTP {resp.status_code}"
    except Exception as e:
        is_healthy = False
        detail = str(e)

    source.connection_status = "healthy" if is_healthy else "unhealthy"
    source.last_health_check_at = datetime.now(timezone.utc)
    await db.commit()

    return {
        "sourceId": str(source_id),
        "connectionStatus": source.connection_status,
        "detail": detail,
    }
