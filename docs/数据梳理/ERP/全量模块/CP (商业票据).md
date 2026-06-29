---
module: "CP"
name_zh: "商业票据"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 197
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# CP (商业票据)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 197

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


- **CP_DEF_BANKACCOUNT (默认银行账号)**
- **CP_DEF_BANKACCOUNT_D (默认银行账号单身)**
- **CP_DOC (收支单)**
- **CP_DOC_D (收支单单身)**


---


---


> Tables: 4

### CP_DEF_BANKACCOUNT (默认银行账号)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CP_DEF_BANKACCOUNT_ID | 主键 | GUID | Y | Y |
| 4 | CP_TYPE | 收付类型 | number | Y |  |
| 5 | TRANS_ORG_FLAG | 限定条件标识-业务域 | number(0/1) | Y |  |
| 6 | SETTLEMENT_METHOD_FLAG | 限定条件标识-结算方式 | number(0/1) | Y |  |
| 7 | CURRENCY_FLAG | 限定条件标识-货币 | number(0/1) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### CP_DEF_BANKACCOUNT_D (默认银行账号单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CP_DEF_BANKACCOUNT_D_ID | 主键 | GUID | Y | Y |
| 3 | TRANS_ORG_TYPE | 业务域类型 | number | Y |  |
| 4 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
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
| 33 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 34 | SOURCE_ID_ROid |  | GUID | Y |  |
| 35 | CP_DEF_BANKACCOUNT_ID |  | GUID | Y |  |

### CP_DOC (收支单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CP_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | INITIALIZED_FLAG | 初始化标识 | number(0/1) | Y |  |
| 12 | CP_TYPE | 收付类型 | number | Y |  |
| 13 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 14 | SETTLE_METHOD_CATEGORY_DETAIL | 结算方式类别明细 | number | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 17 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 18 | ACCOUNTS_SYS_FLAG | 需往来系统核销标识 | number(0/1) | Y |  |
| 19 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 20 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 21 | CURRENCY_ID | 货币 | GUID | Y |  |
| 22 | OTHER_ARAP_ITEM_ID | 收付项目 | GUID | Y |  |
| 23 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 24 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 25 | JOURNAL_INDICATOR | 产生分录码 | number(0/1) | Y |  |
| 26 | EMPLOYEE_ID | 业务员 | GUID | Y |  |
| 27 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 28 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 29 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 30 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 31 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 32 | REMARK | 备注 | string(510) | Y |  |
| 33 | NOTE_BOOK_ID | 票据簿 | GUID | Y |  |
| 34 | ACCOUNTS_SYS2_FLAG | 往来系统已核销标识 | number(0/1) | Y |  |
| 35 | ACCOUNTS_SYS_TRANSDOC_TYPE | 往来系统业务单据类型 | number | Y |  |
| 36 | GROUP_FLAG | 群组标识 | number(0/1) | Y |  |
| 37 | SETTLE_EXPENSE_AMT_TC | 结算费用合计(原币) | number(23,8) | Y |  |
| 38 | SETTLE_EXPENSE_AMT_FC | 结算费用合计(本币) | number(23,8) | Y |  |
| 39 | SERIAL_NO | 顺序号 | string(16) | Y |  |
| 40 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 41 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 42 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 43 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 44 | PrintCount | 打印次数 | number | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 58 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 59 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 60 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 61 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 62 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 63 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 64 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 65 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 66 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 67 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 68 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 69 | UDF041 | 自定义字段12 | date | Y |  |
| 70 | UDF042 | 自定义字段13 | date | Y |  |
| 71 | UDF051 | 自定义字段14 | GUID | Y |  |
| 72 | UDF052 | 自定义字段15 | GUID | Y |  |
| 73 | UDF053 | 自定义字段16 | GUID | Y |  |
| 74 | UDF054 | 自定义字段17 | GUID | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |
| 77 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 78 | SOURCE_ID_ROid |  | GUID | Y |  |
| 79 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 80 | SOURCE2_ID_ROid |  | GUID | Y |  |

### CP_DOC_D (收支单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CP_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 5 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 6 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 7 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 8 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 9 | CURRENCY_ID | 货币 | GUID | Y |  |
| 10 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 11 | AMT_TC | 费用金额(原币) | number(23,8) | Y |  |
| 12 | AMT_FC | 费用金额(本币) | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
| 21 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 22 | ApproveDate | 修改日期 | date | Y |  |
| 23 | ApproveBy | 修改人 | GUID | Y |  |
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
| 42 | CP_DOC_ID |  | GUID | Y |  |