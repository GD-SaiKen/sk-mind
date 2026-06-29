---
module: "EXPENSES"
name_zh: "费用管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 287
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# EXPENSES (费用管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 287

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

## Tables


- **EXPENSES_BY_RECEIPT**
- **EXPENSES_DISTRIBUTION_SD (费用分摊记录)**
- **EXPENSES_FUTURE (采购费用预估单)**
- **EXPENSES_FUTURE_D (采购费用预估单单身)**
- **EXPENSES_FUTURE_SD (采购费用预估单子单身)**
- **EXPENSES_REDISTRIBUTION_SD**


---


---


> Tables: 6

### EXPENSES_BY_RECEIPT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EXPENSES_BY_RECEIPT_ID | 主键 | GUID | Y | Y |
| 4 | SUPPLY_CENTER_ID | 供应中心 | GUID | Y |  |
| 5 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 8 | INVENTORY_QTY |  | number(16,6) | Y |  |
| 9 | EXPENSE_PRICE_TC | 费用单价（原币） | number(23,8) | Y |  |
| 10 | EXPENSE_AMOUNT_TC | 费用金额（原币） | number(23,8) | Y |  |
| 11 | EXPENSE_PRICE_BC | 费用单价（本币） | number(23,8) | Y |  |
| 12 | EXPENSE_AMOUNT_BC | 费用金额（本币） | number(23,8) | Y |  |
| 13 | ESTIMATION_TIMES | 暂估次数 | number | Y |  |
| 14 | ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 15 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 16 | SOURCE_TYPE | 来源类型 | string(40) | Y |  |
| 17 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 18 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 19 | BIN_ID | 库位 | GUID | Y |  |
| 20 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 21 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 22 | CURRENCY_ID | 货币 | GUID | Y |  |
| 23 | EXPENSE_ID | 费用编号 | GUID | Y |  |
| 24 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | REFERENCE_SOURCE_ID | 参考单据 | GUID | Y |  |
| 27 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 28 | VERIFIED_AMOUNT_TC | 已核销费用金额(原币) | number(23,8) | Y |  |
| 29 | VERIFIED_AMOUNT_BC | 已核销费用金额(本币) | number(23,8) | Y |  |
| 30 | ALLOCATED_AMOUNT_BC | 已摊入费用金额(本币) | number(23,8) | Y |  |
| 31 | EXP_ALLOC_DOC_D_ID | 费用分摊单分摊明细 | GUID | Y |  |
| 32 | PROJECT_ID | 项目 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 41 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 42 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 43 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 44 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 45 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 46 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 47 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 48 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 49 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 50 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 51 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 52 | UDF041 | 自定义字段12 | date | Y |  |
| 53 | UDF042 | 自定义字段13 | date | Y |  |
| 54 | UDF051 | 自定义字段14 | GUID | Y |  |
| 55 | UDF052 | 自定义字段15 | GUID | Y |  |
| 56 | UDF053 | 自定义字段16 | GUID | Y |  |
| 57 | UDF054 | 自定义字段17 | GUID | Y |  |
| 58 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 61 | ApproveDate | 修改日期 | date | Y |  |
| 62 | ApproveBy | 修改人 | GUID | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |
| 65 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE_ID_ROid |  | GUID | Y |  |
| 67 | TO_ASSET_STATUS | 转资状态 | number | Y |  |
| 68 | REFERENCE_SOURCE2_ID | 到货单单身主键 | GUID | Y |  |
| 69 | TO_ASSET_SOURCE_ID_RTK |  | string(400) | Y |  |
| 70 | TO_ASSET_SOURCE_ID_ROid |  | GUID | Y |  |

