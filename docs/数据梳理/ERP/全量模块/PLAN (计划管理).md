---
module: "PLAN"
name_zh: "计划管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 9
columns: 440
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# PLAN (计划管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 9 | Columns: 440

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[BOM (物料清单)|BOM (物料清单)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **PLAN_BOM (计划BOM)**
- **PLAN_BOM_D (计划BOM单身)**
- **PLAN_D (设备维护项目)**
- **PLAN_DISPLAY_COLOR**
- **PLAN_DISTRIBUTION (配送任务)**
- **PLAN_MAT (设备维护料件需求)**
- **PLAN_STRATEGY (规划策略单头信息)**
- **PLAN_STRATEGY_D (规划策略MPS资源信息)**


---


---


> Tables: 9

### PLAN (维护设备维护方案)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PLAN_ID | 主键 | GUID | Y | Y |
| 4 | PLAN_CODE | 维护方案编号 | string(80) | Y |  |
| 5 | PLAN_NAME | 维护方案名称 | string(160) | Y |  |
| 6 | PLAN_LEVEL | 维护级别 | string(40) | Y |  |
| 7 | REF_WORKHOURS | 参考作业时数 | number | Y |  |
| 8 | SUIT_EQT | 适用设备说明 | string(510) | Y |  |
| 9 | SHUTDOWN | 停机 | number(0/1) | Y |  |
| 10 | REF_SHUTDOWN_HOURS | 参考停机时数 | number | Y |  |
| 11 | EQT_PERIOD_ID | 周期 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 38 | Attachments | 附件 | string | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |

### PLAN_BOM (计划BOM)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PLAN_BOM_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_ID | 计划主件 | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | Attachments | 附件 | string | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |

### PLAN_BOM_D (计划BOM单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PLAN_BOM_D_ID | 主键 | GUID | Y | Y |
| 3 | PLAN_RATE | 计划比率 | number(5,4) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_ID | 计划元件 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 元件特征码 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | PLAN_BOM_ID |  | GUID | Y |  |

### PLAN_D (设备维护项目)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PLAN_D_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 维护项目 | GUID | Y |  |
| 4 | CONTENT | 维护内容 | string(160) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | PLAN_ID |  | GUID | Y |  |

### PLAN_DISPLAY_COLOR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PLAN_DISPLAY_COLOR_ID | 主键 | GUID | Y | Y |
| 2 | DISPLAY_COLOR | 生产计划条形图颜色 | string(14) | Y |  |
| 3 | PLANT_ID | 工厂 | GUID | Y |  |
| 4 | PrintCount | 打印次数 | number | Y |  |
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
| 29 | Attachments | 附件 | string | Y |  |
| 30 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 36 | SOURCE_ID_ROid |  | GUID | Y |  |

### PLAN_DISTRIBUTION (配送任务)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SequenceNumber |  | number | Y |  |
| 7 | PLAN_DISTRIBUTION_ID | 主键 | GUID | Y | Y |
| 8 | CATEGORY | 单据性质 | string(40) | Y |  |
| 9 | PLAN_DISTRIBUTION_DATE | 预计配送日期 | date | Y |  |
| 10 | DIRECTOR | 直供发起方 | GUID | Y |  |
| 11 | ITEM_ID | 品号 | GUID | Y |  |
| 12 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 13 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 14 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 15 | FROM_WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 16 | FROM_BIN_ID | 发货库位 | GUID | Y |  |
| 17 | LOGISTICS_QTY | 物流数量 | number(16,6) | Y |  |
| 18 | SORTING_QTY | 已分货量 | number(16,6) | Y |  |
| 19 | DISTRIBUTION_QTY | 已转配送量 | number(16,6) | Y |  |
| 20 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 21 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 22 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 23 | PLAN_DELIVERY_DATE | 预交货日期 | date | Y |  |
| 24 | PRIORITY_DISTRIBUTION | 配送优先级 | string(10) | Y |  |
| 25 | TEMP_DISTRIBUTION | 临时配送 | number(0/1) | Y |  |
| 26 | CONT_MAN | 订货人 | string(20) | Y |  |
| 27 | CONT_TEL | 联系电话 | string(40) | Y |  |
| 28 | RECEIVE_ADDR | 收货地址 | string(510) | Y |  |
| 29 | CLOSED | 结束码 | string(40) | Y |  |
| 30 | LAST_INVENTORY_QTY | 余量库存单位数量 | number(16,6) | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | FEATURE_VALUE | 物流分类 | string(120) | Y |  |
| 33 | DRP_CODE | DRP计划 | string(40) | Y |  |
| 34 | PrintCount | 打印次数 | number | Y |  |
| 35 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 36 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 37 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 38 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | CreateDate | 创建日期 | date | Y |  |
| 58 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 59 | ModifiedDate | 修改日期 | date | Y |  |
| 60 | CreateBy | 创建者 | GUID | Y |  |
| 61 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 62 | ModifiedBy | 修改者 | GUID | Y |  |
| 63 | Attachments | 附件 | string | Y |  |
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |
| 69 | Owner_Org_RTK |  | string(400) | Y |  |
| 70 | Owner_Org_ROid |  | GUID | Y |  |
| 71 | DISTRIBUTION_OBJECT_RTK |  | string(400) | Y |  |
| 72 | DISTRIBUTION_OBJECT_ROid |  | GUID | Y |  |
| 73 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 74 | SOURCE_ID_ROid |  | GUID | Y |  |

### PLAN_MAT (设备维护料件需求)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PLAN_MAT_ID | 主键 | GUID | Y | Y |
| 3 | DEMAND_TYPE | 需求料件类型 | string(40) | Y |  |
| 4 | INSTRUCTION | 料件需求说明 | string(510) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_NAME | 品名 | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | UNIT_ID | 业务单位 | GUID | Y |  |
| 10 | QTY | 业务数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | PLAN_ID |  | GUID | Y |  |

### PLAN_STRATEGY (规划策略单头信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PLAN_STRATEGY_ID | 主键 | GUID | Y | Y |
| 4 | PLAN_STRATEGY_CODE | 编号 | string(40) | Y |  |
| 5 | PLAN_STRATEGY_NAME | 名称 | string(120) | Y |  |
| 6 | STRATEGY_MODE | 规划模式 | string(40) | Y |  |
| 7 | MPS_STATUS | MPS状态 | string(40) | Y |  |
| 8 | MRP_STATUS | MRP状态 | string(40) | Y |  |
| 9 | MDS_LEVEL | 是否启动MDS | number(0/1) | Y |  |
| 10 | MPS_LEVEL | 是否启动MPS | number(0/1) | Y |  |
| 11 | MRP_LEVEL | 是否启动MRP | number(0/1) | Y |  |
| 12 | MDS_OFFSET_RULE | 冲销原则 | string(40) | Y |  |
| 13 | MDS_DEMAND_TIME_FENCE | 需求栅栏 | number | Y |  |
| 14 | MDS_DEMAND_PRIORITY_ORDER | 项目优先序 | string(12) | Y |  |
| 15 | MDS_DEMAND_TYPE | 来源优先序 | string(40) | Y |  |
| 16 | MPS_DEMAND_SOURCE | 需求来源 | string(40) | Y |  |
| 17 | MPS_FORECAST_ALLOCATION | 预测分配 | string(40) | Y |  |
| 18 | MPS_MO_ALLOCATION | 在制工单计算方式 | string(40) | Y |  |
| 19 | MPS_TRANSFER_LOT_FLAG | 考虑移转批量 | number(0/1) | Y |  |
| 20 | MPS_ATTRITION_RATE_FLAG | 考虑损耗率 | number(0/1) | Y |  |
| 21 | MPS_REPLACE_FLAG | 考虑取代料 | number(0/1) | Y |  |
| 22 | MPS_ALTERNATIVE_FLAG | 考虑替代料 | number(0/1) | Y |  |
| 23 | MPS_REQUIREMENT_CALCULATION | 需求计算方式 | string(40) | Y |  |
| 24 | MPS_SCHEDULING_STRATEGY | 排程策略 | string(40) | Y |  |
| 25 | MPS_LEAD_TIME | 提前天数 | number | Y |  |
| 26 | MRP_TIME_BUCKET | 时距设定 | string(40) | Y |  |
| 27 | MRP_DEMAND_SOURCE | 需求来源 | string(40) | Y |  |
| 28 | MRP_FORECAST_ALLOCATION | 预测分配 | string(40) | Y |  |
| 29 | MRP_PROCUREMENT_PLAN | 采购计画范围 | string(40) | Y |  |
| 30 | MRP_TRANSFER_LOT_FLAG | 考虑移转批量 | number(0/1) | Y |  |
| 31 | MRP_ATTRITION_RATE_FLAG | 考虑损耗率 | number(0/1) | Y |  |
| 32 | MRP_REPLACE_FLAG | 考虑取代料 | number(0/1) | Y |  |
| 33 | MRP_ALTERNATIVE_FLAG | 考虑替代料 | number(0/1) | Y |  |
| 34 | MRP_REQUIREMENT_CALCULATION | 需求计算方式 | string(40) | Y |  |
| 35 | MRP_PRODUCTION_PLAN_FLAG | 是否生成生产计划 | number(0/1) | Y |  |
| 36 | MRP_TIME_BUCKET_ID | 时距编号 | GUID | Y |  |
| 37 | MRP_SAFT_STOCK_FLAG | 考虑安全库存 | number(0/1) | Y |  |
| 38 | REMARK | 备注 | string(510) | Y |  |
| 39 | MDS_SALES_ORDER_FLAG | 考虑銷售訂單 | number(0/1) | Y |  |
| 40 | MDS_INNER_ORDER_FLAG | 考虑內部订单 | number(0/1) | Y |  |
| 41 | MDS_FORECAST_FLAG | 考虑生產預測 | number(0/1) | Y |  |
| 42 | MDS_TRANSFER_FLAG | 考虑调拨申请单 | number(0/1) | Y |  |
| 43 | MPS_SAFT_STOCK_FLAG | 考虑安全库存 | number(0/1) | Y |  |
| 44 | CONSIDERED_LOCK_STOCK | 考虑库存锁定 | number(0/1) | Y |  |
| 45 | MPS_KEEP_ISSUED_PLANS | 保留已发放计划天数 | number | Y |  |
| 46 | MRP_KEEP_ISSUED_PLANS | 保留已发放计划天数 | number | Y |  |
| 47 | MPS_ISSUED_ZERO_PLANS | 发放需求为零的计划 | number(0/1) | Y |  |
| 48 | MRP_ISSUED_ZERO_PLANS | 发放需求为零的计划 | number(0/1) | Y |  |
| 49 | MRP_SCHEDULING_STRATEGY | 排程策略 | string(40) | Y |  |
| 50 | MPS_LOCK_RANGE | 锁定范围 | string(40) | Y |  |
| 51 | MRP_LOCK_RANGE | 锁定范围 | string(40) | Y |  |
| 52 | PLAN_TYPE | 生成计划类型 | string(40) | Y |  |
| 53 | RESERVED_PLAN_001 | 计划预留1 | string(40) | Y |  |
| 54 | RESERVED_PLAN_002 | 计划预留2 | string(40) | Y |  |
| 55 | RESERVED_PLAN_003 | 重展相依需求方式 | string(40) | Y |  |
| 56 | RESERVED_PLAN_004 | 显示/维护每日产出 | number(0/1) | Y |  |
| 57 | RESERVED_PLAN_005 | 自动重展相依需求 | number(0/1) | Y |  |
| 58 | RESERVED_PLAN_006 | 计划预留6 | string(510) | Y |  |
| 59 | RESERVED_PLAN_007 | 计划预留7 | string(510) | Y |  |
| 60 | Attachments | 附件 | string | Y |  |
| 61 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 62 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 63 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 64 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 65 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 66 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 67 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 68 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 69 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 70 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 71 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 72 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 73 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 74 | UDF041 | 自定义字段12 | date | Y |  |
| 75 | UDF042 | 自定义字段13 | date | Y |  |
| 76 | UDF051 | 自定义字段14 | GUID | Y |  |
| 77 | UDF052 | 自定义字段15 | GUID | Y |  |
| 78 | UDF053 | 自定义字段16 | GUID | Y |  |
| 79 | UDF054 | 自定义字段17 | GUID | Y |  |
| 80 | CreateDate | 创建日期 | date | Y |  |
| 81 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 82 | ModifiedDate | 修改日期 | date | Y |  |
| 83 | CreateBy | 创建者 | GUID | Y |  |
| 84 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 85 | ModifiedBy | 修改者 | GUID | Y |  |
| 86 | Version | 版本号，不要随意更改 | binary | Y |  |
| 87 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 88 | ApproveDate | 修改日期 | date | Y |  |
| 89 | ApproveBy | 修改人 | GUID | Y |  |
| 90 | Owner_Org_RTK |  | string(400) | Y |  |
| 91 | Owner_Org_ROid |  | GUID | Y |  |
| 92 | MRP_DEMAND_PRIORITY_ORDER | 需求优先序 | string(40) | Y |  |
| 93 | MRP_MANUFACTURING_PART | 自制件 | number(0/1) | Y |  |
| 94 | MRP_PROCESSING_PART | 委外加工件 | number(0/1) | Y |  |
| 95 | MRP_PURCHASING_PART | 采购件 | number(0/1) | Y |  |
| 96 | MRP_INNER_PURCHASING_PART | 内部采购件 | number(0/1) | Y |  |
| 97 | MRP_TRANSFER_PART | 调拨件 | number(0/1) | Y |  |
| 98 | MRP_ADDED_DIFFERENCE | 毛需求仅补充差额 | number(0/1) | Y |  |
| 99 | MRP_CRITICAL_ITEM_TYPE | 关键料类型 | string(40) | Y |  |
| 100 | LOCK | 全锁定 | number(0/1) | Y |  |
| 101 | FROZEN | 全冻结 | number(0/1) | Y |  |
| 102 | MRP_SAFT_STOCK_PRIORITY | 安全库存需求优先级 | number | Y |  |
| 103 | MPS_SAFT_STOCK_PRIORITY | 安全库存需求优先级 | number | Y |  |
| 104 | DIRECT_LOADING_DATA | 维护作业直接加载数据 | number(0/1) | Y |  |
| 105 | PLAN_SYNC_MODE | 计划同步每日产量方式 | string(40) | Y |  |
| 106 | INTERNAL_ITEM_PLAN |  | number(0/1) | Y |  |

### PLAN_STRATEGY_D (规划策略MPS资源信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PLAN_STRATEGY_D_ID | GUID | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | RESOURCE_ID | 资源编号 | GUID | Y |  |
| 4 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 5 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 6 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 7 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 8 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 9 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 10 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 11 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 12 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 13 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 14 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 15 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 16 | UDF041 | 自定义字段12 | date | Y |  |
| 17 | UDF042 | 自定义字段13 | date | Y |  |
| 18 | UDF051 | 自定义字段14 | GUID | Y |  |
| 19 | UDF052 | 自定义字段15 | GUID | Y |  |
| 20 | UDF053 | 自定义字段16 | GUID | Y |  |
| 21 | UDF054 | 自定义字段17 | GUID | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | PLAN_STRATEGY_ID |  | GUID | Y |  |