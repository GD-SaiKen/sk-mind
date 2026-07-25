"""APScheduler 定时同步调度器 — 为每个 cron 任务注册独立 Job。

调度器只负责「到点把同步任务入 RQ 队列」，真实执行仍走 RQ Worker
（``run_api_full_sync`` / ``run_sync_task``），与前端手动点按钮触发的派发逻辑
完全一致（见 ``app.modules.ingestion.router.execute_task``）。

> ⚠️ 历史坑：早期实现里 `_trigger_task` 入队的是 `run_echo_sync`（一个造随机数的
> mock stub），导致定时同步「看起来在跑、实际从没真同步」，水位一直不更新。
> 现已改为复用 router 的 `_enqueue_api_sync` / `_enqueue`，与手动触发同口径。
"""

import logging
import uuid
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.database import async_session_factory
from app.modules.ingestion import dao
from app.modules.ingestion.models import IngestionBatch

logger = logging.getLogger("sk-mind.scheduler")

scheduler = AsyncIOScheduler()


def _normalize_cron(expr: str) -> str:
    """把 Quartz 风格（6/7 字段，含「秒」与 ``?``）的 cron 表达式归一为
    APScheduler ``CronTrigger.from_crontab`` 接受的 5 字段标准格式
    （分 时 日 月 周）。

    - 6 字段视为 ``秒 分 时 日 月 周``：丢弃「秒」，保留后 5 字段。
    - 7 字段视为 ``秒 分 时 日 月 周 年``：丢弃「秒」和「年」。
    - 字段中的 ``?`` 视为 ``*``（Quartz 的「不指定」占位符）。
    """
    parts = expr.strip().split()
    if len(parts) == 6:
        parts = parts[1:]        # 丢弃「秒」
    elif len(parts) == 7:
        parts = parts[1:-1]      # 丢弃「秒」和「年」
    parts = [("*" if p == "?" else p) for p in parts]
    return " ".join(parts)


async def _trigger_task(task_id: str, task_name: str):
    """触发单个任务的同步执行 —— 与 ``router.execute_task`` 的派发逻辑保持一致。

    调度器只创建 batch 并入队，真实同步在 RQ Worker 中执行，不阻塞调度循环，
    也不会和正在跑的同步冲突。
    """
    # 懒加载，避免与 router 形成导入环
    from app.modules.ingestion.router import _enqueue, _enqueue_api_sync

    async with async_session_factory() as db:
        try:
            task = await dao.task_get_by_id(db, uuid.UUID(task_id))
            if not task or task.status != "active":
                return

            batch = IngestionBatch(
                task_id=task.id,
                trigger_type="scheduled",
                status="running",
                started_at=datetime.now(timezone.utc),
                triggered_by="scheduler",
            )
            await dao.batch_insert(db, batch)
            await db.commit()  # 先提交，确保 Worker 入队后能立即看到 batch

            _cfg = (task.config or {})
            access_method = _cfg.get("accessMethod") or _cfg.get("access_method") or ""
            if access_method in ("api", "api_pull"):
                config_path = _cfg.get("configPath") or _cfg.get("config_path") or ""
                interfaces = _cfg.get("interfaces")
                # 真实同步引擎（ApiSyncEngine）—— 与手动触发完全一致
                job_id = _enqueue_api_sync(
                    task.id, batch.id, config_path, interfaces,
                    data_source_id=task.data_source_id,
                )
            else:
                # 非 API 任务：沿用 router 的默认派发（legacy / v2 入口）
                job_id = _enqueue(task.id, batch.id, task_name)

            logger.info(
                "定时同步已入队: task=%s batch=%s job=%s",
                task_name, str(batch.id)[:12], job_id,
            )
        except Exception:
            logger.exception("定时同步触发失败: task=%s", task_name)


async def _load_and_schedule():
    """从 DB 加载所有 cron 任务，注册到 APScheduler（并注销已删除/禁用的）。"""
    async with async_session_factory() as db:
        tasks, _ = await dao.task_list(db, status="active")
        registered = set()
        for task in tasks:
            if task.schedule_type == "cron" and task.cron_expression:
                job_id = f"cron_{task.id}"
                try:
                    trigger = CronTrigger.from_crontab(_normalize_cron(task.cron_expression))
                    scheduler.add_job(
                        _trigger_task,
                        trigger=trigger,
                        args=[str(task.id), task.name],
                        id=job_id,
                        replace_existing=True,
                    )
                    registered.add(job_id)
                    logger.info("已注册定时任务: %s cron=%s", task.name, task.cron_expression)
                except Exception:
                    logger.warning(
                        "无法解析 cron: task=%s expr=%s", task.name, task.cron_expression
                    )

        # 注销 DB 中已不存在 / 已禁用的 cron job
        for job in scheduler.get_jobs():
            if job.id.startswith("cron_") and job.id not in registered:
                scheduler.remove_job(job.id)


def start_scheduler():
    """启动 APScheduler — 每个 cron 任务独立 Job，精确按表达式触发。

    - 启动后立即加载一次（不用等第一个轮询周期）
    - 每 60 秒从 DB 重新同步（检测新增/修改/删除的 cron 任务）
    """
    scheduler.add_job(
        _load_and_schedule,
        trigger="date",
        run_date=datetime.now(timezone.utc),
        id="sync_reload_once",
    )
    scheduler.add_job(
        _load_and_schedule,
        trigger="interval",
        seconds=60,
        id="sync_reload",
        replace_existing=True,
    )
    scheduler.start()
    logger.info("同步调度器已启动")


def shutdown_scheduler():
    """停止 APScheduler。"""
    scheduler.shutdown(wait=False)
    logger.info("同步调度器已停止")
