---
module: "BATCH"
name_zh: "批次策略"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 139
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# BATCH (批次策略)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 139

## Related Modules

- [[ABTABAC (表格映射)|ABTABAC (表格映射)]]
- [[ABTABVC (表格方案)|ABTABVC (表格方案)]]
- [[ACCCODE (科目数据集)|ACCCODE (科目数据集)]]
- [[ACCESS (权限控制)|ACCESS (权限控制)]]
- [[ACCPERIOD (会计期间)|ACCPERIOD (会计期间)]]
- [[ALTER (变更)|ALTER (变更)]]
- [[AM (资产报表)|AM (资产报表)]]
- [[AU (辅助特性)|AU (辅助特性)]]

---

## Tables


- **BATCH_PLAN_STRATEGY**
- **BATCH_PLAN_STRATEGY_D**


---


---


> Tables: 2

### BATCH_PLAN_STRATEGY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PLAN_STRATEGY_ID | 规划策略 | GUID | Y |  |
| 4 | PLAN_STRATEGY_CODE | 编号 | string(40) | Y |  |
| 5 | PLAN_STRATEGY_NAME | 名称 | string(120) | Y |  |
| 6 | STRATEGY_MODE | 规划模式 | string(40) | Y |  |
| 7 | MDS_LEVEL | 是否启动MDS | number(0/1) | Y |  |
| 8 | MPS_LEVEL | 是否启动MPS | number(0/1) | Y |  |
| 9 | MRP_LEVEL | 是否启动MRP | number(0/1) | Y |  |
| 10 | MDS_OFFSET_RULE | 冲销原则 | string(40) | Y |  |
| 11 | MDS_DEMAND_TIME_FENCE | 需求栅栏 | number | Y |  |
| 12 | MDS_DEMAND_PRIORITY_ORDER | 需求优先级 | string(12) | Y |  |
| 13 | MDS_DEMAND_TYPE | 需求形式 | string(40) | Y |  |
| 14 | MPS_FORECAST_ALLOCATION | 预测分配 | string(40) | Y |  |
| 15 | MPS_MO_ALLOCATION | 在制工单计算方式 | string(40) | Y |  |
| 16 | MPS_SCHEDULING_STRATEGY | 排程策略 | string(40) | Y |  |
| 17 | MPS_LEAD_TIME | 提前天数 | number | Y |  |
| 18 | MPS_TRANSFER_LOT_FLAG | 是否考虑移转批量 | number(0/1) | Y |  |
| 19 | MPS_ATTRITION_RATE_FLAG | 是否考虑损耗率 | number(0/1) | Y |  |
| 20 | MPS_REPLACE_FLAG | 是否考虑取代料 | number(0/1) | Y |  |
| 21 | MPS_ALTERNATIVE_FLAG | 是否考虑替代料 | number(0/1) | Y |  |
| 22 | MPS_REQUIREMENT_CALCULATION | 需求计算方式 | string(40) | Y |  |
| 23 | MRP_TIME_BUCKET | 时距设定 | string(40) | Y |  |
| 24 | MRP_TIME_BUCKET_ID | 主键 | GUID | Y |  |
| 25 | MRP_DEMAND_SOURCE | 需求来源 | string(40) | Y |  |
| 26 | MRP_FORECAST_ALLOCATION | 预测分配 | string(40) | Y |  |
| 27 | MRP_PROCUREMENT_PLAN | 采购计划范围 | string(40) | Y |  |
| 28 | MRP_TRANSFER_LOT_FLAG | 是否考虑移转批量 | number(0/1) | Y |  |
| 29 | MRP_ATTRITION_RATE_FLAG | 是否考虑损耗率 | number(0/1) | Y |  |
| 30 | MRP_REPLACE_FLAG | 是否考虑取代料 | number(0/1) | Y |  |
| 31 | MRP_ALTERNATIVE_FLAG | 是否考虑替代料 | number(0/1) | Y |  |
| 32 | MRP_PRODUCTION_PLAN_FLAG | 是否生成生产计划 | number(0/1) | Y |  |
| 33 | MRP_REQUIREMENT_CALCULATION | 需求计算方式 | string(40) | Y |  |
| 34 | REMARK | 备注 | string(440) | Y |  |
| 35 | MPS_DEMAND_SOURCE | 需求来源 | string(40) | Y |  |
| 36 | MPS_STATUS | MPS状态 | string(40) | Y |  |
| 37 | MRP_STATUS | MRP状态 | string(40) | Y |  |
| 38 | CONSIDERED_LOCK_STOCK | 考虑库存锁定 | number(0/1) | Y |  |
| 39 | MDS_SALES_ORDER_FLAG | 考虑銷售訂單 | number(0/1) | Y |  |
| 40 | MDS_FORECAST_FLAG | 考虑生產預測 | number(0/1) | Y |  |
| 41 | MDS_TRANSFER_FLAG | 考虑调拨申请单 | number(0/1) | Y |  |
| 42 | MDS_INNER_ORDER_FLAG | 考虑內部订单 | number(0/1) | Y |  |
| 43 | MPS_SAFT_STOCK_FLAG | 考虑安全库存 | number(0/1) | Y |  |
| 44 | MRP_SAFT_STOCK_FLAG | 考虑安全库存 | number(0/1) | Y |  |
| 45 | MPS_KEEP_ISSUED_PLANS | 保留已发放计划天数 | number | Y |  |
| 46 | MRP_KEEP_ISSUED_PLANS | 保留已发放计划天数 | number | Y |  |
| 47 | MPS_ISSUED_ZERO_PLANS | 发放需求为零的计划 | number(0/1) | Y |  |
| 48 | MRP_ISSUED_ZERO_PLANS | 发放需求为零的计划 | number(0/1) | Y |  |
| 49 | BATCH_PLAN_STRATEGY_ID | 主键 | GUID | Y | Y |
| 50 | MRP_SCHEDULING_STRATEGY | 排程策略 | string(40) | Y |  |
| 51 | MRP_LOCK_RANGE | MRP锁定范围 | string(40) | Y |  |
| 52 | MPS_LOCK_RANGE | MPS锁定范围 | string(40) | Y |  |
| 53 | PLAN_TYPE | 生成计划类型 | string(40) | Y |  |
| 54 | MDS_VERSION | 计划批号 | string(120) | Y |  |
| 55 | FROM_MDS_VERSION | 来源计划批号 | string(120) | Y |  |
| 56 | ROOT_MDS_VERSION | 原始计划批号 | string(120) | Y |  |
| 57 | DELETE_FLAG | 是否删除 | number(0/1) | Y |  |
| 58 | LOCK | 全锁定 | number(0/1) | Y |  |
| 59 | FROZEN | 全冻结 | number(0/1) | Y |  |
| 60 | RESERVED_PLAN_001 | 计划预留1 | string(40) | Y |  |
| 61 | RESERVED_PLAN_002 | 计划预留2 | string(40) | Y |  |
| 62 | RESERVED_PLAN_003 | 计划预留3 | string(40) | Y |  |
| 63 | RESERVED_PLAN_004 | 计划预留4 | number(0/1) | Y |  |
| 64 | RESERVED_PLAN_005 | 计划预留5 | number(0/1) | Y |  |
| 65 | RESERVED_PLAN_006 | 计划预留6 | string(510) | Y |  |
| 66 | RESERVED_PLAN_007 | 计划预留7 | string(510) | Y |  |
| 67 | CreateDate | 创建日期 | date | Y |  |
| 68 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 69 | ModifiedDate | 修改日期 | date | Y |  |
| 70 | CreateBy | 创建者 | GUID | Y |  |
| 71 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 72 | ModifiedBy | 修改者 | GUID | Y |  |
| 73 | Attachments | 附件 | string | Y |  |
| 74 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 75 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 76 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 77 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 78 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 79 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 80 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 81 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 82 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 83 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 84 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 85 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 86 | UDF041 | 自定义字段12 | date | Y |  |
| 87 | UDF042 | 自定义字段13 | date | Y |  |
| 88 | UDF051 | 自定义字段14 | GUID | Y |  |
| 89 | UDF052 | 自定义字段15 | GUID | Y |  |
| 90 | UDF053 | 自定义字段16 | GUID | Y |  |
| 91 | UDF054 | 自定义字段17 | GUID | Y |  |
| 92 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 93 | Version | 版本号，不要随意更改 | binary | Y |  |
| 94 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 95 | ApproveDate | 修改日期 | date | Y |  |
| 96 | ApproveBy | 修改人 | GUID | Y |  |
| 97 | Owner_Org_RTK |  | string(400) | Y |  |
| 98 | Owner_Org_ROid |  | GUID | Y |  |
| 99 | MRP_DEMAND_PRIORITY_ORDER | 需求优先序 | string(40) | Y |  |
| 100 | MRP_MANUFACTURING_PART | 自制件 | number(0/1) | Y |  |
| 101 | MRP_PROCESSING_PART | 委外加工件 | number(0/1) | Y |  |
| 102 | MRP_PURCHASING_PART | 采购件 | number(0/1) | Y |  |
| 103 | MRP_INNER_PURCHASING_PART | 内部采购件 | number(0/1) | Y |  |
| 104 | MRP_TRANSFER_PART | 调拨件 | number(0/1) | Y |  |
| 105 | MRP_ADDED_DIFFERENCE | 毛需求仅补充差额 | number(0/1) | Y |  |
| 106 | MRP_CRITICAL_ITEM_TYPE | 关键料类型 | string(40) | Y |  |
| 107 | RELEASE_COMPLETION | 发放完成 | number(0/1) | Y |  |
| 108 | MPS_SAFT_STOCK_PRIORITY | 安全库存需求优先级 | number | Y |  |
| 109 | MRP_SAFT_STOCK_PRIORITY | 安全库存需求优先级 | number | Y |  |
| 110 | INTERNAL_ITEM_PLAN |  | number(0/1) | Y |  |

### BATCH_PLAN_STRATEGY_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BATCH_PLAN_STRATEGY_D_ID | 主健 | GUID | Y | Y |
| 2 | RESOURCE_ID | 资源编号 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | BATCH_PLAN_STRATEGY_ID |  | GUID | Y |  |