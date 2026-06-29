---
module: "PAYMENT"
name_zh: "付款管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 19
columns: 975
category: financial
semantic_object: "Payment/付款"
original_tables: 19
filtered_out: 0
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# PAYMENT (付款管理) - Payment/付款

> [!info] Phase 1 Core Module
> Semantic Object: Payment/付款
> Kept: 19 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 3

## Related Modules

- [[../modules/GL (总账).md|GL (总账)]]
- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]

---

## Tables

- **PAYMENT_ADVICE_DOC (付款建议单)**
- **PAYMENT_ADVICE_DOC_D (付款建议单单身)**
- **PAYMENT_ADVICE_DOC_SD (付款建议单子单身)**
- **PAYMENT_ADVICE_PCI (付款建议PCI)**
- **PAYMENT_ADVICE_PCI_D (付款单身明细)**
- **PAYMENT_ADVICE_TW_DOC (付款建议单)**
- **PAYMENT_ADVICE_TW_DOC_D (付款建议单单身)**
- **PAYMENT_ADVICE_TW_DOC_SD (付款建议单子单身)**
- **PAYMENT_DOC (付款单单身)**
- **PAYMENT_DOC_D (付款单单身)**
- **PAYMENT_DOC_PREPAYMENT (付款单转账款)**
- **PAYMENT_DOC_VERIFIED (付款单应付核销)**
- **PAYMENT_PROMOTION_DOC (付款单据)**
- **PAYMENT_PROMOTION_DOC_D (付款单身明细)**
- **PAYMENT_PROMOTION_DOC_D1 (付款促销单明细1)**
- **PAYMENT_PROMOTION_DOC_D2 (付款促销单明细2)**
- **PAYMENT_PROMOTION_DOC_D3 (付款促销单明细3)**
- **PAYMENT_PROMOTION_DOC_D4 (付款促销单明细4)**
- **PAYMENT_TERM (收付款条件)**

---

## Table Details

### PAYMENT_ADVICE_DOC (付款建议单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PAYMENT_ADVICE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 10 | ADVISING_NET_AMT_TC | 建议实付金额合计(原币) | number(23,8) | Y |  |
| 11 | AUTH_NET_AMT_TC | 核准实付金额合计(原币) | number(23,8) | Y |  |
| 12 | PAID_AMT_TC | 实际支付金额合计(原币) | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CURRENCY_ID | 货币 | GUID | Y |  |
| 15 | PrintCount | 打印次数 | number | Y |  |
| 16 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 17 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 18 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 19 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |


### PAYMENT_ADVICE_DOC_D (付款建议单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_ADVICE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 4 | BALANCE_AMT_TC | 应付余额(原币) | number(23,8) | Y |  |
| 5 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 6 | ADVISING_CASH_DISC_AMT_TC | 建议现金折扣(原币) | number(23,8) | Y |  |
| 7 | ADVISING_NET_AMT_TC | 建议实付金额(原币) | number(23,8) | Y |  |
| 8 | AUTH_CASH_DISC_AMT_TC | 核准现金折扣(原币) | number(23,8) | Y |  |
| 9 | AUTH_NET_AMT_TC | 核准实付金额(原币) | number(23,8) | Y |  |
| 10 | PAID_AMT_TC | 实际支付金额(原币) | number(23,8) | Y |  |
| 11 | CASH_DISCOUNT_AMT_TC | 现金折扣(原币) | number(23,8) | Y |  |
| 12 | AUTH_REMARK | 核准备注 | string(510) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 15 | BANK_ACCOUNT_ID | 主键 | GUID | Y |  |
| 16 | EMPLOYEE_ID | 付款业务员 | GUID | Y |  |
| 17 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 18 | PAYMENT_DOC_ID | 付款单 | GUID | Y |  |
| 19 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 20 | DUE_DATE | 到期日 | date | Y |  |
| 21 | CHARGE_BURDEN_MODE | 手续费负担方式 | number | Y |  |
| 22 | CHARGE_SETTLEMENT_METHOD_ID | 手续费结算方式 | GUID | Y |  |
| 23 | CHARGE_AMT_TC | 手续费(原币) | number(23,8) | Y |  |
| 24 | CHARGE_EXPENSE_ID | 手续费用项目 | GUID | Y |  |
| 25 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 26 | FIN_INSTITUTION_ACCOUNT_NO | 金融机构账号 | string(60) | Y |  |
| 27 | NOTE_PREFIX_CODE | 票据前置码 | string(10) | Y |  |
| 28 | NOTE_NO | 票据流水号 | string(30) | Y |  |
| 29 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 30 | TWNM_NOTE_BOOK_FLAG | 票据本标识 | number(0/1) | Y |  |
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
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 61 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 62 | SOURCE_ID_ROid |  | GUID | Y |  |
| 63 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 64 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 65 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 67 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 68 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 69 | PAYMENT_ADVICE_DOC_ID |  | GUID | Y |  |


