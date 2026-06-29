---
module: "CHANGE"
name_zh: "变更执行"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 436
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# CHANGE (变更执行)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 8 | Columns: 436

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[BOM (物料清单)|BOM (物料清单)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **CHANGE_EXEC (变更处理)**
- **CHANGE_EXEC_ITEM (元件变更信息)**
- **CHANGE_EXEC_NEW (变更处理新件处理)**
- **CHANGE_EXEC_NEW_MO_D (变更处理新件工单单身用料信息)**
- **CHANGE_EXEC_OLD (变更处理旧件处理)**
- **CHANGE_EXEC_OLD_MO_D (变更处理旧件工单单身用料信息)**
- **CHANGE_WAREHOUSE (移库单)**
- **CHANGE_WAREHOUSE_D (移库单单身)**


---


---


> Tables: 8

### CHANGE_EXEC (变更处理)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CHANGE_EXEC_ID | 主键 | GUID | Y | Y |
| 4 | SUPPLY_CENTER_ID | 限定采购域 | GUID | Y |  |
| 5 | PLANT_ID | 限定工单工厂 | GUID | Y |  |
| 6 | ISSUE_RETURN_DOC_ID | 自动退料单别 | GUID | Y |  |
| 7 | REMARK | 变更说明 | string(4000) | Y |  |
| 8 | MO_DOC_ID | 工单单别 | GUID | Y |  |
| 9 | PURCHASE_ORDER_DOC_ID | 采购单别 | GUID | Y |  |
| 10 | SALES_ORDER_DOC_SD_ID | 目标源单新行 | GUID | Y |  |
| 11 | CLOSE | 结束码 | string(40) | Y |  |
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
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | SOURCE_ORIGINAL_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ORIGINAL_ID_ROid |  | GUID | Y |  |
| 48 | CHANGE_DOC_SD_ID_RTK |  | string(400) | Y |  |
| 49 | CHANGE_DOC_SD_ID_ROid |  | GUID | Y |  |

### CHANGE_EXEC_ITEM (元件变更信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CHANGE_EXEC_ITEM_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_CATEGORY | 品号分类 | string(40) | Y |  |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 7 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 8 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 9 | M_ID | 主件 | GUID | Y |  |
| 10 | CATEGORY | 变更分类 | string(40) | Y |  |
| 11 | UP_LEVEL_ITEM_ID | 上阶品号 | GUID | Y |  |
| 12 | UP_LEVEL_ITEM_FEATURE_ID | 上阶特征码 | GUID | Y |  |
| 13 | QTY | 数量 | number(16,6) | Y |  |
| 14 | OLD_ITEM_ID | 品号 | GUID | Y |  |
| 15 | OLD_ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 16 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 17 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 18 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 19 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 20 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 21 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 22 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 23 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 24 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 25 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 26 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 27 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 28 | UDF041 | 自定义字段12 | date | Y |  |
| 29 | UDF042 | 自定义字段13 | date | Y |  |
| 30 | UDF051 | 自定义字段14 | GUID | Y |  |
| 31 | UDF052 | 自定义字段15 | GUID | Y |  |
| 32 | UDF053 | 自定义字段16 | GUID | Y |  |
| 33 | UDF054 | 自定义字段17 | GUID | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | CHANGE_EXEC_ID |  | GUID | Y |  |

### CHANGE_EXEC_NEW (变更处理新件处理)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CHANGE_EXEC_NEW_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | ITEM_TYPE | 元件类型 | string(40) | Y |  |
| 5 | PARENT_ITEM_ID | 上阶主件品号 | GUID | Y |  |
| 6 | PARENT_ITEM_FEATURE_ID | 上阶主件特征码 | GUID | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | ORI_REQUIRED_QTY | 原库存单位需求量 | number(16,6) | Y |  |
| 10 | REQUIRED_QTY | 确定库存单位需求量 | number(16,6) | Y |  |
| 11 | SOLUTION_TYPE | 处理建议 | string(40) | Y |  |
| 12 | STATUS | 状态 | string(40) | Y |  |
| 13 | EMPLOYEE_ID | 负责人 | GUID | Y |  |
| 14 | ORIGINAL_START_DATE | 预计开工日(旧) | date | Y |  |
| 15 | ORIGINAL_COMPLETE_DATE | 预计完工日(旧) | date | Y |  |
| 16 | START_DATE | 预计开工日/预计下单日 | date | Y |  |
| 17 | COMPLETE_DATE | 预计完工日/预计到货日 | date | Y |  |
| 18 | REMARK | 备注 | string(2000) | Y |  |
| 19 | DOC_ID | 单别 | GUID | Y |  |
| 20 | ORI_BUSINESS_QTY | 原业务单位需求量 | number(16,6) | Y |  |
| 21 | BUSINESS_QTY | 确定业务单位需求量 | number(16,6) | Y |  |
| 22 | UNIT_ID | 库存单位 | GUID | Y |  |
| 23 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 24 | ADMIN_UNIT_ID | 负责人部门 | GUID | Y |  |
| 25 | CHECK | 选择 | number(0/1) | Y |  |
| 26 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 27 | ITEM_ROUTING_ID | 工艺路线 | GUID | Y |  |
| 28 | PURCHASE_ORDER_D_ID | 委外采购单 | GUID | Y |  |
| 29 | PO_CHANGE_D_ID | 委外采购变更单 | GUID | Y |  |
| 30 | OUT_PURCHASE_ORDER_DOC_ID | 委外采购单别 | GUID | Y |  |
| 31 | PO_CHANGE_TYPE | 采购变更类型 | string(40) | Y |  |
| 32 | PMC_STATUS | 任务执行状态 | string(40) | Y |  |
| 33 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 34 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 35 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 36 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 37 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 38 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 39 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 40 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 41 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 42 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 43 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 44 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 45 | UDF041 | 自定义字段12 | date | Y |  |
| 46 | UDF042 | 自定义字段13 | date | Y |  |
| 47 | UDF051 | 自定义字段14 | GUID | Y |  |
| 48 | UDF052 | 自定义字段15 | GUID | Y |  |
| 49 | UDF053 | 自定义字段16 | GUID | Y |  |
| 50 | UDF054 | 自定义字段17 | GUID | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 59 | ApproveDate | 修改日期 | date | Y |  |
| 60 | ApproveBy | 修改人 | GUID | Y |  |
| 61 | CHANGE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 62 | CHANGE_SOURCE_ID_ROid |  | GUID | Y |  |
| 63 | CHANGE_DOC_ID_RTK |  | string(400) | Y |  |
| 64 | CHANGE_DOC_ID_ROid |  | GUID | Y |  |
| 65 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE_ID_ROid |  | GUID | Y |  |
| 67 | CHANGE_SOURCE_D_ID_RTK |  | string(400) | Y |  |
| 68 | CHANGE_SOURCE_D_ID_ROid |  | GUID | Y |  |
| 69 | CHANGE_EXEC_ID |  | GUID | Y |  |

### CHANGE_EXEC_NEW_MO_D (变更处理新件工单单身用料信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CHANGE_EXEC_NEW_MO_D_ID | 主键 | GUID | Y | Y |
| 3 | MO_D_ID | 工单单身主键 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | REQUIRED_QTY | 需领用量 | number(16,6) | Y |  |
| 9 | UNIT_ID | 库存单位 | GUID | Y |  |
| 10 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 11 | BIN_ID | 库位 | GUID | Y |  |
| 12 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 13 | REPLACE_ITEM | 取替代方式 | string(40) | Y |  |
| 14 | UP_LEVEL_ITEM_ID | 上阶主件品号 | GUID | Y |  |
| 15 | UP_LEVEL_ITEM_FEATURE_ID | 上阶主件特征码 | GUID | Y |  |
| 16 | REPLACED_ITEM_ID | 被取替代品号 | GUID | Y |  |
| 17 | REPLACED_ITEM_FEATURE_ID | 被取替代特征码 | GUID | Y |  |
| 18 | ITEM_GROUP | 元件群组 | GUID | Y |  |
| 19 | REPLACE_GROUP | 替代群组 | GUID | Y |  |
| 20 | REQUIRED_SECOND_QTY | 需领用第二数量 | number(16,6) | Y |  |
| 21 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 22 | OPERATION_ID | 工艺 | GUID | Y |  |
| 23 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 24 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 25 | PLAN_ISSUE_DATE | 预计领料日期 | date | Y |  |
| 26 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 27 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 28 | REMARK | 备注 | string(510) | Y |  |
| 29 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 30 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 31 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 32 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 33 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 34 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 35 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 36 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 37 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 38 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 39 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 40 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 41 | UDF041 | 自定义字段12 | date | Y |  |
| 42 | UDF042 | 自定义字段13 | date | Y |  |
| 43 | UDF051 | 自定义字段14 | GUID | Y |  |
| 44 | UDF052 | 自定义字段15 | GUID | Y |  |
| 45 | UDF053 | 自定义字段16 | GUID | Y |  |
| 46 | UDF054 | 自定义字段17 | GUID | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | CHANGE_EXEC_NEW_ID |  | GUID | Y |  |

### CHANGE_EXEC_OLD (变更处理旧件处理)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CHANGE_EXEC_OLD_ID | 主键 | GUID | Y | Y |
| 3 | CHECK | 选择 | number(0/1) | Y |  |
| 4 | CHANGE_TYPE | 变更原因 | string(40) | Y |  |
| 5 | ITEM_TYPE | 元件类型 | string(40) | Y |  |
| 6 | PARENT_ITEM_ID | 上阶主件品号 | GUID | Y |  |
| 7 | PARENT_ITEM_FEATURE_ID | 上阶主件特征码 | GUID | Y |  |
| 8 | ITEM_ID | 品号 | GUID | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | ORI_REQUIRED_QTY | 原库存单位需求量 | number(16,6) | Y |  |
| 11 | REQUIRED_QTY | 新库存单位需求量 | number(16,6) | Y |  |
| 12 | CURRENT_STATUS | 目前状况 | string(40) | Y |  |
| 13 | SOLUTION_TYPE | 处理建议 | string(40) | Y |  |
| 14 | STATUS | 状态 | string(40) | Y |  |
| 15 | ORIGINAL_START_DATE | 预计开工日/预计下单日(旧) | date | Y |  |
| 16 | ORIGINAL_COMPLETE_DATE | 预计完工日/预计到货日(旧) | date | Y |  |
| 17 | START_DATE | 预计开工日/预计下单日 | date | Y |  |
| 18 | COMPLETE_DATE | 预计完工日/预计到货日 | date | Y |  |
| 19 | REMARK | 备注 | string(2000) | Y |  |
| 20 | ORI_BUSINESS_QTY | 原业务单位需求量 | number(16,6) | Y |  |
| 21 | BUSINESS_QTY | 新业务单位需求量 | number(16,6) | Y |  |
| 22 | UNIT_ID | 库存单位 | GUID | Y |  |
| 23 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 24 | COMPLETED_QTY | 已入库量 | number(16,6) | Y |  |
| 25 | PMC_STATUS | 任务执行状态 | string(40) | Y |  |
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
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | ORIGINAL_DOC_ID_RTK |  | string(400) | Y |  |
| 55 | ORIGINAL_DOC_ID_ROid |  | GUID | Y |  |
| 56 | CHANGE_DOC_ID_RTK |  | string(400) | Y |  |
| 57 | CHANGE_DOC_ID_ROid |  | GUID | Y |  |
| 58 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE_ID_ROid |  | GUID | Y |  |
| 60 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 62 | SOURCE_DOC_ID_RTK |  | string(400) | Y |  |
| 63 | SOURCE_DOC_ID_ROid |  | GUID | Y |  |
| 64 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 65 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 66 | CHANGE_EXEC_ID |  | GUID | Y |  |

### CHANGE_EXEC_OLD_MO_D (变更处理旧件工单单身用料信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CHANGE_EXEC_OLD_MO_D_ID | 主键 | GUID | Y | Y |
| 3 | MO_D_ID | 工单单身序号 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | REQUIRED_QTY | 新需求量 | number(16,6) | Y |  |
| 7 | RETURN_QTY | 需退料量 | number(16,6) | Y |  |
| 8 | SOLUTION_TYPE | 处理方法 | string(40) | Y |  |
| 9 | SOLUTION_STATUS | 处理状态 | string(40) | Y |  |
| 10 | ISSUE_RETURN_DOC_ID | 退料单别 | GUID | Y |  |
| 11 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 12 | BIN_ID | 库位 | GUID | Y |  |
| 13 | ISSUE_RECEIPT_D_ID | 退料单号 | GUID | Y |  |
| 14 | EMPLOYEE_ID | 负责人 | GUID | Y |  |
| 15 | REMARK | 备注 | string(2000) | Y |  |
| 16 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 17 | ADMIN_UNIT_ID | 负责人部门 | GUID | Y |  |
| 18 | ORIGINAL_REQUIRED_QTY | 原需求量 | number(16,6) | Y |  |
| 19 | ISCHANGE | 是否需处理 | number(0/1) | Y |  |
| 20 | OLD_ORIGINAL_REQUIRED_QTY | 原需求量 | number(16,6) | Y |  |
| 21 | OLD_ISSUED_QTY | 原已领用量 | number(16,6) | Y |  |
| 22 | ISSUED_QTY | 已领用量 | number(16,6) | Y |  |
| 23 | OLD_WAREHOUSE_ID | 原仓库 | GUID | Y |  |
| 24 | OLD_BIN_ID | 原库位 | GUID | Y |  |
| 25 | OLD_ITEM_LOT_ID | 原批号 | GUID | Y |  |
| 26 | PMC_STATUS | 任务执行状态 | string(40) | Y |  |
| 27 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 28 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 29 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 30 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 31 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 32 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 33 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 34 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 35 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 36 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 37 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 38 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 39 | UDF041 | 自定义字段12 | date | Y |  |
| 40 | UDF042 | 自定义字段13 | date | Y |  |
| 41 | UDF051 | 自定义字段14 | GUID | Y |  |
| 42 | UDF052 | 自定义字段15 | GUID | Y |  |
| 43 | UDF053 | 自定义字段16 | GUID | Y |  |
| 44 | UDF054 | 自定义字段17 | GUID | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | CHANGE_EXEC_OLD_ID |  | GUID | Y |  |

### CHANGE_WAREHOUSE (移库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | CHANGE_WAREHOUSE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OUT_DATE | 出库日期 | date | Y |  |
| 9 | SHOP_ID | 出库门店 | GUID | Y |  |
| 10 | OUT_WAREHOUSS_ID | 移出仓库 | GUID | Y |  |
| 11 | IN_WAREHOUSS_ID | 移入仓库 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | POS_ID | POS机号 | GUID | Y |  |
| 14 | CLASS_ID | 班次 | number | Y |  |
| 15 | PrintCount | 打印次数 | number | Y |  |
| 16 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 17 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 18 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 19 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |
| 52 | OUT_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 53 | OUT_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 54 | IN_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 55 | IN_COST_DOMAIN_ID_ROid |  | GUID | Y |  |

### CHANGE_WAREHOUSE_D (移库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CHANGE_WAREHOUSE_D_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | UNIT_ID | 单位 | GUID | Y |  |
| 8 | QTY |  | number(16,6) | Y |  |
| 9 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 10 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 11 | COST | 单位成本 | number(23,8) | Y |  |
| 12 | COST_AMT | 成本金额 | number(23,8) | Y |  |
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
| 39 | CHANGE_WAREHOUSE_ID |  | GUID | Y |  |