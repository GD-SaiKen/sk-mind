"""开发服务器入口 — 在 IDE 中右键 ▶ Run 即可启动 FastAPI 开发服务器。

使用方式:
    python backend/run_dev.py          # 从项目根目录运行
    或在 IDEA/PyCharm 中直接点击 ▶ 运行
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,          # 热重载，改代码自动重启
        log_level="info",
    )
