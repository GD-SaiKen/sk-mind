---
module: "AP"
name_zh: "应付账款"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 15
columns: 692
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# AP (应付账款)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 15 | Columns: 692

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]
- [[CLOSE (关账检查)|CLOSE (关账检查)]]

---

## Tables


- **AP_AGING_TEMPLATE (应付账龄分析模板信息)**
- **AP_AGING_TEMPLATE_D (应付账龄分析模板单身)**
- **AP_B005 (AP_B005)**
- **AP_B006 (AP_B006)**
- **AP_CHECK_SET**
- **AP_EXCHANGE_DOC (应付调汇单)**
- **AP_EXCHANGE_DOC_CURR (应付调汇单即时余额)**
- **AP_EXCHANGE_DOC_D (应付调汇单单身)**
- **AP_REFUND_DOC (退款单)**
- **AP_REFUND_DOC_CA (退款单转账款)**
- **AP_REFUND_DOC_D (退款单单身)**
- **AP_REFUND_DOC_VERIFIED (应付退款单应付核销)**
- **AP_TAXINV_RELATION (应付税务发票关联关系)**
- **AP_TRANSFER_DOC**
- **AP_TRANSFER_DOC_D**


---


---


> Tables: 15

### AP_AGING_TEMPLATE (应付账龄分析模板信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AP_AGING_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | TEMPLATE_CODE |  | string(12) | Y |  |
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

### AP_AGING_TEMPLATE_D (应付账龄分析模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_AGING_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 3 | AGE_START | 账龄起 | number | Y |  |
| 4 | AGE_END | 账龄止 | number | Y |  |
| 5 | AGE_DESCRIPTION |  | string(510) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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
| 35 | AP_AGING_TEMPLATE_ID |  | GUID | Y |  |

### AP_B005 (AP_B005)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AP_B005_ID | 主键 | GUID | Y | Y |
| 2 | AP_B005_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### AP_B006 (AP_B006)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AP_B006_ID | 主键 | GUID | Y | Y |
| 2 | AP_B006_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### AP_CHECK_SET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AP_CHECK_SET_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | AP_FLAG | 应付对账标识 | number(0/1) | Y |  |
| 6 | AP_ACCOUNT_TYPE | 应付对账科目类型 | number | Y |  |
| 7 | AP_ESTI_FLAG | 应付暂估对账标识 | number(0/1) | Y |  |
| 8 | AP_ESTI_ACCOUNT_TYPE | 应付暂估对账科目类型 | number | Y |  |
| 9 | PREPAYMENT_FLAG | 预付对账标识 | number(0/1) | Y |  |
| 10 | PREPAYMENT_ACCOUNT_TYPE | 预付对账科目类型 | number | Y |  |
| 11 | OTHER_AP_FLAG | 其他应付对账标识 | number(0/1) | Y |  |
| 12 | OTHER_AP_ACCOUNT_TYPE | 其他应付对账科目类型 | number | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 50 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 52 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE4_ID_ROid |  | GUID | Y |  |

### AP_EXCHANGE_DOC (应付调汇单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AP_EXCHANGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 12 | EXCHANGE_LOSS_AMT | 期间汇兑损失合计 | number(23,8) | Y |  |
| 13 | CURR_EXCHANGE_LOSS_AMT | 即时汇兑损失合计 | number(23,8) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
| 16 | DATA_SOURCE | 数据来源 | number | Y |  |
| 17 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 18 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 19 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 20 | GLMB_JE_ID | 主键 | GUID | Y |  |
| 21 | PrintCount | 打印次数 | number | Y |  |
| 22 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 23 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 24 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 25 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Attachments | 附件 | string | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |

### AP_EXCHANGE_DOC_CURR (应付调汇单即时余额)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_EXCHANGE_DOC_CURR_ID | 主键 | GUID | Y | Y |
| 3 | PAYABLES_TYPE | 应付款类型 | number | Y |  |
| 4 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 5 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 6 | BALANCE_AMT_TC | 应付/预付余额(原币) | number(23,8) | Y |  |
| 7 | BALANCE_AMT_FC | 应付/预付余额(本币) | number(23,8) | Y |  |
| 8 | REVALUATION_BALANCE_AMT | 调整后余额 | number(23,8) | Y |  |
| 9 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 10 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 11 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
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
| 43 | AP_EXCHANGE_DOC_ID |  | GUID | Y |  |

