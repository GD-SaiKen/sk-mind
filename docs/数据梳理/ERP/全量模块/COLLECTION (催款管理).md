---
module: "COLLECTION"
name_zh: "催款管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 249
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# COLLECTION (催款管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 249

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


- **COLLECTION_DOC (收款单)**
- **COLLECTION_DOC_ADVREC (收款单转预收)**
- **COLLECTION_DOC_D (收款单单身)**
- **COLLECTION_DOC_VERIFIED (收款单应收核销)**


---


---


> Tables: 4

### COLLECTION_DOC (收款单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | COLLECTION_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE |  | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 12 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 13 | CASH_TRANS_INDICATOR | 现结标识 | number(0/1) | Y |  |
| 14 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 15 | MULTI_CURRENCY_INDICATOR | 异货币核销标识 | number(0/1) | Y |  |
| 16 | COLLECTION_AMT_TC | 实收金额合计(原币) | number(23,8) | Y |  |
| 17 | COLLECTION_AMT_FC | 实收金额合计(本币) | number(23,8) | Y |  |
| 18 | SETTLE_EXPENSE_AMT_TC | 结算费用合计(原币) | number(23,8) | Y |  |
| 19 | SETTLE_EXPENSE_AMT_FC | 结算费用合计(本币) | number(23,8) | Y |  |
| 20 | ADDITIONAL_EXPENSE_AMT_TC | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 21 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 22 | AR_VERIFICATION_AMT_TC | 应收核销金额合计(原币) | number(23,8) | Y |  |
| 23 | AR_VERIFICATION_AMT_FC | 应收核销金额合计(本币) | number(23,8) | Y |  |
| 24 | CASH_DISCOUNT_AMT_TC | 现金折扣合计(原币) | number(23,8) | Y |  |
| 25 | CASH_DISCOUNT_AMT_FC | 现金折扣合计(本币) | number(23,8) | Y |  |
| 26 | ADV_REC_VERIFIED_AMT_TC | 预收冲减金额合计(原币) | number(23,8) | Y |  |
| 27 | ADV_REC_VERIFIED_AMT_FC | 预收冲减金额合计(本币) | number(23,8) | Y |  |
| 28 | ADV_REC_AMT_TC | 转预收金额合计(原币) | number(23,8) | Y |  |
| 29 | ADV_REC_AMT_FC | 转预收金额合计(本币) | number(23,8) | Y |  |
| 30 | AR_EXCHANGE_LOSS_AMT | 应收核销-汇兑损失合计 | number(23,8) | Y |  |
| 31 | ADV_REC_EXCHANGE_LOSS_AMT | 预收冲减-汇兑损失合计 | number(23,8) | Y |  |
| 32 | LOSS_AMT_TC | 财务损失合计(原币) | number(23,8) | Y |  |
| 33 | LOSS_AMT_FC | 财务损失合计(本币) | number(23,8) | Y |  |
| 34 | GAIN_AMT_TC | 利得(原币) | number(23,8) | Y |  |
| 35 | GAIN_AMT_FC | 利得(本币) | number(23,8) | Y |  |
| 36 | GAIN_REMARK | 利得备注 | string(510) | Y |  |
| 37 | REMARK | 备注 | string(510) | Y |  |
| 38 | EMPLOYEE_ID | 收款业务员 | GUID | Y |  |
| 39 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 40 | CURRENCY_ID | 货币 | GUID | Y |  |
| 41 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 42 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 43 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 44 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 45 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 46 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 47 | OFFSET_INSTAL_ADV_FLAG | 分期预收款冲减标识 | number(0/1) | Y |  |
| 48 | NMC_INDICATOR | 受控出纳管理系统标识 | number(0/1) | Y |  |
| 49 | CREDIT_RECEIVABLES_AMT_TC | 转贷项应收款合计(原币) | number(23,8) | Y |  |
| 50 | CREDIT_RECEIVABLES_AMT_FC | 转贷项应收款合计(本币) | number(23,8) | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 53 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 54 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 55 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 56 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 57 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 58 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 59 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 60 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 61 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 62 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 63 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 64 | UDF041 | 自定义字段12 | date | Y |  |
| 65 | UDF042 | 自定义字段13 | date | Y |  |
| 66 | UDF051 | 自定义字段14 | GUID | Y |  |
| 67 | UDF052 | 自定义字段15 | GUID | Y |  |
| 68 | UDF053 | 自定义字段16 | GUID | Y |  |
| 69 | UDF054 | 自定义字段17 | GUID | Y |  |
| 70 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 71 | ApproveDate | 修改日期 | date | Y |  |
| 72 | ApproveBy | 修改人 | GUID | Y |  |
| 73 | PrintCount | 打印次数 | number | Y |  |
| 74 | CreateDate | 创建日期 | date | Y |  |
| 75 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 76 | ModifiedDate | 修改日期 | date | Y |  |
| 77 | CreateBy | 创建者 | GUID | Y |  |
| 78 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 79 | ModifiedBy | 修改者 | GUID | Y |  |
| 80 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 81 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 82 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 83 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 84 | Attachments | 附件 | string | Y |  |
| 85 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 86 | Owner_Org_RTK |  | string(400) | Y |  |
| 87 | Owner_Org_ROid |  | GUID | Y |  |
| 88 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 89 | SOURCE_ID_ROid |  | GUID | Y |  |
| 90 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 91 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 92 | CURRENCY_EXG_LOSS_AMT | 实收货币汇兑损失 | number(23,8) | Y |  |