### PAYMENT_ADVICE_DOC_SD (付款建议单子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SELECTION_INDICATOR | 选定标识 | number(0/1) | Y |  |
| 3 | PAYMENT_ADVICE_DOC_SD_ID | 主键 | GUID | Y | Y |
| 4 | PAYABLES_TYPE | 账款类型 | number | Y |  |
| 5 | DUE_DATE | 到期日 | date | Y |  |
| 6 | BALANCE_AMT_TC | 应付余额(原币) | number(23,8) | Y |  |
| 7 | AUTH_NET_AMT_TC | 核准实付金额(原币) | number(23,8) | Y |  |
| 8 | ADVISING_CASH_DISC_AMT_TC | 建议现金折扣(原币) | number(23,8) | Y |  |
| 9 | ADVISING_NET_AMT_TC | 建议实付金额(原币) | number(23,8) | Y |  |
| 10 | AUTH_CASH_DISC_AMT_TC | 核准现金折扣(原币) | number(23,8) | Y |  |
| 11 | PAID_AMT_TC | 实际支付金额(原币) | number(23,8) | Y |  |
| 12 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 13 | CASH_DISCOUNT_AMT_TC | 现金折扣(原币) | number(23,8) | Y |  |
| 14 | AUTH_REMARK | 核准备注 | string(510) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
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
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | PAYMENT_ADVICE_DOC_D_ID |  | GUID | Y |  |


### PAYMENT_ADVICE_PCI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PAYMENT_ADVICE_PCI_ID | 主键 | GUID | Y | Y |
| 4 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 5 | BANK_ACCOUNT_ID | 付款银行 | GUID | Y |  |
| 6 | TWNM_NOTE_BOOK_FLAG | 票据本标识 | number(0/1) | Y |  |
| 7 | CHARGE_SETTLEMENT_METHOD_ID | 手续费结算方式 | GUID | Y |  |
| 8 | CHARGE_AMT_TC | 手续费(原币) | number(23,8) | Y |  |
| 9 | CHARGE_EXPENSE_ID | 手续费用项目 | GUID | Y |  |
| 10 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 11 | DUE_DATE | 到期日 | date | Y |  |
| 12 | AUTH_NET_AMT_TC | 核准实付金额合计(原币) | number(23,8) | Y |  |
| 13 | CURRENCY_ID | 货币 | GUID | Y |  |
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
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |


### PAYMENT_ADVICE_PCI_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_ADVICE_PCI_D_ID | 主键 | GUID | Y | Y |
| 3 | CHECK_FLAG | 选中标识 | number(0/1) | Y |  |
| 4 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 5 | BANK_ACCOUNT_ID | 付款银行 | GUID | Y |  |
| 6 | TWNM_NOTE_BOOK_FLAG | 票据本标识 | number(0/1) | Y |  |
| 7 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 8 | DUE_DATE | 到期日 | date | Y |  |
| 9 | CHARGE_BURDEN_MODE | 手续费负担方式 | number | Y |  |
| 10 | CHARGE_SETTLEMENT_METHOD_ID | 手续费结算方式 | GUID | Y |  |
| 11 | CHARGE_AMT_TC | 手续费(原币) | number(23,8) | Y |  |
| 12 | CHARGE_EXPENSE_ID | 手续费用项目 | GUID | Y |  |
| 13 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 14 | FIN_INSTITUTION_ACCOUNT_NO | 金融机构账号 | string(60) | Y |  |
| 15 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 16 | NOTE_PREFIX_CODE | 票据前置码 | string(10) | Y |  |
| 17 | NOTE_NO | 票据流水号 | string(16) | Y |  |
| 18 | AUTH_NET_AMT_TC | 核准实付金额(原币) | number(23,8) | Y |  |
| 19 | PAYMENT_ADVICE_DOC_D_ID | 付款建议单单身主键 | GUID | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |
| 47 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 49 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 51 | PAYMENT_ADVICE_PCI_ID |  | GUID | Y |  |


### PAYMENT_ADVICE_TW_DOC (付款建议单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | PAYMENT_ADVICE_TW_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CURRENCY_ID | 货币 | GUID | Y |  |
| 8 | NMC_INDICATOR | 受控票据管理系统 | number(0/1) | Y |  |
| 9 | ADVISING_CASH_DISC_AMT_TC | 建议现金折扣合计(原币) | number(23,8) | Y |  |
| 10 | AUTH_CASH_DISC_AMT_TC | 核准现金折扣合计(原币) | number(23,8) | Y |  |
| 11 | ADVISING_NET_AMT_TC | 建议实付合计(原币) | number(23,8) | Y |  |
| 12 | AUTH_NET_AMT_TC | 核准实付合计(原币) | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | PrintCount | 打印次数 | number | Y |  |
| 15 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 16 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 17 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 18 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |


### PAYMENT_ADVICE_TW_DOC_D (付款建议单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_ADVICE_TW_DOC_D_ID |  | GUID | Y | Y |
| 3 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 4 | BALANCE_AMT_TC | 应付余额(原币) | number(23,8) | Y |  |
| 5 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 6 | AVAILABLE_AMT_TC | 可付余额(原币) | number(23,8) | Y |  |
| 7 | ADVISING_CASH_DISC_AMT_TC | 建议现金折扣(原币) | number(23,8) | Y |  |
| 8 | ADVISING_NET_AMT_TC | 建议实付金额(原币) | number(23,8) | Y |  |
| 9 | AUTH_CASH_DISC_AMT_TC | 核准现金折扣(原币) | number(23,8) | Y |  |
| 10 | AUTH_NET_AMT_TC | 核准实付金额(原币) | number(23,8) | Y |  |
| 11 | AUTH_COUNT | 核准账款笔数 | number | Y |  |
| 12 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 13 | BANK_ACCOUNT_ID | 付款银行 | GUID | Y |  |
| 14 | SCHEDULED_TRANSFER_FLAG | 预约付款标识 | number(0/1) | Y |  |
| 15 | CASHING_DATE | 兑现日 | date | Y |  |
| 16 | TWNM_ITEM_ID | 存提项目 | GUID | Y |  |
| 17 | TWNM_NOTE_BOOK_D_ID | 票据本 | GUID | Y |  |
| 18 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 19 | CHARGE_BURDEN_MODE | 费用负担方式 | number | Y |  |
| 20 | CHARGE_SETTLEMENT_METHOD_ID | 费用结算方式 | GUID | Y |  |
| 21 | CHARGE_AMT_TC | 费用(原币) | number(23,8) | Y |  |
| 22 | CHARGE_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 23 | FIN_INSTITUTION_ID | 供应商银行 | GUID | Y |  |
| 24 | FIN_INSTITUTION_ACCOUNT_NO | 供应商银行账号 | string(60) | Y |  |
| 25 | FINANCE_DOC_TYPE | 金融单据类型 | number | Y |  |
| 26 | EMPLOYEE_ID | 付款业务员 | GUID | Y |  |
| 27 | ADMIN_UNIT_ID | 付款业务部门 | GUID | Y |  |
| 28 | SETTLEMENT_METHOD_CATEGORY | 结算方式类别 | number | Y |  |
| 29 | SYSTEM_REMARK | 系统信息 | string(510) | Y |  |
| 30 | PAYMENT_REMARK | 付款备注 | string(510) | Y |  |
| 31 | AUTH_REMARK | 核准备注 | string(510) | Y |  |
| 32 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 33 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 34 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 35 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 36 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 37 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 38 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 39 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 40 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 41 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 42 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 43 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 44 | UDF041 | 自定义字段12 | date | Y |  |
| 45 | UDF042 | 自定义字段13 | date | Y |  |
| 46 | UDF051 | 自定义字段14 | GUID | Y |  |
| 47 | UDF052 | 自定义字段15 | GUID | Y |  |
| 48 | UDF053 | 自定义字段16 | GUID | Y |  |
| 49 | UDF054 | 自定义字段17 | GUID | Y |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE_ID_ROid |  | GUID | Y |  |
| 62 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 63 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 64 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 65 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 66 | PAYMENT_ADVICE_TW_DOC_ID |  | GUID | Y |  |


