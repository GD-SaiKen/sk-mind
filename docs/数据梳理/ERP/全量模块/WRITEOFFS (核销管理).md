---
module: "WRITEOFFS"
name_zh: "核销管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 0
columns: 0
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# WRITEOFFS (核销管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 0 | Columns: 0

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]

---

# WRITEOFFS (核销管理)

> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
 | Server: .\\SQLEXPRESS | Tables: 6 | Generated: 2026-06-25 10:52

---


> Tables: 6

### WRITEOFFS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | WRITEOFFS_ID | 核销明细主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | BUSINESS_QTY | 核销业务数量 | number(16,6) | Y |  |
| 6 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | SECOND_UNIT_QTY | 核销第二单位数量 | number(16,6) | Y |  |
| 10 | WRITEDOFF_INV_QTY | 核销库存单位数量 | number(16,6) | Y |  |
| 11 | SOURCE_ID | 源单ID | GUID | Y |  |
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
| 37 | BC_GEN_SI_ID |  | GUID | Y |  |

### WRITEOFFS_IR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_ID | 品号 | GUID | Y |  |
| 2 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 3 | INV_QTY | 核销库存单位数量 | number(16,6) | Y |  |
| 4 | BUSINESS_QTY | 核销业务单位数量 | number(16,6) | Y |  |
| 5 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 6 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | MO_ID | 工单 | GUID | Y |  |
| 10 | OPERATION_ID | 工艺 | GUID | Y |  |
| 11 | REPLACED_MO_D_ID | 主键 | GUID | Y |  |
| 12 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 13 | SOURCE_TYPE | 类别 | string(40) | Y |  |
| 14 | WRITEOFFS_IR_ID |  | string(400) | Y | Y |
| 15 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 16 | MO_D_ID | 工单单身 | GUID | Y |  |
| 17 | ISSUE_RECEIPT_REQ_D_ID | 领料申请单单身 | GUID | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE_ID_ROid |  | GUID | Y |  |
| 45 | BC_GEN_IR_ID |  | GUID | Y |  |

### WRITEOFFS_MR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_ID | 品号 | GUID | Y |  |
| 2 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 3 | ACCEPTED_INV_QTY | 核销库存单位数量 | number(18,0) | Y |  |
| 4 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 5 | ACCEPTED_QTY | 业务单位数量 | number(18,0) | Y |  |
| 6 | DESTROYED_QTY | 破坏数量 | number(18,0) | Y |  |
| 7 | SCRAP_QTY | 报废数量 | number(18,0) | Y |  |
| 8 | DESTROYED_SECOND_QTY | 破坏第二数量 | number(18,0) | Y |  |
| 9 | SCRAP_SECOND_QTY | 报废第二数量 | number(18,0) | Y |  |
| 10 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 11 | BIN_ID | 库位 | GUID | Y |  |
| 12 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 13 | SECOND_QTY | 第二单位数量 | number(18,0) | Y |  |
| 14 | MO_ID | 工单 | GUID | Y |  |
| 15 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 16 | ITEM_DESCRIPTION | 品名 | string(400) | Y |  |
| 17 | ITEM_SPECIFICATION | 规格 | string(400) | Y |  |
| 18 | SequenceNumber | 序号 | number | Y |  |
| 19 | WRITEOFFS_MR_ID |  | string(400) | Y | Y |
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
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |
| 47 | BC_GEN_MR_ID |  | GUID | Y |  |

### WRITEOFFS_PR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | WRITEOFFS_PR_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | BUSINESS_QTY | 核销业务数量 | number(16,6) | Y |  |
| 6 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | SECOND_UNIT_QTY | 核销第二单位数量 | number(16,6) | Y |  |
| 10 | WRITEDOFF_INV_QTY | 核销库存单位数量 | number(16,6) | Y |  |
| 11 | PURCHASE_ARRIVAL_D_ID | 到货明细 | GUID | Y |  |
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
| 37 | BC_GEN_PR_ID |  | GUID | Y |  |

### WRITEOFFS_TI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | WRITEOFFS_TI_ID | 主键 | GUID | Y | Y |
| 2 | SOURCE_ID | 主键 | GUID | Y |  |
| 3 | ITEM_ID | 主键 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 主键 | GUID | Y |  |
| 5 | ITEM_LOT_ID | 主键 | GUID | Y |  |
| 6 | TO_BIN_ID | 主键 | GUID | Y |  |
| 7 | WRITEDOFF_INV_QTY | 核销库存单位数量 | number(16,6) | Y |  |
| 8 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 9 | BUSINESS_QTY | 业务单位数量 | number(16,6) | Y |  |
| 10 | SECOND_UNIT_QTY | 第二单位数量 | number(16,6) | Y |  |
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
| 36 | BC_GEN_TI_ID |  | GUID | Y |  |

### WRITEOFFS_TO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | WRITEOFFS_TO_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 4 | WRITEDOFF_INV_QTY | 核销库存单位数量 | number(16,6) | Y |  |
| 5 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 6 | BUSINESS_QTY | 业务单位数量 | number(16,6) | Y |  |
| 7 | FROM_BIN_ID | 主键 | GUID | Y |  |
| 8 | TO_BIN_ID | 主键 | GUID | Y |  |
| 9 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 10 | SECOND_UNIT_QTY | 第二单位数量 | number(16,6) | Y |  |
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
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 37 | SOURCE_ID_ROid |  | GUID | Y |  |
| 38 | BC_GEN_TO_ID |  | GUID | Y |  |