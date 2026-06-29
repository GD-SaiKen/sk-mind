---
module: "SIMULATE"
name_zh: "成本模拟"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 299
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# SIMULATE (成本模拟)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 299

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]

---

## Tables


- **SIMULATE_COST_RESOURCE (品号模拟成本来源)**
- **SIMULATE_COST_RESULT (品号模拟成本结果)**
- **SIMULATE_COST_TEMPLATE (模拟成本模板)**
- **SIMULATE_TEMPLATE (模拟输入导入模板)**
- **SIMULATE_TEMPLATE_D (模拟输入导入模板单身)**
- **SIMULATE_TEMPLATE_SD (模拟输入导入模板子单身)**


---


---


> Tables: 6

### SIMULATE_COST_RESOURCE (品号模拟成本来源)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SIMULATE_COST_RESOURCE_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_FEATURE_ID |  | GUID | Y |  |
| 5 | ITEM_ID | 主键 | GUID | Y |  |
| 6 | CE1_CUR_LEVEL |  | number(23,8) | Y |  |
| 7 | CE2_CUR_LEVEL |  | number(23,8) | Y |  |
| 8 | CE3_CUR_LEVEL |  | number(23,8) | Y |  |
| 9 | CE4_CUR_LEVEL |  | number(23,8) | Y |  |
| 10 | CE5_CUR_LEVEL |  | number(23,8) | Y |  |
| 11 | CE6_CUR_LEVEL |  | number(23,8) | Y |  |
| 12 | CE7_CUR_LEVEL |  | number(23,8) | Y |  |
| 13 | CE8_CUR_LEVEL |  | number(23,8) | Y |  |
| 14 | CE9_CUR_LEVEL |  | number(23,8) | Y |  |
| 15 | CE10_CUR_LEVEL |  | number(23,8) | Y |  |
| 16 | CE11_CUR_LEVEL |  | number(23,8) | Y |  |
| 17 | CE12_CUR_LEVEL |  | number(23,8) | Y |  |
| 18 | CE13_CUR_LEVEL |  | number(23,8) | Y |  |
| 19 | CE14_CUR_LEVEL |  | number(23,8) | Y |  |
| 20 | CE15_CUR_LEVEL |  | number(23,8) | Y |  |
| 21 | CE16_CUR_LEVEL |  | number(23,8) | Y |  |
| 22 | CE17_CUR_LEVEL |  | number(23,8) | Y |  |
| 23 | CE18_CUR_LEVEL |  | number(23,8) | Y |  |
| 24 | CE19_CUR_LEVEL |  | number(23,8) | Y |  |
| 25 | CE20_CUR_LEVEL |  | number(23,8) | Y |  |
| 26 | REMARK |  | string(510) | Y |  |
| 27 | COMPANY_ID | 主键 | GUID | Y |  |
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
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |

