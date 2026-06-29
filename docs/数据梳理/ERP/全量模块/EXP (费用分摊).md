---
module: "EXP"
name_zh: "费用分摊"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 466
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# EXP (费用分摊)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 8 | Columns: 466

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


- **EXP_ALLOC_DOC (费用分摊单)**
- **EXP_ALLOC_DOC_BENEFIT (费用分摊单受益业务对象)**
- **EXP_ALLOC_DOC_D (费用分摊单分摊明细)**
- **EXP_ALLOC_DOC_EID (费用分摊单费用明细)**
- **EXP_ALLOC_DOC_EIS (费用分摊单费用汇总)**
- **EXP_PAYABLE_DOC (费用应付单)**
- **EXP_PAYABLE_DOC_D (费用应付单单身)**
- **EXP_PAYABLE_DOC_TAXINV (费用应付单税务发票)**


---


---


> Tables: 8

### EXP_ALLOC_DOC (费用分摊单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | EXP_ALLOC_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | SUPPLIER_ID | 费用供应商 | GUID | Y |  |
| 12 | MULTI_EXPENSE_INDICATOR | 多费用项目分摊标识 | number(0/1) | Y |  |
| 13 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 14 | ALLOCABLE_AMT | 本次需分摊金额合计 | number(23,8) | Y |  |
| 15 | ALLOCATED_AMT | 本次已分摊金额合计 | number(23,8) | Y |  |
| 16 | ESTI_REVERSE_AP_STATUS | 应付暂估冲回状态 | number | Y |  |
| 17 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 18 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 19 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 20 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | PROJECT_ID | 项目 | GUID | Y |  |
| 23 | PrintCount | 打印次数 | number | Y |  |
| 24 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 25 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 26 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 27 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | Attachments | 附件 | string | Y |  |
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |

### EXP_ALLOC_DOC_BENEFIT (费用分摊单受益业务对象)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXP_ALLOC_DOC_BENEFIT_ID |  | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 业务源单类型 | number | Y |  |
| 4 | TRANS_DATE | 业务日期 | date | Y |  |
| 5 | ALLOCATION_AMT | 本次分摊金额 | number(23,8) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 8 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 9 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 10 | RECEIPT_PURPRICE_AMT | 入库价款金额 | number(23,8) | Y |  |
| 11 | PURCHASE_TYPE | 采购核算类型 | number | Y |  |
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
| 38 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 39 | SOURCE_ID_ROid |  | GUID | Y |  |
| 40 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 42 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 44 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 46 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 50 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE7_ID_ROid |  | GUID | Y |  |
| 52 | SOURCE8_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE8_ID_ROid |  | GUID | Y |  |
| 54 | SOURCE9_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE9_ID_ROid |  | GUID | Y |  |
| 56 | EXP_ALLOC_DOC_ID |  | GUID | Y |  |

### EXP_ALLOC_DOC_D (费用分摊单分摊明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXP_ALLOC_DOC_D_ID |  | GUID | Y | Y |
| 3 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 4 | CURRENCY_ID | 货币 | GUID | Y |  |
| 5 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 6 | ESTI_SUPPLIER_ID | 预估供应商 | GUID | Y |  |
| 7 | ESTI_AMT_TC | 预估金额(原币) | number(23,8) | Y |  |
| 8 | ESTI_AMT_FC | 预估金额(本币) | number(23,8) | Y |  |
| 9 | UNVERIFIED_AMT_TC | 未核销预估金额(原币) | number(23,8) | Y |  |
| 10 | UNVERIFIED_AMT_FC | 未核销预估金额(本币) | number(23,8) | Y |  |
| 11 | VERIFICATION_AMT_TC | 本次核销预估金额(原币) | number(23,8) | Y |  |
| 12 | VERIFICATION_AMT_FC | 本次核销预估金额(本币) | number(23,8) | Y |  |
| 13 | ALLOCATION_BASIS_VALUE | 分摊依据数值 | number(23,8) | Y |  |
| 14 | ALLOCATION_AMT | 本次分摊金额 | number(23,8) | Y |  |
| 15 | PPV | 价差 | number(23,8) | Y |  |
| 16 | ADJUSTMENT_DOC_ID | 调整单号 | GUID | Y |  |
| 17 | ADJUSTMENT_DOC_D_ID | 调整单序号 | GUID | Y |  |
| 18 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 19 | RERAP_INDICATOR | 需处理应付暂估冲回标识 | number(0/1) | Y |  |
| 20 | ESTI_REVERSE_AP_EXG | 应付暂估冲回汇率 | number(18,9) | Y |  |
| 21 | ESTI_REVERSE_AP_AMT_TC | 应付暂估冲回金额(原币) | number(23,8) | Y |  |
| 22 | ESTI_REVERSE_AP_AMT_FC | 应付暂估冲回金额(本币) | number(23,8) | Y |  |
| 23 | ESTI_REVERSE_AP_EXG_LOSS_AMT | 应付暂估冲回汇兑损失 | number(23,8) | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
| 25 | SOURCE_DOC_TYPE | 业务源单类型 | number | Y |  |
| 26 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE_ID_ROid |  | GUID | Y |  |
| 54 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 56 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 57 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 58 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 60 | EXP_ALLOC_DOC_ID |  | GUID | Y |  |

