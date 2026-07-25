"""一键启动 RQ Worker（消费同步任务队列）。

启动时会自动清理环境，确保「只有 1 个 worker、加载最新代码」：
  1. 杀掉其他真正在跑的 run_worker.py 进程（精确匹配 python 进程 + 脚本路径，
     且绝不杀自己 / 祖先进程（如 WebStorm 启动器），避免误杀导致退出码 15）
  2. 清掉 Redis 中残留的 worker 注册（避免幽灵 worker 抢活）+ failed 队列
  3. 清空 __pycache__（确保从最新源码重新编译）
  4. Redis 单例锁：若已有其他实例且未退出，发「请退出」信号并等待；
     仍占用则本次优雅退出（不崩溃）
然后以 SimpleWorker 监听 ingestion 队列。直接重启本文件即可。

启动日志同时写入 backend/run_worker.log，便于排查。
"""

if __name__ == "__main__":
    import os
    import sys
    import time
    import socket
    import shutil
    import logging
    import threading

    _SELF_PID = os.getpid()
    _BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
    _SCRIPT_NAME = os.path.basename(__file__)  # run_worker.py

    # ── 日志：stdout + 文件 ──
    _log = logging.getLogger("run_worker")
    _log.setLevel(logging.INFO)
    _fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    _sh = logging.StreamHandler(sys.stdout)
    _sh.setFormatter(_fmt)
    _log.addHandler(_sh)
    try:
        _fh = logging.FileHandler(os.path.join(_BACKEND_DIR, "run_worker.log"), encoding="utf-8")
        _fh.setFormatter(_fmt)
        _log.addHandler(_fh)
    except Exception:
        pass

    LOCK_KEY = "skmind:worker:lock"
    DIE_KEY = "skmind:worker:please_die"

    def _token() -> str:
        return f"{_SELF_PID}@{socket.gethostname()}|{time.time()}"

    def _ancestor_pids() -> set:
        """收集自己及其所有祖先进程 pid，清理时绝不杀这些。"""
        anc = set()
        try:
            import psutil

            p = psutil.Process(_SELF_PID)
            while p is not None:
                anc.add(p.pid)
                try:
                    p = p.parent()
                except Exception:
                    p = None
        except Exception:
            anc.add(_SELF_PID)
        return anc

    def _kill_other_workers():
        """只杀真正的 python 进程且脚本参数精确等于本文件，且不杀祖先。"""
        try:
            import psutil
        except Exception as _e:
            _log.warning("psutil 不可用，跳过进程级清理：%s", _e)
            return

        ancestors = _ancestor_pids()
        killed = []
        for p in psutil.process_iter(["pid", "cmdline", "exe"]):
            pid = p.pid
            if pid in ancestors:  # 绝不杀自己 / 祖先（WebStorm 启动器等）
                continue
            _cmd = p.info.get("cmdline") or []
            _exe = (p.info.get("exe") or "").lower().replace("\\", "/")
            if "python" not in _exe:  # 只针对 python 进程
                continue
            # 精确匹配：任一参数为本文件（run_worker.py）
            if any(
                c and c.replace("\\", "/").rstrip("/").endswith(_SCRIPT_NAME)
                for c in _cmd
            ):
                try:
                    p.kill()
                    killed.append(pid)
                except Exception:
                    pass
        if killed:
            _log.info("已杀掉其他 worker 进程: %s", killed)
        else:
            _log.info("未发现其他 worker 进程（无需杀）")

    def _clear_pycache():
        try:
            for _root, _dirs, _files in os.walk(_BACKEND_DIR):
                if "__pycache__" in _dirs:
                    shutil.rmtree(
                        os.path.join(_root, "__pycache__"), ignore_errors=True
                    )
            _log.info("已清理 __pycache__")
        except Exception as _e:
            _log.warning("清 __pycache__ 失败（不影响启动）: %s", _e)

    def _clear_redis_regs(r):
        try:
            from rq import Worker, Queue

            for _w in Worker.all(connection=r):
                try:
                    _w.register_death()
                except Exception:
                    pass
            try:
                Queue("failed", connection=r).empty()
            except Exception:
                pass
            _log.info("已清理 Redis 残留 worker 注册 / failed 队列")
        except Exception as _e:
            _log.warning("清 Redis 残留失败（不影响启动）: %s", _e)

    def _acquire_lock(r, token, ttl=7200, stale_after=600):
        val = r.get(LOCK_KEY)
        if not val:
            return bool(r.set(LOCK_KEY, token, nx=True, ex=ttl))
        s = val.decode(errors="ignore")
        try:
            ts = float(s.split("|")[-1])
        except Exception:
            ts = 0.0
        # 锁主人超过 stale_after 秒未刷新 → 视为陈旧，强制接管
        if time.time() - ts > stale_after:
            return bool(r.set(LOCK_KEY, token, xx=True, ex=ttl))
        return False

    stop_evt = threading.Event()

    def _heartbeat(r, token, ttl=7200):
        while not stop_evt.is_set():
            try:
                r.set(LOCK_KEY, token, xx=True, ex=ttl)
            except Exception:
                pass
            stop_evt.wait(60)

    def _watch_die(worker, r):
        """后台监听「请退出」信号：新实例启动后会置位 DIE_KEY，
        本实例（新代码）检测到后优雅退出，实现无缝重启。"""
        for _ in range(30):  # 最多等 ~60s
            if stop_evt.is_set():
                return
            try:
                if r.get(DIE_KEY):
                    _log.info("收到退出信号 (please_die)，正在优雅退出…")
                    if hasattr(worker, "should_exit"):
                        worker.should_exit = True
                    return
            except Exception:
                pass
            time.sleep(2)

    try:
        # ── 1. 杀掉其他真正的 worker 进程（安全匹配）──
        _kill_other_workers()
        time.sleep(1)

        # ── 2. 清 __pycache__ ──
        _clear_pycache()

        # ── 3. 导入依赖 + 清 Redis 残留 ──
        from redis import Redis
        from rq import SimpleWorker, Queue
        from app.core.config import settings
        from app.core.logging import ColoredFormatter

        _r = Redis.from_url(settings.REDIS_URL)
        _clear_redis_regs(_r)

        token = _token()
        # 若已有其他实例，请其优雅退出
        if _r.exists(LOCK_KEY):
            _r.set(DIE_KEY, "1", ex=60)

        acquired = False
        for _ in range(20):  # 最多等 ~10s 让旧实例退出
            if _acquire_lock(_r, token):
                acquired = True
                break
            time.sleep(0.5)

        if not acquired:
            _log.warning(
                "已有其他 worker 实例在运行且未退出，本次启动退出以避免重复消费。"
                "请先在 WebStorm 停止旧实例，或运行 backend/scripts/restart_worker.ps1。"
            )
            sys.exit(0)

        # ── 4. 启动单个 Worker ──
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(ColoredFormatter())
        logging.getLogger().handlers = [handler]
        logging.getLogger().setLevel(logging.INFO)
        logging.getLogger("rq").setLevel(logging.WARNING)

        redis_conn = Redis.from_url(settings.REDIS_URL)
        queues = [Queue("ingestion", connection=redis_conn)]
        worker = SimpleWorker(queues, connection=redis_conn)
        _log.info("启动单个 SimpleWorker，监听队列: ingestion (pid=%s)", _SELF_PID)

        # 心跳保活锁 + 监听退出信号
        threading.Thread(
            target=_heartbeat, args=(_r, token), daemon=True
        ).start()
        threading.Thread(target=_watch_die, args=(worker, _r), daemon=True).start()

        try:
            worker.work()
        finally:
            stop_evt.set()
            try:
                _r.delete(LOCK_KEY)
            except Exception:
                pass
            try:
                _r.delete(DIE_KEY)
            except Exception:
                pass
            _log.info("Worker 已停止，锁已释放。")
    except KeyboardInterrupt:
        _log.info("收到 Ctrl+C，退出。")
        stop_evt.set()
        try:
            _r.delete(LOCK_KEY)
        except Exception:
            pass
    except Exception as _fatal:
        _log.exception("run_worker 启动失败: %s", _fatal)
        sys.exit(1)