### PAYMENT_ADVICE_TW_DOC_SD (付款建议单子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_ADVICE_TW_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | PAYABLES_TYPE | 账款类型 | number | Y |  |
| 4 | SELECTION_FLAG | 选择标识 | number(0/1) | Y |  |
| 5 | PAYMENT_DATE | 付款日 | date | Y |  |
| 6 | CASHING_DATE | 兑现日 | date | Y |  |
| 7 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 8 | BALANCE_AMT_TC | 应付余额(原币) | number(23,8) | Y |  |
| 9 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 10 | AVAILABLE_AMT_TC | 可付余额(原币) | number(23,8) | Y |  |
| 11 | ADVISING_CASH_DISC_AMT_TC | 建议现金折扣(原币) | number(23,8) | Y |  |
| 12 | ADVISING_NET_AMT_TC | 建议实付金额(原币) | number(23,8) | Y |  |
| 13 | AUTH_CASH_DISC_AMT_TC | 核准现金折扣(原币) | number(23,8) | Y |  |
| 14 | AUTH_NET_AMT_TC | 核准实付金额(原币) | number(23,8) | Y |  |
| 15 | AUTH_REMARK | 核准备注 | string(510) | Y |  |
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
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | PAYMENT_ADVICE_TW_DOC_D_ID |  | GUID | Y |  |


### PAYMENT_DOC (付款单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PAYMENT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 12 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 13 | CASH_TRANS_INDICATOR | 现结标识 | number(0/1) | Y |  |
| 14 | MULTI_CURRENCY_INDICATOR | 异货币核销标识 | number(0/1) | Y |  |
| 15 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 16 | PAYMENT_AMT_TC | 实付金额合计(原币) | number(23,8) | Y |  |
| 17 | PAYMENT_AMT_FC | 实付金额合计(本币) | number(23,8) | Y |  |
| 18 | ADDITIONAL_EXPENSE_AMT_TC | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 19 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 20 | AP_VERIFICATION_AMT_TC | 应付核销金额合计(原币) | number(23,8) | Y |  |
| 21 | AP_VERIFICATION_AMT_FC | 应付核销金额合计(本币) | number(23,8) | Y |  |
| 22 | CASH_DISCOUNT_AMT_TC | 现金折扣合计(原币) | number(23,8) | Y |  |
| 23 | CASH_DISCOUNT_AMT_FC | 现金折扣合计(本币) | number(23,8) | Y |  |
| 24 | PREPAYMENT_VERIFIED_AMT_TC | 预付冲减金额合计(原币) | number(23,8) | Y |  |
| 25 | AP_EXCHANGE_LOSS_AMT | 应付核销-汇兑损失合计 | number(23,8) | Y |  |
| 26 | PREPAYMENT_EXG_LOSS_AMT | 预付冲减-汇兑损失合计 | number(23,8) | Y |  |
| 27 | PREPAYMENT_AMT_TC | 转预付金额合计(原币) | number(23,8) | Y |  |
| 28 | PREPAYMENT_AMT_FC | 转预付金额合计(本币) | number(23,8) | Y |  |
| 29 | GAIN_AMT_TC | 利得合计(原币) | number(23,8) | Y |  |
| 30 | GAIN_AMT_FC | 利得合计(功能币) | number(23,8) | Y |  |
| 31 | LOSS_AMT_TC | 财务损失(原币) | number(23,8) | Y |  |
| 32 | LOSS_AMT_FC | 财务损失(本币) | number(23,8) | Y |  |
| 33 | LOSS_REMARK | 财务损失备注 | string(510) | Y |  |
| 34 | REMARK | 备注 | string(510) | Y |  |
| 35 | PREPAYMENT_VERIFIED_AMT_FC | 预付冲减金额合计(本币) | number(23,8) | Y |  |
| 36 | EMPLOYEE_ID | 付款业务员 | GUID | Y |  |
| 37 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 38 | CURRENCY_ID | 货币 | GUID | Y |  |
| 39 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 40 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 41 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 42 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 43 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 44 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 45 | OFFSET_INSTAL_ADV_FLAG | 分期预付款冲减标识 | number(0/1) | Y |  |
| 46 | DIRECT_FLAG | 直接标识 | number(0/1) | Y |  |
| 47 | NMC_INDICATOR | 受控出纳管理系统标识 | number(0/1) | Y |  |
| 48 | DEBIT_PAYABLES_AMT_TC | 转借项应付款合计(原币) | number(23,8) | Y |  |
| 49 | DEBIT_PAYABLES_AMT_FC | 转借项应付款合计(本币) | number(23,8) | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 52 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 53 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 54 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 55 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 56 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 57 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 58 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 59 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 60 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 61 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 62 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 63 | UDF041 | 自定义字段12 | date | Y |  |
| 64 | UDF042 | 自定义字段13 | date | Y |  |
| 65 | UDF051 | 自定义字段14 | GUID | Y |  |
| 66 | UDF052 | 自定义字段15 | GUID | Y |  |
| 67 | UDF053 | 自定义字段16 | GUID | Y |  |
| 68 | UDF054 | 自定义字段17 | GUID | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | CreateDate | 创建日期 | date | Y |  |
| 73 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 74 | ModifiedDate | 修改日期 | date | Y |  |
| 75 | CreateBy | 创建者 | GUID | Y |  |
| 76 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 77 | ModifiedBy | 修改者 | GUID | Y |  |
| 78 | Attachments | 附件 | string | Y |  |
| 79 | PrintCount | 打印次数 | number | Y |  |
| 80 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 81 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 82 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 83 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 84 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 85 | Owner_Org_RTK |  | string(400) | Y |  |
| 86 | Owner_Org_ROid |  | GUID | Y |  |
| 87 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 88 | SOURCE_ID_ROid |  | GUID | Y |  |
| 89 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 90 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 91 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 92 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 93 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 94 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 95 | CURRENCY_EXG_LOSS_AMT | 实付货币汇兑损失 | number(23,8) | Y |  |


### PAYMENT_DOC_D (付款单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 5 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 6 | DUE_DATE | 到期日 | date | Y |  |
| 7 | AMT_TC | 实付/结算费用金额(原币) | number(23,8) | Y |  |
| 8 | AMT_FC | 实付/结算费用金额(本币) | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 11 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 12 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 13 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 14 | CURRENCY_ID | 货币 | GUID | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | SOURCE_DOC_TRANS_DETAIL | 来源单据业务明细 | number | Y |  |
| 17 | GROUP_FLAG | 群组标识 | number(0/1) | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE_ID_ROid |  | GUID | Y |  |
| 45 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 47 | PAYMENT_DOC_ID |  | GUID | Y |  |