### COLLECTION_DOC_ADVREC (收款单转预收)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COLLECTION_DOC_ADVREC_ID |  | GUID | Y | Y |
| 3 | TRANS_DOC_TYPE | 业务单据类型 | number | Y |  |
| 4 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 5 | ADV_REC_AMT_TC | 本次预收金额(原币) | number(23,8) | Y |  |
| 6 | ADV_REC_AMT_FC | 本次预收金额(本币) | number(23,8) | Y |  |
| 7 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 10 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 11 | TRANS_DESCRIPTION | 款项描述 | string(120) | Y |  |
| 12 | INSTALLMENT_INDICATOR | 分期标识 | number(0/1) | Y |  |
| 13 | ADV_REC_LIMIT_AMT_TC | 可预收金额(原币) | number(23,8) | Y |  |
| 14 | LINE_TYPE | 行类型 | number | Y |  |
| 15 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 16 | OTHER_ARAP_ITEM_ID | 其他应收项目 | GUID | Y |  |
| 17 | PAYMENT_DATE | 付款日 | date | Y |  |
| 18 | CASHING_DATE | 兑现日 | date | Y |  |
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
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 52 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 54 | COLLECTION_DOC_ID |  | GUID | Y |  |

### COLLECTION_DOC_D (收款单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COLLECTION_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO |  | string(60) | Y |  |
| 5 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 6 | DUE_DATE | 到期日 | date | Y |  |
| 7 | AMT_TC | 实收/结算费用金额(原币) | number(23,8) | Y |  |
| 8 | AMT_FC | 实收/结算费用金额(本币) | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 11 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 12 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 13 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 14 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 50 | COLLECTION_DOC_ID |  | GUID | Y |  |

### COLLECTION_DOC_VERIFIED (收款单应收核销)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COLLECTION_DOC_VERIFIED_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | BALANCE_AMT_TC | 应收/预收余额(原币) | number(23,8) | Y |  |
| 6 | BALANCE_AMT_FC | 应收/预收余额(本币) | number(23,8) | Y |  |
| 7 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 8 | VERIFICATION_TOTAL_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 9 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 10 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 11 | VERIFICATION_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 12 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 13 | CASH_DISCOUNT_AMT_TC | 现金折扣(原币) | number(23,8) | Y |  |
| 14 | CASH_DISCOUNT_AMT_FC | 现金折扣(本币) | number(23,8) | Y |  |
| 15 | LOSS_AMT_TC | 财务损失(原币) | number(23,8) | Y |  |
| 16 | LOSS_AMT_FC | 财务损失(本币) | number(23,8) | Y |  |
| 17 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
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
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 52 | SOURCE_ID_ROid |  | GUID | Y |  |
| 53 | COLLECTION_DOC_ID |  | GUID | Y |  |