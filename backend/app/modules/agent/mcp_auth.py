"""MCP API Key 认证依赖。"""

import logging

from fastapi import Header, HTTPException, status

from app.core.config import settings

logger = logging.getLogger("sk-mind")


async def verify_mcp_api_key(authorization: str = Header(default="")) -> None:
    """API Key 认证：读取 Authorization 头，与 settings.MCP_API_KEY 对比。

    当 MCP_API_KEY 为空时（默认），允许所有请求（dev 模式），输出 warning。
    """
    api_key = settings.MCP_API_KEY

    if not api_key:
        logger.warning("MCP_API_KEY is not set — allowing all MCP requests (dev mode)")
        return

    token = authorization.removeprefix("Bearer ").strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API key",
        )

    if token != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
