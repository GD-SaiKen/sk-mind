---
module: "CFS"
name_zh: "财务结转"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 23
columns: 999
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# CFS (财务结转)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 23 | Columns: 999

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CLOSE (关账检查)|CLOSE (关账检查)]]

---

## Tables


- **CFS_CARRYOVER_SETUP (损益结转设置)**
- **CFS_CARRYOVER_SETUP_D (损益结转设置单身)**
- **CFS_CYCLICALITY (合并周期)**
- **CFS_CYCLICALITY_D (合并周期单身)**
- **CFS_DATA (合并报表数据)**
- **CFS_DATA_DETAIL (合并报表数据明细)**
- **CFS_ITEM (报表项目)**
- **CFS_ITEM_DATASET (报表项目表)**
- **CFS_ITEM_FORMULA**
- **CFS_ITEM_FORMULA_D**
- **CFS_ITEM_INITIAL**
- **CFS_ITEM_INITIAL_D**
- **CFS_MEMO_DATA (合并报表备查簿)**
- **CFS_MEMO_DATA_DETAIL (合并报表备查簿明细)**
- **CFS_MEMO_FORMULA**
- **CFS_MEMO_FORMULA_D**
- **CFS_OBY_ADJUST (年初合并数调整)**
- **CFS_SCHEME**
- **CFS_SCHEME_D**
- **CFS_SCHEME_SD**
- **CFS_STATUS (合并报表状态表)**
- **CFS_WH_TEMPLATE (合并工作底稿格式设定)**
- **CFS_WH_TEMPLATE_D (合并工作底稿格式设定单身)**


---


---


> Tables: 23

