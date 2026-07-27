"""run_scheduler.py — 启动 APScheduler 定时同步调度器（独立进程）。

与 run_worker.py / run_api.py 同级，git 跟踪。
调度器只负责把 cron 任务入 RQ 队列，真实同步由 RQ Worker 执行
（run_api_full_sync / run_sync_task），与前端手动点按钮触发的派发逻辑完全一致。

启动：
    cd backend && ../.venv/Scripts/python.exe run_scheduler.py
"""

import asyncio
import logging
import os
import signal
from pathlib import Path

# 加载 .env（同步引擎连接器需要 env 中的 DB / API 配置）
_env_path = Path(__file__).resolve().parents[0] / ".env"
if _env_path.exists():
    try:
        from dotenv import load_dotenv

        load_dotenv(_env_path)
    except ImportError:
        pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s",
)
logger = logging.getLogger("sk-mind.run_scheduler")

from app.modules.ingestion.scheduler import start_scheduler, shutdown_scheduler  # noqa: E402


async def main() -> None:
    logger.info("启动同步调度器进程 ...")
    start_scheduler()
    logger.info("调度器运行中（Ctrl+C 退出）")

    loop = asyncio.get_event_loop()
    stop = asyncio.Event()

    def _request_stop(*_):
        logger.info("收到退出信号，停止调度器")
        stop.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, _request_stop)
        except (NotImplementedError, RuntimeError, ValueError):
            try:
                signal.signal(sig, _request_stop)
            except (ValueError, OSError):
                pass

    try:
        await stop.wait()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        shutdown_scheduler()
        logger.info("调度器进程已退出")


if __name__ == "__main__":
    asyncio.run(main())
