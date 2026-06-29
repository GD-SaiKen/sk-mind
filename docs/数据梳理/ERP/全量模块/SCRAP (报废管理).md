---
module: "SCRAP"
name_zh: "报废管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 123
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# SCRAP (报废管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 123

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


- **SCRAP_DOC (报废单)**
- **SCRAP_DOC_D (报废单单身)**


---


---


> Tables: 2

### SCRAP_DOC (报废单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SCRAP_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 报废日期 | date | Y |  |
| 8 | SCRAP_REASON | 报废原因 | string(510) | Y |  |
| 9 | PIECES |  | number | Y |  |
| 10 | ORIGIN | 报废来源 | string(40) | Y |  |
| 11 | GENERATE_MODE | 生成方式 | string(40) | Y |  |
| 12 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | FROM_WAREHOUSE_ID | 限用转出仓库 | GUID | Y |  |
| 15 | TO_WAREHOUSE_ID | 限用转入仓库 | GUID | Y |  |
| 16 | COMPANY_ID |  | GUID | Y |  |
| 17 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 18 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 19 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 20 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 21 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 22 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 23 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Attachments | 附件 | string | Y |  |
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | PrintCount | 打印次数 | number | Y |  |
| 55 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 56 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 57 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 58 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |

### SCRAP_DOC_D (报废单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SCRAP_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 12 | PIECES |  | number | Y |  |
| 13 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 16 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 17 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 18 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 19 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 20 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 21 | ITEM_ID | 品号 | GUID | Y |  |
| 22 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 23 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 24 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 25 | ITEM_LOT_ID |  | GUID | Y |  |
| 26 | FROM_BIN_ID |  | GUID | Y |  |
| 27 | TO_BIN_ID |  | GUID | Y |  |
| 28 | PROJECT_ID | 项目 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 58 | SOURCE_ID_ROid |  | GUID | Y |  |
| 59 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 60 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 61 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 62 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 63 | SCRAP_DOC_ID |  | GUID | Y |  |