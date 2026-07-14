"""结构化 + 彩色日志配置。生产用 JSON，开发用彩色。"""

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any


# ANSI 颜色码
_RESET = "\033[0m"
_COLORS = {
    logging.DEBUG:    "\033[36m",   # cyan
    logging.INFO:     "",           # default (white)
    logging.WARNING:  "\033[33m",   # yellow
    logging.ERROR:    "\033[31m",   # red
    logging.CRITICAL: "\033[1;31m", # bold red
}


class JSONFormatter(logging.Formatter):
    """生产环境：单行 JSON。"""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info and record.exc_info[1]:
            payload["exception"] = str(record.exc_info[1])
        return json.dumps(payload, ensure_ascii=False, default=str)


class ColoredFormatter(logging.Formatter):
    """开发环境：彩色控制台输出。"""

    def format(self, record: logging.LogRecord) -> str:
        color = _COLORS.get(record.levelno, "")
        ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
        msg = f"{color}{record.levelname:<7}{_RESET} {ts}  {record.getMessage()}"
        if record.exc_info and record.exc_info[1]:
            msg += f"\n{_COLORS[logging.ERROR]}{record.exc_info[1]}{_RESET}"
        return msg


def setup_logging(level: str = "INFO", dev: bool = True) -> None:
    """初始化日志。dev=True 用彩色输出，False 用 JSON。"""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColoredFormatter() if dev else JSONFormatter())

    root = logging.getLogger()
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    root.handlers.clear()
    root.addHandler(handler)

    # 静默第三方库
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("redis").setLevel(logging.WARNING)
    logging.getLogger("apscheduler").setLevel(logging.WARNING)
    logging.getLogger("rq").setLevel(logging.WARNING)
