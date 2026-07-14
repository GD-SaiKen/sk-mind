"""RQ Worker 启动入口 — 监听 ingestion 队列执行同步任务。

用法：python -m app.workers
"""
import logging

from redis import Redis
from rq import SimpleWorker, Queue

from app.core.config import settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s %(message)s")
logger = logging.getLogger("sk-mind.worker")

if __name__ == "__main__":
    redis_conn = Redis.from_url(settings.REDIS_URL)
    queues = [Queue("ingestion", connection=redis_conn)]
    worker = SimpleWorker(queues, connection=redis_conn)
    logger.info("Worker started (SimpleWorker), listening on queue 'ingestion'")
    worker.work()
