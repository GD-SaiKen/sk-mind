---
module: "NEGOTIATE"
name_zh: "议价管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 170
category: purchase
tags: ["ERP", "E10", "purchase"]
created: 2026-06-25 10:52
---

# NEGOTIATE (议价管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 170

## Related Modules

- [[IMPORT (进口管理)|IMPORT (进口管理)]]
- [[PO (采购订单)|PO (采购订单)]]
- [[PURCHASE (采购管理)|PURCHASE (采购管理)]]
- [[REQUISITION (请购管理)|REQUISITION (请购管理)]]
- [[SUPPLIER (供应商)|SUPPLIER (供应商)]]
- [[SUPPLY (供应中心)|SUPPLY (供应中心)]]

---

## Tables


- **NEGOTIATE_D**
- **NEGOTIATE_ITEM**
- **NEGOTIATE_SD**


---


---


> Tables: 4

### NEGOTIATE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | NEGOTIATE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | NEGOTIATE_DATE | 审核日期 | date | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
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
| 28 | PrintCount | 打印次数 | number | Y |  |
| 29 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 30 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 31 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 32 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |

### NEGOTIATE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | NEGOTIATE_D_ID | 主键 | GUID | Y | Y |
| 2 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 3 | TAX_RATE |  | number(5,4) | Y |  |
| 4 | NEGOTIATE_QTY | 议价数量 | number(16,6) | Y |  |
| 5 | PRICE | 單價 | number(23,8) | Y |  |
| 6 | AMOUNT |  | number(23,8) | Y |  |
| 7 | COMPONENT_PRICE | 分量计价 | number(0/1) | Y |  |
| 8 | APPROVE_PRICE | 核定单价 | number(23,8) | Y |  |
| 9 | APPROVE_AMOUNT | 核定金额 | number(23,8) | Y |  |
| 10 | ORIGINAL_PRICE | 最近核价 | number(23,8) | Y |  |
| 11 | ADJUSTMENT_RATE | 调整幅度% | number(6,4) | Y |  |
| 12 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 13 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 14 | CERTIFICATION | 核定 | number(0/1) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | INQUIRIES_DATE | 询价日期 | date | Y |  |
| 17 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 18 | CURRENCY_ID | 币种 | GUID | Y |  |
| 19 | TAX_ID | 税种 | GUID | Y |  |
| 20 | NEGOTIATE_UNIT_ID | 议价单位 | GUID | Y |  |
| 21 | SOURCE_ID | 来源ID | GUID | Y |  |
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
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | NEGOTIATE_ITEM_ID |  | GUID | Y |  |

### NEGOTIATE_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | NEGOTIATE_ITEM_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 3 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 4 | PRICE_TYPE | 价格类型 | string(40) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | OPERATION_ID | 工艺 | GUID | Y |  |
| 8 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | NEGOTIATE_ID |  | GUID | Y |  |

### NEGOTIATE_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | NEGOTIATE_SD_ID | 主键 | GUID | Y | Y |
| 2 | BEGIN_QTY | 数量>= | number(16,6) | Y |  |
| 3 | END_QTY | 数量< | number(16,6) | Y |  |
| 4 | PRICE | 單價 | number(23,8) | Y |  |
| 5 | ORIGINAL_PRICE | 原单价 | number(23,8) | Y |  |
| 6 | ADJUSTMENT_RATE | 调整幅度% | number(6,4) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | SOURCE_ID | 来源ID | GUID | Y |  |
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
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | NEGOTIATE_D_ID |  | GUID | Y |  |