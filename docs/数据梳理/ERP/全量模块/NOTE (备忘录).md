---
module: "NOTE"
name_zh: "备忘录"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 300
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# NOTE (备忘录)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 5 | Columns: 300

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[PARA (参数设置)|PARA (参数设置)]]

---

## Tables


- **NOTE_BOOK (票据簿)**
- **NOTE_HISTORY**
- **NOTE_HISTORY_D**
- **NOTE_HISTORY_PAYMENT**
- **NOTE_NO_DETAIL (票据号码明细档)**


---


---


> Tables: 5

### NOTE_BOOK (票据簿)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | NOTE_BOOK_ID | 主键 | GUID | Y | Y |
| 4 | BANK_ID | 银行 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | NOTE_CATEGORY | 票据类别 | number | Y |  |
| 7 | NOTE_NO_PREFIX | 票号前缀 | string(16) | Y |  |
| 8 | START_SERIAL_NO | 起始号码 | number | Y |  |
| 9 | CUTOFF_SERIAL_NO | 截止号码 | number | Y |  |
| 10 | TOTAL_COUNTS | 总张数 | number | Y |  |
| 11 | USED_COUNTS | 已用张数 | number | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 21 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 22 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 23 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 24 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 25 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 26 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 27 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 28 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 29 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 30 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 31 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 32 | UDF041 | 自定义字段12 | date | Y |  |
| 33 | UDF042 | 自定义字段13 | date | Y |  |
| 34 | UDF051 | 自定义字段14 | GUID | Y |  |
| 35 | UDF052 | 自定义字段15 | GUID | Y |  |
| 36 | UDF053 | 自定义字段16 | GUID | Y |  |
| 37 | UDF054 | 自定义字段17 | GUID | Y |  |
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### NOTE_HISTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | NOTE_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | NOTE_NATURE | 票据性质 | number | Y |  |
| 5 | INITIALIZED_FLAG | 初始化标识 | number(0/1) | Y |  |
| 6 | TRANS_DATE | 业务日期 | date | Y |  |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | NOTE_ACT | 票据行为 | number | Y |  |
| 11 | NOTE_ACT_DETAIL | 票据行为明细 | number | Y |  |
| 12 | NOTE_TRANS_SEQNO | 票据业务序号 | number | Y |  |
| 13 | TRANS_BANK_FULLNAME | 业务受理行全称 | string(144) | Y |  |
| 14 | TRANS_BANK_NO | 业务受理行行号 | string(40) | Y |  |
| 15 | TRANS_BANK_ADDRESS | 业务受理行地址 | string(510) | Y |  |
| 16 | FACE_CURRENCY_EXG | 票面货币_汇率 | number(18,9) | Y |  |
| 17 | FACE_AMT_TC | 票面金额(原币) | number(23,8) | Y |  |
| 18 | FACE_AMT_FC | 票面金额(本币) | number(23,8) | Y |  |
| 19 | FACE_CURRENCY_ID | 票面货币 | GUID | Y |  |
| 20 | MATURITY_AMT_TC | 到期金额(原币) | number(23,8) | Y |  |
| 21 | MATURITY_AMT_FC | 到期金额(本币) | number(23,8) | Y |  |
| 22 | FACE_CURR_DISCINT_AMT_TC | 票面货币_贴现息(原币) | number(23,8) | Y |  |
| 23 | FACE_CURR_DISCINT_AMT_FC | 票面货币_贴现息(本币) | number(23,8) | Y |  |
| 24 | TRANS_CURRENCY_EXG | 业务货币汇率 | number(18,9) | Y |  |
| 25 | TRANS_CURRENCY_ID | 业务货币 | GUID | Y |  |
| 26 | TRANS_CURR_AMT_TC | 业务金额(原币) | number(23,8) | Y |  |
| 27 | TRANS_CURR_AMT_FC | 业务金额(本币) | number(23,8) | Y |  |
| 28 | TRANS_CURR2_AMT_TC | 业务金额2(原币) | number(23,8) | Y |  |
| 29 | TRANS_CURR2_AMT_FC | 业务金额2(本币) | number(23,8) | Y |  |
| 30 | APR | 年利率 | number(6,5) | Y |  |
| 31 | DISCOUNT_DAYS | 贴现天数 | number | Y |  |
| 32 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 33 | ADDITIONAL_EXPENSE_AMT_TC | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 34 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 35 | CARRYING_FACE_EXG | 账面票面汇率 | number(18,9) | Y |  |
| 36 | CARRYING_FACE_AMT_TC | 账面票面金额(原币) | number(23,8) | Y |  |
| 37 | CARRYING_FACE_AMT_FC | 账面票面金额(本币) | number(23,8) | Y |  |
| 38 | CARRYING_FACE_EXG_LOSS_AMT | 账面票面汇兑损失 | number(23,8) | Y |  |
| 39 | ACCRUED_INTEREST_EXG | 已计利息汇率 | number(18,9) | Y |  |
| 40 | ACCRUED_INTEREST_AMT_TC | 已计利息金额(原币) | number(23,8) | Y |  |
| 41 | ACCRUED_INTEREST_AMT_FC | 已计利息金额(本币) | number(23,8) | Y |  |
| 42 | FI_EXPENSE_INTEREST_AMT | 已计财务费用利息收支 | number(23,8) | Y |  |
| 43 | INTEREST_EXG_LOSS_AMT | 已计利息汇兑损失 | number(23,8) | Y |  |
| 44 | CARRYING_EXG | 账面价值汇率 | number(18,9) | Y |  |
| 45 | CARRYING_AMT_TC | 账面价值金额(原币) | number(23,8) | Y |  |
| 46 | CARRYING_AMT_FC | 账面价值金额(本币) | number(23,8) | Y |  |
| 47 | CARRYING_EXG_LOSS_AMT | 账面价值汇兑损失 | number(23,8) | Y |  |
| 48 | INTEREST_NET_AMT_TC | 利息净额(原币) | number(23,8) | Y |  |
| 49 | INTEREST_NET_AMT_FC | 利息净额(本币) | number(23,8) | Y |  |
| 50 | ADDITIONAL_INTEREST_EXG | 补计利息汇率 | number(18,9) | Y |  |
| 51 | ADDITIONAL_INTEREST_AMT_TC | 补计利息金额(原币) | number(23,8) | Y |  |
| 52 | ADDITIONAL_INTEREST_AMT_FC | 补计利息金额(本币) | number(23,8) | Y |  |
| 53 | TRANS_EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 54 | ENDORSEE_TYPE | 被背书人类型 | number | Y |  |
| 55 | ACCOUNTS_SYS_FLAG | 需往来系统核销标识 | number(0/1) | Y |  |
| 56 | ACCOUNTS_SYS2_FLAG | 已被往来系统核销标识 | number(0/1) | Y |  |
| 57 | ACCOUNTS_SYS_CONTROL | 往来系统核销引用控制 | string(40) | Y |  |
| 58 | ACCOUNTS_SYS3_FLAG | 需转往来系统标识 | number(0/1) | Y |  |
| 59 | ACCOUNTS_SYS4_FLAG | 已转往来系统标识 | number(0/1) | Y |  |
| 60 | ACCOUNTS_SYS_TRANSDOC_NO | 往来系统业务单号 | string(80) | Y |  |
| 61 | LAST_NOTE_STATUS | 最近票据状态 | number | Y |  |
| 62 | LAST_NOTE_STATUS_DETAIL | 最近票据状态明细 | number | Y |  |
| 63 | LAST_STATUS_TRANS_DATE | 最近状态业务日期 | date | Y |  |
| 64 | LAST_STATUS_BOOKKEEPING_DATE | 最近状态记账日期 | date | Y |  |
| 65 | LAST_NOTE_STATUS2 | 次近票据状态 | number | Y |  |
| 66 | LAST_NOTE_STATUS_DETAIL2 | 次近票据状态明细 | number | Y |  |
| 67 | LAST_STATUS_TRANS_DATE2 | 次近状态业务日期 | date | Y |  |
| 68 | LAST_STATUS_BOOKKEEPING_DATE2 | 次近状态记账日期 | date | Y |  |
| 69 | LAST_ACT_TRANS_DATE | 最近行为业务日期 | date | Y |  |
| 70 | LAST_ACT_BOOKKEEPING_DATE | 最近行为记账日期 | date | Y |  |
| 71 | OLD_TRANS_BANK_ACCOUNT_ID | 原业务受理行账号 | GUID | Y |  |
| 72 | OLD_TRANS_BANK_FULLNAME | 原业务受理行全称 | string(144) | Y |  |
| 73 | OLD_TRANS_BANK_NO | 原业务受理行行号 | string(40) | Y |  |
| 74 | PLEDGEE | 质权人 | string(144) | Y |  |
| 75 | ACT_REMARK | 行为备注 | string(510) | Y |  |
| 76 | OTHER_ARAP_ITEM_ID | 收付项目 | GUID | Y |  |
| 77 | OLD_TRANS_CURRENCY_ID | 原业务货币 | GUID | Y |  |
| 78 | TRANS_REMARK | 业务备注 | string(510) | Y |  |
| 79 | JOURNAL_INDICATOR | 产生分录码 | number(0/1) | Y |  |
| 80 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 81 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 82 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 83 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 84 | NOTE_TYPE_ID | 票据类型 | GUID | Y |  |
| 85 | TRANS_BANK_ACCOUNT_ID | 业务受理行账号 | GUID | Y |  |
| 86 | INITIAL_TRANS_FLAG | 初始业务标识 | number(0/1) | Y |  |
| 87 | REVERSE_ORIGINAL_LINE_ID | 撤销源交易行 | GUID | Y |  |
| 88 | VIEW_SYS_CODE | 视图编号 | string(6) | Y |  |
| 89 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 90 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 91 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 92 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 93 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 94 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 95 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 96 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 97 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 98 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 99 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 100 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 101 | UDF041 | 自定义字段12 | date | Y |  |
| 102 | UDF042 | 自定义字段13 | date | Y |  |
| 103 | UDF051 | 自定义字段14 | GUID | Y |  |
| 104 | UDF052 | 自定义字段15 | GUID | Y |  |
| 105 | UDF053 | 自定义字段16 | GUID | Y |  |
| 106 | UDF054 | 自定义字段17 | GUID | Y |  |
| 107 | PrintCount | 打印次数 | number | Y |  |
| 108 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 109 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 110 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 111 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 112 | Version | 版本号，不要随意更改 | binary | Y |  |
| 113 | CreateDate | 创建日期 | date | Y |  |
| 114 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 115 | ModifiedDate | 修改日期 | date | Y |  |
| 116 | CreateBy | 创建者 | GUID | Y |  |
| 117 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 118 | ModifiedBy | 修改者 | GUID | Y |  |
| 119 | Attachments | 附件 | string | Y |  |
| 120 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 121 | Owner_Org_RTK |  | string(400) | Y |  |
| 122 | Owner_Org_ROid |  | GUID | Y |  |
| 123 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 124 | SOURCE_ID_ROid |  | GUID | Y |  |
| 125 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 126 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 127 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 128 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 129 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 130 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 131 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 132 | SOURCE5_ID_ROid |  | GUID | Y |  |

### NOTE_HISTORY_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | NOTE_HISTORY_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 5 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 6 | AMT_TC | 费用金额(原币) | number(23,8) | Y |  |
| 7 | AMT_FC | 费用金额(本币) | number(23,8) | Y |  |
| 8 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 9 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 10 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 11 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 12 | CURRENCY_ID | 货币 | GUID | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | NOTE_HISTORY_ID |  | GUID | Y |  |

### NOTE_HISTORY_PAYMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | NOTE_HISTORY_PAYMENT_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 5 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 6 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 7 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 8 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CURRENCY_ID | 货币 | GUID | Y |  |
| 11 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 12 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 13 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 14 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 15 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 16 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 17 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 18 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 19 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 20 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 21 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 22 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 23 | UDF041 | 自定义字段12 | date | Y |  |
| 24 | UDF042 | 自定义字段13 | date | Y |  |
| 25 | UDF051 | 自定义字段14 | GUID | Y |  |
| 26 | UDF052 | 自定义字段15 | GUID | Y |  |
| 27 | UDF053 | 自定义字段16 | GUID | Y |  |
| 28 | UDF054 | 自定义字段17 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 37 | SOURCE_ID_ROid |  | GUID | Y |  |
| 38 | NOTE_HISTORY_ID |  | GUID | Y |  |

