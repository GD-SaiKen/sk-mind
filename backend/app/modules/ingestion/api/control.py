"""批次控制端点 — 取消运行中的同步 + 回退已写入的 Raw 数据。"""

import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.queue import redis_conn
from app.modules.auth.models import User
from app.modules.ingestion import dao

logger = logging.getLogger(__name__)

control_router = APIRouter()


def _find_rq_job_for_batch(batch_id: uuid.UUID):
    """在 ingestion 队列（queued/started/failed）中找到与 batch 对应的 RQ job。

    RQ job 入队参数固定为 (task_id, batch_id, ...)，故比对 args[1] 即可定位。
    """
    from rq import Queue
    from rq.job import Job
    from rq.registry import StartedJobRegistry, FailedJobRegistry

    q = Queue("ingestion", connection=redis_conn)
    candidate_ids = set(q.get_job_ids())
    try:
        candidate_ids |= set(StartedJobRegistry(queue=q).get_job_ids())
        candidate_ids |= set(FailedJobRegistry(queue=q).get_job_ids())
    except Exception:
        pass
    target = str(batch_id)
    for jid in candidate_ids:
        try:
            job = Job.fetch(jid, connection=redis_conn)
        except Exception:
            continue
        args = job.args or []
        if len(args) >= 2 and str(args[1]) == target:
            return job
    return None


@control_router.post("/batches/{batch_id}/cancel")
async def cancel_batch(
    batch_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """取消运行中的同步批次。

    双保险终止：
    1) 发布 Redis pub/sub cancel 信号 —— 运行中的 Worker 在页/分片安全点轮询到后
       立即中止（真正的「运行中止」，而非只改 DB）。
    2) 通过 RQ ``send_stop_job_command`` 给对应 job 置停止标志 —— Worker 完成当前
       任务后不再领取下一个排队 job，防止取消后又被积压任务顶上。
    """
    batch = await dao.batch_get_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="批次不存在")
    if batch.status not in ("running", "pending"):
        raise HTTPException(status_code=400, detail=f"批次状态为 {batch.status}，无法取消")

    # 1. 发布取消信号到 Redis（Worker 监听此 channel 自行终止）
    redis_conn.publish(f"batch:{batch_id}:control", "cancel")

    # 2. 给 RQ job 发停止命令（真正撤销 job，而非只改 DB）
    try:
        from rq.command import send_stop_job_command
        job = _find_rq_job_for_batch(batch_id)
        if job is not None:
            send_stop_job_command(redis_conn, job.id)
            logger.info("已发送 RQ stop 命令 job=%s batch=%s", job.id[:8], batch_id)
        else:
            logger.info("未找到 batch %s 对应的 RQ job（可能已完成或尚未入队）", batch_id)
    except Exception:
        logger.warning("发送 RQ stop 命令失败（不影响 pub/sub 取消）", exc_info=True)

    # 3. 标记批次为 cancelled（即时 UI 反馈）
    batch.status = "cancelled"
    from datetime import datetime, timezone
    batch.finished_at = datetime.now(timezone.utc)
    batch.error_summary = f"由 {current_user.username} 手动取消"
    await dao.batch_update(db, batch)

    # 4. 发布 SSE 终止事件
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
