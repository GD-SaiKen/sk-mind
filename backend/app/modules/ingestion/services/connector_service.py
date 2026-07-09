"""Connector 工厂服务 — 根据数据源配置创建对应的连接器实例。

对应策略文档：04-同步引擎技术实现 §3。
"""

import json
import uuid

from app.modules.ingestion.connectors.api_client import HttpxApiConnector
from app.modules.ingestion.connectors.sqlserver import SqlServerConnector


class ConnectorService:
    """根据 ConnectorConfig 和数据源类型创建连接器。

    当前支持的连接器类型：sqlserver / api。
    """

    @staticmethod
    def create_sqlserver(config: dict) -> SqlServerConnector:
        """从配置字典创建 SqlServerConnector。"""
        return SqlServerConnector(
            host=config["host"],
            port=config.get("port", 1433),
            database=config["database"],
            username=config["username"],
            password=config["password"],
            driver=config.get("driver", "ODBC Driver 17 for SQL Server"),
            schema=config.get("schema", "dbo"),
            connect_timeout=config.get("connect_timeout", 30),
            query_timeout=config.get("query_timeout", 300),
        )

    @staticmethod
    def create_api(config: dict) -> HttpxApiConnector:
        """从配置字典创建 HttpxApiConnector。"""
        return HttpxApiConnector(
            base_url=config["base_url"],
            auth_type=config.get("auth_type", "bearer"),
            auth_credentials=config.get("auth_credentials"),
            auth_header_name=config.get("auth_header_name", "Authorization"),
            auth_token_prefix=config.get("auth_token_prefix", "Bearer"),
            auth_url=config.get("auth_url"),
            auth_credentials_map=config.get("auth_credentials_map"),
            auth_credentials_2=config.get("auth_credentials_2"),
            auth_header_name_2=config.get("auth_header_name_2", ""),
            qps_limit=config.get("qps_limit", 10),
            timeout=config.get("timeout", 30),
            max_retries=config.get("max_retries", 3),
            retry_backoff=config.get("retry_backoff", 1.5),
            records_path=config.get("records_path", "data.list"),
            total_path=config.get("total_path", "data.total"),
            default_headers=config.get("default_headers"),
        )

    @staticmethod
    def create_from_db_models(
        connector_config,  # ConnectorConfig ORM instance
    ) -> SqlServerConnector | HttpxApiConnector:
        """从 ORM 模型创建连接器。

        Args:
            connector_config: ConnectorConfig ORM 实例。

        Returns:
            对应的连接器实例。

        Raises:
            ValueError: 不支持的 config_type。
        """
        extra = {}
        if connector_config.extra_config:
            extra = json.loads(connector_config.extra_config)

        config = {
            "host": connector_config.host,
            "port": connector_config.port,
            "database": connector_config.database_name,
            "username": connector_config.username,
            "password": connector_config.credential_ref or "",
            **extra,
        }

        if connector_config.config_type == "db_connection":
            return ConnectorService.create_sqlserver(config)
        elif connector_config.config_type == "api_config":
            return ConnectorService.create_api(config)
        else:
            raise ValueError(
                f"不支持的连接器类型: {connector_config.config_type}"
            )
