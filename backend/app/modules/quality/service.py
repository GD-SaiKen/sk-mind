"""Quality 模块服务层。"""

from app.modules.quality.dao import (
    issue_get_by_id,
    issue_list_all,
    issue_update_status,
    rule_get_by_id,
    rule_insert,
    rule_list_all,
    rule_update,
    run_list_all,
)

# 当前阶段服务层直接委托给 DAO，后续可在此层添加质量检查引擎等业务逻辑
