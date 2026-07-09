"""令牌桶限流器 — 控制 API 请求频率。

对应策略文档：03-API拉取同步策略 §4。
"""

import threading
import time


class TokenBucket:
    """简单的令牌桶限流器，线程安全。

    使用示例::

        limiter = TokenBucket(rate=10)  # 10 QPS
        for i in range(100):
            limiter.acquire()           # 必要时阻塞等待
            send_request()
    """

    def __init__(self, rate: int):
        """初始化令牌桶。

        Args:
            rate: 每秒允许的请求数（QPS）。
        """
        if rate <= 0:
            raise ValueError("rate 必须大于 0")
        self.rate = rate
        self._tokens = float(rate)
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self) -> None:
        """获取一个令牌，必要时阻塞等待直到令牌可用。"""
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_refill
            self._tokens = min(self.rate, self._tokens + elapsed * self.rate)
            self._last_refill = now

            if self._tokens < 1.0:
                wait = (1.0 - self._tokens) / self.rate
                # 释放锁后等待，避免阻塞其他线程
                pass
            else:
                self._tokens -= 1.0
                return

        # 在锁外等待
        time.sleep(wait)
        with self._lock:
            self._tokens -= 1.0

    @property
    def available(self) -> float:
        """当前可用令牌数（仅用于监控，非精确值）。"""
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_refill
            tokens = min(self.rate, self._tokens + elapsed * self.rate)
            return tokens
