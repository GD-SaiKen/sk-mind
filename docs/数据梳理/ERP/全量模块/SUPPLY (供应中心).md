---
module: "SUPPLY"
name_zh: "供应中心"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 284
category: purchase
tags: ["ERP", "E10", "purchase"]
created: 2026-06-25 10:52
---

# SUPPLY (供应中心)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 284

## Related Modules

- [[IMPORT (进口管理)|IMPORT (进口管理)]]
- [[NEGOTIATE (议价管理)|NEGOTIATE (议价管理)]]
- [[PO (采购订单)|PO (采购订单)]]
- [[PURCHASE (采购管理)|PURCHASE (采购管理)]]
- [[REQUISITION (请购管理)|REQUISITION (请购管理)]]
- [[SUPPLIER (供应商)|SUPPLIER (供应商)]]

---

## Tables


- **SUPPLY_CENTER (采购域信息)**
- **SUPPLY_CENTER_DEPT (采购域采购部门信息)**
- **SUPPLY_CENTER_PLANT (采购域服务工厂/储运信息)**
- **SUPPLY_SYNERGY (供应协同关系信息)**
- **SUPPLY_SYNERGY_FI_D (供应协同结算路径明细)**
- **SUPPLY_SYNERGY_SD (供应协同关系信息)**


---


---


> Tables: 6

### SUPPLY_CENTER (采购域信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SUPPLY_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | SUPPLY_CENTER_CODE | 采购域编号 | string(40) | Y |  |
| 5 | SUPPLY_CENTER_NAME | 采购域名称 | string(40) | Y |  |
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

### SUPPLY_CENTER_DEPT (采购域采购部门信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SUPPLY_CENTER_DEPT_ID | 主键 | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | MAIN | 默认 | number(0/1) | Y |  |
| 4 | BUYER_ID | 业务员 | GUID | Y |  |
| 5 | DEPARTMENT_ID | 部门 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | SUPPLY_CENTER_ID |  | GUID | Y |  |

### SUPPLY_CENTER_PLANT (采购域服务工厂/储运信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SUPPLY_CENTER_PLANT_ID | 主键 | GUID | Y | Y |
| 2 | MAIN | 主要 | number(0/1) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 5 | INVOICE_COMPANY_ID | 默认结算公司 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | SUPPLY_CENTER_ID |  | GUID | Y |  |

### SUPPLY_SYNERGY (供应协同关系信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SUPPLY_SYNERGY_ID | 主键 | GUID | Y | Y |
| 4 | SUPPLY_SYNERGY_CODE | 协同关系编号 | string(20) | Y |  |
| 5 | SUPPLY_SYNERGY_NAME | 协同关系名称 | string(40) | Y |  |
| 6 | SUPPLY_TYPE | 供应协同类型 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | REQUIRE_PLANT_ID | 需求工厂/储运 | GUID | Y |  |
| 9 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 10 | DELIVERY_PLANT_ID | 发货工厂/储运 | GUID | Y |  |
| 11 | INNER_ORDER_DOC_ID | 内部订单单据类型 | GUID | Y |  |
| 12 | MAIN | 主要 | number(0/1) | Y |  |
| 13 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 14 | SETTLEMENT_SOURCE | 一段式立账发起方 | number | Y |  |
| 15 | INDEPENDENT_SETTLEMENT | 结算公司对外独立立账 | number(0/1) | Y |  |
| 16 | PAYABLE_DOC_ID | 结算公司应付单类型 | GUID | Y |  |
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
| 49 | REQUIRE_Owner_Org_RTK |  | string(400) | Y |  |
| 50 | REQUIRE_Owner_Org_ROid |  | GUID | Y |  |
| 51 | GENERATE_DIRE | 抛转方向 | string(400) | Y |  |
| 52 | GENERATE_AUTO | 自动抛转 | number(0/1) | Y |  |
| 53 | CLIENT_ISSUE_RECEIPT_DOC_ID | 需求方(委托方)领料单别 | GUID | Y |  |
| 54 | PRODUCER_MO_DOC_ID | 发货方(生产方)工单单别 | GUID | Y |  |
| 55 | MATERIAL_FEES_INCLUDE | 供应商供料价格纳入委外加工费 | number(0/1) | Y |  |
| 56 | CLIENT_WAREHOUSE_INV_ID | 主键 | GUID | Y |  |
| 57 | CLIENT_WAREHOUSE_NON_INV_ID | 主键 | GUID | Y |  |
| 58 | PRODUCER_WAREHOUSE_INV_ID | 主键 | GUID | Y |  |
| 59 | CLIENT_TRANSFER_DOC_ID | 需求方(委托方)调拨单单别 | GUID | Y |  |
| 60 | PRODUCER_MORECEIPT_DOC_ID | 发货方(生产方)入库单单别 | GUID | Y |  |
| 61 | PRODUCER_ISSUERECEIPT_DOC_ID | 发货方(生产方)出库单单别 | GUID | Y |  |
| 62 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 63 | OUT_PA_ID | 对外到货单 | GUID | Y |  |
| 64 | OUT_PR_ID | 对外采购退货单 | GUID | Y |  |
| 65 | CLIENT_ISSUE_RETURN_DOC_ID | 需求方(委托方)退料单别 | GUID | Y |  |
| 66 | PRODUCER_REMO_DOC_ID | 发货方(生产方)重工工单单别 | GUID | Y |  |
| 67 | TRANSFER_REQUISITION_ID | 调拨申请单单别 | GUID | Y |  |
| 68 | ITEM_CODE_KEEP | 工艺委外生产方品号同委托方主件品号 | number(0/1) | Y |  |
| 69 | MO_RECEIPT_AUTO_SD_PA | 生产入库自动生成销货到货单 | number(0/1) | Y |  |
| 70 | SALES_DELIVERY_DOC_ID | 销货单据类型 | GUID | Y |  |
| 71 | PURCHASE_ARRIVAL_DOC_ID | 到货单据类型 | GUID | Y |  |
| 72 | GROUP_SYNERGY_TYPE | 集团内委外类型 | string(40) | Y |  |

