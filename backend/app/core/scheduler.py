"""APScheduler 定时同步调度器 — 为每个 cron 任务注册独立 Job。"""

import logging
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.database import async_session_factory
from app.modules.ingestion import dao
from app.modules.ingestion.models import IngestionBatch

logger = logging.getLogger("sk-mind.scheduler")

scheduler = AsyncIOScheduler()


async def _trigger_task(task_id: str, task_name: str):
    """触发单个任务的同步执行。"""
    import uuid

    async with async_session_factory() as db:
        try:
            task = await dao.task_get_by_id(db, uuid.UUID(task_id))
            if not task or task.status != "active":
                return

            batch = IngestionBatch(
                task_id=task.id,
                trigger_type="scheduled",
                status="pending",
                triggered_by="scheduler",
            )
            await dao.batch_insert(db, batch)

            from app.core.queue import redis_conn
            from rq import Queue
            queue = Queue("ingestion", connection=redis_conn)
            job = queue.enqueue(
                "app.modules.ingestion.tasks.sync_tasks.run_echo_sync",
                str(task.id), str(batch.id),
                f"{task_name} (scheduled {datetime.now(timezone.utc).strftime('%m-%d %H:%M')})",
                job_timeout=600,
            )
            batch.status = "running"
            batch.started_at = datetime.now(timezone.utc)
            await dao.batch_update(db, batch)
            await dao.task_update_sync_status(db, task, "running")

            logger.info("定时同步: task=%s batch=%s job=%s", task_name, str(batch.id)[:12], job.id)
        except Exception:
            logger.exception("定时同步触发失败: task=%s", task_name)


async def _load_and_schedule():
    """从 DB 加载所有 cron 任务，注册到 APScheduler。"""
    async with async_session_factory() as db:
        tasks, _ = await dao.task_list(db, status="active")
        for task in tasks:
            if task.schedule_type == "cron" and task.cron_expression:
                try:
                    trigger = CronTrigger.from_crontab(task.cron_expression)
                    scheduler.add_job(
                        _trigger_task,
                        trigger=trigger,
                        args=[str(task.id), task.name],
                        id=f"cron_{task.id}",
                        replace_existing=True,
                    )
                    logger.info("已注册定时任务: %s cron=%s", task.name, task.cron_expression)
                except Exception:
                    logger.warning("无法解析 cron: task=%s expr=%s", task.name, task.cron_expression)


def start_scheduler():
    """启动 APScheduler — 每个 cron 任务独立 Job，精确按表达式触发。"""
    scheduler.add_job(
        _load_and_schedule,
        trigger="interval",
        minutes=5,
        id="sync_reload",
        replace_existing=True,
    )
    scheduler.start()
    logger.info("同步调度器已启动")


def shutdown_scheduler():
    """停止 APScheduler。"""
    scheduler.shutdown(wait=False)
    logger.info("同步调度器已停止")