### EXPENSES_DISTRIBUTION_SD (费用分摊记录)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPENSES_DISTRIBUTION_SD_ID |  | GUID | Y | Y |
| 3 | EXPENSE_AMOUNT_TC | 费用金额（原币） | number(23,8) | Y |  |
| 4 | EXPENSE_AMOUNT_BC | 费用金额（本币） | number(23,8) | Y |  |
| 5 | EXPENSE_PRICE_TC | 费用单价（原币） | number(23,8) | Y |  |
| 6 | EXPENSE_PRICE_BC | 费用单价（本币） | number(23,8) | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 10 | REMARK |  | string(510) | Y |  |
| 11 | EXPENSE_TYPE | 费用类型 | number | Y |  |
| 12 | EXP_ALLOCATION | 费用分摊方式 | number | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | DISTRIBUTION_D_ID |  | GUID | Y |  |

### EXPENSES_FUTURE (采购费用预估单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EXPENSES_FUTURE_ID | 主键 | GUID | Y | Y |
| 4 | EXPENSES_FUTURE_DATE |  | date | Y |  |
| 5 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | PURCHASE_ORDER_ID | 主键 | GUID | Y |  |
| 8 | DOC_DATE | 单据日期 | date | Y |  |
| 9 | PrintCount | 打印次数 | number | Y |  |
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
| 28 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 29 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 30 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 31 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Attachments | 附件 | string | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | EXPENSES_FUTURE_TYPE | 类型 | string(40) | Y |  |
| 47 | PURCHASE_ARRIVAL_ID | 到货单 | GUID | Y |  |

### EXPENSES_FUTURE_D (采购费用预估单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPENSES_FUTURE_D_ID | 主键 | GUID | Y | Y |
| 3 | EXPENSE_TYPE | 费用类型 | number | Y |  |
| 4 | EXPENSE_ID | 费用编号 | GUID | Y |  |
| 5 | CURRENCY_ID | 币种 | GUID | Y |  |
| 6 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 7 | EXPENSE_AMOUNT_TC | 费用金额(原币) | number(23,8) | Y |  |
| 8 | EXPENSE_AMOUNT_BC | 费用金额(本币) | number(23,8) | Y |  |
| 9 | EXP_ALLOCATION | 费用分摊方式 | number | Y |  |
| 10 | SUPPLIER_ID | 费用供应商 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SOURCE_ID | GUID | GUID | Y |  |
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
| 41 | EXPENSES_FUTURE_ID |  | GUID | Y |  |
| 42 | SOURCE2_ID | 到货单序号 | GUID | Y |  |

### EXPENSES_FUTURE_SD (采购费用预估单子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPENSES_FUTURE_SD_ID | 主键 | GUID | Y | Y |
| 3 | EXPENSE_AMOUNT_TC | 费用金额(原币) | number(23,8) | Y |  |
| 4 | EXPENSE_AMOUNT_BC | 费用金额(本币) | number(23,8) | Y |  |
| 5 | EXPENSE_PRICE_TC | 费用单价(原币) | number(23,8) | Y |  |
| 6 | EXPENSE_PRICE_BC | 费用单价(本币) | number(23,8) | Y |  |
| 7 | SOURCE_ID | 采购订单次序号 | GUID | Y |  |
| 8 | ITEM_ID | 品号 | GUID | Y |  |
| 9 | ITEM_FEATURE_ID | GUID | GUID | Y |  |
| 10 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 41 | EXPENSES_FUTURE_D_ID |  | GUID | Y |  |
| 42 | SOURCE2_ID | 到货单序号 | GUID | Y |  |

### EXPENSES_REDISTRIBUTION_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPENSES_REDISTRIBUTION_SD_ID | 主键 | GUID | Y | Y |
| 3 | EXPENSE_AMOUNT_TC | 费用金额（原币） | number(23,8) | Y |  |
| 4 | EXPENSE_AMOUNT_BC | 费用金额（本币） | number(23,8) | Y |  |
| 5 | EXPENSE_PRICE_TC | 费用单价（原币） | string(400) | Y |  |
| 6 | EXPENSE_PRICE_BC | 费用单价（本币） | string(400) | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | EXPENSE_TYPE | 费用类型 | number | Y |  |
| 12 | EXP_ALLOCATION | 费用分摊方式 | number | Y |  |
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
| 43 | REDISTRIBUTION_ID |  | GUID | Y |  |