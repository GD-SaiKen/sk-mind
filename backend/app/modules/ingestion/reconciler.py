"""数据对账模块（对标 d2a E3 分段对账，适配 API 场景）。

L1 轻量对账：每次同步后，用 API 第一页返回的 ``total``（来自 ``total_path``）
与 DB 行数做轻量对比，发现缺失记录并写审计。

L2 深度对账 / L3 行级对账：后续任务实现（分段拉取 + 逐段对比 + 修复）。
"""

import logging
from typing import Any, Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

# 默认差异阈值（百分比）。B1.5 将从 YAML reconciliation.threshold_pct 覆盖。
DEFAULT_THRESHOLD_PCT = 5.0


class Reconciler:
    """数据对账执行器。"""

    def __init__(self, db: Session):
        self._db = db

    def reconcile_l1(
        self,
        data_source_id: Any,
        interface_name: str,
        target_table: str,
        api_total: Optional[int],
        batch_id: Any = None,
        threshold_pct: float = DEFAULT_THRESHOLD_PCT,
        enabled: bool = True,
    ) -> Optional[dict]:
        """L1 轻量对账：API 总量 vs DB 行数，写入 ``sync_reconciliations``。

        状态分级（doc 08 §2.2）：
          - diff_count <= 0      -> ``pass``    （窗口拉取场景 DB 历史累计多于窗口总量属正常，无缺失）
          - diff>0 且 ratio<thr  -> ``warning``
          - diff>0 且 ratio>=thr -> ``failed``

        Args:
            data_source_id: 数据源 UUID
            interface_name: 接口名
            target_table: 目标 raw 表（schema.table）
            api_total: API 第一页 total（None 表示接口未配置 total_path，跳过）
            batch_id: 关联批次 ID
            threshold_pct: 差异率阈值（百分比），默认 5
            enabled: 是否启用对账（YAML reconciliation.enabled=false 时跳过）

        Returns:
            写入的对账记录 dict；跳过或失败时返回 None。
        """
        if not enabled:
            logger.info("对账 L1 跳过（enabled=false）: %s", interface_name)
            return None
        if api_total is None:
            logger.info("对账 L1 跳过（无 total_path / api_total=None）: %s", interface_name)
            return None

        # DB 行数（raw 表按接口分表，无需按 _source_id 过滤）
        try:
            db_count = self._db.execute(
                text(f"SELECT COUNT(*) FROM {target_table}")
            ).scalar() or 0
        except Exception as e:  # 表不存在等异常不应中断同步主流程
            logger.warning("对账 L1 查 DB 行数失败 %s: %s", target_table, e)
            return None

        diff_count = int(api_total) - int(db_count)
        # 差异率以"源端总量"为基准，反映 DB 缺失比例
        diff_ratio = (diff_count / api_total) if api_total else 0.0

        if diff_count <= 0:
            status = "pass"
        elif diff_ratio < (threshold_pct / 100.0):
            status = "warning"
        else:
            status = "failed"

        try:
            self._db.execute(
                text(
                    "INSERT INTO sync_reconciliations "
                    "(data_source_id, interface_name, batch_id, check_level, "
                    " api_total, db_count, diff_count, diff_ratio, status) "
                    "VALUES (:ds, :iface, :bid, 'L1', :at, :dc, :df, :dr, :st)"
                ),
                {
                    "ds": data_source_id,
                    "iface": interface_name,
                    "bid": batch_id,
                    "at": int(api_total),
                    "dc": int(db_count),
                    "df": diff_count,
                    "dr": round(float(diff_ratio), 4),
                    "st": status,
                },
            )
            self._db.commit()
            logger.info(
                "对账 L1 完成 %s: api_total=%s db_count=%s diff=%s ratio=%.4f status=%s",
                interface_name, api_total, db_count, diff_count, diff_ratio, status,
            )
            return {
                "interface_name": interface_name,
                "api_total": int(api_total),
                "db_count": int(db_count),
                "diff_count": diff_count,
                "diff_ratio": round(float(diff_ratio), 4),
                "status": status,
            }
        except Exception as e:
            self._db.rollback()
            logger.warning("对账 L1 写入失败 %s: %s", interface_name, e)
            return None