### SIMULATE_COST_RESULT (品号模拟成本结果)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SIMULATE_COST_RESULT_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 主键 | GUID | Y |  |
| 5 | PARENT_ITEM_ID | BOM主件品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | VERSION_TIMES | 版次 | string(40) | Y |  |
| 8 | VERSION_DESCRIPTION | 版本描述 | string(510) | Y |  |
| 9 | SIMULATE_DATE | 模拟日期 | date | Y |  |
| 10 | BOM_STRUCTURE_CODE | Bom结构内码 | string(8000) | Y |  |
| 11 | BOM_VERSION_TIMES | Bom版次 | string(8) | Y |  |
| 12 | INCLUDING_LOSS_RATE | 计算损耗率 | number(0/1) | Y |  |
| 13 | SALES_ORDER_DOC_D_ID | 主键 | GUID | Y |  |
| 14 | CE1_CUR_LEVEL | CE1本阶模拟成本 | number(23,8) | Y |  |
| 15 | CE2_CUR_LEVEL | CE2本阶模拟成本 | number(23,8) | Y |  |
| 16 | CE3_CUR_LEVEL | CE3本阶模拟成本 | number(23,8) | Y |  |
| 17 | CE4_CUR_LEVEL | CE4本阶模拟成本 | number(23,8) | Y |  |
| 18 | CE5_CUR_LEVEL | CE5本阶模拟成本 | number(23,8) | Y |  |
| 19 | CE6_CUR_LEVEL | CE6本阶模拟成本 | number(23,8) | Y |  |
| 20 | CE7_CUR_LEVEL | CE7本阶模拟成本 | number(23,8) | Y |  |
| 21 | CE8_CUR_LEVEL | CE8本阶模拟成本 | number(23,8) | Y |  |
| 22 | CE9_CUR_LEVEL | CE9本阶模拟成本 | number(23,8) | Y |  |
| 23 | CE10_CUR_LEVEL | CE10本阶模拟成本 | number(23,8) | Y |  |
| 24 | CE11_CUR_LEVEL | CE11本阶模拟成本 | number(23,8) | Y |  |
| 25 | CE12_CUR_LEVEL | CE12本阶模拟成本 | number(23,8) | Y |  |
| 26 | CE13_CUR_LEVEL | CE13本阶模拟成本 | number(23,8) | Y |  |
| 27 | CE14_CUR_LEVEL | CE14本阶模拟成本 | number(23,8) | Y |  |
| 28 | CE15_CUR_LEVEL | CE15本阶模拟成本 | number(23,8) | Y |  |
| 29 | CE16_CUR_LEVEL | CE16本阶模拟成本 | number(23,8) | Y |  |
| 30 | CE17_CUR_LEVEL | CE17本阶模拟成本 | number(23,8) | Y |  |
| 31 | CE18_CUR_LEVEL | CE18本阶模拟成本 | number(23,8) | Y |  |
| 32 | CE19_CUR_LEVEL | CE19本阶模拟成本 | number(23,8) | Y |  |
| 33 | CE20_CUR_LEVEL | CE20本阶模拟成本 | number(23,8) | Y |  |
| 34 | CE1_LOW_LEVEL | CE1下阶模拟成本 | number(23,8) | Y |  |
| 35 | CE2_LOW_LEVEL | CE2下阶模拟成本 | number(23,8) | Y |  |
| 36 | CE3_LOW_LEVEL | CE3下阶模拟成本 | number(23,8) | Y |  |
| 37 | CE4_LOW_LEVEL | CE4下阶模拟成本 | number(23,8) | Y |  |
| 38 | CE5_LOW_LEVEL | CE5下阶模拟成本 | number(23,8) | Y |  |
| 39 | CE6_LOW_LEVEL | CE6下阶模拟成本 | number(23,8) | Y |  |
| 40 | CE7_LOW_LEVEL | CE7下阶模拟成本 | number(23,8) | Y |  |
| 41 | CE8_LOW_LEVEL | CE8下阶模拟成本 | number(23,8) | Y |  |
| 42 | CE9_LOW_LEVEL | CE9下阶模拟成本 | number(23,8) | Y |  |
| 43 | CE10_LOW_LEVEL | CE10下阶模拟成本 | number(23,8) | Y |  |
| 44 | CE11_LOW_LEVEL | CE11下阶模拟成本 | number(23,8) | Y |  |
| 45 | CE12_LOW_LEVEL | CE12下阶模拟成本 | number(23,8) | Y |  |
| 46 | CE13_LOW_LEVEL | CE13下阶模拟成本 | number(23,8) | Y |  |
| 47 | CE14_LOW_LEVEL | CE14下阶模拟成本 | number(23,8) | Y |  |
| 48 | CE15_LOW_LEVEL | CE15下阶模拟成本 | number(23,8) | Y |  |
| 49 | CE16_LOW_LEVEL | CE16下阶模拟成本 | number(23,8) | Y |  |
| 50 | CE17_LOW_LEVEL | CE17下阶模拟成本 | number(23,8) | Y |  |
| 51 | CE18_LOW_LEVEL | CE18下阶模拟成本 | number(23,8) | Y |  |
| 52 | CE19_LOW_LEVEL | CE19下阶模拟成本 | number(23,8) | Y |  |
| 53 | CE20_LOW_LEVEL | CE20下阶模拟成本 | number(23,8) | Y |  |
| 54 | REMARK | 备注 | string(510) | Y |  |
| 55 | COMPANY_ID | 主键 | GUID | Y |  |
| 56 | MATERIAL_COST_PRICE_BY | 材料成本取价方式 | string(40) | Y |  |
| 57 | PARENT_ITEM_FEATURE_ID |  | GUID | Y |  |
| 58 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 59 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
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
| 90 | Owner_Org_RTK |  | string(400) | Y |  |
| 91 | Owner_Org_ROid |  | GUID | Y |  |
| 92 | CEOTHER_CUR_LEVEL | 其它本阶模拟成本 | number(23,8) | Y |  |
| 93 | CEOTHER_LOW_LEVEL | 其它下阶模拟成本 | number(23,8) | Y |  |

### SIMULATE_COST_TEMPLATE (模拟成本模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | SIMULATE_COST_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 5 | REMARK |  | string(510) | Y |  |
| 6 | COST_ELEMENT_ID | 主键 | GUID | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### SIMULATE_TEMPLATE (模拟输入导入模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SIMULATE_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 2 | IMPORT_NO | 模板编号 | string(80) | Y |  |
| 3 | PROGRAM_NO | 作业编号 | string(120) | Y |  |
| 4 | TYPEKEY | 作业TypeKey | string(120) | Y |  |
| 5 | DISPLAYNAME | 名称 | string(400) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | SHEET_TYPE | 模板类型 | number | Y |  |
| 8 | Attachments | 附件 | string | Y |  |
| 9 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |

### SIMULATE_TEMPLATE_D (模拟输入导入模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SIMULATE_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 2 | SHEET_NAME | 工作表名称 | string(400) | Y |  |
| 3 | INPUT_SEQUENCE | 输入顺序 | number | Y |  |
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
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | SIMULATE_TEMPLATE_ID |  | GUID | Y |  |

### SIMULATE_TEMPLATE_SD (模拟输入导入模板子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SIMULATE_TEMPLATE_SD_ID |  | GUID | Y | Y |
| 2 | PATH | 当前控件对应的路径 | string(400) | Y |  |
| 3 | CONTROL_NAME | 控件名称 | string(120) | Y |  |
| 4 | DISPLAYNAME | 模板显示名称 | string(120) | Y |  |
| 5 | INPUT_SEQUENCE | 输入顺序 | number | Y |  |
| 6 | INPUT_PROPERTY | 导入时设置控件属性 | string(120) | Y |  |
| 7 | OUTPUT_PROPERTY | 导出时获取控件属性 | string(120) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | FIELD_LENGTH | 字段长度 | number | Y |  |
| 10 | FIELD_ACCURACY | 字段精度 | number | Y |  |
| 11 | PICKLIST_TYPENAME | PICKLIST名称 | string(400) | Y |  |
| 12 | REQUIRE_INPUT | 不可空白 | number(0/1) | Y |  |
| 13 | IGNORE_INPUT | 导入时忽略 | number(0/1) | Y |  |
| 14 | IGNORE_MODI | 修改时忽略 | number(0/1) | Y |  |
| 15 | IS_DETAILWINDOW | 是否为子单身窗口 | number(0/1) | Y |  |
| 16 | FIELD_NAME | 字段名称 | string(120) | Y |  |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | SIMULATE_TEMPLATE_D_ID |  | GUID | Y |  |