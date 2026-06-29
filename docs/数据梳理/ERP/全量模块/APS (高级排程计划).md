---
module: "APS"
name_zh: "高级排程计划"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 84
columns: 4599
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# APS (高级排程计划)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 84 | Columns: 4599

## Related Modules

- [[BOM (物料清单)|BOM (物料清单)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **APS_AGENT_LOG**
- **APS_CMT_DO_LOCK**
- **APS_CMT_INV_ALLOC**
- **APS_CMT_MO_PEG**
- **APS_CMT_OVERTIME**
- **APS_CONFIG**
- **APS_CUSTOM_REPORT_CONFIG**
- **APS_DAILY_EFFICIENCY**
- **APS_DO**
- **APS_DO_LOCK**
- **APS_GANTT_EQLOAD**
- **APS_GANTT_MODETAIL**
- **APS_GANTT_MODIFY_MO**
- **APS_GANTT_RIGHTBLOCK**
- **APS_INV_ALLOC**
- **APS_ITEM_PRODUCT**
- **APS_ITEM_WAREHOUSE_BIN**
- **APS_KERNEL_LOG**
- **APS_MENU_CONFIG**
- **APS_MENU_HIERARCHY**
- **APS_MESSAGE_CODE**
- **APS_MO**
- **APS_MO_D**
- **APS_MO_PEG**
- **APS_MO_PRODUCT**
- **APS_MO_SUB**
- **APS_MPSITEM**
- **APS_MPT_LOG (按单规划异动记录信息)**
- **APS_MPT_MAIN (按单规划主信息)**
- **APS_MPT_MAIN_BOM (按单规划相依需求信息)**
- **APS_MPT_MAIN_PEG (按单规划配置明细信息)**
- **APS_MPT_MAIN_RESOURCE (按单规划生产明细信息)**
- **APS_MPT_MAIN_SPLIT (按单规划拆单明细信息)**
- **APS_MPT_MAIN_SPLITPEG (按单规划拆单配置明细信息)**
- **APS_MULTI_LANGUAGE**
- **APS_OMP_DO**
- **APS_OMP_MO**
- **APS_OMP_MOPEG**
- **APS_OMP_PO**
- **APS_OMP_WORK_CALENDAR**
- **APS_OMP_WORK_MODEL**
- **APS_OPERATION_MASTER**
- **APS_OUT_DAILY_DO**
- **APS_OUT_DAILY_MO**
- **APS_OUT_DAILY_OP**
- **APS_OUT_DEMAND**
- **APS_OUT_DO**
- **APS_OUT_FO_DEMAND**
- **APS_OUT_INV_ALLOC**
- **APS_OUT_INVENTORY**
- **APS_OUT_ITEM_BALANCE**
- **APS_OUT_ITEM_BALANCE_D**
- **APS_OUT_MO**
- **APS_OUT_MO_D**
- **APS_OUT_MO_MATREQ**
- **APS_OUT_MO_PEG**
- **APS_OUT_MO_PROCESS**
- **APS_OUT_MO_PRODUCT**
- **APS_OUT_MOPPEG**
- **APS_OUT_MR**
- **APS_OUT_MRP**
- **APS_OUT_MRP_D**
- **APS_OUT_ORDER_PEG**
- **APS_OUT_PO**
- **APS_OUT_RECENTPR**
- **APS_OUT_SUB_SUPPLY**
- **APS_OUT_SUPPLY**
- **APS_OUT_TIMEBUCKET**
- **APS_OUT_TIMEBUCKET_D**
- **APS_OVERTIME**
- **APS_PLAN_CASE**
- **APS_PLAN_RESOURCE**
- **APS_PLAN_STRATEGY**
- **APS_PO**
- **APS_REPORT_CONFIG**
- **APS_SERVER_COMMAND_QUEUE**
- **APS_SERVER_STATUS**
- **APS_SERVER_STATUS_MAPPING**
- **APS_SFT_DISPATCH**
- **APS_TMP_DEMAND**
- **APS_TMP_DO**
- **APS_TMP_MO**
- **APS_TMP_PO**
- **APS_USER_STATUS**


---


---


> Tables: 84

### APS_AGENT_LOG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_AGENT_LOG_ID | 主键 | GUID | Y | Y |
| 2 | LOG_LEVEL | 訊息層級 | string(10) | Y |  |
| 3 | USER_ID | 使用者代號 | string(400) | Y |  |
| 4 | MESSAGE | 系統用欄位 | string(400) | Y |  |
| 5 | DESCRIPT | 訊息內容 | string(400) | Y |  |
| 6 | MODI_TIME | 維護時間 | date | Y |  |
| 7 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 8 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 9 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 10 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
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
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |

### APS_CMT_DO_LOCK

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_CMT_DO_LOCK_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 訂單編號 | string(120) | Y |  |
| 3 | ITEM_CODE | 品號 | string(210) | Y |  |
| 4 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 5 | ORDER_QTY | 訂購數量 | number(16,6) | Y |  |
| 6 | DUE_DATE | 交期 | date | Y |  |
| 7 | ORDER_TYPE | 訂單型式 | string(120) | Y |  |
| 8 | PRIORITY | 優先順序 | number | Y |  |
| 9 | LOCK_STATUS | 鎖定訊息 | string(120) | Y |  |
| 10 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 11 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 12 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |

### APS_CMT_INV_ALLOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_CMT_INV_ALLOC_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_CODE | 品號 | string(210) | Y |  |
| 3 | FED_QTY | 供給數量 | number(16,6) | Y |  |
| 4 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 5 | IS_MATERIAL | 採購件 | number | Y |  |
| 6 | ORDER_ID | 配給的對象 | string(120) | Y |  |
| 7 | WAREHOUSE_CODE | 庫別 | string(120) | Y |  |
| 8 | LOCATION | 位置 | string(120) | Y |  |
| 9 | IS_LOCK | 鎖定供需 | number | Y |  |
| 10 | IS_DEMAND_ORDER | 訂單需求 | number | Y |  |
| 11 | BIN_CODE | 庫位 | string(120) | Y |  |
| 12 | CUS_STRING1 | 保留欄位元_文字1 | string(120) | Y |  |
| 13 | CUS_STRING2 | 保留欄位元_文字2 | string(120) | Y |  |
| 14 | CUS_STRING3 | 保留欄位元_文字3 | string(120) | Y |  |
| 15 | CUS_NUMERIC1 | 保留欄位_數值1 | number | Y |  |
| 16 | CUS_NUMERIC2 | 保留欄位_數值2 | number(16,6) | Y |  |
| 17 | CUS_NUMERIC3 | 保留欄位_數值3 | number(16,6) | Y |  |
| 18 | CUS_DATE1 | 保留欄位_日期1 | date | Y |  |
| 19 | CUS_DATE2 | 保留欄位_日期2 | date | Y |  |
| 20 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 21 | ORIG_PART_ID | 原始需求品號 | string(210) | Y |  |
| 22 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 23 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 24 | SUB_TYPE | 取替代型態 | number | Y |  |
| 25 | UNIQUE_ID | 唯一碼 | string(120) | Y |  |
| 26 | REAL_FED_QTY | 實際配置數量 | number(16,6) | Y |  |
| 27 | GROUP_QTY | 供應套數 | number(16,6) | Y |  |
| 28 | SUPER_ORDER_ID | 最上階訂單號 | string(120) | Y |  |
| 29 | LOCK_STATUS | 鎖定訊息 | string(120) | Y |  |
| 30 | PEG_TYPE | 鎖定型態 | number | Y |  |
| 31 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 32 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 33 | PLAN_LEVEL | 規劃層級 | string(20) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |

### APS_CMT_MO_PEG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_CMT_MO_PEG_ID | 主键 | GUID | Y | Y |
| 2 | FED_ORDER_ID | 供給單號 | string(120) | Y |  |
| 3 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 4 | FEDED_ORDER_ID | 被供給單號 | string(120) | Y |  |
| 5 | IS_DEMAND | 訂單需求 | number | Y |  |
| 6 | FED_QTY | 供給數量 | number(16,6) | Y |  |
| 7 | IS_STOCK | 採購件 | number | Y |  |
| 8 | SUPPLY_QTY | 可供給數量 | number(16,6) | Y |  |
| 9 | IS_LOCK | 鎖定供需 | number | Y |  |
| 10 | ITEM_CODE | 品號 | string(210) | Y |  |
| 11 | REQUIRE_TIME | 需求日期 | date | Y |  |
| 12 | CUS_STRING1 | 保留欄位元_文字1 | string(120) | Y |  |
| 13 | CUS_STRING2 | 保留欄位元_文字2 | string(120) | Y |  |
| 14 | CUS_STRING3 | 保留欄位元_文字3 | string(120) | Y |  |
| 15 | CUS_NUMERIC1 | 保留欄位_數值1 | number | Y |  |
| 16 | CUS_NUMERIC2 | 保留欄位_數值2 | number(16,6) | Y |  |
| 17 | CUS_NUMERIC3 | 保留欄位_數值3 | number(16,6) | Y |  |
| 18 | CUS_DATE1 | 保留欄位_日期1 | date | Y |  |
| 19 | CUS_DATE2 | 保留欄位_日期2 | date | Y |  |
| 20 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 21 | ORIG_PART_ID | 原始需求品號 | string(210) | Y |  |
| 22 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 23 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 24 | SUB_TYPE | 取替代型態 | number | Y |  |
| 25 | UNIQUE_ID | 唯一碼 | string(120) | Y |  |
| 26 | REAL_FED_QTY | 實際配置數量 | number(16,6) | Y |  |
| 27 | GROUP_QTY | 供應套數 | number(16,6) | Y |  |
| 28 | SUPER_ORDER_ID | 最上階訂單號 | string(120) | Y |  |
| 29 | LOCK_STATUS | 鎖定訊息 | string(120) | Y |  |
| 30 | DISPATCH_STATUS | 產能鎖定訊息 | string(120) | Y |  |
| 31 | PEG_TYPE | 產能鎖定訊息 | string(120) | Y |  |
| 32 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 33 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 34 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 43 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 44 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 45 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 46 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 47 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 48 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 49 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 50 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 51 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 52 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 53 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 54 | UDF041 | 自定义字段12 | date | Y |  |
| 55 | UDF042 | 自定义字段13 | date | Y |  |
| 56 | UDF051 | 自定义字段14 | GUID | Y |  |
| 57 | UDF052 | 自定义字段15 | GUID | Y |  |
| 58 | UDF053 | 自定义字段16 | GUID | Y |  |
| 59 | UDF054 | 自定义字段17 | GUID | Y |  |
| 60 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 61 | Version | 版本号，不要随意更改 | binary | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |

### APS_CMT_OVERTIME

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_CMT_OVERTIME_ID | 主键 | GUID | Y | Y |
| 2 | IS_OUTSOURCING | 是否为外包 | number | Y |  |
| 3 | EQUIP_TYPE | 设备型态 | number | Y |  |
| 4 | RESOURCE_CODE | 资源编号 | string(120) | Y |  |
| 5 | CALENDAR_DATE | 日期 | date | Y |  |
| 6 | START_TIME | 开始时间(秒) | number | Y |  |
| 7 | END_TIME | 结束时间(秒) | number |  |  |
| 8 | OVERTIME_TYPE | 加班型态 | number |  |  |
| 9 | IS_SCHEDULED | 是否排程 | number |  |  |
| 10 | CUS_STRING1 |  | string(120) |  |  |
| 11 | CUS_STRING2 |  | string(120) |  |  |
| 12 | CUS_STRING3 |  | string(120) |  |  |
| 13 | CUS_NUMERIC1 |  | number |  |  |
| 14 | CUS_NUMERIC2 |  | number(17,6) |  |  |
| 15 | CUS_NUMERIC3 |  | number(17,6) |  |  |
| 16 | CUS_DATE1 |  | date |  |  |
| 17 | CUS_DATE2 |  | date |  |  |
| 18 | WORK_TIME | 加班/保修时间(秒) | number | Y |  |
| 19 | OWNER_ORG | 工厂 | string(120) | Y |  |
| 20 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 21 | ORIG_WORK_TIME | 原加班时间 | string(120) |  |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | Attachments | 附件 | string | Y |  |
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
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |

### APS_CONFIG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_CONFIG_ID | 主键 | GUID | Y | Y |
| 2 | KEY_ID | 參數ID | string(120) | Y |  |
| 3 | KEY_GROUP | 參數群組 | number | Y |  |
| 4 | KEY_VALUE | 參數值 | string(120) | Y |  |
| 5 | KEY_NAME | 參數名稱 | string(120) | Y |  |
| 6 | KEY_SECTION | 參數分類 | string(120) | Y |  |
| 7 | KEY_DESCRIPT | 參數說明 | string(400) | Y |  |
| 8 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 9 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 10 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 11 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
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
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |

### APS_CUSTOM_REPORT_CONFIG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_CUSTOM_REPORT_CONFIG_ID | 主键 | GUID | Y | Y |
| 2 | REPORT_ID | 系統欄位 | string(40) | Y |  |
| 3 | REPORT_SUB_ID | 系統欄位 | string(100) | Y |  |
| 4 | REPORT_GROUP | 系統欄位 | string(40) | Y |  |
| 5 | REPORT_NAME | 系統欄位 | string(400) | Y |  |
| 6 | REPORT_STYLE | 系統欄位 | number | Y |  |
| 7 | DESCRPTION | 訊息內容 | string(100) | Y |  |
| 8 | DATA_GROUP | 資料串接群組 | string(100) | Y |  |
| 9 | METADATA | 系統用欄位 | string | Y |  |
| 10 | CREATE_USER | 建立者 | string(100) | Y |  |
| 11 | CREATE_TIME | 建立時間 | date | Y |  |
| 12 | MODIFY_USER | 維護人 | string(100) | Y |  |
| 13 | MODIFY_TIME | 維護時間 | date | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |

### APS_DAILY_EFFICIENCY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_DAILY_EFFICIENCY_ID | 主键 | GUID | Y | Y |
| 2 | IS_OUTSOURCING | 外包 | number | Y |  |
| 3 | EQUIP_TYPE | 資源型態 | number | Y |  |
| 4 | RESOURCE_CODE | 資源編號 | string(120) | Y |  |
| 5 | CALENDAR_DATE | 日期 | date | Y |  |
| 6 | EFFICIENCY | 資源效率 | number(16,6) | Y |  |
| 7 | CUS_STRING1 | 保留欄位元_文字1 | string(120) | Y |  |
| 8 | CUS_STRING2 | 保留欄位元_文字2 | string(120) | Y |  |
| 9 | CUS_STRING3 | 保留欄位元_文字3 | string(120) | Y |  |
| 10 | CUS_NUMERIC1 | 保留欄位_數值1 | number | Y |  |
| 11 | CUS_NUMERIC2 | 保留欄位_數值2 | number(16,6) | Y |  |
| 12 | CUS_NUMERIC3 | 保留欄位_數值3 | number(16,6) | Y |  |
| 13 | CUS_DATE1 | 保留欄位_日期1 | date | Y |  |
| 14 | CUS_DATE2 | 保留欄位_日期2 | date | Y |  |
| 15 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 16 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 17 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 18 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
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
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |

### APS_DO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_DO_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 需求订单编号 | string(120) | Y |  |
| 3 | ITEM_CODE | 订购品项之品号 | string(120) | Y |  |
| 4 | ORDER_QTY | 订购数量 | number(16,6) | Y |  |
| 5 | DUE_DATE | 交期 | date | Y |  |
| 6 | CAN_CONSUME | 是否能被消耗（预测订单用） | number | Y |  |
| 7 | CUSTOMER_ID | 客户代号 | string(120) | Y |  |
| 8 | IS_SCHEDULED | 是否纳入排程 | number | Y |  |
| 9 | ORDER_TYPE | 订单型式 | string(120) | Y |  |
| 10 | PART_FAMILY_ID | 同一产品族的品号 | string(120) | Y |  |
| 11 | PRIORITY | 订单之优先级 | number | Y |  |
| 12 | SALE_ORDER_ID | 销售订单之编号 | string(120) | Y |  |
| 13 | CUSTOMER_ORDER_ID | 客户单号 | string(120) | Y |  |
| 14 | SHIPPED_QTY | (销)已出货量 | number(16,6) | Y |  |
| 15 | UNIT_ID | 订购产品单位 | string(120) | Y |  |
| 16 | CUSTOMER_GROUP_ID | 客户群组编号 | string(120) | Y |  |
| 17 | OWNER | 订单拥有者 | string(120) | Y |  |
| 18 | TRANSFER_RATE | 转换率 | number(16,8) | Y |  |
| 19 | ORDER_DATE | 订单开立日期 | date | Y |  |
| 20 | ALLOC_RULE_ID | 分配法则 | string(120) | Y |  |
| 21 | SHIP_DAY | 运输天数 | number | Y |  |
| 22 | CUSTOMER_PART_ID | 客户品号 | string(210) | Y |  |
| 23 | IS_NON_DELAYED | 是否严守交期 | number | Y |  |
| 24 | CUS_STRING1 |  | string(120) | Y |  |
| 25 | CUS_STRING2 |  | string(120) | Y |  |
| 26 | CUS_STRING3 |  | string(120) | Y |  |
| 27 | CUS_NUMERIC1 |  | number | Y |  |
| 28 | CUS_NUMERIC2 |  | number(16,6) | Y |  |
| 29 | CUS_NUMERIC3 |  | number(16,6) | Y |  |
| 30 | CUS_DATE1 |  | date | Y |  |
| 31 | CUS_DATE2 |  | date | Y |  |
| 32 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 33 | SPARE_QTY | 赠品或备品数量 | number(16,6) | Y |  |
| 34 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 35 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 36 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 37 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 38 | BUSINESS_QTY | 业务订购量 | number(16,0) | Y |  |
| 39 | BUSSINESS_UNIT_ID | 业务单位 | string(120) | Y |  |
| 40 | PROGRESS | 订单进度 | number(16,6) | Y |  |
| 41 | ORIG_IS_SCHEDULED | 原始规划旗标 | number | Y |  |
| 42 | ORIG_PRIORITY | 原始优先续 | number | Y |  |
| 43 | ORIG_DUE_DATE | 原始交期 | date | Y |  |
| 44 | SOURCE_ID_RTK | 来源码 | string(400) | Y |  |
| 45 | SOURCE_ID_ROid | 源单键值 | GUID | Y |  |
| 46 | NETTING_TYPE | 订单需求计算类型 | number | Y |  |
| 47 | MDS_D_ID | MDS_D_ID | GUID | Y |  |
| 48 | NETTING_TYPE_DOWN | 耗用特性继承 | number | Y |  |
| 49 | MDS_START_DATE | 沖銷起始日期 | date | Y |  |
| 50 | MDS_END_DATE | 沖銷結束日期 | date | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 59 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 60 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 61 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 62 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 63 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 64 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 65 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 66 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 67 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 68 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 69 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 70 | UDF041 | 自定义字段12 | date | Y |  |
| 71 | UDF042 | 自定义字段13 | date | Y |  |
| 72 | UDF051 | 自定义字段14 | GUID | Y |  |
| 73 | UDF052 | 自定义字段15 | GUID | Y |  |
| 74 | UDF053 | 自定义字段16 | GUID | Y |  |
| 75 | UDF054 | 自定义字段17 | GUID | Y |  |
| 76 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 77 | Version | 版本号，不要随意更改 | binary | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |

### APS_DO_LOCK

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_DO_LOCK_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 訂單編號 | string(120) | Y |  |
| 3 | ITEM_CODE | 品號 | string(210) | Y |  |
| 4 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 5 | ORDER_QTY | 訂購數量 | number(16,6) | Y |  |
| 6 | DUE_DATE | 交期 | date | Y |  |
| 7 | ORDER_TYPE | 訂單型式 | string(120) | Y |  |
| 8 | PRIORITY | 優先順序 | number | Y |  |
| 9 | LOCK_STATUS | 鎖定訊息 | string(120) | Y |  |
| 10 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 11 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 12 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 13 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 14 | IS_AUTO_LOCK | 自動鎖定 | number | Y |  |
| 15 | ORIG_PLAN_STRATEGY_CODE | 原規劃策略 | string(120) | Y |  |
| 16 | ORIG_PLAN_LEVEL | 原規劃層級 | string(120) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |

### APS_GANTT_EQLOAD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_GANTT_EQLOAD_ID | 主键 | GUID | Y | Y |
| 2 | RESOURCE_CODE | 資源編號 | string(120) | Y |  |
| 3 | OUT_DATE | 產出日 | date | Y |  |
| 4 | AVAILABLE_TIME | 可用工時 | number(16,6) | Y |  |
| 5 | OVER_TIME | 加工時間 | number(16,6) | Y |  |
| 6 | MAINTENANCE_TIME | 維護時間 | number(16,6) | Y |  |
| 7 | WIP_WORK_TIME | WIP加工時間 | number(16,6) | Y |  |
| 8 | MO_WORK_TIME | 建議生產時間 | number(16,6) | Y |  |
| 9 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 10 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 11 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 12 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |

### APS_GANTT_MODETAIL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_GANTT_MODETAIL_ID | 主键 | GUID | Y | Y |
| 2 | RESOURCE_GROUP_CODE | 資源群組 | string(120) | Y |  |
| 3 | RESOURCE_CODE | 資源編號 | string(120) | Y |  |
| 4 | OUT_DATE | 產出日 | date | Y |  |
| 5 | SKL_SEQ | 排程順序 | number | Y |  |
| 6 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 7 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 8 | PRODUCE_QTY | 生產量 | number(16,6) | Y |  |
| 9 | OUT_QTY | 產出數量 | number(16,6) | Y |  |
| 10 | PO_CONSTRAINT_DATE | 物料限制時間 | date | Y |  |
| 11 | PLAN_RELEASE_DATE | 預計發放時間 | date | Y |  |
| 12 | PLAN_COMPLETE_DATE | 預計完工時間 | date | Y |  |
| 13 | BW_COMPLETE_DATE | 理想完工日 | date | Y |  |
| 14 | ITEM_CODE | 品號 | string(210) | Y |  |
| 15 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 16 | ITEM_NAME | 品名 | string(120) | Y |  |
| 17 | PROCESS_CYCLE_TIME | 加工製造週期 | number | Y |  |
| 18 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 19 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 20 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 21 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | Attachments | 附件 | string | Y |  |
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
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |

### APS_GANTT_MODIFY_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_GANTT_MODIFY_MO_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 4 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 5 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 6 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
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
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |

### APS_GANTT_RIGHTBLOCK

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_GANTT_RIGHTBLOCK_ID | 主键 | GUID | Y | Y |
| 2 | UNIQUE_ID | 唯一碼 | string(120) | Y |  |
| 3 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 4 | OUT_DATE | 產出日 | date | Y |  |
| 5 | OUT_QTY | 產出數量 | number(16,6) | Y |  |
| 6 | EQUIP_GROUP_ID | 資源群組編號 | string(120) | Y |  |
| 7 | PART_ID | 品號 | string(210) | Y |  |
| 8 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 9 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 10 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 11 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 12 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 13 | ORDER_PARENT_ID | 上階碼 | string(120) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |

### APS_INV_ALLOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_INV_ALLOC_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_CODE | 品號 | string(210) | Y |  |
| 3 | FED_QTY | 供給數量 | number(16,6) | Y |  |
| 4 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 5 | IS_MATERIAL | 採購件 | number | Y |  |
| 6 | ORDER_ID | 配給的對象 | string(120) | Y |  |
| 7 | WAREHOUSE_CODE | 庫別 | string(120) | Y |  |
| 8 | LOCATION | 位置 | string(120) | Y |  |
| 9 | IS_LOCK | 鎖定供需 | number | Y |  |
| 10 | IS_DEMAND_ORDER | 訂單需求 | number | Y |  |
| 11 | BIN_CODE | 庫位 | string(120) | Y |  |
| 12 | CUS_STRING1 | 保留欄位元_文字1 | string(120) | Y |  |
| 13 | CUS_STRING2 | 保留欄位元_文字2 | string(120) | Y |  |
| 14 | CUS_STRING3 | 保留欄位元_文字3 | string(120) | Y |  |
| 15 | CUS_NUMERIC1 | 保留欄位_數值1 | number | Y |  |
| 16 | CUS_NUMERIC2 | 保留欄位_數值2 | number(16,6) | Y |  |
| 17 | CUS_NUMERIC3 | 保留欄位_數值3 | number(16,6) | Y |  |
| 18 | CUS_DATE1 | 保留欄位_日期1 | date | Y |  |
| 19 | CUS_DATE2 | 保留欄位_日期2 | date | Y |  |
| 20 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 21 | ORIG_PART_ID | 原始需求品號 | string(210) | Y |  |
| 22 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 23 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 24 | SUB_TYPE | 取替代型態 | number | Y |  |
| 25 | UNIQUE_ID | 唯一碼 | string(120) | Y |  |
| 26 | REAL_FED_QTY | 實際配置數量 | number(16,6) | Y |  |
| 27 | GROUP_QTY | 供應套數 | number(16,6) | Y |  |
| 28 | SUPER_ORDER_ID | 最上階訂單號 | string(120) | Y |  |
| 29 | LOCK_STATUS | 鎖定訊息 | string(120) | Y |  |
| 30 | PEG_TYPE | 鎖定型態 | number | Y |  |
| 31 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 32 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 33 | CASE_CODE | 案例代碼 | string(120) | Y |  |
| 34 | PLAN_LEVEL | 規劃層級 | string(20) | Y |  |
| 35 | ORIG_PLAN_STRATEGY_CODE | 原規劃策略 | string(120) | Y |  |
| 36 | ORIG_PLAN_LEVEL | 原案例編號 | string(120) | Y |  |
| 37 | TARGET_ITEM | 目標品項 | number | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |

### APS_ITEM_PRODUCT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_ITEM_PRODUCT_ID | 主键 | GUID | Y | Y |
| 2 | PARENT_ITEM_CODE | 主件品號 | string(210) | Y |  |
| 3 | PARENT_FEATURE_ID | 主件品號特徵碼 | string(210) | Y |  |
| 4 | ITEM_CODE | 聯副產品品號 | string(210) | Y |  |
| 5 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 6 | PRODUCT_TYPE | 產出類型 | string(120) | Y |  |
| 7 | PRODUCT_RATE | 產出比率 | number(16,6) | Y |  |
| 8 | REMARK | 備註 | string(400) | Y |  |
| 9 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 10 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 11 | CASE_CODE | 案例編號 | string(20) | Y |  |
| 12 | PLAN_LEVEL | 規劃層級 | string(20) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |

### APS_ITEM_WAREHOUSE_BIN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_ITEM_WAREHOUSE_BIN_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_CODE | 品號 | string(210) | Y |  |
| 3 | WAREHOUSE_CODE | 庫別 | string(120) | Y |  |
| 4 | BIN_CODE | 庫位 | string(120) | Y |  |
| 5 | UNALLOCATE_QTY | 未分配量 | number(16,6) | Y |  |
| 6 | LOCATION | 位置 | string(120) | Y |  |
| 7 | IS_LIMITED_BY_SR | 供給法則生效 | number | Y |  |
| 8 | CUS_STRING1 | 保留欄位元_文字1 | string(120) | Y |  |
| 9 | CUS_STRING2 | 保留欄位元_文字2 | string(120) | Y |  |
| 10 | CUS_STRING3 | 保留欄位元_文字3 | string(120) | Y |  |
| 11 | CUS_NUMERIC1 | 保留欄位_數值1 | number | Y |  |
| 12 | CUS_NUMERIC2 | 保留欄位_數值2 | number(16,6) | Y |  |
| 13 | CUS_NUMERIC3 | 保留欄位_數值3 | number(16,6) | Y |  |
| 14 | CUS_DATE1 | 保留欄位_日期1 | date | Y |  |
| 15 | CUS_DATE2 | 保留欄位_日期2 | date | Y |  |
| 16 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 17 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 18 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 19 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 20 | PLAN_LEVEL | 規劃層級 | string(20) | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Attachments | 附件 | string | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |

### APS_KERNEL_LOG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_KERNEL_LOG_ID | 主键 | GUID | Y | Y |
| 2 | LOG_MODULE | 訊息模組 | string(120) | Y |  |
| 3 | LOG_ID | 訊息代號 | number | Y |  |
| 4 | LOG_TIME | 訊息時間 | date | Y |  |
| 5 | LOG_TYPE | 訊息類型 | string(120) | Y |  |
| 6 | LOG_PHASE | 訊息階段 | string(120) | Y |  |
| 7 | OBJECT_NAME | 物件名稱 | string(120) | Y |  |
| 8 | FUNCTION_NAME | 函式名稱 | string(120) | Y |  |
| 9 | DESCRIPT | 訊息內容 | string(400) | Y |  |
| 10 | MSG_CODE | 訊息代碼 | string(120) | Y |  |
| 11 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 12 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 13 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 14 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
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
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MENU_CONFIG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MENU_CONFIG_ID | 主鍵 | GUID | Y | Y |
| 2 | MENU_ID | 選單編號 | string(40) | Y |  |
| 3 | MENU_SUB_ID | 選單次編號 | string(6) | Y |  |
| 4 | MENU_NAME | 選單名稱 | string(120) | Y |  |
| 5 | REPORT_ID | 報表編號 | string(40) | Y |  |
| 6 | REPORT_SUB_ID | 報表次編號 | string(6) | Y |  |
| 7 | CREATE_USER | 建立者 | string(100) | Y |  |
| 8 | CREATE_TIME | 建立時間 | date | Y |  |
| 9 | MODIFY_USER | 維護人 | string(100) | Y |  |
| 10 | MODIFY_TIME | 維護時間 | date | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
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
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MENU_HIERARCHY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MENU_HIERARCHY_ID | 主键 | GUID | Y | Y |
| 2 | MENU_MEMBER_ID | 系統用欄位 | string(40) | Y |  |
| 3 | P_MENU_MEMBER_ID | 系統欄位 | string(40) | Y |  |
| 4 | SEQUENCE | 順序 | number | Y |  |
| 5 | IS_OPERATION | 保留欄位 | number | Y |  |
| 6 | OPERATION_ID | 作業編號 | string(40) | Y |  |
| 7 | MEMBER_CAPTION | 系統欄位 | string(100) | Y |  |
| 8 | IS_ADD_SEPARATOR_ON_MENU | 系統欄位 | number | Y |  |
| 9 | PERMISSION_CONTROL | 系統欄位 | number | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MESSAGE_CODE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MESSAGE_CODE_ID | 主键 | GUID | Y | Y |
| 2 | MSG_ID | 訊息ID | string(120) | Y |  |
| 3 | LANGUAGE_TYPE | 語系分類 | string(120) | Y |  |
| 4 | MSG_DESCRIPT | 訊息文字 | string(400) | Y |  |
| 5 | Version | 版本号，不要随意更改 | binary | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
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
| 31 | RESERVED_001 |  | string(510) | Y |  |
| 32 | RESERVED_002 |  | string(510) | Y |  |
| 33 | RESERVED_011 |  | GUID | Y |  |
| 34 | RESERVED_012 |  | GUID | Y |  |
| 35 | RESERVED_021 |  | date | Y |  |
| 36 | RESERVED_022 |  | date | Y |  |
| 37 | RESERVED_031 |  | number(16,6) | Y |  |
| 38 | RESERVED_032 |  | number(16,6) | Y |  |
| 39 | RESERVED_041 |  | number(23,8) | Y |  |
| 40 | RESERVED_042 |  | number(23,8) | Y |  |
| 41 | RESERVED_051 |  | number(23,8) | Y |  |
| 42 | RESERVED_052 |  | number(23,8) | Y |  |
| 43 | RESERVED_061 |  | number | Y |  |
| 44 | RESERVED_062 |  | number | Y |  |
| 45 | RESERVED_071 |  | number(0/1) | Y |  |
| 46 | RESERVED_072 |  | number(0/1) | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MO_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | MFG_ORDER_ID | string(120) | Y |  |
| 3 | DEMAND_QTY | DEMAND_QTY | number(16,6) | Y |  |
| 4 | ERP_ORDER_ID | ERP_ORDER_ID | string(120) | Y |  |
| 5 | FIRM_COMPLETE_DATE | FIRM_COMPLETE_DATE | date | Y |  |
| 6 | FIRM_RELEASE_DATE | ERP预计开立日期 | date | Y |  |
| 7 | ITEM_CODE | 品号 | string(120) | Y |  |
| 8 | PRIORITY | 优先级 | number | Y |  |
| 9 | ROUTE_ID | 途程编号 | string(160) | Y |  |
| 10 | UNIT_ID | 计数单位 | string(120) | Y |  |
| 11 | MATERIAL_RELEASED | 制令是否已完全发料 | number | Y |  |
| 12 | PROJECT_ID | 计划批号 | string(120) | Y |  |
| 13 | PRODUCED_QTY | (生)已生产量 | number(16,6) | Y |  |
| 14 | SCRAP_QTY | (生)报废数量 | number(16,6) | Y |  |
| 15 | OWNER | 制令拥有者 | string(120) | Y |  |
| 16 | STATE | 制令执行状态 | number | Y |  |
| 17 | TRANSFER_RATE | 转换率 | number(16,6) | Y |  |
| 18 | SUPPLY_RULE_ID | 供给法则 | string(120) | Y |  |
| 19 | IS_FIRM | 单据是否锁定不可移动 | number | Y |  |
| 20 | CREATOR | 开立者 | string(120) | Y |  |
| 21 | PO_CONSTRAINT_DATE | 关键物料进料限制时间点 | date | Y |  |
| 22 | IS_NEW |  | number | Y |  |
| 23 | HAS_ROUTE | 是否使用制令制程数据 | number | Y |  |
| 24 | IS_OUTSOURCING | 此制令是否为外包制令 | number | Y |  |
| 25 | OUTSOURCE_ID | 外包商码 | string(120) | Y |  |
| 26 | PLAN_COMPLETE_DATE | 预计完工时间 | date | Y |  |
| 27 | PLAN_RELEASE_DATE | 预计发放时间 | date | Y |  |
| 28 | IS_LIMITED_BY_SR | 是否不受供给法则限制 | number | Y |  |
| 29 | SURPLUS_DEMAND_TYPE | 制令多余量需求建立模式 | number | Y |  |
| 30 | CUS_STRING1 |  | string(120) | Y |  |
| 31 | CUS_STRING2 |  | string(120) | Y |  |
| 32 | CUS_STRING3 |  | string(120) | Y |  |
| 33 | CUS_NUMERIC1 |  | number | Y |  |
| 34 | CUS_NUMERIC2 |  | number(16,6) | Y |  |
| 35 | CUS_NUMERIC3 |  | number(16,6) | Y |  |
| 36 | CUS_DATE1 |  | date | Y |  |
| 37 | CUS_DATE2 |  | date | Y |  |
| 38 | IS_REL_TO_SFT | 是否已发放至SFT | number | Y |  |
| 39 | WS_ID | 工作中心编号 | string(120) | Y |  |
| 40 | IS_REWORK | 是否为重工工单 | number | Y |  |
| 41 | EXPLORATION_TYPE | 已开工单展料方式 | number | Y |  |
| 42 | SOURCE_DO_ID |  | string(120) | Y |  |
| 43 | SOURCE_MO_ID |  | string(120) | Y |  |
| 44 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 45 | OWNER_ORG | 工厂 | string(120) | Y |  |
| 46 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 47 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 48 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 49 | TRANSFER_ORDER | 转单 | string(120) | Y |  |
| 50 | OUTSOURCE_MATERIAL | 物料外包 | number | Y |  |
| 51 | MODI_DATE | 外包完成日 | date | Y |  |
| 52 | ORIG_PLAN_STRATEGY_CODE | 原规划策略编号 | string(120) | Y |  |
| 53 | ORIG_PLAN_LEVEL | 原规划层级 | string(120) | Y |  |
| 54 | SOURCE_ID_RTK | 来源码 | string(400) | Y |  |
| 55 | SOURCE_ID_ROid | 源单键值 | GUID | Y |  |
| 56 | NETTING_TYPE_DOWN | 耗用特性继承 | number | Y |  |
| 57 | NETTING_TYPE | 耗用特性 | number | Y |  |
| 58 | BOM_DATE | BOM日期 | date | Y |  |
| 59 | VERSION_TIMES | BOM版次 | string(8) | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 68 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 69 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 70 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 71 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 72 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 73 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 74 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 75 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 76 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 77 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 78 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 79 | UDF041 | 自定义字段12 | date | Y |  |
| 80 | UDF042 | 自定义字段13 | date | Y |  |
| 81 | UDF051 | 自定义字段14 | GUID | Y |  |
| 82 | UDF052 | 自定义字段15 | GUID | Y |  |
| 83 | UDF053 | 自定义字段16 | GUID | Y |  |
| 84 | UDF054 | 自定义字段17 | GUID | Y |  |
| 85 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 86 | Version | 版本号，不要随意更改 | binary | Y |  |
| 87 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 88 | ApproveDate | 修改日期 | date | Y |  |
| 89 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MO_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MO_D_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 制令编号 | string(120) | Y |  |
| 3 | ITEM_CODE | 品号 | string(120) | Y |  |
| 4 | SEQUENCE_TXT | 组件序号 | string(120) | Y |  |
| 5 | SEQU_NUM |  | string(120) | Y |  |
| 6 | INPUT_PART_RELEASE_QTY | 组件已领用量 | number(16,6) | Y |  |
| 7 | WAREHOUSE_CODE | 仓储编号 | string(120) | Y |  |
| 8 | INPUT_PART_DEMAND_QTY | (库)组件总需求量 | number(16,6) | Y |  |
| 9 | BIN_CODE | 储位 | string(120) | Y |  |
| 10 | IS_CONSIGNED |  | number | Y |  |
| 11 | OPERATION_ID | 作业编号 | string(120) | Y |  |
| 12 | IS_BACK_FLUSH | 领料是否倒冲 | number | Y |  |
| 13 | INPUT_PART_R_DEMAND_QTY | (库)组件真实需求量 | number(16,6) | Y |  |
| 14 | INPUT_PART_S_DEMAND_QTY | (库)组件损耗需求量 | number(16,6) | Y |  |
| 15 | CUS_STRING1 |  | string(120) | Y |  |
| 16 | CUS_STRING2 |  | string(120) | Y |  |
| 17 | CUS_STRING3 |  | string(120) | Y |  |
| 18 | CUS_NUMERIC1 |  | number | Y |  |
| 19 | CUS_NUMERIC2 |  | number(16,6) | Y |  |
| 20 | CUS_NUMERIC3 |  | number(16,0) | Y |  |
| 21 | CUS_DATE1 |  | date | Y |  |
| 22 | CUS_DATE2 |  | date | Y |  |
| 23 | IS_AUTOISSUE |  | number | Y |  |
| 24 | REPLACED_ITEM_CODE | 替代 | string(120) | Y |  |
| 25 | FEATURE_CODE | 组件品号特征码 | string(120) | Y |  |
| 26 | REPLACED_ITEM_FEATURE_CODE | 原主料料号特征码 | string(120) | Y |  |
| 27 | ISSUE_MATERIAL_PERIOD | 投料间距 | string(120) | Y |  |
| 28 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 29 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 30 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 31 | PLAN_LEVEL | 规划层级 | string(20) | Y |  |
| 32 | IS_REWORK |  | number | Y |  |
| 33 | DEPEND_NUM |  | number(16,6) | Y |  |
| 34 | GROUP_ALTCODE | 替代群组码 | string(120) | Y |  |
| 35 | GROUP_CODE | 群组码 | string(120) | Y |  |
| 36 | GROUP_QTY | 供給上阶相对數量 | number(16,6) | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 45 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 46 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 47 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 48 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 49 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 50 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 51 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 52 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 53 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 54 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 55 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 56 | UDF041 | 自定义字段12 | date | Y |  |
| 57 | UDF042 | 自定义字段13 | date | Y |  |
| 58 | UDF051 | 自定义字段14 | GUID | Y |  |
| 59 | UDF052 | 自定义字段15 | GUID | Y |  |
| 60 | UDF053 | 自定义字段16 | GUID | Y |  |
| 61 | UDF054 | 自定义字段17 | GUID | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | Version | 版本号，不要随意更改 | binary | Y |  |
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MO_PEG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MO_PEG_ID | 主键 | GUID | Y | Y |
| 2 | FED_ORDER_ID | 供給單號 | string(120) | Y |  |
| 3 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 4 | FEDED_ORDER_ID | 被供給單號 | string(120) | Y |  |
| 5 | IS_DEMAND | 訂單需求 | number | Y |  |
| 6 | FED_QTY | 供給數量 | number(16,6) | Y |  |
| 7 | IS_STOCK | 採購件 | number | Y |  |
| 8 | SUPPLY_QTY | 可供給數量 | number(16,6) | Y |  |
| 9 | IS_LOCK | 鎖定供需 | number | Y |  |
| 10 | ITEM_CODE | 品號 | string(210) | Y |  |
| 11 | REQUIRE_TIME | 需求日期 | date | Y |  |
| 12 | CUS_STRING1 | 保留欄位元_文字1 | string(120) | Y |  |
| 13 | CUS_STRING2 | 保留欄位元_文字2 | string(120) | Y |  |
| 14 | CUS_STRING3 | 保留欄位元_文字3 | string(120) | Y |  |
| 15 | CUS_NUMERIC1 | 保留欄位_數值1 | number | Y |  |
| 16 | CUS_NUMERIC2 | 保留欄位_數值2 | number(16,6) | Y |  |
| 17 | CUS_NUMERIC3 | 保留欄位_數值3 | number(16,6) | Y |  |
| 18 | CUS_DATE1 | 保留欄位_日期1 | date | Y |  |
| 19 | CUS_DATE2 | 保留欄位_日期2 | date | Y |  |
| 20 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 21 | ORIG_PART_ID | 原始需求品號 | string(210) | Y |  |
| 22 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 23 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 24 | SUB_TYPE | 取替代型態 | number | Y |  |
| 25 | UNIQUE_ID | 唯一碼 | string(120) | Y |  |
| 26 | REAL_FED_QTY | 實際配置數量 | number(16,6) | Y |  |
| 27 | GROUP_QTY | 供應套數 | number(16,6) | Y |  |
| 28 | SUPER_ORDER_ID | 最上階訂單號 | string(120) | Y |  |
| 29 | LOCK_STATUS | 鎖定訊息 | string(120) | Y |  |
| 30 | DISPATCH_STATUS | 產能鎖定訊息 | string(120) | Y |  |
| 31 | PEG_TYPE | 鎖定型態 | number | Y |  |
| 32 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 33 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 34 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 35 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 36 | ORIG_PLAN_STRATEGY_CODE | 原規劃策略 | string(120) | Y |  |
| 37 | ORIG_PLAN_LEVEL | 原案例編號 | string(120) | Y |  |
| 38 | TARGET_ITEM | 目標品項 | number | Y |  |
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Attachments | 附件 | string | Y |  |
| 46 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 47 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 48 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 49 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 50 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 51 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 52 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 53 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 54 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 55 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 56 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 57 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 58 | UDF041 | 自定义字段12 | date | Y |  |
| 59 | UDF042 | 自定义字段13 | date | Y |  |
| 60 | UDF051 | 自定义字段14 | GUID | Y |  |
| 61 | UDF052 | 自定义字段15 | GUID | Y |  |
| 62 | UDF053 | 自定义字段16 | GUID | Y |  |
| 63 | UDF054 | 自定义字段17 | GUID | Y |  |
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MO_PRODUCT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MO_PRODUCT_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | ITEM_CODE | 品號 | string(210) | Y |  |
| 4 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 5 | PRODUCT_TYPE | 產出類型 | string(120) | Y |  |
| 6 | PLAN_QTY | 預計產出數量 | number(16,6) | Y |  |
| 7 | COMPLETED_QTY | 已入庫數量 | number(16,6) | Y |  |
| 8 | SCRAP_QTY | 報廢數量 | number(16,6) | Y |  |
| 9 | DESTROYED_QTY | 破壞數量 | number(16,6) | Y |  |
| 10 | COST_RATE | 成本比率 | number(16,6) | Y |  |
| 11 | REMARK | 備註 | string(400) | Y |  |
| 12 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 13 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 14 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 15 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
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
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MO_SUB

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MO_SUB_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | SOURCE_MFG_ORDER_ID | 來源工單 | string(120) | Y |  |
| 4 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 5 | PRODUCED_QTY | 已生產量 | number(16,6) | Y |  |
| 6 | SCRAP_QTY | 報廢數量 | number(16,6) | Y |  |
| 7 | PRODUCE_QTY | 生產量 | number(16,6) | Y |  |
| 8 | FIRM_COMPLETE_DATE | ERP預計完工日 | date | Y |  |
| 9 | FIRM_RELEASE_DATE | ERP預計開立日 | date | Y |  |
| 10 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 11 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 12 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 13 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MPSITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPSITEM_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 4 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 5 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 6 | ITEM_CODE | 品號 | string(210) | Y |  |
| 7 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 8 | TARGET_ITEM | 目標品項 | number | Y |  |
| 9 | STOP_BALANCE_ITEM | 關閉供需平衡 | number | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MPT_LOG (按单规划异动记录信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_LOG_ID | 主键 | GUID | Y | Y |
| 2 | APS_MPT_LOG_CODE | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 案例/计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | LOG_TXT | 记录内容 | string(510) | Y |  |
| 8 | LOG_TIME | 记录时间 | date | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 35 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 36 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 37 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 38 | RESERVED_021 | 预留字段021 | date | Y |  |
| 39 | RESERVED_022 | 预留字段022 | date | Y |  |
| 40 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 41 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 42 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 43 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 44 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 45 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 46 | RESERVED_061 | 预留字段061 | number | Y |  |
| 47 | RESERVED_062 | 预留字段062 | number | Y |  |
| 48 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 49 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 50 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MPT_MAIN (按单规划主信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_MAIN_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 按件/计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | NODE_ID | 节点编号 | string(120) | Y |  |
| 8 | PARENT_ID | 父节点编号 | string(120) | Y |  |
| 9 | BOMLEVEL | 层级码 | number | Y |  |
| 10 | SUPPLY_TYPE | 供给类型 | string(40) | Y |  |
| 11 | LOT_VERSION | 计划批号 | string(120) | Y |  |
| 12 | DEMAND_ORDER_ID | 单号 | string(120) | Y |  |
| 13 | FEATURE_GROUP_CODE | 品号群组 | string(20) | Y |  |
| 14 | ITEM_CODE | 品号 | string(80) | Y |  |
| 15 | SUPPLY_QTY | 供给数量 | number(16,6) | Y |  |
| 16 | ORDER_ORG_QTY | 计划数量 | number(16,6) | Y |  |
| 17 | ORDER_MODI_QTY | 生产调拨数量 | number(16,6) | Y |  |
| 18 | UNIT_ID | 单位 | string(8) | Y |  |
| 19 | PLAN_RELEASE_DATE | 预计开工日 | date | Y |  |
| 20 | PLAN_COMPLETE_DATE | 预计完工日 | date | Y |  |
| 21 | BOM_VERSION | BOM版次 | string(8) | Y |  |
| 22 | BOM_DATE | BOM日期 | date | Y |  |
| 23 | DOC_CODE | 单据类型 | string(8) | Y |  |
| 24 | DOC_NAME | 单据类型名称 | string(20) | Y |  |
| 25 | ITEM_PROPERTY | 性质 | string(40) | Y |  |
| 26 | ROUTE_CONTROL | 工艺路线管理 | number(0/1) | Y |  |
| 27 | ROUTING_CODE | 工艺路线 | string(40) | Y |  |
| 28 | ROUTING_NAME | 工艺路线名称 | string(120) | Y |  |
| 29 | IS_FIRM | 排程时间冻结 | number(0/1) | Y |  |
| 30 | DO_IS_LOCK | 供需关联锁定 | number(0/1) | Y |  |
| 31 | SUPER_ORDER_ID | 需求单号 | string(120) | Y |  |
| 32 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 33 | SECOND_UNIT | 第二单位 | string(8) | Y |  |
| 34 | REMARK | 备注 | string(510) | Y |  |
| 35 | DEMAND_DATE | 需求日期 | date | Y |  |
| 36 | PLANNER_CODE | 计划员 | string(120) | Y |  |
| 37 | DEC_DIGIT | 小数位数 | number | Y |  |
| 38 | BELONG_ID_CODE | 工作中心/调拨工厂/委外供应商编号 | string(120) | Y |  |
| 39 | BELONG_ID_NAME | 工作中心/调拨工厂/委外供应商名称 | string(120) | Y |  |
| 40 | IS_SPLITED | 已拆单 | number(0/1) | Y |  |
| 41 | IS_MODIFIED | 已锁定 | number(0/1) | Y |  |
| 42 | CURRENT_RELEASE_QTY | 本次发放数量 | number(16,6) | Y |  |
| 43 | RELEASED_QTY | 已发放数量 | number(16,6) | Y |  |
| 44 | KEEP_FLAG | 重新规划锁定 | number(0/1) | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
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
| 70 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 71 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 72 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 73 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 74 | RESERVED_021 | 预留字段021 | date | Y |  |
| 75 | RESERVED_022 | 预留字段022 | date | Y |  |
| 76 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 77 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 78 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 79 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 80 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 81 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 82 | RESERVED_061 | 预留字段061 | number | Y |  |
| 83 | RESERVED_062 | 预留字段062 | number | Y |  |
| 84 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 85 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 86 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 87 | Version | 版本号，不要随意更改 | binary | Y |  |
| 88 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 89 | ApproveDate | 修改日期 | date | Y |  |
| 90 | ApproveBy | 修改人 | GUID | Y |  |
| 91 | BELONG_ID_RTK |  | string(400) | Y |  |
| 92 | BELONG_ID_ROid |  | GUID | Y |  |

### APS_MPT_MAIN_BOM (按单规划相依需求信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_MAIN_BOM_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 案例/计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | SEQ |  | number | Y |  |
| 8 | ITEM_CODE | 品号 | string(80) | Y |  |
| 9 | ITEM_NAME | 品名 | string(120) | Y |  |
| 10 | ITEM_SPEC | 规格 | string(510) | Y |  |
| 11 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 12 | ITEM_FEATURE_SPEC | 特征码规格 | string(120) | Y |  |
| 13 | DRAWING_NO | 图号 | string(510) | Y |  |
| 14 | USE_DATE | 预计领料日期 | date | Y |  |
| 15 | USE_QTY | 需领用量 | number(16,6) | Y |  |
| 16 | UNIT_CODE | 单位 | string(8) | Y |  |
| 17 | ROUTING_ID | 工艺路线主键 | GUID | Y |  |
| 18 | ROUTING_CODE | 工艺 | string(20) | Y |  |
| 19 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 20 | REPLACED_ITEM_CODE | 取替代品号 | string(80) | Y |  |
| 21 | REPLACED_FEATURE_CODE | 取替代特征码 | string(120) | Y |  |
| 22 | REPLACED_QTY | 被取替代料量 | number(16,6) | Y |  |
| 23 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 24 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 25 | WAREHOUSE_ID | 仓库主键 | GUID | Y |  |
| 26 | WAREHOUSE_CODE | 仓库编号 | string(20) | Y |  |
| 27 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 28 | SECOND_UNIT_CODE | 第二单位 | string(8) | Y |  |
| 29 | REMARK | 备注 | string(510) | Y |  |
| 30 | DICIMAL_DIGIT | 小数位数 | number | Y |  |
| 31 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 32 | REPLACE_ITEM | 取替代料方式 | string(40) | Y |  |
| 33 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 34 | PARENT_ITEM_ID | 父阶品号 | GUID | Y |  |
| 35 | PARENT_ITEM_FEATURE_ID | 父阶特征码 | GUID | Y |  |
| 36 | EXTRACT_ITEM_ID | 上阶品号 | GUID | Y |  |
| 37 | EXTRACT_ITEM_FEATURE_ID | 上街特征码 | GUID | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 64 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 65 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 66 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 67 | RESERVED_021 | 预留字段021 | date | Y |  |
| 68 | RESERVED_022 | 预留字段022 | date | Y |  |
| 69 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 70 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 71 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 72 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 73 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 74 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 75 | RESERVED_061 | 预留字段061 | number | Y |  |
| 76 | RESERVED_062 | 预留字段062 | number | Y |  |
| 77 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 78 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 79 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 80 | Version | 版本号，不要随意更改 | binary | Y |  |
| 81 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 82 | ApproveDate | 修改日期 | date | Y |  |
| 83 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MPT_MAIN_PEG (按单规划配置明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_MAIN_PEG_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 案例计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | SEQ | 序号 | number | Y |  |
| 8 | DEMAND_TYPE | 需求类型 | string(40) | Y |  |
| 9 | SUPER_ORDER_ID | 需求单号 | string(120) | Y |  |
| 10 | SUPPLY_QTY | 供给数量 | number(16,6) | Y |  |
| 11 | DO_IS_LOCK | 供需关联锁定 | number(0/1) | Y |  |
| 12 | UP_ITEM_CODE | 主料品号 | string(80) | Y |  |
| 13 | SUPPLY_ITEM_CODE | 需求品号 | string(80) | Y |  |
| 14 | SUPPLY_ITEM_NAME | 需求品名 | string(120) | Y |  |
| 15 | SUPPLY_ITEM_SPECIFICATION | 需求规格 | string(510) | Y |  |
| 16 | SUPPLY_FEATURE_CODE | 需求特征码 | string(120) | Y |  |
| 17 | SUPPLY_FEATURE_SPECIFICATION | 需求特征码规格 | string(120) | Y |  |
| 18 | DEMAND_DATE | 需求单据需求日期 | date | Y |  |
| 19 | SUPPLY_UNIT_ID | 需求单位 | string(8) | Y |  |
| 20 | SUB_TYPE | 类型 | string(40) | Y |  |
| 21 | CURRENT_DEMAND_DATE | 本阶需求日期 | date | Y |  |
| 22 | CURRENT_DEMAND_QTY | 本阶需求数量 | number(16,6) | Y |  |
| 23 | MAIN_ITEM_CODE | 主料品号 | string(120) | Y |  |
| 24 | MAIN_ITEM_NAME | 主料品名 | string(120) | Y |  |
| 25 | MAIN_ITEM_SPECIFICATION | 主料规格 | string(510) | Y |  |
| 26 | MAIN_FEATURE_CODE | 主料特征码 | string(120) | Y |  |
| 27 | MAIN_FEATURE_SPECIFICATION | 主料特征码规格 | string(120) | Y |  |
| 28 | MAIN_DRAWING_NO | 主料图号 | string(510) | Y |  |
| 29 | MAIN_UNIT_ID | 主料单位 | string(8) | Y |  |
| 30 | MAIN_DEMAND_QTY | 主料需求数量 | number(16,6) | Y |  |
| 31 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 32 | SECOND_UNIT | 第二单位 | string(8) | Y |  |
| 33 | REMARK | 备注 | string(510) | Y |  |
| 34 | SUPPLY_TYPE | 供给类型 | string(40) | Y |  |
| 35 | FED_ORDER_ID | 供给单号 | string(120) | Y |  |
| 36 | DICIMAL_DIGIT | 小数位数 | number | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 45 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 46 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 47 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 48 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 49 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 50 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 51 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 52 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 53 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 54 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 55 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 56 | UDF041 | 自定义字段12 | date | Y |  |
| 57 | UDF042 | 自定义字段13 | date | Y |  |
| 58 | UDF051 | 自定义字段14 | GUID | Y |  |
| 59 | UDF052 | 自定义字段15 | GUID | Y |  |
| 60 | UDF053 | 自定义字段16 | GUID | Y |  |
| 61 | UDF054 | 自定义字段17 | GUID | Y |  |
| 62 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 63 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 64 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 65 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 66 | RESERVED_021 | 预留字段021 | date | Y |  |
| 67 | RESERVED_022 | 预留字段022 | date | Y |  |
| 68 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 69 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 70 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 71 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 72 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 73 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 74 | RESERVED_061 | 预留字段061 | number | Y |  |
| 75 | RESERVED_062 | 预留字段062 | number | Y |  |
| 76 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 77 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 78 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 79 | Version | 版本号，不要随意更改 | binary | Y |  |
| 80 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 81 | ApproveDate | 修改日期 | date | Y |  |
| 82 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MPT_MAIN_RESOURCE (按单规划生产明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_MAIN_RESOURCE_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 案例/计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | SEQ | 节点编号 | number | Y |  |
| 8 | RESOURCE_CODE | 资源编号 | string(40) | Y |  |
| 9 | RESOURCE_TYPE | 资源形态 | string(400) | Y |  |
| 10 | RESOURCE_NAME | 资源名称 | string(120) | Y |  |
| 11 | RESOURCE_DATE | 生产日期 | date | Y |  |
| 12 | RESOURCE_QTY | 生产数量 | number(16,6) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | DICIMAL_DIGIT | 小数位数 | number | Y |  |
| 15 | APS_DOC_NO | APS单号 | string(120) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
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
| 41 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 42 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 43 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 44 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 45 | RESERVED_021 | 预留字段021 | date | Y |  |
| 46 | RESERVED_022 | 预留字段022 | date | Y |  |
| 47 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 48 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 49 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 50 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 51 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 52 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 53 | RESERVED_061 | 预留字段061 | number | Y |  |
| 54 | RESERVED_062 | 预留字段062 | number | Y |  |
| 55 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 56 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 57 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MPT_MAIN_SPLIT (按单规划拆单明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_MAIN_SPLIT_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 案例/计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | NODE_ID | 节点编号 | string(120) | Y |  |
| 8 | PARENT_ID | 父节点编号 | string(120) | Y |  |
| 9 | BOMLEVEL | 层级码 | number | Y |  |
| 10 | SUPPLY_TYPE | 供给类型 | string(40) | Y |  |
| 11 | LOT_VERSION | 计划批号 | string(120) | Y |  |
| 12 | DEMAND_ORDER_ID | 单号 | string(120) | Y |  |
| 13 | FEATURE_GROUP_CODE | 品号群组 | string(20) | Y |  |
| 14 | ITEM_CODE | 品号 | string(80) | Y |  |
| 15 | SUPPLY_QTY | 供给数量 | number(16,6) | Y |  |
| 16 | ORDER_ORG_QTY | 计划数量 | number(16,6) | Y |  |
| 17 | ORDER_MODI_QTY | 生产调拨数量 | number(16,6) | Y |  |
| 18 | UNIT_ID | 单位 | string(8) | Y |  |
| 19 | PLAN_RELEASE_DATE | 预计开工日 | date | Y |  |
| 20 | PLAN_COMPLETE_DATE | 预计完工日 | date | Y |  |
| 21 | BOM_VERSION | BOM版次 | string(8) | Y |  |
| 22 | BOM_DATE | BOM日期 | date | Y |  |
| 23 | DOC_CODE | 单据类型 | string(8) | Y |  |
| 24 | DOC_NAME | 单据类型名称 | string(20) | Y |  |
| 25 | ITEM_PROPERTY | 性质 | string(40) | Y |  |
| 26 | ROUTE_CONTROL | 工艺路线管理 | number(0/1) | Y |  |
| 27 | ROUTING_CODE | 工艺路线 | string(40) | Y |  |
| 28 | ROUTING_NAME | 工艺路线名称 | string(120) | Y |  |
| 29 | IS_FIRM | 排程时间冻结 | number(0/1) | Y |  |
| 30 | DO_IS_LOCK | 供需关联锁定 | number(0/1) | Y |  |
| 31 | SUPER_ORDER_ID | 需求单号 | string(120) | Y |  |
| 32 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 33 | SECOND_UNIT | 第二单位 | string(8) | Y |  |
| 34 | REMARK | 备注 | string(510) | Y |  |
| 35 | DEMAND_DATE | 需求日期 | date | Y |  |
| 36 | PLANNER_CODE | 计划员 | string(120) | Y |  |
| 37 | DEC_DIGIT | 小数位数 | number | Y |  |
| 38 | BELONG_ID_CODE | 工作中心/调拨工厂/委外供应商编号 | string(120) | Y |  |
| 39 | BELONG_ID_NAME | 工作中心/调拨工厂/委外供应商名称 | string(120) | Y |  |
| 40 | IS_SPLITED | 已拆单 | number(0/1) | Y |  |
| 41 | IS_MODIFIED | 已锁定 | number(0/1) | Y |  |
| 42 | ORIG_DEMAND_ORDER_ID | 原始单号 | string(120) | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Attachments | 附件 | string | Y |  |
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
| 68 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 69 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 70 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 71 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 72 | RESERVED_021 | 预留字段021 | date | Y |  |
| 73 | RESERVED_022 | 预留字段022 | date | Y |  |
| 74 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 75 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 76 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 77 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 78 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 79 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 80 | RESERVED_061 | 预留字段061 | number | Y |  |
| 81 | RESERVED_062 | 预留字段062 | number | Y |  |
| 82 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 83 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 84 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 85 | Version | 版本号，不要随意更改 | binary | Y |  |
| 86 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 87 | ApproveDate | 修改日期 | date | Y |  |
| 88 | ApproveBy | 修改人 | GUID | Y |  |
| 89 | BELONG_ID_RTK |  | string(400) | Y |  |
| 90 | BELONG_ID_ROid |  | GUID | Y |  |

### APS_MPT_MAIN_SPLITPEG (按单规划拆单配置明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MPT_MAIN_SPLITPEG_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 4 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 5 | CASE_CODE | 案例/计划批号 | string(120) | Y |  |
| 6 | KEY_CODE | 内部识别码 | string(120) | Y |  |
| 7 | SEQ | 序号 | number | Y |  |
| 8 | DEMAND_TYPE | 需求类型 | string(40) | Y |  |
| 9 | SUPER_ORDER_ID | 需求单号 | string(120) | Y |  |
| 10 | SUPPLY_QTY | 供给数量 | number(16,6) | Y |  |
| 11 | DO_IS_LOCK | 供需关联锁定 | number(0/1) | Y |  |
| 12 | UP_ITEM_CODE | 主料品号 | string(80) | Y |  |
| 13 | SUPPLY_ITEM_CODE | 需求品号 | string(80) | Y |  |
| 14 | SUPPLY_ITEM_NAME | 需求品名 | string(120) | Y |  |
| 15 | SUPPLY_ITEM_SPECIFICATION | 需求规格 | string(510) | Y |  |
| 16 | SUPPLY_FEATURE_CODE | 需求特征码 | string(120) | Y |  |
| 17 | SUPPLY_FEATURE_SPECIFICATION | 需求特征码规格 | string(120) | Y |  |
| 18 | DEMAND_DATE | 需求单据需求日期 | date | Y |  |
| 19 | SUPPLY_UNIT_ID | 需求单位 | string(8) | Y |  |
| 20 | SUB_TYPE | 类型 | string(40) | Y |  |
| 21 | CURRENT_DEMAND_DATE | 本阶需求日期 | date | Y |  |
| 22 | CURRENT_DEMAND_QTY | 本阶需求数量 | number(16,6) | Y |  |
| 23 | MAIN_ITEM_CODE | 主料品号 | string(120) | Y |  |
| 24 | MAIN_ITEM_NAME | 主料品名 | string(120) | Y |  |
| 25 | MAIN_ITEM_SPECIFICATION | 主料规格 | string(510) | Y |  |
| 26 | MAIN_FEATURE_CODE | 主料特征码 | string(120) | Y |  |
| 27 | MAIN_FEATURE_SPECIFICATION | 主料特征码规格 | string(120) | Y |  |
| 28 | MAIN_DRAWING_NO | 主料图号 | string(510) | Y |  |
| 29 | MAIN_UNIT_ID | 主料单位 | string(8) | Y |  |
| 30 | MAIN_DEMAND_QTY | 主料需求数量 | number(16,6) | Y |  |
| 31 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 32 | SECOND_UNIT | 第二单位 | string(8) | Y |  |
| 33 | REMARK | 备注 | string(510) | Y |  |
| 34 | SUPPLY_TYPE | 供给类型 | string(40) | Y |  |
| 35 | FED_ORDER_ID | 供给单号 | string(120) | Y |  |
| 36 | DICIMAL_DIGIT | 小数位数 | number | Y |  |
| 37 | ORIG_DEMAND_ORDER_ID | 原始单号 | string(120) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | RESERVED_001 | 预留字段001 | string(510) | Y |  |
| 64 | RESERVED_002 | 预留字段002 | string(510) | Y |  |
| 65 | RESERVED_011 | 预留字段011 | GUID | Y |  |
| 66 | RESERVED_012 | 预留字段012 | GUID | Y |  |
| 67 | RESERVED_021 | 预留字段021 | date | Y |  |
| 68 | RESERVED_022 | 预留字段022 | date | Y |  |
| 69 | RESERVED_031 | 预留字段031 | number(16,6) | Y |  |
| 70 | RESERVED_032 | 预留字段032 | number(16,6) | Y |  |
| 71 | RESERVED_041 | 预留字段041 | number(23,8) | Y |  |
| 72 | RESERVED_042 | 预留字段042 | number(23,8) | Y |  |
| 73 | RESERVED_051 | 预留字段051 | number(23,8) | Y |  |
| 74 | RESERVED_052 | 预留字段052 | number(23,8) | Y |  |
| 75 | RESERVED_061 | 预留字段061 | number | Y |  |
| 76 | RESERVED_062 | 预留字段062 | number | Y |  |
| 77 | RESERVED_071 | 预留字段071 | number(0/1) | Y |  |
| 78 | RESERVED_072 | 预留字段072 | number(0/1) | Y |  |
| 79 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 80 | Version | 版本号，不要随意更改 | binary | Y |  |
| 81 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 82 | ApproveDate | 修改日期 | date | Y |  |
| 83 | ApproveBy | 修改人 | GUID | Y |  |

### APS_MULTI_LANGUAGE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_MULTI_LANGUAGE_ID | 主键 | GUID | Y | Y |
| 2 | GROUP_ID | 多語系產品編號 | string(120) | Y |  |
| 3 | KEY_ID | 語系編號 | string(120) | Y |  |
| 4 | KEY_VALUE | 語系顯示文字 | string(400) | Y |  |
| 5 | KEY_LANGUAGE | 語系 | string(120) | Y |  |
| 6 | Version | 版本号，不要随意更改 | binary | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
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
| 32 | RESERVED_001 |  | string(510) | Y |  |
| 33 | RESERVED_002 |  | string(510) | Y |  |
| 34 | RESERVED_011 |  | GUID | Y |  |
| 35 | RESERVED_012 |  | GUID | Y |  |
| 36 | RESERVED_021 |  | date | Y |  |
| 37 | RESERVED_022 |  | date | Y |  |
| 38 | RESERVED_031 |  | number(16,6) | Y |  |
| 39 | RESERVED_032 |  | number(16,6) | Y |  |
| 40 | RESERVED_041 |  | number(23,8) | Y |  |
| 41 | RESERVED_042 |  | number(23,8) | Y |  |
| 42 | RESERVED_051 |  | number(23,8) | Y |  |
| 43 | RESERVED_052 |  | number(23,8) | Y |  |
| 44 | RESERVED_061 |  | number | Y |  |
| 45 | RESERVED_062 |  | number | Y |  |
| 46 | RESERVED_071 |  | number(0/1) | Y |  |
| 47 | RESERVED_072 |  | number(0/1) | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OMP_DO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OMP_DO_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 訂單編號 | string(120) | Y |  |
| 3 | PART_ID | 品號 | string(210) | Y |  |
| 4 | ORDER_QTY | 訂購數量 | number(16,6) | Y |  |
| 5 | DUE_DATE | 交期 | date | Y |  |
| 6 | CUSTOMER_ID | 客戶編號 | string(120) | Y |  |
| 7 | IS_SCHEDULED | 納入排程 | number | Y |  |
| 8 | ORDER_TYPE | 訂單型式 | string(120) | Y |  |
| 9 | PRIORITY | 優先順序 | number | Y |  |
| 10 | SALE_ORDER_ID | 銷售訂單編號 | string(120) | Y |  |
| 11 | CUSTOMER_ORDER_ID | 客戶單號 | string(120) | Y |  |
| 12 | SHIPPED_QTY | 已出貨量 | number(16,6) | Y |  |
| 13 | ORDER_DATE | 訂單開立日期 | date | Y |  |
| 14 | IS_NON_DELAYED | 嚴守交期 | number | Y |  |
| 15 | UNIT_ID | 單位 | string(120) | Y |  |
| 16 | REAL_DUE_DATE | 真實交期 | date | Y |  |
| 17 | ITEM_CODE | 品號 | string(210) | Y |  |
| 18 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 19 | SPARE_QTY | 贈備品量 | number(16,6) | Y |  |
| 20 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 21 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 22 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 23 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 24 | BUSINESS_QTY | 業務數量 | number(16,6) | Y |  |
| 25 | BUSSINESS_UNIT_ID | 業務單位 | string(120) | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
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
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OMP_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OMP_MO_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 4 | PRODUCED_QTY | 已生產量 | number(16,6) | Y |  |
| 5 | ERP_ORDER_ID | EPR工單編號 | string(120) | Y |  |
| 6 | FIRM_COMPLETE_DATE | ERP預計完工日 | date | Y |  |
| 7 | FIRM_RELEASE_DATE | ERP預計開立日 | date | Y |  |
| 8 | PART_ID | 品號 | string(210) | Y |  |
| 9 | ROUTE_ID | 途程編號 | string(160) | Y |  |
| 10 | SCRAP_QTY | 報廢數量 | number(16,6) | Y |  |
| 11 | STATE | 狀態 | number | Y |  |
| 12 | PO_CONSTRAINT_DATE | 物料限制時間 | date | Y |  |
| 13 | IS_NEW | 建議單據 | number | Y |  |
| 14 | PLAN_COMPLETE_DATE | 預計完工時間 | date | Y |  |
| 15 | PLAN_RELEASE_DATE | 預計發放時間 | date | Y |  |
| 16 | HAS_ROUTE | 使用工單製程 | number | Y |  |
| 17 | IS_OUTSOURCING | 外包 | number | Y |  |
| 18 | OUTSOURCE_ID | 外包商編號 | string(120) | Y |  |
| 19 | UNIT_ID | 單位 | string(120) | Y |  |
| 20 | IS_FIRM | 鎖定 | number | Y |  |
| 21 | ITEM_CODE | 品號 | string(210) | Y |  |
| 22 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 23 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 24 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 25 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 26 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 27 | BOM_DATE | BOM日期 | date | Y |  |
| 28 | VERSION_TIMES | BOM版次 | string(8) | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Attachments | 附件 | string | Y |  |
| 36 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 37 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 38 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 39 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 40 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 41 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 42 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 43 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 44 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 45 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 46 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 47 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 48 | UDF041 | 自定义字段12 | date | Y |  |
| 49 | UDF042 | 自定义字段13 | date | Y |  |
| 50 | UDF051 | 自定义字段14 | GUID | Y |  |
| 51 | UDF052 | 自定义字段15 | GUID | Y |  |
| 52 | UDF053 | 自定义字段16 | GUID | Y |  |
| 53 | UDF054 | 自定义字段17 | GUID | Y |  |
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OMP_MOPEG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OMP_MOPEG_ID | 主键 | GUID | Y | Y |
| 2 | FED_ORDER_ID | 供給單號 | string(120) | Y |  |
| 3 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 4 | FEDED_ORDER_ID | 被供給單號 | string(120) | Y |  |
| 5 | IS_DEMAND | 訂單需求 | number | Y |  |
| 6 | FED_QTY | 供給數量 | number(16,6) | Y |  |
| 7 | IS_STOCK | 採購件 | number | Y |  |
| 8 | SUPPLY_QTY | 可供給數量 | number(16,6) | Y |  |
| 9 | IS_LOCK | 鎖定供需 | number | Y |  |
| 10 | PART_ID | 品號 | string(210) | Y |  |
| 11 | REQUIRE_TIME | 需求日期 | date | Y |  |
| 12 | PEG_SEQ | 配置順序 | number | Y |  |
| 13 | IS_PO_MOST_CRITICAL | 最關鍵採購 | number | Y |  |
| 14 | ITEM_CODE | 品號 | string(210) | Y |  |
| 15 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 16 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 17 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 18 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 19 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 20 | USE_DIFFERENT_PRODUCT | 聯副產品 | number | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Attachments | 附件 | string | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OMP_PO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OMP_PO_ID | 主键 | GUID | Y | Y |
| 2 | PURCHASE_ORDER_ID | 採購單編號 | string(120) | Y |  |
| 3 | PART_ID | 品號 | string(210) | Y |  |
| 4 | PURCHASE_QTY | 預計採購數量 | number(16,6) | Y |  |
| 5 | IS_NEW | 建議單據 | number | Y |  |
| 6 | FIRM_RELEASE_DATE | ERP預計開立日 | date | Y |  |
| 7 | FIRM_AVAILABLE_DATE | ERP預計到廠日 | date | Y |  |
| 8 | PLAN_RELEASE_DATE | 預計發放時間 | date | Y |  |
| 9 | PLAN_AVAILABLE_DATE | 預計到廠日期 | date | Y |  |
| 10 | SUPPLIER_ID | 供應商編號 | string(120) | Y |  |
| 11 | ERP_ORDER_ID | EPR工單編號 | string(120) | Y |  |
| 12 | STOCKED_QTY | 已入庫數量 | number(16,6) | Y |  |
| 13 | STATE | 狀態 | number | Y |  |
| 14 | IS_FIRM | 鎖定 | number | Y |  |
| 15 | UNINSPECT_QTY | 待驗量 | number(16,6) | Y |  |
| 16 | UNSTOCKED_QTY | 待入庫量 | number(16,6) | Y |  |
| 17 | RETURN_QTY | 驗退量 | number(16,6) | Y |  |
| 18 | LOCATION | 供應商位置 | string(120) | Y |  |
| 19 | UNIT_ID | 單位 | string(400) | Y |  |
| 20 | LEAD_TIME | 前置時間 | number(16,6) | Y |  |
| 21 | FIRM_SUPPLY_DATE | ERP預計到庫日 | date | Y |  |
| 22 | PLAN_SUPPLY_DATE | 預計到庫日期 | date | Y |  |
| 23 | ITEM_CODE | 品號 | string(210) | Y |  |
| 24 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 25 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 26 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 27 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 28 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 29 | BUSINESS_QTY | BUSINESS_QTY | number(16,6) | Y |  |
| 30 | BUSINESS_UNIT_ID | BUSINESS_UNIT_ID | string(120) | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Attachments | 附件 | string | Y |  |
| 38 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 39 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 40 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 41 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 42 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 43 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 44 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 45 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 46 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 47 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 48 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 49 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 50 | UDF041 | 自定义字段12 | date | Y |  |
| 51 | UDF042 | 自定义字段13 | date | Y |  |
| 52 | UDF051 | 自定义字段14 | GUID | Y |  |
| 53 | UDF052 | 自定义字段15 | GUID | Y |  |
| 54 | UDF053 | 自定义字段16 | GUID | Y |  |
| 55 | UDF054 | 自定义字段17 | GUID | Y |  |
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 59 | ApproveDate | 修改日期 | date | Y |  |
| 60 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OMP_WORK_CALENDAR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OMP_WORK_CALENDAR_ID | 主键 | GUID | Y | Y |
| 2 | WORK_CALENDAR_CODE | 工作曆編號 | string(120) | Y |  |
| 3 | CALENDAR_DATE | 日期 | date | Y |  |
| 4 | WORK_MODEL_ID | 工作模式編號 | string(120) | Y |  |
| 5 | WORK_TIME | 當日工作時間 | number | Y |  |
| 6 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 7 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 8 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 9 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OMP_WORK_MODEL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OMP_WORK_MODEL_ID | 主键 | GUID | Y | Y |
| 2 | WM_ID | 工作模式編號 | string(120) | Y |  |
| 3 | START_TIME | 開始秒數 | number | Y |  |
| 4 | END_TIME | 當日結束時間 | number | Y |  |
| 5 | TYPE | 工作型態 | number | Y |  |
| 6 | WM_NAME | 工作模式名稱 | string(120) | Y |  |
| 7 | WM_DESCRIPT | 工作模式描述 | string(120) | Y |  |
| 8 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 9 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 10 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 11 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
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
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OPERATION_MASTER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OPERATION_MASTER_ID | 主键 | GUID | Y | Y |
| 2 | OPERATION_ID | 作業編號 | string(120) | Y |  |
| 3 | MP_AVAILABLE | 系統欄位 | number | Y |  |
| 4 | OP_CAPTION | 保留欄位 | string(120) | Y |  |
| 5 | CP_AVAILABLE | 保留欄位 | number | Y |  |
| 6 | MCP_AVAILABLE | 保留欄位 | number | Y |  |
| 7 | PROGRAM_ID | 系統欄位 | string(120) | Y |  |
| 8 | NOTE | 備註 | string(400) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_DAILY_DO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_DAILY_DO_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 訂單編號 | string(400) | Y |  |
| 3 | OUT_DATE | 產出日 | date | Y |  |
| 4 | OUT_QTY | 產出數量 | number(16,6) | Y |  |
| 5 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 6 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 7 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 8 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_DAILY_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_DAILY_MO_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | OUT_DATE | 產出日 | date | Y |  |
| 4 | OUT_QTY | 產出數量 | number(16,6) | Y |  |
| 5 | SETUP_CYCLE_TIME | 整備製造週期 | number | Y |  |
| 6 | PROCESS_CYCLE_TIME | 加工製造週期 | number | Y |  |
| 7 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 8 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 9 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 10 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
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
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_DAILY_OP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_DAILY_OP_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 制令编号 | string(120) | Y |  |
| 3 | SEQU_NUM | 加工顺序 | string(120) | Y |  |
| 4 | OUT_DATE | 产出日期 | date | Y |  |
| 5 | IS_OUTSOURCING | 是否为外包 | number | Y |  |
| 6 | EQUIP_TYPE | 设备型态 | number | Y |  |
| 7 | RESOURCE_CODE | 设备编号 | string(120) | Y |  |
| 8 | SKL_SEQ | 排程顺序 | number | Y |  |
| 9 | ROUTE_ID | 途程编号 | string(120) | Y |  |
| 10 | OPERATION_ID | 作业编号 | string(120) | Y |  |
| 11 | OUT_QTY | 预估产出数量 | number(16,6) | Y |  |
| 12 | SETUP_CYCLE_TIME | 整备制造周期 | number | Y |  |
| 13 | PROCESS_CYCLE_TIME | 加工制造周期 | number | Y |  |
| 14 | RESOURCE_GROUP_CODE | 设备群组 | string(120) | Y |  |
| 15 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 16 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 17 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 18 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
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
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | FIXED_LEAD_TIME_FLAG | 固定前置标志 | number(0/1) | Y |  |

### APS_OUT_DEMAND

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_DEMAND_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_SOURCE_ID | 需求來源編號 | string(120) | Y |  |
| 3 | DEMAND_SOURCE_TYPE | 需求來源型態 | number | Y |  |
| 4 | DEMAND_SEQUENCE | 需求序 | number | Y |  |
| 5 | ALLOCATE_SEQUENCE | 分配序 | number | Y |  |
| 6 | SUBSTITUTE_SEQUENCE | 替代序 | number | Y |  |
| 7 | DEMAND_ORDER_ID | 訂單編號 | string(120) | Y |  |
| 8 | PART_ID | 品號 | string(210) | Y |  |
| 9 | SUB_TYPE | 取替代型態 | number | Y |  |
| 10 | DEMAND_TIME | 需求日 | date | Y |  |
| 11 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 12 | FO_CONSUME_QTY | 預測耗用量 | number(16,6) | Y |  |
| 13 | PROJECT_SHORT_QTY | 預計短缺量 | number(16,6) | Y |  |
| 14 | ORIG_PART_ID | 原始需求品號 | string(210) | Y |  |
| 15 | ORIG_DEMAND_QTY | 主料需求數量 | number(16,6) | Y |  |
| 16 | SOURCE_PART_ID | 上階需求料號 | string(210) | Y |  |
| 17 | RELEASED_QTY | 已領用量 | number(16,6) | Y |  |
| 18 | V_TO_R_DEMAND_QTY | 虛擬訂單實際需求量 | number(16,6) | Y |  |
| 19 | ITEM_CODE | 品號 | string(210) | Y |  |
| 20 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 21 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 22 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 23 | MO_ITEM_CODE | 工單品號 | string(210) | Y |  |
| 24 | MO_FEATURE_CODE | 工單特徵碼 | string(120) | Y |  |
| 25 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 26 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 27 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 28 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 29 | SEQUENCE_TXT | BOM序號 | string(120) | Y |  |
| 30 | DEPEND_NUM | 領料序 | number(16,6) | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Attachments | 附件 | string | Y |  |
| 38 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 39 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 40 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 41 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 42 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 43 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 44 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 45 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 46 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 47 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 48 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 49 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 50 | UDF041 | 自定义字段12 | date | Y |  |
| 51 | UDF042 | 自定义字段13 | date | Y |  |
| 52 | UDF051 | 自定义字段14 | GUID | Y |  |
| 53 | UDF052 | 自定义字段15 | GUID | Y |  |
| 54 | UDF053 | 自定义字段16 | GUID | Y |  |
| 55 | UDF054 | 自定义字段17 | GUID | Y |  |
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 59 | ApproveDate | 修改日期 | date | Y |  |
| 60 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_DO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_DO_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 需求订单编号 | string(120) | Y |  |
| 3 | PART_ID | 订购品项之品号 | string(210) | Y |  |
| 4 | ORDER_QTY | 订购数量 | number(16,6) | Y |  |
| 5 | DUE_DATE | 交期 | date | Y |  |
| 6 | CAN_CONSUME | 是否能被消耗 | number | Y |  |
| 7 | CUSTOMER_ID | 客户代号 | string(120) | Y |  |
| 8 | CUSTOMER_GROUP_ID | 客户群组编号 | string(120) | Y |  |
| 9 | IS_SCHEDULED | 是否纳入排程 | number | Y |  |
| 10 | ORDER_TYPE | 订单型式 | string(120) | Y |  |
| 11 | PART_FAMILY_ID | 同一产品族的品号 | string(120) | Y |  |
| 12 | PRIORITY | 订单之优先级 | number | Y |  |
| 13 | SALE_ORDER_ID | 销售订单 | string(120) | Y |  |
| 14 | CUSTOMER_ORDER_ID | 客户单号 | string(120) | Y |  |
| 15 | SHIPPED_QTY |  | number(16,6) | Y |  |
| 16 | COMPLETE_QTY | (库)系统规划后可完成数量 | number(16,6) | Y |  |
| 17 | F_CONSUM_QTY | (库)预测耗用量 | number(16,6) | Y |  |
| 18 | SHORT_QTY | 短缺 | number(16,6) | Y |  |
| 19 | REL_SHORT_QTY | (库) 实际短缺量 | number(16,6) | Y |  |
| 20 | PRODUCE_QTY | 应生产量 | number(16,6) | Y |  |
| 21 | RELEASE_DATE |  | date | Y |  |
| 22 | COMPLETE_DATE |  | date | Y |  |
| 23 | CAN_SCHEDULE | 信息作检查 | number | Y |  |
| 24 | ERROR_MSG | 订单相关错误讯 | string(120) | Y |  |
| 25 | LATE_MSG |  | string(510) | Y |  |
| 26 | USE_PART_FAMILY |  | string(120) | Y |  |
| 27 | MP_RELEASE_DATE | MP阶段规划的预计开工日 | date | Y |  |
| 28 | MP_COMPLETE_DATE | MP阶段规划的预计完工日 | date | Y |  |
| 29 | UNIT_ID | 订单记录之计量单位 | string(120) | Y |  |
| 30 | IS_CONSIGN_SHORT | 是否有客供料缺料 | number | Y |  |
| 31 | OWNER | 订单拥有者 | string(120) | Y |  |
| 32 | PLANNER | 订单规划者 | string(120) | Y |  |
| 33 | BUYER | 订单采买者 | string(120) | Y |  |
| 34 | TRANSFER_RATE | 转换率 | number(16,8) | Y |  |
| 35 | ORDER_DATE | 订单开立日期 | date | Y |  |
| 36 | PLAN_UNIT_ID | APS规划时之单位 | string(120) | Y |  |
| 37 | IS_NON_DELAYED | 是否严守交期 | number | Y |  |
| 38 | ON_TIME_QTY |  | number(16,6) | Y |  |
| 39 | REAL_DUE_DATE | 真实交期 | date | Y |  |
| 40 | ITEM_CODE | 品号(去特征码) | string(120) | Y |  |
| 41 | FEATURE_CODE | 品号特征码 | string(120) | Y |  |
| 42 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 43 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 44 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 45 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 46 | SHORT_MSG | 短缺製令或採購令 | string(120) | Y |  |
| 47 | NETTING_TYPE_DOWN | 耗用特性继承 | number | Y |  |
| 48 | NETTING_TYPE | 耗用特性 | number | Y |  |
| 49 | CR_VALUE | CR值 | number(16,6) |  |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | Attachments | 附件 | string | Y |  |
| 57 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 58 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 59 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 60 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 61 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 62 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 63 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 64 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 65 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 66 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 67 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 68 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 69 | UDF041 | 自定义字段12 | date | Y |  |
| 70 | UDF042 | 自定义字段13 | date | Y |  |
| 71 | UDF051 | 自定义字段14 | GUID | Y |  |
| 72 | UDF052 | 自定义字段15 | GUID | Y |  |
| 73 | UDF053 | 自定义字段16 | GUID | Y |  |
| 74 | UDF054 | 自定义字段17 | GUID | Y |  |
| 75 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 76 | Version | 版本号，不要随意更改 | binary | Y |  |
| 77 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 78 | ApproveDate | 修改日期 | date | Y |  |
| 79 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_FO_DEMAND

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_FO_DEMAND_ID | 主键 | GUID | Y | Y |
| 2 | FO_ORDER_ID | 预测订单编号 | string(120) | Y |  |
| 3 | ITEM_CODE | 品号 | string(120) | Y |  |
| 4 | FEATURE_CODE | 品号特征码 | string(120) | Y |  |
| 5 | MDS_START_DATE | 冲销起始日期 | date | Y |  |
| 6 | FO_DEMAND_TIME | 预测订单交期 | date | Y |  |
| 7 | UNIT_ID | 单位 | string(120) | Y |  |
| 8 | MDS_END_DATE | 冲销结束日期 | date | Y |  |
| 9 | FO_ORDER_QTY | 预测订单开立数量 | number(16,6) | Y |  |
| 10 | DEMAND_ORDER_ID | 订单编号 | string(120) | Y |  |
| 11 | DO_DUE_DATE | 订单交期 | date | Y |  |
| 12 | WRITE_OFF_QTY | 冲销数量 | number(16,6) | Y |  |
| 13 | SEQUENCE | 冲销顺序 | number | Y |  |
| 14 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 15 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 16 | CASE_CODE | 案例编号 | string(120) | Y |  |
| 17 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
| 26 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### APS_OUT_INV_ALLOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_INV_ALLOC_ID | 主键 | GUID | Y | Y |
| 2 | PART_ID | PART_ID | string(210) | Y |  |
| 3 | FED_QTY | FED_QTY | number(16,6) | Y |  |
| 4 | DEMAND_QTY | DEMAND_QTY | number(16,6) | Y |  |
| 5 | IS_MATERIAL | IS_MATERIAL | number | Y |  |
| 6 | ORDER_ID | ORDER_ID | string(120) | Y |  |
| 7 | WAREHOUSE_CODE | WAREHOUSE_CODE | string(120) | Y |  |
| 8 | IS_LOCK | IS_LOCK | number | Y |  |
| 9 | IS_DEMAND_ORDER | IS_DEMAND_ORDER | number | Y |  |
| 10 | BIN_CODE | BIN_CODE | string(120) | Y |  |
| 11 | PEG_SEQ | 全域配置順序 | number | Y |  |
| 12 | ITEM_CODE | ITEM_CODE | string(210) | Y |  |
| 13 | FEATURE_CODE | FEATURE_CODE | string(210) | Y |  |
| 14 | ORIG_PART_ID | ORIG_PART_ID | string(210) | Y |  |
| 15 | REPLACED_ITEM_CODE | REPLACED_ITEM_CODE | string(210) | Y |  |
| 16 | REPLACED_FEATURE_CODE | REPLACED_FEATURE_CODE | string(210) | Y |  |
| 17 | SUB_TYPE | SUB_TYPE | number | Y |  |
| 18 | UNIQUE_ID | UNIQUE_ID | string(120) | Y |  |
| 19 | GROUP_QTY | GROUP_QTY | number(16,6) | Y |  |
| 20 | SUPER_ORDER_ID | SUPER_ORDER_ID | string(120) | Y |  |
| 21 | DEPEND_NUM | 工單元件需求編號 | number(16,6) | Y |  |
| 22 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 23 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 24 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 25 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
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
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_INVENTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_INVENTORY_ID | 主键 | GUID | Y | Y |
| 2 | PART_ID | 品號 | string(210) | Y |  |
| 3 | WAREHOUSE_CODE | 庫別 | string(120) | Y |  |
| 4 | BIN_CODE | 庫位 | string(120) | Y |  |
| 5 | ORIGINAL_QTY | 原庫存數 | number(16,6) | Y |  |
| 6 | R_CONSUM_QTY | 實際耗用量 | number(16,6) | Y |  |
| 7 | UNALLOCATE_QTY | 未分配量 | number(16,6) | Y |  |
| 8 | SUBSTITUTE_QTY | 主料替他量 | number(16,6) | Y |  |
| 9 | ITEM_CODE | 品號 | string(210) | Y |  |
| 10 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 11 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 12 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 13 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 14 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
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
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_ITEM_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_ITEM_BALANCE_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 订单单号 | string(120) | Y |  |
| 3 | ITEM_CODE | 品号 | string(120) | Y |  |
| 4 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 5 | DEMAND_SOURCE_ID | 需求单号 | string(120) | Y |  |
| 6 | ORDER_ID | 新开单据 | string(120) | Y |  |
| 7 | INVENTORY_QTY | 现有库存量 | number(16,6) | Y |  |
| 8 | SAFETY_STOCK_QTY | 安全库存量 | number(16,6) | Y |  |
| 9 | RESERVED_ORDER_QTY | 行政保留量 | number(16,6) | Y |  |
| 10 | PLN_ORDER | 计划销货量 | number(16,6) | Y |  |
| 11 | RLS_ORDER | 预计销货量 | number(16,6) | Y |  |
| 12 | PLN_MO | 计划生产量 | number(16,6) | Y |  |
| 13 | PLN_PO | 计划采购量 | number(16,6) | Y |  |
| 14 | PLN_MO_D | 计划领料量 | number(16,6) | Y |  |
| 15 | RLS_MO_D | 预计领料量 | number(16,6) | Y |  |
| 16 | RLS_MO | 预计生产量 | number(16,6) | Y |  |
| 17 | RLS_PO | 预计进货量 | number(16,6) | Y |  |
| 18 | PLN_MO1 | APS生产计划 | number(16,6) | Y |  |
| 19 | PLN_PO1 | APS采购计划 | number(16,6) | Y |  |
| 20 | RLS_PR | 预计请购量 | number(16,6) | Y |  |
| 21 | INTRANSIT_QTY | 预计调入量 | number(16,6) | Y |  |
| 22 | INSPECTING_QTY | 采购在验量 | number(16,6) | Y |  |
| 23 | INSPECTED_QTY | 采购待入库量 | number(16,6) | Y |  |
| 24 | REPLACE_QTY | 替代他料量 | number(16,6) | Y |  |
| 25 | REPLACED_QTY | 被替代量 | number(16,6) | Y |  |
| 26 | BALANCE_QTY | 预计可用量 | number(16,6) | Y |  |
| 27 | OWNER_ORG | 工厂 | string(120) | Y |  |
| 28 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 29 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 30 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Attachments | 附件 | string | Y |  |
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
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

### APS_OUT_ITEM_BALANCE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_ITEM_BALANCE_D_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 订单单号 | string(120) | Y |  |
| 3 | ITEM_CODE | 品号 | string(120) | Y |  |
| 4 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 5 | DEMAND_SOURCE_ID | 需求单号 | string(120) | Y |  |
| 6 | ORDER_ID | 新开单据 | string(120) | Y |  |
| 7 | ORDER_TYPE | 数据类型 | string(120) | Y |  |
| 8 | DT | 供需日期 | date | Y |  |
| 9 | ORIG_DT | 原始日期 | date | Y |  |
| 10 | QTY | 数量 | number(16,6) | Y |  |
| 11 | ERP_ORDER_ID | 单据 | string(120) | Y |  |
| 12 | OWNER_ORG | 工厂 | string(120) | Y |  |
| 13 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 14 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 15 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 24 | ApproveDate | 修改日期 | date | Y |  |
| 25 | ApproveBy | 修改人 | GUID | Y |  |
| 26 | APS_OUT_ITEM_BALANCE_ID |  | GUID | Y |  |
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
| 45 | GROUP_SEQ |  | number | Y |  |

### APS_OUT_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MO_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 制令编号 | string(120) | Y |  |
| 3 | DEMAND_QTY | 需求数量 | number(16,6) | Y |  |
| 4 | ERP_ORDER_ID | EPR中对应的制令单号 | string(120) | Y |  |
| 5 | FIRM_COMPLETE_DATE | ERP预计完工日期 | date | Y |  |
| 6 | FIRM_RELEASE_DATE | ERP预计开立日期 | date | Y |  |
| 7 | IS_NEW | 制令状态 | number | Y |  |
| 8 | PART_ID | 制令品号 | string(210) | Y |  |
| 9 | PLAN_COMPLETE_DATE | APS预计完工时间 | date | Y |  |
| 10 | PLAN_RELEASE_DATE | APS预计完工时间 | date | Y |  |
| 11 | PRIORITY | 优先级 | number | Y |  |
| 12 | RELEASE_QTY | 此制令之开立数量 | number(16,6) | Y |  |
| 13 | ROUTE_ID | 途程编号 | string(160) | Y |  |
| 14 | TYPE | 品项型式 | number | Y |  |
| 15 | UNIT_ID | 单位 | string(120) | Y |  |
| 16 | MATERIAL_RELEASED | 制令是否已完全发料 | number | Y |  |
| 17 | IS_ATP | 是否为ATP需求订单 | number | Y |  |
| 18 | PROJECT_ID | 计划批号 | string(120) | Y |  |
| 19 | PARENT_DEMAND_ORDER_ID | 此制令供给的需求订单 | string(120) | Y |  |
| 20 | PARENT_MFG_ORDER_ID | 此制令供给的上阶制令 | string(120) | Y |  |
| 21 | PARENT_SOURCE_MFG_ORDER |  | string(120) | Y |  |
| 22 | PRODUCED_QTY | 已生产量 | number(16,6) | Y |  |
| 23 | UNALLOCATE_QTY | 未分配量 | number(16,6) | Y |  |
| 24 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 25 | OWNER | 制令拥有者 | string(120) | Y |  |
| 26 | STATE | 制令执行状态 | number | Y |  |
| 27 | PLAN_UNIT | APS规划时之单位 | string(120) | Y |  |
| 28 | TRANSFER_RATE | 转换率 | number(16,8) | Y |  |
| 29 | BW_COMPLETE_DATE | 制令在Backward递推时的完工日 | date | Y |  |
| 30 | PO_CONSTRAINT_DATE | 关键物料进料限制时间点 | date | Y |  |
| 31 | SUBSTITUTE_QTY | 主料替他量 | number(16,6) | Y |  |
| 32 | P_SHORT_QTY | 预计短缺量 | number(16,6) | Y |  |
| 33 | R_CONSUM_QTY | 实际耗用量 | number(16,6) | Y |  |
| 34 | SUG_CREATE_QTY | SUG_CREATE_QTY | number(16,6) | Y |  |
| 35 | NEW_OWNER | 新拥有者 | string(120) | Y |  |
| 36 | HAS_ROUTE | 是否使用制令制程数据 | number | Y |  |
| 37 | SUPPLY_RULE_ID | 供给法则 | string(120) | Y |  |
| 38 | IS_AUTO_OS | 是否为自动转外包制令 | number | Y |  |
| 39 | IS_AUTO_PUR_MODI | 是否因自动外购而取消 | number | Y |  |
| 40 | OUTSOURCE_ID | 外包商编号 | string(120) | Y |  |
| 41 | ORIG_SUPPLY_RULE_ID | 原供给法则 | string(120) | Y |  |
| 42 | OS_CODE | 外包码 | number | Y |  |
| 43 | V_SUG_CREATE_QTY |  | number(16,6) | Y |  |
| 44 | SURPLUS_DEMAND_TYPE | 制令多余量需求建立模式 | number | Y |  |
| 45 | MOD_CONSUM_QTY | MOD订单耗用量 | number(16,6) | Y |  |
| 46 | BW_RELEASE_DATE | backward起始时间 | date | Y |  |
| 47 | F_CONSUM_QTY | 预测耗用量 | number(16,6) | Y |  |
| 48 | V_TO_R_CONSUM_QTY | 虚拟订单实际需求量 | number(16,6) | Y |  |
| 49 | MP_ROUTE_ID | MP途程编号 | string(160) | Y |  |
| 50 | IS_OUTSOURCING | 是否为外包 | number | Y |  |
| 51 | IS_LIMITED_BY_SR | 是否受供给法则限制 | number | Y |  |
| 52 | ITEM_CODE | 品号 | string(120) | Y |  |
| 53 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 54 | OWNER_ORG | 工厂 | string(120) | Y |  |
| 55 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 56 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 57 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 58 | LOT_MO_COMPLETE_DATE | 批工单预计移转日期 | date | Y |  |
| 59 | NETTING_TYPE_DOWN | 耗用特性继承 | number | Y |  |
| 60 | NETTING_TYPE | 耗用特性 | number | Y |  |
| 61 | MO_REMAIN_PROCESS_TIME | 剩餘產能 | number |  |  |
| 62 | BOM_DATE | BOM日期 | date | Y |  |
| 63 | VERSION_TIMES | BOM版次 | string(8) | Y |  |
| 64 | CreateDate | 创建日期 | date | Y |  |
| 65 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 66 | ModifiedDate | 修改日期 | date | Y |  |
| 67 | CreateBy | 创建者 | GUID | Y |  |
| 68 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 69 | ModifiedBy | 修改者 | GUID | Y |  |
| 70 | Attachments | 附件 | string | Y |  |
| 71 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 72 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 73 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 74 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 75 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 76 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 77 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 78 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 79 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 80 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 81 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 82 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 83 | UDF041 | 自定义字段12 | date | Y |  |
| 84 | UDF042 | 自定义字段13 | date | Y |  |
| 85 | UDF051 | 自定义字段14 | GUID | Y |  |
| 86 | UDF052 | 自定义字段15 | GUID | Y |  |
| 87 | UDF053 | 自定义字段16 | GUID | Y |  |
| 88 | UDF054 | 自定义字段17 | GUID | Y |  |
| 89 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 90 | Version | 版本号，不要随意更改 | binary | Y |  |
| 91 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 92 | ApproveDate | 修改日期 | date | Y |  |
| 93 | ApproveBy | 修改人 | GUID | Y |  |
| 94 | INTERNAL_ITEM |  | number(0/1) | Y |  |

### APS_OUT_MO_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MO_D_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | DEPEND_NUM | 領料序 | number(16,6) | Y |  |
| 4 | PRODUCT_NUM | 需求序號 | number | Y |  |
| 5 | INPUT_PART_ID | 元件品號 | string(210) | Y |  |
| 6 | COMPLETE_DATE | 預計完工日 | date | Y |  |
| 7 | RELEASE_DATE | 開立日 | date | Y |  |
| 8 | OUTPUT_PART_ID | 主件品號 | string(210) | Y |  |
| 9 | PROJECT_ID | 計畫批號 | string(120) | Y |  |
| 10 | USE_DATE | 預計領用日 | date | Y |  |
| 11 | USE_QTY | 應領用量 | number(16,6) | Y |  |
| 12 | IS_AUTOISSUE | 自動領料 | number | Y |  |
| 13 | ERP_ORDER_ID | EPR工單編號 | string(120) | Y |  |
| 14 | ORIG_INPUT_PART_ID | 原主料料號 | string(210) | Y |  |
| 15 | SOURCE_PART_ID | 上階需求料號 | string(210) | Y |  |
| 16 | PROJ_SHRINK_QTY | 耗率數量 | number(16,6) | Y |  |
| 17 | IS_CONSIGNED | 客供料 | number | Y |  |
| 18 | SUB_TYPE | 取替代型態 | number | Y |  |
| 19 | ITEM_CODE | 品號 | string(210) | Y |  |
| 20 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 21 | MO_ITEM_CODE | 工單品號 | string(210) | Y |  |
| 22 | MO_FEATURE_CODE | 工單特徵碼 | string(120) | Y |  |
| 23 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 24 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 25 | UP_LEVEL_ITEM_CODE | 上階品號 | string(210) | Y |  |
| 26 | UP_LEVEL_FEATURE_CODE | 上階特徵碼 | string(120) | Y |  |
| 27 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 28 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 29 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 30 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 31 | ITEM_TYPE | 材料類型 | string(120) | Y |  |
| 32 | ISSUE_OVERRUN_RATE | 超領率 | number(16,6) | Y |  |
| 33 | ISSUE_SHORTAGE_RATE | 缺領率 | number(16,6) | Y |  |
| 34 | OPERATION_ID | 作業編號 | string(120) | Y |  |
| 35 | ISSUE_MATERIAL_PERIOD | 投料間距 | number(16,6) | Y |  |
| 36 | REPLACED_QTY | 被取代數量 | number(16,6) | Y |  |
| 37 | GROUP_ALTCODE | 替代群組碼 | string(120) | Y |  |
| 38 | GROUP_CODE | 群祖碼 | string(120) | Y |  |
| 39 | GROUP_QTY | 供應套數 | number(16,6) | Y |  |
| 40 | SEQUENCE_TXT | BOM序號 | string(120) | Y |  |
| 41 | SEQU_ORDER | BOM順序號 | string(120) | Y |  |
| 42 | QTY_PER_VAR | 領料用量(變動) | number(16,6) | Y |  |
| 43 | QTY_PER_FIX | 領料用量(固定) | number(16,6) | Y |  |
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Attachments | 附件 | string | Y |  |
| 51 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 52 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 53 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 54 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 55 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 56 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 57 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 58 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 59 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 60 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 61 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 62 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 63 | UDF041 | 自定义字段12 | date | Y |  |
| 64 | UDF042 | 自定义字段13 | date | Y |  |
| 65 | UDF051 | 自定义字段14 | GUID | Y |  |
| 66 | UDF052 | 自定义字段15 | GUID | Y |  |
| 67 | UDF053 | 自定义字段16 | GUID | Y |  |
| 68 | UDF054 | 自定义字段17 | GUID | Y |  |
| 69 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 70 | Version | 版本号，不要随意更改 | binary | Y |  |
| 71 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 72 | ApproveDate | 修改日期 | date | Y |  |
| 73 | ApproveBy | 修改人 | GUID | Y |  |
| 74 | COMPONENT_LOCATION | 插件位置 | string | Y |  |

### APS_OUT_MO_MATREQ

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MO_MATREQ_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | ROUTE_ID | 途程編號 | string(160) | Y |  |
| 4 | SEQU_NUM | 加工序號 | string(120) | Y |  |
| 5 | OPERATION_ID | 作業編號 | string(120) | Y |  |
| 6 | INPUT_PART_ID | 元件品號 | string(210) | Y |  |
| 7 | REQUIRE_TIME | 需求日期 | date | Y |  |
| 8 | ITEM_CODE | 品號 | string(210) | Y |  |
| 9 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 10 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 11 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 12 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 13 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MO_PEG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MO_PEG_ID | 主键 | GUID | Y | Y |
| 2 | FED_ORDER_ID | FED_ORDER_ID | string(120) | Y |  |
| 3 | DEMAND_QTY | DEMAND_QTY | number(16,6) | Y |  |
| 4 | FEDED_ORDER_ID | FEDED_ORDER_ID | string(120) | Y |  |
| 5 | IS_DEMAND | IS_DEMAND | number | Y |  |
| 6 | FED_QTY | FED_QTY | number(16,6) | Y |  |
| 7 | IS_STOCK | IS_STOCK | number | Y |  |
| 8 | SUPPLY_QTY | SUPPLY_QTY | number(16,6) | Y |  |
| 9 | IS_LOCK | IS_LOCK | number | Y |  |
| 10 | PART_ID | PART_ID | string(210) | Y |  |
| 11 | REQUIRE_TIME | REQUIRE_TIME | date | Y |  |
| 12 | PEG_SEQ | PEG_SEQ | number | Y |  |
| 13 | IS_PO_MOST_CRITICAL | IS_PO_MOST_CRITICAL | number | Y |  |
| 14 | ITEM_CODE | ITEM_CODE | string(120) | Y |  |
| 15 | FEATURE_CODE | FEATURE_CODE | string(120) | Y |  |
| 16 | ORIG_PART_ID | ORIG_PART_ID | string(210) | Y |  |
| 17 | REPLACED_ITEM_CODE | REPLACED_ITEM_CODE | string(120) | Y |  |
| 18 | REPLACED_FEATURE_CODE | REPLACED_FEATURE_CODE | string(120) | Y |  |
| 19 | SUB_TYPE | SUB_TYPE | number | Y |  |
| 20 | UNIQUE_ID | UNIQUE_ID | string(120) | Y |  |
| 21 | USE_DIFFERENT_PRODUCT | USE_DIFFERENT_PRODUCT | number | Y |  |
| 22 | GROUP_QTY | GROUP_QTY | number(16,6) | Y |  |
| 23 | SUPER_ORDER_ID | SUPER_ORDER_ID | string(120) | Y |  |
| 24 | DEPEND_NUM | DEPEND_NUM | number(16,6) | Y |  |
| 25 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 26 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 27 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 28 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Attachments | 附件 | string | Y |  |
| 36 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 37 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 38 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 39 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 40 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 41 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 42 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 43 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 44 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 45 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 46 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 47 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 48 | UDF041 | 自定义字段12 | date | Y |  |
| 49 | UDF042 | 自定义字段13 | date | Y |  |
| 50 | UDF051 | 自定义字段14 | GUID | Y |  |
| 51 | UDF052 | 自定义字段15 | GUID | Y |  |
| 52 | UDF053 | 自定义字段16 | GUID | Y |  |
| 53 | UDF054 | 自定义字段17 | GUID | Y |  |
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MO_PROCESS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MO_PROCESS_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | ROUTE_ID | 途程編號 | string(160) | Y |  |
| 4 | SEQU_NUM | 加工序號 | string(120) | Y |  |
| 5 | OPERATION_ID | 作業編號 | string(120) | Y |  |
| 6 | IS_OUTSOURCING | 外包 | number | Y |  |
| 7 | EQUIP_TYPE | 資源型態 | number | Y |  |
| 8 | EQUIP_ID | 資源編號 | string(120) | Y |  |
| 9 | SKL_SEQ | 排程順序 | number | Y |  |
| 10 | MFG_QTY | 製造數量 | number(16,6) | Y |  |
| 11 | START_TIME | 開始時間 | date | Y |  |
| 12 | END_TIME | 完成時間 | date | Y |  |
| 13 | WS_ID | 工作中心編號 | string(120) | Y |  |
| 14 | EQUIP_GROUP_ID | 資源群組編號 | string(120) | Y |  |
| 15 | EST | 最早可開工日 | date | Y |  |
| 16 | LET | 最晚需完工時間 | date | Y |  |
| 17 | IS_PARALLEL | 平行資源任務 | number | Y |  |
| 18 | IS_SETUP_SAVING | 連批 | number | Y |  |
| 19 | LACK_TIME | 壓縮時間 | number(16,6) | Y |  |
| 20 | OVERLAP_RATIO | 產能重疊比例 | number(16,6) | Y |  |
| 21 | IS_SCHEDULED_END | 超出排程邊界 | number | Y |  |
| 22 | SETUP_START_TIME | 整備開始時間 | date | Y |  |
| 23 | SETUP_END_TIME | 整備結束時間 | date | Y |  |
| 24 | PROCESS_START_TIME | 加工開始時間 | date | Y |  |
| 25 | PROCESS_END_TIME | 加工結束時間 | date | Y |  |
| 26 | SETUP_CYCLE_TIME | 整備製造週期 | number | Y |  |
| 27 | PROCESS_CYCLE_TIME | 加工製造週期 | number | Y |  |
| 28 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 29 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 30 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 31 | PLAN_LEVEL | 規劃層級 | string(20) | Y |  |
| 32 | PRE_OP_START_TIME | 前置開始時間 | date | Y |  |
| 33 | PRE_OP_END_TIME | 前置結束時間 | date | Y |  |
| 34 | POST_OP_START_TIME | 後置開始時間 | date | Y |  |
| 35 | POST_OP_END_TIME | 後置結束時間 | date | Y |  |
| 36 | PRE_OP_CYCLE_TIME | 前置週期時間 | number | Y |  |
| 37 | POST_OP_CYCLE_TIME | 後置週期時間 | number | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MO_PRODUCT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MO_PRODUCT_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | ITEM_CODE | 品號 | string(210) | Y |  |
| 4 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 5 | PRODUCT_TYPE | 產出類型 | string(120) | Y |  |
| 6 | PLAN_QTY | 預計產出數量 | number(16,6) | Y |  |
| 7 | PRODUCT_RATE | 產出比率 | number(16,6) | Y |  |
| 8 | COST_RATE | 成本利率 | number(16,6) | Y |  |
| 9 | REMARK | 備註 | string(400) | Y |  |
| 10 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 11 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 12 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 13 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MOPPEG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MOPPEG_ID | 主键 | GUID | Y | Y |
| 2 | INPUT_MFG_ORDER_ID | 上階工單單號 | string(120) | Y |  |
| 3 | INPUT_SEQU_NUM | 上階製程式號 | string(120) | Y |  |
| 4 | INPUT_EQUIP_TYPE | 上階製程資源型態 | number | Y |  |
| 5 | INPUT_IS_OUTSOURCING | 上階製程是否外包 | number | Y |  |
| 6 | INPUT_EQUIP_ID | 上階製程資源編號 | string(120) | Y |  |
| 7 | OUTPUT_MFG_ORDER_ID | 下階工單單號 | string(120) | Y |  |
| 8 | OUTPUT_SEQU_NUM | 下階製程式號 | string(120) | Y |  |
| 9 | OUTPUT_EQUIP_TYPE | 下階製程資源型態 | number | Y |  |
| 10 | OUTPUT_IS_OUTSOURCING | 下階製程外包 | number | Y |  |
| 11 | OUTPUT_EQUIP_ID | 下階製程資源編號 | string(120) | Y |  |
| 12 | PARENT_DO_ID | 來源訂單 | string(120) | Y |  |
| 13 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 14 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 15 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 16 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MR_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | DEPEND_NUM | 領料序 | number(16,6) | Y |  |
| 4 | PRODUCT_NUM | 需求序號 | number | Y |  |
| 5 | INPUT_PART_ID | 元件品號 | string(210) | Y |  |
| 6 | COMPLETE_DATE | 預計完工日 | date | Y |  |
| 7 | RELEASE_DATE | 開立日 | date | Y |  |
| 8 | OUTPUT_PART_ID | 主件品號 | string(210) | Y |  |
| 9 | PROJECT_ID | 計畫批號 | string(120) | Y |  |
| 10 | USE_DATE | 預計領用日 | date | Y |  |
| 11 | USE_QTY | 應領用量 | number(16,6) | Y |  |
| 12 | IS_AUTOISSUE | 自動領料 | number | Y |  |
| 13 | ERP_ORDER_ID | EPR工單編號 | string(120) | Y |  |
| 14 | ORIG_INPUT_PART_ID | 原主料料號 | string(210) | Y |  |
| 15 | SOURCE_PART_ID | 上階需求料號 | string(210) | Y |  |
| 16 | PROJ_SHRINK_QTY | 耗率數量 | number(16,6) | Y |  |
| 17 | IS_CONSIGNED | 客供料 | number | Y |  |
| 18 | ITEM_CODE | 品號 | string(210) | Y |  |
| 19 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 20 | MO_ITEM_CODE | 工單品號 | string(210) | Y |  |
| 21 | MO_FEATURE_CODE | 工單特徵碼 | string(120) | Y |  |
| 22 | REPLACED_ITEM_CODE | 需求(主料)品號 | string(210) | Y |  |
| 23 | REPLACED_FEATURE_CODE | 需求品號特徵碼 | string(210) | Y |  |
| 24 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 25 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 26 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 27 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 28 | GROUP_ALTCODE | 替代群組碼 | string(120) | Y |  |
| 29 | GROUP_CODE | 群祖碼 | string(120) | Y |  |
| 30 | GROUP_QTY | 供給上階相對數量 | number(16,6) | Y |  |
| 31 | SEQU_ORDER | BOM順序號 | string(120) | Y |  |
| 32 | QTY_PER_VAR | 領料用量(變動) | number(16,6) | Y |  |
| 33 | QTY_PER_FIX | 領料用量(固定) | number(16,6) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MRP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MRP_ID | 主键 | GUID | Y | Y |
| 2 | SERIAL_NUM | 流水編號 | number | Y |  |
| 3 | SD_TIME | 供需日期 | date | Y |  |
| 4 | ORDER_UNFULFILL_QTY | 訂單未交量 | number(16,6) | Y |  |
| 5 | FORECAST_QTY | 計畫出貨量 | number(16,6) | Y |  |
| 6 | SAFTY_STOCK_QTY | 安全庫存量 | number(16,6) | Y |  |
| 7 | ATP_QTY | ATP需求量 | number(16,6) | Y |  |
| 8 | SUB_ORDER_UNFULFILL_QTY | 訂單未交替他需求量 | number(16,6) | Y |  |
| 9 | SUB_FORECAST_QTY | 預測替他需求量 | number(16,6) | Y |  |
| 10 | SUB_ATP_QTY | ATP替他需求量 | number(16,6) | Y |  |
| 11 | PLAN_MO_MAT_QTY | 計劃備料量 | number(16,6) | Y |  |
| 12 | SUB_PLAN_MO_MAT_QTY | 計劃備料替他需求量 | number(16,6) | Y |  |
| 13 | MO_MAT_QTY | 工單備料量 | number(16,6) | Y |  |
| 14 | SUB_MO_MAT_QTY | 工單備料替他需求量 | number(16,6) | Y |  |
| 15 | MO_MAT_QTY_RED | 備料重排減少量 | number(16,6) | Y |  |
| 16 | MO_MAT_QTY_ADD | 備料重排增加量 | number(16,6) | Y |  |
| 17 | INVENTORY_QTY | 庫存單位數量 | number(16,6) | Y |  |
| 18 | INSPECTED_QTY | 採購待入庫數量 | number(16,6) | Y |  |
| 19 | SUB_INVENTORY_QTY | 替代庫存量 | number(16,6) | Y |  |
| 20 | PR_QTY | 請購量 | number(16,6) | Y |  |
| 21 | IN_PURCHASE_QTY | 待進貨量 | number(16,6) | Y |  |
| 22 | INTRANSIT_QTY | 待撥入量 | number(16,6) | Y |  |
| 23 | UNRELEASED_WIP_QTY | 未發放在製量 | number(16,6) | Y |  |
| 24 | RELEASED_WIP_QTY | 已發放在製量 | number(16,6) | Y |  |
| 25 | SUB_PR_QTY | 替代請購量 | number(16,6) | Y |  |
| 26 | SUB_PURCHASE_QTY | 替代在製量 | number(16,6) | Y |  |
| 27 | SUB_WIP_QTY | 替代在製量 | number(16,6) | Y |  |
| 28 | RES_DUE_DATE_RED | 重排減少量 | number(16,6) | Y |  |
| 29 | RES_DUE_DATE_ADD | 重排增加量 | number(16,6) | Y |  |
| 30 | ON_HAND | 預估結存 | number(16,6) | Y |  |
| 31 | PLAN_PURCHASE_QTY | 規劃採購量 | number(16,6) | Y |  |
| 32 | SUB_PLAN_PURCHASE_QTY | 替代規劃採購量 | number(16,6) | Y |  |
| 33 | PLAN_MFG_QTY | 規劃製造量 | number(16,6) | Y |  |
| 34 | SUB_PLAN_MFG_QTY | 替代規劃製造量 | number(16,6) | Y |  |
| 35 | PROJECTED_ON_HAND | 預計結存 | number(16,6) | Y |  |
| 36 | PLAN_ON_HAND | 規劃結存 | number(16,6) | Y |  |
| 37 | ITEM_CODE | 品號 | string(210) | Y |  |
| 38 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 39 | TIME_BUCKET_ID | 時距編號(GUID) | string(120) | Y |  |
| 40 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 41 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 42 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 43 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 44 | INSPECTING_QTY | 採購在驗數量 | number(16,6) | Y |  |
| 45 | RESERVED_ORDER_QTY | 行政保留量 | number(16,6) | Y |  |
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | Attachments | 附件 | string | Y |  |
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
| 71 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 72 | Version | 版本号，不要随意更改 | binary | Y |  |
| 73 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 74 | ApproveDate | 修改日期 | date | Y |  |
| 75 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_MRP_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_MRP_D_ID | 主键 | GUID | Y | Y |
| 2 | B_REAL_SD_TIME | 實際供需區間 | date | Y |  |
| 3 | REAL_SD_TIME | 供需日期(實際) | date | Y |  |
| 4 | SD_TYPE | 供需類別 | string(120) | Y |  |
| 5 | SOURCE_ORDER_ID | 來源單號 | string(120) | Y |  |
| 6 | SOURCE_ORDER_SERIAL | 來源項次 | string(120) | Y |  |
| 7 | IS_DUE_FIRM | 凍結交期 | number | Y |  |
| 8 | QTY | 數量 | number(16,6) | Y |  |
| 9 | B_PLAN_SD_TIME | 規劃供需區間 | date | Y |  |
| 10 | PLAN_SD_TIME | 供需日期 | date | Y |  |
| 11 | ITEM_CODE | 品號 | string(210) | Y |  |
| 12 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 13 | MO_ITEM_CODE | 工單品號 | string(210) | Y |  |
| 14 | MO_FEATURE_CODE | 工單特徵碼 | string(120) | Y |  |
| 15 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 16 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 17 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 18 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 19 | REPLACED_ITEM_CODE | 被替代品號 | string(210) | Y |  |
| 20 | REPLACED_FEATURE_CODE | 被替代特徵碼 | string(120) | Y |  |
| 21 | SUB_TYPE | 替代型態 | number | Y |  |
| 22 | SUPPLY_DEMAND_TYPE | 供需碼 | string(120) | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_ORDER_PEG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_ORDER_PEG_ID | 主键 | GUID | Y | Y |
| 2 | FED_ORDER_ID | 供給單號 | string(120) | Y |  |
| 3 | FEDED_ORDER_ID | 被供給單號 | string(120) | Y |  |
| 4 | IS_DEMAND | 訂單需求 | number | Y |  |
| 5 | IS_LOCK | 鎖定供需 | number | Y |  |
| 6 | IS_STOCK | 採購件 | number | Y |  |
| 7 | PARENT | 最上層需求單據 | string(120) | Y |  |
| 8 | LEVEL_CODE | 低階碼 | number | Y |  |
| 9 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 10 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 11 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 12 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_PO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_PO_ID | 主键 | GUID | Y | Y |
| 2 | PURCHASE_ORDER_ID | 采购令编号 | string(120) | Y |  |
| 3 | PART_ID | 订购品项 | string(120) | Y |  |
| 4 | PURCHASE_QTY | 预计采购数量 | number(16,6) | Y |  |
| 5 | IS_NEW | 是否开启采购单 | number | Y |  |
| 6 | FIRM_RELEASE_DATE | ERP预计开立日期 | date | Y |  |
| 7 | FIRM_AVAILABLE_DATE | ERP预计抵达(到厂)日期 | date | Y |  |
| 8 | PLAN_RELEASE_DATE | APS开立日期 | date | Y |  |
| 9 | PLAN_AVAILABLE_DATE | APS抵达(到厂)日期 | date | Y |  |
| 10 | SUPPLIER_ID | 供货商编号 | string(120) | Y |  |
| 11 | ERP_ORDER_ID | EPR中对应的采购令单号 | string(120) | Y |  |
| 12 | UNIT_ID | 采购单位 | string(120) | Y |  |
| 13 | PROJECT_ID | 计划批号 | string(120) | Y |  |
| 14 | IS_ATP |  | number | Y |  |
| 15 | LOCATION | 供货商位置 | string(120) | Y |  |
| 16 | PARENT_DEMAND_ORDER_ID | 采购令供给的需求订单 | string(120) | Y |  |
| 17 | PARENT_MFG_ORDER_ID | 采购令供给的上阶制令 | string(120) | Y |  |
| 18 | PARENT_SOURCE_MFG_ORDER |  | string(120) | Y |  |
| 19 | STOCKED_QTY | 采购令已入库数量 | number(16,6) | Y |  |
| 20 | UNALLOCATE_QTY | 未被耗用的量 | number(16,6) | Y |  |
| 21 | IS_HOLD | 采购令是否为保留状态 | number | Y |  |
| 22 | OWNER | 采购令拥有者 | string(120) | Y |  |
| 23 | STATE | 采购单据执行状态 | number | Y |  |
| 24 | PLAN_UNIT_ID | APS规划时之单位 | string(120) | Y |  |
| 25 | TRANSFER_RATE | 转换率 | number(16,8) | Y |  |
| 26 | IS_FIRM | 否锁定不可移动 | number | Y |  |
| 27 | UNINSPECT_QTY | 待验量 | number(16,6) | Y |  |
| 28 | UNSTOCKED_QTY | 待入库量 | number(16,6) | Y |  |
| 29 | RETURN_QTY | 验退量 | number(16,6) | Y |  |
| 30 | SUBSTITUTE_QTY | 主料替他量 | number(16,6) | Y |  |
| 31 | R_CONSUM_QTY | 实际耗用量 | number(16,6) | Y |  |
| 32 | SUG_CREATE_QTY |  | number(16,6) | Y |  |
| 33 | BW_COMPLETE_DATE | 采购在MP的Backward阶段所计算出的交期 | date | Y |  |
| 34 | NEW_OWNER | 新拥有者 | string(120) | Y |  |
| 35 | SUPPLY_RULE_ID | 供给法则 | string(120) | Y |  |
| 36 | IS_AUTO_PUR | 是否为制造转采购单 | number | Y |  |
| 37 | IS_AUTO_PUR_MODI | 是否因自动外购而取消 | number | Y |  |
| 38 | AUTO_PUR_MO_ID | 自动转外购前的工单单号 | string(120) | Y |  |
| 39 | ORIG_SUPPLY_RULE_ID | 原始的供给法则 | string(120) | Y |  |
| 40 | LEAD_TIME | 采购令的前置时间 | number(16,6) | Y |  |
| 41 | V_SUG_CREATE_QTY |  | number(16,6) | Y |  |
| 42 | FIRM_SUPPLY_DATE | ERP预计到库日期 | date | Y |  |
| 43 | PLAN_SUPPLY_DATE | APS预计到库日期 | date | Y |  |
| 44 | MOD_CONSUM_QTY | MOD订单耗用量 | number(16,6) | Y |  |
| 45 | BW_RELEASE_DATE | backward起始时间 | date | Y |  |
| 46 | F_CONSUM_QTY | 预测耗用量 | number(16,6) | Y |  |
| 47 | V_TO_R_CONSUM_QTY | 虚拟订单实际需求量 | number(16,6) | Y |  |
| 48 | ITEM_CODE | 品号 | string(120) | Y |  |
| 49 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 50 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 51 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 52 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 53 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 54 | RELEASE_LACK_DAY | 是否延迟到货 | number | Y |  |
| 55 | DELAY_AVAIABLE_DATE | 延迟到货天数 | number | Y |  |
| 56 | NETTING_TYPE_DOWN | 耗用特性继承 | number | Y |  |
| 57 | NETTING_TYPE | 耗用特性 | number | Y |  |
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | Attachments | 附件 | string | Y |  |
| 65 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 66 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 67 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 68 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 69 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 70 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 71 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 72 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 73 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 74 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 75 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 76 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 77 | UDF041 | 自定义字段12 | date | Y |  |
| 78 | UDF042 | 自定义字段13 | date | Y |  |
| 79 | UDF051 | 自定义字段14 | GUID | Y |  |
| 80 | UDF052 | 自定义字段15 | GUID | Y |  |
| 81 | UDF053 | 自定义字段16 | GUID | Y |  |
| 82 | UDF054 | 自定义字段17 | GUID | Y |  |
| 83 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 84 | Version | 版本号，不要随意更改 | binary | Y |  |
| 85 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 86 | ApproveDate | 修改日期 | date | Y |  |
| 87 | ApproveBy | 修改人 | GUID | Y |  |
| 88 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 89 | SOURCE_ID_ROid |  | GUID | Y |  |
| 90 | INTERNAL_ITEM |  | number(0/1) | Y |  |

### APS_OUT_RECENTPR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_RECENTPR_ID | 主键 | GUID | Y | Y |
| 2 | PR_DOC_ID | ERP單號 | string(120) | Y |  |
| 3 | PURCHASE_ORDER_ID | 採購單編號 | string(120) | Y |  |
| 4 | SUPPLY_DEMAND_PLAN_ID | ERP採購計劃ID | string(120) | Y |  |
| 5 | SUPPLY_DEMAND_PLAN_D_ID | ERP採購計劃單身ID | string(120) | Y |  |
| 6 | DOC_ID | 單據類型 | string(120) | Y |  |
| 7 | DOC_DATE | 單據日期 | date | Y |  |
| 8 | ITEM_ID | 品號(GUID) | string(210) | Y |  |
| 9 | ITEM_FEATURE_ID | 特徵碼(GUID) | string(120) | Y |  |
| 10 | ERP_UNIT_ID | ERP單位 | string(120) | Y |  |
| 11 | BUSINESS_QTY | 業務數量 | number(16,6) | Y |  |
| 12 | SECOND_QTY | 第二單位數量 | number(16,6) | Y |  |
| 13 | INV_QTY | 庫存單位數量 | number(16,6) | Y |  |
| 14 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 15 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 16 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 17 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
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
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_SUB_SUPPLY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_SUB_SUPPLY_ID | 主键 | GUID | Y | Y |
| 2 | PART_ID | 品號 | string(210) | Y |  |
| 3 | SUB_PART_ID | 替代料號 | string(210) | Y |  |
| 4 | SUPPLY_TYPE | 供給型態 | string(120) | Y |  |
| 5 | WAREHOUSE_ID | 庫別 | string(120) | Y |  |
| 6 | STOCK_LOCATION | 供給庫位 | string(120) | Y |  |
| 7 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 8 | PUR_ORDER_ID | 供給採購單編號 | string(120) | Y |  |
| 9 | SUB_MAIN_QTY | 替代料供給量 | number(16,6) | Y |  |
| 10 | SUB_QTY | 替代料供給量 | number(16,6) | Y |  |
| 11 | ITEM_CODE | 品號 | string(210) | Y |  |
| 12 | FEATURE_CODE | 品號特徵碼 | string(210) | Y |  |
| 13 | REPLACE_ITEM_CODE | 替代品號 | string(210) | Y |  |
| 14 | REPLACE_FEATURE_CODE | 替代特徵碼 | string(120) | Y |  |
| 15 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 16 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 17 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 18 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
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
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_SUPPLY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_SUPPLY_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_SOURCE_ID | 需求來源編號 | string(120) | Y |  |
| 3 | DEMAND_SOURCE_TYPE | 需求來源型態 | number | Y |  |
| 4 | DEMAND_SEQUENCE | 需求序 | number | Y |  |
| 5 | ALLOCATE_SEQUENCE | 分配序 | number | Y |  |
| 6 | SUBSTITUTE_SEQUENCE | 替代序 | number | Y |  |
| 7 | SUPPLY_SEQUENCE | 供給序 | number | Y |  |
| 8 | SUPPLY_TYPE | 供給型態 | string(120) | Y |  |
| 9 | SUPPLY_ORDER_ID | 供給單號 | string(120) | Y |  |
| 10 | SUPPLY_WH_ID | 供給庫別 | string(120) | Y |  |
| 11 | SUPPLY_SL_ID | 供給庫位 | string(120) | Y |  |
| 12 | SUPPLY_QTY | 可供給數量 | number(16,6) | Y |  |
| 13 | SUPPLY_TIME | 供給時間 | date | Y |  |
| 14 | ORIG_SUPPLY_QTY | 原供給量 | number(16,6) | Y |  |
| 15 | UNIQ_CODE | 唯一碼 | number | Y |  |
| 16 | PARENT_UNIQ_CODE | 上階唯一碼 | number | Y |  |
| 17 | INSPECTING_QTY | 採購在驗數量 | number(16,6) | Y |  |
| 18 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 19 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 20 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 21 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 22 | USE_DIFFERENT_PRODUCT | 聯副產品 | number | Y |  |
| 23 | UNIQUE_ID | 唯一碼 | string(120) | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Attachments | 附件 | string | Y |  |
| 31 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 32 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 33 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 34 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 35 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 36 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 37 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 38 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 39 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 40 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 41 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 42 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 43 | UDF041 | 自定义字段12 | date | Y |  |
| 44 | UDF042 | 自定义字段13 | date | Y |  |
| 45 | UDF051 | 自定义字段14 | GUID | Y |  |
| 46 | UDF052 | 自定义字段15 | GUID | Y |  |
| 47 | UDF053 | 自定义字段16 | GUID | Y |  |
| 48 | UDF054 | 自定义字段17 | GUID | Y |  |
| 49 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_TIMEBUCKET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_TIMEBUCKET_ID | 主键 | GUID | Y | Y |
| 2 | TIME_BUCKET_CODE | 時距編號 | string(120) | Y |  |
| 3 | TIME_BUCKET_ID | 時距編號(GUID) | string(120) | Y |  |
| 4 | TIME_BUCKET_TYPE | 時距方式 | string(120) | Y |  |
| 5 | START_TIME | 開始時間 | date | Y |  |
| 6 | END_TIME | 完成時間 | date | Y |  |
| 7 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 8 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 9 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 10 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
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
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OUT_TIMEBUCKET_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OUT_TIMEBUCKET_D_ID | 主键 | GUID | Y | Y |
| 2 | TIME_BUCKET_CODE | 時距編號 | string(120) | Y |  |
| 3 | TIME_BUCKET_ID | 時距編號(GUID) | string(120) | Y |  |
| 4 | START_TIME | 開始時間 | date | Y |  |
| 5 | DEMAND_TIME | 需求日 | date | Y |  |
| 6 | OFF_DAY_FLAG | 假日 | number | Y |  |
| 7 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 8 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 9 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 10 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
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
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |

### APS_OVERTIME

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_OVERTIME_ID | 主键 | GUID | Y | Y |
| 2 | IS_OUTSOURCING |  | number | Y |  |
| 3 | EQUIP_TYPE |  | number | Y |  |
| 4 | RESOURCE_CODE |  | string(120) | Y |  |
| 5 | CALENDAR_DATE |  | date | Y |  |
| 6 | START_TIME |  | number | Y |  |
| 7 | END_TIME |  | number |  |  |
| 8 | OVERTIME_TYPE |  | number |  |  |
| 9 | IS_SCHEDULED |  | number |  |  |
| 10 | CUS_STRING1 |  | string(120) |  |  |
| 11 | CUS_STRING2 |  | string(120) |  |  |
| 12 | CUS_STRING3 |  | string(120) |  |  |
| 13 | CUS_NUMERIC1 |  | number |  |  |
| 14 | CUS_NUMERIC2 |  | number(17,6) |  |  |
| 15 | CUS_NUMERIC3 |  | number(17,6) |  |  |
| 16 | CUS_DATE1 |  | date |  |  |
| 17 | CUS_DATE2 |  | date |  |  |
| 18 | WORK_TIME |  | number | Y |  |
| 19 | OWNER_ORG |  | string(120) | Y |  |
| 20 | PLAN_STRATEGY_CODE |  | string(120) | Y |  |
| 21 | CASE_CODE |  | string(120) | Y |  |
| 22 | PLAN_LEVEL |  | string(120) | Y |  |
| 23 | ORIG_WORK_TIME |  | number |  |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Attachments | 附件 | string | Y |  |
| 31 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 32 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 33 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 34 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 35 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 36 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 37 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 38 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 39 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 40 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 41 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 42 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 43 | UDF041 | 自定义字段12 | date | Y |  |
| 44 | UDF042 | 自定义字段13 | date | Y |  |
| 45 | UDF051 | 自定义字段14 | GUID | Y |  |
| 46 | UDF052 | 自定义字段15 | GUID | Y |  |
| 47 | UDF053 | 自定义字段16 | GUID | Y |  |
| 48 | UDF054 | 自定义字段17 | GUID | Y |  |
| 49 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |

### APS_PLAN_CASE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_PLAN_CASE_ID | 主键 | GUID | Y | Y |
| 2 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 3 | CASE_NAME | 案例描述 | string(120) | Y |  |
| 4 | CASE_MODI_TIME | 案例修改時間 | date | Y |  |
| 5 | PLAN_CASE_ALIAS | 案例別名 | string(120) | Y |  |
| 6 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 7 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 8 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |

### APS_PLAN_RESOURCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_PLAN_RESOURCE_ID | 主键 | GUID | Y | Y |
| 2 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 3 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 4 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 5 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 6 | RESOURCE_CODE | 資源編號 | string(120) | Y |  |
| 7 | REMARK | 備註 | string(400) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
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
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |

### APS_PLAN_STRATEGY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_PLAN_STRATEGY_ID | 主键 | GUID | Y | Y |
| 2 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 3 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 4 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 5 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 6 | PLAN_STRATEGY_NAME | 規劃策略名稱 | string(120) | Y |  |
| 7 | MDS_LEVEL | 是否啟動MDS參數 | number | Y |  |
| 8 | MPS_LEVEL | 是否啟動MPS | number | Y |  |
| 9 | MRP_LEVEL | 是否啟動MRP | number | Y |  |
| 10 | MDS_OFFSET_RULE | 沖銷原則 | number | Y |  |
| 11 | MDS_DEMAND_TIME_FENCE | 需求柵欄 | number | Y |  |
| 12 | MDS_DEMAND_PRIORITY_ORDER | 需求優先順序 | string(120) | Y |  |
| 13 | MDS_DEMAND_TYPE | 需求形式 | string(120) | Y |  |
| 14 | MPS_DEMAND_SOURCE | 需求來源 | string(120) | Y |  |
| 15 | MPS_FORECAST_ALLOCATION | 預測分配 | string(120) | Y |  |
| 16 | MPS_MO_ALLOCATION | 在制工單計算方式 | string(120) | Y |  |
| 17 | MPS_TRANSFER_LOT_FLAG | 是否考慮移轉批量 | number | Y |  |
| 18 | MPS_ATTRITION_RATE_FLAG | 是否考慮損耗率 | number | Y |  |
| 19 | MPS_REPLACE_FLAG | 是否考慮取代料 | number | Y |  |
| 20 | MPS_ALTERNATIVE_FLAG | 是否考慮替代料 | number | Y |  |
| 21 | MPS_REQUIREMENT_CALCULATION | 需求計算方式 | string(400) | Y |  |
| 22 | MRP_TIME_BUCKET | 時距設定 | string(400) | Y |  |
| 23 | MRP_TIME_BUCKET_ID | 時距編號 | GUID | Y |  |
| 24 | MRP_DEMAND_SOURCE | 需求來源 | string(400) | Y |  |
| 25 | MRP_FORECAST_ALLOCATION | 預測分配 | string(400) | Y |  |
| 26 | MRP_PROCUREMENT_PLAN | 預測分配 | string(400) | Y |  |
| 27 | MRP_ATTRITION_RATE_FLAG | 是否考慮損耗率 | number | Y |  |
| 28 | MRP_REPLACE_FLAG | 是否考慮取代料 | number | Y |  |
| 29 | MRP_ALTERNATIVE_FLAG | 是否考慮替代料 | number | Y |  |
| 30 | MRP_PRODUCTION_PLAN_FLAG | 是否生成生產計畫 | number | Y |  |
| 31 | MRP_REQUIREMENT_CALCULATION | 需求計算方式 | string(120) | Y |  |
| 32 | REMARK | 備註 | string(400) | Y |  |
| 33 | MDS_ID | MDS編號 | string(120) | Y |  |
| 34 | VERSION_TIMES | MDS版號 | string(120) | Y |  |
| 35 | OUTSOURCING_FLAG | 啟用外包 | number | Y |  |
| 36 | OVERTIME_FLAG | 啟用加班 | number | Y |  |
| 37 | KEEP_DUE_DATE | 嚴守交期 | number | Y |  |
| 38 | MPS_SCHEDULING_STRATEGY | 排程策略 | string(120) | Y |  |
| 39 | MPS_LEAD_TIME | 提前天數 | number | Y |  |
| 40 | MPS_REPLACE_ALTERNATIVE_RULE | 廢止 | string(120) | Y |  |
| 41 | MPS_ORIGINAL_ITEM_FLAG | 廢止 | number | Y |  |
| 42 | MRP_REPLACE_ALTERNATIVE_RULE | 廢止 | string(120) | Y |  |
| 43 | MRP_ORIGINAL_ITEM_FLAG | 廢止 | number | Y |  |
| 44 | INCLUDE_FORECAST | 納入預測 | number | Y |  |
| 45 | INCLUDE_ORDER | 納入訂單 | number | Y |  |
| 46 | INCLUDE_SAFETYSTOCK | 納入安全存量 | number | Y |  |
| 47 | INCLUDE_MO_D | 納入工單領料需求 | number | Y |  |
| 48 | INCLUDE_INVENTORY | 納入庫存 | number | Y |  |
| 49 | INCLUDE_MO | 納入工單 | number | Y |  |
| 50 | INCLUDE_PR | 納入請購單 | number | Y |  |
| 51 | INCLUDE_PO | 納入採購單 | number | Y |  |
| 52 | INCLUDE_TRANSFER | 納入調撥單 | number | Y |  |
| 53 | INCLUDE_LOCKEDPLAN | 納入鎖定計畫量 | number | Y |  |
| 54 | MRP_TRANSFER_LOT_FLAG | 是否考慮移轉批量 | number | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | Attachments | 附件 | string | Y |  |
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
| 80 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 81 | Version | 版本号，不要随意更改 | binary | Y |  |
| 82 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 83 | ApproveDate | 修改日期 | date | Y |  |
| 84 | ApproveBy | 修改人 | GUID | Y |  |
| 85 | MRP_SAFT_STOCK_PRIORITY | 安全库存需求优先级 | number | Y |  |
| 86 | MPS_SAFT_STOCK_PRIORITY | 安全库存需求优先级 | number | Y |  |

### APS_PO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_PO_ID | 主键 | GUID | Y | Y |
| 2 | PURCHASE_ORDER_ID | 采购令编号 | string(120) | Y |  |
| 3 | ITEM_CODE | 品号 | string(120) | Y |  |
| 4 | PURCHASE_QTY | 采购令预计采购数量 | number(16,6) | Y |  |
| 5 | IS_NEW |  | number | Y |  |
| 6 | FIRM_RELEASE_DATE | ERP预计开立日期 | date | Y |  |
| 7 | FIRM_AVAILABLE_DATE | ERP预计抵达(到厂)日期 | date | Y |  |
| 8 | SUPPLIER_ID | 供货商编号 | string(120) | Y |  |
| 9 | ERP_ORDER_ID | EPR中对应的采购令单号 | string(120) | Y |  |
| 10 | UNIT_ID | 采购单位 | string(120) | Y |  |
| 11 | PROJECT_ID | 计划批号 | string(120) | Y |  |
| 12 | STOCKED_QTY | 采购令已入库数量 | number(16,6) | Y |  |
| 13 | IS_HOLD | 是否为保留状态 | number | Y |  |
| 14 | OWNER | 采购令拥有者 | string(120) | Y |  |
| 15 | STATE | 采购单据执行状态 | number | Y |  |
| 16 | TRANSFER_RATE | 转换率 | number(16,8) | Y |  |
| 17 | SUPPLY_RULE_ID | 供给法则 | string(120) | Y |  |
| 18 | IS_FIRM | 单据是否锁定不可移动 | number | Y |  |
| 19 | UNINSPECT_QTY | (采)待验量 | number(16,6) | Y |  |
| 20 | UNSTOCKED_QTY | (采)待入库量 | number(16,6) | Y |  |
| 21 | RETURN_QTY | (采)验退量 | number(16,6) | Y |  |
| 22 | LOCATION | 供货商位置 | string(120) | Y |  |
| 23 | CREATOR | 开立者 | string(120) | Y |  |
| 24 | INSPECTING_QTY | (采)在验量 | number(16,6) | Y |  |
| 25 | PLAN_RELEASE_DATE | 预计开立日期 | date | Y |  |
| 26 | PLAN_AVAILABLE_DATE | 预计抵达日期 | date | Y |  |
| 27 | IS_LIMITED_BY_SR | 是否不受供给法则限制 | number | Y |  |
| 28 | FIRM_SUPPLY_DATE | ERP预计到库日期 | date | Y |  |
| 29 | CUS_STRING1 |  | string(120) | Y |  |
| 30 | CUS_STRING2 |  | string(120) | Y |  |
| 31 | CUS_STRING3 |  | string(120) | Y |  |
| 32 | CUS_NUMERIC1 |  | number | Y |  |
| 33 | CUS_NUMERIC2 |  | number(16,6) | Y |  |
| 34 | CUS_NUMERIC3 |  | number(16,6) | Y |  |
| 35 | CUS_DATE1 |  | date | Y |  |
| 36 | CUS_DATE2 |  | date | Y |  |
| 37 | SOURCE_DO_ID |  | string(120) | Y |  |
| 38 | SOURCE_MO_ID |  | string(120) | Y |  |
| 39 | FEATURE_CODE | 特征码 | string(120) | Y |  |
| 40 | OWNER_ORG | 厂别 | string(120) | Y |  |
| 41 | PLAN_STRATEGY_CODE | 规划策略 | string(120) | Y |  |
| 42 | CASE_CODE | 案例代码 | string(120) | Y |  |
| 43 | PLAN_LEVEL | 规划层级 | string(120) | Y |  |
| 44 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 45 | BUSINESS_UNIT_ID | 业务单位 | string(120) | Y |  |
| 46 | PURCHASE_ORDER_KEY |  | string(120) | Y |  |
| 47 | PURCHASE_ORDER_D_KEY |  | string(120) | Y |  |
| 48 | PURCHASE_ORDER_SD_KEY |  | string(120) | Y |  |
| 49 | TRANSFER_ORDER |  | string(120) | Y |  |
| 50 | OUTSOURCE_MATERIAL | 物料外包 | number(16,6) | Y |  |
| 51 | MODI_DATE | 外包完成日 | date | Y |  |
| 52 | ORIG_PLAN_STRATEGY_CODE | 原规划策略编号 | string(120) | Y |  |
| 53 | ORIG_PLAN_LEVEL | 原规划层级 | string(120) | Y |  |
| 54 | SOURCE_ID_RTK | 来源码 | string(400) | Y |  |
| 55 | SOURCE_ID_ROid | 源单键值 | GUID | Y |  |
| 56 | CreateDate | 创建日期 | date | Y |  |
| 57 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 58 | ModifiedDate | 修改日期 | date | Y |  |
| 59 | CreateBy | 创建者 | GUID | Y |  |
| 60 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 61 | ModifiedBy | 修改者 | GUID | Y |  |
| 62 | Attachments | 附件 | string | Y |  |
| 63 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 64 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 65 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 66 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 67 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 68 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 69 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 70 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 71 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 72 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 73 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 74 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 75 | UDF041 | 自定义字段12 | date | Y |  |
| 76 | UDF042 | 自定义字段13 | date | Y |  |
| 77 | UDF051 | 自定义字段14 | GUID | Y |  |
| 78 | UDF052 | 自定义字段15 | GUID | Y |  |
| 79 | UDF053 | 自定义字段16 | GUID | Y |  |
| 80 | UDF054 | 自定义字段17 | GUID | Y |  |
| 81 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 82 | Version | 版本号，不要随意更改 | binary | Y |  |
| 83 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 84 | ApproveDate | 修改日期 | date | Y |  |
| 85 | ApproveBy | 修改人 | GUID | Y |  |

### APS_REPORT_CONFIG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_REPORT_CONFIG_ID | 主键 | GUID | Y | Y |
| 2 | REPORT_ID | 作業編號 | string(40) | Y |  |
| 3 | REPORT_SUB_ID | 次作業編號 | string(100) | Y |  |
| 4 | REPORT_GROUP | 作業群組 | string(40) | Y |  |
| 5 | REPORT_NAME | 作業名稱 | string(400) | Y |  |
| 6 | REPORT_STYLE | 作業型態 | number | Y |  |
| 7 | DESCRPTION | 作業說明 | string(100) | Y |  |
| 8 | DATA_GROUP | 資料串接群組 | string(100) | Y |  |
| 9 | METADATA | 作業設定內容 | string | Y |  |
| 10 | CREATE_USER | 建立者 | string(100) | Y |  |
| 11 | CREATE_TIME | 建立時間 | date | Y |  |
| 12 | MODIFY_USER | 維護人 | string(100) | Y |  |
| 13 | MODIFY_TIME | 維護時間 | date | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
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
| 40 | RESERVED_001 |  | string(510) | Y |  |
| 41 | RESERVED_002 |  | string(510) | Y |  |
| 42 | RESERVED_011 |  | GUID | Y |  |
| 43 | RESERVED_012 |  | GUID | Y |  |
| 44 | RESERVED_021 |  | date | Y |  |
| 45 | RESERVED_022 |  | date | Y |  |
| 46 | RESERVED_031 |  | number(16,6) | Y |  |
| 47 | RESERVED_032 |  | number(16,6) | Y |  |
| 48 | RESERVED_041 |  | number(23,8) | Y |  |
| 49 | RESERVED_042 |  | number(23,8) | Y |  |
| 50 | RESERVED_051 |  | number(23,8) | Y |  |
| 51 | RESERVED_052 |  | number(23,8) | Y |  |
| 52 | RESERVED_061 |  | number | Y |  |
| 53 | RESERVED_062 |  | number | Y |  |
| 54 | RESERVED_071 |  | number(0/1) | Y |  |
| 55 | RESERVED_072 |  | number(0/1) | Y |  |
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |

### APS_SERVER_COMMAND_QUEUE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_SERVER_COMMAND_QUEUE_ID | 主键 | GUID | Y | Y |
| 2 | COMMAND_ID | 命令 | string(120) | Y |  |
| 3 | CODE1 | 工廠編號 | string(120) | Y |  |
| 4 | CODE2 | 規劃策略編號 | string(120) | Y |  |
| 5 | CODE3 | 規劃層級 | string(120) | Y |  |
| 6 | CODE4 | 使用者編號 | string(120) | Y |  |
| 7 | CODE5 | 案例編號 | string(120) | Y |  |
| 8 | CODE6 | 語系編號 | string(120) | Y |  |
| 9 | CODE7 | 預留參數 | string(120) | Y |  |
| 10 | CODE8 | 預留參數 | string(120) | Y |  |
| 11 | CODE9 | 預留參數 | string(120) | Y |  |
| 12 | CODE10 | 命令識別編號 | string(120) | Y |  |
| 13 | STATUS | 狀態 | number | Y |  |
| 14 | MODI_TIME | 維護時間 | date | Y |  |
| 15 | CREATE_TIME | 建立時間 | date | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
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
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |

### APS_SERVER_STATUS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_SERVER_STATUS_ID | 主键 | GUID | Y | Y |
| 2 | SERIAL_ID | 流水編號 | string(120) | Y |  |
| 3 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 4 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 5 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 6 | USER_ID | 使用者代號 | string(120) | Y |  |
| 7 | MODULE_ID | 模組ID | string(120) | Y |  |
| 8 | SERVER_STATUS | 伺服器狀態 | string(120) | Y |  |
| 9 | MODI_DATE | 維護時間 | date | Y |  |
| 10 | COMMAND_SOURCE | 命令來源 | string(120) | Y |  |
| 11 | STATUS | 狀態 | number | Y |  |
| 12 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |

### APS_SERVER_STATUS_MAPPING

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_SERVER_STATUS_MAPPING_ID | 主键 | GUID | Y | Y |
| 2 | STATUS_ID | 狀態編號 | string(120) | Y |  |
| 3 | STATUS_DESCRIPT | 狀態說明 | string(120) | Y |  |
| 4 | STATUS_FOR_INQUIRE | 回應狀態 | string(120) | Y |  |
| 5 | STATUS_FOR_SCHEDULE | 排程狀態 | string(120) | Y |  |
| 6 | Version | 版本号，不要随意更改 | binary | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
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
| 32 | RESERVED_001 |  | string(510) | Y |  |
| 33 | RESERVED_002 |  | string(510) | Y |  |
| 34 | RESERVED_011 |  | GUID | Y |  |
| 35 | RESERVED_012 |  | GUID | Y |  |
| 36 | RESERVED_021 |  | date | Y |  |
| 37 | RESERVED_022 |  | date | Y |  |
| 38 | RESERVED_031 |  | number(16,6) | Y |  |
| 39 | RESERVED_032 |  | number(16,6) | Y |  |
| 40 | RESERVED_041 |  | number(23,8) | Y |  |
| 41 | RESERVED_042 |  | number(23,8) | Y |  |
| 42 | RESERVED_051 |  | number(23,8) | Y |  |
| 43 | RESERVED_052 |  | number(23,8) | Y |  |
| 44 | RESERVED_061 |  | number | Y |  |
| 45 | RESERVED_062 |  | number | Y |  |
| 46 | RESERVED_071 |  | number(0/1) | Y |  |
| 47 | RESERVED_072 |  | number(0/1) | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |

### APS_SFT_DISPATCH

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_SFT_DISPATCH_ID | 主键 | GUID | Y | Y |
| 2 | SCHEDULE_DATE | 派工日期 | date | Y |  |
| 3 | IS_OUTSOURCING | 外包 | number | Y |  |
| 4 | EQUIP_TYPE | 資源型態 | number | Y |  |
| 5 | RESOURCE_CODE | 資源編號 | string(120) | Y |  |
| 6 | SCHEDULE_SEQU | 派工順序 | number | Y |  |
| 7 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 8 | ROUTE_ID | 途程編號 | string(160) | Y |  |
| 9 | SEQU_NUM | 加工序號 | string(120) | Y |  |
| 10 | OPERATION_ID | 作業編號 | string(120) | Y |  |
| 11 | PROCESS_QTY | 派工數量 | number(16,6) | Y |  |
| 12 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 13 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 14 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 15 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 16 | RESOURCE_GROUP_CODE | 資源群組 | string(120) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |

### APS_TMP_DEMAND

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_TMP_DEMAND_ID | 主键 | GUID | Y | Y |
| 2 | CHILD_ID | 子編號 | number | Y |  |
| 3 | PARENTID | 上階ID | number | Y |  |
| 4 | BOMLEVEL | 階層碼 | number | Y |  |
| 5 | FED_ORDER_ID | 供給單號 | string(120) | Y |  |
| 6 | FEDED_ORDER_ID | 被供給單號 | string(120) | Y |  |
| 7 | SUPER_ORDER_ID | 最上階訂單號 | string(120) | Y |  |
| 8 | SUPPLY_ORDER_ID | 供給單號 | string(120) | Y |  |
| 9 | DEMAND_SOURCE_ID | 需求來源編號 | string(120) | Y |  |
| 10 | DEMAND_SOURCE_TYPE | 需求來源型態 | string(120) | Y |  |
| 11 | DEMAND_SEQUENCE | 需求序 | number | Y |  |
| 12 | ALLOCATE_SEQUENCE | 分配序 | number | Y |  |
| 13 | SUBSTITUTE_SEQUENCE | 替代序 | number | Y |  |
| 14 | SUPPLY_TYPE | 供給型態 | string(120) | Y |  |
| 15 | PART_ID | 品號 | string(210) | Y |  |
| 16 | SUB_TYPE | 取替代型態 | number | Y |  |
| 17 | DEMAND_TIME | 需求日 | date | Y |  |
| 18 | DEMAND_QTY | 需求數量 | number(16,6) | Y |  |
| 19 | FO_CONSUME_QTY | 預測耗用量 | number(16,6) | Y |  |
| 20 | PROJECT_SHORT_QTY | 預計短缺量 | number(16,6) | Y |  |
| 21 | SUPPLY_SEQUENCE | 供給序 | number | Y |  |
| 22 | SUPPLY_WH_ID | 供給庫別 | string(120) | Y |  |
| 23 | SUPPLY_SL_ID | 供給庫位 | string(120) | Y |  |
| 24 | SUPPLY_QTY | 可供給數量 | number(16,6) | Y |  |
| 25 | UNIT_QTY | 用量比例 | number(16,8) | Y |  |
| 26 | UP_SUPPLY_QTY | 保留欄位 | number(16,6) | Y |  |
| 27 | RELEASED_QTY | 已領用量 | number(16,6) | Y |  |
| 28 | ORIG_PART_ID | 原始需求品號 | string(210) | Y |  |
| 29 | SUPPLY_TIME | 供給時間 | date | Y |  |
| 30 | ORIG_SUPPLY_QTY | 原供給量 | number(16,6) | Y |  |
| 31 | UNIQ_CODE | 唯一碼 | number | Y |  |
| 32 | PARENT_UNIQ_CODE | 上階唯一碼 | number | Y |  |
| 33 | ORIG_DEMAND_QTY | 主料需求數量 | number(16,6) | Y |  |
| 34 | SOURCE_PART_ID | 上階需求料號 | string(210) | Y |  |
| 35 | V_TO_R_DEMAND_QTY | 虛擬訂單實際需求量 | number(16,6) | Y |  |
| 36 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 37 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 38 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 39 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 40 | ITEM_CODE | 品號 | string(210) | Y |  |
| 41 | FEATURE_CODE | 特徵碼 | string(120) | Y |  |
| 42 | REPLACED_ITEM_CODE | 主料品號 | string(210) | Y |  |
| 43 | REPLACED_FEATURE_CODE | 主料特徵碼 | string(120) | Y |  |
| 44 | MO_ITEM_CODE | 工單品號 | string(210) | Y |  |
| 45 | MO_FEATURE_CODE | 工單特徵碼 | string(120) | Y |  |
| 46 | USE_DIFFERENT_PRODUCT | 聯副產品 | number | Y |  |
| 47 | UNIQUE_ID | 鎖定唯一碼 | string(120) | Y |  |
| 48 | SEQUENCE_TXT | BOM序號 | string(120) | Y |  |
| 49 | DEPEND_NUM | 領料序號 | number(16,6) | Y |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | Attachments | 附件 | string | Y |  |
| 57 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 58 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 59 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 60 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 61 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 62 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 63 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 64 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 65 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 66 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 67 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 68 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 69 | UDF041 | 自定义字段12 | date | Y |  |
| 70 | UDF042 | 自定义字段13 | date | Y |  |
| 71 | UDF051 | 自定义字段14 | GUID | Y |  |
| 72 | UDF052 | 自定义字段15 | GUID | Y |  |
| 73 | UDF053 | 自定义字段16 | GUID | Y |  |
| 74 | UDF054 | 自定义字段17 | GUID | Y |  |
| 75 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 76 | Version | 版本号，不要随意更改 | binary | Y |  |
| 77 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 78 | ApproveDate | 修改日期 | date | Y |  |
| 79 | ApproveBy | 修改人 | GUID | Y |  |
| 80 | INTERNAL_ITEM |  | number(0/1) | Y |  |

### APS_TMP_DO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_TMP_DO_ID | 主键 | GUID | Y | Y |
| 2 | DEMAND_ORDER_ID | 訂單編號 | string(120) | Y |  |
| 3 | PART_ID | 品號 | string(210) | Y |  |
| 4 | ORDER_TYPE | 訂單型式 | string(120) | Y |  |
| 5 | DUE_DATE | 交期 | date | Y |  |
| 6 | PRIORITY | 優先順序 | number | Y |  |
| 7 | ORDER_QTY | 訂購數量 | number(16,6) | Y |  |
| 8 | SHIPPED_QTY | 已出貨量 | number(16,6) | Y |  |
| 9 | RELEASE_DATE | 開立日 | date | Y |  |
| 10 | COMPLETE_DATE | 預計完工日 | date | Y |  |
| 11 | IS_SCHEDULED | 納入排程 | number | Y |  |
| 12 | IS_NON_DELAYED | 嚴守交期 | number | Y |  |
| 13 | LATE_MSG | 延遲訊息 | string(400) | Y |  |
| 14 | REAL_DUE_DATE | 真實交期 | date | Y |  |
| 15 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 16 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 17 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 18 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 19 | CR_VALUE | CR值 | number(16,6) |  |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
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
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |

### APS_TMP_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_TMP_MO_ID | 主键 | GUID | Y | Y |
| 2 | MFG_ORDER_ID | 工單編號 | string(120) | Y |  |
| 3 | DEMAND_QTY | 需求數量 | string(120) | Y |  |
| 4 | ERP_ORDER_ID | EPR工單編號 | string(120) | Y |  |
| 5 | FIRM_COMPLETE_DATE | ERP預計完工日 | date | Y |  |
| 6 | FIRM_RELEASE_DATE | ERP預計開立日 | date | Y |  |
| 7 | IS_NEW | 建議單據 | number | Y |  |
| 8 | PART_ID | 品號 | string(210) | Y |  |
| 9 | PLAN_COMPLETE_DATE | 預計完工時間 | date | Y |  |
| 10 | PLAN_RELEASE_DATE | 預計發放時間 | date | Y |  |
| 11 | ROUTE_ID | 途程編號 | string(160) | Y |  |
| 12 | PRODUCED_QTY | 已生產量 | number(16,6) | Y |  |
| 13 | SCRAP_QTY | 報廢數量 | number(16,6) | Y |  |
| 14 | STATE | 狀態 | number | Y |  |
| 15 | PO_CONSTRAINT_DATE | 物料限制時間 | date | Y |  |
| 16 | HAS_ROUTE | 使用工單製程 | number | Y |  |
| 17 | IS_AUTO_OS | 自動轉外包工單 | number | Y |  |
| 18 | IS_AUTO_PUR_MODI | 自動外購取消 | number | Y |  |
| 19 | OUTSOURCE_ID | 外包商編號 | string(120) | Y |  |
| 20 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 21 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 22 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 23 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 24 | MO_REMAIN_PROCESS_TIME | 剩餘產能 | number |  |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Attachments | 附件 | string | Y |  |
| 32 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 33 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 34 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 35 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 36 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 37 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 38 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 39 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 40 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 41 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 42 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 43 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 44 | UDF041 | 自定义字段12 | date | Y |  |
| 45 | UDF042 | 自定义字段13 | date | Y |  |
| 46 | UDF051 | 自定义字段14 | GUID | Y |  |
| 47 | UDF052 | 自定义字段15 | GUID | Y |  |
| 48 | UDF053 | 自定义字段16 | GUID | Y |  |
| 49 | UDF054 | 自定义字段17 | GUID | Y |  |
| 50 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |

### APS_TMP_PO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_TMP_PO_ID | 主键 | GUID | Y | Y |
| 2 | FIRM_AVAILABLE_DATE | ERP預計到廠日 | date | Y |  |
| 3 | LOCATION | 供應商位置 | string(120) | Y |  |
| 4 | PART_ID | 品號 | string(210) | Y |  |
| 5 | PURCHASE_ORDER_ID | 採購單編號 | string(120) | Y |  |
| 6 | PURCHASE_QTY | 預計採購數量 | number(16,6) | Y |  |
| 7 | FIRM_RELEASE_DATE | ERP預計開立日 | date | Y |  |
| 8 | SUPPLIER_ID | 供應商編號 | string(120) | Y |  |
| 9 | ERP_ORDER_ID | EPR工單編號 | string(120) | Y |  |
| 10 | STOCKED_QTY | 已入庫數量 | number(16,6) | Y |  |
| 11 | STATE | 狀態 | number | Y |  |
| 12 | UNINSPECT_QTY | 待驗量 | number(16,6) | Y |  |
| 13 | UNSTOCKED_QTY | 待入庫量 | number(16,6) | Y |  |
| 14 | RETURN_QTY | 驗退量 | number(16,6) | Y |  |
| 15 | PLAN_AVAILABLE_DATE | 預計到廠日期 | date | Y |  |
| 16 | PLAN_RELEASE_DATE | 預計發放時間 | date | Y |  |
| 17 | IS_NEW | 建議單據 | number | Y |  |
| 18 | IS_AUTO_PUR | 製造轉採購單 | number | Y |  |
| 19 | AUTO_PUR_MO_ID | 自動轉外購前的工單單號 | string(120) | Y |  |
| 20 | IS_AUTO_PUR_MODI | 自動外購取消 | number | Y |  |
| 21 | FIRM_SUPPLY_DATE | ERP預計到庫日 | date | Y |  |
| 22 | PLAN_SUPPLY_DATE | 預計到庫日期 | date | Y |  |
| 23 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 24 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 25 | CASE_CODE | 案例編號 | string(120) | Y |  |
| 26 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 35 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 36 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 37 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 38 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 39 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 40 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 41 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 42 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 43 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 44 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 45 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 46 | UDF041 | 自定义字段12 | date | Y |  |
| 47 | UDF042 | 自定义字段13 | date | Y |  |
| 48 | UDF051 | 自定义字段14 | GUID | Y |  |
| 49 | UDF052 | 自定义字段15 | GUID | Y |  |
| 50 | UDF053 | 自定义字段16 | GUID | Y |  |
| 51 | UDF054 | 自定义字段17 | GUID | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |

### APS_USER_STATUS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | APS_USER_STATUS_ID | 主键 | GUID | Y | Y |
| 2 | USER_ID | 使用者代號 | string(120) | Y |  |
| 3 | LOGIN_TIME | 登入時間 | date | Y |  |
| 4 | COMPUTER_NAME | 登入主機 | string(120) | Y |  |
| 5 | OWNER_ORG | 廠別 | string(120) | Y |  |
| 6 | PLAN_STRATEGY_CODE | 規劃策略 | string(120) | Y |  |
| 7 | PLAN_LEVEL | 規劃層級 | string(120) | Y |  |
| 8 | CASE_CODE | 案例/计划批号 | string(120) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |