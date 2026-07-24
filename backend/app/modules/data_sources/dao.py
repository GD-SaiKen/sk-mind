"""DataSource 模块数据访问层。"""

import json
import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.data_sources.models import ConnectorConfig, DataSource


async def _enrich_with_task_info(
    db: AsyncSession,
    ds: DataSource,
    ds_id: uuid.UUID,
) -> None:
    """填充数据源的 task_count 和 last_sync_at 计算字段。"""
    # 统计关联的接入任务数
    task_count_sql = text(
        "SELECT count(*) FROM ingestion_tasks WHERE data_source_id = :ds_id AND status != 'disabled'"
    )
    count_result = await db.execute(task_count_sql, {"ds_id": ds_id})
    ds.task_count = count_result.scalar_one()  # type: ignore[attr-defined]

    # 获取最近一次同步时间
    sync_sql = text(
        "SELECT last_sync_at FROM ingestion_tasks WHERE data_source_id = :ds_id ORDER BY last_sync_at DESC NULLS LAST LIMIT 1"
    )
    sync_result = await db.execute(sync_sql, {"ds_id": ds_id})
    row = sync_result.fetchone()
    ds.last_sync_at = row[0] if row and row[0] else None  # type: ignore[attr-defined]

    # 预置连接配置占位（详情页由 _attach_connection_config 覆写为真实值，
    # 列表保持 None 避免逐条查询；确保响应序列化时属性一定存在）
    ds.connection_config = None  # type: ignore[attr-defined]


async def list_all(
    db: AsyncSession,
    keyword: str | None = None,
    source_type: str | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[DataSource], int]:
    query = select(DataSource)
    if keyword:
        query = query.filter(DataSource.name.ilike(f"%{keyword}%"))
    if source_type:
        query = query.filter(DataSource.source_type == source_type)
    if status:
        query = query.filter(DataSource.status == status)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(DataSource.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    items = list(result.scalars().all())

    # 批量填充 task_count 和 last_sync_at
    for ds in items:
        await _enrich_with_task_info(db, ds, ds.id)
    return items, total


async def get_by_id(db: AsyncSession, ds_id: uuid.UUID) -> DataSource | None:
    ds = await db.get(DataSource, ds_id)
    if ds is not None:
        await _enrich_with_task_info(db, ds, ds_id)
    return ds


async def insert(db: AsyncSession, ds: DataSource) -> DataSource:
    db.add(ds)
    await db.flush()
    return ds


async def update(db: AsyncSession, ds: DataSource) -> DataSource:
    await db.flush()
    return ds


# ── 连接配置（ConnectorConfig） ──────────────────────────────

async def upsert_connection_config(
    db: AsyncSession,
    ds_id: uuid.UUID,
    config_type: str,
    extra_config: dict,
    credential_ref: Optional[str] = None,
) -> ConnectorConfig:
    """新建或更新某数据源的连接配置（同 config_type 单条）。

    Args:
        ds_id: 数据源 ID。
        config_type: 连接类型，如 api_config / db_connection。
        extra_config: 配置字典，序列化为 JSON 存入 extra_config 列。
        credential_ref: 凭据引用（后续迁移到加密存储）。

    Returns:
        ConnectorConfig ORM 实例。
    """
    stmt = select(ConnectorConfig).where(
        ConnectorConfig.data_source_id == ds_id,
        ConnectorConfig.config_type == config_type,
    )
    result = await db.execute(stmt)
    cfg = result.scalar_one_or_none()

    payload = json.dumps(extra_config, ensure_ascii=False)

    if cfg is None:
        cfg = ConnectorConfig(
            data_source_id=ds_id,
            config_type=config_type,
            extra_config=payload,
            credential_ref=credential_ref,
        )
        db.add(cfg)
    else:
        cfg.extra_config = payload
        if credential_ref is not None:
            cfg.credential_ref = credential_ref
    await db.flush()
    return cfg


async def get_connection_config(
    db: AsyncSession,
    ds_id: uuid.UUID,
) -> Optional[ConnectorConfig]:
    """读取某数据源的连接配置。"""
    stmt = select(ConnectorConfig).where(
        ConnectorConfig.data_source_id == ds_id
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()
