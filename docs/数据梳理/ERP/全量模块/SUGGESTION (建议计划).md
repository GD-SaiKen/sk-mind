---
module: "SUGGESTION"
name_zh: "建议计划"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 366
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# SUGGESTION (建议计划)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 366

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[BOM (物料清单)|BOM (物料清单)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]

---

## Tables


- **SUGGESTION_PLAN**
- **SUGGESTION_PLAN_BOM (供需计划单身)**
- **SUGGESTION_PLAN_DEMAND (计划需求来源)**
- **SUGGESTION_PLAN_PRODUCT (计划产出信息)**
- **SUGGESTION_PLAN_RESOURCE (生产明细信息)**
- **SUGGESTION_PLAN_TREE**


---


---


> Tables: 6

### SUGGESTION_PLAN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | Checked | 选择 | number | Y |  |
| 5 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 6 | ApproveDate | 修改日期 | date | Y |  |
| 7 | ApproveBy | 修改人 | GUID | Y |  |
| 8 | SUGGESTION_PLAN_ID | 主键 | GUID | Y | Y |
| 9 | PLAN_STRATEGY_ID | 规划策略 | GUID | Y |  |
| 10 | MDS_VERSION_TIMES | 需求版次 | string(120) | Y |  |
| 11 | PLAN_TYPE | 计划类型 | string(40) | Y |  |
| 12 | PLAN_MODE | 计划模式 | string(40) | Y |  |
| 13 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 14 | URGENT | 紧急 | number(0/1) | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 17 | DOC_DATE | 开单日 | date | Y |  |
| 18 | SUPPLY_DATE | 供给日期 | date | Y |  |
| 19 | DEMAND_DATE | 需求日期 | date | Y |  |
| 20 | PLAN_SUGGESTED_QTY | 计划建议数量 | number(16,6) | Y |  |
| 21 | QTY | 采购/生产量 | number(16,6) | Y |  |
| 22 | CURRENT_RELEASE_QTY | 本次发放数量 | number(16,6) | Y |  |
| 23 | RELEASED_QTY | 已发放数量 | number(16,6) | Y |  |
| 24 | UNIT_ID | 单位 | GUID | Y |  |
| 25 | BOM_VERSION_TIMES | BOM版次 | string(8) | Y |  |
| 26 | BOM_DATE | BOM日期 | date | Y |  |
| 27 | FROZEN_FLAG | 排程时间冻结 | number(0/1) | Y |  |
| 28 | LOCKED_FLAG | 供需关连锁定 | number(0/1) | Y |  |
| 29 | DOC_ID | 单据性质 | GUID | Y |  |
| 30 | SUPPLY_CENTER_ID | 供应中心 | GUID | Y |  |
| 31 | SUGGEST_SUPPLIER_ID | 建议供应商 | GUID | Y |  |
| 32 | TO_PLANT_ID | 主鍵 | GUID | Y |  |
| 33 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 34 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 35 | ROUTING_CONTROL | 工艺路线管理 | number(0/1) | Y |  |
| 36 | ITEM_ROUTING_ID | 工艺路线编号 | GUID | Y |  |
| 37 | DEMAND | 需求单号 | string(510) | Y |  |
| 38 | SOURCE_DEMAND_DATE | 需求日期 | date | Y |  |
| 39 | PLANNER | 计划员 | GUID | Y |  |
| 40 | REMARK | 备注 | string(510) | Y |  |
| 41 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 42 | GROUP_ITEM_ID | 品号群组 | GUID | Y |  |
| 43 | ITEM_ROUTING_CONTROL | 工艺管理 | string(40) | Y |  |
| 44 | SUGGESTION_PLAN_RESOURCE_ID | 生产明细 | GUID | Y |  |
| 45 | SUGGESTION_PLAN_BOM_ID | 相依需求 | GUID | Y |  |
| 46 | SUGGESTION_PLAN_PRODUCT_ID | 计划产出 | GUID | Y |  |
| 47 | SUGGESTION_PLAN_DEMAND_ID | 需求来源 | GUID | Y |  |
| 48 | APS_STATUS | APS状况 | string(8) | Y |  |
| 49 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 50 | KEEP_FLAG | 重新规划锁定 | number(0/1) | Y |  |
| 51 | OLD_PLAN_SUGGESTED_QTY | 原计划建议量 | number(16,6) | Y |  |
| 52 | RESERVED_PLAN_001 | 计划预留1 | string(510) | Y |  |
| 53 | RESERVED_PLAN_002 | 计划预留2 | string(510) | Y |  |
| 54 | RESERVED_PLAN_003 | 计划预留3 | string(510) | Y |  |
| 55 | RESERVED_PLAN_004 | 计划预留4 | number(0/1) | Y |  |
| 56 | RESERVED_PLAN_005 | 计划预留5 | number(0/1) | Y |  |
| 57 | RESERVED_PLAN_007 | 计划预留7 | string(40) | Y |  |
| 58 | RESERVED_PLAN_006 | 计划预留6 | string(40) | Y |  |
| 59 | PrintCount | 打印次数 | number | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 87 | Owner_Org_RTK |  | string(400) | Y |  |
| 88 | Owner_Org_ROid |  | GUID | Y |  |
| 89 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 90 | SOURCE_ID_ROid |  | GUID | Y |  |
| 91 | BOM_RATE_FIX | 领料用量 | number(16,6) | Y |  |
| 92 | BOMLEVEL | 保留字段 | number(10,0) | Y |  |
| 93 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |
| 94 | SUGGESTION_PLAN_TREE_ID | 计划底稿树 | GUID | Y |  |
| 95 | RESOURCE_ID_RTK |  | string(400) | Y |  |
| 96 | RESOURCE_ID_ROid |  | GUID | Y |  |