### EXP_ALLOC_DOC_EID (费用分摊单费用明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXP_ALLOC_DOC_EID_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 费用源单类型 | number | Y |  |
| 4 | EXPENSE_DATE | 费用日期 | date | Y |  |
| 5 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 6 | UNALLOCATED_AMT | 未分摊金额 | number(23,8) | Y |  |
| 7 | ALLOCABLE_AMT | 本次需分摊金额 | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 35 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 36 | SOURCE_ID_ROid |  | GUID | Y |  |
| 37 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 39 | EXP_ALLOC_DOC_ID |  | GUID | Y |  |

### EXP_ALLOC_DOC_EIS (费用分摊单费用汇总)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXP_ALLOC_DOC_EIS_ID |  | GUID | Y | Y |
| 3 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 4 | ALLOCABLE_AMT | 本次需分摊金额 | number(23,8) | Y |  |
| 5 | ALLOCATED_AMT | 本次已分摊金额 | number(23,8) | Y |  |
| 6 | ALLOCATION_MODE | 分摊方式 | number | Y |  |
| 7 | ALLOCATION_BASIS | 分摊依据 | number | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 35 | EXP_ALLOC_DOC_ID |  | GUID | Y |  |

### EXP_PAYABLE_DOC (费用应付单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | EXP_PAYABLE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 12 | SETTLEMENT_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 13 | ORDER_SUPPLIER_ID | 采购供应商 | GUID | Y |  |
| 14 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 15 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 16 | TRANS_TYPE | 业务类型 | number | Y |  |
| 17 | CURRENCY_ID | 货币 | GUID | Y |  |
| 18 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 19 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 20 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 21 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 22 | PAYMENT_DATE | 付款日 | date | Y |  |
| 23 | CASHING_DATE | 兑现日 | date | Y |  |
| 24 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 25 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 26 | EXP_CATEGORY | 费用类别 | number | Y |  |
| 27 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 28 | TAX_CONTROL_INDICATOR | 税务发票控制 | number(0/1) | Y |  |
| 29 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 30 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 31 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 32 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 33 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣率到期日1 | date | Y |  |
| 34 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣率 | date | Y |  |
| 35 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣率 | date | Y |  |
| 36 | AMT_UNTAX_TC | 无税金额合计（原币） | number(23,8) | Y |  |
| 37 | TAX_TC | 税额合计（原币） | number(23,8) | Y |  |
| 38 | AMT_UNTAX_FC | 无税金额合计（本币） | number(23,8) | Y |  |
| 39 | TAX_FC | 税额合计（本币） | number(23,8) | Y |  |
| 40 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 41 | PAYMENT_DOC_ID | 现结付款单号 | GUID | Y |  |
| 42 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 43 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 44 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 45 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 46 | REMARK | 备注 | string(510) | Y |  |
| 47 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 48 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 49 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 50 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 51 | TAX_INVOICE_TYPE | 税务发票类型 | number | Y |  |
| 52 | TAX_INVOICE_SOURCE | 税务发票来源 | number | Y |  |
| 53 | ISSUE_INVOICE_STATUS | 传入税管状态 | number | Y |  |
| 54 | TAX_DEDUCTIBLE_INDICATOR | 税额抵扣标识 | number(0/1) | Y |  |
| 55 | TAX_INVOICE_CATEGORY_DISC_ID | 折让税务发票种类 | GUID | Y |  |
| 56 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 57 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 58 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 59 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 60 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 61 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 62 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 63 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 64 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 65 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 66 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 67 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 68 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 69 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 70 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 71 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 72 | UDF041 | 自定义字段12 | date | Y |  |
| 73 | UDF042 | 自定义字段13 | date | Y |  |
| 74 | UDF051 | 自定义字段14 | GUID | Y |  |
| 75 | UDF052 | 自定义字段15 | GUID | Y |  |
| 76 | UDF053 | 自定义字段16 | GUID | Y |  |
| 77 | UDF054 | 自定义字段17 | GUID | Y |  |
| 78 | PrintCount | 打印次数 | number | Y |  |
| 79 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 80 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 81 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 82 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 83 | Version | 版本号，不要随意更改 | binary | Y |  |
| 84 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 85 | ApproveDate | 修改日期 | date | Y |  |
| 86 | ApproveBy | 修改人 | GUID | Y |  |
| 87 | CreateDate | 创建日期 | date | Y |  |
| 88 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 89 | ModifiedDate | 修改日期 | date | Y |  |
| 90 | CreateBy | 创建者 | GUID | Y |  |
| 91 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 92 | ModifiedBy | 修改者 | GUID | Y |  |
| 93 | Attachments | 附件 | string | Y |  |
| 94 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 95 | Owner_Org_RTK |  | string(400) | Y |  |
| 96 | Owner_Org_ROid |  | GUID | Y |  |
| 97 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 98 | SOURCE2_ID_ROid |  | GUID | Y |  |