### AP_EXCHANGE_DOC_D (应付调汇单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_EXCHANGE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | PAYABLES_TYPE | 应付款类型 | number | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | BALANCE_AMT_TC |  | number(23,8) | Y |  |
| 6 | BALANCE_AMT_FC | 应付/预付余额(功能币) | number(23,8) | Y |  |
| 7 | REVALUATION_BALANCE_AMT | 调整后余额 | number(23,8) | Y |  |
| 8 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
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
| 43 | AP_EXCHANGE_DOC_ID |  | GUID | Y |  |

### AP_REFUND_DOC (退款单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | AP_REFUND_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 12 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 13 | MULTI_CURRENCY_INDICATOR | 异货币核销标识 | number(0/1) | Y |  |
| 14 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 15 | COLLECTION_AMT_TC | 实收金额合计(原币) | number(23,8) | Y |  |
| 16 | COLLECTION_AMT_FC | 实收金额合计(本币) | number(23,8) | Y |  |
| 17 | SETTLE_EXPENSE_AMT_TC | 结算费用合计(原币) | number(23,8) | Y |  |
| 18 | SETTLE_EXPENSE_AMT_FC | 结算费用合计(本币) | number(23,8) | Y |  |
| 19 | ADDITIONAL_EXPENSE_AMT_TC | 附加结算费用合计(原币) | number(23,8) | Y |  |
| 20 | ADDITIONAL_EXPENSE_AMT_FC | 附加结算费用合计(本币) | number(23,8) | Y |  |
| 21 | AP_VERIFICATION_AMT_TC | 应付核销金额合计(原币) | number(23,8) | Y |  |
| 22 | AP_VERIFICATION_AMT_FC | 应付核销金额合计(本币) | number(23,8) | Y |  |
| 23 | CASH_DISCOUNT_AMT_TC | 现金折扣合计(原币) | number(23,8) | Y |  |
| 24 | CASH_DISCOUNT_AMT_FC | 现金折扣合计(本币) | number(23,8) | Y |  |
| 25 | PREPAYMENT_VERIFIED_AMT_TC | 预付核销金额合计(原币) | number(23,8) | Y |  |
| 26 | PREPAYMENT_VERIFIED_AMT_FC | 预付核销金额合计(本币) | number(23,8) | Y |  |
| 27 | AP_EXCHANGE_LOSS_AMT | 应付核销-汇兑损失合计 | number(23,8) | Y |  |
| 28 | PREPAYMENT_EXG_LOSS_AMT | 预付核销-汇兑损失合计 | number(23,8) | Y |  |
| 29 | LOSS_AMT_TC | 财务损失合计(原币) | number(23,8) | Y |  |
| 30 | LOSS_AMT_FC | 财务损失合计(本币) | number(23,8) | Y |  |
| 31 | GAIN_AMT_TC | 利得(原币) | number(23,8) | Y |  |
| 32 | GAIN_AMT_FC | 利得(本币) | number(23,8) | Y |  |
| 33 | GAIN_REMARK | 利得备注 | string(510) | Y |  |
| 34 | REMARK | 备注 | string(510) | Y |  |
| 35 | EMPLOYEE_ID | 收款业务员 | GUID | Y |  |
| 36 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 37 | CURRENCY_ID | 货币 | GUID | Y |  |
| 38 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 39 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 40 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 41 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 42 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 43 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 44 | NMC_INDICATOR | 受控出纳管理系统标识 | number(0/1) | Y |  |
| 45 | PAYABLES_AMT_TC | 转应付款合计(原币) | number(23,8) | Y |  |
| 46 | PAYABLES_AMT_FC | 转应付款合计(本币) | number(23,8) | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
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
| 70 | PrintCount | 打印次数 | number | Y |  |
| 71 | CreateDate | 创建日期 | date | Y |  |
| 72 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 73 | ModifiedDate | 修改日期 | date | Y |  |
| 74 | CreateBy | 创建者 | GUID | Y |  |
| 75 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 76 | ModifiedBy | 修改者 | GUID | Y |  |
| 77 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 78 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 79 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 80 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 81 | Attachments | 附件 | string | Y |  |
| 82 | Owner_Org_RTK |  | string(400) | Y |  |
| 83 | Owner_Org_ROid |  | GUID | Y |  |
| 84 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 85 | SOURCE_ID_ROid |  | GUID | Y |  |
| 86 | CURRENCY_EXG_LOSS_AMT | 实收货币汇兑损失 | number(23,8) | Y |  |

