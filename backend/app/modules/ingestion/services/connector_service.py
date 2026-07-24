"""Connector 工厂服务 — 根据数据源配置创建对应的连接器实例。

对应策略文档：04-同步引擎技术实现 §3。
"""

import json
import logging
import uuid

from sqlalchemy import text

from app.modules.ingestion.connectors.api_client import HttpxApiConnector
from app.modules.ingestion.connectors.sqlserver import SqlServerConnector

logger = logging.getLogger(__name__)


# ── DB 配置 → 引擎配置 ──────────────────────────────────────


def build_engine_config(db, data_source_id: uuid.UUID) -> dict | None:
    """从 DB ConnectorConfig 构建 ApiSyncEngine 期望的配置字典。

    读取 ``ConnectorConfig.extra_config`` JSON（snake_case 键，与 YAML 的
    ``connection`` 段同构），返回::

        {
            "connection": { base_url, auth_type, ... },
            "interfaces": [],   # 空列表，由调用方从 YAML 合并
        }

    Args:
        db: 同步 SQLAlchemy Session（RQ worker 使用 ``get_sync_db()``）。
        data_source_id: 数据源 UUID。

    Returns:
        配置字典；若该数据源在 DB 中无 ConnectorConfig 记录则返回 None。
    """
    row = db.execute(
        text(
            "SELECT extra_config FROM connector_configs "
            "WHERE data_source_id = :ds_id LIMIT 1"
        ),
        {"ds_id": str(data_source_id)},
    ).fetchone()

    if not row or not row[0]:
        return None

    extra = json.loads(row[0])

    config: dict = {
        "connection": extra,
        "interfaces": [],
    }

    logger.info(
        "Built engine config from DB for source %s: base_url=%s, auth_type=%s",
        data_source_id,
        extra.get("base_url", "N/A"),
        extra.get("auth_type", "N/A"),
    )
    return config


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
