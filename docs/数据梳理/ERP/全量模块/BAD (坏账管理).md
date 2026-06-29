---
module: "BAD"
name_zh: "坏账管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 105
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# BAD (坏账管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 105

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


- **BAD_DEBT_DOC (坏账损失单)**
- **BAD_DEBT_DOC_D (坏账损失单单身)**


---


---


> Tables: 2

### BAD_DEBT_DOC (坏账损失单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | BAD_DEBT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 业务日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 12 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 13 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 14 | BAD_DEBT_AMT_TC | 坏账金额合计(原币) | number(23,8) | Y |  |
| 15 | BAD_DEBT_AMT_FC | 坏账金额合计(功能币) | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | CURRENCY_ID | 货币 | GUID | Y |  |
| 18 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 19 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 20 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 21 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 22 | PrintCount | 打印次数 | number | Y |  |
| 23 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 24 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 25 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 26 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 57 | Owner_Org_RTK |  | string(400) | Y |  |
| 58 | Owner_Org_ROid |  | GUID | Y |  |
| 59 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE_ID_ROid |  | GUID | Y |  |

### BAD_DEBT_DOC_D (坏账损失单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BAD_DEBT_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 4 | BALANCE_AMT_TC | 应收/其他应收余额(原币) | number(23,8) | Y |  |
| 5 | BALANCE_AMT_FC | 应收/其他应收余额(功能币) | number(23,8) | Y |  |
| 6 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 7 | BAD_DEBT_AMT_TC | 坏账金额(原币) | number(23,8) | Y |  |
| 8 | BAD_DEBT_AMT_FC | 坏账金额(功能币) | number(23,8) | Y |  |
| 9 | PROVISION_AMT | 坏账准备 | number(23,8) | Y |  |
| 10 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 13 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 14 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
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
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 45 | BAD_DEBT_DOC_ID |  | GUID | Y |  |