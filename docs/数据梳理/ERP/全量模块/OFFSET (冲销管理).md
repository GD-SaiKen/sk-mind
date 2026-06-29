---
module: "OFFSET"
name_zh: "冲销管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 164
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# OFFSET (冲销管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 164

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


- **OFFSET_DOC (往来冲账单)**
- **OFFSET_DOC_AP (往来冲账单单身-应付)**
- **OFFSET_DOC_D (往来冲账单单身-应收)**


---


---


> Tables: 3

### OFFSET_DOC (往来冲账单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | OFFSET_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | ARSETTLEMENT_OBJECT_TYPE | 应收结算对象类型 | number | Y |  |
| 12 | APSETTLEMENT_OBJECT_TYPE | 应收结算对象类型 | number | Y |  |
| 13 | SPECIFIC_CURRENCY_INDICATOR | 特定货币 | number(0/1) | Y |  |
| 14 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 15 | RECEIVABLE_AMT_TC | 应收/预收合计 (原币) | number(23,8) | Y |  |
| 16 | RECEIVABLE_AMT_FC | 应收/预收合计(本币) | number(23,8) | Y |  |
| 17 | PAYABLE_AMT_TC | 应付/预付合计(原币) | number(23,8) | Y |  |
| 18 | PAYABLE_AMT_FC | 应付/预付合计(本币) | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | TRANS_TYPE | 业务类型 | number | Y |  |
| 21 | NON_OFFSET_AMT_TC | 未冲减金额(原币) | number(23,8) | Y |  |
| 22 | NON_OFFSET_AMT_FC | 未冲减金额(本币) | number(23,8) | Y |  |
| 23 | CURRENCY_ID | 货币 | GUID | Y |  |
| 24 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 25 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 26 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 27 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
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
| 46 | PrintCount | 打印次数 | number | Y |  |
| 47 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 48 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 49 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 50 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 61 | ApproveDate | 修改日期 | date | Y |  |
| 62 | ApproveBy | 修改人 | GUID | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |
| 65 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE_ID_ROid |  | GUID | Y |  |
| 67 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 68 | SOURCE2_ID_ROid |  | GUID | Y |  |

### OFFSET_DOC_AP (往来冲账单单身-应付)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OFFSET_DOC_AP_ID | 主键 | GUID | Y | Y |
| 3 | PAYABLES_TYPE | 应付款类型 | number | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 6 | BALANCE_AMT_TC | 应付/预付余额(原币) | number(23,8) | Y |  |
| 7 | BALANCE_AMT_FC | 应付/预付余额(本币) | number(23,8) | Y |  |
| 8 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 9 | VERIFICATION_TOTAL_AMT_TC |  | number(23,8) | Y |  |
| 10 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 11 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 12 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
| 16 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 17 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 48 | OFFSET_DOC_ID |  | GUID | Y |  |

### OFFSET_DOC_D (往来冲账单单身-应收)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OFFSET_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 6 | BALANCE_AMT_TC | 应收/预收余额(原币) | number(23,8) | Y |  |
| 7 | BALANCE_AMT_FC | 应收/预收余额(本币) | number(23,8) | Y |  |
| 8 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 9 | VERIFICATION_TOTAL_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 10 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 11 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 12 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
| 16 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 17 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 48 | OFFSET_DOC_ID |  | GUID | Y |  |