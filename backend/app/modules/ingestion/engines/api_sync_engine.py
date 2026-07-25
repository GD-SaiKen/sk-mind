"""ApiSyncEngine: config-driven REST API -> PostgreSQL sync engine.

Sync strategy per interface:
- **First sync** (no watermark, is_time_based=True): full pull with a wide date
  range (2020-01-01 ~ now). Some MES APIs accept date filtering (optional params);
  sending a broad range ensures we get all data in one paginated pull.
  Single paginated request, NOT day-by-day slicing.
- **Incremental sync** (watermark exists, is_time_based=True): pull only data
  from ``watermark - replay_days`` to ``now`` via the API's date params.
  Upsert ensures overlapping data is idempotent.
- **Non-time-based interfaces** (is_time_based=False): always full pull
  (these are small config/master-data tables that don't support date filtering).

Reuses HttpxApiConnector (fetch), ColumnMapper (map), StageWriter (write),
WatermarkStore (watermark tracking).
"""

import json
import logging
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

import yaml
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.connectors.api_client import HttpxApiConnector
from app.modules.ingestion.connectors.api_mapper import ColumnMapper
from app.modules.ingestion.reconciler import DEFAULT_THRESHOLD_PCT, Reconciler
from app.modules.ingestion.schema_manager import TRACKING_COLUMNS, _INDEX_COLUMNS
from app.modules.ingestion.stage_writer import StageWriter
from app.modules.ingestion.watermark import WatermarkStore

logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    """Load a data source YAML config file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


class ApiSyncEngine:
    """Executes sync for a configured API data source.

    First sync → full pull; subsequent syncs → incremental (date-filtered).
    Non-time-based interfaces always do full pull.
    """

    def __init__(
        self,
        config: dict,
        db: Session,
        fetcher=None,
        replay_window_days: int = 3,
    ):
        self._cfg = config
        self._db = db
        self._writer = StageWriter(db)
        self._watermark = WatermarkStore(db)
        self._reconciler = Reconciler(db)
        self._fetcher = fetcher  # None -> create per-interface
        self._ensured_tables: set[str] = set()
        self._replay_days = replay_window_days

    # ─── public API ────────────────────────────

    def sync_all(
        self,
        task_id: uuid.UUID,
        data_source_id: uuid.UUID,
        interfaces: list[str] | None = None,
        batch=None,
    ) -> dict:
        """Sync every (or selected) interface.

        For each interface:
        1. Determine sync mode: full (first time / non-time-based) or incremental.
        2. Build request body — add date params for incremental.
        3. Paginate through all pages.
        4. Upsert rows into the target raw table.
        5. Save watermark on success.

        Returns:
            {"interface_name": {"success": N, "rejected": N, "mode": "full"|"incremental"}, ...}
        """
        results: dict[str, dict] = {}
        # 仅选中真正要同步的接口（与手动/部分同步一致）
        selected = [
            i for i in self._cfg["interfaces"]
            if not interfaces or i["name"] in interfaces
        ]
        multi = len(selected) > 1
        for iface in selected:
            # ⚠️ 关键修复（多接口任务 batch 错标 bug）：
            # 传入的 `batch` 是路由预创建的「任务级父 batch」。它只应作为聚合摘要
            # 记录（由调用方 run_api_full_sync 在 sync_all 之后写入总和），绝不能
            # 被复用为某个接口的批次——否则它会顶着第一个接口名（如 andonApiController）
            # 显示聚合总量，与真正的 per-interface 子批次重名，UI 出现两个同名行、
            # 数字对不上的错觉（之前表现为「闪一下 114 又变 691」）。
            # 因此：单接口任务才复用父 batch（保持 1 行的历史行为），多接口任务每个
            # 接口都建独立子 batch，父 batch 留给调用方写聚合摘要。
            if not multi and batch is not None:
                b = batch
            else:
                b = self._writer.create_batch(task_id, trigger_type="manual")
            b.source_signature = iface["name"]
            self._writer.start_batch(b)

            connector = self._get_connector()
            connector.connect()
            try:
                result = self._sync_interface(iface, connector, b, data_source_id)
                self._writer.finish_batch(
                    b, "success",
                    pulled=result.get("pulled", 0),
                    success=result.get("success", 0),
                    rejected=result.get("rejected", 0),
                    skip=result.get("unchanged", 0),
                    source_signature=iface["name"],
                )
                results[iface["name"]] = result
            except Exception:
                self._writer.finish_batch(b, "failed", error_summary="sync error")
                raise
            finally:
                connector.disconnect()

        return results

    # ─── helpers ───────────────────────────────

    def _get_connector(self) -> HttpxApiConnector:
        """Build connector from connection config.

        Resolves ``auth_credentials_env`` / ``auth_credentials_2_env`` from
        environment variables when the value keys are absent.
        """
        import os

        conn = self._cfg["connection"]
        if self._fetcher:
            return self._fetcher

        # Resolve env-var-style credential references
        auth_credentials = conn.get("auth_credentials")
        if not auth_credentials:
            env_key = conn.get("auth_credentials_env")
            if env_key:
                auth_credentials = os.environ.get(env_key, "")

        auth_credentials_2 = conn.get("auth_credentials_2")
        if not auth_credentials_2:
            env_key_2 = conn.get("auth_credentials_2_env")
            if env_key_2:
                auth_credentials_2 = os.environ.get(env_key_2, "")

        return HttpxApiConnector(
            base_url=conn["base_url"],
            auth_type=conn.get("auth_type", "none"),
            auth_header_name=conn.get("auth_header_name", "Authorization"),
            auth_header_name_2=conn.get("auth_header_name_2", ""),
            auth_credentials=auth_credentials,
            auth_credentials_2=auth_credentials_2,
            qps_limit=conn.get("qps_limit", 10),
            timeout=conn.get("timeout", 30),
            ssl_verify=conn.get("ssl_verify", True),
        )

    def _ensure_raw_table(self, target_table: str, sample_row: dict) -> None:
        """Create the raw table if it doesn't exist, inferring columns from a sample API row.

        Must be called BEFORE ``ColumnMapper`` so it can find the business columns.
        """
        if target_table in self._ensured_tables:
            return

        schema, table = target_table.split(".", 1)
        check = text(
            "SELECT EXISTS (SELECT 1 FROM information_schema.tables "
            "WHERE table_schema = :schema AND table_name = :table)"
        )
        exists = self._db.execute(check, {"schema": schema, "table": table}).scalar_one()
        if exists:
            self._ensured_tables.add(target_table)
            return

        # Convert camelCase API keys to snake_case column names
        col_names = {ColumnMapper._to_snake(k) for k in sample_row.keys()}

        col_defs: list[str] = []
        for col in sorted(col_names):
            col_defs.append(f'    "{col}" TEXT')

        for name, typedef in TRACKING_COLUMNS:
            col_defs.append(f'    "{name}" {typedef}')

        full_name = f"{schema}.{table}"
        ddl = f"CREATE TABLE {full_name} (\n" + ",\n".join(col_defs) + "\n)"
        self._db.execute(text(ddl))
        self._db.commit()

        for idx_col in _INDEX_COLUMNS:
            idx_name = f"idx_{table}_{idx_col}"
            self._db.execute(text(
                f"CREATE INDEX IF NOT EXISTS {idx_name} ON {full_name} ({idx_col})"
            ))
        self._db.commit()

        self._ensured_tables.add(target_table)
        logger.info("Auto-created raw table %s with %d data columns", full_name, len(col_names))

    def _determine_sync_mode(
        self, iface: dict, data_source_id: uuid.UUID
    ) -> tuple[str, Optional[datetime], Optional[datetime]]:
        """Determine sync mode and date range for this interface.

        Returns:
            (mode, start_dt, end_dt)
            - mode="full", start=None, end=None: non-time-based → no date params
            - mode="full", start=2020-01-01, end=now: first sync of time-based →
              wide date range (API date params are optional, broad range ensures
              complete data in one pull)
            - mode="incremental", start=wm-replay, end=now: time-based + watermark
        """
        time_cfg = iface.get("time_config", {})
        is_time_based = time_cfg.get("is_time_based", False)

        if not is_time_based:
            return "full", None, None

        now = datetime.now(timezone.utc)

        # Time-based: check watermark
        wm = self._watermark.get(data_source_id, iface["name"])
        if wm is None:
            # First sync — wide date range (single request, NOT day-by-day slicing).
            # API date params are optional; sending a broad range ensures we get
            # all data in one paginated pull even if the API supports date filtering.
            start = datetime(2020, 1, 1, tzinfo=timezone.utc)
            return "full", start, now

        # Incremental: replay window for safety (upsert handles overlaps)
        start = wm - timedelta(days=self._replay_days)
        return "incremental", start, now

    def _build_date_params(
        self, iface: dict, start_dt: datetime, end_dt: datetime
    ) -> dict:
        """Build date parameter dict for sync from time_config.

        Supports three format types in YAML ``time_config.format``:
        - ``millis``: Java millisecond timestamps (int), e.g. 1784822400000
        - ``"%Y-%m-%d"``: date-only string, e.g. "2026-07-22"
        - ``"%Y-%m-%d %H:%M:%S"``: datetime string, e.g. "2026-07-22 00:00:00"

        All datetimes are converted to Beijing time (UTC+8) before formatting,
        because MES APIs expect local time strings/timestamps.
        """
        time_cfg = iface.get("time_config", {})
        param_start = time_cfg.get("param_start", "startDate")
        param_end = time_cfg.get("param_end", "endDate")
        fmt = time_cfg.get("format", "%Y-%m-%d")

        # Convert UTC → Beijing time (UTC+8) — MES APIs expect local time
        bj_tz = timezone(timedelta(hours=8))
        start_local = start_dt.astimezone(bj_tz)
        end_local = end_dt.astimezone(bj_tz)

        if fmt == "millis":
            # Java millisecond timestamps (int) — .timestamp() returns Unix
            # seconds in float; multiply by 1000 for millis.
            return {
                param_start: int(start_local.timestamp() * 1000),
                param_end: int(end_local.timestamp() * 1000),
            }

        return {
            param_start: start_local.strftime(fmt),
            param_end: end_local.strftime(fmt),
        }

    def _sync_interface(
        self,
        iface: dict,
        connector: HttpxApiConnector,
        batch,
        data_source_id: uuid.UUID,
    ) -> dict:
        """Sync a single interface.

        Sync mode is determined by watermark + time_config:
        - First sync or non-time-based → full pull (no date params)
        - Watermark exists + time-based → incremental (date-filtered)

        After successful write, watermark is saved/updated.
        """
        # ── Determine sync mode ──
        mode, start_dt, end_dt = self._determine_sync_mode(iface, data_source_id)

        # ── Build request body ──
        body = {**iface.get("request_body_template", {}), "pageNum": 1, "pageSize": 100}

        # Add date params for both incremental and first-full (time-based APIs
        # may accept date filtering even though params are optional).
        time_cfg = iface.get("time_config", {})

        if start_dt is not None:
            date_params = self._build_date_params(iface, start_dt, end_dt)
            body.update(date_params)

        # Format date range for progress message (handle millis format)
        bj_tz = timezone(timedelta(hours=8))
        start_local = start_dt.astimezone(bj_tz) if start_dt else None
        end_local = end_dt.astimezone(bj_tz) if end_dt else None
        range_str = (
            f"{start_local:%Y-%m-%d %H:%M} ~ {end_local:%Y-%m-%d %H:%M}"
            if start_local and end_local else ""
        )

        if mode == "incremental":
            progress_msg = f"正在拉取 {iface['name']} (增量: {range_str})..."
        elif start_dt is not None:
            progress_msg = f"正在拉取 {iface['name']} (全量: {range_str})..."
        else:
            progress_msg = f"正在拉取 {iface['name']} (全量)..."

        # Apply interface-level records_path override
        saved_paths = (connector._records_path, connector._total_path)
        connector._records_path = iface.get("records_path", connector._records_path)
        connector._total_path = iface.get("total_path", connector._total_path)

        target_table = iface["target_table"]

        # ── Progress: fetching data ──
        self._update_progress(batch, progress_msg)
        logger.info("Syncing %s: mode=%s", iface["name"], mode)

        rows = list(connector.fetch_all_pages(
            iface["endpoint"],
            method=iface.get("method", "POST"),
            body=body,
        ))
        # 捕获 API 第一页 total（来自 total_path），供对账 L1 使用
        api_total = connector.last_total

        # Restore original paths
        connector._records_path, connector._total_path = saved_paths

        if not rows:
            self._update_progress(batch, f"{iface['name']}: 无数据")
            # Only save watermark for incremental syncs (empty result is valid —
            # no new data since last sync). For first full sync, empty result
            # might indicate an API error — don't save watermark so next sync
            # retries as full.
            if mode == "incremental":
                self._watermark.save(data_source_id, iface["name"])
            # 对账 L1（B1.3）：即使无数据也记录（若 API 有 total）
            self._run_reconcile_l1(
                data_source_id, iface, target_table, api_total, batch,
                sync_mode=mode, pulled=0,
            )
            return {
                "success": 0, "rejected": 0,
                "inserted": 0, "updated": 0, "unchanged": 0,
                "pulled": 0, "mode": mode,
            }

        # ── Progress: writing rows ──
        pulled = len(rows)
        self._update_progress(batch, f"正在写入 {pulled} 行 → {target_table}...")

        # Ensure the raw table exists before mapping (critical: first sync)
        self._ensure_raw_table(target_table, rows[0])

        # Schema 漂移检测（B1.2）：检测 API 新字段并自动加列，必须在
        # ColumnMapper 初始化之前执行。异常不中断同步主流程。
        try:
            self._check_schema_drift(target_table, rows[0])
        except Exception as e:
            logger.warning("Schema drift 检测失败 %s: %s", target_table, e)

        mapper = ColumnMapper(self._get_table_business_columns(target_table))
        flat_rows = self._flatten_rows(rows, mapper)

        pk = iface.get("pk_fields", [])
        validation_rejected = 0
        if pk:
            flat_rows, validation_rejected = self._validate_rows(flat_rows, pk)

        result = self._writer.write(
            target_table=target_table,
            batch=batch,
            rows=flat_rows,
            source_id=str(data_source_id),
            source_signature=iface["name"],
            sync_mode="upsert" if pk else "insert",
            pk_fields=pk if pk else None,
        )

        # ── Save watermark on success ──
        self._watermark.save(data_source_id, iface["name"])

        # ── Progress: done ──
        # 写入行数 = 实际变更（新增+更新），与"拉取行数/跳过行数"区分开
        self._update_progress(
            batch,
            f"{iface['name']} 完成 ({mode}): 写入 {result.get('success', 0)} 行 "
            f"(新增 {result.get('inserted', 0)}, 更新 {result.get('updated', 0)}, "
            f"跳过 {result.get('unchanged', 0)}), 拒绝 {result.get('rejected', 0)}",
        )
        # 透传真实拉取量；把"写入前校验拒绝"并回写入拒绝计数
        result["pulled"] = pulled
        result["rejected"] = result.get("rejected", 0) + validation_rejected
        result["mode"] = mode
        # 对账 L1（B1.3）：按同步模式选对比基准（增量 vs 本批拉取数）
        self._run_reconcile_l1(
            data_source_id, iface, target_table, api_total, batch,
            sync_mode=mode, pulled=pulled,
        )
        return result

    def _update_progress(self, batch, step: str) -> None:
        """Update batch.progress_step and commit so the SSE endpoint can read it."""
        try:
            batch.progress_step = step
            self._db.commit()
        except Exception:
            self._db.rollback()

    def _validate_rows(
        self, rows: list[dict], pk_fields: list[str]
    ) -> tuple[list[dict], int]:
        """Basic pre-write validation.

        - PK non-null: rows with null/empty pk are rejected (dropped).
        - Dedup within batch: duplicate pk keeps the last occurrence.
        - Quality flags: non-numeric create_date flagged (not blocking).

        Returns: (valid_rows, rejected_count)
        """
        if not pk_fields:
            return rows, 0

        valid: list[dict] = []
        rejected = 0
        seen: dict[str, int] = {}

        for row in rows:
            pk_vals = [row.get(pk) for pk in pk_fields]
            if any(v is None or v == "" for v in pk_vals):
                rejected += 1
                continue
            pk_key = "|".join(str(v) for v in pk_vals)
            if pk_key in seen:
                valid[seen[pk_key]] = row
                continue
            seen[pk_key] = len(valid)

            flags = row.get("_quality_flags", [])
            if not isinstance(flags, list):
                flags = []
            cd = row.get("create_date")
            if cd is not None:
                try:
                    int(str(cd))
                except (ValueError, TypeError):
                    flags = flags + ["invalid_create_date"]
            if flags:
                row["_quality_flags"] = flags
            valid.append(row)

        return valid, rejected

    @staticmethod
    def _flatten_rows(rows: list[dict], mapper: ColumnMapper) -> list[dict]:
        """Map API rows to flat dicts via ColumnMapper.

        Raw layer stores all values as-is — no type conversion.
        Timestamps remain as Java-millis integers; type coercion
        to proper datetime is the Clean layer's responsibility.
        """
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

    def _check_schema_drift(
        self, target_table: str, sample_row: dict
    ) -> list[str]:
        """检测并处理 schema 漂移：API 返回了新字段但 DB 表没有对应列。

        对比 ``sample_row`` 的 snake_case keys 与 DB 业务列，新列自动
        ``ALTER TABLE ... ADD COLUMN IF NOT EXISTS TEXT``，并写入
        ``sync_schema_changes`` 审计。无漂移返回空列表。

        ⚠️ 必须在 ``_sync_interface`` 中 ``_ensure_raw_table`` 之后、``ColumnMapper``
        初始化之前调用，且每次同步都执行（不能放在 ``_ensure_raw_table`` 内部，
        因为该方法在表已存在时直接 return）。异常不中断同步主流程。

        Returns:
            新增的列名列表（空列表 = 无漂移）。
        """
        existing = self._get_table_business_columns(target_table)
        sample_cols = {ColumnMapper._to_snake(k) for k in sample_row.keys()}
        new_cols = sample_cols - existing

        if not new_cols:
            return []

        for col in sorted(new_cols):
            self._db.execute(text(
                f'ALTER TABLE {target_table} ADD COLUMN IF NOT EXISTS "{col}" TEXT'
            ))
            logger.warning("Schema drift: %s 新增列 %s", target_table, col)

        self._db.commit()

        # 记录审计（多列合并为一行，column_name 用逗号连接）
        self._db.execute(
            text(
                "INSERT INTO sync_schema_changes "
                "(table_name, change_type, column_name, detail) "
                "VALUES (:t, 'added', :c, :d)"
            ),
            {
                "t": target_table,
                "c": ",".join(sorted(new_cols)),
                "d": json.dumps({"sample_keys": list(sample_row.keys())}),
            },
        )
        self._db.commit()

        return sorted(new_cols)

    def _run_reconcile_l1(
        self,
        data_source_id,
        iface: dict,
        target_table: str,
        api_total: Optional[int],
        batch,
        sync_mode: str = "full",
        pulled: int = 0,
    ) -> None:
        """调用对账 L1，异常不中断同步主流程。

        Args:
            sync_mode: 当前同步模式（full / incremental），决定对比基准。
            pulled: 本批实际拉取行数，增量模式下作为对比基准（验证窗口内拉全）。
        """
        try:
            recon_cfg = iface.get("reconciliation", {}) or {}
            self._reconciler.reconcile_l1(
                data_source_id=data_source_id,
                interface_name=iface["name"],
                target_table=target_table,
                api_total=api_total,
                batch_id=getattr(batch, "id", None),
                sync_mode=sync_mode,
                pulled=pulled,
                threshold_pct=float(recon_cfg.get("threshold_pct", DEFAULT_THRESHOLD_PCT)),
                enabled=bool(recon_cfg.get("enabled", True)),
                auto_repair=bool(recon_cfg.get("auto_repair", False)),
            )
        except Exception as e:
            logger.warning("对账 L1 执行异常 %s: %s", iface["name"], e)
