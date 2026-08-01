"""软删除检测模块 (B3.1)。

对 PK-based 接口，定期拉取全量 API PK 列表，与 raw 表中已有 PK 取差集，
将「DB 有但 API 没有」的行标记为软删除（``_deleted_at = now()``）。

设计要点：
- 复用 ``HttpxApiConnector``（与 ApiSyncEngine 同一连接构建方式）。
- 分页拉取，每页 5000 条，避免单次请求超时；大表（十万级）按 PK 分块 UPDATE。
- 差集计算在 Python 内完成（API PK 集合 - DB PK 集合），再分块 UPDATE。
- API 返回空（疑似故障）时**跳过标记**，避免把全表误判为删除。
- 对「API 有但 DB 已标记删除」的行执行 un-mark（``_deleted_at = NULL``），
  保证软删除可逆（数据回填/API 抖动后自动恢复）。
"""

from datetime import datetime, timezone
from typing import Optional
import logging

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.connectors.api_client import HttpxApiConnector

logger = logging.getLogger(__name__)

# 每批处理 / 每批 UPDATE 的 PK 数量（大表分段，避免单语句过大）
CHUNK_SIZE = 5000


def _norm(v) -> Optional[str]:
    """归一化 PK 值用于集合比较。

    API 常返回 int（如 123），raw 表列是 text（'123'），直接比较会失配。
    统一转 str 后比较；None 保持 None（不参与差集）。
    """
    if v is None:
        return None
    return str(v).strip()


