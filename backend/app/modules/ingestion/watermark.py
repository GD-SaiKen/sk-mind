"""Watermark read/write for incremental sync."""

import uuid
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session


class WatermarkStore:
    """Persists per-interface sync watermarks in the sync_watermarks table."""

    def __init__(self, db: Session):
        self._db = db

    def get(self, data_source_id: uuid.UUID, interface_name: str) -> datetime | None:
        """Return last_synced_at or None if never synced."""
        row = self._db.execute(
            text(
                "SELECT last_synced_at FROM sync_watermarks "
                "WHERE data_source_id = :ds_id AND interface_name = :name"
            ),
            {"ds_id": data_source_id, "name": interface_name},
        ).fetchone()
        return row.last_synced_at if row else None

    def set(
        self,
        data_source_id: uuid.UUID,
        interface_name: str,
        synced_at: datetime,
    ) -> None:
        """Upsert watermark."""
        self._db.execute(
            text(
                "INSERT INTO sync_watermarks (data_source_id, interface_name, last_synced_at) "
                "VALUES (:ds_id, :name, :ts) "
                "ON CONFLICT (data_source_id, interface_name) "
                "DO UPDATE SET last_synced_at = EXCLUDED.last_synced_at, "
                "              updated_at = now()"
            ),
            {"ds_id": data_source_id, "name": interface_name, "ts": synced_at},
        )
        self._db.commit()
