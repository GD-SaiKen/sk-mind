"""APScheduler 定时同步调度器 — 在 FastAPI 生命周期中启动。"""

import logging
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.database import async_session_factory
from app.modules.ingestion import dao
from app.modules.ingestion.models import IngestionBatch

logger = logging.getLogger("sk-mind.scheduler")

scheduler = AsyncIOScheduler()


def _build_batch(task, trigger_type: str) -> IngestionBatch:
    return IngestionBatch(
        task_id=task.id,
        trigger_type=trigger_type,
        status="pending",
        triggered_by="scheduler",
    )


async def _trigger_task(task, trigger_type: str):
    """触发单个任务的同步执行。"""
    async with async_session_factory() as db:
        try:
            batch = _build_batch(task, trigger_type)
            await dao.batch_insert(db, batch)

            from app.core.queue import redis_conn
            from rq import Queue
            queue = Queue("ingestion", connection=redis_conn)
            job = queue.enqueue(
                "app.modules.ingestion.tasks.sync_tasks.run_echo_sync",
                str(task.id), str(batch.id),
                f"{task.name} (scheduled {datetime.now(timezone.utc).strftime('%m-%d %H:%M')})",
                job_timeout=600,
            )
            batch.status = "running"
            batch.started_at = datetime.now(timezone.utc)
            await dao.batch_update(db, batch)

            # 更新 last_sync_at
            await dao.task_update_sync_status(db, task, "running")

            logger.info(
                "定时同步已触发: task=%s batch=%s job=%s",
                task.name, str(batch.id)[:12], job.id,
            )
        except Exception:
            logger.exception("定时同步触发失败: task=%s", task.name)


async def _run_scheduled_tasks():
    """遍历所有 cron 任务，触发到时间的同步。"""
    async with async_session_factory() as db:
        tasks, _ = await dao.task_list(db, status="active")
        for task in tasks:
            if task.schedule_type == "cron" and task.cron_expression:
                await _trigger_task(task, "scheduled")


def start_scheduler():
    """启动 APScheduler — 在 FastAPI lifespan startup 中调用。"""
    # 每分钟检查一次是否有 cron 任务需要触发
    scheduler.add_job(
        _run_scheduled_tasks,
        trigger="interval",
        minutes=1,
        id="sync_scheduler_check",
        replace_existing=True,
    )
    scheduler.start()
    logger.info("同步调度器已启动（每分钟检查）")


def shutdown_scheduler():
    """停止 APScheduler。"""
    scheduler.shutdown(wait=False)
    logger.info("同步调度器已停止")