class SoftDeleteDetector:
    """按接口检测软删除。"""

    def __init__(self, config: dict, db: Session):
        self._cfg = config
        self._db = db

    # ── 公共 API ──

    def detect(
        self,
        interface_name: str,
        target_table: str,
        pk_fields: list[str],
        *,
        ds_id=None,
        enable: Optional[bool] = None,
    ) -> dict:
        """检测并标记软删除。

        Args:
            interface_name: 接口名（用于定位 YAML 接口定义与日志）。
            target_table: 目标 raw 表（schema.table）。
            pk_fields: 主键字段列表（API/raw 列同名）。
            ds_id: 数据源 id（仅用于日志）。
            enable: 是否启用检测。None → 读 YAML 接口 ``detect_deletes``。

        Returns:
            {"skipped": bool, "reason": str, "deleted": int, "api_count": int}
        """
        iface = self._find_interface(interface_name)
        if iface is None:
            logger.warning("软删除检测 %s: 未在 config 找到接口定义", interface_name)
            return {"skipped": True, "reason": "interface_not_found", "deleted": 0}

        eff = enable if enable is not None else bool(iface.get("detect_deletes", False))
        if not eff:
            logger.info("软删除检测 %s: 未启用（detect_deletes=false），跳过", interface_name)
            return {"skipped": True, "reason": "detect_deletes_disabled", "deleted": 0}
        if not pk_fields:
            logger.info("软删除检测 %s: 无 PK 字段，跳过", interface_name)
            return {"skipped": True, "reason": "no_pk_fields", "deleted": 0}

        # 1. 确保 _deleted_at 列存在（已有 raw 表迁移）
        self._ensure_deleted_at_column(target_table)

        # 2. 拉取全量 API PK
        connector = self._build_connector()
        api_pks = self._fetch_api_pks(connector, iface, pk_fields)
        if not api_pks:
            # 疑似 API 故障：宁可不动，也不误删全表
            logger.warning(
                "软删除检测 %s: API 返回 0 条 PK，疑似接口故障，跳过标记以避免误删",
                interface_name,
            )
            return {"skipped": True, "reason": "api_empty", "deleted": 0}

        # 3. 差集 → 标记删除 + 还原复现行
        deleted = self._mark_diff(target_table, pk_fields, api_pks)
        logger.info(
            "软删除检测 %s: 标记删除 %d 行（API 现有 %d PK，数据源=%s）",
            interface_name, deleted, len(api_pks), ds_id,
        )
        return {"skipped": False, "deleted": deleted, "api_count": len(api_pks)}

    # ── 内部 ──

    def _find_interface(self, name: str) -> Optional[dict]:
        for i in self._cfg.get("interfaces", []):
            if i.get("name") == name:
                return i
        return None

    def _build_connector(self) -> HttpxApiConnector:
        import os

        conn = self._cfg["connection"]
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
            proxy=conn.get("proxy"),
        )

    def _ensure_deleted_at_column(self, target_table: str) -> None:
        self._db.execute(
            text(f'ALTER TABLE {target_table} ADD COLUMN IF NOT EXISTS "_deleted_at" TIMESTAMP')
        )
        self._db.commit()

    def _fetch_api_pks(
        self, connector: HttpxApiConnector, iface: dict, pk_fields: list[str]
    ) -> set:
        """分页拉取 API 全量数据，提取 PK 集合（仅保留全 PK 非空的行）。"""
        api_pks: set = set()
        # 取全量（无日期参数）→ 用宽范围；pageSize=5000 减少请求次数
        body = {**iface.get("request_body_template", {}), "pageNum": 1, "pageSize": CHUNK_SIZE}

        saved = (connector._records_path, connector._total_path)
        connector._records_path = iface.get("records_path", connector._records_path)
        connector._total_path = iface.get("total_path", connector._total_path)
        connector.connect()
        try:
            for row in connector.fetch_all_pages(
                iface["endpoint"],
                method=iface.get("method", "POST"),
                body=body,
                page_size=CHUNK_SIZE,
            ):
                pk_val = tuple(_norm(row.get(k)) for k in pk_fields)
                if all(v is not None for v in pk_val):
                    api_pks.add(pk_val)
        finally:
            connector.disconnect()
            connector._records_path, connector._total_path = saved
        return api_pks

    def _mark_diff(self, target_table: str, pk_fields: list[str], api_pks: set) -> int:
        """计算 DB PK 与 API PK 的差集，标记删除 / 还原复现。

        Returns:
            本运行标记删除的行数。
        """
        col_list = ", ".join(f'"{c}"' for c in pk_fields)
        # 同时取出 _deleted_at，避免对每行的二次查询
        rows = self._db.execute(
            text(f'SELECT {col_list}, "_deleted_at" FROM {target_table}')
        ).mappings().all()

        db_map: dict = {}  # norm_pk -> (orig_tuple, deleted_at)
        for r in rows:
            orig = tuple(r[c] for c in pk_fields)
            norm = tuple(_norm(r[c]) for c in pk_fields)
            db_map[norm] = (orig, r["_deleted_at"])

        db_pks_norm = set(db_map.keys())
        api_pks_norm = {tuple(_norm(v) for v in pk) for pk in api_pks}

        # DB 有、API 无 → 标记删除
        to_mark = [db_map[p][0] for p in db_pks_norm if p not in api_pks_norm]
        # API 有、DB 已标记删除 → 还原（数据回填/抖动恢复）
        to_unmark = [
            db_map[p][0] for p in api_pks_norm
            if p in db_map and db_map[p][1] is not None
        ]

        placeholders = ", ".join(f":{c}" for c in pk_fields)
        mark_stmt = text(
            f'UPDATE {target_table} SET "_deleted_at" = :ts '
            f'WHERE ({col_list}) = ({placeholders}) AND "_deleted_at" IS NULL'
        )
        unmark_stmt = text(
            f'UPDATE {target_table} SET "_deleted_at" = NULL '
            f'WHERE ({col_list}) = ({placeholders}) AND "_deleted_at" IS NOT NULL'
        )

        run_ts = datetime.now(timezone.utc)
        for chunk in _chunks(to_mark, CHUNK_SIZE):
            self._db.execute(
                mark_stmt,
                [{"ts": run_ts, **dict(zip(pk_fields, p))} for p in chunk],
            )
        for chunk in _chunks(to_unmark, CHUNK_SIZE):
            self._db.execute(
                unmark_stmt,
                [dict(zip(pk_fields, p)) for p in chunk],
            )
        self._db.commit()

        # 本运行标记数（精确，按时间戳聚合）
        n = self._db.execute(
            text(f'SELECT count(*) FROM {target_table} WHERE "_deleted_at" = :ts'),
            {"ts": run_ts},
        ).scalar() or 0
        return int(n)


def _chunks(lst: list, n: int):
    """把列表按 n 切片。"""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]