### CFS_CARRYOVER_SETUP (损益结转设置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_CARRYOVER_SETUP_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | DEF_ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 6 | REMARK | 备注 | string(400) | Y |  |
| 7 | DEF_ADJ_VOUCHER_TYPE_ID | 调整凭证类型 | GUID | Y |  |
| 8 | DEF_CYP_CFS_ITEM_ID | 默认本年利润项目 | GUID | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
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
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_CARRYOVER_SETUP_D (损益结转设置单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_CARRYOVER_SETUP_D_ID | 主键 | GUID | Y | Y |
| 3 | PROFIT_LOSS_CFS_ITEM_ID | 损益项目 | GUID | Y |  |
| 4 | CYP_CFS_ITEM_ID | 本年利润项目 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | CFS_CARRYOVER_SETUP_ID |  | GUID | Y |  |

### CFS_CYCLICALITY (合并周期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_CYCLICALITY_ID | 主键 | GUID | Y | Y |
| 4 | CFS_CYCLICALITY_CODE | 合并周期编号 | string(12) | Y |  |
| 5 | CFS_CYCLICALITY_NAME | 合并周期名称 | string(40) | Y |  |
| 6 | ACCPERIOD_DATASET_ID | 会计期间表 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | Attachments | 附件 | string | Y |  |
| 9 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### CFS_CYCLICALITY_D (合并周期单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_CYCLICALITY_D_ID | 主键 | GUID | Y | Y |
| 3 | CFS_PERIOD_CODE | 合并期号 | string(20) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | START_PERIOD_CODE | 开始期间期号 | string(20) | Y |  |
| 6 | CUTOFF_PERIOD_CODE | 结束期间期号 | string(20) | Y |  |
| 7 | START_PERIOD_SEQNO | 开始期间序号 | number | Y |  |
| 8 | CUTOFF_PERIOD_SEQNO | 结束期间序号 | number | Y |  |
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
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | CFS_CYCLICALITY_ID |  | GUID | Y |  |

### CFS_DATA (合并报表数据)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_DATA_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | CFS_SCHEME_D_ID | 合并范围 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 8 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 9 | DATA_TYPE | 报表项目数据类型 | number | Y |  |
| 10 | YEAR_ACCUM_FLAG | 年度累计数合并 | number(0/1) | Y |  |
| 11 | FUN_CURRENCY_ID | 个别报表货币 | GUID | Y |  |
| 12 | HISTORY_DR_AMT | 个调前_借方 | number(23,8) | Y |  |
| 13 | HISTORY_CR_AMT | 个调前_贷方 | number(23,8) | Y |  |
| 14 | HISTORY_NET_AMT | 个调前_净额 | number(23,8) | Y |  |
| 15 | ADJUST_DR_AMT | 个调数_借方 | number(23,8) | Y |  |
| 16 | ADJUST_CR_AMT | 个调数_贷方 | number(23,8) | Y |  |
| 17 | ADJUST_NET_AMT | 个调数_净额 | number(23,8) | Y |  |
| 18 | CURR_DR_AMT | 个调后_借方 | number(23,8) | Y |  |
| 19 | CURR_CR_AMT | 个调后_贷方 | number(23,8) | Y |  |
| 20 | CURR_NET_AMT | 个调后_净额 | number(23,8) | Y |  |
| 21 | CFS_CURRENCY_ID | 合并货币 | GUID | Y |  |
| 22 | HISTORY_TRANS_DR_AMT | 个调前_折算_借方 | number(23,8) | Y |  |
| 23 | HISTORY_TRANS_CR_AMT | 个调前_折算_贷方 | number(23,8) | Y |  |
| 24 | HISTORY_TRANS_NET_AMT | 个调前_折算_净额 | number(23,8) | Y |  |
| 25 | ADJUST_TRANS_DR_AMT | 个调数_折算_借方 | number(23,8) | Y |  |
| 26 | ADJUST_TRANS_CR_AMT | 个调数_折算_贷方 | number(23,8) | Y |  |
| 27 | ADJUST_TRANS_NET_AMT | 个调数_折算_净额 | number(23,8) | Y |  |
| 28 | CURR_TRANS_DR_AMT | 个调后_折算_借方 | number(23,8) | Y |  |
| 29 | CURR_TRANS_CR_AMT | 个调后_折算_贷方 | number(23,8) | Y |  |
| 30 | CURR_TRANS_NET_AMT | 个调后_折算_净额 | number(23,8) | Y |  |
| 31 | GROUP_ADJUST_DR_AMT | 集团调整数_借方 | number(23,8) | Y |  |
| 32 | GROUP_ADJUST_CR_AMT | 集团调整数_贷方 | number(23,8) | Y |  |
| 33 | ELIMINATE_DR_AMT | 抵销数_借方 | number(23,8) | Y |  |
| 34 | ELIMINATE_CR_AMT | 抵销数_贷方 | number(23,8) | Y |  |
| 35 | CONSOLIDATE_DR_AMT | 合并数_借方 | number(23,8) | Y |  |
| 36 | CONSOLIDATE_CR_AMT | 合并数_贷方 | number(23,8) | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 45 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 46 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 47 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 48 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 49 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 50 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 51 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 52 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 53 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 54 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 55 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 56 | UDF041 | 自定义字段12 | date | Y |  |
| 57 | UDF042 | 自定义字段13 | date | Y |  |
| 58 | UDF051 | 自定义字段14 | GUID | Y |  |
| 59 | UDF052 | 自定义字段15 | GUID | Y |  |
| 60 | UDF053 | 自定义字段16 | GUID | Y |  |
| 61 | UDF054 | 自定义字段17 | GUID | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | Version | 版本号，不要随意更改 | binary | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |
| 66 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 67 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_DATA_DETAIL (合并报表数据明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_DATA_DETAIL_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | CFS_SCHEME_D_ID | 合并范围 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 8 | DATA_PERIOD_SEQNO | 数据明细期间序号 | number | Y |  |
| 9 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 10 | FUN_CURRENCY_ID | 个别报表货币 | GUID | Y |  |
| 11 | HISTORY_DR_AMT | 个调前_借方 | number(23,8) | Y |  |
| 12 | HISTORY_CR_AMT | 个调前_贷方 | number(23,8) | Y |  |
| 13 | HISTORY_NET_AMT | 个调前_净额 | number(23,8) | Y |  |
| 14 | ADJUST_DR_AMT | 个调数_借方 | number(23,8) | Y |  |
| 15 | ADJUST_CR_AMT | 个调数_贷方 | number(23,8) | Y |  |
| 16 | ADJUST_NET_AMT | 个调数_净额 | number(23,8) | Y |  |
| 17 | CURR_DR_AMT | 个调后_借方 | number(23,8) | Y |  |
| 18 | CURR_CR_AMT | 个调后_贷方 | number(23,8) | Y |  |
| 19 | CURR_NET_AMT | 个调后_净额 | number(23,8) | Y |  |
| 20 | CFS_CURRENCY_ID | 合并货币 | GUID | Y |  |
| 21 | EXCHANGE_RATE | 折算汇率 | number(18,9) | Y |  |
| 22 | HISTORY_TRANS_DR_AMT | 个调前_折算_借方 | number(23,8) | Y |  |
| 23 | HISTORY_TRANS_CR_AMT | 个调前_折算_贷方 | number(23,8) | Y |  |
| 24 | HISTORY_TRANS_NET_AMT | 个调前_折算_净额 | number(23,8) | Y |  |
| 25 | ADJUST_TRANS_DR_AMT | 个调数_折算_借方 | number(23,8) | Y |  |
| 26 | ADJUST_TRANS_CR_AMT | 个调数_折算_贷方 | number(23,8) | Y |  |
| 27 | ADJUST_TRANS_NET_AMT | 个调数_折算_净额 | number(23,8) | Y |  |
| 28 | CURR_TRANS_DR_AMT | 个调后_折算_借方 | number(23,8) | Y |  |
| 29 | CURR_TRANS_CR_AMT | 个调后_折算_贷方 | number(23,8) | Y |  |
| 30 | CURR_TRANS_NET_AMT | 个调后_折算_净额 | number(23,8) | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Attachments | 附件 | string | Y |  |
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
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |
| 60 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_ITEM (报表项目)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | CFS_ITEM_CODE | 报表项目编号 | string(60) | Y |  |
| 5 | CFS_ITEM_NAME | 报表项目名称 | string(80) | Y |  |
| 6 | CFS_ITEM_ALIAS | 报表项目别名 | string(840) | Y |  |
| 7 | CFS_ITEM_DATASET_ID | 报表项目表 | GUID | Y |  |
| 8 | STMT_ELEMENT | 报表要素 | number | Y |  |
| 9 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 10 | DATA_TYPE | 数据类型 | number | Y |  |
| 11 | FATHER_CFS_ITEM_ID | 上级报表项目 | GUID | Y |  |
| 12 | SYS_CODE | 内码 | string(80) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | NATURE | 性质 | number | Y |  |
| 15 | SYS_SORT_CODE | 排序内码 | string(80) | Y |  |
| 16 | CFS_ITEM_LEVEL | 项目层级 | number | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |

### CFS_ITEM_DATASET (报表项目表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_ITEM_DATASET_ID | 主键 | GUID | Y | Y |
| 4 | CFS_ITEM_DATASET_CODE | 报表项目表编号 | string(12) | Y |  |
| 5 | CFS_ITEM_DATASET_NAME | 报表项目表名称 | string(40) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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

### CFS_ITEM_FORMULA

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_ITEM_FORMULA_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | FATHER_CFS_SCHEME_D_ID | 上层合并范围 | GUID | Y |  |
| 6 | YEAR_ACCUM_FLAG | 年度累计数合并 | number(0/1) | Y |  |
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
| 32 | Attachments | 附件 | string | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |
| 40 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_ITEM_FORMULA_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_ITEM_FORMULA_D_ID | 主键 | GUID | Y | Y |
| 3 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 4 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 5 | DATA_TYPE | 数据类型 | number | Y |  |
| 6 | YEAR_ACCUM_FLAG | 年度累计数合并 | number(0/1) | Y |  |
| 7 | DATA_FORMULA | 取数公式 | string | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | CFS_ITEM_FORMULA_ID |  | GUID | Y |  |

### CFS_ITEM_INITIAL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_ITEM_INITIAL_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | CFS_CYCLICALITY_ID | 合并周期 | GUID | Y |  |
| 6 | CURRENCY_ID | 货币 | GUID | Y |  |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 28 | Attachments | 附件 | string | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_ITEM_INITIAL_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_ITEM_INITIAL_D_ID |  | GUID | Y | Y |
| 3 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 4 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 5 | YEAR_OPENING_AMT | 年初数 | number(23,8) | Y |  |
| 6 | P01_DR_AMT | 期间1_借方金额 | number(23,8) | Y |  |
| 7 | P01_CR_AMT | 期间1_贷方金额 | number(23,8) | Y |  |
| 8 | P02_DR_AMT | 期间2_借方金额 | number(23,8) | Y |  |
| 9 | P02_CR_AMT | 期间2_贷方金额 | number(23,8) | Y |  |
| 10 | P03_DR_AMT | 期间3_借方金额 | number(23,8) | Y |  |
| 11 | P03_CR_AMT | 期间3_贷方金额 | number(23,8) | Y |  |
| 12 | P04_DR_AMT | 期间4_借方金额 | number(23,8) | Y |  |
| 13 | P04_CR_AMT | 期间4_贷方金额 | number(23,8) | Y |  |
| 14 | P05_DR_AMT | 期间5_借方金额 | number(23,8) | Y |  |
| 15 | P05_CR_AMT | 期间5_贷方金额 | number(23,8) | Y |  |
| 16 | P06_DR_AMT | 期间6_借方金额 | number(23,8) | Y |  |
| 17 | P06_CR_AMT | 期间6_贷方金额 | number(23,8) | Y |  |
| 18 | P07_DR_AMT | 期间7_借方金额 | number(23,8) | Y |  |
| 19 | P07_CR_AMT | 期间7_贷方金额 | number(23,8) | Y |  |
| 20 | P08_DR_AMT | 期间8_借方金额 | number(23,8) | Y |  |
| 21 | P08_CR_AMT | 期间8_贷方金额 | number(23,8) | Y |  |
| 22 | P09_DR_AMT | 期间9_借方金额 | number(23,8) | Y |  |
| 23 | P09_CR_AMT | 期间9_贷方金额 | number(23,8) | Y |  |
| 24 | P10_DR_AMT | 期间10_借方金额 | number(23,8) | Y |  |
| 25 | P10_CR_AMT | 期间10_贷方金额 | number(23,8) | Y |  |
| 26 | P11_DR_AMT | 期间11_借方金额 | number(23,8) | Y |  |
| 27 | P11_CR_AMT | 期间11_贷方金额 | number(23,8) | Y |  |
| 28 | P12_DR_AMT | 期间12_借方金额 | number(23,8) | Y |  |
| 29 | P12_CR_AMT | 期间12_贷方金额 | number(23,8) | Y |  |
| 30 | P13_DR_AMT | 期间13_借方金额 | number(23,8) | Y |  |
| 31 | P13_CR_AMT | 期间13_贷方金额 | number(23,8) | Y |  |
| 32 | P14_DR_AMT | 期间14_借方金额 | number(23,8) | Y |  |
| 33 | P14_CR_AMT | 期间14_贷方金额 | number(23,8) | Y |  |
| 34 | P15_DR_AMT | 期间15_借方金额 | number(23,8) | Y |  |
| 35 | P15_CR_AMT | 期间15_贷方金额 | number(23,8) | Y |  |
| 36 | P16_DR_AMT | 期间16_借方金额 | number(23,8) | Y |  |
| 37 | P16_CR_AMT | 期间16_贷方金额 | number(23,8) | Y |  |
| 38 | REMARK | 备注 | string(510) | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | CFS_ITEM_INITIAL_ID |  | GUID | Y |  |

### CFS_MEMO_DATA (合并报表备查簿)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_MEMO_DATA_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | COMPANY1_ID | 本方公司 | GUID | Y |  |
| 6 | CFS_SCHEME_D1_ID | 本方合并范围 | GUID | Y |  |
| 7 | COMPANY2_ID | 对方公司 | GUID | Y |  |
| 8 | CFS_SCHEME_D2_ID | 对方合并范围 | GUID | Y |  |
| 9 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 10 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 11 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 12 | DATA_TYPE | 数据类型 | number | Y |  |
| 13 | YEAR_ACCUM_FLAG | 年度累计数合并 | number(0/1) | Y |  |
| 14 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 15 | FUN_CURRENCY_ID | 个别报表货币 | GUID | Y |  |
| 16 | HISTORY_AMT_FC | 调整前金额 | number(23,8) | Y |  |
| 17 | ADJUST_AMT_FC | 调整金额 | number(23,8) | Y |  |
| 18 | CURR_AMT_FC | 调整后金额 | number(23,8) | Y |  |
| 19 | CFS_CURRENCY_ID | 合并货币 | GUID | Y |  |
| 20 | HISTORY_TRANS_AMT | 调整前金额_折算 | number(23,8) | Y |  |
| 21 | ADJUST_TRANS_AMT | 调整金额_折算 | number(23,8) | Y |  |
| 22 | CURR_TRANS_AMT | 调整后金额_折算 | number(23,8) | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### CFS_MEMO_DATA_DETAIL (合并报表备查簿明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_MEMO_DATA_DETAIL_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | COMPANY1_ID | 本方公司 | GUID | Y |  |
| 6 | CFS_SCHEME_D1_ID | 本方合并范围 | GUID | Y |  |
| 7 | COMPANY2_ID | 对方公司 | GUID | Y |  |
| 8 | CFS_SCHEME_D2_ID | 对方合并范围 | GUID | Y |  |
| 9 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 10 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 11 | GL_PERIOD_SEQNO | 总账期间序号 | number | Y |  |
| 12 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 13 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 14 | TRANS_CURRENCY_ID | 交易货币 | GUID | Y |  |
| 15 | FUN_CURRENCY_ID | 个别报表货币 | GUID | Y |  |
| 16 | HISTORY_AMT_TC | 调整前金额-原币 | number(23,8) | Y |  |
| 17 | HISTORY_AMT_FC | 调整前金额-报告币 | number(23,8) | Y |  |
| 18 | ADJUST_AMT_TC | 调整金额-原币 | number(23,8) | Y |  |
| 19 | ADJUST_AMT_FC | 调整金额-报告币 | number(23,8) | Y |  |
| 20 | CURR_AMT_TC | 调整后金额-原币 | number(23,8) | Y |  |
| 21 | CURR_AMT_FC | 调整后金额-报告币 | number(23,8) | Y |  |
| 22 | CFS_CURRENCY_ID | 合并货币 | GUID | Y |  |
| 23 | EXCHANGE_RATE | 折算汇率 | number(18,9) | Y |  |
| 24 | HISTORY_TRANS_AMT | 调整前金额_折算 | number(23,8) | Y |  |
| 25 | ADJUST_TRANS_AMT | 调整金额_折算 | number(23,8) | Y |  |
| 26 | CURR_TRANS_AMT | 调整后金额_折算 | number(23,8) | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
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
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | Owner_Org_RTK |  | string(400) | Y |  |
| 55 | Owner_Org_ROid |  | GUID | Y |  |

### CFS_MEMO_FORMULA

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_MEMO_FORMULA_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | COMPANY_ID | 合并组织 | GUID | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
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
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### CFS_MEMO_FORMULA_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 3 | CFS_DIRECTION | 合并方向 | number | Y |  |
| 4 | DATA_TYPE | 数据类型 | number | Y |  |
| 5 | YEAR_ACCUM_FLAG | 年度累计数合并 | number(0/1) | Y |  |
| 6 | DATA_FORMULA | 取数公式 | string | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CFS_MEMO_FORMULA_D_ID | 主键 | GUID | Y | Y |
| 9 | MULTI_FORMAL_FLAG | 多公式标识 | number(0/1) | Y |  |
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
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | CFS_MEMO_FORMULA_ID |  | GUID | Y |  |

### CFS_OBY_ADJUST (年初合并数调整)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_OBY_ADJUST_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | CFS_SCHEME_D_ID | 合并范围 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 8 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 9 | CFS_CURRENCY_ID | 合并货币 | GUID | Y |  |
| 10 | GROUP_ADJUST_DR_AMT | 集团调整数_借方 | number(23,8) | Y |  |
| 11 | GROUP_ADJUST_CR_AMT | 集团调整数_贷方 | number(23,8) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
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
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_SCHEME

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_SCHEME_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_CODE | 编号 | string(12) | Y |  |
| 5 | CFS_SCHEME_NAME | 名称 | string(40) | Y |  |
| 6 | LEGAL_CFS_SCHEME_FLAG | 法定合并方案标识 | number(0/1) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CFS_CYCLICALITY_ID | 合并周期 | GUID | Y |  |
| 9 | CFS_ITEM_DATASET_ID | 报表项目表 | GUID | Y |  |
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

### CFS_SCHEME_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CFS_SCHEME_D_ID | 主键 | GUID | Y | Y |
| 2 | CFS_SCOPE_CODE | 合并范围编号 | string(20) | Y |  |
| 3 | CFS_SCOPE_NAME | 合并范围名称 | string(40) | Y |  |
| 4 | CURRENCY_ID | 合并货币 | GUID | Y |  |
| 5 | YEAR_ACCUM_FLAG | 按年度累计数合并 | number(0/1) | Y |  |
| 6 | VALID_STATUS | 生失效状态 | string(40) | Y |  |
| 7 | FATHER_CFS_SCHEME_D_ID | 上层合并范围 | GUID | Y |  |
| 8 | SYS_CODE | 内码 | string(80) | Y |  |
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
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | CFS_SCHEME_ID |  | GUID | Y |  |

### CFS_SCHEME_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_SCHEME_SD_ID | 主键 | GUID | Y | Y |
| 3 | CFS_SCHEME_ID | 合并方案主键 | GUID | Y |  |
| 4 | CONTROL_FLAG | 控制方标识 | number(0/1) | Y |  |
| 5 | COMPANY_ID | 公司编号 | GUID | Y |  |
| 6 | VALID_STATUS | 生失效状态 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CURRENCY_ID | 报告货币 | GUID | Y |  |
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
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | CFS_SCHEME_D_ID |  | GUID | Y |  |

### CFS_STATUS (合并报表状态表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_STATUS_ID | 主键 | GUID | Y | Y |
| 4 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 5 | CFS_SCHEME_D_ID | 合并范围 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | CFS_PERIOD_SEQNO | 合并期间序号 | number | Y |  |
| 8 | CONSOLIDATE_STATUS | 合并状态 | number | Y |  |
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
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |

### CFS_WH_TEMPLATE (合并工作底稿格式设定)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CFS_WH_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | CFS_WH_TEMPLATE_CODE | 报表编号 | string(12) | Y |  |
| 5 | CFS_WH_TEMPLATE_NAME | 报表名称 | string(40) | Y |  |
| 6 | CFS_SCHEME_ID | 合并方案 | GUID | Y |  |
| 7 | CFS_NATURE | 报表性质 | number | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
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

### CFS_WH_TEMPLATE_D (合并工作底稿格式设定单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CFS_WH_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 3 | PRINT_CODE1 | 列印码1 | number | Y |  |
| 4 | PRINT_CODE2 | 列印码2 | number | Y |  |
| 5 | SPACE | 空格 | number | Y |  |
| 6 | CFS_ITEM_ID | 报表项目 | GUID | Y |  |
| 7 | CFS_ITEM_NAME | 报表项目名称 | string(840) | Y |  |
| 8 | DATA_TYPE | 数据类型 | number | Y |  |
| 9 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 10 | COMPUTE1 | 第1项合计值 | number | Y |  |
| 11 | COMPUTE2 | 第2项合计值 | number | Y |  |
| 12 | COMPUTE3 | 第3项合计值 | number | Y |  |
| 13 | COMPUTE4 | 第4项合计值 | number | Y |  |
| 14 | COMPUTE5 | 第5项合计值 | number | Y |  |
| 15 | COMPUTE6 | 第6项合计值 | number | Y |  |
| 16 | COMPUTE7 | 第7项合计值 | number | Y |  |
| 17 | COMPUTE8 | 第8项合计值 | number | Y |  |
| 18 | COMPUTE9 | 第9项合计值 | number | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
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
| 45 | CFS_WH_TEMPLATE_ID |  | GUID | Y |  |