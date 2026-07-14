"""批次控制端点 — 取消运行中的同步 + 回退已写入的 Raw 数据。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.queue import redis_conn
from app.modules.auth.models import User
from app.modules.ingestion import dao

control_router = APIRouter()


@control_router.post("/batches/{batch_id}/cancel")
async def cancel_batch(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """取消运行中的同步批次。发送 Redis pub/sub cancelled 信号，Worker 检测后终止。"""
    batch = await dao.batch_get_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="批次不存在")
    if batch.status not in ("running", "pending"):
        raise HTTPException(status_code=400, detail=f"批次状态为 {batch.status}，无法取消")

    # 1. 发布取消信号到 Redis（Worker 监听此 channel 自行终止）
    redis_conn.publish(f"batch:{batch_id}:control", "cancel")

    # 2. 标记批次为 cancelled
    batch.status = "cancelled"
    from datetime import datetime, timezone
    batch.finished_at = datetime.now(timezone.utc)
    batch.error_summary = f"由 {current_user.username} 手动取消"
    await dao.batch_update(db, batch)

    # 3. 发布 SSE 终止事件
    import json
    redis_conn.publish(
        f"batch:{batch_id}:progress",
        json.dumps({"pct": 0, "step": "已取消", "status": "cancelled"}),
    )

    return {"code": 0, "msg": "已发送取消信号", "data": {"batchId": str(batch_id)}}


@control_router.post("/batches/{batch_id}/rollback")
async def rollback_batch(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """回退批次写入的 Raw 层数据。按 _batch_id 删除所有 raw schema 表中的该批次数据。"""
    batch = await dao.batch_get_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="批次不存在")

    # 查 raw schema 下所有包含 _batch_id 列的表
    tables_result = await db.execute(text(
        "SELECT table_name FROM information_schema.columns"
        " WHERE table_schema = 'raw' AND column_name = '_batch_id'"
    ))
    raw_tables = [r[0] for r in tables_result.fetchall()]

    deleted_total = 0
    bid = str(batch_id)
    for tbl in raw_tables:
        result = await db.execute(
            text(f"DELETE FROM raw.{tbl} WHERE _batch_id = :bid"),
            {"bid": bid},
        )
        deleted_total += result.rowcount

    await db.commit()

    # 更新批次备注
    batch.error_summary = f"已回退 {deleted_total} 行"
    await dao.batch_update(db, batch)

    return {
        "code": 0,
        "msg": f"已回退 {deleted_total} 行数据（{len(raw_tables)} 张表）",
        "data": {"batchId": bid, "deletedRows": deleted_total, "tablesScanned": len(raw_tables)},
    }
