---
module: "MDS"
name_zh: "主数据"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 110
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# MDS (主数据)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 110

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


- **MDS_D**


---


---


> Tables: 2

### MDS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MDS_ID | 主键 | GUID | Y | Y |
| 4 | VERSION_TIMES | 版次 | string(120) | Y |  |
| 5 | FORECAST_DATE | 预测日期 | date | Y |  |
| 6 | START_DATE | 起始日期 | date | Y |  |
| 7 | END_DATE | 结束日期 | date | Y |  |
| 8 | DEMAND_TIME_FENCE | 需求栅栏 | number | Y |  |
| 9 | OFFSET_RULE | 冲销原则 | string(80) | Y |  |
| 10 | DEMAND_PRIORITY_ORDER | 项目优先序 | string(12) | Y |  |
| 11 | DEMAND_TYPE | 来源优先序 | string(40) | Y |  |
| 12 | PLAN_STRATEGY_ID | 规划策略 | GUID | Y |  |
| 13 | TIME_BUCKET_ID | 时距编号 | GUID | Y |  |
| 14 | MDS_REMARK | 主需求版次备注 | string(400) | Y |  |
| 15 | CONSIDERED_SALES_ORDER | 考虑销售订单 | number(0/1) | Y |  |
| 16 | CONSIDERED_TRANSFER_REQ | 考虑调拨申请单 | number(0/1) | Y |  |
| 17 | CONSIDERED_INNER_ORDER | 考虑内部订单 | number(0/1) | Y |  |
| 18 | CONSIDERED_FORECAST | 考虑生产预测 | number(0/1) | Y |  |
| 19 | DEMAND_START_DATE | 需求起始日期 | date | Y |  |
| 20 | DEMAND_END_DATE | 需求结束日期 | date | Y |  |
| 21 | STRATEGY_MODE | 规划模式 | string(40) | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### MDS_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MDS_D_ID | 主键 | GUID | Y | Y |
| 2 | SEQ | 序号 | string(10) | Y |  |
| 3 | PRIORITY_ORDER | 优先顺序 | string(12) | Y |  |
| 4 | DEMAND_DATE | 需求结束日期 | date | Y |  |
| 5 | DEMAND_QTY | 已交业务数量 | number(16,6) | Y |  |
| 6 | DOC_DATE | 单据日期 | date | Y |  |
| 7 | ORIGINAL_DEMAND_QTY | 业务数量 | number(16,6) | Y |  |
| 8 | OFFSET_QTY | 冲销量 | number(16,6) | Y |  |
| 9 | OFFSET_RULE | 冲销原則 | string(40) | Y |  |
| 10 | OFFSET_STATUS | 冲销状况 | string(40) | Y |  |
| 11 | APS_FLAG | 纳入APS | number(0/1) | Y |  |
| 12 | START_DATE | 起始日期 | date | Y |  |
| 13 | END_DATE | 结束日期 | date | Y |  |
| 14 | DELIVERED_QTY | 已出货量 | number(16,6) | Y |  |
| 15 | INVENTORY_QTY | 库存单位需求量 | number(16,6) | Y |  |
| 16 | ITEM_ID | 品号 | GUID | Y |  |
| 17 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 18 | UNIT_ID | 库存单位 | GUID | Y |  |
| 19 | FAMILY_ITEM_ID | 产品系列 | GUID | Y |  |
| 20 | PLAN_DELIVERY_DATE | 预交货日 | date | Y |  |
| 21 | NETTING_TYPE | 需求计算类型 | string(40) | Y |  |
| 22 | DEMAND | 需求单号 | string(510) | Y |  |
| 23 | DEMAND_START_DATE | 需求开始日期 | date | Y |  |
| 24 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
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
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 54 | SOURCE_ID_ROid |  | GUID | Y |  |
| 55 | ORI_SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | ORI_SOURCE_ID_ROid |  | GUID | Y |  |
| 57 | MDS_ID |  | GUID | Y |  |