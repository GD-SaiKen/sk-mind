---
module: "AR"
name_zh: "应收账款"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 22
columns: 1012
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# AR (应收账款)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 22 | Columns: 1012

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]
- [[CLOSE (关账检查)|CLOSE (关账检查)]]

---

## Tables


- **AR_AGING_TEMPLATE (应收账龄分析模板信息)**
- **AR_AGING_TEMPLATE_D (应收账龄分析模板单身)**
- **AR_AGING_TEMPLATE_SD (应收账龄分析模板子单身)**
- **AR_B005 (AR_B005)**
- **AR_B007 (AR_B007)**
- **AR_CHECK_SET**
- **AR_EXCHANGE_DOC (应收调汇单)**
- **AR_EXCHANGE_DOC_CURR (应收调汇单即时余额)**
- **AR_EXCHANGE_DOC_D (应收调汇单单身)**
- **AR_PROVISION_DOC (坏账准备单)**
- **AR_PROVISION_DOC_D (坏账准备单单身)**
- **AR_RECOVERY_DOC (坏账收回单)**
- **AR_RECOVERY_DOC_D (坏账收回单单身)**
- **AR_REFUND_DOC (应收退款单)**
- **AR_REFUND_DOC_CA (应收退款单转账款)**
- **AR_REFUND_DOC_D (应收退款单单身)**
- **AR_REFUND_DOC_VERIFIED (应收退款单应收核销)**
- **AR_SALES_COST_DETAIL (应收销售成本明细档)**
- **AR_SALES_COST_ELEMENT**
- **AR_SALES_COST_STATS (应收销售成本统计档)**
- **AR_TRANSFER_DOC (维护应收转销单)**
- **AR_TRANSFER_DOC_D (维护应收转销单单身)**


---


---


> Tables: 22

### AR_AGING_TEMPLATE (应收账龄分析模板信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AR_AGING_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | TEMPLATE_CODE | 编号 | string(12) | Y |  |
| 5 | TEMPLATE_NAME |  | string(40) | Y |  |
| 6 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | TEMPLATE_CATEGORY | 模板类别 | number | Y |  |
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

