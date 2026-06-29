---
module: "BANK"
name_zh: "银行管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 9
columns: 442
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# BANK (银行管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 9 | Columns: 442

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]
- [[CLOSE (关账检查)|CLOSE (关账检查)]]

---

## Tables


- **BANK_ACCOUNT (银行账号信息)**
- **BANK_ACCOUNT_D**
- **BANK_BALANCE**
- **BANK_EXCHANGE_DOC (银行调汇单)**
- **BANK_EXCHANGE_DOC_D (银行调汇单单身)**
- **BANK_HISTORY**
- **BANK_TRANSFER_DOC (银行调拨单)**
- **BANK_TRANSFER_DOC_D (银行调拨单单身)**


---


---


> Tables: 9

### BANK (银行信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BANK_CODE | 银行编号 | string(40) | Y |  |
| 4 | BANK_ID | 主键 | GUID | Y | Y |
| 5 | BANK_SHORT_NAME | 银行简称 | string(40) | Y |  |
| 6 | BANK_FULL_NAME | 银行全称 | string(144) | Y |  |
| 7 | BANK_EN_FULL_NAME | 银行英文全称 | string(200) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | ADDRESS | 地址 | string(510) | Y |  |
| 10 | CONTACT | 联系人 | string(72) | Y |  |
| 11 | TELEPHONEP | 电话 | string(40) | Y |  |
| 12 | BANK_STATEMENT_DIR | 银行对账单方向 | number | Y |  |
| 13 | AUTOMATIC_REMITTANCE_FLAG | 自动汇款 | number(0/1) | Y |  |
| 14 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 15 | BANK_NO | 银行行号 | string(40) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### BANK_ACCOUNT (银行账号信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BANK_ACCOUNT_ID | 主键 | GUID | Y | Y |
| 4 | BANK_ID | 银行编号 | GUID | Y |  |
| 5 | BANK_ACCOUNT_NO | 银行账号 | string(60) | Y |  |
| 6 | PORPUSE | 用途 | string(60) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | ID_NUMBER | 统编/身份证号 | string(100) | Y |  |
| 9 | ACCOUNT_NAME | 户名 | string(160) | Y |  |
| 10 | CONTACT | 联系人 | string(72) | Y |  |
| 11 | TELEPHONE | 电话 | string(40) | Y |  |
| 12 | FAX_NO | 传真 | string(40) | Y |  |
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

### BANK_ACCOUNT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BANK_ACCOUNT_D_ID | 主键 | GUID | Y | Y |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CURRENCY_ID | 货币 | GUID | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | BANK_ACCOUNT_ID |  | GUID | Y |  |

### BANK_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BANK_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 6 | OPENING_AMT_TC | 期初金额(原币) | number(23,8) | Y |  |
| 7 | OPENING_AMT_FC | 期初金额(本币) | number(23,8) | Y |  |
| 8 | DEBIT_AMT_TC | 本期借方发生额(原币) | number(23,8) | Y |  |
| 9 | DEBIT_AMT_FC | 本期借方发生额(本币) | number(23,8) | Y |  |
| 10 | CREDIT_AMT_TC | 本期贷方发生额(原币) | number(23,8) | Y |  |
| 11 | CREDIT_AMT_FC | 本期贷方发生额(本币) | number(23,8) | Y |  |
| 12 | CURRENCY_ID | 货币 | GUID | Y |  |
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
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |

### BANK_EXCHANGE_DOC (银行调汇单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | BANK_EXCHANGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | EXCHANGE_LOSS_AMT | 汇兑损失合计 | number(23,8) | Y |  |
| 12 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 13 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 16 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
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
| 35 | PrintCount | 打印次数 | number | Y |  |
| 36 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 37 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 38 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 39 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### BANK_EXCHANGE_DOC_D (银行调汇单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BANK_EXCHANGE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | string(40) | Y |  |
| 4 | CURRENCY_ID | 货币 | GUID | Y |  |
| 5 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 6 | BALANCE_AMT_TC | 余额(原币) | number(23,8) | Y |  |
| 7 | BALANCE_AMT_FC | 余额(本币) | number(23,8) | Y |  |
| 8 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 9 | REVALUATION_BALANCE_AMT | 调整后余额 | number(23,8) | Y |  |
| 10 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 13 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 14 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 15 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 16 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 17 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 18 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 19 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 20 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 21 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 22 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 23 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 24 | UDF041 | 自定义字段12 | date | Y |  |
| 25 | UDF042 | 自定义字段13 | date | Y |  |
| 26 | UDF051 | 自定义字段14 | GUID | Y |  |
| 27 | UDF052 | 自定义字段15 | GUID | Y |  |
| 28 | UDF053 | 自定义字段16 | GUID | Y |  |
| 29 | UDF054 | 自定义字段17 | GUID | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | BANK_EXCHANGE_DOC_ID |  | GUID | Y |  |