### AP_REFUND_DOC_CA (退款单转账款)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_REFUND_DOC_CA_ID |  | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | OTHER_ARAP_ITEM_ID | 其他应付项目 | GUID | Y |  |
| 5 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 6 | AMT_TC | 账款金额(原币) | number(23,8) | Y |  |
| 7 | AMT_FC | 账款金额(本币) | number(23,8) | Y |  |
| 8 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 9 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 10 | PAYMENT_DATE | 付款日 | date | Y |  |
| 11 | CASHING_DATE | 兑现日 | date | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 14 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
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
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | AP_REFUND_DOC_ID |  | GUID | Y |  |

### AP_REFUND_DOC_D (退款单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_REFUND_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | SETTLEMENT_NO |  | string(60) | Y |  |
| 5 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 6 | DUE_DATE | 到期日 | date | Y |  |
| 7 | AMT_TC | 实收/结算费用金额(原币) | number(23,8) | Y |  |
| 8 | AMT_FC | 实收/结算费用金额(本币) | number(23,8) | Y |  |
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
| 47 | AP_REFUND_DOC_ID |  | GUID | Y |  |

### AP_REFUND_DOC_VERIFIED (应付退款单应付核销)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_REFUND_DOC_VERIFIED_ID | 主键 | GUID | Y | Y |
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
| 15 | LOSS_AMT_TC | 财务损失(原币) | number(23,8) | Y |  |
| 16 | LOSS_AMT_FC | 财务损失(本币) | number(23,8) | Y |  |
| 17 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 20 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 21 | RESPONSIBILITY_ADMIN_UNIT_ID | 主键 | GUID | Y |  |
| 22 | CURRENCY_ID | 货币 | GUID | Y |  |
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
| 50 | AP_REFUND_DOC_ID |  | GUID | Y |  |

### AP_TAXINV_RELATION (应付税务发票关联关系)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AP_TAXINV_RELATION_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | PrintCount | 打印次数 | number | Y |  |
| 6 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 7 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 8 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 9 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |
| 44 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 46 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE3_ID_ROid |  | GUID | Y |  |

### AP_TRANSFER_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AP_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | PAYABLES_TYPE | 应付款类型 | number | Y |  |
| 12 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 13 | RESPONSIBILITY_INDICATOR | 变更责任区域 | number(0/1) | Y |  |
| 14 | PAYMENT_TERM_INDICATOR | 变更付款条件 | number(0/1) | Y |  |
| 15 | PAYMENT_DATE | 付款日 | date | Y |  |
| 16 | CASHING_DATE | 兑现日 | date | Y |  |
| 17 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 18 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 19 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 20 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 21 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 22 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 23 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 24 | TRANSFER_AMT_TC | 转销合计(原币) | number(23,8) | Y |  |
| 25 | TRANSFER_AMT_FC | 转销合计(本币) | number(23,8) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 28 | CURRENCY_ID | 货币 | GUID | Y |  |
| 29 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 30 | RESPONSIBILITY_ADMIN_UNIT_ID | 主键 | GUID | Y |  |
| 31 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
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
| 76 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 77 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 78 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 79 | SOURCE3_ID_ROid |  | GUID | Y |  |

### AP_TRANSFER_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | AP_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 4 | TRANSFERED_TOTAL_AMT_TC | 转销合计(原币) | number(23,8) | Y |  |
| 5 | TRANSFERED_TOTAL_AMT_FC | 转销合计(本币) | number(23,8) | Y |  |
| 6 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | BALANCE_AMT_TC | 应付/预付余额(原币) | number(23,8) | Y |  |
| 9 | BALANCE_AMT_FC | 应付/预付余额(本币) | number(23,8) | Y |  |
| 10 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 11 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 12 | ORIG_RESP_EMPLOYEE_ID | 原责任人员 | GUID | Y |  |
| 13 | ORIG_RESP_ADMIN_UNIT_ID | 原责任部门 | GUID | Y |  |
| 14 | TRANSFERED_AMT_FC | 转销合计(本币) | number(23,8) | Y |  |
| 15 | PROJECT_SOURCE | 项目来源 | number | Y |  |
| 16 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 45 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 47 | AP_TRANSFER_DOC_ID |  | GUID | Y |  |