### SUPPLY_SYNERGY_FI_D (供应协同结算路径明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SUPPLY_SYNERGY_FI_D_ID | 主键 | GUID | Y | Y |
| 3 | PRICE_RATE | 比例 | number(5,4) | Y |  |
| 4 | PRICE_MODE | 取价方式 | string(40) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 7 | SETTLEMENT_SOURCE | 内部结算发起方 | string(40) | Y |  |
| 8 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 11 | TO_PLANT_ID | 调入工厂/储运 | GUID | Y |  |
| 12 | TO_COMPANY_ID | 调入公司 | GUID | Y |  |
| 13 | TO_WAREHOUSE_ID | 调入仓库 | GUID | Y |  |
| 14 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 15 | FROM_PLANT_ID | 调出方 | GUID | Y |  |
| 16 | FROM_COMPANY_ID | 调出公司 | GUID | Y |  |
| 17 | FROM_WAREHOUSE_ID | 调出仓库 | GUID | Y |  |
| 18 | CURRENCY_ID | 币种 | GUID | Y |  |
| 19 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 20 | INNER_ARRIVAL_DOC_ID | 调入方内部到货单 | GUID | Y |  |
| 21 | INNER_ARRIVAL_RETURN_DOC_ID | 调入方内部退货单 | GUID | Y |  |
| 22 | INNER_DELIVERY_DOC_ID | 调出方内部销货单 | GUID | Y |  |
| 23 | INNER_DELIVERY_RETURN_DOC_ID | 调出方内部销退单 | GUID | Y |  |
| 24 | PURCHASE_RECEIPT_DOC_ID | 调出方采购入库单 | GUID | Y |  |
| 25 | SALES_ISSUE_DOC_ID | 调出方销售出库单 | GUID | Y |  |
| 26 | RE_PURCHASE_RECEIPT_DOC_ID | 调出方采购退货出库单 | GUID | Y |  |
| 27 | RE_SALES_ISSUE_DOC_ID | 调出方销退入库单 | GUID | Y |  |
| 28 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 29 | RE_SETTLEMENT_PATH_TYPE | 退货结算路径类型 | number | Y |  |
| 30 | RECEIVABLE_DOC_ID | 应收单类型 | GUID | Y |  |
| 31 | PAYABLE_DOC_ID | 应付单类型 | GUID | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | TO_Owner_Org_RTK |  | string(400) | Y |  |
| 61 | TO_Owner_Org_ROid |  | GUID | Y |  |
| 62 | SUPPLY_SYNERGY_ID |  | GUID | Y |  |
| 63 | FROM_SD_ID | 调出方销货单 | GUID | Y |  |
| 64 | TO_PR_ID | 调入方采购退货单 | GUID | Y |  |
| 65 | FROM_SR_ID | 调出方销退单 | GUID | Y |  |
| 66 | TO_PO_ID | 调入方采购订单 | GUID | Y |  |
| 67 | FROM_SO_ID | 调出方销售订单 | GUID | Y |  |
| 68 | TO_PA_ID | 调入方到货单 | GUID | Y |  |

### SUPPLY_SYNERGY_SD (供应协同关系信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_DESCRIPTION | 品名 | string(400) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(400) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | PRICE_UNIT_ID | 单位 | GUID | Y |  |
| 7 | PRICE | 单价 | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | SUPPLY_SYNERGY_SD_ID | 主键 | GUID | Y | Y |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | SUPPLY_SYNERGY_FI_D_ID |  | GUID | Y |  |