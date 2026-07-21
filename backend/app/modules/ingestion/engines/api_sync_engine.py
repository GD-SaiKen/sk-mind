"""ApiSyncEngine: config-driven REST API → PostgreSQL sync engine.

Two modes:
- full (backfill): pull all data from history_start_date to today,
  writing through staging → atomic promotion.
- incremental: read last watermark, pull new rows, upsert.

Reuses HttpxApiConnector (fetch), ColumnMapper (map), StageWriter (write).
"""

import logging
import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any, Iterator

import yaml
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.connectors.api_client import HttpxApiConnector
from app.modules.ingestion.connectors.api_mapper import ColumnMapper
from app.modules.ingestion.stage_writer import StageWriter
from app.modules.ingestion.watermark import WatermarkStore

logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    """Load a data source YAML config file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def slice_days(start: date, end: date) -> Iterator[tuple[date, date]]:
    """Yield (day_start, day_end) pairs for time-based API pagination.

    MES API limits queries to max 1 day per request.
    """
    if start > end:
        raise ValueError(f"start {start} > end {end}")
    current = start
    while current <= end:
        yield (current, current + timedelta(days=1))
        current += timedelta(days=1)


class ApiSyncEngine:
    """Executes full or incremental sync for a configured API data source.

    Constructor accepts the parsed YAML config dict and an optional
    fetcher override (for d2a or testing).
    """

    def __init__(self, config: dict, db: Session, fetcher=None):
        self._cfg = config
        self._db = db
        self._writer = StageWriter(db)
        self._watermark = WatermarkStore(db)
        self._fetcher = fetcher  # None → create per-interface

    # ─── public API ────────────────────────────

    def sync_full(
        self,
        task_id: uuid.UUID,
        data_source_id: uuid.UUID,
        interfaces: list[str] | None = None,
    ) -> dict:
        """Full backfill from history_start_date to today.

        Returns:
            {"interface_name": {"success": N, "rejected": N}, ...}
        """
        history_start = date.fromisoformat(
            self._cfg.get("history_start_date", "2020-01-01")
        )
        today = date.today()

        results = {}
        for iface in self._cfg["interfaces"]:
            if interfaces and iface["name"] not in interfaces:
                continue
            batch = self._writer.create_batch(task_id, trigger_type="backfill")
            self._writer.start_batch(batch)

            connector = self._get_connector()
            connector.connect()
            source_id = str(data_source_id)
            try:
                total = {"success": 0, "rejected": 0}
                if iface.get("time_config", {}).get("is_time_based", True):
                    for day_start, day_end in slice_days(history_start, today):
                        day_result = self._sync_day(
                            iface, connector, batch, source_id, "full",
                            day_start, day_end,
                        )
                        total["success"] += day_result["success"]
                        total["rejected"] += day_result["rejected"]
                        logger.info(
                            "  %s %s→%s: +%d rows",
                            iface["name"], day_start, day_end, day_result["success"],
                        )
                else:
                    result = self._sync_non_time(iface, connector, batch, source_id, "full")
                    total = result

                self._writer.finish_batch(
                    batch, "success",
                    total=total["success"],
                    success=total["success"],
                    rejected=total["rejected"],
                )
                results[iface["name"]] = total
            except Exception:
                self._writer.finish_batch(batch, "failed", error_summary="sync error")
                raise
            finally:
                connector.disconnect()

        return results

    def sync_incremental(
        self,
        task_id: uuid.UUID,
        data_source_id: uuid.UUID,
        interfaces: list[str] | None = None,
    ) -> dict:
        """Incremental sync from last watermark to now."""
        today = date.today()
        results = {}
        for iface in self._cfg["interfaces"]:
            if interfaces and iface["name"] not in interfaces:
                continue
            last_sync = self._watermark.get(data_source_id, iface["name"])
            if last_sync is None:
                default_start = today - timedelta(days=30)
                start_day = default_start
            else:
                start_day = last_sync.date()

            batch = self._writer.create_batch(task_id, trigger_type="incremental")
            self._writer.start_batch(batch)
            connector = self._get_connector()
            connector.connect()
            source_id = str(data_source_id)
            try:
                total = {"success": 0, "rejected": 0}
                if iface.get("time_config", {}).get("is_time_based", True):
                    for day_start, day_end in slice_days(start_day, today):
                        day_result = self._sync_day(
                            iface, connector, batch, source_id, "incremental",
                            day_start, day_end,
                        )
                        total["success"] += day_result["success"]
                        total["rejected"] += day_result["rejected"]
                else:
                    total = self._sync_non_time(iface, connector, batch, source_id, "incremental")

                self._writer.finish_batch(
                    batch, "success",
                    total=total["success"],
                    success=total["success"],
                    rejected=total["rejected"],
                )
                self._watermark.set(
                    data_source_id, iface["name"],
                    datetime.now(timezone.utc),
                )
                results[iface["name"]] = total

            except Exception:
                self._writer.finish_batch(batch, "failed", error_summary="sync error")
                raise
            finally:
                connector.disconnect()

        return results

    # ─── helpers ───────────────────────────────

    def _get_connector(self) -> HttpxApiConnector:
        """Build connector from connection config."""
        conn = self._cfg["connection"]
        if self._fetcher:
            return self._fetcher
        return HttpxApiConnector(
            base_url=conn["base_url"],
            auth_type=conn.get("auth_type", "none"),
            auth_header_name=conn.get("auth_header_name", "Authorization"),
            auth_header_name_2=conn.get("auth_header_name_2", ""),
            auth_credentials=conn.get("auth_credentials"),
            auth_credentials_2=conn.get("auth_credentials_2"),
            qps_limit=conn.get("qps_limit", 10),
            timeout=conn.get("timeout", 30),
        )

    def _sync_day(
        self,
        iface: dict,
        connector: HttpxApiConnector,
        batch,
        source_id: str,
        sync_mode: str,
        day_start: date,
        day_end: date,
    ) -> dict:
        """Sync one day slice for a time-based interface."""
        tc = iface.get("time_config", {})
        fmt = tc.get("format", "%Y-%m-%d")

        body = {
            **iface.get("request_body_template", {}),
            "pageNum": 1,
            "pageSize": 100,
            tc.get("param_start", "startDate"): day_start.strftime(fmt),
        }
        if tc.get("param_end"):
            body[tc["param_end"]] = day_end.strftime(fmt)

        # Apply interface-level records_path override
        saved_paths = (connector._records_path, connector._total_path)
        connector._records_path = iface.get("records_path", connector._records_path)
        connector._total_path = iface.get("total_path", connector._total_path)

        target_table = iface["target_table"]
        rows = list(connector.fetch_all_pages(
            iface["endpoint"],
            method=iface.get("method", "POST"),
            body=body,
        ))

        # Restore original paths
        connector._records_path, connector._total_path = saved_paths

        if not rows:
            return {"success": 0, "rejected": 0}

        mapper = ColumnMapper(self._get_table_business_columns(target_table))
        flat_rows = self._flatten_rows(rows, mapper)

        return self._writer.write(
            target_table=target_table,
            batch=batch,
            rows=flat_rows,
            source_id=source_id,
            source_signature=f"{iface['name']}:{day_start}",
            sync_mode=sync_mode,
        )

    def _sync_non_time(
        self,
        iface: dict,
        connector,
        batch,
        source_id: str,
        sync_mode: str,
    ) -> dict:
        """Sync a non-time-based interface (single pull)."""
        body = {**iface.get("request_body_template", {}), "pageNum": 1, "pageSize": 100}

        # Apply interface-level records_path override
        saved_paths = (connector._records_path, connector._total_path)
        connector._records_path = iface.get("records_path", connector._records_path)
        connector._total_path = iface.get("total_path", connector._total_path)

        target_table = iface["target_table"]

        rows = list(connector.fetch_all_pages(
            iface["endpoint"],
            method=iface.get("method", "POST"),
            body=body,
        ))

        # Restore original paths
        connector._records_path, connector._total_path = saved_paths

        if not rows:
            return {"success": 0, "rejected": 0}

        mapper = ColumnMapper(self._get_table_business_columns(target_table))
        flat_rows = self._flatten_rows(rows, mapper)

        return self._writer.write(
            target_table=target_table,
            batch=batch,
            rows=flat_rows,
            source_id=source_id,
            source_signature=iface["name"],
            sync_mode=sync_mode,
        )

    @staticmethod
    def _flatten_rows(rows: list[dict], mapper: ColumnMapper) -> list[dict]:
        """Map API rows to flat dicts via ColumnMapper."""
        flat_rows = []
        for r in rows:
            m = mapper.map_row(r)
            flat = {**m["columns"]}
            for jk, jv in m["jsonb_cols"].items():
                flat[jk] = jv
            flat_rows.append(flat)
        return flat_rows

    def _get_table_business_columns(self, full_table_name: str) -> set[str]:
        """Query information_schema for business columns (excluding tracking)."""
        schema, table = full_table_name.split(".", 1)
        result = self._db.execute(
            text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_schema = :schema AND table_name = :table "
                "AND column_name NOT LIKE '_\\_%' ESCAPE '\\' "
                "ORDER BY ordinal_position"
            ),
            {"schema": schema, "table": table},
        )
        return {row.column_name for row in result}
