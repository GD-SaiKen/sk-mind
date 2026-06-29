---
module: "PRODUCT"
name_zh: "产品管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 192
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# PRODUCT (产品管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 192

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


- **PRODUCT_PLAN_FACT_TABLE (生产进度分析表)**
- **PRODUCT_SUB_GROUP**
- **PRODUCT_SUB_GROUP_D**
- **PRODUCT_YIELD_FACT_TABLE (产品良率分析表)**


---


---


> Tables: 4

### PRODUCT_PLAN_FACT_TABLE (生产进度分析表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MO_ID | 工单单号 | GUID | Y |  |
| 4 | ITEM_ID | 主件品号 | GUID | Y |  |
| 5 | ITEM_CODE | 主件品号 | string(80) | Y |  |
| 6 | ITEM_NAME | 主件品名 | string(120) | Y |  |
| 7 | ITEM_SPEC | 主件规格 | string(510) | Y |  |
| 8 | ITEM_FEATURE_CODE | 主件特征码 | string(120) | Y |  |
| 9 | ITEM_FEATURE_SPEC | 主件特征码规格 | string(510) | Y |  |
| 10 | ADMIN_UNIT_CODE | 部门编码 | string(20) | Y |  |
| 11 | ADMIN_UNIT_NAME | 部门名称 | string(40) | Y |  |
| 12 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 13 | WORK_CENTER_CODE | 工作中心编码 | string(20) | Y |  |
| 14 | WORK_CENTER_NAME | 工作中心名称 | string(40) | Y |  |
| 15 | STATUS | 状态码 | string(40) | Y |  |
| 16 | ATP_QTY | 达交数量 | number(16,6) | Y |  |
| 17 | PLAN_QTY | 预计产量 | number(16,6) | Y |  |
| 18 | PLAN_START_DATE | 预计开工日期 | date | Y |  |
| 19 | PLAN_COMPLETE_DATE | 预计完工日期 | date | Y |  |
| 20 | START_ON_TIME | 准时开工 | number(0/1) | Y |  |
| 21 | FINISH_ON_TIME | 准时完工 | number(0/1) | Y |  |
| 22 | UNIT_ID | 单位 | GUID | Y |  |
| 23 | UNIT_CODE | 单位编码 | string(8) | Y |  |
| 24 | UNIT_NAME | 单位名称 | string(20) | Y |  |
| 25 | PRODUCT_PLAN_FACT_TABLE_ID | 主键 | GUID | Y | Y |
| 26 | ITEM_FEATURE_ID | 主件特征码 | GUID | Y |  |
| 27 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
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
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |

### PRODUCT_SUB_GROUP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PRODUCT_SUB_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |
| 5 | GROUP_ITEM_NAME | 群组品名 | string(120) | Y |  |
| 6 | GROUP_ITEM_SPECIFICATION | 群组规格 | string(510) | Y |  |
| 7 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 8 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 9 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### PRODUCT_SUB_GROUP_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PRODUCT_SUB_GROUP_D_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 4 | UNIT_ID | 单位 | GUID | Y |  |
| 5 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 6 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 7 | PRIORITY | 优先序 | string(400) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | PRODUCT_SUB_GROUP_ID |  | GUID | Y |  |

### PRODUCT_YIELD_FACT_TABLE (产品良率分析表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DATE | 日期 | date | Y |  |
| 4 | ITEM_CODE | 品号 | string(80) | Y |  |
| 5 | ITEM_NAME | 品名 | string(120) | Y |  |
| 6 | ITEM_SPEC | 规格 | string(510) | Y |  |
| 7 | ITEM_FEATURE_CODE | 特征码 | string(120) | Y |  |
| 8 | ITEM_FEATURE_SPEC | 特征码规格 | string(510) | Y |  |
| 9 | ADMIN_UNIT_CODE | 部门编码 | string(20) | Y |  |
| 10 | ADMIN_UNIT_NAME | 部门名称 | string(40) | Y |  |
| 11 | WORK_CENTER_CODE | 工作中心编码 | string(20) | Y |  |
| 12 | WORK_CENTER_NAME | 工作中心名称 | string(40) | Y |  |
| 13 | CATEGORY | 单据性质 | string(40) | Y |  |
| 14 | QTY | 合格数量 | number(16,6) | Y |  |
| 15 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 16 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 17 | REWORK | 重工数量 | number(16,6) | Y |  |
| 18 | UNIT_CODE | 单位编码 | string(8) | Y |  |
| 19 | UNIT_NAME | 单位名称 | string(20) | Y |  |
| 20 | ITEM_ID | 品号 | GUID | Y |  |
| 21 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 22 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 23 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 24 | UNIT_ID | 单位 | GUID | Y |  |
| 25 | PRODUCT_YIELD_FACT_TABLE_ID | 主键 | GUID | Y | Y |
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
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |