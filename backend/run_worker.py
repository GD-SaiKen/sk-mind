"""一键启动 RQ Worker（消费同步任务队列）。"""

if __name__ == "__main__":
    import logging, sys
    from redis import Redis
    from rq import SimpleWorker, Queue
    from app.core.config import settings
    from app.core.logging import ColoredFormatter

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColoredFormatter())
    logging.getLogger().handlers = [handler]
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("rq").setLevel(logging.WARNING)

    redis_conn = Redis.from_url(settings.REDIS_URL)
    queues = [Queue("ingestion", connection=redis_conn)]
    worker = SimpleWorker(queues, connection=redis_conn)
    worker.work()
