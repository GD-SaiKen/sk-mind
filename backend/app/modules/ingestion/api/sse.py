"""SSE 实时进度流 — 通过 Redis pub/sub 推送批次同步进度。"""

import asyncio
import json
import uuid

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.core.queue import redis_conn

sse_router = APIRouter()


@sse_router.get("/batches/{batch_id}/stream")
async def stream_batch_progress(batch_id: uuid.UUID):
    """订阅 Redis pub/sub channel `batch:{batch_id}:progress`，推送 SSE 事件。

    Worker 端在 sync_tasks.py 中每阶段 publish 进度到该 channel。
    前端用 EventSource 连接，无需轮询。
    """
    channel = f"batch:{batch_id}:progress"
    pubsub = redis_conn.pubsub()
    pubsub.subscribe(channel)

    async def event_stream():
        try:
            for msg in pubsub.listen():
                if msg["type"] != "message":
                    continue
                data = json.loads(msg["data"])
                yield f"data: {json.dumps(data)}\n\n"
                if data.get("status") in ("success", "failed"):
                    break
        except asyncio.CancelledError:
            pass
        finally:
            pubsub.unsubscribe(channel)
            pubsub.close()

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
