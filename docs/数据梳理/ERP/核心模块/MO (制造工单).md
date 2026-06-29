---
module: "MO"
name_zh: "制造工单"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 41
columns: 2212
category: manufacturing
semantic_object: "ManufacturingOrder/制造工单"
original_tables: 42
filtered_out: 0
tags: ["ERP", "E10", "manufacturing", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# MO (制造工单) - ManufacturingOrder/制造工单

> [!info] Phase 1 Core Module
> Semantic Object: ManufacturingOrder/制造工单
> Kept: 41 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 2

## Related Modules

- [[../modules/BOM (物料清单).md|BOM (物料清单)]]
- [[../modules/WORK (工作中心).md|WORK (工作中心)]]
- [[../modules/ECN (工程变更).md|ECN (工程变更)]]
- [[../modules/ROUTE (工艺路线).md|ROUTE (工艺路线)]]

---

## Tables

- **MO_CHANGE (工单变更单)**
- **MO_CHANGE_D (工单变更单单身)**
- **MO_D (工单单身档)**
- **MO_DAILY_PRODUCTION_QTY (工单每日产量档)**
- **MO_DEMAND (工单需求信息)**
- **MO_DISPATCHED (工单已派工)**
- **MO_INSPECTION (生产入库检验单)**
- **MO_INSPECTION_AI (品质检验不良原因--计数)**
- **MO_INSPECTION_D (生产入库检验单计数单身)**
- **MO_INSPECTION_D1 (生产入库检验单计量单身)**
- **MO_INSPECTION_SD (多次检验信息)**
- **MO_INSPECTION_VI (品质检验不良原因--计量)**
- **MO_ISSUED_SETS (工单领料状况)**
- **MO_PRODUCT (工单产出信息)**
- **MO_R_INSPECTION (工艺检验单)**
- **MO_R_INSPECTION_AI (品质检验不良原因-计数)**
- **MO_R_INSPECTION_D (工艺检验单计数单身)**
- **MO_R_INSPECTION_D1 (工艺检验单计量单身)**
- **MO_R_INSPECTION_SD (多次检验信息)**
- **MO_R_INSPECTION_VI (品质检验不良原因-计量)**
- **MO_RECEIPT (生产入库单)**
- **MO_RECEIPT_D (生产入库单单身)**
- **MO_RECEIPT_REQUISTION (生产入库申请单)**
- **MO_RECEIPT_REQUISTION_D (生产入库申请单单身)**
- **MO_RECEIPT_TO_ISSUE (维护入库转领料单)**
- **MO_RECEIPT_TO_ISSUE_D (工单单身明细)**
- **MO_RECEIPT_TO_ISSUE_SD (工单子单身)**
- **MO_ROUTING (工单工艺信息)**
- **MO_ROUTING_D (工单工艺单身)**
- **MO_ROUTING_DISPATCH (工单工艺派工信息)**
- **MO_ROUTING_DISPATCH_D (工单工艺派工信息明细)**
- **MO_ROUTING_MATERIAL (工单工艺路线物料)**
- **MO_ROUTING_PATH (工单工艺路径信息)**
- **MO_ROUTING_PATH_WC (工单工艺路径工作中心信息)**
- **MO_ROUTING_PRODUCT (工单工艺期间产出信息)**
- **MO_ROUTING_PRODUCT_D (工单工艺期间产出信息单身)**
- **MO_ROUTING_SUB_OPERATION (工单子工艺信息)**
- **MO_ROUTING_WIP (工单工艺工作中心生产信息)**
- **MO_ROUTING_WIP_MATERIAL (工单在制物料)**
- **MO_ROUTING_WORK_CENTER (工单工艺工作中心约束)**
- **MO_SPLIT (工单拆分)**

---

## Table Details

### MO_CHANGE (工单变更单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MO_CHANGE_ID | 主键 | GUID | Y | Y |
| 4 | CHANGE_VERSION | 变更版本 | string(8) | Y |  |
| 5 | CHANGE_DATE | 变更日期 | date | Y |  |
| 6 | CHANGE_REASON | 变更原因 | string(510) | Y |  |
| 7 | DOC_DATE | 单据日期 | date | Y |  |
| 8 | URGENT | 急料 | number(0/1) | Y |  |
| 9 | BOM_VERSION_TIMES |  | string(8) | Y |  |
| 10 | BOM_DATE | BOM日期 | date | Y |  |
| 11 | ITEM_DESCRIPTION | 产品品名 | string(120) | Y |  |
| 12 | ITEM_SPECIFICATION | 产品规格 | string(510) | Y |  |
| 13 | PLAN_START_DATE | 预计开工日 | date | Y |  |
| 14 | PLAN_COMPLETE_DATE | 预计完工日 | date | Y |  |
| 15 | ACTUAL_START_DATE | 实际开工日 | date | Y |  |
| 16 | ACTUAL_COMPLETE_DATE | 实际完工日 | date | Y |  |
| 17 | PLAN_QTY | 预计产量 | number(16,6) | Y |  |
| 18 | PLAN_LOT | 计划批号 | string(120) | Y |  |
| 19 | REQUIRED_DATE | 需求日期 | date | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | ORIGINAL_DOC_DATE | 原开单日期 | date | Y |  |
| 22 | ORIGINAL_ITEM_DESCRIPTION | 原产品品名 | string(120) | Y |  |
| 23 | ORIGINAL_ITEM_SPECIFICATION | 原产品规格 | string(510) | Y |  |
| 24 | ORIGINAL_BOM_VERSION_TIMES | 原BOM版次 | string(8) | Y |  |
| 25 | ORIGINAL_BOM_DATE | 原BOM日期 | date | Y |  |
| 26 | ORIGINAL_URGENT | 原急料 | number(0/1) | Y |  |
| 27 | ORIGINAL_PLAN_QTY | 原预计产量 | number(16,6) | Y |  |
| 28 | ORIGINAL_PLAN_START_DATE | 原预计开工日 | date | Y |  |
| 29 | ORIGINAL_PLAN_COMPLETE_DATE | 原预计完工日 | date | Y |  |
| 30 | ORIGINAL_ACTUAL_START_DATE | 原实际开工日 | date | Y |  |
| 31 | ORIGINAL_ACTUAL_COMPLETE_DATE | 原实际完工日 | date | Y |  |
| 32 | ORIGINAL_PLAN_LOT | 原计划批号 | string(120) | Y |  |
| 33 | ORIGINAL_REQUIREMENT_DATE | 原需求日期 | date | Y |  |
| 34 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 35 | STATUS | 状态码 | string(40) | Y |  |
| 36 | ROUTING_CONTROL | 工艺管理 | number(0/1) | Y |  |
| 37 | ORIGINAL_STATUS | 原状态码 | string(40) | Y |  |
| 38 | ORIGINAL_ROUTING_CONTROL | 原工艺管理 | number(0/1) | Y |  |
| 39 | RECEIPT_REQ_CONTROL | 入库申请 | number(0/1) | Y |  |
| 40 | ORIGINAL_RECEIPT_REQ_CONTROL | 原入库申请 | number(0/1) | Y |  |
| 41 | MO_ID | 工单单号 | GUID | Y |  |
| 42 | ITEM_ID | 产品品号 | GUID | Y |  |
| 43 | BUSINESS_UNIT_ID | 单位 | GUID | Y |  |
| 44 | ITEM_FEATURE_ID | 产品特征码 | GUID | Y |  |
| 45 | ITEM_ROUTING_ID | 工艺路线 | GUID | Y |  |
| 46 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 47 | PARA_MO_ID | 母工单单号 | GUID | Y |  |
| 48 | ORIGINAL_ITEM_ID | 原产品品号 | GUID | Y |  |
| 49 | ORIGINAL_BUSINESS_UNIT_ID | 原单位 | GUID | Y |  |
| 50 | ORIGINAL_ITEM_FEATURE_ID | 原产品特征码 | GUID | Y |  |
| 51 | ORIGINAL_ITEM_ROUTING_ID | 原工艺路线 | GUID | Y |  |
| 52 | ORIGINAL_PARA_MO_ID | 原母工单单号 | GUID | Y |  |
| 53 | ORIGINAL_ADMIN_UNIT_ID | 原生产部门 | GUID | Y |  |
| 54 | UP_MO_ID | 上阶工单单号 | GUID | Y |  |
| 55 | ORIGINAL_UP_MO_ID | 原上阶工单单号 | GUID | Y |  |
| 56 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 57 | ORIGINAL_ITEM_LOT_ID | 原批号 | GUID | Y |  |
| 58 | DOC_ID | 单据性质 | GUID | Y |  |
| 59 | PLAN_SECOND_QTY | 预计产量第二数量 | number(16,6) | Y |  |
| 60 | ORIGINAL_PLAN_SECOND_QTY | 原预计产量第二数量 | number(16,6) | Y |  |
| 61 | ITEM_ROUTING_CONTROL | 工艺管理 | string(40) | Y |  |
| 62 | ORI_ITEM_ROUTING_CONTROL | 原工艺管理 | string(40) | Y |  |
| 63 | TRANSACTION_DATE | 工单变更日期 | date | Y |  |
| 64 | PROJECT_ID | 项目 | GUID | Y |  |
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | PrintCount | 打印次数 | number | Y |  |
| 67 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 68 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 69 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 70 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 71 | CreateDate | 创建日期 | date | Y |  |
| 72 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 73 | ModifiedDate | 修改日期 | date | Y |  |
| 74 | CreateBy | 创建者 | GUID | Y |  |
| 75 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 76 | ModifiedBy | 修改者 | GUID | Y |  |
| 77 | Attachments | 附件 | string | Y |  |
| 78 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 79 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 80 | ApproveDate | 修改日期 | date | Y |  |
| 81 | ApproveBy | 修改人 | GUID | Y |  |
| 82 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 83 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 84 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 85 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 86 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 87 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 88 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 89 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 90 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 91 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 92 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 93 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 94 | UDF041 | 自定义字段12 | date | Y |  |
| 95 | UDF042 | 自定义字段13 | date | Y |  |
| 96 | UDF051 | 自定义字段14 | GUID | Y |  |
| 97 | UDF052 | 自定义字段15 | GUID | Y |  |
| 98 | UDF053 | 自定义字段16 | GUID | Y |  |
| 99 | UDF054 | 自定义字段17 | GUID | Y |  |
| 100 | Owner_Org_RTK |  | string(400) | Y |  |
| 101 | Owner_Org_ROid |  | GUID | Y |  |
| 102 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 103 | SOURCE_ID_ROid |  | GUID | Y |  |
| 104 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 105 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 106 | PMC_STATUS | 任务执行状态 | string(40) | Y |  |


### MO_CHANGE_D (工单变更单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_CHANGE_D_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | ITEM_DESCRIPTION | 材料品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 材料规格 | string(510) | Y |  |
| 6 | REPLACE_ITEM | 取替代料 | string(40) | Y |  |
| 7 | REQUIRED_QTY | 需领用量 | number(16,6) | Y |  |
| 8 | ITEM_TYPE | 材料类型 | string(40) | Y |  |
| 9 | PLAN_ISSUE_DATE | 预计领料日 | date | Y |  |
| 10 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ORIGINAL_ITEM_DESCRIPTION | 原材料名称 | string(120) | Y |  |
| 13 | ORIGINAL_ITEM_SPECIFICATION | 原材料规格 | string(510) | Y |  |
| 14 | ORIGINAL_REPLACE_ITEM | 原取替代料 | string(40) | Y |  |
| 15 | ORIGINAL_REQUIRED_QTY | 原需领用量 | number(16,6) | Y |  |
| 16 | ORIGINAL_ITEM_TYPE | 原材料类型 | string(40) | Y |  |
| 17 | ORIGINAL_REPLACED_QTY | 原被取替代数量 | number(16,6) | Y |  |
| 18 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 19 | ORIGINAL_PLAN_ISSUE_DATE | 原预计领料日期 | date | Y |  |
| 20 | ITEM_GROUP | 元件群组 | GUID | Y |  |
| 21 | REPLACE_GROUP | 替代群组 | GUID | Y |  |
| 22 | ORIGINAL_ITEM_GROUP | 元件群组 | GUID | Y |  |
| 23 | ORIGINAL_REPLACE_GROUP | 替代群组 | GUID | Y |  |
| 24 | UP_LEVEL_ITEM_FEATURE_ID | 上阶主件特征码 | GUID | Y |  |
| 25 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 26 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 27 | ORIGINAL_UP_LEVEL_FEATURE_ID | 原上阶主件特征码 | GUID | Y |  |
| 28 | ORIGINAL_ISSUE_OVERRUN_RATE | 原超领率 | number(5,4) | Y |  |
| 29 | ORIGINAL_ISSUE_SHORTAGE_RATE | 原缺领率 | number(5,4) | Y |  |
| 30 | ITEM_ID | 材料品号 | GUID | Y |  |
| 31 | UNIT_ID | 单位 | GUID | Y |  |
| 32 | ITEM_FEATURE_ID | 材料特征码 | GUID | Y |  |
| 33 | REPLACED_ITEM_ID | 被取替代品号 | GUID | Y |  |
| 34 | UP_LEVEL_ITEM_ID | 上阶主件品号 | GUID | Y |  |
| 35 | OPERATION_ID | 工艺 | GUID | Y |  |
| 36 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 37 | ORIGINAL_MO_CHANGE_D_ID | 原主键 | GUID | Y |  |
| 38 | ORIGINAL_ITEM_ID | 原材料品号 | GUID | Y |  |
| 39 | ORIGINAL_UNIT_ID | 原单位 | GUID | Y |  |
| 40 | ORIGINAL_ITEM_FEATURE_ID | 原品号特征码 | GUID | Y |  |
| 41 | ORIGINAL_REPLACED_ITEM_ID | 原被取替代品号 | GUID | Y |  |
| 42 | ORIGINAL_UP_LEVEL_ITEM_ID | 原上阶主件品号 | GUID | Y |  |
| 43 | ORIGINAL_OPERATION_ID | 原工艺 | GUID | Y |  |
| 44 | ORIGINAL_WAREHOUSE_ID | 原仓库 | GUID | Y |  |
| 45 | REPLACED_FEATURE_ID | 被取替代特征码 | GUID | Y |  |
| 46 | ORIGINAL_REPLACED_FEATURE_ID | 原被取替代特征码 | GUID | Y |  |
| 47 | BIN_ID | 库位 | GUID | Y |  |
| 48 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 49 | ORIGINAL_BIN_ID | 原库位 | GUID | Y |  |
| 50 | ORIGINAL_ITEM_LOT_ID | 原批号 | GUID | Y |  |
| 51 | ORIGINAL_REQUIRED_SECOND_QTY | 原需领用量第二数量 | number(16,6) | Y |  |
| 52 | REQUIRED_SECOND_QTY | 需领用量第二数量 | number(16,6) | Y |  |
| 53 | PROJECT_ID | 项目 | GUID | Y |  |
| 54 | ORIGINAL_PROJECT_ID | 原项目 | GUID | Y |  |
| 55 | LEAST_REQUIRED_QTY | 最低需求数量 | number(16,6) | Y |  |
| 56 | ORIGINAL_LEAST_REQUIRED_QTY | 原最低需求数量 | number(16,6) | Y |  |
| 57 | ORIGINAL_COMPONENT_LOCATION | 原插件位置 | string | Y |  |
| 58 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |
| 69 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 70 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 71 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 72 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 73 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 74 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 75 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 76 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 77 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 78 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 79 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 80 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 81 | UDF041 | 自定义字段12 | date | Y |  |
| 82 | UDF042 | 自定义字段13 | date | Y |  |
| 83 | UDF051 | 自定义字段14 | GUID | Y |  |
| 84 | UDF052 | 自定义字段15 | GUID | Y |  |
| 85 | UDF053 | 自定义字段16 | GUID | Y |  |
| 86 | UDF054 | 自定义字段17 | GUID | Y |  |
| 87 | MO_CHANGE_ID |  | GUID | Y |  |


### MO_D (工单单身档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 材料品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 材料规格 | string(510) | Y |  |
| 5 | REPLACE_ITEM | 取替代料 | string(40) | Y |  |
| 6 | UP_LEVEL_ITEM_ID | 上阶主件品号 | GUID | Y |  |
| 7 | REPLACED_ITEM_ID | 被取替代品号 | GUID | Y |  |
| 8 | REPLACED_ITEM_FEATURE_ID | 被取替代特征码 | GUID | Y |  |
| 9 | REQUIRED_QTY | 需领用量 | number(16,6) | Y |  |
| 10 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 11 | ISSUED_QTY | 已领用量 | number(16,6) | Y |  |
| 12 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 13 | PLAN_ISSUE_DATE | 预计领料日期 | date | Y |  |
| 14 | ACTUAL_ISSUE_DATE | 实际领料日期 | date | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 17 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 18 | UP_LEVEL_ITEM_FEATURE_ID | 上阶主件特征码 | GUID | Y |  |
| 19 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 20 | ITEM_GROUP | 元件群组 | GUID | Y |  |
| 21 | REPLACE_GROUP | 替代群组 | GUID | Y |  |
| 22 | ITEM_ID | 材料品号 | GUID | Y |  |
| 23 | UNIT_ID | 单位 | GUID | Y |  |
| 24 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 25 | OPERATION_ID | 工艺 | GUID | Y |  |
| 26 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 27 | BIN_ID | 库位 | GUID | Y |  |
| 28 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 29 | REQUIRED_SECOND_QTY | 需领用量第二数量 | number(16,6) | Y |  |
| 30 | ISSUED_SECOND_QTY | 已领用量第二数量 | number(16,6) | Y |  |
| 31 | ISSUED_REQ_QTY | 已申请量 | number(16,6) | Y |  |
| 32 | ISSUED_REQ_SECOND_QTY | 已申请第二数量 | number(16,6) | Y |  |
| 33 | MO_D_PIC | 工单材料图片 | string(4000) | Y |  |
| 34 | PROJECT_ID | 项目 | GUID | Y |  |
| 35 | LEAST_REQUIRED_QTY | 最低需领用量 | number(16,6) | Y |  |
| 36 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 37 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 38 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 39 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 40 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 41 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 42 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 43 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 44 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 45 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 46 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 47 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 48 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 49 | UDF041 | 自定义字段12 | date | Y |  |
| 50 | UDF042 | 自定义字段13 | date | Y |  |
| 51 | UDF051 | 自定义字段14 | GUID | Y |  |
| 52 | UDF052 | 自定义字段15 | GUID | Y |  |
| 53 | UDF053 | 自定义字段16 | GUID | Y |  |
| 54 | UDF054 | 自定义字段17 | GUID | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | Version | 版本号，不要随意更改 | binary | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | MO_ID |  | GUID | Y |  |
| 66 | ITEM_TYPE_02 | 供料方式_02 | string(40) | Y |  |
| 67 | TRANSFER_QTY | 调拨数量 | number(16,6) | Y |  |


### MO_DAILY_PRODUCTION_QTY (工单每日产量档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_DAILY_PRODUCTION_QTY_ID | 主键 | GUID | Y | Y |
| 3 | PRODUCTION_DATE | 生产日期 | date | Y |  |
| 4 | PRODUCTION_QTY | 生产数量 | number(16,6) | Y |  |
| 5 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 36 | SOURCE_ID_ROid |  | GUID | Y |  |
| 37 | MO_ID |  | GUID | Y |  |


### MO_DEMAND (工单需求信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_DEMAND_ID | 主键 | GUID | Y | Y |
| 3 | DEMAND_QTY | 订单数量 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | LOCKED_FLAG | 供需关连锁定 | number(0/1) | Y |  |
| 6 | PROJECT_ID | 项目 | GUID | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | DEMAND_DOC_RTK |  | string(400) | Y |  |
| 36 | DEMAND_DOC_ROid |  | GUID | Y |  |
| 37 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | MO_ID |  | GUID | Y |  |


### MO_DISPATCHED

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | MO_DISPATCHED_ID | 主键 | GUID | Y | Y |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 6 | CURRENCY_ID | 币种 | GUID | Y |  |
| 7 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 8 | PURCHASED_QTY | 已委外数量 | number(16,6) | Y |  |
| 9 | APPLY_QTY | 分配数量 | number(16,6) | Y |  |
| 10 | PLAN_COMPLETE_DATE | 预计完工日期 | date | Y |  |
| 11 | PRICE | 委外单价 | number(16,6) | Y |  |
| 12 | PURCHASE_STATUS | 采购状态 | string(40) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 15 | BUSINESS_UNIT_ID | 采购单位 | GUID | Y |  |
| 16 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 17 | MO_ID | 工单 | GUID | Y |  |
| 18 | TAX_ID | 税种 | GUID | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |


### MO_INSPECTION (生产入库检验单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | MO_INSPECTION_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(400) | Y |  |
| 8 | INSPECTION_DATE | 检验日期 | date | Y |  |
| 9 | INSPECTION_TIMES | 最大抽样次数 | string(400) | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 12 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 13 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 14 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 15 | INSPECTION_QTY | 送检数量 | number(16,6) | Y |  |
| 16 | INSPECTION_UNIT_ID | 品管单位 | GUID | Y |  |
| 17 | STRICTNESS_DEGREE | 宽严程度 | string(40) | Y |  |
| 18 | INSPECTION_DUE_DATE | 检验期限 | date | Y |  |
| 19 | SUBMIT_DEPT_ID | 送检部门 | GUID | Y |  |
| 20 | SUBMIT_EMP_ID | 送检人员 | GUID | Y |  |
| 21 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 22 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 23 | ACCEPTABLE_QTY | 合格数量 | number(16,6) | Y |  |
| 24 | UNQUALIFIED_QTY | 不合格量 | number(16,6) | Y |  |
| 25 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 26 | DECISION | 判定结果 | string(400) | Y |  |
| 27 | DECISION_DESCRIPTION | 判定说明 | string(510) | Y |  |
| 28 | RESULT_STATUS | 业务判定状态 | string(400) | Y |  |
| 29 | REMARK | 备注 | string(510) | Y |  |
| 30 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 31 | SOURCE_ID | 源单 | GUID | Y |  |
| 32 | INSPECTION_PLAN_ID | 质检方案 | GUID | Y |  |
| 33 | COMPANY_ID | 公司 | GUID | Y |  |
| 34 | PROJECT_ID | 项目 | GUID | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | PrintCount | 打印次数 | number | Y |  |
| 54 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 55 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 56 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 57 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | Attachments | 附件 | string | Y |  |
| 65 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 66 | Version | 版本号，不要随意更改 | binary | Y |  |
| 67 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 68 | ApproveDate | 修改日期 | date | Y |  |
| 69 | ApproveBy | 修改人 | GUID | Y |  |
| 70 | Owner_Org_RTK |  | string(400) | Y |  |
| 71 | Owner_Org_ROid |  | GUID | Y |  |


### MO_INSPECTION_AI (品质检验不良原因--计数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_INSPECTION_AI_ID | 主键 | GUID | Y | Y |
| 3 | DEFECTS | 不合格数 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | MO_INSPECTION_D_ID |  | GUID | Y |  |


### MO_INSPECTION_D (生产入库检验单计数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_INSPECTION_D_ID | 主键 | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | DEFECT_CLASS | 缺点等级 | string(400) | Y |  |
| 4 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 5 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 6 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 7 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 8 | DECISION | 合格否 | number(0/1) | Y |  |
| 9 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 12 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 13 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 14 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 15 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 16 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 17 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 18 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 19 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 20 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 21 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 22 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 23 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 24 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 25 | UDF041 | 自定义字段12 | date | Y |  |
| 26 | UDF042 | 自定义字段13 | date | Y |  |
| 27 | UDF051 | 自定义字段14 | GUID | Y |  |
| 28 | UDF052 | 自定义字段15 | GUID | Y |  |
| 29 | UDF053 | 自定义字段16 | GUID | Y |  |
| 30 | UDF054 | 自定义字段17 | GUID | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | MO_INSPECTION_ID |  | GUID | Y |  |


### MO_INSPECTION_D1 (生产入库检验单计量单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_INSPECTION_D1_ID | 主键 | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | DEFECT_CLASS | 缺点等级 | string(400) | Y |  |
| 4 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 5 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 6 | ACCEPTANCE_CONSTANT | 接收常数k | number(16,6) | Y |  |
| 7 | SS | 样本标准差S | number(16,6) | Y |  |
| 8 | XX | 平均值X | number(16,6) | Y |  |
| 9 | UU | 标准上限 | number(16,6) | Y |  |
| 10 | LL | 标准下限 | number(16,6) | Y |  |
| 11 | QU | 质量QU | number(16,6) | Y |  |
| 12 | QL | 质量QL | number(16,6) | Y |  |
| 13 | DECISION | 合格否 | number(0/1) | Y |  |
| 14 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 17 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | MO_INSPECTION_ID |  | GUID | Y |  |


### MO_INSPECTION_SD (多次检验信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_INSPECTION_SD_ID | 主键 | GUID | Y | Y |
| 2 | INSPECTION_TIMES | 检验次数 | number | Y |  |
| 3 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 4 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 5 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 6 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | MO_INSPECTION_D_ID |  | GUID | Y |  |


### MO_INSPECTION_VI (品质检验不良原因--计量)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_INSPECTION_VI_ID | 主键 | GUID | Y | Y |
| 2 | DEFECTS | 不合格数 | number(16,6) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | MO_INSPECTION_D1_ID |  | GUID | Y |  |


### MO_ISSUED_SETS (工单领料状况)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ISSUED_SETS_ID | 主键 | GUID | Y | Y |
| 2 | ISSUE_TYPE | 领料模式 | string(40) | Y |  |
| 3 | REQ_ISSUED_SETS | 已申请套数 | number(16,6) | Y |  |
| 4 | ISSUED_SETS | 已领套数 | number(16,6) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | ISSUE_DESTINATION_RTK |  | string(400) | Y |  |
| 34 | ISSUE_DESTINATION_ROid |  | GUID | Y |  |
| 35 | MO_ID |  | GUID | Y |  |


### MO_PRODUCT (工单产出信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_PRODUCT_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | UNIT_ID | 库存单位 | GUID | Y |  |
| 8 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 9 | PER_QTY | 产出比例 | number(16,6) | Y |  |
| 10 | PLAN_QTY | 预计产量 | number(16,6) | Y |  |
| 11 | REQ_QTY | 入库申请数量 | number(16,6) | Y |  |
| 12 | COMPLETED_QTY | 入库数量 | number(16,6) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 15 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 16 | PLAN_SECOND_QTY | 预计产量第二数量 | number(16,6) | Y |  |
| 17 | REQ_SECOND_QTY | 入库申请第二数量 | number(16,6) | Y |  |
| 18 | COMPLETED_SECOND_QTY | 已入库第二数量 | number(16,6) | Y |  |
| 19 | SCRAP_SECOND_QTY | 报废第二数量 | number(16,6) | Y |  |
| 20 | DESTROYED_SECOND_QTY | 破坏第二数量 | number(16,6) | Y |  |
| 21 | WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | MO_ID |  | GUID | Y |  |


### MO_R_INSPECTION (工艺检验单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MO_R_INSPECTION_ID | 主键 | GUID | Y | Y |
| 7 | INSPECTION_DATE | 检验日期 | date | Y |  |
| 8 | INSPECTION_PLAN_ID | 质检方案 | GUID | Y |  |
| 9 | ITEM_ID | 品号 | GUID | Y |  |
| 10 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 12 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 13 | SOURCE_ID | 源单 | GUID | Y |  |
| 14 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 15 | OPERATION_ID | 工艺 | GUID | Y |  |
| 16 | MO_ROUTING_D_ID | 后道工序 | GUID | Y |  |
| 17 | INSPECTION_QTY | 送检数量 | number(16,6) | Y |  |
| 18 | INSPECTION_UNIT_ID | 品管单位 | GUID | Y |  |
| 19 | STRICTNESS_DEGREE | 宽严程度 | string(40) | Y |  |
| 20 | INSPECTION_DUE_DATE | 检验期限 | date | Y |  |
| 21 | SUBMIT_DEPT_ID | 送检部门 | GUID | Y |  |
| 22 | SUBMIT_EMP_ID | 送检人员 | GUID | Y |  |
| 23 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 24 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 25 | ACCEPTABLE_QTY | 合格数量 | number(16,6) | Y |  |
| 26 | UNQUALIFIED_QTY | 不合格量 | number(16,6) | Y |  |
| 27 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 28 | DECISION | 判定结果 | string(40) | Y |  |
| 29 | DECISION_DESCRIPTION | 判定说明 | string(510) | Y |  |
| 30 | RESULT_STATUS | 业务判断状态 | string(40) | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | CATEGORY | 单据性质 | string(40) | Y |  |
| 33 | TO_OPERATION_ID | 后道工艺 | GUID | Y |  |
| 34 | INSPECTION_TIMES | 最大抽样次数 | string(40) | Y |  |
| 35 | COMPANY_ID | 公司 | GUID | Y |  |
| 36 | PROJECT_ID | 项目 | GUID | Y |  |
| 37 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 38 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 39 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 40 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 41 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 42 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 43 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 44 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 45 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 46 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 47 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 48 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 49 | UDF041 | 自定义字段12 | date | Y |  |
| 50 | UDF042 | 自定义字段13 | date | Y |  |
| 51 | UDF051 | 自定义字段14 | GUID | Y |  |
| 52 | UDF052 | 自定义字段15 | GUID | Y |  |
| 53 | UDF053 | 自定义字段16 | GUID | Y |  |
| 54 | UDF054 | 自定义字段17 | GUID | Y |  |
| 55 | PrintCount | 打印次数 | number | Y |  |
| 56 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 57 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 58 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 59 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | CreateDate | 创建日期 | date | Y |  |
| 62 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 63 | ModifiedDate | 修改日期 | date | Y |  |
| 64 | CreateBy | 创建者 | GUID | Y |  |
| 65 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 66 | ModifiedBy | 修改者 | GUID | Y |  |
| 67 | Attachments | 附件 | string | Y |  |
| 68 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |


### MO_R_INSPECTION_AI (品质检验不良原因-计数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_R_INSPECTION_AI_ID | 主键 | GUID | Y | Y |
| 3 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 4 | DEFECTS | 不合格数 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | MO_R_INSPECTION_D_ID |  | GUID | Y |  |


### MO_R_INSPECTION_D (工艺检验单计数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SEQUENCE | 检验顺序 | number | Y |  |
| 2 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 3 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 4 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 5 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 6 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 7 | DECISION | 合格否 | number(0/1) | Y |  |
| 8 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 11 | MO_R_INSPECTION_D_ID | 主键 | GUID | Y | Y |
| 12 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 13 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 14 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 15 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 16 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 17 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 18 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 19 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 20 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 21 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 22 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 23 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 24 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 25 | UDF041 | 自定义字段12 | date | Y |  |
| 26 | UDF042 | 自定义字段13 | date | Y |  |
| 27 | UDF051 | 自定义字段14 | GUID | Y |  |
| 28 | UDF052 | 自定义字段15 | GUID | Y |  |
| 29 | UDF053 | 自定义字段16 | GUID | Y |  |
| 30 | UDF054 | 自定义字段17 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | MO_R_INSPECTION_ID |  | GUID | Y |  |


### MO_R_INSPECTION_D1 (工艺检验单计量单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SEQUENCE | 检验顺序 | number | Y |  |
| 2 | MO_R_INSPECTION_D1_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 4 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 5 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 6 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 7 | ACCEPTANCE_CONSTANT | 接受常数k | number(16,6) | Y |  |
| 8 | SS | 样品标准差S | number(16,6) | Y |  |
| 9 | XX | 平均值X | number(16,6) | Y |  |
| 10 | UU | 标准上限 | number(16,6) | Y |  |
| 11 | LL | 标准下限 | number(16,6) | Y |  |
| 12 | QU | 质量QU | number(16,6) | Y |  |
| 13 | QL | 质量QL | number(16,6) | Y |  |
| 14 | DECISION | 合格否 | number(0/1) | Y |  |
| 15 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 16 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | MO_R_INSPECTION_ID |  | GUID | Y |  |


### MO_R_INSPECTION_SD (多次检验信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_R_INSPECTION_SD_ID | 主键 | GUID | Y | Y |
| 2 | IINPECTION_TIME | 检验次数 | number | Y |  |
| 3 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 4 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 5 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 6 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | MO_R_INSPECTION_D_ID |  | GUID | Y |  |


### MO_R_INSPECTION_VI (品质检验不良原因-计量)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_R_INSPECTION_VI_ID | 主键 | GUID | Y | Y |
| 2 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 3 | DEFECTS | 不合格数 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | MO_R_INSPECTION_D1_ID |  | GUID | Y |  |


### MO_RECEIPT (生产入库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MO_RECEIPT_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | BACKFLUSH_UPDATE | 自动扣料更新码 | number(0/1) | Y |  |
| 9 | JOURNALIZED_COST | 生成分录-成本 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 12 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 13 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 14 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 15 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 16 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 17 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 18 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 19 | WIP_NO | WIP传入ID | string(40) | Y |  |
| 20 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 21 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 22 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 23 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 24 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 25 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 26 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 27 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 28 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 29 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 30 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 31 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 32 | UDF041 | 自定义字段12 | date | Y |  |
| 33 | UDF042 | 自定义字段13 | date | Y |  |
| 34 | UDF051 | 自定义字段14 | GUID | Y |  |
| 35 | UDF052 | 自定义字段15 | GUID | Y |  |
| 36 | UDF053 | 自定义字段16 | GUID | Y |  |
| 37 | UDF054 | 自定义字段17 | GUID | Y |  |
| 38 | PrintCount | 打印次数 | number | Y |  |
| 39 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 40 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 41 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 42 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Attachments | 附件 | string | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | Owner_Org_RTK |  | string(400) | Y |  |
| 56 | Owner_Org_ROid |  | GUID | Y |  |
| 57 | SOURCE_DOC_ID_RTK |  | string(400) | Y |  |
| 58 | SOURCE_DOC_ID_ROid |  | GUID | Y |  |
| 59 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE_ID_ROid |  | GUID | Y |  |
| 61 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |


### MO_RECEIPT_D (生产入库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_RECEIPT_D_ID | 主键 | GUID | Y | Y |
| 3 | RECEIPT_REQUISTION_DOC_SEQ | 项次 | number | Y |  |
| 4 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 6 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 7 | ACCEPTED_QTY | 验收数量 | number(16,6) | Y |  |
| 8 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 9 | ACCEPTED_PACKING_QTY1 | 验收大包装数量 | number(16,6) | Y |  |
| 10 | ACCEPTED_PACKING_QTY2 | 验收中包装数量 | number(16,6) | Y |  |
| 11 | ACCEPTED_PACKING_QTY3 | 验收小包装数量 | number(16,6) | Y |  |
| 12 | ACCEPTED_PACKING_QTY4 | 验收最小包装数量 | number(16,6) | Y |  |
| 13 | ACCEPTED_PACKING_QTY | 验收包装数量描述 | string(240) | Y |  |
| 14 | SECOND_QTY | 第二单位验收数量 | number(16,6) | Y |  |
| 15 | ACCEPTED_INVENTORY_QTY | 验收库存数量 | number(16,6) | Y |  |
| 16 | SCRAPED_QTY | 已报废数量 | number(16,6) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | EFFECTIVE_DATE | 有效日期 | date | Y |  |
| 19 | REINSEPCTION_DATE | 复检日期 | date | Y |  |
| 20 | PRODUCTION_DATE | 生产日期 | date | Y |  |
| 21 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 22 | MO_RECEIPT_REQUISTION_D_ID | 入库申请单单号 | GUID | Y |  |
| 23 | MO_ID | 工单单号 | GUID | Y |  |
| 24 | ITEM_ID | 产品品号 | GUID | Y |  |
| 25 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 26 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 27 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 28 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 29 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 30 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 31 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 32 | SOURCE_MO_ID | 源工单 | GUID | Y |  |
| 33 | BIN_ID | 库位 | GUID | Y |  |
| 34 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 35 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 36 | MO_PRODUCT_ID | 工单产出ID | GUID | Y |  |
| 37 | SCRAP_SECOND_QTY | 报废第二数量 | number(16,6) | Y |  |
| 38 | DESTROYED_SECOND_QTY | 破坏第二数量 | number(16,6) | Y |  |
| 39 | PROJECT_ID | 项目 | GUID | Y |  |
| 40 | WIP_DOCNO | WIP单号序号 | string(50) | Y |  |
| 41 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 42 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 43 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 44 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 45 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 46 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 47 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 48 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 49 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 50 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 51 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 52 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 53 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 54 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 55 | UDF041 | 自定义字段12 | date | Y |  |
| 56 | UDF042 | 自定义字段13 | date | Y |  |
| 57 | UDF051 | 自定义字段14 | GUID | Y |  |
| 58 | UDF052 | 自定义字段15 | GUID | Y |  |
| 59 | UDF053 | 自定义字段16 | GUID | Y |  |
| 60 | UDF054 | 自定义字段17 | GUID | Y |  |
| 61 | CreateDate | 创建日期 | date | Y |  |
| 62 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 63 | ModifiedDate | 修改日期 | date | Y |  |
| 64 | CreateBy | 创建者 | GUID | Y |  |
| 65 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 66 | ModifiedBy | 修改者 | GUID | Y |  |
| 67 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 68 | ApproveDate | 修改日期 | date | Y |  |
| 69 | ApproveBy | 修改人 | GUID | Y |  |
| 70 | Version | 版本号，不要随意更改 | binary | Y |  |
| 71 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 72 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 73 | MO_RECEIPT_ID |  | GUID | Y |  |


### MO_RECEIPT_REQUISTION (生产入库申请单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MO_RECEIPT_REQUISTION_ID | 主键 | GUID | Y | Y |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 9 | CLOSE | 结束码 | string(40) | Y |  |
| 10 | TRANSACTION_DATE | 申请日期 | date | Y |  |
| 11 | WIP_NO | WIP传入ID | string(40) | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 15 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 16 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 17 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |


### MO_RECEIPT_REQUISTION_D (生产入库申请单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_RECEIPT_REQUISTION_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | REQUEST_QTY | 申请数量 | number(16,6) | Y |  |
| 6 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 7 | ACCEPTED_QTY | 验收数量 | number(16,6) | Y |  |
| 8 | INSPECTION_RETURN_QTY | 验退数量 | number(16,6) | Y |  |
| 9 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 10 | REQUEST_PACKING_QTY1 | 申请大包装数量 | number(16,6) | Y |  |
| 11 | REQUEST_PACKING_QTY2 | 申请中包装数量 | number(16,6) | Y |  |
| 12 | REQUEST_PACKING_QTY3 | 申请小包装数量 | number(16,6) | Y |  |
| 13 | REQUEST_PACKING_QTY4 | 申请最小包装数量 | number(16,6) | Y |  |
| 14 | REQUEST_PACKING_QTY | 申请包装数量描述 | string(240) | Y |  |
| 15 | SECOND_QTY | 第二单位申请数量 | number(16,6) | Y |  |
| 16 | REQUEST_INVENTORY_QTY | 申请库存数量 | number(16,6) | Y |  |
| 17 | URGENT | 急料 | number(0/1) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | RECEIPT_QTY | 入库数量 | number(16,6) | Y |  |
| 20 | CONCESSION_QTY | 特采量 | number(16,6) | Y |  |
| 21 | QUALIFIED_BUSINESS_QTY | 合格业务数量 | number(16,6) | Y |  |
| 22 | UNQUALIFIED_BUSINESS_QTY | 不合格业务数量 | number(16,6) | Y |  |
| 23 | IN_DESTROYED_BUSINESS_QTY | 检验破坏业务数量 | number(16,6) | Y |  |
| 24 | INSPECTION_STATUS | 检验状态 | string(40) | Y |  |
| 25 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 26 | MO_ID | 工单单号 | GUID | Y |  |
| 27 | ITEM_ID | 产品品号 | GUID | Y |  |
| 28 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 29 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 30 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 31 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 32 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 33 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 34 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 35 | SOURCE_MO_ID | 源工单 | GUID | Y |  |
| 36 | BIN_ID | 库位 | GUID | Y |  |
| 37 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 38 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 39 | CLOSE | 结束码 | string(40) | Y |  |
| 40 | ASSIGN_FINISH_PERSON | 指定完工人员 | GUID | Y |  |
| 41 | SCRAP_RECEIPT_QTY | 报废入库数量 | number(16,6) | Y |  |
| 42 | DESTROYED_RECEIPT_QTY | 破坏入库数量 | number(16,6) | Y |  |
| 43 | MO_PRODUCT_ID | 工单产出ID | GUID | Y |  |
| 44 | PROJECT_ID | 项目 | GUID | Y |  |
| 45 | WIP_DOCNO | WIP單號序号 | string(50) | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 54 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 55 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 56 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 57 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 58 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 59 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 60 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 61 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 62 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 63 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 64 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 65 | UDF041 | 自定义字段12 | date | Y |  |
| 66 | UDF042 | 自定义字段13 | date | Y |  |
| 67 | UDF051 | 自定义字段14 | GUID | Y |  |
| 68 | UDF052 | 自定义字段15 | GUID | Y |  |
| 69 | UDF053 | 自定义字段16 | GUID | Y |  |
| 70 | UDF054 | 自定义字段17 | GUID | Y |  |
| 71 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 72 | ApproveDate | 修改日期 | date | Y |  |
| 73 | ApproveBy | 修改人 | GUID | Y |  |
| 74 | MO_RECEIPT_REQUISTION_ID |  | GUID | Y |  |


### MO_RECEIPT_TO_ISSUE (维护入库转领料单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MO_RECEIPT_TO_ISSUE_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 入库日期 | date | Y |  |
| 8 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
| 17 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | PrintCount | 打印次数 | number | Y |  |
| 41 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 42 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 43 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 44 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |
| 47 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE_ID_ROid |  | GUID | Y |  |


### MO_RECEIPT_TO_ISSUE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | RECEIPT_REQUISTION_DOC_SEQ | 项次 | number | Y |  |
| 3 | MO_RECEIPT_TO_ISSUE_D_ID | 主键 | GUID | Y | Y |
| 4 | MO_FROM_ID | 入库工单 | GUID | Y |  |
| 5 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 6 | ITEM_ID | 产品品号 | GUID | Y |  |
| 7 | ITEM_DESCRIPTION | 品名 | string(510) | Y |  |
| 8 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 11 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 12 | BIN_ID | 库位 | GUID | Y |  |
| 13 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 14 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 15 | ACCEPTED_QTY | 允收数量 | number(16,6) | Y |  |
| 16 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 17 | ACCEPTED_PACKING_QTY1 | 允收大包装数量 | number(16,6) | Y |  |
| 18 | ACCEPTED_PACKING_QTY2 | 允收中包装数量 | number(16,6) | Y |  |
| 19 | ACCEPTED_PACKING_QTY3 | 允收小包装数量 | number(16,6) | Y |  |
| 20 | ACCEPTED_PACKING_QTY4 | 允收最小包装数量 | number(16,6) | Y |  |
| 21 | ACCEPTED_PACKING_QTY | 允收包装数量描述 | string(240) | Y |  |
| 22 | SECOND_QTY | 第二单位验收数量 | number(16,6) | Y |  |
| 23 | ACCEPTED_INVENTORY_QTY | 允收库存数量 | number(16,6) | Y |  |
| 24 | SCRAPED_QTY | 已报废数量 | number(16,6) | Y |  |
| 25 | EFFECTIVE_DATE | 有效日期 | date | Y |  |
| 26 | REINSEPCTION_DATE | 复验日期 | date | Y |  |
| 27 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 28 | PRODUCTION_DATE | 生产日期 | date | Y |  |
| 29 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 30 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 31 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 32 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 33 | MO_PRODUCT_ID | 工单产出ID | GUID | Y |  |
| 34 | SCRAP_SECOND_QTY | 报废第二数量 | number(16,6) | Y |  |
| 35 | DESTROYED_SECOND_QTY | 破坏第二数量 | number(16,6) | Y |  |
| 36 | PROJECT_ID | 项目 | GUID | Y |  |
| 37 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 38 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 39 | MO_RECEIPT_ID | 生产入库单 | GUID | Y |  |
| 40 | REMARK | 备注 | string(510) | Y |  |
| 41 | MO_RECEIPT_REQUISTION_D_ID | 入库申请单单号 | GUID | Y |  |
| 42 | SOURCE_MO_ID | 主键 | GUID | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 50 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 51 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 52 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 53 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 54 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 55 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 56 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 57 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 58 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 59 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 60 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 61 | UDF041 | 自定义字段12 | date | Y |  |
| 62 | UDF042 | 自定义字段13 | date | Y |  |
| 63 | UDF051 | 自定义字段14 | GUID | Y |  |
| 64 | UDF052 | 自定义字段15 | GUID | Y |  |
| 65 | UDF053 | 自定义字段16 | GUID | Y |  |
| 66 | UDF054 | 自定义字段17 | GUID | Y |  |
| 67 | Version | 版本号，不要随意更改 | binary | Y |  |
| 68 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 69 | SOURCE_ID_ROid |  | GUID | Y |  |
| 70 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 71 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 72 | MO_RECEIPT_TO_ISSUE_ID |  | GUID | Y |  |


### MO_RECEIPT_TO_ISSUE_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_RECEIPT_TO_ISSUE_SD_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_TYPE | 类别 | string(40) | Y |  |
| 4 | TO_MO_ID | 工单单号 | GUID | Y |  |
| 5 | ITEM_ID | 材料品号 | GUID | Y |  |
| 6 | ITEM_DESCRIPTION | 材料品名 | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION | 材料规格 | string(510) | Y |  |
| 8 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 9 | ISSUE_RECEIPT_QTY | 领退料数量 | number(16,6) | Y |  |
| 10 | ACTUAL_ISSUE_RECEIPT_QTY | 实际数量 | number(16,6) | Y |  |
| 11 | SECOND_QTY | 领料第二数量 | number(16,6) | Y |  |
| 12 | ACTUAL_SECOND_QTY | 实际第二数量 | number(16,6) | Y |  |
| 13 | INVENTORY_QTY | 领料库存数量 | number(16,6) | Y |  |
| 14 | ACTUAL_INVENTORY_QTY | 实际库存数量 | number(16,6) | Y |  |
| 15 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 16 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 17 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 18 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 19 | ACTUAL_PACKING_QTY1 | 实际大包装数量 | number(16,6) | Y |  |
| 20 | ACTUAL_PACKING_QTY2 | 实际中包装数量 | number(16,6) | Y |  |
| 21 | ACTUAL_PACKING_QTY3 | 实际小包装数量 | number(16,6) | Y |  |
| 22 | ACTUAL_PACKING_QTY4 | 实际最小包装数量 | number(16,6) | Y |  |
| 23 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 24 | VMI_SETTLED | VMI结算码 | string(40) | Y |  |
| 25 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 26 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 27 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 28 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 29 | PACKING4_UNIT_ID | 最小包装方式 | GUID | Y |  |
| 30 | ITEM_FEATURE_ID | 材料特征码 | GUID | Y |  |
| 31 | UNIT_ID | 单位 | GUID | Y |  |
| 32 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 33 | OPERATION_ID | 工艺 | GUID | Y |  |
| 34 | BIN_ID | 库位 | GUID | Y |  |
| 35 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 36 | ISSUE_RECEIPT_ID | 领料单 | GUID | Y |  |
| 37 | REPLACED_QTY | 被替代数量 | number(16,6) | Y |  |
| 38 | MO_D_ID | 工单单身 | GUID | Y |  |
| 39 | BC_CHECK_STATUS | 检核码 | string(40) | Y |  |
| 40 | REPLACED_MO_D_ID | 被取替代工单单身 | GUID | Y |  |
| 41 | PROJECT_ID | 项目 | GUID | Y |  |
| 42 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 43 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 44 | REMARK | 备注 | string(510) | Y |  |
| 45 | ISSUE_COMMENT | 领料说明 | string(510) | Y |  |
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 53 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 54 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 55 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 56 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 57 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 58 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 59 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 60 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 61 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 62 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 63 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 64 | UDF041 | 自定义字段12 | date | Y |  |
| 65 | UDF042 | 自定义字段13 | date | Y |  |
| 66 | UDF051 | 自定义字段14 | GUID | Y |  |
| 67 | UDF052 | 自定义字段15 | GUID | Y |  |
| 68 | UDF053 | 自定义字段16 | GUID | Y |  |
| 69 | UDF054 | 自定义字段17 | GUID | Y |  |
| 70 | Version | 版本号，不要随意更改 | binary | Y |  |
| 71 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 72 | SOURCE_ID_ROid |  | GUID | Y |  |
| 73 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 74 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 75 | ISSUE_DESTINATION_RTK |  | string(400) | Y |  |
| 76 | ISSUE_DESTINATION_ROid |  | GUID | Y |  |
| 77 | MO_RECEIPT_TO_ISSUE_D_ID |  | GUID | Y |  |


### MO_ROUTING (工单工艺信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MO_ROUTING_ID | 主键 | GUID | Y | Y |
| 4 | GRAPHIC_ATTRIBUTE | 图形属性 | binary |  |  |
| 5 | MO_ID | 工单 | GUID | Y |  |
| 6 | DOC_ID | 单据性质 | GUID | Y |  |
| 7 | GRAPHIC_ATTRIBUTE_XML | 图形属性 | string | Y |  |
| 8 | Version | 版本号，不要随意更改 | binary | Y |  |
| 9 | PrintCount | 打印次数 | number | Y |  |
| 10 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 11 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 12 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 13 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 22 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 23 | ApproveDate | 修改日期 | date | Y |  |
| 24 | ApproveBy | 修改人 | GUID | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |
| 45 | LEAST_GIO_TIME | 最近投产时间 | date | Y |  |


### MO_ROUTING_D (工单工艺单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_ROUTING_D_ID | 主键 | GUID | Y | Y |
| 3 | OPERATION_SEQ | 工序 | string(20) | Y |  |
| 4 | CHARACTER | 性质 | string(40) | Y |  |
| 5 | STANDARD_MACHINE_HOUR | 标准机时(秒) | number | Y |  |
| 6 | ACT_MACHINE_HOURS | 实际机时(秒) | number | Y |  |
| 7 | STANDARD_MAN_HOUR | 标准人时(秒) | number | Y |  |
| 8 | ACT_MAN_HOURS | 实际人时(秒) | number | Y |  |
| 9 | FIXED_LEAD_TIME | 固定前置天数 | number(7,3) | Y |  |
| 10 | DYNAMIC_LEAD_TIME | 变动前置天数 | number(7,3) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SPLIT_MERGE | 拆并方式 | string(40) | Y |  |
| 13 | POSITION_FLAG | 起讫标记 | string(40) | Y |  |
| 14 | OPERATION_COMMENT | 工艺说明 | string(510) | Y |  |
| 15 | CONVERSION_RATE | 转换率 | number(16,6) | Y |  |
| 16 | DENOMINATOR | 底数 | number | Y |  |
| 17 | RECEIPT_OVERRUN_RATE | 超入率 | number(5,4) | Y |  |
| 18 | HOUR_BATCH_QTY | 工时批量 | number | Y |  |
| 19 | PIECE_PRICE | 计件单价 | number(23,8) | Y |  |
| 20 | LABOR_RATIO | 工时工资率 | number(16,6) | Y |  |
| 21 | LAGGED_TIME | 落后天数 | number(7,3) | Y |  |
| 22 | TRANSFER_BATCH_QTY |  | number | Y |  |
| 23 | ISSUED_QTY | 正常投入 | number(16,6) | Y |  |
| 24 | REWORK_ISSUE_QTY | 返工投入 | number(16,6) | Y |  |
| 25 | TO_CHECK_IN_QTY | 待上线量(作废) | number(16,6) | Y |  |
| 26 | SKIP_TRANSFER_QTY | 跳站转出(作废) | number(16,6) | Y |  |
| 27 | PLAN_START_DATE | 预计开工日期 | date | Y |  |
| 28 | PLAN_COMPLETE_DATE | 预计完工日期 | date | Y |  |
| 29 | ACT_START_DATE | 实际开工日期 | date | Y |  |
| 30 | ACT_COMPLETE_DATE | 实际开工日期 | date | Y |  |
| 31 | WORK_CENTER_CONSTRAIN | 工作中心约束 | number(0/1) | Y |  |
| 32 | TRANSFER_IN_QTY | 投入调整量 | number(16,6) | Y |  |
| 33 | TRANSFER_OUT_QTY | 转出调整量 | number(16,6) | Y |  |
| 34 | TO_ISSUE_QTY | 待投入量 | number(16,6) | Y |  |
| 35 | PRE_PROCESSING_UNIT_ID | 加工前单位 | GUID | Y |  |
| 36 | AFTER_PROCESSING_UNIT_ID | 加工后单位 | GUID | Y |  |
| 37 | OPERATION_ID | 主键 | GUID | Y |  |
| 38 | INSPECT_MODE | 质检模式 | string(40) | Y |  |
| 39 | AUTO_DECIDE | 自动判定 | number(0/1) | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 51 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 52 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 53 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 54 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 55 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 56 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 57 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 58 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 59 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 60 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 61 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 62 | UDF041 | 自定义字段12 | date | Y |  |
| 63 | UDF042 | 自定义字段13 | date | Y |  |
| 64 | UDF051 | 自定义字段14 | GUID | Y |  |
| 65 | UDF052 | 自定义字段15 | GUID | Y |  |
| 66 | UDF053 | 自定义字段16 | GUID | Y |  |
| 67 | UDF054 | 自定义字段17 | GUID | Y |  |
| 68 | MO_ROUTING_ID |  | GUID | Y |  |
| 69 | DISPATCHED_QTY | 派工数量 | number(16,6) | Y |  |
| 70 | COLLECT_QTY | 报工数量 | number(16,6) | Y |  |


### MO_ROUTING_DISPATCH (工单工艺派工信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MO_ROUTING_DISPATCH_ID | 主键 | GUID | Y | Y |
| 7 | DISPATCH_DATE | 派工日期 | date | Y |  |
| 8 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | DISPATCH_SEQ | 序号 | number | Y |  |
| 11 | CATEGORY | 单据性质 | string(40) | Y |  |
| 12 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 13 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 14 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 15 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 16 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 17 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 18 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 19 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 20 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 21 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 22 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 23 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 24 | UDF041 | 自定义字段12 | date | Y |  |
| 25 | UDF042 | 自定义字段13 | date | Y |  |
| 26 | UDF051 | 自定义字段14 | GUID | Y |  |
| 27 | UDF052 | 自定义字段15 | GUID | Y |  |
| 28 | UDF053 | 自定义字段16 | GUID | Y |  |
| 29 | UDF054 | 自定义字段17 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | PrintCount | 打印次数 | number | Y |  |
| 32 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 33 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 34 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 35 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | ORDER_BY | 排序方式 | string(40) | Y |  |
| 50 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE_ID_ROid |  | GUID | Y |  |


### MO_ROUTING_DISPATCH_D (工单工艺派工信息明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_ROUTING_DISPATCH_D_ID | 主键 | GUID | Y | Y |
| 3 | MO_ROUTING_D_ID | 工单工艺 | GUID | Y |  |
| 4 | DISPATCH_QTY | 派工数量 | number(16,6) | Y |  |
| 5 | MACHINE_ID | 机器 | GUID | Y |  |
| 6 | WORK_TEAM_ID | 班组 | GUID | Y |  |
| 7 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 8 | DISPATCH_MACHINE_HOUR | 派工机时 | number | Y |  |
| 9 | DISPATCH_MAN_HOUR | 派工人时 | number | Y |  |
| 10 | PLAN_START_DATE | 计划开工 | date | Y |  |
| 11 | PLAN_COMPLETE_DATE | 计划完工 | date | Y |  |
| 12 | COMPLETED_QTY | 已报工数量 | number(16,6) | Y |  |
| 13 | COMPLETED_MACHINE_HOUR | 已报工机时 | number | Y |  |
| 14 | COMPLETED_MAN_HOUR | 已报工人时 | number | Y |  |
| 15 | ACTUAL_START_DATE | 实际开工 | date | Y |  |
| 16 | ACTUAL_COMPLETE_DATE | 实际完工 | date | Y |  |
| 17 | CLOSE | 结束码 | string(40) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | MO_ROUTING_DISPATCH_ID |  | GUID | Y |  |
| 48 | OPERATING_QTY | 运行量 | number(16,6) | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |


### MO_ROUTING_MATERIAL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_MATERIAL_ID | 主键 | GUID | Y | Y |
| 2 | SUM_QTY | 数量 | number(16,6) | Y |  |
| 3 | ISSUED_QTY | 已领料数量 | number(16,6) | Y |  |
| 4 | TRNSFERED_QTY | 已调拨数量 | number(16,6) | Y |  |
| 5 | SECEND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | RESERVE_ID | 预留字段1 | GUID | Y |  |
| 7 | RESERVE_QTY | 预留字段2 | number(16,6) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 15 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 16 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 17 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 18 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 19 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 20 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 21 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 22 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 23 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 24 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 25 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 26 | UDF041 | 自定义字段12 | date | Y |  |
| 27 | UDF042 | 自定义字段13 | date | Y |  |
| 28 | UDF051 | 自定义字段14 | GUID | Y |  |
| 29 | UDF052 | 自定义字段15 | GUID | Y |  |
| 30 | UDF053 | 自定义字段16 | GUID | Y |  |
| 31 | UDF054 | 自定义字段17 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | MO_ROUTING_D_ID |  | GUID | Y |  |


### MO_ROUTING_PATH (工单工艺路径信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_PATH_ID | 主键 | GUID | Y | Y |
| 2 | TO_SEQ | 工序 | string(20) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CONVERSION_RATE | 转换率 | number(16,6) | Y |  |
| 5 | DENOMINATOR | 底数 | number | Y |  |
| 6 | SUMMATION_CONVERSION_RATE | 累计转换率 | number(16,6) | Y |  |
| 7 | QTY_PER |  | number(16,6) | Y |  |
| 8 | PRE_PROCESSING_UNIT_ID | 加工前单位 | GUID | Y |  |
| 9 | AFTER_PROCESSING_UNIT_ID | 加工后单位 | GUID | Y |  |
| 10 | PATH_TYPE | 路径类型 | string(40) | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 19 | ApproveDate | 修改日期 | date | Y |  |
| 20 | ApproveBy | 修改人 | GUID | Y |  |
| 21 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 22 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 23 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 24 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 25 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 26 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 27 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 28 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 29 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 30 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 31 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 32 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 33 | UDF041 | 自定义字段12 | date | Y |  |
| 34 | UDF042 | 自定义字段13 | date | Y |  |
| 35 | UDF051 | 自定义字段14 | GUID | Y |  |
| 36 | UDF052 | 自定义字段15 | GUID | Y |  |
| 37 | UDF053 | 自定义字段16 | GUID | Y |  |
| 38 | UDF054 | 自定义字段17 | GUID | Y |  |
| 39 | MO_ROUTING_D_ID |  | GUID | Y |  |


### MO_ROUTING_PATH_WC (工单工艺路径工作中心信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_PATH_WC_ID | 主键 | GUID | Y | Y |
| 2 | COMPLETED_QTY | 完成数量 | number(16,6) | Y |  |
| 3 | BONUS_QTY | 超入量 | number(16,6) | Y |  |
| 4 | REWORK_QTY | 返工数量 | number(16,6) | Y |  |
| 5 | SKIP_TRANSFER_QTY | 跳站转出 | number(16,6) | Y |  |
| 6 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 7 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | TO_QC_QTY | 待检验量 | number(16,6) | Y |  |
| 10 | TO_DECIDE_QTY | 待判定量 | number(16,6) | Y |  |
| 11 | ACCEPTED_QTY | 允收量 | number(16,6) | Y |  |
| 12 | REJECT_QTY | 拒收量 | number(16,6) | Y |  |
| 13 | CONCESSION_QTY | 让步接受量 | number(16,6) | Y |  |
| 14 | QC_SCRAP_QTY | 检验报废量 | number(16,6) | Y |  |
| 15 | QC_DESTROYED_QTY | 检验破坏量 | number(16,6) | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 24 | ApproveDate | 修改日期 | date | Y |  |
| 25 | ApproveBy | 修改人 | GUID | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | SOURCE_ID_IN_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_IN_ROid |  | GUID | Y |  |
| 46 | SOURCE_ID_OUT_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_OUT_ROid |  | GUID | Y |  |
| 48 | MO_ROUTING_PATH_ID |  | GUID | Y |  |
| 49 | REWORK_COMPLETED_QTY | 返工完成数量 | number(16,6) | Y |  |


### MO_ROUTING_PRODUCT (工单工艺期间产出信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MO_ROUTING_PRODUCT_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | PLANT_ID | 主鍵 | GUID | Y |  |
| 8 | MO_ID | 工单 | GUID | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | PrintCount | 打印次数 | number | Y |  |
| 11 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 12 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 13 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 14 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |


### MO_ROUTING_PRODUCT_D (工单工艺期间产出信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MO_ROUTING_PRODUCT_D_ID | 主键 | GUID | Y | Y |
| 3 | MO_ROUTING_D_ID | 工单工艺 | GUID | Y |  |
| 4 | PRODUCT_TYPE | 产出类型 | number | Y |  |
| 5 | CHARACTER | 性质 | string(40) | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_NAME | 品名 | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | COMPLETED_QTY | 完成数量 | number(16,6) | Y |  |
| 11 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 12 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 15 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 16 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 17 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 18 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 19 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 20 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 21 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 22 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 23 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 24 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 25 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 26 | UDF041 | 自定义字段12 | date | Y |  |
| 27 | UDF042 | 自定义字段13 | date | Y |  |
| 28 | UDF051 | 自定义字段14 | GUID | Y |  |
| 29 | UDF052 | 自定义字段15 | GUID | Y |  |
| 30 | UDF053 | 自定义字段16 | GUID | Y |  |
| 31 | UDF054 | 自定义字段17 | GUID | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | MO_ROUTING_PRODUCT_ID |  | GUID | Y |  |


### MO_ROUTING_SUB_OPERATION (工单子工艺信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_SUB_OPERATION_ID | 主键 | GUID | Y | Y |
| 2 | SUB_OPERATION_SEQ | 子工序 | string(20) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | HOUR_BATCH_QTY | 工时批量 | number | Y |  |
| 5 | PIECE_PRICE | 计件单价 | number(23,8) | Y |  |
| 6 | LABOR_RATIO | 工时工资率 | number(16,6) | Y |  |
| 7 | STANDARD_MACHINE_HOUR | 标准机时(秒) | number | Y |  |
| 8 | ACT_MACHINE_HOUR | 实际机时(秒) | number | Y |  |
| 9 | STANDARD_MAN_HOUR | 标准人时(秒) | number | Y |  |
| 10 | ACT_MAN_HOUR | 实际人时(秒) | number | Y |  |
| 11 | SUB_OPERATION_ID | 子工艺 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 20 | ApproveDate | 修改日期 | date | Y |  |
| 21 | ApproveBy | 修改人 | GUID | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | MO_ROUTING_D_ID |  | GUID | Y |  |
| 41 | COLLECT_QTY | 报工数量 | number(16,6) | Y |  |


### MO_ROUTING_WIP (工单工艺工作中心生产信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_WIP_ID | 主键 | GUID | Y | Y |
| 2 | TO_CHECK_IN_QTY | 待上线量 | number(16,6) | Y |  |
| 3 | TO_CHECK_OUT_QTY | 待下线量 | number(16,6) | Y |  |
| 4 | TO_TRANSFER_QTY | 待转移量 | number(16,6) | Y |  |
| 5 | TO_QC_QTY | 待检验量 | number(16,6) | Y |  |
| 6 | COMPLETED_QTY | 完成数量 | number(16,6) | Y |  |
| 7 | BONUS_QTY | 朝如数量 | number(16,6) | Y |  |
| 8 | HOLD_QTY | 暂存数量 | number(16,6) | Y |  |
| 9 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 10 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 11 | REJECT_QTY | 验退数量 | number(16,6) | Y |  |
| 12 | INVENTORY_PROFIT_LOSS_QTY | 盘盈亏量 | number(16,6) | Y |  |
| 13 | CONCESSION_QTY | 特采量 | number(16,6) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | ISSUED_QTY | 投入量 | number(16,6) | Y |  |
| 16 | TRANSFER_IN_QTY | 投入调整量 | number(16,6) | Y |  |
| 17 | TRANSFER_OUT_QTY | 转出调整量 | number(16,6) | Y |  |
| 18 | QUALIFIED_BUSINESS_QTY | 合格业务数量 | number(16,6) | Y |  |
| 19 | UNQUALIFIED_BUSINESS_QTY | 不合格业务数量 | number(16,6) | Y |  |
| 20 | IN_DESTROYED_BUSINESS_QTY | 检验破坏业务数量 | number(16,6) | Y |  |
| 21 | INSPECTION_STATUS | 检验状态 | string(40) | Y |  |
| 22 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 23 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 24 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 25 | PRICE | 采购单价 | number(23,8) | Y |  |
| 26 | SKIP_TRANSFER_QTY | 跳站转出 | number(16,6) | Y |  |
| 27 | REWORK_QTY | 返工数量 | number(16,6) | Y |  |
| 28 | CURRENCY_ID | 币种 | GUID | Y |  |
| 29 | ACT_START_DATETIME | 实际开工时间 | date | Y |  |
| 30 | ACT_COMPLETE_DATETIME | 实际完工时间 | date | Y |  |
| 31 | PLAN_COMPLETE_DATE | 预计完工日期 | date | Y |  |
| 32 | TO_DECIDE_QTY | 待判定量 | number(16,6) | Y |  |
| 33 | ACCEPTED_QTY | 允收量 | number(16,6) | Y |  |
| 34 | QC_SCRAP_QTY | 检验报废量 | number(16,6) | Y |  |
| 35 | QC_DESTROYED_QTY | 检验破坏量 | number(16,6) | Y |  |
| 36 | TO_DISPATCH_QTY | 待派工量 | number(16,6) | Y |  |
| 37 | TO_ARRIVAL_QTY | 委外待收货量 | number(16,6) | Y |  |
| 38 | FIRST_CHECKIN_TIME | 最早上线时间 | date | Y |  |
| 39 | LAST_CHECKOUT_DATETIME | 最晚下线时间 | date | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 51 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 52 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 53 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 54 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 55 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 56 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 57 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 58 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 59 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 60 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 61 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 62 | UDF041 | 自定义字段12 | date | Y |  |
| 63 | UDF042 | 自定义字段13 | date | Y |  |
| 64 | UDF051 | 自定义字段14 | GUID | Y |  |
| 65 | UDF052 | 自定义字段15 | GUID | Y |  |
| 66 | UDF053 | 自定义字段16 | GUID | Y |  |
| 67 | UDF054 | 自定义字段17 | GUID | Y |  |
| 68 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 69 | SOURCE_ID_ROid |  | GUID | Y |  |
| 70 | MO_ROUTING_D_ID |  | GUID | Y |  |
| 71 | DISPATCHED_QTY | 派工数量 | number(16,6) | Y |  |
| 72 | TO_PURCHASE_RETURN_QTY | 委外待退货量 | number(16,6) | Y |  |
| 73 | REWORK_COMPLETED_QTY | 返工完成数量 | number(16,6) | Y |  |
| 74 | COLLECT_QTY | 报工数量 | number(16,6) | Y |  |
| 75 | TRANSFER_QTY | 调拨数量 | number(16,6) | Y |  |
| 76 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 77 | REWORK_ISSUED_QTY | 返工投入量 | number(16,6) | Y |  |


### MO_ROUTING_WIP_MATERIAL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_WIP_MATERIAL_ID | 主键 | GUID | Y | Y |
| 2 | SUM_QTY | 数量 | number(16,6) | Y |  |
| 3 | ISSUED_QTY | 已领料数量 | number(16,6) | Y |  |
| 4 | TRNSFERED_QTY | 已调拨数量 | number(16,6) | Y |  |
| 5 | SECEND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | RESERVE_ID | 预留字段1 | GUID | Y |  |
| 7 | RESERVE_QTY | 预留字段2 | number(16,6) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 15 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 16 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 17 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 18 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 19 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 20 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 21 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 22 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 23 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 24 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 25 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 26 | UDF041 | 自定义字段12 | date | Y |  |
| 27 | UDF042 | 自定义字段13 | date | Y |  |
| 28 | UDF051 | 自定义字段14 | GUID | Y |  |
| 29 | UDF052 | 自定义字段15 | GUID | Y |  |
| 30 | UDF053 | 自定义字段16 | GUID | Y |  |
| 31 | UDF054 | 自定义字段17 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | MO_ROUTING_D_ID |  | GUID | Y |  |


### MO_ROUTING_WORK_CENTER (工单工艺工作中心约束)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MO_ROUTING_WORK_CENTER_ID | 主键 | GUID | Y | Y |
| 2 | MAIN_STATION | 主要 | number(0/1) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | Version | 版本号，不要随意更改 | binary | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 12 | ApproveDate | 修改日期 | date | Y |  |
| 13 | ApproveBy | 修改人 | GUID | Y |  |
| 14 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 15 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 16 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 17 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 18 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 19 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 20 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 21 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 22 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 23 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 24 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 25 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 26 | UDF041 | 自定义字段12 | date | Y |  |
| 27 | UDF042 | 自定义字段13 | date | Y |  |
| 28 | UDF051 | 自定义字段14 | GUID | Y |  |
| 29 | UDF052 | 自定义字段15 | GUID | Y |  |
| 30 | UDF053 | 自定义字段16 | GUID | Y |  |
| 31 | UDF054 | 自定义字段17 | GUID | Y |  |
| 32 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 33 | SOURCE_ID_ROid |  | GUID | Y |  |
| 34 | MO_ROUTING_D_ID |  | GUID | Y |  |
| 35 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |


### MO_SPLIT (工单拆分)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PrintCount | 打印次数 | number | Y |  |
| 4 | MO_SPLIT_ID | 主键 | GUID | Y | Y |
| 5 | SPLIT_SEQ | 拆分流水号 | string(22) | Y |  |
| 6 | SPLIT_DATE | 拆分日期 | date | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | MO_SPLIT_QTY | 可拆分数量 | number(16,6) | Y |  |
| 9 | NEW_PLAN_START_DATE | 新预计开工日期 | date | Y |  |
| 10 | NEW_PLAN_COMPLETE_DATE | 新预计完工日期 | date | Y |  |
| 11 | NEW_PLANNED_QTY | 新预计产量 | number(16,6) | Y |  |
| 12 | NEW_MO_ID | 新工单单号 | string(40) | Y |  |
| 13 | MO_ID | 工单单号 | GUID | Y |  |
| 14 | NEW_MO_DOC_ID | 新单据类型 | GUID | Y |  |
| 15 | ADMIN_UNIT_ID | 新生产部门 | GUID | Y |  |
| 16 | ITEM_LOT_ID | 生产批号 | GUID | Y |  |
| 17 | DOC_ID | 主键 | GUID | Y |  |
| 18 | PLAN_SECOND_QTY | 预计产量第二数量 | number(16,6) | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | Attachments | 附件 | string | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |
| 51 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 52 | SOURCE_ID_ROid |  | GUID | Y |  |
