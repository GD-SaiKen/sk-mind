---
module: "VOUCHER"
name_zh: "凭证管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 266
category: financial
semantic_object: "Voucher/凭证"
original_tables: 5
filtered_out: 0
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# VOUCHER (凭证管理) - Voucher/凭证

> [!info] Phase 1 Core Module
> Semantic Object: Voucher/凭证
> Kept: 4 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 0

## Related Modules

- [[../modules/GL (总账).md|GL (总账)]]
- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]

---

## Tables

- **VOUCHER_BROKEN (凭证断号)**
- **VOUCHER_D (凭证单身)**
- **VOUCHER_SD (凭证子单身)**
- **VOUCHER_VERIFIED (凭证冲账子单身)**

---

## Table Details

### VOUCHER_BROKEN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | VOUCHER_BROKEN_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | BROKEN_TYPE | 断号类型 | number | Y |  |
| 8 | BROKEN_NO | 断号 | number | Y |  |
| 9 | VOUCHER_TYPE_ID | 凭证类型 | GUID | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |


### VOUCHER_D (凭证单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | VOUCHER_D_ID | 主键 | GUID | Y | Y |
| 3 | ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 4 | BALANCE_DIRECTION | 平衡方向(借/贷) | number | Y |  |
| 5 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 6 | TRANS_CURRENCY_AMT | 原币金额 | number(23,8) | Y |  |
| 7 | FUNCTION_CURRENCY_AMT | 本币金额 | number(23,8) | Y |  |
| 8 | TRANS_QTY |  | number(16,6) | Y |  |
| 9 | TRANS_PRICE | 单价 | number(23,8) | Y |  |
| 10 | SETTLEMENT_NO |  | string(60) | Y |  |
| 11 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 12 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 13 | ACCOUNT_CODE_ID | 科目编号 | GUID | Y |  |
| 14 | TRANS_CURRENCY_ID | 交易货币 | GUID | Y |  |
| 15 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 16 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 17 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 18 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 19 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 20 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 21 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 22 | ENTRY_TYPE | 立冲账类型 | number | Y |  |
| 23 | MULTI_CURRENCY_FLAG | 异货币冲账标识 | number(0/1) | Y |  |
| 24 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 25 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 26 | VERIFICATION_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 27 | VERIFICATION_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 28 | SIMPLE_REFERENCE_DOC_LINE_ID | 简参单据行 | GUID | Y |  |
| 29 | PROJECT_ID | 项目 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | PostStatus |  | string(400) | Y |  |
| 59 | PostDate |  | date | Y |  |
| 60 | PostBy |  | GUID | Y |  |
| 61 | VOUCHER_ID |  | GUID | Y |  |


### VOUCHER_SD (凭证子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | VOUCHER_SD_ID | 主键 | GUID | Y | Y |
| 3 | CASHFLOW_AMT | 现金流量金额 | number(23,8) | Y |  |
| 4 | CASHFLOW_ITEM_ID | 现金流量项目编号 | GUID | Y |  |
| 5 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 33 | PostStatus |  | string(400) | Y |  |
| 34 | PostDate |  | date | Y |  |
| 35 | PostBy |  | GUID | Y |  |
| 36 | VOUCHER_D_ID |  | GUID | Y |  |


### VOUCHER_VERIFIED (凭证冲账子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | VOUCHER_VERIFIED_ID | 主键 | GUID | Y | Y |
| 3 | OPEN_ITEM_ID | 未清项目 | GUID | Y |  |
| 4 | OI_VOUCHER_ID | 未清项目_立账凭证 | GUID | Y |  |
| 5 | OI_VOUCHER_D_ID | 未清项目_立账凭证行 | GUID | Y |  |
| 6 | CURRENCY_ID | 货币 | GUID | Y |  |
| 7 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 8 | BALANCE_AMT_TC | 余额(原币) | number(23,8) | Y |  |
| 9 | BALANCE_AMT_FC | 余额(本币) | number(23,8) | Y |  |
| 10 | VERIFICATION_TOTAL_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 11 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 12 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 13 | VERIFICATION_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 14 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 15 | EXCHANGE_GL_AMT | 汇兑损益 | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | BALANCE_DIRECTION | 平衡方向(借/贷) | number | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | PostStatus |  | string(400) | Y |  |
| 47 | PostDate |  | date | Y |  |
| 48 | PostBy |  | GUID | Y |  |
| 49 | VOUCHER_D_ID |  | GUID | Y |  |
