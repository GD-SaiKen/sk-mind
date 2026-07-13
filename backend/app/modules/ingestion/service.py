"""Ingestion 模块服务层 — 委托 DAO，为未来业务逻辑扩展预留入口。

当前 CRUD 操作直接委托 DAO；复杂业务编排（如执行前的校验）在此层扩展。
"""

from app.modules.ingestion import dao

# ── 任务 ──
task_list = dao.task_list
task_get_by_id = dao.task_get_by_id
task_insert = dao.task_insert
task_update = dao.task_update

# ── 批次 ──
batch_list = dao.batch_list
batch_get_by_id = dao.batch_get_by_id
batch_insert = dao.batch_insert
batch_update = dao.batch_update

# ── 错误 ──
error_list = dao.error_list
error_insert = dao.error_insert
