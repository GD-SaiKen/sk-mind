---
module: "JOURNAL"
name_zh: "日记账"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 273
category: financial
semantic_object: "JournalEntry/日记账"
original_tables: 5
filtered_out: 0
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# JOURNAL (日记账) - JournalEntry/日记账

> [!info] Phase 1 Core Module
> Semantic Object: JournalEntry/日记账
> Kept: 5 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 0

## Related Modules

- [[../modules/GL (总账).md|GL (总账)]]
- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]

---

## Tables

- **JOURNAL_ENTRY (分录)**
- **JOURNAL_ENTRY_D (分录明细)**
- **JOURNAL_ENTRY_DA (分录DA)**
- **JOURNAL_ENTRY_SD (分录现金流量)**
- **JOURNAL_ENTRY_SUMMARY (分录汇总)**

---

## Table Details

### JOURNAL_ENTRY (分录)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | JOURNAL_ENTRY_ID | 主键 | GUID | Y | Y |
| 4 | BATCH_NO | 分录批号 | string(60) | Y |  |
| 5 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 6 | BATCH_SEQNO | 分录批序号 | number | Y |  |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | VOUCHER_TYPE_ID | 凭证类型 | GUID | Y |  |
| 12 | VOUCHER_ID | 凭证OID | GUID | Y |  |
| 13 | JOURNAL_ENTRY_SOURCE | 分录来源 | number | Y |  |
| 14 | VOUCHER_FLAG | 生成凭证 | number(0/1) | Y |  |
| 15 | REVERSE_MOMENT | 回转时机 | number | Y |  |
| 16 | OFFSET_MOMENT | 冲销时机 | number | Y |  |
| 17 | REVERSE_VOUCHER_TYPE_ID | 回转凭证类型 | GUID | Y |  |
| 18 | DEBIT_AMT | 借方本币合计 | number(23,8) | Y |  |
| 19 | CREDIT_AMT | 贷方本币合计 | number(23,8) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | DOC_ID | 业务单据类型 | GUID | Y |  |
| 22 | ATTACHMENT | 附件数 | number | Y |  |
| 23 | VOUCHER_STATUS | 凭证状态 | number | Y |  |
| 24 | PrintCount | 打印次数 | number | Y |  |
| 25 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 26 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 27 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 28 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |
| 61 | IM_ESTI_RNP_TYPE | 存货暂估月初冲回类型 | number | Y |  |


### JOURNAL_ENTRY_D (分录明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | JOURNAL_ENTRY_D_ID | 主键 | GUID | Y | Y |
| 3 | TRANS_DOC_NO | 业务单据单号 | string(80) | Y |  |
| 4 | TRANS_DOC_LINE_SEQNO | 业务单据行序号 | number | Y |  |
| 5 | COST_FLAG | 成本分录 | number(0/1) | Y |  |
| 6 | CATEGORY1 | 分类1 | string(400) | Y |  |
| 7 | CATEGORY2 | 分类2 | string(400) | Y |  |
| 8 | CATEGORY3 | 分类3 | string(400) | Y |  |
| 9 | AMT_SOURCE | 金额来源 | string(400) | Y |  |
| 10 | ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 11 | ACCOUNT_CODE_ID | 科目编号 | GUID | Y |  |
| 12 | CURRENCY_ID | 货币 | GUID | Y |  |
| 13 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 14 | BALANCE_DIRECTION | 平衡方向(借/贷) | number | Y |  |
| 15 | AMT_TC | 原币金额 | number(23,8) | Y |  |
| 16 | AMT_FC | 本币金额 | number(23,8) | Y |  |
| 17 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 18 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 19 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 20 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 21 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 22 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 23 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 24 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 25 | SETTLEMENT_NO |  | string(60) | Y |  |
| 26 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 27 | GROUP_NO | 分组 | number | Y |  |
| 28 | GROUP_SEQNO | 组内序号 | number | Y |  |
| 29 | ORIG_ADMIN_UNIT_ID | 业务单据-部门 | GUID | Y |  |
| 30 | ORIG_CUSTOMER_ID | 业务单据-客户 | GUID | Y |  |
| 31 | ORIG_SUPPLIER_ID | 业务单据-供应商 | GUID | Y |  |
| 32 | ORIG_EMPLOYEE_ID | 业务单据-人员 | GUID | Y |  |
| 33 | ORIG_SALES_CENTER_ID | 业务单据-销售中心 | GUID | Y |  |
| 34 | ORIG_SUPPLY_CENTER_ID | 业务单据-供应中心 | GUID | Y |  |
| 35 | ORIG_PLANT_ID | 业务单据-工厂 | GUID | Y |  |
| 36 | ORIG_SETTLEMENT_METHOD_ID | 业务单据-结算方式 | GUID | Y |  |
| 37 | ORIG_SETTLEMENT_NO | 业务单据-结算号 | string(60) | Y |  |
| 38 | ORIG_SETTLEMENT_DATE | 业务单据-结算日期 | date | Y |  |
| 39 | REMARK | 备注 | string(510) | Y |  |
| 40 | TRANS_DOC_LINE_STATUS | 分录状态 | number | Y |  |
| 41 | CATEGORY4 | 分类4 | string(40) | Y |  |
| 42 | AUXILIARY_ITEM | 辅助核算项目 | string(20) | Y |  |
| 43 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 44 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 45 | PROJECT_ID | 项目 | GUID | Y |  |
| 46 | ORIG_PROJECT_ID | 业务单据-项目 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 58 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 59 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 60 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 61 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 62 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 63 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 64 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 65 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 66 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 67 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 68 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 69 | UDF041 | 自定义字段12 | date | Y |  |
| 70 | UDF042 | 自定义字段13 | date | Y |  |
| 71 | UDF051 | 自定义字段14 | GUID | Y |  |
| 72 | UDF052 | 自定义字段15 | GUID | Y |  |
| 73 | UDF053 | 自定义字段16 | GUID | Y |  |
| 74 | UDF054 | 自定义字段17 | GUID | Y |  |
| 75 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 76 | SOURCE_ID_ROid |  | GUID | Y |  |
| 77 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 78 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 79 | JOURNAL_ENTRY_ID |  | GUID | Y |  |


