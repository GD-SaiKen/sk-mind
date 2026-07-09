"""RQ 任务队列配置。"""

from redis import Redis

from app.core.config import settings

redis_conn = Redis.from_url(
    settings.REDIS_URL,
    decode_responses=False,
)
