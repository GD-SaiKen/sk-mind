---
module: "PREPAID"
name_zh: "预付账款"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 165
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# PREPAID (预付账款)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 165

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


- **PREPAID_PURCHASE (预付购料)**
- **PREPAID_PURCHASE_D (预付购料明細)**
- **PREPAID_PURCHASE_EXPENSES**


---


---


> Tables: 3

### PREPAID_PURCHASE (预付购料)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PREPAID_PURCHASE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 9 | PAID_CATEGORY | 类别 | string(40) | Y |  |
| 10 | LC_NO | L/C_NO | string(40) | Y |  |
| 11 | LC_ISSUE_BANK | 开状银行 | GUID | Y |  |
| 12 | LIMITATION_CATEGORY | 额度别 | string(8) | Y |  |
| 13 | LC_ISSUE_DATE | 开状日期 | date | Y |  |
| 14 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 15 | EFFECTIVE_DATE | 有效日期 | date | Y |  |
| 16 | FORWARD_DAYS | 远期天数 | number | Y |  |
| 17 | LICENSE_NO | 许可证号 | string(40) | Y |  |
| 18 | SHIPPING_DEADLINE | 装船期限 | date | Y |  |
| 19 | SHIPPING_TYPE | 运送方式 | string(80) | Y |  |
| 20 | ETD | 预计送货日 | date | Y |  |
| 21 | ETA | 预计到达日 | date | Y |  |
| 22 | LC_ISSUE_EXCHANGE_RATE | 开状汇率 | number(18,9) | Y |  |
| 23 | LC_ISSUE_AMT | 开状金额 | number(23,8) | Y |  |
| 24 | TT_PO_AMT_OC | 采购金额合计 | number(23,8) | Y |  |
| 25 | MODIFIED_AMT | 修改金额 | number(23,8) | Y |  |
| 26 | ARRIVAL_AMT | 已到货额 | number(23,8) | Y |  |
| 27 | SELF_FUNDING_RATE | 自筹比率 | number(5,4) | Y |  |
| 28 | SELF_FUNDING_AMT_IN_TRS_CUR | 原币自筹金额 | number(23,8) | Y |  |
| 29 | SELF_FUNDING_AMT_IN_LOC_CUR | 本币自筹金额 | number(23,8) | Y |  |
| 30 | TOTAL_EXPENSES_IN_LOC_CUR | 本币费用合计 | number(23,8) | Y |  |
| 31 | AMORTIZED_EXPENSES | 已摊费用 | number(23,8) | Y |  |
| 32 | AMORTIZED_SELF_FUNDING_AMT | 已摊自筹额 | number(23,8) | Y |  |
| 33 | REMARK | 备注 | string(510) | Y |  |
| 34 | CLOSE | 结束码 | string(40) | Y |  |
| 35 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 36 | LOAN_BATCH_NO | 借款批号 | string(20) | Y |  |
| 37 | ACCEPTANCE_DATE | 承兑日期 | date | Y |  |
| 38 | ON_BOARD_DATE | 装船日期 | date | Y |  |
| 39 | LOAN_DAYS | 放款天数 | number | Y |  |
| 40 | EXP_PAY_DATE | 预计付款日 | date | Y |  |
| 41 | EFFECTIVE_DAYS | 有效天数 | number | Y |  |
| 42 | INTEREST_RATE | 利息比率 | number(5,4) | Y |  |
| 43 | LOANS_IN_TRANS_CURR | 原币借款金额 | number(23,8) | Y |  |
| 44 | PLANT_ID | 收货工厂 | GUID | Y |  |
| 45 | MORTGAGE_AMT_IN_TRANS_CURR | 原币抵押金额 | number(23,8) | Y |  |
| 46 | REIMBURSEMENT_IN_TRANS_CURR | 原币还款金额 | number(23,8) | Y |  |
| 47 | LC_ISSUE_AMT_IN_LOCAL_CURR | 本币开状金额 | number(23,8) | Y |  |
| 48 | LOANS_IN_LOCAL_CURR | 本币借款金额 | number(23,8) | Y |  |
| 49 | MORTGAGE_AMT_IN_LOCAL_CURR | 本币抵押金额 | number(23,8) | Y |  |
| 50 | REIMBURSEMENT_IN_LOCAL_CURR | 本币还款金额 | number(23,8) | Y |  |
| 51 | LC_ISSUE_CURRENCY_ID | 开状币别 | GUID | Y |  |
| 52 | PrintCount | 打印次数 | number | Y |  |
| 53 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 54 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 55 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 56 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 57 | CreateDate | 创建日期 | date | Y |  |
| 58 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 59 | ModifiedDate | 修改日期 | date | Y |  |
| 60 | CreateBy | 创建者 | GUID | Y |  |
| 61 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 62 | ModifiedBy | 修改者 | GUID | Y |  |
| 63 | Attachments | 附件 | string | Y |  |
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 67 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 68 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 69 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 70 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 71 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 72 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 73 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 74 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 75 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 76 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 77 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 78 | UDF041 | 自定义字段12 | date | Y |  |
| 79 | UDF042 | 自定义字段13 | date | Y |  |
| 80 | UDF051 | 自定义字段14 | GUID | Y |  |
| 81 | UDF052 | 自定义字段15 | GUID | Y |  |
| 82 | UDF053 | 自定义字段16 | GUID | Y |  |
| 83 | UDF054 | 自定义字段17 | GUID | Y |  |
| 84 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 85 | ApproveDate | 修改日期 | date | Y |  |
| 86 | ApproveBy | 修改人 | GUID | Y |  |
| 87 | Owner_Org_RTK |  | string(400) | Y |  |
| 88 | Owner_Org_ROid |  | GUID | Y |  |

### PREPAID_PURCHASE_D (预付购料明細)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ORDER_SD_ID | 采购订单次序号 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 5 | BIN_ID | 库位 | GUID | Y |  |
| 6 | PREPAID_PURCHASE_D_ID | 主键 | GUID | Y | Y |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | PREPAID_PURCHASE_ID |  | GUID | Y |  |

### PREPAID_PURCHASE_EXPENSES

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PREPAID_PURCHASE_EXPENSES_ID | 主键 | GUID | Y | Y |
| 3 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 4 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 5 | EXPENSE_AMOUNT | 费用金额 | number(23,8) | Y |  |
| 6 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 7 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 8 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 9 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 10 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 11 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 12 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 15 | SUPPLIER_ID | 主键 | GUID | Y |  |
| 16 | TAX_ID | 税种 | GUID | Y |  |
| 17 | CURRENCY_ID | 币种 | GUID | Y |  |
| 18 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 19 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 45 | PREPAID_PURCHASE_ID |  | GUID | Y |  |