### AR_AGING_TEMPLATE_D (应收账龄分析模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AGE_START | 账龄起(天) | number | Y |  |
| 3 | AGE_END | 账龄止(天) | number | Y |  |
| 4 | AGE_DESCRIPTION |  | string(510) | Y |  |
| 5 | DEF_PROVISION_ACCRUED_RATE | .默认坏账准备计提比率( | number(5,4) | Y |  |
| 6 | AR_AGING_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | AR_AGING_TEMPLATE_ID |  | GUID | Y |  |

### AR_AGING_TEMPLATE_SD (应收账龄分析模板子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PROVISION_INDICATOR | 计提准备 | number(0/1) | Y |  |
| 3 | PROVISION_ACCRUED_RATE | 账准备计提比率 | number(5,4) | Y |  |
| 4 | AR_AGING_TEMPLATE_SD_ID | 主键 | GUID | Y | Y |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CUSTOMER_CREDIT_RATING_ID | 信用等级 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 14 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 15 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 16 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 17 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 18 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 19 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 20 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 21 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 22 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 23 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 24 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 25 | UDF041 | 自定义字段12 | date | Y |  |
| 26 | UDF042 | 自定义字段13 | date | Y |  |
| 27 | UDF051 | 自定义字段14 | GUID | Y |  |
| 28 | UDF052 | 自定义字段15 | GUID | Y |  |
| 29 | UDF053 | 自定义字段16 | GUID | Y |  |
| 30 | UDF054 | 自定义字段17 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | AR_AGING_TEMPLATE_D_ID |  | GUID | Y |  |

### AR_B005 (AR_B005)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AR_B005_ID | 主键 | GUID | Y | Y |
| 2 | AR_B005_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### AR_B007 (AR_B007)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AR_B007_ID | 主键 | GUID | Y | Y |
| 2 | AR_B007_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### AR_CHECK_SET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AR_CHECK_SET_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | AR_FLAG | 应收对账标识 | number(0/1) | Y |  |
| 6 | AR_ACCOUNT_TYPE | 应收对账科目类型 | number | Y |  |
| 7 | ADVREC_FLAG | 预收对账标识 | number(0/1) | Y |  |
| 8 | ADVREC_ACCOUNT_TYPE | 预收对账科目类型 | number | Y |  |
| 9 | OTHER_AR_FLAG | 其他应收对账标识 | number(0/1) | Y |  |
| 10 | OTHER_AR_ACCOUNT_TYPE | 其他应收对账科目类型 | number | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 37 | Attachments | 附件 | string | Y |  |
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE3_ID_ROid |  | GUID | Y |  |

### AR_EXCHANGE_DOC (应收调汇单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AR_EXCHANGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | CURR_EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 12 | EXCHANGE_LOSS_AMT | 期间汇兑损失合计 | number(23,8) | Y |  |
| 13 | CURR_EXCHANGE_LOSS_AMT | 即时汇兑损失合计 | number(23,8) | Y |  |
| 14 | REMARK |  | string(510) | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
| 16 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 17 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 18 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 19 | GLOB_JE_ID | 主键 | GUID | Y |  |
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
| 38 | PrintCount | 打印次数 | number | Y |  |
| 39 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 40 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 41 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 42 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Attachments | 附件 | string | Y |  |
| 50 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | Owner_Org_RTK |  | string(400) | Y |  |
| 56 | Owner_Org_ROid |  | GUID | Y |  |

### AR_EXCHANGE_DOC_CURR (应收调汇单即时余额)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_EXCHANGE_DOC_CURR_ID | 主键 | GUID | Y | Y |
| 3 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | BALANCE_AMT_TC | 应收/预收余额(原币) | number(23,8) | Y |  |
| 6 | BALANCE_AMT_FC | 应收/预收余额(本币) | number(23,8) | Y |  |
| 7 | REVALUATION_BALANCE_AMT | 调整后余额 | number(23,8) | Y |  |
| 8 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 9 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 10 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 11 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 14 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 15 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 16 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 17 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 18 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 19 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 20 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 21 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 22 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 23 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 24 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 25 | UDF041 | 自定义字段12 | date | Y |  |
| 26 | UDF042 | 自定义字段13 | date | Y |  |
| 27 | UDF051 | 自定义字段14 | GUID | Y |  |
| 28 | UDF052 | 自定义字段15 | GUID | Y |  |
| 29 | UDF053 | 自定义字段16 | GUID | Y |  |
| 30 | UDF054 | 自定义字段17 | GUID | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | AR_EXCHANGE_DOC_ID |  | GUID | Y |  |

### AR_EXCHANGE_DOC_D (应收调汇单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_EXCHANGE_DOC_D_ID |  | GUID | Y | Y |
| 3 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | BALANCE_AMT_TC | 应收/预收余额(原币) | number(23,8) | Y |  |
| 6 | BALANCE_AMT_FC | 应收/预收余额(本币) | number(23,8) | Y |  |
| 7 | REVALUATION_BALANCE_AMT | 调整后余额 | number(23,8) | Y |  |
| 8 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 11 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 12 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 13 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 14 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 15 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 16 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 17 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 18 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 19 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 20 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 21 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 22 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 23 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 24 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 25 | UDF041 | 自定义字段12 | date | Y |  |
| 26 | UDF042 | 自定义字段13 | date | Y |  |
| 27 | UDF051 | 自定义字段14 | GUID | Y |  |
| 28 | UDF052 | 自定义字段15 | GUID | Y |  |
| 29 | UDF053 | 自定义字段16 | GUID | Y |  |
| 30 | UDF054 | 自定义字段17 | GUID | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | AR_EXCHANGE_DOC_ID |  | GUID | Y |  |

### AR_PROVISION_DOC (坏账准备单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AR_PROVISION_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 12 | AGE_BASE_DATE | 账龄基准日 | date | Y |  |
| 13 | REMARK | 被准 | string(510) | Y |  |
| 14 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 15 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 16 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 17 | ORIGINAL_PROVISION_AMT | 已提坏账金额合计 | number(23,8) | Y |  |
| 18 | ACCRUED_PROVISION_AMT | 已提坏账准备合计 | number(23,8) | Y |  |
| 19 | ADDED_PROVISION_AMT | 补提坏账准备合计 | number(23,8) | Y |  |
| 20 | PROVISION_ACCRUED_MODE | 坏账准备计提方式 | number | Y |  |
| 21 | GLOB_JE_ID | 主键 | GUID | Y |  |
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

### AR_PROVISION_DOC_D (坏账准备单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_PROVISION_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | DUE_DATE | 到期日 | date | Y |  |
| 4 | AGE_DESCRIPTION |  | string(510) | Y |  |
| 5 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 6 | BALANCE_AMT_TC | 应收/其他应收余额(原币) | number(23,8) | Y |  |
| 7 | BALANCE_AMT_FC | 应收/其他应收余额(本币) | number(23,8) | Y |  |
| 8 | ACCRUED_RATE | 本次坏账准备计提比率 | number(5,4) | Y |  |
| 9 | ORIGINAL_PROVISION_AMT | 坏账准备已提金额 | number(23,8) | Y |  |
| 10 | ACCRUED_PROVISION_AMT | 本次坏账准备应提金额 | number(23,8) | Y |  |
| 11 | ADDED_PROVISION_AMT | 本次坏账准备补提金额 | number(23,8) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 14 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 15 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 16 | CUSTOMER_CREDIT_RATING_ID | 客户信用等级 | GUID | Y |  |
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
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |
| 47 | AR_PROVISION_DOC_ID |  | GUID | Y |  |

### AR_RECOVERY_DOC (坏账收回单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AR_RECOVERY_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 10 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 11 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 12 | RECOVERY_AMT_TC | 坏账收回金额(原币) | number(23,8) | Y |  |
| 13 | RECOVERY_AMT_FC | 坏账收回金额(本币) | number(23,8) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 16 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 17 | CURRENCY_ID | 货币 | GUID | Y |  |
| 18 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 19 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 20 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 21 | GLMB_JE_ID | 主键 | GUID | Y |  |
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

### AR_RECOVERY_DOC_D (坏账收回单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_RECOVERY_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | BAD_DEBT_AMT_TC | 坏账金额(原币) | number(23,8) | Y |  |
| 4 | RECOVERY_AMT_TC | 坏账收回金额(原币) | number(23,8) | Y |  |
| 5 | RECOVERY_AMT_FC | 坏账收回金额(功能币) | number(23,8) | Y |  |
| 6 | PROVISION_AMT | 坏账准备 | number(23,8) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 9 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 10 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
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
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 41 | AR_RECOVERY_DOC_ID |  | GUID | Y |  |

### AR_REFUND_DOC (应收退款单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AR_REFUND_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 12 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 13 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 14 | MULTI_CURRENCY_INDICATOR | 异货币核销标识 | number(0/1) | Y |  |
| 15 | REFUND_AMT_TC | 实付金额合计(原币) | number(23,8) | Y |  |
| 16 | REFUND_AMT_FC | 实付金额合计(本币) | number(23,8) | Y |  |
| 17 | ADDITIONAL_EXPENSE_AMT_TC | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 18 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 19 | AR_VERIFICATION_AMT_TC | 应收核销金额合计(原币) | number(23,8) | Y |  |
| 20 | AR_VERIFICATION_AMT_FC | 应收核销金额合计(本币) | number(23,8) | Y |  |
| 21 | ADV_REC_VERIFIED_AMT_TC | 预收核销金额合计(原币) | number(23,8) | Y |  |
| 22 | ADV_REC_VERIFIED_AMT_FC | 预收核销金额合计(本币) | number(23,8) | Y |  |
| 23 | CASH_DISCOUNT_AMT_TC | 现金折扣合计(原币) | number(23,8) | Y |  |
| 24 | CASH_DISCOUNT_AMT_FC | 现金折扣合计(本币) | number(23,8) | Y |  |
| 25 | AR_EXCHANGE_LOSS_AMT | 应收核销-汇兑损失合计 | number(23,8) | Y |  |
| 26 | ADV_REC_EXCHANGE_LOSS_AMT | 预收核销-汇兑损失合计 | number(23,8) | Y |  |
| 27 | GAIN_AMT_TC | 利得合计(原币) | number(23,8) | Y |  |
| 28 | GAIN_AMT_FC | 利得合计(本币) | number(23,8) | Y |  |
| 29 | LOSS_AMT_TC | 财务损失(原币) | number(23,8) | Y |  |
| 30 | LOSS_AMT_FC | 财务损失(本币) | number(23,8) | Y |  |
| 31 | LOSS_REMARK |  | string(510) | Y |  |
| 32 | REMARK | 备注 | string(510) | Y |  |
| 33 | EMPLOYEE_ID | 付款业务员 | GUID | Y |  |
| 34 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 35 | CURRENCY_ID | 货币 | GUID | Y |  |
| 36 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 37 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 38 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 39 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 40 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 41 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 42 | NMC_INDICATOR | 受控出纳管理系统标识 | number(0/1) | Y |  |
| 43 | RECEIVABLES_AMT_TC | 转应收款合计(原币) | number(23,8) | Y |  |
| 44 | RECEIVABLES_AMT_FC | 转应收款合计(本币) | number(23,8) | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 47 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 48 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 49 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 50 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 51 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 52 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 53 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 54 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 55 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 56 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 57 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 58 | UDF041 | 自定义字段12 | date | Y |  |
| 59 | UDF042 | 自定义字段13 | date | Y |  |
| 60 | UDF051 | 自定义字段14 | GUID | Y |  |
| 61 | UDF052 | 自定义字段15 | GUID | Y |  |
| 62 | UDF053 | 自定义字段16 | GUID | Y |  |
| 63 | UDF054 | 自定义字段17 | GUID | Y |  |
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |
| 67 | CreateDate | 创建日期 | date | Y |  |
| 68 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 69 | ModifiedDate | 修改日期 | date | Y |  |
| 70 | CreateBy | 创建者 | GUID | Y |  |
| 71 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 72 | ModifiedBy | 修改者 | GUID | Y |  |
| 73 | PrintCount | 打印次数 | number | Y |  |
| 74 | Attachments | 附件 | string | Y |  |
| 75 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 76 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 77 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 78 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 79 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 80 | Owner_Org_RTK |  | string(400) | Y |  |
| 81 | Owner_Org_ROid |  | GUID | Y |  |
| 82 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 83 | SOURCE_ID_ROid |  | GUID | Y |  |
| 84 | CURRENCY_EXG_LOSS_AMT | 实付货币汇兑损失 | number(23,8) | Y |  |

### AR_REFUND_DOC_CA (应收退款单转账款)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_REFUND_DOC_CA_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 5 | AMT_TC | 账款金额(原币) | number(23,8) | Y |  |
| 6 | AMT_FC | 账款金额(本币) | number(23,8) | Y |  |
| 7 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 8 | OTHER_ARAP_ITEM_ID | 其他应收项目 | GUID | Y |  |
| 9 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 10 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 11 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 12 | PAYMENT_DATE | 付款日 | date | Y |  |
| 13 | CASHING_DATE | 兑现日 | date | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | PROJECT_ID | 项目 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | AR_REFUND_DOC_ID |  | GUID | Y |  |

### AR_REFUND_DOC_D (应收退款单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_REFUND_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO |  | string(60) | Y |  |
| 5 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 6 | DUE_DATE | 到期日 | date | Y |  |
| 7 | AMT_TC | 实付/结算费用金额(原币) | number(23,8) | Y |  |
| 8 | AMT_FC | 实付/结算费用金额(本币) | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 11 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 12 | SETTLEMENT_EXPENSE_ID | 结算费用 | GUID | Y |  |
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
| 50 | AR_REFUND_DOC_ID |  | GUID | Y |  |

### AR_REFUND_DOC_VERIFIED (应收退款单应收核销)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_REFUND_DOC_VERIFIED_ID | 主键 | GUID | Y | Y |
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
| 15 | GAIN_AMT_TC | 利得(原币) | number(23,8) | Y |  |
| 16 | GAIN_AMT_FC | 利得(本币) | number(23,8) | Y |  |
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
| 53 | AR_REFUND_DOC_ID |  | GUID | Y |  |

### AR_SALES_COST_DETAIL (应收销售成本明细档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AR_SALES_COST_DETAIL_ID | 主键 | GUID | Y | Y |
| 4 | SALSE_TRANSDOC_LINE_ID | 销售业务单据行 | GUID | Y |  |
| 5 | SALSE_TRANSDOC_COST_AMT | 销售业务成本 | number(23,8) | Y |  |
| 6 | PRICE_QTY | 计价数量_应收 | number(16,6) | Y |  |
| 7 | SALES_COST_AMT | 销售成本_应收 | number(23,8) | Y |  |
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
| 40 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ID_ROid |  | GUID | Y |  |
| 42 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 44 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 45 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 46 | IM_FICATEGORY_ID | 存货会计分类 | GUID | Y |  |
| 47 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 48 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 49 | CALCULATE_FLAG | 金额转换 | number | Y |  |

### AR_SALES_COST_ELEMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AR_SALES_COST_ELEMENT_ID | 主键 | GUID | Y | Y |
| 4 | SALSE_TRANSDOC_LINE_ID | 销售业务单据行 | GUID | Y |  |
| 5 | AR_SALES_COST_DETAIL_ID | 应收销售成本明细档主键 | GUID | Y |  |
| 6 | SALES_COST_AMT | 销售成本_应收 | number(23,8) | Y |  |
| 7 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
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

### AR_SALES_COST_STATS (应收销售成本统计档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AR_SALES_COST_STATS_ID | 主键 | GUID | Y | Y |
| 4 | SALSE_TRANSDOC_LINE_ID | 销货业务单据行 | GUID | Y |  |
| 5 | ACCUM_PRICE_QTY | 累计计价数量_应收 | number(16,6) | Y |  |
| 6 | ACCUM_SALES_COST_AMT | 累计销售成本_应收 | number(23,8) | Y |  |
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

### AR_TRANSFER_DOC (维护应收转销单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AR_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 12 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 13 | TRANSFER_AMT_TC | 转销原币合计 | number(23,8) | Y |  |
| 14 | TRANSFER_AMT_FC | 转销合计(本币) | number(23,8) | Y |  |
| 15 | RESPONSIBILITY_INDICATOR | 责任区域 | number(0/1) | Y |  |
| 16 | PAYMENT_TERM_INDICATOR | 变更付款条件 | number(0/1) | Y |  |
| 17 | PAYMENT_DATE | 付款日 | date | Y |  |
| 18 | CASHING_DATE | 兑现日 | date | Y |  |
| 19 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 20 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 21 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 22 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 23 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 24 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 25 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | SETTLEMENT_OBJECT_TYPE | 应收结算对象类型 | number | Y |  |
| 28 | CURRENCY_ID | 货币 | GUID | Y |  |
| 29 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 30 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 31 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 32 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 33 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 34 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 35 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 36 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 37 | PrintCount | 打印次数 | number | Y |  |
| 38 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 39 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 40 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 41 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 42 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 43 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 44 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 45 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 46 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 47 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 48 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 49 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 50 | UDF041 | 自定义字段12 | date | Y |  |
| 51 | UDF042 | 自定义字段13 | date | Y |  |
| 52 | UDF051 | 自定义字段14 | GUID | Y |  |
| 53 | UDF052 | 自定义字段15 | GUID | Y |  |
| 54 | UDF053 | 自定义字段16 | GUID | Y |  |
| 55 | UDF054 | 自定义字段17 | GUID | Y |  |
| 56 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 57 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 58 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 59 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |
| 74 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 75 | SOURCE_ID_ROid |  | GUID | Y |  |
| 76 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 77 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 78 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 79 | SOURCE2_ID_ROid |  | GUID | Y |  |

### AR_TRANSFER_DOC_D (维护应收转销单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AR_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 4 | BALANCE_AMT_TC | 应收/预收余额(原币) | number(23,8) | Y |  |
| 5 | BALANCE_AMT_FC | 应收/预收余额(本币) | number(23,8) | Y |  |
| 6 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 7 | TRANSFERED_TOTAL_AMT_TC | 转销合计(原币) | number(23,8) | Y |  |
| 8 | TRANSFERED_TOTAL_AMT_FC | 转销合计(本币) | number(23,8) | Y |  |
| 9 | TRANSFERED_AMT_FC | 转销(本币) | number(23,8) | Y |  |
| 10 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ORIG_RESP_EMPLOYEE_ID | 原责任人员 | GUID | Y |  |
| 13 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 14 | ORIG_RESP_ADMIN_UNIT_ID | 原责任部门 | GUID | Y |  |
| 15 | PROJECT_ID | 项目 | GUID | Y |  |
| 16 | PROJECT_SOURCE | 项目来源 | number | Y |  |
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
| 42 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 44 | AR_TRANSFER_DOC_ID |  | GUID | Y |  |