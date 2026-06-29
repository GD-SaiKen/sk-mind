---
module: "ENDING"
name_zh: "期末结转"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 166
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# ENDING (期末结转)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 166

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


- **ENDING_CARRYOVER_SETUP (期间损益结转设置信息)**
- **ENDING_CARRYOVER_SETUP_D (期间损益结转设置信息单身)**
- **ENDING_EXGADJ_SETUP (期末调汇设置信息)**
- **ENDING_EXGADJ_SETUP_D (期末调汇设置信息单身)**


---


---


> Tables: 4

### ENDING_CARRYOVER_SETUP (期间损益结转设置信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ENDING_CARRYOVER_SETUP_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿编号 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | DEF_ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 7 | FORCED_TRANSFER_INDICATOR | 对调汇科目按其属性-余额方向进行强制调汇 | number(0/1) | Y |  |
| 8 | DEF_STDP_VOUCHER_TYPE_ID | 标准期间-默认结转凭证类型 | GUID | Y |  |
| 9 | DEF_IADJP_VOUCHER_TYPE_ID | 中期调整期间-默认结转凭证类型 | GUID | Y |  |
| 10 | DEF_AADJP_VOUCHER_TYPE_ID | 年末调整期间-默认结转凭证类型 | GUID | Y |  |
| 11 | DEF_CYP_ACCOUNT_CODE_ID | 默认本年利润科目编号 | GUID | Y |  |
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
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### ENDING_CARRYOVER_SETUP_D (期间损益结转设置信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ENDING_CARRYOVER_SETUP_D_ID |  | GUID | Y | Y |
| 3 | REMARK |  | string(510) | Y |  |
| 4 | PROFIT_LOSS_ACCOUNT_CODE_ID | 损益科目编号 | GUID | Y |  |
| 5 | CYP_ACCOUNT_CODE_ID | 本年利润科目编号 | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ENDING_CARRYOVER_SETUP_ID |  | GUID | Y |  |

### ENDING_EXGADJ_SETUP (期末调汇设置信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ENDING_EXGADJ_SETUP_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿编号 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | DEF_ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 7 | BALANCE_DIRECTION | 汇兑损益科目分录方向 | number | Y |  |
| 8 | FORCED_ADJUST_INDICATOR | 对调汇科目按其属性-余额方向进行强制调汇 | number(0/1) | Y |  |
| 9 | DEF_STDP_VOUCHER_TYPE_ID | 标准期间-默认调汇凭证类型 | GUID | Y |  |
| 10 | DEF_IADJP_VOUCHER_TYPE_ID | 中期调整期间-默认调汇凭证类型 | GUID | Y |  |
| 11 | DEF_AADJP_VOUCHER_TYPE_ID | 年末调整期间-默认调汇凭证类型 | GUID | Y |  |
| 12 | DEF_EXGGL_ACCOUNT_CODE_ID | 默认汇兑损益科目编号 | GUID | Y |  |
| 13 | DEF_CASHFLOW_ITEM_ID | 默认现金流量项目编号 | GUID | Y |  |
| 14 | ADVANCED_INDICATOR | 高级设置标识 | number(0/1) | Y |  |
| 15 | DEF_EXGL_ACCOUNT_CODE_ID | 默认汇兑损失科目 | GUID | Y |  |
| 16 | EXGL_BALANCE_DIRECTION | 汇兑损失科目分录方向 | number | Y |  |
| 17 | DEF_EXGG_ACCOUNT_CODE_ID | 默认汇兑收益科目 | GUID | Y |  |
| 18 | EXGG_BALANCE_DIRECTION | 汇兑收益科目分录方向 | number | Y |  |
| 19 | CASHFLOW_ITEM_IN_ID | 汇兑收益现金流量项目 | GUID | Y |  |
| 20 | CASHFLOW_ITEM_OUT_ID | 汇兑损失现金流量项目 | GUID | Y |  |
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
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### ENDING_EXGADJ_SETUP_D (期末调汇设置信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ENDING_EXGADJ_SETUP_D_ID | 主键 | GUID | Y | Y |
| 3 | REMARK |  | string(510) | Y |  |
| 4 | FOREIGN_CURRENCY_ID | 外币 | GUID | Y |  |
| 5 | EXGGL_ACCOUNT_CODE_ID | 汇兑损益科目编号 | GUID | Y |  |
| 6 | CASHFLOW_ITEM_ID | 现金流量项目编号 | GUID | Y |  |
| 7 | EXGL_ACCOUNT_CODE_ID | 汇兑损失科目 | GUID | Y |  |
| 8 | EXGG_ACCOUNT_CODE_ID | 汇兑收益科目 | GUID | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ENDING_EXGADJ_SETUP_ID |  | GUID | Y |  |