### SUGGESTION_PLAN_BOM (供需计划单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SUGGESTION_PLAN_BOM_ID | 主键 | GUID | Y | Y |
| 3 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 7 | SUPPLY_DEMAND_DATE | 供需日期 | date | Y |  |
| 8 | QTY | 数量 | number(16,6) | Y |  |
| 9 | UNIT_ID | 单位 | GUID | Y |  |
| 10 | REPLACE_ITEM | 取替代方式 | string(40) | Y |  |
| 11 | REPLACED_ITEM_ID | 被取替代品号 | GUID | Y |  |
| 12 | REPLACED_ITEM_FEATURE_ID | 被取替代特征码 | GUID | Y |  |
| 13 | ITEM_GROUP | 元件群组 | GUID | Y |  |
| 14 | REPLACE_GROUP | 替代群组 | GUID | Y |  |
| 15 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 16 | PARENT_ITEM_ID | 主件品号 | GUID | Y |  |
| 17 | PARENT_ITEM_FEATURE_ID | 主件品号特征码 | GUID | Y |  |
| 18 | EXTRACT_ITEM_ID | 展阶品号 | GUID | Y |  |
| 19 | EXTRACT_ITEM_FEATURE_ID | 展阶品号特征码 | GUID | Y |  |
| 20 | OPERATION_ID | 工艺 | GUID | Y |  |
| 21 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 22 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 23 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 24 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 25 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | SUGGESTION_PLAN_ID | 供需计划 | GUID | Y |  |
| 28 | LEAST_REQUIRED_QTY | 最低需求数量 | number(16,6) | Y |  |
| 29 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 30 | OLD_QTY | 原数量 | number(16,6) | Y |  |
| 31 | OLD_REPLACED_QTY | 原被替代数量 | number(16,6) | Y |  |
| 32 | OLD_SECOND_QTY | 原第二单位数量 | number(16,6) | Y |  |
| 33 | OLD_LEAST_REQUIRED_QTY | 原最低需求数量 | number(16,6) | Y |  |
| 34 | PrintCount | 打印次数 | number | Y |  |
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
| 53 | CreateDate | 创建日期 | date | Y |  |
| 54 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 55 | ModifiedDate | 修改日期 | date | Y |  |
| 56 | CreateBy | 创建者 | GUID | Y |  |
| 57 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 58 | ModifiedBy | 修改者 | GUID | Y |  |
| 59 | Attachments | 附件 | string | Y |  |
| 60 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 61 | Version | 版本号，不要随意更改 | binary | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |

