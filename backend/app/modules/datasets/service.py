"""Dataset 模块服务层。"""

from app.modules.datasets.dao import (
    data_table_list_by_dataset,
    dataset_field_list,
    dataset_get_by_id,
    dataset_insert,
    dataset_list_all,
    dataset_update,
)

# 当前阶段服务层直接委托给 DAO，后续可在此层添加业务逻辑
