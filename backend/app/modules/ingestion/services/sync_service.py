"""同步编排服务（sync — RQ Worker 使用）。

对应策略文档：
- 02-数据库视图同步策略 §3
- 03-API拉取同步策略 §6, §10
- 06-同步运维与前后端交互 §1
"""

import hashlib
import json
import logging
import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.ingestion.connectors.base import ColumnInfo, DatabaseConnector, ApiConnector
from app.modules.ingestion.models import ImportError, IngestionBatch, IngestionTask
from app.modules.ingestion.services.sync_database import get_sync_db

logger = logging.getLogger(__name__)


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class SyncService:
    """数据同步编排服务。

    在 RQ Worker 中运行，所有数据库操作用同步 Session。
    """

    def __init__(self, db: Session | None = None):
        self._db = db or get_sync_db()

    # ── 全量同步（数据库视图模式） ─────────────

    def execute_full_sync(
        self,
        task_id: uuid.UUID,
        source_object_name: str,
        connector: DatabaseConnector,
        raw_table_name: str,
        rq_job=None,
    ) -> dict[str, int]:
        """执行全量同步。

        Args:
            task_id: 任务 ID。
            source_object_name: 源表名。
            connector: 数据库连接器（已连接）。
            raw_table_name: 目标 Raw 表名（含 schema，如 "raw.erp_dbo_sale_order"）。
            rq_job: RQ Job 对象（用于进度上报）。

        Returns:
            统计信息: {"total": int, "success": int, "failed": int}。
        """
        batch = self._create_batch(task_id, "manual")
        self._update_batch_status(batch, "running")
        self._update_progress(rq_job, 0, f"开始全量同步: {source_object_name}")

        try:
            # 1. Schema 检测
            columns = connector.fetch_schema(source_object_name)
            self._ensure_raw_table(raw_table_name, columns)

            # 2. 分批同步
            total = connector.count_rows(source_object_name)
            batch_size = self._choose_batch_size(total)
            offset = 0
            success_count = 0
            failed_count = 0

            self._update_progress(
                rq_job, 0,
                f"全量同步中: {source_object_name}, 总量 {total} 行"
            )

            while offset < total:
                progress = int(offset / total * 100) if total else 100
                self._update_progress(
                    rq_job, progress,
                    f"同步中 {offset}/{total}"
                )

                rows = list(connector.fetch_data(
                    source_object_name, offset=offset, limit=batch_size
                ))

                for row in rows:
                    try:
                        record = dict(row)
                        record["_batch_id"] = str(batch.id)
                        record["_source_system"] = "ERP_E10"
                        record["_source_object"] = source_object_name
                        record["_source_row_hash"] = self._compute_hash(record)
                        record["_ingested_at"] = _utcnow()

                        self._insert_raw_row(raw_table_name, record)
                        success_count += 1
                    except Exception as e:
                        failed_count += 1
                        self._record_error(
                            batch_id=batch.id,
                            source_object=source_object_name,
                            error_level="row",
                            error_type="insert_error",
                            error_message=str(e),
                            raw_value=str(row)[:500],
                        )

                self._db.commit()
                offset += batch_size

            # 3. 更新批次
            batch.record_count = total
            batch.success_count = success_count
            batch.fail_count = failed_count
            batch.status = "success" if failed_count == 0 else "partial_success"
            batch.finished_at = _utcnow()
            self._db.commit()

            self._update_progress(rq_job, 100, "全量同步完成")
            return {"total": total, "success": success_count, "failed": failed_count}

        except Exception as e:
            logger.exception("全量同步失败: %s", e)
            batch.status = "failed"
            batch.error_summary = str(e)[:1000]
            batch.finished_at = _utcnow()
            self._db.commit()
            raise

    # ── API 拉取同步 ────────────────────────

    def execute_api_pull(
        self,
        task_id: uuid.UUID,
        endpoint: str,
        method: str,
        body: dict[str, Any] | None,
        source_system: str,
        connector: ApiConnector,
        page_size: int = 100,
        max_pages: int | None = None,
        rq_job=None,
    ) -> dict[str, int]:
        """执行 API 拉取同步。

        Args:
            task_id: 任务 ID。
            endpoint: API 端点路径。
            method: HTTP 方法。
            body: 请求体模板。
            source_system: 来源系统标识（如 "MES_LIGHT"）。
            connector: API 连接器（已连接）。
            page_size: 每页数量。
            max_pages: 最大页数。
            rq_job: RQ Job 对象。

        Returns:
            统计信息。
        """
        batch = self._create_batch(task_id, "manual")
        self._update_batch_status(batch, "running")
        self._update_progress(rq_job, 0, f"开始 API 拉取: {endpoint}")

        try:
            success_count = 0
            failed_count = 0
            page = 0

            for page_records in connector.fetch_all_pages(
                endpoint, method=method, body=body,
                page_size=page_size, max_pages=max_pages,
            ):
                page += 1
                if not isinstance(page_records, list):
                    page_records = [page_records]

                for record in page_records:
                    if not isinstance(record, dict):
                        failed_count += 1
                        continue
                    try:
                        self._insert_api_record(
                            batch_id=str(batch.id),
                            source_system=source_system,
                            source_object=endpoint,
                            api_url=endpoint,
                            request_params=json.dumps(body or {}),
                            payload=record,
                        )
                        success_count += 1
                    except Exception as e:
                        failed_count += 1
                        self._record_error(
                            batch_id=batch.id,
                            source_object=endpoint,
                            error_level="row",
                            error_type="api_insert_error",
                            error_message=str(e),
                            raw_value=str(record)[:500],
                        )

                self._db.commit()
                self._update_progress(
                    rq_job, -1,
                    f"API 拉取中: 第 {page} 页, 已入库 {success_count} 条"
                )

            total = success_count + failed_count
            batch.record_count = total
            batch.success_count = success_count
            batch.fail_count = failed_count
            batch.status = "success" if failed_count == 0 else "partial_success"
            batch.finished_at = _utcnow()
            self._db.commit()

            self._update_progress(rq_job, 100, "API 拉取完成")
            return {"total": total, "success": success_count, "failed": failed_count}

        except Exception as e:
            logger.exception("API 拉取失败: %s", e)
            batch.status = "failed"
            batch.error_summary = str(e)[:1000]
            batch.finished_at = _utcnow()
            self._db.commit()
            raise

    # ── 批次管理 ────────────────────────────

    def _create_batch(
        self, task_id: uuid.UUID, trigger_type: str
    ) -> IngestionBatch:
        """创建新的执行批次。"""
        batch = IngestionBatch(
            task_id=task_id,
            trigger_type=trigger_type,
            status="pending",
        )
        self._db.add(batch)
        self._db.commit()
        return batch

    def _update_batch_status(self, batch: IngestionBatch, status: str) -> None:
        """更新批次状态。"""
        batch.status = status
        if status == "running" and not batch.started_at:
            batch.started_at = _utcnow()
        self._db.commit()

    # ── Raw 层写入 ──────────────────────────

    def _ensure_raw_table(self, table_name: str, columns: list[ColumnInfo]) -> None:
        """确保 PostgreSQL Raw 物理表存在（不存在则创建）。"""
        # 检查表是否存在
        schema, tbl = self._parse_schema_table(table_name)
        check_sql = text(
            "SELECT EXISTS ("
            "  SELECT 1 FROM information_schema.tables "
            "  WHERE table_schema = :schema AND table_name = :table"
            ")"
        )
        result = self._db.execute(check_sql, {"schema": schema, "table": tbl})
        exists = result.scalar_one()

        if exists:
            return

        # 生成 DDL
        from app.modules.ingestion.connectors.sqlserver import SqlServerConnector

        col_defs = []
        for col in columns:
            pg_type = SqlServerConnector.TYPE_MAP.get(
                col.data_type.lower().split("(")[0].strip(), "TEXT"
            )
            nullable = "" if col.is_nullable else " NOT NULL"
            col_defs.append(f'    "{col.name}" {pg_type}{nullable}')

        tracking_cols = [
            '    "_batch_id"          VARCHAR(64)  NOT NULL',
            '    "_source_system"     VARCHAR(64)  NOT NULL',
            '    "_source_object"     VARCHAR(256) NOT NULL',
            '    "_source_row_hash"   VARCHAR(64)  NOT NULL',
            '    "_ingested_at"       TIMESTAMPTZ  NOT NULL DEFAULT NOW()',
            '    "_is_deleted"        BOOLEAN      NOT NULL DEFAULT FALSE',
        ]

        ddl = f'CREATE TABLE {table_name} (\n'
        ddl += ",\n".join(col_defs + tracking_cols)
        ddl += "\n)"

        self._db.execute(text(ddl))
        self._db.commit()
        logger.info("创建 Raw 表: %s (%d 列)", table_name, len(columns))

    def _insert_raw_row(self, table_name: str, record: dict[str, Any]) -> None:
        """向 Raw 物理表插入一行数据。"""
        # 过滤掉不在表结构中的字段（安全措施）
        columns = ", ".join(f'"{k}"' for k in record.keys())
        placeholders = ", ".join(f":{k}" for k in record.keys())
        sql = text(
            f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        )
        self._db.execute(sql, record)

    def _ensure_api_table(self, table_name: str) -> None:
        """确保 Raw API 分表存在（不存在则创建）。

        表结构固定：追踪字段 + payload JSONB + 去重唯一约束。
        """
        schema, tbl = self._parse_schema_table(table_name)
        check = text(
            "SELECT EXISTS (SELECT 1 FROM information_schema.tables "
            "WHERE table_schema = :s AND table_name = :t)"
        )
        result = self._db.execute(check, {"s": schema, "t": tbl})
        if result.scalar_one():
            return

        ddl = text(
            f"CREATE TABLE {table_name} ("
            "  _raw_id              BIGSERIAL PRIMARY KEY,"
            "  _batch_id            VARCHAR(64)  NOT NULL,"
            "  _source_system       VARCHAR(64)  NOT NULL,"
            "  _source_object       VARCHAR(256) NOT NULL,"
            "  _source_row_hash     VARCHAR(64)  NOT NULL,"
            "  _api_url             VARCHAR(512) NOT NULL,"
            "  _api_request_params  JSONB,"
            "  _api_response_at     TIMESTAMPTZ  NOT NULL DEFAULT NOW(),"
            "  _ingested_at         TIMESTAMPTZ  NOT NULL DEFAULT NOW(),"
            "  _is_deleted          BOOLEAN      NOT NULL DEFAULT FALSE,"
            "  payload              JSONB        NOT NULL"
            ")"
        )
        self._db.execute(ddl)

        idx = text(
            f"CREATE UNIQUE INDEX IF NOT EXISTS uq_{tbl}_dedup "
            f"ON {table_name} (_batch_id, _source_row_hash)"
        )
        self._db.execute(idx)
        self._db.commit()
        logger.info("Created API raw table: %s", table_name)

    def _insert_api_record(
        self,
        batch_id: str,
        source_system: str,
        source_object: str,
        api_url: str,
        request_params: str,
        payload: dict[str, Any],
    ) -> None:
        """向 raw.{system}_{source_object} 分表写入 API 响应数据。"""
        table_name = f"raw.{source_system.lower()}_{source_object}"
        self._ensure_api_table(table_name)

        sql = text(
            f"INSERT INTO {table_name} "
            "(_batch_id, _source_system, _source_object, _source_row_hash, "
            " _api_url, _api_request_params, _api_response_at, _ingested_at, payload) "
            "VALUES (:batch_id, :source_system, :source_object, :source_row_hash, "
            " :api_url, :api_request_params, :api_response_at, :ingested_at, :payload) "
            "ON CONFLICT (_batch_id, _source_row_hash) DO NOTHING"
        )
        self._db.execute(sql, {
            "batch_id": batch_id,
            "source_system": source_system,
            "source_object": source_object,
            "source_row_hash": self._compute_hash(payload),
            "api_url": api_url,
            "api_request_params": request_params,
            "api_response_at": _utcnow(),
            "ingested_at": _utcnow(),
            "payload": json.dumps(payload, ensure_ascii=False),
        })

    # ── 错误记录 ────────────────────────────

    def _record_error(
        self,
        batch_id: uuid.UUID,
        source_object: str,
        error_level: str,
        error_type: str,
        error_message: str,
        raw_value: str = "",
    ) -> None:
        """记录同步错误明细。"""
        error = ImportError(
            batch_id=batch_id,
            error_level=error_level,
            error_type=error_type,
            error_message=error_message[:2000],
            raw_value=raw_value[:2000],
            field_name=source_object if error_level == "field" else None,
        )
        self._db.add(error)

    # ── 工具方法 ────────────────────────────

    @staticmethod
    def _choose_batch_size(total: int) -> int:
        """根据数据量选择合适的批次大小。"""
        if total < 100_000:
            return 10_000
        elif total < 1_000_000:
            return 20_000
        else:
            return 50_000

    @staticmethod
    def _compute_hash(data: dict[str, Any]) -> str:
        """计算数据字典的 SHA-256 hash。"""
        serialized = json.dumps(data, sort_keys=True, ensure_ascii=False, default=str)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()[:16]

    @staticmethod
    def _parse_schema_table(full_name: str) -> tuple[str, str]:
        """解析 schema.table 格式。"""
        parts = full_name.split(".", 1)
        if len(parts) == 2:
            return parts[0], parts[1]
        return "raw", parts[0]

    @staticmethod
    def _update_progress(rq_job, progress: int, step: str) -> None:
        """更新 RQ 任务进度。"""
        if rq_job:
            rq_job.meta["progress"] = progress
            rq_job.meta["step"] = step
            rq_job.save_meta()
