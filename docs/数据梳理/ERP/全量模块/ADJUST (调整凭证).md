---
module: "ADJUST"
name_zh: "调整凭证"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 177
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# ADJUST (调整凭证)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 177

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]
- [[CLOSE (关账检查)|CLOSE (关账检查)]]

---

## Tables


- **ADJUST_TEMPLATE (调整分录模板)**
- **ADJUST_TEMPLATE_D (调整分录模板单身)**
- **ADJUST_VOUCHER**
- **ADJUST_VOUCHER_D**


---


---


> Tables: 4

### ADJUST_TEMPLATE (调整分录模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ADJUST_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | ADJUST_TEMPLATE_CODE | 调整模板编号 | string(12) | Y |  |
| 5 | ADJUST_TEMPLATE_NAME | 调整模板名称 | string(40) | Y |  |
| 6 | ADJUST_TYPE | 调整类型 | number | Y |  |
| 7 | ZERO_FLAG | 生成金额为零的分录行 | number(0/1) | Y |  |
| 8 | CFS_ITEM_DATASET_ID | 报表项目表 | GUID | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### ADJUST_TEMPLATE_D (调整分录模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ADJUST_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 3 | DEF_ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 4 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 5 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 6 | GROUP_NO | 组号 | number | Y |  |
| 7 | DATA_TYPE | 取数方式 | number | Y |  |
| 8 | ADJUST_AMT | 调整金额 | number(23,8) | Y |  |
| 9 | ADJUST_FORMULA | 公式 | string | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
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
| 36 | ADJUST_TEMPLATE_ID |  | GUID | Y |  |

### ADJUST_VOUCHER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ADJUST_VOUCHER_ID | 主键 | GUID | Y | Y |
| 7 | ADJUST_TYPE | 调整类型 | number | Y |  |
| 8 | DATA_TYPE | 数据类型 | number | Y |  |
| 9 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 10 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 11 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 12 | DATA_PERIOD_SEQNO | 数据明细期间序号 | number | Y |  |
| 13 | FUN_CURRENCY_ID | 个别报表货币 | GUID | Y |  |
| 14 | CFS_CURRENCY_ID | 合并货币 | GUID | Y |  |
| 15 | FATHER_CFS_SCHEME_D_ID | 上层合并范围 | GUID | Y |  |
| 16 | ADJUST_ROLE | 调整角色 | number | Y |  |
| 17 | DR_AMT | 借方合计 | number(23,8) | Y |  |
| 18 | CR_AMT | 贷方合计 | number(23,8) | Y |  |
| 19 | PL_CARRY_OVER_FLAG | 损益结转标识 | number(0/1) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
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
| 39 | PrintCount | 打印次数 | number | Y |  |
| 40 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 41 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 42 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 43 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |
| 58 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE_ID_ROid |  | GUID | Y |  |
| 60 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE2_ID_ROid |  | GUID | Y |  |

### ADJUST_VOUCHER_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ADJUST_VOUCHER_D_ID |  | GUID | Y | Y |
| 3 | DEF_ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 4 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 5 | DR_AMT | 借方金额 | number(23,8) | Y |  |
| 6 | CR_AMT | 贷方金额 | number(23,8) | Y |  |
| 7 | CFS_DATA_FLAG | 合并数影响标识 | number(0/1) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | ADJUST_VOUCHER_ID |  | GUID | Y |  |