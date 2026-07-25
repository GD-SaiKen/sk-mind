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
        sync_mode: str = "full",
        pulled: Optional[int] = None,
        threshold_pct: float = DEFAULT_THRESHOLD_PCT,
        enabled: bool = True,
        auto_repair: bool = False,
    ) -> Optional[dict]:
        """L1 轻量对账：按同步模式分作用域对比，写入 ``sync_reconciliations``。

        ⚠️ 作用域（关键修正，B1.3）：
          - **全量 (full)**：``api_total``（API 整库总量）对比 ``db_count``（整张
            raw 表行数）。二者应大致相等。
          - **增量 (incremental)**：``api_total`` 是「当前时间窗口」里 API 报告的
            总量，绝不能和整表累计行数对比（否则产生无意义的负差异率）。正确对比
            基准是「本批实际拉取行数 ``pulled``」——验证窗口内是否拉全（分页截断 /
            API 丢返回等问题会让 pulled < api_total）。

        状态分级（doc 08 §2.2，统一以 ``compared`` 为基准）：
          - diff_count = api_total - compared
          - diff_count <= 0      -> ``pass``
          - diff>0 且 ratio<thr  -> ``warning``
          - diff>0 且 ratio>=thr -> ``failed``

        Args:
            data_source_id: 数据源 UUID
            interface_name: 接口名
            target_table: 目标 raw 表（schema.table）
            api_total: API 第一页 total（None 表示接口未配置 total_path，跳过）
            batch_id: 关联批次 ID
            sync_mode: 同步模式 ``full`` / ``incremental``
            pulled: 本批实际拉取行数（增量模式必传；全量模式可省略）
            threshold_pct: 差异率阈值（百分比），默认 5
            enabled: 是否启用对账（YAML reconciliation.enabled=false 时跳过）
            auto_repair: 差异超阈值时是否自动触发 L2 修复（L2 尚未实现，仅记录意图）

        Returns:
            写入的对账记录 dict；跳过或失败时返回 None。
        """
        if not enabled:
            logger.info("对账 L1 跳过（enabled=false）: %s", interface_name)
            return None
        if api_total is None:
            logger.info("对账 L1 跳过（无 total_path / api_total=None）: %s", interface_name)
            return None

        pulled_count = int(pulled) if pulled is not None else 0
        db_count = 0

        if sync_mode == "incremental":
            # 增量：对比基准是「本批拉取行数」，不查整表（避免无意义的负差异 + 大表 COUNT 开销）
            compared = pulled_count
        else:
            # 全量：对比整表行数
            try:
                db_count = self._db.execute(
                    text(f"SELECT COUNT(*) FROM {target_table}")
                ).scalar() or 0
            except Exception as e:  # 表不存在等异常不应中断同步主流程
                logger.warning("对账 L1 查 DB 行数失败 %s: %s", target_table, e)
                return None
            compared = int(db_count)

        diff_count = int(api_total) - compared
        # 差异率以"源端总量"为基准，反映缺失比例
        diff_ratio = (diff_count / api_total) if api_total else 0.0

        # 状态分级（关键：增量按 pulled 与 api_total 的方向判定，
        # 避免 API total 字段不可信时被 diff<=0 一律粉饰为"一致"）
        status = "pass"
        if sync_mode == "incremental":
            if pulled_count < api_total:
                # 窗口内没拉全：分页截断 / API 丢返回 → 真实丢数
                status = "failed" if diff_ratio >= (threshold_pct / 100.0) else "warning"
            elif api_total > 0 and (pulled_count - api_total) / api_total > 0.2:
                # 实际拉取远超 API 声明总量 → total 字段不可信，L1 失去校验意义
                status = "warning"
            else:
                status = "pass"
        else:
            if diff_count <= 0:
                # 全量：compared=db_count。若 DB 行数远超 API 声明总量 → total 不可信
                if api_total > 0 and (db_count - api_total) / api_total > 0.2:
                    status = "warning"
                else:
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
                    " api_total, db_count, pulled_count, diff_count, diff_ratio, "
                    " status, sync_mode) "
                    "VALUES (:ds, :iface, :bid, 'L1', :at, :dc, :pc, :df, :dr, :st, :sm)"
                ),
                {
                    "ds": data_source_id,
                    "iface": interface_name,
                    "bid": batch_id,
                    "at": int(api_total),
                    "dc": int(db_count),
                    "pc": pulled_count,
                    "df": diff_count,
                    "dr": round(float(diff_ratio), 4),
                    "st": status,
                    "sm": sync_mode,
                },
            )
            self._db.commit()
            logger.info(
                "对账 L1 完成 %s: mode=%s api_total=%s compared=%s (db=%s/pulled=%s) "
                "diff=%s ratio=%.4f status=%s",
                interface_name, sync_mode, api_total, compared,
                db_count, pulled_count, diff_count, diff_ratio, status,
            )
            # auto_repair：差异超阈值时记录 L2 自动修复意图（L2 尚未实现）
            if auto_repair and status == "failed":
                logger.info(
                    "对账 L1 差异超阈值且 auto_repair=true，已记录 L2 自动修复意图（L2 未实现）: %s",
                    interface_name,
                )
            return {
                "interface_name": interface_name,
                "api_total": int(api_total),
                "db_count": int(db_count),
                "pulled_count": pulled_count,
                "diff_count": diff_count,
                "diff_ratio": round(float(diff_ratio), 4),
                "status": status,
                "sync_mode": sync_mode,
                "auto_repair": auto_repair,
            }
        except Exception as e:
            self._db.rollback()
            logger.warning("对账 L1 写入失败 %s: %s", interface_name, e)
            return None
