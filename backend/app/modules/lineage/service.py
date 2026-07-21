"""Lineage 模块服务层。"""

from app.modules.lineage.dao import (
    edge_get_by_id,
    edge_insert,
    edge_list_all,
    edge_update,
)

# 当前阶段服务层直接委托给 DAO，后续可在此层添加血缘图谱查询等业务逻辑
