---
module: "PP"
name_zh: "排程变更"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 161
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# PP (排程变更)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 161

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


- **PP_CHANGE (预付购料变更单)**
- **PP_CHANGE_D (预付购料变更明細)**
- **PP_CHANGE_EXPENSES (预付购料费用变更)**


---


---


> Tables: 3

### PP_CHANGE (预付购料变更单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PP_CHANGE_ID | 主键 | GUID | Y | Y |
| 4 | CHANGE_DATE | 变更日期 | date | Y |  |
| 5 | PREPAID_PURCHASE_ID | 预付购料单号 | GUID | Y |  |
| 6 | CHANGE_VERSION | 变更版本 | string(8) | Y |  |
| 7 | DOC_DATE | 单据日期 | date | Y |  |
| 8 | REMARK_CHANGE | 变更原因 | string(510) | Y |  |
| 9 | PAID_CATEGORY | 类别 | string(40) | Y |  |
| 10 | LC_NO | LC_NO | string(40) | Y |  |
| 11 | LC_ISSUE_EXCHANGE_RATE | 开状汇率 | number(18,9) | Y |  |
| 12 | MOD_LC_ISSUE_AMT | 修改金额 | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | SELF_FUNDING_RATE | 自筹比率 | number(5,4) | Y |  |
| 15 | SELF_FUNDING_AMT_IN_TRS_CUR | 原币修改自筹金额 | number(23,8) | Y |  |
| 16 | SELF_FUNDING_AMT_IN_LOC_CUR | 本币修改自筹金额 | number(23,8) | Y |  |
| 17 | TOTAL_EXPENSES_IN_LOC_CUR | 本币费用合计 | number(23,8) | Y |  |
| 18 | ORI_LC_ISSUE_EXCHANGE_RATE | 原开状汇率 | number(18,9) | Y |  |
| 19 | LC_ISSUE_AMT | 原开状金额 | number(23,8) | Y |  |
| 20 | ORI_REMARK | 原备注意见 | string(510) | Y |  |
| 21 | ORI_SELF_FUNDING_RATE | 原自筹比率 | number(5,4) | Y |  |
| 22 | OR_SELF_FUNDING_AMT_IN_TRS_CUR | 原原币自筹金额 | number(23,8) | Y |  |
| 23 | OR_SELF_FUNDING_AMT_IN_LOC_CUR | 原本币自筹金额 | number(23,8) | Y |  |
| 24 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 25 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 26 | LC_ISSUE_CURRENCY_ID | 开状币别 | GUID | Y |  |
| 27 | ORI_PLANT_ID | 原收货工厂 | GUID | Y |  |
| 28 | ORI_TOTAL_EXPENSES_IN_LOC_CUR | 原本币费用合计 | number(23,8) | Y |  |
| 29 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 30 | PrintCount | 打印次数 | number | Y |  |
| 31 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 32 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 33 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 34 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | Owner_Org_RTK |  | string(400) | Y |  |
| 66 | Owner_Org_ROid |  | GUID | Y |  |

### PP_CHANGE_D (预付购料变更明細)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BIN_ID | 库位 | GUID | Y |  |
| 3 | WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 4 | REMARK_CHANGE | 变更原因 | string(510) | Y |  |
| 5 | ORI_WAREHOUSE_ID | 原入库仓库 | GUID | Y |  |
| 6 | ORI_BIN_ID | 原库位 | GUID | Y |  |
| 7 | PP_CHANGE_D_ID | 主键 | GUID | Y | Y |
| 8 | PURCHASE_ORDER_SD_ID | 采购订单单号 | GUID | Y |  |
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
| 34 | PP_CHANGE_ID |  | GUID | Y |  |

### PP_CHANGE_EXPENSES (预付购料费用变更)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 3 | TAX_ID | 税种 | GUID | Y |  |
| 4 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 5 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 6 | EXPENSE_AMOUNT | 费用金额 | number(23,8) | Y |  |
| 7 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 8 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 9 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 10 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 11 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 12 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 13 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 14 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | ORI_EXPENSE_ID | 原费用项目 | GUID | Y |  |
| 17 | ORI_SUPPLIER_ID | 原供应商 | GUID | Y |  |
| 18 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 19 | ORI_TAX_RATE | 原增值稅率 | number(5,4) | Y |  |
| 20 | ORI_CURRENCY_ID | 原币种 | GUID | Y |  |
| 21 | ORI_EXCHANGE_RATE | 原汇率 | number(18,9) | Y |  |
| 22 | ORI_EXPENSE_AMOUNT | 原费用金额 | number(23,8) | Y |  |
| 23 | ORI_AMOUNT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 24 | ORI_TAX_OC | 原币税额 | number(23,8) | Y |  |
| 25 | ORI_AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 26 | ORI_TAX_BC | 本币税额 | number(23,8) | Y |  |
| 27 | ORI_PAYMENT_TERM_ID | 原付款条件 | GUID | Y |  |
| 28 | ORI_TAX_INVOICE_CATEGORY_ID | 原发票种类 | GUID | Y |  |
| 29 | ORI_TAX_INVOICE_NO | 原税务发票号码 | string(510) | Y |  |
| 30 | ORI_DEDUCTIBLE_INDICATOR | 原可抵扣VAT标识 | number(0/1) | Y |  |
| 31 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 32 | SOURCE_ID | 原序号 | GUID | Y |  |
| 33 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 34 | CURRENCY_ID | 币种 | GUID | Y |  |
| 35 | PP_CHANGE_EXPENSES_ID |  | GUID | Y | Y |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 61 | PP_CHANGE_ID |  | GUID | Y |  |