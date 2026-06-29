---
module: "CASH"
name_zh: "现金回收"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 106
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# CASH (现金回收)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 106

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


- **CASH_RECYCLING_DOC (现金存取单)**
- **CASH_RECYCLING_DOC_D (现金存取单单身)**


---


---


> Tables: 2

### CASH_RECYCLING_DOC (现金存取单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CASH_RECYCLING_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | RECYCLING_TYPE | 存取类型 | number | Y |  |
| 12 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 13 | SETTLE_METHOD_CATEGORY_DETAIL | 结算方式类别明细 | number | Y |  |
| 14 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
| 16 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 17 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 18 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 19 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 20 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 21 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 22 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 23 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 24 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 25 | NOTE_BOOK_ID | 票据簿 | GUID | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | SERIAL_NO | 顺序号 | string(16) | Y |  |
| 28 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 29 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 30 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 31 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 32 | PrintCount | 打印次数 | number | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |

### CASH_RECYCLING_DOC_D (现金存取单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CASH_RECYCLING_DOC_D_ID | 主键 | GUID | Y | Y |
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
| 42 | CASH_RECYCLING_DOC_ID |  | GUID | Y |  |