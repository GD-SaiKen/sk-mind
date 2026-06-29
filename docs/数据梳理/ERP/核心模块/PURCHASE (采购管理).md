---
module: "PURCHASE"
name_zh: "采购管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 22
columns: 1763
category: purchase
semantic_object: "Purchase/采购管理"
original_tables: 22
filtered_out: 0
tags: ["ERP", "E10", "purchase", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# PURCHASE (采购管理) - Purchase/采购管理

> [!info] Phase 1 Core Module
> Semantic Object: Purchase/采购管理
> Kept: 22 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 2

## Related Modules

- [[../modules/PO (采购订单).md|PO (采购订单)]]
- [[../modules/SUPPLIER (供应商).md|SUPPLIER (供应商)]]
- [[../modules/REQUISITION (请购管理).md|REQUISITION (请购管理)]]
- [[../modules/IMPORT (进口管理).md|IMPORT (进口管理)]]

---

## Tables

- **PURCHASE_ARRIVAL (到货单)**
- **PURCHASE_ARRIVAL_D (到货单明细)**
- **PURCHASE_ARRIVAL_TAXINV (到货单税务发票)**
- **PURCHASE_CONTRACT (采购合同)**
- **PURCHASE_CONTRACT_D (合同明细)**
- **PURCHASE_FACT_TABLE (采购统计分析表)**
- **PURCHASE_FINANCE_INFO (采购出入库业务财务信息)**
- **PURCHASE_GOODS (采购入库单)**
- **PURCHASE_GOODS_D (采购入库单单身)**
- **PURCHASE_ISSUE (采购退货出库单)**
- **PURCHASE_ISSUE_D (采购退货出库单单身)**
- **PURCHASE_ORDER (采购订单)**
- **PURCHASE_ORDER_D (采购单身明细)**
- **PURCHASE_ORDER_SD (采购子单身)**
- **PURCHASE_ORDER_SD1 (采购订单子单身1)**
- **PURCHASE_ORDER_SSD (采购订单孙单身)**
- **PURCHASE_RECEIPT (采购入库单)**
- **PURCHASE_RECEIPT_D (采购入库单单身)**
- **PURCHASE_REJECT_RETURN (维护拒收退货单)**
- **PURCHASE_REJECT_RETURN_D (维护拒收退货单单身)**
- **PURCHASE_RETURN (采购退货单)**
- **PURCHASE_RETURN_D (采购退货单单身)**

---

## Table Details

### PURCHASE_ARRIVAL (到货单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PURCHASE_ARRIVAL_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | ARRIVAL_DATE | 到货日期 | date | Y |  |
| 9 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 10 | SUPPLIER_ORDER_NO | 供应商单号 | string(510) | Y |  |
| 11 | EXCHANGE_RATE | 匯率 | number(18,9) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | PIECES |  | number | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | SUPPLIER_CONTACT_NAME | 供应商联系人 | string(72) | Y |  |
| 16 | SUPPLIER_ADDR_NAME | 供应商地址 | string(510) | Y |  |
| 17 | INVOICE_CONTACT_NAME | 结算联系人 | string(72) | Y |  |
| 18 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 19 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 20 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 21 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 22 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 23 | SOURCE_TYPE | 来源别 | string(40) | Y |  |
| 24 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 25 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 26 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 27 | SUPPLIER_ADDR_ID | 供应商地址编号 | GUID | Y |  |
| 28 | INVOICE_CONTACT_ID | 结算联系人编号 | GUID | Y |  |
| 29 | INVOICE_ADDR_ID | 结算地址编号 | GUID | Y |  |
| 30 | RECEIPT_EMPLOYEE_ID | 收货人 | GUID | Y |  |
| 31 | PLANT_ID | 收货工厂/储运 | GUID | Y |  |
| 32 | CURRENCY_ID | 币种 | GUID | Y |  |
| 33 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 34 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 35 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 36 | SUPPLIER_CONTACT_ID | 供应商联系人编号 | GUID | Y |  |
| 37 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 38 | INVOICE_COMPANY_ID |  | GUID | Y |  |
| 39 | SYNERGY_ID | 内部协同关系 | GUID | Y |  |
| 40 | SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 41 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 42 | DIRECT_INVOICING_INDICATOR | 随货附票 | number(0/1) | Y |  |
| 43 | OFFSET_DEPOSIT_INDICATOR | 订金冲减 | number(0/1) | Y |  |
| 44 | RECEIPTED_STATUS | 入库状态 | string(40) | Y |  |
| 45 | SETTLEMENT_INDICATOR | 当前可结算 | number(0/1) | Y |  |
| 46 | SIGN_DATE | 签收日期 | date | Y |  |
| 47 | TAX_ID | 税种 | GUID | Y |  |
| 48 | WIP_NO | WIP集成ID | string(40) | Y |  |
| 49 | WIP_E10_INSPECTION | WIP集成由E10质检 | number(0/1) | Y |  |
| 50 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 53 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 54 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 55 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 56 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 57 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 58 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 59 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 60 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 61 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 62 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 63 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 64 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 65 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 66 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 67 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 68 | UDF041 | 自定义字段12 | date | Y |  |
| 69 | UDF042 | 自定义字段13 | date | Y |  |
| 70 | UDF051 | 自定义字段14 | GUID | Y |  |
| 71 | UDF052 | 自定义字段15 | GUID | Y |  |
| 72 | UDF053 | 自定义字段16 | GUID | Y |  |
| 73 | UDF054 | 自定义字段17 | GUID | Y |  |
| 74 | PrintCount | 打印次数 | number | Y |  |
| 75 | CreateDate | 创建日期 | date | Y |  |
| 76 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 77 | ModifiedDate | 修改日期 | date | Y |  |
| 78 | CreateBy | 创建者 | GUID | Y |  |
| 79 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 80 | ModifiedBy | 修改者 | GUID | Y |  |
| 81 | Attachments | 附件 | string | Y |  |
| 82 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 83 | ApproveDate | 修改日期 | date | Y |  |
| 84 | ApproveBy | 修改人 | GUID | Y |  |
| 85 | Owner_Org_RTK |  | string(400) | Y |  |
| 86 | Owner_Org_ROid |  | GUID | Y |  |
| 87 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 88 | SOURCE_ID_ROid |  | GUID | Y |  |
| 89 | RECEIVE_Owner_Org_RTK |  | string(400) | Y |  |
| 90 | RECEIVE_Owner_Org_ROid |  | GUID | Y |  |
| 91 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 92 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 93 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 94 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 95 | DOC_Sequence | 单据顺序 | number | Y |  |
| 96 | SOURCE_SUPPLIER_ID | 最终供应商 | GUID | Y |  |
| 97 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 98 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |


### PURCHASE_ARRIVAL_D (到货单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ARRIVAL_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 8 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 9 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 10 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 11 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 13 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 14 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 15 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 16 | PRICE | 單價 | number(23,8) | Y |  |
| 17 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 18 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 19 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 20 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 21 | TAX_RATE |  | number(5,4) | Y |  |
| 22 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 23 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 24 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 25 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 26 | AMOUNT |  | number(23,8) | Y |  |
| 27 | ACCEPTED_BUSINESS_QTY | 允收业务数量 | number(16,6) | Y |  |
| 28 | ACCEPTED_INVENTORY_QTY | 允收库存单位数量 | number(16,6) | Y |  |
| 29 | RETURN_BUSINESS_QTY | 拒收业务数量 | number(16,6) | Y |  |
| 30 | SCRAP_BUSINESS_QTY | 报废业务数量 | number(16,6) | Y |  |
| 31 | OVERDUE_INDICATOR | 超期码 | number(0/1) | Y |  |
| 32 | INSPECTION_STATUS | 检验状态 | string(40) | Y |  |
| 33 | PIECES |  | number | Y |  |
| 34 | RETURNED_BUSINESS_QTY | 已退回业务数量 | number(16,6) | Y |  |
| 35 | RECEIPTED_BUSINESS_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 36 | RECEIPT_CLOSE | 入库结束码 | string(40) | Y |  |
| 37 | SCRAPED_BUSINESS_QTY | 已报废业务数量 | number(16,6) | Y |  |
| 38 | REMARK | 备注 | string(510) | Y |  |
| 39 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 40 | INSPECTED_QTY | 已检验业务数量 | number(16,6) | Y |  |
| 41 | SP_RECEIPT_BUSINESS_QTY | 特采业务数量 | number(16,6) | Y |  |
| 42 | SP_RECEIPT_INVENTORY_QTY | 特采库存单位数量 | number(16,6) | Y |  |
| 43 | MANUFACTURER | 品牌信息 | string(510) | Y |  |
| 44 | PAYMENT_PENDED | 暂不付款 | number(0/1) | Y |  |
| 45 | QUALIFIED_BUSINESS_QTY | 合格业务数量 | number(16,6) | Y |  |
| 46 | UNQUALIFIED_BUSINESS_QTY | 不合格业务数量 | number(16,6) | Y |  |
| 47 | IN_DESTROYED_BUSINESS_QTY | 检验破坏业务数量 | number(16,6) | Y |  |
| 48 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 49 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 50 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 51 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 52 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 53 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 54 | PACKING3_UNIT_ID | 主键 | GUID | Y |  |
| 55 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 56 | TAX_ID | 税种 | GUID | Y |  |
| 57 | WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 58 | OPERATION_ID | 工艺 | GUID | Y |  |
| 59 | BIN_ID | 库位 | GUID | Y |  |
| 60 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 61 | ITEM_CERTIFICATION_D_ID |  | GUID | Y |  |
| 62 | MO_ID | 工单ID | GUID | Y |  |
| 63 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 64 | SETTLEMENT_AMT_UN_TAX_OC | 已结算未税金额 | number(23,8) | Y |  |
| 65 | SETTLEMENT_TAX_OC | 已结算税额 | number(23,8) | Y |  |
| 66 | PURCHASE_ORDER_ID | 采购订单ID | GUID | Y |  |
| 67 | SIGN_TYPE | 签收状态 | string(40) | Y |  |
| 68 | RETURN_REASON_ID | 差异原因 | GUID | Y |  |
| 69 | SUPP_INDEM_BUSINESS_QTY | 供应商认赔业务数量 | number(16,6) | Y |  |
| 70 | SUPP_INDEM_PRICE_QTY | 供应商认赔计价数量 | number(16,6) | Y |  |
| 71 | LOSS_BUSINESS_QTY | 损耗认赔业务数量 | number(16,6) | Y |  |
| 72 | LOSS_PRICE_QTY | 损耗认赔计价数量 | number(16,6) | Y |  |
| 73 | SHOULD_SETTLE_PRICE_QTY | 应结算计价数量 | number(16,6) | Y |  |
| 74 | JUDGED_QTY | 已判定业务数量 | number(16,6) | Y |  |
| 75 | SP_APPROVE_FLAG | 特批 | number(0/1) | Y |  |
| 76 | PROJECT_ID | 项目 | GUID | Y |  |
| 77 | DEDUCT_ARRIVED_QTY | 扣已到货量 | number(0/1) | Y |  |
| 78 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 79 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 80 | WIP_DOCNO | WIP集成单号序号 | string(50) | Y |  |
| 81 | Version | 版本号，不要随意更改 | binary | Y |  |
| 82 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 83 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 84 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 85 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 86 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 87 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 88 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 89 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 90 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 91 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 92 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 93 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 94 | UDF041 | 自定义字段12 | date | Y |  |
| 95 | UDF042 | 自定义字段13 | date | Y |  |
| 96 | UDF051 | 自定义字段14 | GUID | Y |  |
| 97 | UDF052 | 自定义字段15 | GUID | Y |  |
| 98 | UDF053 | 自定义字段16 | GUID | Y |  |
| 99 | UDF054 | 自定义字段17 | GUID | Y |  |
| 100 | CreateDate | 创建日期 | date | Y |  |
| 101 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 102 | ModifiedDate | 修改日期 | date | Y |  |
| 103 | CreateBy | 创建者 | GUID | Y |  |
| 104 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 105 | ModifiedBy | 修改者 | GUID | Y |  |
| 106 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 107 | ApproveDate | 修改日期 | date | Y |  |
| 108 | ApproveBy | 修改人 | GUID | Y |  |
| 109 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 110 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 111 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 112 | SOURCE_ID_ROid |  | GUID | Y |  |
| 113 | PURCHASE_ARRIVAL_ID |  | GUID | Y |  |
| 114 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 115 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 116 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 117 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 118 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 119 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 120 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 121 | INNER_ORDER_DOC_SD_ID | 内部订单 | GUID | Y |  |
| 122 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 123 | SOURCE_ORDER_ROid |  | GUID | Y |  |
| 124 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 125 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |


### PURCHASE_ARRIVAL_TAXINV (到货单税务发票)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ARRIVAL_TAXINV_ID | 主键 | GUID | Y | Y |
| 3 | TAX_INVOICE_NO | 税务发票号码 | string(28) | Y |  |
| 4 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 5 | TAX_ID | 税种税率 | GUID | Y |  |
| 6 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 7 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 8 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 9 | AMOUNT_BC | 本币价税合计 | number(23,8) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | INV_CERTIFICATE_TYPE | 发票凭证类型 | number | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | PURCHASE_ARRIVAL_ID |  | GUID | Y |  |


### PURCHASE_CONTRACT (采购合同)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PURCHASE_CONTRACT_ID | 主键 | GUID | Y | Y |
| 7 | APPROVE_DATE | 审核日期 | date | Y |  |
| 8 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 9 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 10 | CONTRACT_NO | 合同编号 | string(80) | Y |  |
| 11 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 12 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 13 | CONTRACT_DESCRIBE | 合同描述 | string(160) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | QTY_CONTROL | 总数量控制 | number(0/1) | Y |  |
| 16 | CATEGORY | 单据性质 | string(40) | Y |  |
| 17 | AMT_CONTROL | 总金额控制 | number(0/1) | Y |  |
| 18 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 19 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 20 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 21 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 22 | AMT_UPPER_LIMIT_OC | 上限原币总金额 | number(23,8) | Y |  |
| 23 | DATE_SIGNED | 合同签订日期 | date | Y |  |
| 24 | ORDERED_AMT | 已订货原币总金额 | number(23,8) | Y |  |
| 25 | ORDERED_BUSINESS_QTY | 已订货业务数量 | number(16,6) | Y |  |
| 26 | PIECES |  | number | Y |  |
| 27 | QTY_UPPER_LIMIT | 上限总数量 | number(16,6) | Y |  |
| 28 | SUPPLIER_ADDR_NAME | 供应商地址 | string(510) | Y |  |
| 29 | SUPPLIER_CONTACT_NAME | 供应商联系人 | string(72) | Y |  |
| 30 | CONTRACT_DESCRIPTION | 合同名称 | string(144) | Y |  |
| 31 | INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 32 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 33 | INVOICE_CONTACT_NAME | 结算联系人 | string(72) | Y |  |
| 34 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 35 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 36 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 37 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 38 | COMPANY_ID | 合同公司 | GUID | Y |  |
| 39 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 40 | CURRENCY_ID | 币种 | GUID | Y |  |
| 41 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 42 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 43 | SUPPLIER_ADDR_ID | 地址编码 | GUID | Y |  |
| 44 | SUPPLIER_CONTACT_ID | 联系人编码 | GUID | Y |  |
| 45 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 46 | INVOICE_ADDR_ID | 结算地址编码 | GUID | Y |  |
| 47 | INVOICE_CONTACT_ID | 结算联系人编码 | GUID | Y |  |
| 48 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 49 | PLANT_ID | 收货工厂 | GUID | Y |  |
| 50 | TAX_ID | 税种 | GUID | Y |  |
| 51 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 70 | Version | 版本号，不要随意更改 | binary | Y |  |
| 71 | PrintCount | 打印次数 | number | Y |  |
| 72 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 73 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 74 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 75 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 76 | CreateDate | 创建日期 | date | Y |  |
| 77 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 78 | ModifiedDate | 修改日期 | date | Y |  |
| 79 | CreateBy | 创建者 | GUID | Y |  |
| 80 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 81 | ModifiedBy | 修改者 | GUID | Y |  |
| 82 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 83 | ApproveDate | 修改日期 | date | Y |  |
| 84 | ApproveBy | 修改人 | GUID | Y |  |
| 85 | Attachments | 附件 | string | Y |  |
| 86 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 87 | Owner_Org_RTK |  | string(400) | Y |  |
| 88 | Owner_Org_ROid |  | GUID | Y |  |


### PURCHASE_CONTRACT_D (合同明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_CONTRACT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 6 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 7 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 8 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 9 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 10 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 11 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 12 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 13 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 14 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | TAX_RATE |  | number(5,4) | Y |  |
| 17 | PRICE |  | number(23,8) | Y |  |
| 18 | ORDERED_BUSINESS_QTY | 已订货业务数量 | number(16,6) | Y |  |
| 19 | QTY_LIMIT | 数量限制 | number(0/1) | Y |  |
| 20 | AMT_LIMIT | 金额限制 | number(0/1) | Y |  |
| 21 | BUSINESS_QTY_UPPER_LIMIT | 业务数量上限 | number(16,6) | Y |  |
| 22 | AMT_OC_UPPER_LIMIT | 原币金额上限 | number(23,8) | Y |  |
| 23 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 24 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 25 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 26 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 27 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 28 | AMOUNT |  | number(23,8) | Y |  |
| 29 | ORDERED_AMT | 已订货原币金额 | number(23,8) | Y |  |
| 30 | CLOSE | 结束码 | string(40) | Y |  |
| 31 | PRICE_LIMIT | 单价控制 | number(0/1) | Y |  |
| 32 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 33 | FEATURE_VALUE | 品类值属性值 | string(40) | Y |  |
| 34 | FEATURE_VALUE_DESC | 品类描述属性值描述 | string(120) | Y |  |
| 35 | PIECES | 件数 | number | Y |  |
| 36 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 37 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 38 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 39 | TAX_ID | 税种 | GUID | Y |  |
| 40 | ITEM_ID | 品号 | GUID | Y |  |
| 41 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 42 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 43 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 44 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 45 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 46 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 47 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 48 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 49 | FEATURE_ID | 品类属性项ID | GUID | Y |  |
| 50 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 51 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 52 | PROJECT_ID | 项目 | GUID | Y |  |
| 53 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 54 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 55 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 56 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 57 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 58 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 59 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 60 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 61 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 62 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 63 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 64 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 65 | UDF041 | 自定义字段12 | date | Y |  |
| 66 | UDF042 | 自定义字段13 | date | Y |  |
| 67 | UDF051 | 自定义字段14 | GUID | Y |  |
| 68 | UDF052 | 自定义字段15 | GUID | Y |  |
| 69 | UDF053 | 自定义字段16 | GUID | Y |  |
| 70 | UDF054 | 自定义字段17 | GUID | Y |  |
| 71 | Version | 版本号，不要随意更改 | binary | Y |  |
| 72 | CreateDate | 创建日期 | date | Y |  |
| 73 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 74 | ModifiedDate | 修改日期 | date | Y |  |
| 75 | CreateBy | 创建者 | GUID | Y |  |
| 76 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 77 | ModifiedBy | 修改者 | GUID | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |
| 81 | PURCHASE_CONTRACT_ID |  | GUID | Y |  |


### PURCHASE_FACT_TABLE (采购统计分析表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PURCHASE_FACT_TABLE_ID | 主键 | GUID | Y | Y |
| 4 | DATE | 日期 | string(400) | Y |  |
| 5 | COMPANY_CODE | 公司编号 | string(20) | Y |  |
| 6 | COMPANY_NAME | 公司名称 | string(40) | Y |  |
| 7 | COMPANY_ID | 公司 | GUID | Y |  |
| 8 | ACC_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACC_PERIOD | 会计期间 | string(20) | Y |  |
| 10 | SUPPLIER_CODE | 供应商编号 | string(20) | Y |  |
| 11 | SUPPLIER_NAME | 供应商名称 | string(40) | Y |  |
| 12 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 13 | ITEM_CODE | 品号 | string(80) | Y |  |
| 14 | ITEM_NAME | 品名 | string(120) | Y |  |
| 15 | ITEM_SPEC | 规格 | string(510) | Y |  |
| 16 | ITEM_FEATURE_CODE | 特征码 | string(120) | Y |  |
| 17 | ITEM_FEATURE_SPEC | 特征码规格 | string(510) | Y |  |
| 18 | ITEM_ID | 品号主键 | GUID | Y |  |
| 19 | ITEM_FEATURE_ID | 特征码主键 | GUID | Y |  |
| 20 | ADMIN_UNIT_CODE | 部门编号 | string(20) | Y |  |
| 21 | ADMIN_UNIT_NAME | 部门名称 | string(40) | Y |  |
| 22 | EMPLOYEE_CODE | 业务员编号 | string(20) | Y |  |
| 23 | EMPLOYEE_NAME | 业务员名称 | string(40) | Y |  |
| 24 | SUPPLY_CENTER_CODE | 采购域编号 | string(40) | Y |  |
| 25 | SUPPLY_CENTER_NAME | 采购域名称 | string(40) | Y |  |
| 26 | PO_RECORDS | 采购笔数 | number | Y |  |
| 27 | PO_LATE_RECORDS | 采购延交笔数 | number | Y |  |
| 28 | PO_AMT | 采购金额 | number(23,8) | Y |  |
| 29 | PO_QTY | 采购数量 | number(16,6) | Y |  |
| 30 | PO_QTY2 | 采购第二数量 | number(16,6) | Y |  |
| 31 | PA_RECORDS | 到货笔数 | number | Y |  |
| 32 | PA_AMT | 到货金额 | number(23,8) | Y |  |
| 33 | PA_QTY | 到货数量 | number(16,6) | Y |  |
| 34 | PA_QTY2 | 到货第二数量 | number(16,6) | Y |  |
| 35 | PRICE | 采购加权单价 | number(23,8) | Y |  |
| 36 | MAX_PRICE | 最高采购单价 | number(23,8) | Y |  |
| 37 | MIN_PRICE | 最低采购单价 | number(23,8) | Y |  |
| 38 | PA_QUL_QTY | 合格数量 | number(16,6) | Y |  |
| 39 | PA_NONQUL_QTY | 不合格数量 | number(16,6) | Y |  |
| 40 | PA_QUL_QTY2 | 到货合格第二数量 | number(16,6) | Y |  |
| 41 | PA_NONQUL_QTY2 | 到货不合格第二数量 | number(16,6) | Y |  |
| 42 | PA_REC_QTY | 已入库量 | number(16,6) | Y |  |
| 43 | PA_REC_QTY2 | 已入库第二数量 | number(16,6) | Y |  |
| 44 | PA_SCR_QTY | 已报废量 | number(16,6) | Y |  |
| 45 | PA_SCR_QTY2 | 已报废第二数量 | number(16,6) | Y |  |
| 46 | PA_SP_REC_QTY | 特采数量 | number(16,6) | Y |  |
| 47 | PA_SP_REC_QTY2 | 特采第二数量 | number(16,6) | Y |  |
| 48 | PA_AP_QTY | 已结算数量 | number(16,6) | Y |  |
| 49 | PA_AP_QTY2 | 已结算第二数量 | number(16,6) | Y |  |
| 50 | PA_TCHECK_QTY | 未入库数量 | number(16,6) | Y |  |
| 51 | PA_TCHECK_QTY2 | 未入库第二数量 | number(16,6) | Y |  |
| 52 | IR_RECORDS | 验退笔数 | number | Y |  |
| 53 | IR_QTY | 验退数量 | number(16,6) | Y |  |
| 54 | IR_QTY2 | 验退第二数量 | number(16,6) | Y |  |
| 55 | IR_AMT | 验退金额 | number(23,8) | Y |  |
| 56 | RT_RECORDS | 采退笔数 | number | Y |  |
| 57 | RT_QTY | 采退数量 | number(16,6) | Y |  |
| 58 | RT_QTY2 | 采退第二数量 | number(16,6) | Y |  |
| 59 | RT_AMT | 采退金额 | number(23,8) | Y |  |
| 60 | UNIT_ID | 库存单位 | GUID | Y |  |
| 61 | UNIT_CODE | 库存单位编号 | string(8) | Y |  |
| 62 | UNIT_NAME | 库存单位名称 | string(20) | Y |  |
| 63 | UNIT2_ID | 第二单位 | GUID | Y |  |
| 64 | UNIT2_CODE | 第二单位编号 | string(8) | Y |  |
| 65 | UNIT2_NAME | 第二单位名称 | string(20) | Y |  |
| 66 | CURRENCY_ID | 币种 | GUID | Y |  |
| 67 | CURRENCY_CODE | 币种编号 | string(12) | Y |  |
| 68 | CURRENCY_NAME | 币种名称 | string(40) | Y |  |
| 69 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 70 | TYPE | 业务类型 | string(40) | Y |  |
| 71 | AVG_DELIVERY_DAYS | 平均交货天数 | number | Y |  |
| 72 | DELAY_DELIVERY_DAYS | 延迟交货天数 | number | Y |  |
| 73 | EARLY_DELIVERY_DAYS | 提早交货天数 | number | Y |  |
| 74 | YEAR | 年份 | number | Y |  |
| 75 | MONTH | 月份 | number | Y |  |
| 76 | CreateDate | 创建日期 | date | Y |  |
| 77 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 78 | ModifiedDate | 修改日期 | date | Y |  |
| 79 | CreateBy | 创建者 | GUID | Y |  |
| 80 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 81 | ModifiedBy | 修改者 | GUID | Y |  |
| 82 | Attachments | 附件 | string | Y |  |
| 83 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 84 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 85 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 86 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 87 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 88 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 89 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 90 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 91 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 92 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 93 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 94 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 95 | UDF041 | 自定义字段12 | date | Y |  |
| 96 | UDF042 | 自定义字段13 | date | Y |  |
| 97 | UDF051 | 自定义字段14 | GUID | Y |  |
| 98 | UDF052 | 自定义字段15 | GUID | Y |  |
| 99 | UDF053 | 自定义字段16 | GUID | Y |  |
| 100 | UDF054 | 自定义字段17 | GUID | Y |  |
| 101 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 102 | Version | 版本号，不要随意更改 | binary | Y |  |
| 103 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 104 | ApproveDate | 修改日期 | date | Y |  |
| 105 | ApproveBy | 修改人 | GUID | Y |  |
| 106 | Owner_Org_RTK |  | string(400) | Y |  |
| 107 | Owner_Org_ROid |  | GUID | Y |  |


### PURCHASE_FINANCE_INFO (采购出入库业务财务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PURCHASE_FINANCE_INFO_ID | 主键 | GUID | Y | Y |
| 4 | EMPLOYEE_ID | 业务员 | GUID | Y |  |
| 5 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 6 | PAYMENT_EMPLOYEE_ID | 付款业务员 | GUID | Y |  |
| 7 | PAYMENT_ADMIN_UNIT_ID | 付款业务部门 | GUID | Y |  |
| 8 | CURRENCY_ID | 货币 | GUID | Y |  |
| 9 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 10 | TAX_ID | 税种 | GUID | Y |  |
| 11 | ORDER_SUPPLIER_ID | 采购供应商 | GUID | Y |  |
| 12 | SETTLEMENT_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 13 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 14 | PRICE | 单价 | number(23,8) | Y |  |
| 15 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 16 | DICCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
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
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |
| 51 | SOURCE61_ID_RTK |  | string(400) | Y |  |
| 52 | SOURCE61_ID_ROid |  | GUID | Y |  |
| 53 | SOURCE611_ID_RTK |  | string(400) | Y |  |
| 54 | SOURCE611_ID_ROid |  | GUID | Y |  |
| 55 | SOURCE62_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE62_ID_ROid |  | GUID | Y |  |
| 57 | SOURCE621_ID_RTK |  | string(400) | Y |  |
| 58 | SOURCE621_ID_ROid |  | GUID | Y |  |
| 59 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 61 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 62 | SOURCE3_ID_ROid |  | GUID | Y |  |


### PURCHASE_GOODS (采购入库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | PURCHASE_GOODS_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | RECEIPT_DATE | 入库日期 | date | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | PLANT_ID | 储运机构 | GUID | Y |  |
| 11 | WAREHOUSE_ID | 盘点仓库 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 14 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 15 | POS_ID | POS机号 | GUID | Y |  |
| 16 | CLASS_ID | 班次 | number | Y |  |
| 17 | PrintCount | 打印次数 | number | Y |  |
| 18 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 19 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 20 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 21 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 57 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |


### PURCHASE_GOODS_D (采购入库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_GOODS_D_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | UNIT_ID | 物流单位 | GUID | Y |  |
| 8 | DILIVER_QTY | 配送数量 | number(16,6) | Y |  |
| 9 | QTY | 实收数量 | number(16,6) | Y |  |
| 10 | DIFFERENCE_QTY | 差异 | number(16,6) | Y |  |
| 11 | INVENTORY_QTY | 库存单位实收数量 | number(16,6) | Y |  |
| 12 | SECOND_QTY | 第二实收数量 | number(16,6) | Y |  |
| 13 | INVENTORY_D_QTY | 库存单位实收差异数量 | number(16,6) | Y |  |
| 14 | SECOND_D_QTY | 第二实收差异数量 | number(16,6) | Y |  |
| 15 | COST | 单位成本 | number(23,8) | Y |  |
| 16 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE_ID_ROid |  | GUID | Y |  |
| 45 | PURCHASE_GOODS_ID |  | GUID | Y |  |


### PURCHASE_ISSUE (采购退货出库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PURCHASE_ISSUE_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 10 | PIECES | 件数 | number | Y |  |
| 11 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 12 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 13 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 14 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 15 | COMPANY_ID | 公司 | GUID | Y |  |
| 16 | GLOB_ESTI_JE_INDICATOR | 已生成运营账簿暂估分录 | number(0/1) | Y |  |
| 17 | GLOB_ESTI_JE_ID | 运营账簿暂估分录 | GUID | Y |  |
| 18 | GLOB_COST_JE_INDICATOR | 已生成运营账簿成本分录 | number(0/1) | Y |  |
| 19 | GLOB_COST_JE_ID | 运营账簿成本分录 | GUID | Y |  |
| 20 | GLMB_ESTI_JE_INDICATOR | 已生成管理账簿暂估分录 | number(0/1) | Y |  |
| 21 | GLMB_ESTI_JE_ID | 管理账簿暂估分录 | GUID | Y |  |
| 22 | GLMB_COST_JE_INDICATOR | 已生成管理账簿成本分录 | number(0/1) | Y |  |
| 23 | GLMB_COST_JE_ID | 管理账簿成本分录 | GUID | Y |  |
| 24 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 25 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 26 | VIEW_DOC_NO | 显示单号 | string(40) | Y |  |
| 27 | SUM_BUSINESS_QTY | 业务数量合计 | number(16,6) | Y |  |
| 28 | PrintCount | 打印次数 | number | Y |  |
| 29 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 30 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 31 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 32 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 62 | Version | 版本号，不要随意更改 | binary | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |
| 65 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 66 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 67 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 68 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 69 | DOC_Sequence | 单据顺序 | number | Y |  |
| 70 | SOURCE_SUPPLIER_ID | 最终供应商 | GUID | Y |  |
| 71 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 72 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |


### PURCHASE_ISSUE_D (采购退货出库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ISSUE_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 11 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PIECES | 件数 | number | Y |  |
| 14 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 15 | AMOUNT_OC | 货款原币金额 | number(23,8) | Y |  |
| 16 | AMOUNT_BC | 货款本币金额 | number(23,8) | Y |  |
| 17 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 18 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 19 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 20 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 21 | SETTLEMENT_DIFF_AMT_BC | 当期结算差异调整本币金额 | number(23,8) | Y |  |
| 22 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 23 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 24 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 25 | SETTLEMENT_AMOUNT_OC | 已结算货款原币金额 | number(23,8) | Y |  |
| 26 | SETTLEMENT_AMOUNT_BC | 已结算货款本币金额 | number(23,8) | Y |  |
| 27 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 28 | PLAN_SETTLEMENT_DATE | 预计结算日 | date | Y |  |
| 29 | SETTLEMENT_BUSINESS_QTY | 已结算业务数量 | number(16,6) | Y |  |
| 30 | ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 31 | ESTIMATION_TIMES | 暂估次数 | number | Y |  |
| 32 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 33 | SYNERGY_D_ID | 协同关系序号 | GUID | Y |  |
| 34 | PACKING1_UNIT_ID | 大包裝單位 | GUID | Y |  |
| 35 | PACKING2_UNIT_ID | 中包裝單位 | GUID | Y |  |
| 36 | PACKING3_UNIT_ID | 小包裝單位 | GUID | Y |  |
| 37 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 38 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 39 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 40 | ITEM_ID | 品号 | GUID | Y |  |
| 41 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 42 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 43 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 44 | BIN_ID | 库位 | GUID | Y |  |
| 45 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 46 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 47 | SUPPLIER_IN_OUT | 已出库退领 | number(0/1) | Y |  |
| 48 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 49 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 50 | SETTLEMENT_AMT_UN_TAX_BC | 已结算本币未税金额 | number(23,8) | Y |  |
| 51 | SETTLEMENT_TAX_BC | 已结算本币税额 | number(23,8) | Y |  |
| 52 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 53 | SALES_RETURNED | 已内部销退 | number(0/1) | Y |  |
| 54 | SYNERGY_TYPE | 协同关系类型 | number | Y |  |
| 55 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 56 | RE_SETTLEMENT_PATH_TYPE | 退货结算路径类型 | number | Y |  |
| 57 | SETTLEMENT_START_INDICATOR | 结算起点 | number(0/1) | Y |  |
| 58 | PROJECT_ID | 项目 | GUID | Y |  |
| 59 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 60 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 61 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 62 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | CreateDate | 创建日期 | date | Y |  |
| 67 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 68 | ModifiedDate | 修改日期 | date | Y |  |
| 69 | CreateBy | 创建者 | GUID | Y |  |
| 70 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 71 | ModifiedBy | 修改者 | GUID | Y |  |
| 72 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 73 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 74 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 75 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 76 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 77 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 78 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 79 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 80 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 81 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 82 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 83 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 84 | UDF041 | 自定义字段12 | date | Y |  |
| 85 | UDF042 | 自定义字段13 | date | Y |  |
| 86 | UDF051 | 自定义字段14 | GUID | Y |  |
| 87 | UDF052 | 自定义字段15 | GUID | Y |  |
| 88 | UDF053 | 自定义字段16 | GUID | Y |  |
| 89 | UDF054 | 自定义字段17 | GUID | Y |  |
| 90 | Version | 版本号，不要随意更改 | binary | Y |  |
| 91 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 92 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
| 93 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 94 | SOURCE_ID_ROid |  | GUID | Y |  |
| 95 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 96 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 97 | ORDER_SOURCE_ID_RTK |  | string(400) | Y |  |
| 98 | ORDER_SOURCE_ID_ROid |  | GUID | Y |  |
| 99 | PURCHASE_ISSUE_ID |  | GUID | Y |  |
| 100 | TO_ASSET_STATUS | 转资状态 | number | Y |  |
| 101 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 102 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 103 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 104 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 105 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 106 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 107 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 108 | SYNERGY_SETTLEMENT_GROUP | 协同结算组号 | number | Y |  |
| 109 | TO_ASSET_SOURCE_ID_RTK |  | string(400) | Y |  |
| 110 | TO_ASSET_SOURCE_ID_ROid |  | GUID | Y |  |
| 111 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 112 | SOURCE_ORDER_ROid |  | GUID | Y |  |


### PURCHASE_ORDER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PURCHASE_ORDER_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PURCHASE_DATE | 订单日期 | date | Y |  |
| 9 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 10 | SUPPLIER_CONTACT_NAME | 供应商联系人 | string(72) | Y |  |
| 11 | SUPPLIER_ADDR_NAME | 供应商地址 | string(510) | Y |  |
| 12 | EXCHANGE_RATE | 匯率 | number(18,9) | Y |  |
| 13 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 14 | MULTI_PLANT | 多收货工厂 | number(0/1) | Y |  |
| 15 | DELIVERY_CONTACT_NAME | 发货联系人 | string(72) | Y |  |
| 16 | DELIVERY_ADDR_NAME | 发货地址 | string(510) | Y |  |
| 17 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 18 | INVOICE_CONTACT_NAME | 结算联系人 | string(72) | Y |  |
| 19 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 20 | SUPPLIER_ORDER_NO | 供应商单号 | string(510) | Y |  |
| 21 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 22 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 23 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 24 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 27 | DIRECT_SHIPMENT | 供应商直运 | number(0/1) | Y |  |
| 28 | INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 29 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 30 | EARNEST | 订金 | number(23,8) | Y |  |
| 31 | EARNEST_RATE |  | number(5,4) | Y |  |
| 32 | EARNEST_SETTLEMENT_TYPE | 订金结算方式 | string(40) | Y |  |
| 33 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 34 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算无税金额(原币) | number(23,8) | Y |  |
| 35 | PRE_SETTLEMENT_TAX_OC | 预结算税额（原币） | number(23,8) | Y |  |
| 36 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 37 | COMPANY_ID | 订单公司 | GUID | Y |  |
| 38 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 39 | SUPPLIER_CONTACT_ID | 联系人编码 | GUID | Y |  |
| 40 | SUPPLIER_ADDR_ID | 地址编码 | GUID | Y |  |
| 41 | CURRENCY_ID | 币种 | GUID | Y |  |
| 42 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 43 | PLANT_ID | 收货工厂 | GUID | Y |  |
| 44 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 45 | DELIVERY_CONTACT_ID | 发货联系人编码 | GUID | Y |  |
| 46 | DELIVERY_ADDR_ID | 发货地址编码 | GUID | Y |  |
| 47 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 48 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 49 | INVOICE_CONTACT_ID | 结算联系人编码 | GUID | Y |  |
| 50 | INVOICE_ADDR_ID | 结算地址编码 | GUID | Y |  |
| 51 | PURCHASE_CONTRACT_ID | 采购合同 | GUID | Y |  |
| 52 | TAX_ID | 税种 | GUID | Y |  |
| 53 | OFFSETED_AMT_UN_TAX_OC | 已冲减原币未税金额 | number(23,8) | Y |  |
| 54 | OFFSETED_TAX_OC | 已冲减原币税额 | number(23,8) | Y |  |
| 55 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 56 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 57 | RECEIPTED_AMT_UN_TAX_OC | 需结算已入库原币未税金额 | number(23,8) | Y |  |
| 58 | RECEIPTED_TAX_OC | 需结算已入库原币税额 | number(23,8) | Y |  |
| 59 | PLANT_ADDRESS | 收货地址 | string(510) | Y |  |
| 60 | PIECES | 件数 | number | Y |  |
| 61 | UNSETTLE_POFFSET_AMT_UN_TAX_OC | 未结算预冲减原币未税金额 | number(23,8) | Y |  |
| 62 | UNSETTLE_POFFSET_TAX_OC | 未结算预冲减原币税额 | number(23,8) | Y |  |
| 63 | UNSETTLE_ARR_AMT_UN_TAX_OC | 未结算已到货原币未税金额 | number(23,8) | Y |  |
| 64 | UNSETTLE_ARR_TAX_OC | 未结算已到货原币税额 | number(23,8) | Y |  |
| 65 | SUPPLY_SYNERGY_ID | 供应协同关系 | GUID | Y |  |
| 66 | CLOSE | 结束码 | string(40) | Y |  |
| 67 | WIP_NO | WIP集成抛转传入ID | string(40) | Y |  |
| 68 | PROJECT_ID | 限用项目 | GUID | Y |  |
| 69 | PrintCount | 打印次数 | number | Y |  |
| 70 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 71 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 72 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 73 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 74 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 75 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 76 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 77 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 78 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 79 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 80 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 81 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 82 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 83 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 84 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 85 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 86 | UDF041 | 自定义字段12 | date | Y |  |
| 87 | UDF042 | 自定义字段13 | date | Y |  |
| 88 | UDF051 | 自定义字段14 | GUID | Y |  |
| 89 | UDF052 | 自定义字段15 | GUID | Y |  |
| 90 | UDF053 | 自定义字段16 | GUID | Y |  |
| 91 | UDF054 | 自定义字段17 | GUID | Y |  |
| 92 | CreateDate | 创建日期 | date | Y |  |
| 93 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 94 | ModifiedDate | 修改日期 | date | Y |  |
| 95 | CreateBy | 创建者 | GUID | Y |  |
| 96 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 97 | ModifiedBy | 修改者 | GUID | Y |  |
| 98 | Attachments | 附件 | string | Y |  |
| 99 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 100 | Version | 版本号，不要随意更改 | binary | Y |  |
| 101 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 102 | ApproveDate | 修改日期 | date | Y |  |
| 103 | ApproveBy | 修改人 | GUID | Y |  |
| 104 | Owner_Org_RTK |  | string(400) | Y |  |
| 105 | Owner_Org_ROid |  | GUID | Y |  |
| 106 | REV_ORG_SOURCE_ID_RTK |  | string(400) | Y |  |
| 107 | REV_ORG_SOURCE_ID_ROid |  | GUID | Y |  |
| 108 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 109 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 110 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 111 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 112 | DOC_Sequence | 单据顺序 | number | Y |  |
| 113 | SOURCE_SUPPLIER_ID | 最终供应商 | GUID | Y |  |
| 114 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 115 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |
| 116 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 117 | SOURCE_ORDER_ROid |  | GUID | Y |  |


### PURCHASE_ORDER_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ORDER_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 7 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 12 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 13 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 14 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 15 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 16 | PRICE | 单价 | number(23,8) | Y |  |
| 17 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 18 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 19 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 20 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 21 | AMOUNT | 金额 | number(23,8) | Y |  |
| 22 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 23 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 24 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 25 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 26 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 27 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 28 | MULTI_ARRIVAL_DATE | 多交期 | number(0/1) | Y |  |
| 29 | MANUFACTURER | 品牌信息 | string(510) | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 32 | TRANSFER_GENERATE | 移转生成 | number(0/1) | Y |  |
| 33 | PRE_SETTLEMENT_PRICE_QTY | 预结算计价数量 | number(16,6) | Y |  |
| 34 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 35 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 36 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算无税金额(原币) | number(23,8) | Y |  |
| 37 | PRE_SETTLEMENT_TAX_OC | 预结算税额(原币) | number(23,8) | Y |  |
| 38 | RECEIPTED_PRICE_QTY | 需结算已入库计价数量 | number(16,6) | Y |  |
| 39 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额(原币) | number(23,8) | Y |  |
| 40 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 41 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 42 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 43 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 44 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 45 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 46 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 47 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 48 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 49 | TAX_ID | 税种 | GUID | Y |  |
| 50 | ITEM_CERTIFICATION_D_ID | 认可文号 | GUID | Y |  |
| 51 | OPERATION_ID | 工艺 | GUID | Y |  |
| 52 | OFFSETED_PRICE_QTY | 已冲减计价数量 | number(16,6) | Y |  |
| 53 | PIECES | 件数 | number | Y |  |
| 54 | DIRECT_SUPPLY | 直供 | number(0/1) | Y |  |
| 55 | PROJECT_ID | 项目 | GUID | Y |  |
| 56 | ORDER_PIC | 订单图片 | string(4000) | Y |  |
| 57 | WIP_DOCNO | WIP/MES集成移转单单号序号 | string(50) | Y |  |
| 58 | SUPPLY_DATE | 预计入库日 | date | Y |  |
| 59 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 60 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 61 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 62 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 63 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 64 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 65 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 66 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 67 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 68 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 69 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 70 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 71 | UDF041 | 自定义字段12 | date | Y |  |
| 72 | UDF042 | 自定义字段13 | date | Y |  |
| 73 | UDF051 | 自定义字段14 | GUID | Y |  |
| 74 | UDF052 | 自定义字段15 | GUID | Y |  |
| 75 | UDF053 | 自定义字段16 | GUID | Y |  |
| 76 | UDF054 | 自定义字段17 | GUID | Y |  |
| 77 | CreateDate | 创建日期 | date | Y |  |
| 78 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 79 | ModifiedDate | 修改日期 | date | Y |  |
| 80 | CreateBy | 创建者 | GUID | Y |  |
| 81 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 82 | ModifiedBy | 修改者 | GUID | Y |  |
| 83 | Version | 版本号，不要随意更改 | binary | Y |  |
| 84 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 85 | ApproveDate | 修改日期 | date | Y |  |
| 86 | ApproveBy | 修改人 | GUID | Y |  |
| 87 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 88 | SOURCE_ID_ROid |  | GUID | Y |  |
| 89 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 90 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 91 | PURCHASE_ORDER_ID |  | GUID | Y |  |
| 92 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 93 | SOURCE_ORDER_ROid |  | GUID | Y |  |


### PURCHASE_ORDER_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ORDER_SD_ID | 主键 | GUID | Y | Y |
| 3 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 4 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 5 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 9 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 13 | PIECES | 件数 | number | Y |  |
| 14 | RECEIPTED_BUSINESS_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 15 | RECEIPTED_PRICE_QTY | 已入库计价数量 | number(16,6) | Y |  |
| 16 | RECEIPT_CLOSE | 入库结束码 | string(40) | Y |  |
| 17 | CHECKOUT_QTY | 结账数量 | number(16,6) | Y |  |
| 18 | CHCKOUT_AMT | 结账金额 | number(23,8) | Y |  |
| 19 | CHECKOUT_CLOSE | 结账结束码 | number(0/1) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | SUPPLY_SYNERGY_ID | 供应协同关系 | GUID | Y |  |
| 22 | PLANT_ID | 收货工厂 | GUID | Y |  |
| 23 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 24 | PLANT_ADDRESS | 收货地址 | string(510) | Y |  |
| 25 | ARRIVED_BUSINESS_QTY | 已到货业务数量 | number(16,6) | Y |  |
| 26 | ARRIVED_PRICE_QTY | 已到货计价数量 | number(16,6) | Y |  |
| 27 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 28 | PROJECT_ID | 项目 | GUID | Y |  |
| 29 | SUPPLY_DATE | 预计入库日 | date | Y |  |
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
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE_ID_ROid |  | GUID | Y |  |
| 60 | RECEIVE_Owner_Org_RTK |  | string(400) | Y |  |
| 61 | RECEIVE_Owner_Org_ROid |  | GUID | Y |  |
| 62 | SO_SOURCE_ID_RTK |  | string(400) | Y |  |
| 63 | SO_SOURCE_ID_ROid |  | GUID | Y |  |
| 64 | PURCHASE_ORDER_D_ID |  | GUID | Y |  |
| 65 | AMOUNT | 金额 | number(23,8) | Y |  |
| 66 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 67 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 68 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 69 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 70 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 71 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 72 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 73 | INCLUDE_PLAN | 纳入计划 | number(0/1) | Y |  |
| 74 | TRANSACTION_PLANT_ID | 交易工厂 | GUID | Y |  |


### PURCHASE_ORDER_SD1

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ORDER_SD1_ID | 主键 | GUID | Y | Y |
| 3 | DEMAND_QTY | 需求业务数量 | number(16,6) | Y |  |
| 4 | DEMAND_UNIT_ID | 需求业务单位 | GUID | Y |  |
| 5 | DEMAND_DATE | 需求日期 | date | Y |  |
| 6 | PURCHASED_QTY | 已采业务数量 | number(16,6) | Y |  |
| 7 | ARRIVED_QTY | 已到货业务数量 | number(16,6) | Y |  |
| 8 | RECEIPTED_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 9 | PURCHASE_SEQUENCE | 采购核销优先序 | string(400) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | DEMAND_NO | 需求单号 | string(8000) | Y |  |
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
| 40 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ID_ROid |  | GUID | Y |  |
| 42 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 44 | PURCHASE_ORDER_D_ID |  | GUID | Y |  |


### PURCHASE_ORDER_SSD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ORDER_SSD_ID | 主键 | GUID | Y | Y |
| 3 | DEMAND_QTY | 业务数量 | number(16,6) | Y |  |
| 4 | DEMAND_UNIT_ID | 业务单位 | GUID | Y |  |
| 5 | DEMAND_DATE | 需求日期 | date | Y |  |
| 6 | PURCHASED_QTY | 已采业务数量 | number(16,6) | Y |  |
| 7 | ARRIVED_QTY | 已到货业务数量 | number(16,6) | Y |  |
| 8 | RECEIPTED_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 9 | PURCHASE_SEQUENCE | 采购核销顺序 | number | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | DEMAND_NO | 参考单号 | string(8000) | Y |  |
| 12 | PLAN_ARRIVAL_DATE | 收货信息预到货日 | date | Y |  |
| 13 | REQUISITION_D_DATE | 请购单单身需求日期 | date | Y |  |
| 14 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 15 | LOCKED_FLAG | 供需关连锁定 | number(0/1) | Y |  |
| 16 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 17 | PLAN_SHIP_DATE1 | 销售订单预发货日 | date | Y |  |
| 18 | ARRIVED_INV_QTY | 已到货库存单位数量 | number(16,6) | Y |  |
| 19 | RECEIPTED_INV_QTY | 已入库库存单位数量 | number(16,6) | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 52 | PURCHASE_ORDER_SD_ID |  | GUID | Y |  |


### PURCHASE_RECEIPT (采购入库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | PURCHASE_RECEIPT_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | PIECES | 件数 | number | Y |  |
| 11 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 12 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 13 | SUPPLIER_ARRIVAL_ID | 厂供料到货单 | GUID | Y |  |
| 14 | WAREHOUSE_ID | 限定入库仓库 | GUID | Y |  |
| 15 | SUPPLIER_RECEIPT_ID | 厂供料入库单 | GUID | Y |  |
| 16 | SUPPLIER_ISSUE_RECEIPT_ID | 厂供料领用单 | GUID | Y |  |
| 17 | COMPANY_ID | 公司 | GUID | Y |  |
| 18 | GLOB_ESTI_JE_INDICATOR | 已生成运营账簿暂估分录 | number(0/1) | Y |  |
| 19 | GLOB_COST_JE_INDICATOR | 已生成运营账簿成本分录 | number(0/1) | Y |  |
| 20 | GLMB_ESTI_JE_INDICATOR | 已生成管理账簿暂估分录 | number(0/1) | Y |  |
| 21 | GLMB_COST_JE_INDICATOR | 已生成管理账簿成本分录 | number(0/1) | Y |  |
| 22 | GLOB_ESTI_JE_ID | 运营账簿暂估分录 | GUID | Y |  |
| 23 | GLOB_COST_JE_ID | 运营账簿成本分录 | GUID | Y |  |
| 24 | GLMB_ESTI_JE_ID | 管理账簿暂估分录 | GUID | Y |  |
| 25 | GLMB_COST_JE_ID | 管理账簿成本分录 | GUID | Y |  |
| 26 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 27 | VIEW_DOC_NO | 显示单号 | string(40) | Y |  |
| 28 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 29 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 30 | SUM_BUSINESS_QTY | 业务数量合计 | number(16,6) | Y |  |
| 31 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 32 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 33 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 34 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 44 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 45 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 46 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 47 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 48 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 49 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 50 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 51 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 52 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 53 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 54 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 55 | UDF041 | 自定义字段12 | date | Y |  |
| 56 | UDF042 | 自定义字段13 | date | Y |  |
| 57 | UDF051 | 自定义字段14 | GUID | Y |  |
| 58 | UDF052 | 自定义字段15 | GUID | Y |  |
| 59 | UDF053 | 自定义字段16 | GUID | Y |  |
| 60 | UDF054 | 自定义字段17 | GUID | Y |  |
| 61 | Version | 版本号，不要随意更改 | binary | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | PrintCount | 打印次数 | number | Y |  |
| 66 | Owner_Org_RTK |  | string(400) | Y |  |
| 67 | Owner_Org_ROid |  | GUID | Y |  |
| 68 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 69 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 70 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 71 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 72 | DOC_Sequence | 单据顺序 | number | Y |  |
| 73 | SOURCE_SUPPLIER_ID | 最终供应商 | GUID | Y |  |
| 74 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 75 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |


### PURCHASE_RECEIPT_D (采购入库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_RECEIPT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 12 | PIECES | 件数 | number | Y |  |
| 13 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | ESTIMATION_TIMES | 暂估次数 | number | Y |  |
| 16 | AMOUNT_UN_TAX_OC | 货款原币金额 | number(23,8) | Y |  |
| 17 | AMOUNT_UN_TAX_BC | 货款本币金额 | number(23,8) | Y |  |
| 18 | PLAN_SETTLEMENT_DATE | 预计结算日 | date | Y |  |
| 19 | SETTLEMENT_BUSINESS_QTY | 已结算业务数量 | number(16,6) | Y |  |
| 20 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 21 | SETTLEMENT_AMT_UN_OC | 已结算货款原币金额 | number(23,8) | Y |  |
| 22 | SETTLEMENT_AMT_UN_BC | 已结算货款本币金额 | number(23,8) | Y |  |
| 23 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 24 | SETTLEMENT_DIFF_AMT_BC | 当期结算差异调整本币金额 | number(23,8) | Y |  |
| 25 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 26 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 27 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 28 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 29 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 30 | ITEM_ID | 品号 | GUID | Y |  |
| 31 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 32 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 33 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 34 | BIN_ID | 库位 | GUID | Y |  |
| 35 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 36 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 37 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 38 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 39 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 40 | SOURCE_ID | 源单ID | GUID | Y |  |
| 41 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 42 | SYNERGY_D_ID | 协同序号ID | GUID | Y |  |
| 43 | ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 44 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 45 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 46 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 47 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 48 | SUPPLIER_IN_OUT | 已入库领用 | number(0/1) | Y |  |
| 49 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 50 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 51 | SETTLEMENT_AMT_UN_TAX_BC | 已结算本币未税金额 | number(23,8) | Y |  |
| 52 | SETTLEMENT_TAX_BC | 已结算本币金额 | number(23,8) | Y |  |
| 53 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 54 | SYNERGY_TYPE | 协同关系类型 | number | Y |  |
| 55 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 56 | RE_SETTLEMENT_PATH_TYPE | 退货结算路径类型 | number | Y |  |
| 57 | SETTLEMENT_START_INDICATOR | 结算起点 | number(0/1) | Y |  |
| 58 | PROJECT_ID | 项目 | GUID | Y |  |
| 59 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 60 | DEDUCT_ARRIVED_QTY | 扣已到货量 | number(0/1) | Y |  |
| 61 | SCRAP_BUSINESS_QTY | 报废业务数量 | number(16,6) | Y |  |
| 62 | RETURN_BUSINESS_QTY | 拒收业务数量 | number(16,6) | Y |  |
| 63 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 64 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 65 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 66 | CreateDate | 创建日期 | date | Y |  |
| 67 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 68 | ModifiedDate | 修改日期 | date | Y |  |
| 69 | CreateBy | 创建者 | GUID | Y |  |
| 70 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 71 | ModifiedBy | 修改者 | GUID | Y |  |
| 72 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 73 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 74 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 75 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 76 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 77 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 78 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 79 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 80 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 81 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 82 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 83 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 84 | UDF041 | 自定义字段12 | date | Y |  |
| 85 | UDF042 | 自定义字段13 | date | Y |  |
| 86 | UDF051 | 自定义字段14 | GUID | Y |  |
| 87 | UDF052 | 自定义字段15 | GUID | Y |  |
| 88 | UDF053 | 自定义字段16 | GUID | Y |  |
| 89 | UDF054 | 自定义字段17 | GUID | Y |  |
| 90 | Version | 版本号，不要随意更改 | binary | Y |  |
| 91 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 92 | ApproveDate | 修改日期 | date | Y |  |
| 93 | ApproveBy | 修改人 | GUID | Y |  |
| 94 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 95 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
| 96 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 97 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 98 | ORDER_SOURCE_ID_RTK |  | string(400) | Y |  |
| 99 | ORDER_SOURCE_ID_ROid |  | GUID | Y |  |
| 100 | PURCHASE_RECEIPT_ID |  | GUID | Y |  |
| 101 | TO_ASSET_STATUS | 转资状态 | number | Y |  |
| 102 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 103 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 104 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 105 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 106 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 107 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 108 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 109 | SYNERGY_SETTLEMENT_GROUP | 协同结算组号 | number | Y |  |
| 110 | TO_ASSET_SOURCE_ID_RTK |  | string(400) | Y |  |
| 111 | TO_ASSET_SOURCE_ID_ROid |  | GUID | Y |  |
| 112 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 113 | SOURCE_ORDER_ROid |  | GUID | Y |  |


### PURCHASE_REJECT_RETURN (维护拒收退货单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PURCHASE_REJECT_RETURN_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_DATE | 退货日期 | date | Y |  |
| 9 | SUPPLIER_ADDR_NAME | 供应商地址 | string(510) | Y |  |
| 10 | RETURN_MODE | 退货方式 | string(510) | Y |  |
| 11 | RETURN_REASON | 退货说明 | string(510) | Y |  |
| 12 | PIECES | 件数 | number | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | SUPPLIER_ADDR_ID | 供应商地址ID | GUID | Y |  |
| 15 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 16 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 17 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 18 | PrintCount | 打印次数 | number | Y |  |
| 19 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 20 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 21 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 22 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 48 | Attachments | 附件 | string | Y |  |
| 49 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Owner_Org_RTK |  | string(400) | Y |  |
| 54 | Owner_Org_ROid |  | GUID | Y |  |


### PURCHASE_REJECT_RETURN_D (维护拒收退货单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_REJECT_RETURN_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | ITEM_TYPE | 商品类型 | string(120) | Y |  |
| 6 | PIECES | 件数 | number | Y |  |
| 7 | CLOSE | 结束码 | string(40) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | ITEM_ID | 品号 | GUID | Y |  |
| 10 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 11 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 12 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 13 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 14 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 15 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 16 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 17 | PACKING_QTY | 包装数量描述 | string(80) | Y |  |
| 18 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 20 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 21 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 22 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 23 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 24 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 25 | PROJECT_ID | 项目 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | ORDER_SOURCE_ID_RTK |  | string(400) | Y |  |
| 57 | ORDER_SOURCE_ID_ROid |  | GUID | Y |  |
| 58 | PURCHASE_REJECT_RETURN_ID |  | GUID | Y |  |


### PURCHASE_RETURN (采购退货单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PURCHASE_RETURN_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_DATE | 退货日期 | date | Y |  |
| 9 | SUPPLIER_CONTACT_NAME | 联系人 | string(72) | Y |  |
| 10 | SUPPLIER_ADDR_NAME |  | string(510) | Y |  |
| 11 | EXCHANGE_RATE | 匯率 | number(18,9) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | INVOICE_CONTACT_NAME | 结算联系人 | string(72) | Y |  |
| 14 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 15 | RETURN_MODE | 退货方式 | string(510) | Y |  |
| 16 | RETURN_REASON | 退货说明 | string(510) | Y |  |
| 17 | PIECES |  | number | Y |  |
| 18 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 19 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 20 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 21 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 24 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 25 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 26 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 27 | SUPPLIER_CONTACT_ID | 联系人编号 | GUID | Y |  |
| 28 | SUPPLIER_ADDR_ID | 地址编号 | GUID | Y |  |
| 29 | CURRENCY_ID | 币种 | GUID | Y |  |
| 30 | PAYMENT_TERM_ID |  | GUID | Y |  |
| 31 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 32 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 33 | INVOICE_CONTACT_ID | 结算联系人编号 | GUID | Y |  |
| 34 | INVOICE_ADDR_ID | 结算地址编号 | GUID | Y |  |
| 35 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 36 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 37 | SYNERGY_ID |  | GUID | Y |  |
| 38 | SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 39 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 40 | ISSUE_STATUS | 出库状态 | string(40) | Y |  |
| 41 | SETTLEMENT_INDICATOR | 当前可结算 | number(0/1) | Y |  |
| 42 | DIRECT_INVOICING_INDICATOR | 随货附票 | number(0/1) | Y |  |
| 43 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 44 | TAX_ID | 税种 | GUID | Y |  |
| 45 | WIP_NO | WIP集成传入抛转ID | string(40) | Y |  |
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
| 64 | PrintCount | 打印次数 | number | Y |  |
| 65 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 66 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 67 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 68 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 69 | CreateDate | 创建日期 | date | Y |  |
| 70 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 71 | ModifiedDate | 修改日期 | date | Y |  |
| 72 | CreateBy | 创建者 | GUID | Y |  |
| 73 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 74 | ModifiedBy | 修改者 | GUID | Y |  |
| 75 | Version | 版本号，不要随意更改 | binary | Y |  |
| 76 | Attachments | 附件 | string | Y |  |
| 77 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |
| 81 | Owner_Org_RTK |  | string(400) | Y |  |
| 82 | Owner_Org_ROid |  | GUID | Y |  |
| 83 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 84 | SOURCE_ID_ROid |  | GUID | Y |  |
| 85 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 86 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 87 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 88 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 89 | DOC_Sequence | 单据顺序 | number | Y |  |
| 90 | SOURCE_SUPPLIER_ID | 最终供应商 | GUID | Y |  |
| 91 | AFTER_ROUTING_RETURN | 后道退回 | number(0/1) | Y |  |
| 92 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 93 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |


### PURCHASE_RETURN_D (采购退货单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_RETURN_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 6 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 7 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 11 | PIECES |  | number | Y |  |
| 12 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 13 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 14 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 15 | PRICE | 單價 | number(23,8) | Y |  |
| 16 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 17 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 18 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 19 | TAX_RATE |  | number(5,4) | Y |  |
| 20 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 21 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 22 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 23 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 24 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 25 | AMOUNT |  | number(23,8) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | DEDUCT_RECEIPTED_QTY | 扣已入库量 | number(0/1) | Y |  |
| 28 | ISSUE_CLOSE | 出库结束码 | string(40) | Y |  |
| 29 | ISSUED_BUSINESS_QTY | 已出库业务数量 | number(16,6) | Y |  |
| 30 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 31 | SETTLEMENT_AMT_UN_TAX_BC | 已结算本币未税金额 | number(23,8) | Y |  |
| 32 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 33 | SETTLEMENT_TAX_BC | 已结算本币税额 | number(23,8) | Y |  |
| 34 | SALES_RETURNED | 已内部销退 | number(0/1) | Y |  |
| 35 | ITEM_ID | 品号 | GUID | Y |  |
| 36 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 37 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 38 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 39 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 40 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 41 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 42 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 43 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 44 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 45 | TAX_ID | 税种 | GUID | Y |  |
| 46 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 47 | BIN_ID |  | GUID | Y |  |
| 48 | ITEM_LOT_ID |  | GUID | Y |  |
| 49 | MO_ID | 工单ID | GUID | Y |  |
| 50 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 51 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 52 | PROJECT_ID | 项目 | GUID | Y |  |
| 53 | SN_COLLECTED_QTY | 序列号已采集量 | number(16,6) | Y |  |
| 54 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 55 | WIP_DOCNO | WIP集成移转单单号序号 | string(50) | Y |  |
| 56 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 57 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 58 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 59 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 60 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 61 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 62 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 63 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 64 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 65 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 66 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 67 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 68 | UDF041 | 自定义字段12 | date | Y |  |
| 69 | UDF042 | 自定义字段13 | date | Y |  |
| 70 | UDF051 | 自定义字段14 | GUID | Y |  |
| 71 | UDF052 | 自定义字段15 | GUID | Y |  |
| 72 | UDF053 | 自定义字段16 | GUID | Y |  |
| 73 | UDF054 | 自定义字段17 | GUID | Y |  |
| 74 | CreateDate | 创建日期 | date | Y |  |
| 75 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 76 | ModifiedDate | 修改日期 | date | Y |  |
| 77 | CreateBy | 创建者 | GUID | Y |  |
| 78 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 79 | ModifiedBy | 修改者 | GUID | Y |  |
| 80 | Version | 版本号，不要随意更改 | binary | Y |  |
| 81 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 82 | ApproveDate | 修改日期 | date | Y |  |
| 83 | ApproveBy | 修改人 | GUID | Y |  |
| 84 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 85 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 86 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 87 | SOURCE_ID_ROid |  | GUID | Y |  |
| 88 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 89 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 90 | PURCHASE_RETURN_ID |  | GUID | Y |  |
| 91 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 92 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 93 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 94 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 95 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 96 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 97 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 98 | TO_ASSET_SOURCE_ID_RTK |  | string(400) | Y |  |
| 99 | TO_ASSET_SOURCE_ID_ROid |  | GUID | Y |  |
| 100 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 101 | SOURCE_ORDER_ROid |  | GUID | Y |  |
| 102 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 103 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