### NOTE_NO_DETAIL (票据号码明细档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | NOTE_NO_DETAIL_ID | 主键 | GUID | Y | Y |
| 4 | NOTE_BOOK_ID | 票据簿 | GUID | Y |  |
| 5 | BANK_ID | 银行 | GUID | Y |  |
| 6 | CURRENCY_ID | 货币 | GUID | Y |  |
| 7 | NOTE_NO_PREFIX | 票号前缀 | string(16) | Y |  |
| 8 | SERIAL_NO | 顺序号 | string(16) | Y |  |
| 9 | SERIAL_NO2 | 顺序号2 | number | Y |  |
| 10 | NOTE_NO | 票据号码 | string(60) | Y |  |
| 11 | USED_STATUS | 使用状态 | number | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | NOTE_CATEGORY | 票据类别 | number | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 22 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 23 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 24 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 25 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 26 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 27 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 28 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 29 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 30 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 31 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 32 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 33 | UDF041 | 自定义字段12 | date | Y |  |
| 34 | UDF042 | 自定义字段13 | date | Y |  |
| 35 | UDF051 | 自定义字段14 | GUID | Y |  |
| 36 | UDF052 | 自定义字段15 | GUID | Y |  |
| 37 | UDF053 | 自定义字段16 | GUID | Y |  |
| 38 | UDF054 | 自定义字段17 | GUID | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |