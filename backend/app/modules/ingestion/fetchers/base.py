"""Fetcher abstraction: connect to source -> pull data -> yield uniform row iterator."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Iterable, Optional


@dataclass
class SyncConfig:
    """Unified sync configuration consumed by all Fetcher implementations."""

    source_type: str
    # "database" | "api"
    sync_mode: str
    # "full" | "timestamp" | "cursor"

    # DB-specific
    source_sql: Optional[str] = None
    table_name: Optional[str] = None
    timestamp_column: Optional[str] = None
    cursor_column: Optional[str] = None
    schema: Optional[str] = None

    # Batch control
    batch_size: int = 1000
    last_sync_marker: Optional[dict] = None

    # SQL Server bridge
    bridge_url: Optional[str] = None

    # MongoDB (future)
    database_name: Optional[str] = None
    collection_name: Optional[str] = None

    # API (future)
    method: Optional[str] = None
    endpoint: Optional[str] = None
    params_template: Optional[dict] = None


@dataclass
class FetcherMeta:
    """Metadata returned by every Fetcher after pulling."""

    total_rows: Optional[int]
    columns: list[str]
    source_signature: str
    pulled_at: datetime


class BaseFetcher(ABC):
    """Connect to source -> pull data -> yield uniform row iterator.

    Every Fetcher (DB, API, file) implements this interface.
    The Fetcher's sole responsibility is data retrieval.
    It does NOT write to databases, transform types, or perform business validation.
    """

    @abstractmethod
    def fetch(self, config: SyncConfig) -> tuple[Iterable[dict], FetcherMeta]:
        """Pull data from source and return a row iterator plus metadata.

        Returns:
            Tuple of (row_iterator, metadata).
        """
        ...

    @abstractmethod
    def test_connection(self, config: SyncConfig) -> bool:
        """Test whether the source is reachable with the given config."""
        ...