### JOURNAL_ENTRY_DA

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | JOURNAL_ENTRY_DA_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | DOC_ID | 业务单据类型 | GUID | Y |  |
| 6 | TRANS_DOC_TYPEKEY | 业务单据实体 | string(400) | Y |  |
| 7 | TRANS_DOC_ID | 业务单据 | GUID | Y |  |
| 8 | TRANS_DOC_NO | 业务单据单号 | string(80) | Y |  |
| 9 | JOURNAL_ENTRY_ID | 分录 | GUID | Y |  |
| 10 | COST_FLAG | 成本分录标识 | number(0/1) | Y |  |
| 11 | BATCH_NO | 分录批号 | string(60) | Y |  |
| 12 | BATCH_SEQNO | 分录批序号 | number | Y |  |
| 13 | BATCH_NO2 | 分录批号2 | string(80) | Y |  |
| 14 | VOUCHER_ID | 凭证 | GUID | Y |  |
| 15 | VOUCHER_NO | 凭证号 | string(40) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |


### JOURNAL_ENTRY_SD (分录现金流量)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | JOURNAL_ENTRY_SD_ID | 主键 | GUID | Y | Y |
| 3 | CASHFLOW_ITEM_ID | 现金流量项目编号 | GUID | Y |  |
| 4 | CASHFLOW_AMT | 现金流量金额 | number(23,8) | Y |  |
| 5 | Version | 版本号，不要随意更改 | binary | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 13 | ApproveDate | 修改日期 | date | Y |  |
| 14 | ApproveBy | 修改人 | GUID | Y |  |
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
| 33 | JOURNAL_ENTRY_SUMMARY_ID |  | GUID | Y |  |


### JOURNAL_ENTRY_SUMMARY (分录汇总)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | JOURNAL_ENTRY_SUMMARY_ID | 主键 | GUID | Y | Y |
| 3 | ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 4 | ACCOUNT_CODE_ID | 科目编号 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 7 | BALANCE_DIRECTION | 平衡方向(借/贷) | number | Y |  |
| 8 | AMT_TC | 原币金额 | number(23,8) | Y |  |
| 9 | AMT_FC | 本币金额 | number(23,8) | Y |  |
| 10 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 11 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 12 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 13 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 14 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 15 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 16 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 17 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 18 | SETTLEMENT_NO |  | string(60) | Y |  |
| 19 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 20 | AUXILIARY_ITEM | 辅助核算项目 | string(20) | Y |  |
| 21 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 22 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 23 | PROJECT_ID | 项目 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
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
| 52 | JOURNAL_ENTRY_ID |  | GUID | Y |  |
