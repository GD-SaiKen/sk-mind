"""BridgeAdapter: communication interface with the intermediate bridge server.

SQL Server ERP is deployed on a production server that cannot be directly connected.
Data is retrieved through a bridge script running on an intermediate server.
The bridge script's concrete implementation (HTTP / file exchange / message queue)
is TBD. This module defines the abstraction and a placeholder that returns empty data.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class BridgeError(Exception):
    """Bridge communication exception."""
    pass


@dataclass
class BridgeCommand:
    """Instruction sent from the platform to the bridge script."""

    source_sql: str
    sync_mode: str
    batch_size: int = 1000
    offset: int = 0
    timestamp_column: Optional[str] = None
    cursor_column: Optional[str] = None
    last_sync_marker: Optional[dict] = None
    database: Optional[str] = None
    schema: Optional[str] = None

    @property
    def augmented_sql(self) -> str:
        """Append WHERE / ORDER BY based on sync_mode to the source_sql."""
        sql = self.source_sql.strip().rstrip(";")
        if self.sync_mode == "timestamp" and self.timestamp_column:
            marker = (self.last_sync_marker or {}).get("last_timestamp")
            if marker:
                keyword = "AND" if "WHERE" in sql.upper() else "WHERE"
                sql += f" {keyword} {self.timestamp_column} > '{marker}'"
        elif self.sync_mode == "cursor" and self.cursor_column:
            marker = (self.last_sync_marker or {}).get("last_cursor_id")
            if marker is not None:
                keyword = "AND" if "WHERE" in sql.upper() else "WHERE"
                sql += f" {keyword} {self.cursor_column} > {marker}"
                if "ORDER BY" not in sql.upper():
                    sql += f" ORDER BY {self.cursor_column}"
        return sql


class BridgeAdapter(ABC):
    """Abstraction for communicating with the intermediate bridge server.

    Concrete implementations (HTTP, file, MQ) are built once the bridge
    script's actual protocol is confirmed.
    """

    @abstractmethod
    def execute(self, command: BridgeCommand) -> list[dict]:
        """Send a command to the bridge and return result rows."""
        ...

    @abstractmethod
    def health_check(self) -> bool:
        """Check whether the bridge is reachable."""
        ...

    @abstractmethod
    def fetch_columns(self, table_name: str, schema: str = "dbo") -> list[dict]:
        """Fetch column definitions from the bridge.

        Each column dict: {"name": str, "data_type": str, "is_nullable": bool, ...}
        """
        ...


class PlaceholderBridgeAdapter(BridgeAdapter):
    """Default bridge adapter used before the real bridge script is ready.

    Always returns empty data. health_check returns False.
    """

    def __init__(self, bridge_url: str = ""):
        self._bridge_url = bridge_url

    def execute(self, command: BridgeCommand) -> list[dict]:
        logger.warning(
            "PlaceholderBridgeAdapter: no real bridge configured (url=%s)", self._bridge_url
        )
        return []

    def health_check(self) -> bool:
        return False

    def fetch_columns(self, table_name: str, schema: str = "dbo") -> list[dict]:
        logger.warning("PlaceholderBridgeAdapter: cannot fetch columns (no bridge)")
        return []
