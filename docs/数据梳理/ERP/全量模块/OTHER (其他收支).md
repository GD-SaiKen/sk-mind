---
module: "OTHER"
name_zh: "其他收支"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 413
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# OTHER (其他收支)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 8 | Columns: 413

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


- **OTHER_ARAP_ITEM (维护其他收付项目)**
- **OTHER_BO (维护其他交易对象)**
- **OTHER_CHARGEIN**
- **OTHER_CHARGEOUT**
- **OTHER_PAYABLE_DOC (其他应付单)**
- **OTHER_PAYABLE_DOC_D (其他应付单单身)**
- **OTHER_RECEIVABLE_DOC (其他应收单)**
- **OTHER_RECEIVABLE_DOC_D (其他应收单单身)**


---


---


> Tables: 8

### OTHER_ARAP_ITEM (维护其他收付项目)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | OTHER_ARAP_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | OTHER_ARAP_ITEM_CODE | 其他收付项目编号 | string(12) | Y |  |
| 5 | OTHER_ARAP_ITEM_NAME | 其他收付项目名称 | string(60) | Y |  |
| 6 | OTHER_ARAP_ITEM_TYPE | 其他收付项目类型 | number | Y |  |
| 7 | REMARK |  | string(510) | Y |  |
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
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### OTHER_BO (维护其他交易对象)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | OTHER_BO_ID | 主键 | GUID | Y | Y |
| 4 | OTHER_BO_CODE | 其他交易对象编号 | string(20) | Y |  |
| 5 | OTHER_BO_NAME | 其他交易对象名称 | string(144) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### OTHER_CHARGEIN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | OTHER_CHARGEIN_ID | 主键 | GUID | Y | Y |
| 4 | OTHER_CHARGEIN_CODE | 杂收项目编号 | string(40) | Y |  |
| 5 | OTHER_CHARGEIN_NAME | 杂收项目名称 | string(200) | Y |  |
| 6 | ACCOUNT_CODE_ID | 财务科目 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### OTHER_CHARGEOUT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | OTHER_CHARGEOUT_ID | 主键 | GUID | Y | Y |
| 4 | OTHER_CHARGEOUT_CODE | 杂支项目信息 | string(40) | Y |  |
| 5 | OTHER_CHARGEOUT_NAME | 杂收项目名称 | string(200) | Y |  |
| 6 | ACCOUNT_CODE_ID | 财务科目 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### OTHER_PAYABLE_DOC (其他应付单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | OTHER_PAYABLE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 12 | REVERSE_INDICATOR | 冲红标识 | number(0/1) | Y |  |
| 13 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 14 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 15 | PAYMENT_DATE | 付款日 | date | Y |  |
| 16 | CASHING_DATE | 兑现日 | date | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 19 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 20 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 21 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 22 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 23 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 24 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 25 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 26 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 27 | AMT_TC | 金额合计(原币) | number(23,8) | Y |  |
| 28 | AMT_FC | 金额合计(本币) | number(23,8) | Y |  |
| 29 | TRANS_TYPE | 业务类型 | number | Y |  |
| 30 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 31 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 32 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 33 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 34 | CURRENCY_ID | 货币 | GUID | Y |  |
| 35 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 36 | PAYMENT_DOC_ID | 现结收款单号 | GUID | Y |  |
| 37 | PAYABLE_AMT_TC | 应付金额合计(原币) | number(23,8) | Y |  |
| 38 | PAYABLE_AMT_FC | 应付金额合计(本币) | number(23,8) | Y |  |
| 39 | ADDITIONAL_EXPENSE_AMT_TC | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 40 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 41 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 42 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 43 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 44 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 45 | PROJECT_ID | 项目 | GUID | Y |  |
| 46 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 47 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 48 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 49 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | Attachments | 附件 | string | Y |  |
| 57 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 60 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 61 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 62 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 63 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 64 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 65 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 66 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 67 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 68 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 69 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 70 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 71 | UDF041 | 自定义字段12 | date | Y |  |
| 72 | UDF042 | 自定义字段13 | date | Y |  |
| 73 | UDF051 | 自定义字段14 | GUID | Y |  |
| 74 | UDF052 | 自定义字段15 | GUID | Y |  |
| 75 | UDF053 | 自定义字段16 | GUID | Y |  |
| 76 | UDF054 | 自定义字段17 | GUID | Y |  |
| 77 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 78 | ApproveDate | 修改日期 | date | Y |  |
| 79 | ApproveBy | 修改人 | GUID | Y |  |
| 80 | PrintCount | 打印次数 | number | Y |  |
| 81 | Owner_Org_RTK |  | string(400) | Y |  |
| 82 | Owner_Org_ROid |  | GUID | Y |  |
| 83 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 84 | SOURCE_ID_ROid |  | GUID | Y |  |
| 85 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 86 | SOURCE2_ID_ROid |  | GUID | Y |  |

