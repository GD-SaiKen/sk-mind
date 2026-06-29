---
module: "INQUIRIES"
name_zh: "询价管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 143
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# INQUIRIES (询价管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 143

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


- **INQUIRIES_D**
- **INQUIRIES_SD**


---


---


> Tables: 3

### INQUIRIES

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | INQUIRIES_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | INQUIRIES_DATE | 询价日期 | date | Y |  |
| 9 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 10 | INQUIRIES_TYPE | 询价类型 | string(40) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | PRICE_TYPE | 价格类型 | string(40) | Y |  |
| 13 | EXPIRY_TIME | 有效期间 | string(100) | Y |  |
| 14 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 15 | CURRENCY_ID | 币种 | GUID | Y |  |
| 16 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 17 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 18 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 19 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 20 | PrintCount | 打印次数 | number | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Attachments | 附件 | string | Y |  |
| 28 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### INQUIRIES_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INQUIRIES_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | INQUIRIES_QTY |  | number(16,6) | Y |  |
| 6 | PRICE | 單價 | number(23,8) | Y |  |
| 7 | AMOUNT |  | number(23,8) | Y |  |
| 8 | COMPONENT_PRICE |  | number(0/1) | Y |  |
| 9 | APPROVE_PRICE |  | number(23,8) | Y |  |
| 10 | APPROVE_AMOUNT |  | number(23,8) | Y |  |
| 11 | ORIGINAL_PRICE | 最近核价 | number(23,8) | Y |  |
| 12 | ADJUSTMENT_RATE |  | number(6,4) | Y |  |
| 13 | NEGOTIATE_TYPE |  | string(40) | Y |  |
| 14 | EFFECTIVE_DATE |  | date | Y |  |
| 15 | INEFFECTIVE_DATE |  | date | Y |  |
| 16 | CERTIFICATION | 核定 | number(0/1) | Y |  |
| 17 | REMARK |  | string(510) | Y |  |
| 18 | TAX_RATE |  | number(5,4) | Y |  |
| 19 | ITEM_ID |  | GUID | Y |  |
| 20 | ITEM_FEATURE_ID |  | GUID | Y |  |
| 21 | INQUIRIES_UNIT_ID | 主键 | GUID | Y |  |
| 22 | TAX_ID | 税种 | GUID | Y |  |
| 23 | OPERATION_ID | 工艺 | GUID | Y |  |
| 24 | PROJECT_ID | 项目 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | INQUIRIES_ID |  | GUID | Y |  |
| 54 | REQ_SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | REQ_SOURCE_ID_ROid |  | GUID | Y |  |

### INQUIRIES_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | INQUIRIES_SD_ID | 主键 | GUID | Y | Y |
| 2 | BEGIN_QTY | 数量>= | number(16,6) | Y |  |
| 3 | END_QTY | 数量< | number(16,6) | Y |  |
| 4 | PRICE | 單價 | number(23,8) | Y |  |
| 5 | ORIGINAL_PRICE | 原单价 | number(23,8) | Y |  |
| 6 | ADJUSTMENT_RATE | 调整幅度% | number(6,4) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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
| 36 | INQUIRIES_D_ID |  | GUID | Y |  |