### PAYMENT_DOC_PREPAYMENT (付款单转账款)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_DOC_PREPAYMENT_ID | 主键 | GUID | Y | Y |
| 3 | TRANS_DOC_TYPE | 业务单据类型 | number | Y |  |
| 4 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 5 | PREPAYMENT_AMT_TC | 本次预付金额(原币) | number(23,8) | Y |  |
| 6 | PREPAYMENT_AMT_FC | 本次预付金额(本币) | number(23,8) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 9 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 10 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 11 | TRANS_DESCRIPTION | 款项描述 | string(120) | Y |  |
| 12 | INSTALLMENT_INDICATOR | 分期标识 | number(0/1) | Y |  |
| 13 | PREPAYMENT_LIMIT_AMT_TC | 可预付金额(原币) | number(23,8) | Y |  |
| 14 | LINE_TYPE | 行类型 | number | Y |  |
| 15 | PAYMENT_DATE | 付款日 | date | Y |  |
| 16 | CASHING_DATE | 兑现日 | date | Y |  |
| 17 | OTHER_ARAP_ITEM_ID | 其他应付项目 | GUID | Y |  |
| 18 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 19 | PROJECT_ID | 项目 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |
| 47 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 49 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 51 | PAYMENT_DOC_ID |  | GUID | Y |  |


### PAYMENT_DOC_VERIFIED (付款单应付核销)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_DOC_VERIFIED_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | BALANCE_AMT_TC | 应付/预付余额(原币) | number(23,8) | Y |  |
| 6 | BALANCE_AMT_FC | 应付/预付余额(本币) | number(23,8) | Y |  |
| 7 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 8 | VERIFICATION_TOTAL_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 9 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 10 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 11 | VERIFICATION_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 12 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 13 | CASH_DISCOUNT_AMT_TC | 现金折扣(原币) | number(23,8) | Y |  |
| 14 | CASH_DISCOUNT_AMT_FC | 现金折扣(本币) | number(23,8) | Y |  |
| 15 | GAIN_AMT_TC | 利得(原币) | number(23,8) | Y |  |
| 16 | GAIN_AMT_FC | 利得(本币) | number(23,8) | Y |  |
| 17 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 20 | CURRENCY_ID | 货币 | GUID | Y |  |
| 21 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 22 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | PAYMENT_DOC_ID |  | GUID | Y |  |


### PAYMENT_PROMOTION_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PAYMENT_PROMOTION_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PROMOTION_SCHEDULE_ID | 促销活动 | GUID | Y |  |
| 9 | SHOP_RANGE | 门店范围 | string(40) | Y |  |
| 10 | CUSTOMER_RANGE | 顾客范围 | string(40) | Y |  |
| 11 | BEGDT | 开始日期 | date | Y |  |
| 12 | BEGTM | 开始时间 | date | Y |  |
| 13 | ENDDT | 结束日期 | date | Y |  |
| 14 | ENDTM | 结束时间 | date | Y |  |
| 15 | WEEK_CIRCULATION | 星期循环 | number(0/1) | Y |  |
| 16 | MONDAY | 周一 | number(0/1) | Y |  |
| 17 | TUESDAY | 周二 | number(0/1) | Y |  |
| 18 | WEDNESDAY | 周三 | number(0/1) | Y |  |
| 19 | THURSDAY | 周四 | number(0/1) | Y |  |
| 20 | FRIDAY | 周五 | number(0/1) | Y |  |
| 21 | SATURDAY | 周六 | number(0/1) | Y |  |
| 22 | SUNDAY | 周日 | number(0/1) | Y |  |
| 23 | TIME_CIRCULATION | 时间循环 | number(0/1) | Y |  |
| 24 | WEEK_BEGTM | 起始时间 | date | Y |  |
| 25 | WEEK_ENDTM | 截止时间 | date | Y |  |
| 26 | PROMOTION_DESCRIPTION | 促销简述 | string(200) | Y |  |
| 27 | COUNTER_CHARGE_ID | 费用分摊类型 | GUID | Y |  |
| 28 | REMARK | 备注 | string(510) | Y |  |
| 29 | PrintCount | 打印次数 | number | Y |  |
| 30 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 31 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 32 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 33 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 34 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 35 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 36 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 37 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 38 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 39 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 40 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 41 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 42 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 43 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 44 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 45 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 46 | UDF041 | 自定义字段12 | date | Y |  |
| 47 | UDF042 | 自定义字段13 | date | Y |  |
| 48 | UDF051 | 自定义字段14 | GUID | Y |  |
| 49 | UDF052 | 自定义字段15 | GUID | Y |  |
| 50 | UDF053 | 自定义字段16 | GUID | Y |  |
| 51 | UDF054 | 自定义字段17 | GUID | Y |  |
| 52 | CreateDate | 创建日期 | date | Y |  |
| 53 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 54 | ModifiedDate | 修改日期 | date | Y |  |
| 55 | CreateBy | 创建者 | GUID | Y |  |
| 56 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 57 | ModifiedBy | 修改者 | GUID | Y |  |
| 58 | Attachments | 附件 | string | Y |  |
| 59 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |


### PAYMENT_PROMOTION_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_PROMOTION_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 门店 | GUID | Y |  |
| 4 | JOIN_COUNTER | 参与租柜 | string(40) | Y |  |
| 5 | SHARE_DEFINITION | 分摊定义 | string(40) | Y |  |
| 6 | SHARE_LIMIT | 分摊限制 | string(40) | Y |  |
| 7 | LIMIT_AMT | 限制金额 | number(23,8) | Y |  |
| 8 | LIMIT_QUANTITY | 限制数量 | number(16,6) | Y |  |
| 9 | COMPENSATIN_MODE | 补偿方式 | string(40) | Y |  |
| 10 | EACH_PIECE_AMT | 每件金额 | number(23,8) | Y |  |
| 11 | AMT_RATE | 金额比率 | number(5,4) | Y |  |
| 12 | DISCOUNT_AMT_RATE | 优惠额比率 | number(5,4) | Y |  |
| 13 | DISCOUNT_AMT_LIST | 优惠额比率取价 | string(40) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | PAYMENT_PROMOTION_DOC_ID |  | GUID | Y |  |


### PAYMENT_PROMOTION_DOC_D1

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_PROMOTION_DOC_D1_ID | 主键 | GUID | Y | Y |
| 3 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 4 | DISCOUNT_SET | 折扣设定 | string(40) | Y |  |
| 5 | BILL_DISCOUNT | 整单折扣 | number(5,4) | Y |  |
| 6 | FULL_REDUCTION_SET | 满减设定 | string(40) | Y |  |
| 7 | FULL_REDUCTION_AMT | 整单满减金额 | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
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
| 35 | PAYMENT_PROMOTION_DOC_ID |  | GUID | Y |  |


### PAYMENT_PROMOTION_DOC_D2

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_PROMOTION_DOC_D2_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | DISCOUNT |  | number(5,4) | Y |  |
| 6 | FULL_REDUCTION_CALCULATION | 满减算法 | string(40) | Y |  |
| 7 | REDUCTION_AMT | 满减金额 | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
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
| 35 | PAYMENT_PROMOTION_DOC_D1_ID |  | GUID | Y |  |