### BANK_HISTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BANK_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 6 | DOC_DATE | 业务日期 | date | Y |  |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | SORT_DATE | 排序日期 | date | Y |  |
| 9 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 10 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 11 | TRANS_NATURE | 交易性质 | number | Y |  |
| 12 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 13 | DUE_DATE | 到期日 | date | Y |  |
| 14 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 15 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 16 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | ACCOUNTS_SYS_FLAG | 需往来系统核销标识 | number(0/1) | Y |  |
| 19 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 20 | CURRENCY_ID | 货币 | GUID | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Attachments | 附件 | string | Y |  |
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
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |
| 50 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE_ID_ROid |  | GUID | Y |  |
| 52 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 54 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 56 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 57 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 58 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 60 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 62 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 63 | SOURCE7_ID_ROid |  | GUID | Y |  |
| 64 | SOURCE8_ID_RTK |  | string(400) | Y |  |
| 65 | SOURCE8_ID_ROid |  | GUID | Y |  |
| 66 | SOURCE9_ID_RTK |  | string(400) | Y |  |
| 67 | SOURCE9_ID_ROid |  | GUID | Y |  |
| 68 | EMPLOYEE_ID | 业务员 | GUID | Y |  |
| 69 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |

### BANK_TRANSFER_DOC (银行调拨单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | BANK_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | MULTI_CURRENCY_FLAG | 异货币标识 | number(0/1) | Y |  |
| 12 | SETTLE_METHOD_CATEGORY_DETAIL | 结算方式类别明细 | number | Y |  |
| 13 | TFO_EXCHANGE_RATE | 转出汇率 | number(18,9) | Y |  |
| 14 | TFO_AMT_TC | 转出金额(原币) | number(23,8) | Y |  |
| 15 | TFO_AMT_FC | 转出金额(本币) | number(23,8) | Y |  |
| 16 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 17 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 18 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 19 | TFO_BANK_ACCOUNT_ID | 转出银行账号 | GUID | Y |  |
| 20 | TFO_CURRENCY_ID | 转出货币 | GUID | Y |  |
| 21 | TFI_BANK_ACCOUNT_ID | 转入银行账号 | GUID | Y |  |
| 22 | TFI_CURRENCY_ID | 转入货币 | GUID | Y |  |
| 23 | TFI_EXCHANGE_RATE | 转入汇率 | number(18,9) | Y |  |
| 24 | TFI_AMT_TC | 转入金额(原币) | number(23,8) | Y |  |
| 25 | TFI_AMT_FC | 转入金额(本币) | number(23,8) | Y |  |
| 26 | SETTLE_EXPENSE_AMT_TC | 结算费用合计(原币) | number(23,8) | Y |  |
| 27 | SETTLE_EXPENSE_AMT_FC | 结算费用合计(本币) | number(23,8) | Y |  |
| 28 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 29 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 30 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 33 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 34 | NOTE_BOOK_ID | 票据簿 | GUID | Y |  |
| 35 | SERIAL_NO | 顺序号 | string(16) | Y |  |
| 36 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 37 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 38 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 39 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 40 | PrintCount | 打印次数 | number | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | Attachments | 附件 | string | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 54 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 55 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 56 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 57 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 58 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 59 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 60 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 61 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 62 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 63 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 64 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 65 | UDF041 | 自定义字段12 | date | Y |  |
| 66 | UDF042 | 自定义字段13 | date | Y |  |
| 67 | UDF051 | 自定义字段14 | GUID | Y |  |
| 68 | UDF052 | 自定义字段15 | GUID | Y |  |
| 69 | UDF053 | 自定义字段16 | GUID | Y |  |
| 70 | UDF054 | 自定义字段17 | GUID | Y |  |
| 71 | Owner_Org_RTK |  | string(400) | Y |  |
| 72 | Owner_Org_ROid |  | GUID | Y |  |

### BANK_TRANSFER_DOC_D (银行调拨单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | LINE_TYPE | 行类型 | number | Y |  |
| 3 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 4 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 5 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 6 | AMT_TC | 费用金额(原币) | number(23,8) | Y |  |
| 7 | AMT_FC | 费用金额(本币) | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 10 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 11 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 12 | CURRENCY_ID | 货币 | GUID | Y |  |
| 13 | BANK_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
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
| 42 | BANK_TRANSFER_DOC_ID |  | GUID | Y |  |