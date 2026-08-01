PY = ../.venv/Scripts/python.exe
REQ = requirements.txt

.PHONY: help dev worker scheduler install

help:
	@echo "sk-mind backend tasks:"
	@echo "  make dev       启动 API (uvicorn --reload, :8000)"
	@echo "  make worker    启动 RQ Worker (Windows SimpleWorker)"
	@echo "  make scheduler 启动定时调度器"
	@echo "  make install   安装依赖"

dev:
	$(PY) run_api.py

worker:
	PYTHONPATH=. $(PY) run_worker.py

scheduler:
	$(PY) run_scheduler.py

install:
	$(PY) -m pip install -r $(REQ)