### SUGGESTION_PLAN_DEMAND (计划需求来源)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SUGGESTION_PLAN_DEMAND_ID | 主键 | GUID | Y | Y |
| 3 | SUGGESTION_PLAN_ID | 供需计划 | GUID | Y |  |
| 4 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 5 | ALLOCATE_SEQ | 分配序号 | number | Y |  |
| 6 | REPLACE_SEQ | 替代序号 | number | Y |  |
| 7 | DEMAND_ORDER_ITEM_ID | 需求单据品号 | GUID | Y |  |
| 8 | DEMAND_ORDER_ITEM_FEATURE_ID | 需求单据特征码 | GUID | Y |  |
| 9 | DEMAND_ORDER_QTY | 需求单据数量 | number(16,6) | Y |  |
| 10 | DEMAND_ORDER_DATE | 需求单据需求日期 | date | Y |  |
| 11 | REPLACE_TYPE | 取替代类型 | string(40) | Y |  |
| 12 | DEMAND_DATE | 本阶需求日期 | date | Y |  |
| 13 | DEMAND_QTY | 本阶需求数量 | number(16,6) | Y |  |
| 14 | SUPPLY_QTY | 供给数量 | number(16,6) | Y |  |
| 15 | LOCKED_FLAG | 供需关连锁定 | number(0/1) | Y |  |
| 16 | ORIGINAL_ITEM_ID | 主料品号 | GUID | Y |  |
| 17 | ORIGINAL_ITEM_FEATURE_ID | 主料特征码 | GUID | Y |  |
| 18 | ORIGINAL_DEMAND_QTY | 主料需求数量 | number(16,6) | Y |  |
| 19 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 20 | DEMAND | 需求单号 | string(510) | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | PrintCount | 打印次数 | number | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | Attachments | 附件 | string | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 54 | SOURCE_ID_ROid |  | GUID | Y |  |
| 55 | NOT_RELEASE_QTY | 未发放数量 | number(16,6) | Y |  |
| 56 | UNIT_ID | 单位 | GUID | Y |  |
| 57 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |
| 58 | BOM_RATE | 组成用量 | number(16,6) | Y |  |
| 59 | PARENT_ORDER | 上阶需求单号 | string(120) | Y |  |
| 60 | BOM_RATE_FIX | 领料用量(固定) | number(16,6) | Y |  |

### SUGGESTION_PLAN_PRODUCT (计划产出信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SUGGESTION_PLAN_PRODUCT_ID | 主键 | GUID | Y | Y |
| 3 | SUGGESTION_PLAN_ID | 供需计划 | GUID | Y |  |
| 4 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 5 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | UNIT_ID | 单位 | GUID | Y |  |
| 11 | PER_QTY | 产出比例 | number(16,6) | Y |  |
| 12 | PLAN_QTY | 预计产量 | number(16,6) | Y |  |
| 13 | COST_RATE | 成本比率 | number(5,4) | Y |  |
| 14 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | PrintCount | 打印次数 | number | Y |  |
| 17 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 18 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 19 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 20 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 21 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 22 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 23 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 24 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 25 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 26 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 27 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 28 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 29 | UDF041 | 自定义字段12 | date | Y |  |
| 30 | UDF042 | 自定义字段13 | date | Y |  |
| 31 | UDF051 | 自定义字段14 | GUID | Y |  |
| 32 | UDF052 | 自定义字段15 | GUID | Y |  |
| 33 | UDF053 | 自定义字段16 | GUID | Y |  |
| 34 | UDF054 | 自定义字段17 | GUID | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |

### SUGGESTION_PLAN_RESOURCE (生产明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SUGGESTION_PLAN_RESOURCE_ID | 主键 | GUID | Y | Y |
| 3 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 4 | PRODUCTION_DATE | 生产日期 | date | Y |  |
| 5 | PRODUCTION_QTY | 生产数量 | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | SUGGESTION_PLAN_ID | 供需计划 | GUID | Y |  |
| 8 | PrintCount | 打印次数 | number | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE_ID_ROid |  | GUID | Y |  |
| 41 | FIXED_LEAD_TIME_FLAG | 固定前置标志 | number(0/1) | Y |  |

### SUGGESTION_PLAN_TREE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SUGGESTION_PLAN_TREE_ID | 主键 | GUID | Y | Y |
| 4 | PLAN_STRATEGY_CODE | 规划策略编号 | string(40) | Y |  |
| 5 | PLAN_LEVEL | 规划层级(MRP或MPS) | string(120) | Y |  |
| 6 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 7 | NODE_ID | 节点ID | string(120) | Y |  |
| 8 | PARENTID | 上阶节点 | string(120) | Y |  |
| 9 | SUGGESTION_PLAN_ID | 父主键 | GUID | Y |  |
| 10 | DEMAND_ORDER | 上阶单据编号 | string(120) | Y |  |
| 11 | SUPER_ORDER | 需求单号 | string(120) | Y |  |
| 12 | SUPPLY_TYPE | 供给类型 | string(120) | Y |  |
| 13 | EDIT_TYPE | 可编辑类型 | string(4) | Y |  |
| 14 | IN_MDS | 是否在来源 | number(0/1) | Y |  |
| 15 | SUPPLY_ORDER | 供给单号 | string(120) | Y |  |
| 16 | BOMLEVEL | 层级码 | number(10,0) | Y |  |
| 17 | BOM_RATE | 保留字段 | number(16,6) | Y |  |
| 18 | ITEM_ID | 品号 | GUID | Y |  |
| 19 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 20 | OWNER_ORG | 工厂编号 | string(12) | Y |  |
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
| 39 | PrintCount | 打印次数 | number | Y |  |
| 40 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 41 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 42 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 43 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Attachments | 附件 | string | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |