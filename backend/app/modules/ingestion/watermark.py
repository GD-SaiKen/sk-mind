"""WatermarkStore: per-interface last-sync watermark tracking.

Reads/writes the ``sync_watermarks`` table to determine whether an interface
has been synced before (full pull) or should use incremental pull.

Table schema:
    id              uuid PK
    data_source_id  uuid NOT NULL
    interface_name  varchar NOT NULL
    last_synced_at  timestamptz NOT NULL
    updated_at      timestamptz DEFAULT now()
    last_synced_value text (optional, for cursor-based syncs)

Unique constraint: (data_source_id, interface_name)
"""

import logging
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class WatermarkStore:
    """Track last-sync timestamps per (data_source_id, interface_name)."""

    def __init__(self, db: Session):
        self._db = db

    def get(self, data_source_id: uuid.UUID, interface_name: str) -> Optional[datetime]:
        """Return the last_synced_at for this interface, or None if never synced."""
        result = self._db.execute(
            text(
                "SELECT last_synced_at FROM sync_watermarks "
                "WHERE data_source_id = :ds AND interface_name = :iface"
            ),
            {"ds": str(data_source_id), "iface": interface_name},
        )
        row = result.fetchone()
        return row[0] if row else None

    def exists(self, data_source_id: uuid.UUID, interface_name: str) -> bool:
        """Check if a watermark record exists for this interface."""
        return self.get(data_source_id, interface_name) is not None

    def save(
        self,
        data_source_id: uuid.UUID,
        interface_name: str,
        synced_at: Optional[datetime] = None,
    ) -> None:
        """Upsert the watermark for this interface.

        Uses INSERT ... ON CONFLICT DO UPDATE so it works for both
        first-time and subsequent syncs.
        """
        synced_at = synced_at or datetime.now(timezone.utc)
        self._db.execute(
            text(
                "INSERT INTO sync_watermarks (data_source_id, interface_name, last_synced_at, updated_at) "
                "VALUES (:ds, :iface, :ts, now()) "
                "ON CONFLICT (data_source_id, interface_name) "
                "DO UPDATE SET last_synced_at = EXCLUDED.last_synced_at, "
                "updated_at = now()"
            ),
            {"ds": str(data_source_id), "iface": interface_name, "ts": synced_at},
        )
        self._db.commit()
        logger.info(
            "Watermark saved: ds=%s iface=%s ts=%s",
            str(data_source_id)[:8], interface_name, synced_at.isoformat(),
        )