### OTHER_PAYABLE_DOC_D (其他应付单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OTHER_PAYABLE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO |  | string(60) | Y |  |
| 5 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 6 | DUE_DATE | 到期日 | date | Y |  |
| 7 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 8 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | OTHER_ARAP_ITEM_ID | 其他应付项目 | GUID | Y |  |
| 11 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 12 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 13 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 14 | PROJECT_ID | 项目 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | OTHER_PAYABLE_DOC_ID |  | GUID | Y |  |

### OTHER_RECEIVABLE_DOC (其他应收单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | OTHER_RECEIVABLE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间号 | string(20) | Y |  |
| 11 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 12 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 13 | TRANS_TYPE | 业务类型 | number | Y |  |
| 14 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 15 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 16 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 17 | PAYMENT_DATE | 付款日 | date | Y |  |
| 18 | CASHING_DATE | 兑现日 | date | Y |  |
| 19 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 20 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 21 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 22 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 23 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 24 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 25 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 26 | AMT_TC | 金额合计(原币) | number(23,8) | Y |  |
| 27 | AMT_FC | 金额合计(功能币) | number(23,8) | Y |  |
| 28 | REMARK | 备注 | string(510) | Y |  |
| 29 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 30 | COLLECTION_DOC_ID | 现结收款单号 | GUID | Y |  |
| 31 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 32 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 33 | CURRENCY_ID | 货币 | GUID | Y |  |
| 34 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 35 | SETTLEMENT_METHOD | 结算方式 | GUID | Y |  |
| 36 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 37 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 38 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 39 | ADDITIONAL_EXPENSE_A | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 40 | RECEIVABLE_AMT_FC | 应收金额合计(本币) | number(23,8) | Y |  |
| 41 | RECEIVABLE_AMT_TC | 应收金额合计(原币) | number(23,8) | Y |  |
| 42 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 43 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 44 | GLMB_JE_ID | 主键 | GUID | Y |  |
| 45 | GLOB_JE_ID | 主键 | GUID | Y |  |
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | Attachments | 附件 | string | Y |  |
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 56 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 57 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 58 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 59 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 60 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 61 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 62 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 63 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 64 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 65 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 66 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 67 | UDF041 | 自定义字段12 | date | Y |  |
| 68 | UDF042 | 自定义字段13 | date | Y |  |
| 69 | UDF051 | 自定义字段14 | GUID | Y |  |
| 70 | UDF052 | 自定义字段15 | GUID | Y |  |
| 71 | UDF053 | 自定义字段16 | GUID | Y |  |
| 72 | UDF054 | 自定义字段17 | GUID | Y |  |
| 73 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 74 | ApproveDate | 修改日期 | date | Y |  |
| 75 | ApproveBy | 修改人 | GUID | Y |  |
| 76 | PrintCount | 打印次数 | number | Y |  |
| 77 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 78 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 79 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 80 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 81 | Owner_Org_RTK |  | string(400) | Y |  |
| 82 | Owner_Org_ROid |  | GUID | Y |  |
| 83 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 84 | SOURCE_ID_ROid |  | GUID | Y |  |
| 85 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 86 | SOURCE2_ID_ROid |  | GUID | Y |  |

### OTHER_RECEIVABLE_DOC_D (其他应收单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OTHER_RECEIVABLE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 4 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | LINE_TYPE | 行类型 | number | Y |  |
| 7 | SETTLEMENT_NO |  | string(60) | Y |  |
| 8 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 9 | DUE_DATE | 到期日 | date | Y |  |
| 10 | OTHER_ARAP_ITEM_ID | 其他应收项目 | GUID | Y |  |
| 11 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 12 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 13 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 14 | PROJECT_ID | 项目 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | OTHER_RECEIVABLE_DOC_ID |  | GUID | Y |  |