### EXP_PAYABLE_DOC_D (费用应付单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 3 | TAX_ID | 税种税率 | GUID | Y |  |
| 4 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 5 | BUYER_ID | 业务人员 | GUID | Y |  |
| 6 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 7 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 8 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 9 | VAT_INDICATOR | VAT标识 | number(0/1) | Y |  |
| 10 | AMT_UNTAX_TC | 无税金额原币 | number(23,8) | Y |  |
| 11 | TAX_TC | 税额原币 | number(23,8) | Y |  |
| 12 | AMT_TC | 价税合计原币 | number(23,8) | Y |  |
| 13 | AMT_UNTAX_FC | 无税金额本币 | number(23,8) | Y |  |
| 14 | TAX_FC | 税额本币 | number(23,8) | Y |  |
| 15 | AMT_FC | 价税合计本币 | number(23,8) | Y |  |
| 16 | EXP_PROPERTY | 费用归属性质 | string(40) | Y |  |
| 17 | TAX_DEDUCTIBLE_INDICATOR | 税额抵扣标识 | number(0/1) | Y |  |
| 18 | EXPENSE_AMT | 费用金额 | number(23,8) | Y |  |
| 19 | ALLOCATED_AMT | 已分摊金额 | number(23,8) | Y |  |
| 20 | CLOSE_ALLOC_INDICATOR | 分摊结束码 | number(0/1) | Y |  |
| 21 | EXP_PAYABLE_DOC_D_ID | 主键 | GUID | Y | Y |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | ISSUE_INVOICE_STATUS | 传入税管状态 | number | Y |  |
| 24 | SOURCE_DOC_TYPE | 费用应付来源单据类型 | number | Y |  |
| 25 | EXP_TRANS_AREA | 费用业务范围 | number | Y |  |
| 26 | REVERSE_SOURCE_DOC_LINE_ID | 红冲原始单据行 | GUID | Y |  |
| 27 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 57 | SOURCE_ID_ROid |  | GUID | Y |  |
| 58 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 60 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 62 | EXP_PAYABLE_DOC_ID |  | GUID | Y |  |
| 63 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 64 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 65 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 66 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 67 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 68 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 69 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 70 | EQUAL_TRANS_AMT_UNTAX_TC | 等价值业务无税金额(原币) | number(23,8) | Y |  |
| 71 | EQUAL_TRANS_TAX_TC | 等价值业务税额(原币) | number(23,8) | Y |  |
| 72 | EQUAL_TRANS_AMT_UNTAX_FC | 等价值业务无税金额(本币) | number(23,8) | Y |  |
| 73 | EQUAL_TRANS_TAX_FC | 等价值业务税额(本币) | number(23,8) | Y |  |
| 74 | EQUAL_TRANS_EXG | 等价值业务汇率 | number(18,9) | Y |  |

### EXP_PAYABLE_DOC_TAXINV (费用应付单税务发票)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXP_PAYABLE_DOC_TAXINV_ID |  | GUID | Y | Y |
| 3 | INV_CERTIFICATE_TYPE | 发票凭证类型 | number | Y |  |
| 4 | TAX_INVOICE_NO | 税务发票号码 | string(28) | Y |  |
| 5 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 6 | TAX_ID | 税种税率 | GUID | Y |  |
| 7 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 8 | AMT_UNTAX_FC | 无税金额(本币) | number(23,8) | Y |  |
| 9 | TAX_FC | 税额(本币) | number(23,8) | Y |  |
| 10 | AMT_FC | 价税合计(本币) | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | TAX_INVOICE_SUPPLIER_ID | 税务发票供应商 | GUID | Y |  |
| 13 | TAX_INVOICE_SUPPLIER_NAME | 税务发票供应商名称 | string(144) | Y |  |
| 14 | TAX_INVOICE_SUPPLIER_TAX_NO | 税务发票供应商税号 | string(40) | Y |  |
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
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE_ID_ROid |  | GUID | Y |  |
| 45 | EXP_PAYABLE_DOC_ID |  | GUID | Y |  |