### PAYMENT_PROMOTION_DOC_D3

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_PROMOTION_DOC_D3_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 门店 | GUID | Y |  |
| 4 | COUNTER_ID | 租柜 | GUID | Y |  |
| 5 | SHARE_LIMIT | 分摊限制 | string(40) | Y |  |
| 6 | LIMIT_AMT | 限制金额 | number(23,8) | Y |  |
| 7 | LIMIT_QUANTITY | 限制数量 | number(16,6) | Y |  |
| 8 | COMPENSATIN_MODE | 补偿方式 | string(40) | Y |  |
| 9 | EACH_PIECE_AMT | 每件金额 | number(23,8) | Y |  |
| 10 | AMT_RATE | 金额比率 | number(5,4) | Y |  |
| 11 | DISCOUNT_AMT_RATE | 优惠额比率 | number(5,4) | Y |  |
| 12 | DISCOUNT_AMT_LIST | 优惠额比率取价 | string(40) | Y |  |
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
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | PAYMENT_PROMOTION_DOC_D_ID |  | GUID | Y |  |


### PAYMENT_PROMOTION_DOC_D4

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYMENT_PROMOTION_DOC_D4_ID | 主键 | GUID | Y | Y |
| 3 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
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
| 30 | PAYMENT_PROMOTION_DOC_ID |  | GUID | Y |  |


### PAYMENT_TERM (收付款条件)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PAYMENT_TERM_ID | 主键 | GUID | Y | Y |
| 4 | PAYMENT_TERM_TYPE | 类别 | string(40) | Y |  |
| 5 | PAYMENT_TERM_CODE | 编号 | string(20) | Y |  |
| 6 | PAYMENT_TERM_NAME | 名称 | string(240) | Y |  |
| 7 | RANGE | 范围 | string(40) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | PAY_START_DATE | 收/付款起算日 | string(40) | Y |  |
| 10 | PAY_ADD_MONTH | 收/付款加月数 | number(0/1) | Y |  |
| 11 | PAY_ADD_DAY | 收/付款加日数 | number(0/1) | Y |  |
| 12 | PAY_MONTH | 收/付款月数 | number | Y |  |
| 13 | PAY_DAY | 收/付款日数 | number | Y |  |
| 14 | PAY_COME_UPON | 收/付款逢 | number | Y |  |
| 15 | CASH_START_DATE | 兑现起算日 | string(40) | Y |  |
| 16 | CASH_ADD_MONTH | 兑现加月数 | number(0/1) | Y |  |
| 17 | CASH_ADD_DAY | 兑现加日数 | number(0/1) | Y |  |
| 18 | CASH_MONTH | 兑现月数 | number | Y |  |
| 19 | CASH_DAY | 兑现日数 | number | Y |  |
| 20 | DISCOUNT_CHOOES | 折扣方式 | number | Y |  |
| 21 | DISCOUNT_DAY1 | 折扣期间1 | number | Y |  |
| 22 | DISCOUNT_RATE1 | 折扣比率1 | number(5,4) | Y |  |
| 23 | DISCOUNT_DAY2 | 折扣期间2 | number | Y |  |
| 24 | DISCOUNT_RATE2 | 折扣比率2 | number(5,4) | Y |  |
| 25 | DISCOUNT_DAY3 | 折扣期间3 | number | Y |  |
| 26 | DISCOUNT_RATE3 | 折扣比率3 | number(5,4) | Y |  |
| 27 | PAY_CAN_COME_UPON | 收/付款逢日 | number(0/1) | Y |  |
| 28 | CASH_CAN_COME_UPON | 兑现逢日 | number(0/1) | Y |  |
| 29 | CASH_COME_UPON | 兑现逢 | number | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Attachments | 附件 | string | Y |  |
| 37 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 38 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 39 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 40 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 41 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 42 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 43 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 44 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 45 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 46 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 47 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 48 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 49 | UDF041 | 自定义字段12 | date | Y |  |
| 50 | UDF042 | 自定义字段13 | date | Y |  |
| 51 | UDF051 | 自定义字段14 | GUID | Y |  |
| 52 | UDF052 | 自定义字段15 | GUID | Y |  |
| 53 | UDF053 | 自定义字段16 | GUID | Y |  |
| 54 | UDF054 | 自定义字段17 | GUID | Y |  |
| 55 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | Owner_Org_RTK |  | string(400) | Y |  |
| 61 | Owner_Org_ROid |  | GUID | Y |  |
