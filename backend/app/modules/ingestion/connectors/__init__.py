"""Connector 包 — 连接器实现与工厂函数。"""

from app.modules.ingestion.connectors.base import (
    ApiConnector,
    ApiPageResult,
    ColumnInfo,
    DatabaseConnector,
)
from app.modules.ingestion.connectors.api_client import HttpxApiConnector
from app.modules.ingestion.connectors.rate_limiter import TokenBucket
from app.modules.ingestion.connectors.sqlserver import SqlServerConnector
from app.modules.ingestion.connectors.token_manager import TokenManager

__all__ = [
    "ApiConnector",
    "ApiPageResult",
    "ColumnInfo",
    "DatabaseConnector",
    "HttpxApiConnector",
    "SqlServerConnector",
    "TokenBucket",
    "TokenManager",
]
