---
module: "INNER"
name_zh: "内部交易"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 12
columns: 775
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# INNER (内部交易)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 12 | Columns: 775

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


- **INNER_LIAISON (内部联络单)**
- **INNER_OP_TRANSFER_DOC (维护集团内工艺委外主产品调拨单)**
- **INNER_OP_TRANSFER_DOC_D (集团内工艺委外主产品调拨单单身)**
- **INNER_ORDER_DOC (内部订单)**
- **INNER_ORDER_DOC_D (内部订单单身)**
- **INNER_ORDER_DOC_SD (内部订单子单身)**
- **INNER_SETTLEMENT**
- **INNER_SETTLEMENT_D**
- **INNER_SETTLEMENT_DOC (内部结算单)**
- **INNER_SETTLEMENT_DOC_D (内部结算单单身)**
- **INNER_TRANSFER_DOC (内部调拨单)**
- **INNER_TRANSFER_DOC_D (内部调拨单明细)**


---


---


> Tables: 12

### INNER_LIAISON (内部联络单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | INNER_LIAISON_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | CONFIRM_DATE | 审核日期 | date | Y |  |
| 9 | URGENCY | 紧急程度 | string(40) | Y |  |
| 10 | SUBJECT | 发文事由 | string(510) | Y |  |
| 11 | CONTENT | 内容 | string(8000) | Y |  |
| 12 | RECEIVER | 受文人员 | string(8000) | Y |  |
| 13 | RECEIVER_DEPART | 受文部门 | string(8000) | Y |  |
| 14 | CC_DEPART | 抄送部门 | string(8000) | Y |  |
| 15 | PrintCount | 打印次数 | number | Y |  |
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
| 34 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 35 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 36 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 37 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### INNER_OP_TRANSFER_DOC (维护集团内工艺委外主产品调拨单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | INNER_OP_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 8 | CATEGORY | 单据性质 | string(40) | Y |  |
| 9 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 10 | TRANSFER_TYPE | 调拨类型 | string(40) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | TO_PLANT_ID | 主鍵 | GUID | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 15 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 16 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 17 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |
| 50 | FROM_SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | FROM_SOURCE_ID_ROid |  | GUID | Y |  |

### INNER_OP_TRANSFER_DOC_D (集团内工艺委外主产品调拨单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INNER_OP_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | FROM_MO_ROUTING_D_ID | 转出工单工艺 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 9 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 10 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 11 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
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
| 41 | INNER_OP_TRANSFER_DOC_ID |  | GUID | Y |  |

### INNER_ORDER_DOC (内部订单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | INNER_ORDER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | ORDER_DATE | 订单日期 | date | Y |  |
| 9 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 10 | SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 11 | CURRENCY_ID | 交易原币 | GUID | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 14 | EARNEST_RATE | 订金比例 | number(5,4) | Y |  |
| 15 | EARNEST | 订金 | number(23,8) | Y |  |
| 16 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 17 | TO_PLANT_ID | 调入工厂/储运 | GUID | Y |  |
| 18 | TO_COMPANY_ID | 调入公司 | GUID | Y |  |
| 19 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 20 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 21 | BUYER_ID | 采购员 | GUID | Y |  |
| 22 | PURCHASE_DEPT_ID | 采购部门 | GUID | Y |  |
| 23 | FROM_PLANT_ID | 调出工厂/储运 | GUID | Y |  |
| 24 | FROM_COMPANY_ID | 调出公司 | GUID | Y |  |
| 25 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 26 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 27 | SALES_ID | 业务员 | GUID | Y |  |
| 28 | SALES_DEPT_ID | 销售部门 | GUID | Y |  |
| 29 | DELIVERY_ADDR | 发货地址 | string(510) | Y |  |
| 30 | RECEIPT_ADDR | 收货地址 | string(510) | Y |  |
| 31 | TO_CURRENCY_BC_ID | 调入方本币 | GUID | Y |  |
| 32 | TO_EXCHANGE_RATE | 调入方汇率 | number(18,9) | Y |  |
| 33 | FROM_CURRENCY_BC_ID | 调出方本币 | GUID | Y |  |
| 34 | FROM_EXCHANGE_RATE | 调出方汇率 | number(18,9) | Y |  |
| 35 | PIECES |  | number | Y |  |
| 36 | REMARK | 备注 | string(510) | Y |  |
| 37 | REMARK_FROM | 备注(调出方) | string(510) | Y |  |
| 38 | REMARK_TO | 备注(调入方) | string(510) | Y |  |
| 39 | TO_TAX_INVOICE_CATEGORY_ID | 调入方发票种类 | GUID | Y |  |
| 40 | FROM_TAX_INVOICE_CATEGORY_ID | 调出方发票种类 | GUID | Y |  |
| 41 | TO_AMT_UNINCLUDE_TAX_OC | 调入方原币未税金额 | number(23,8) | Y |  |
| 42 | TO_TAX_OC | 调入方原币税额 | number(23,8) | Y |  |
| 43 | FROM_AMT_UNINCLUDE_TAX_OC | 调出方原币未税金额 | number(23,8) | Y |  |
| 44 | FROM_TAX_OC | 调出方原币税额 | number(23,8) | Y |  |
| 45 | TO_AMT_UNINCLUDE_TAX_BC | 调入方本币未税金额 | number(23,8) | Y |  |
| 46 | TO_TAX_BC | 调入方本币税额 | number(23,8) | Y |  |
| 47 | FROM_AMT_UNINCLUDE_TAX_BC | 调出方本币未税金额 | number(23,8) | Y |  |
| 48 | FROM_TAX_BC | 调出方本币税额 | number(23,8) | Y |  |
| 49 | SETTLEMENT_SOURCE | 结算发起方 | string(40) | Y |  |
| 50 | TAX_ID | 税种 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 70 | PrintCount | 打印次数 | number | Y |  |
| 71 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 72 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 73 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 74 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 75 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 76 | ApproveDate | 修改日期 | date | Y |  |
| 77 | ApproveBy | 修改人 | GUID | Y |  |
| 78 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 79 | CreateDate | 创建日期 | date | Y |  |
| 80 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 81 | ModifiedDate | 修改日期 | date | Y |  |
| 82 | CreateBy | 创建者 | GUID | Y |  |
| 83 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 84 | ModifiedBy | 修改者 | GUID | Y |  |
| 85 | Attachments | 附件 | string | Y |  |
| 86 | Owner_Org_RTK |  | string(400) | Y |  |
| 87 | Owner_Org_ROid |  | GUID | Y |  |
| 88 | IS_INNER | 集团内委外 | number(0/1) | Y |  |

### INNER_ORDER_DOC_D (内部订单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INNER_ORDER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 8 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 9 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 10 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 11 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 12 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 13 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 14 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 15 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 16 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 17 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 18 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 20 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 21 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 22 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 23 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 24 | PRICE_MODE | 取价方式 | string(40) | Y |  |
| 25 | PRICE_RATE | 比例 | number(5,4) | Y |  |
| 26 | PRICE |  | number(23,8) | Y |  |
| 27 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 28 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 29 | AMOUNT |  | number(23,8) | Y |  |
| 30 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 31 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 32 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 33 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 34 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 35 | FROM_TAX_ID | 调出方税种 | GUID | Y |  |
| 36 | FROM_TAX_RATE | 调出方税率 | number(5,4) | Y |  |
| 37 | TO_TAX_ID | 调入方税种 | GUID | Y |  |
| 38 | TO_TAX_RATE | 调入方税率 | number(5,4) | Y |  |
| 39 | FROM_AMT_UNINCLUDE_TAX_OC | 调出方原币未税金额 | number(23,8) | Y |  |
| 40 | FROM_TAX_OC | 调出方原币税额 | number(23,8) | Y |  |
| 41 | TO_AMT_UNINCLUDE_TAX_OC | 调入方原币未税金额 | number(23,8) | Y |  |
| 42 | TO_TAX_OC | 调入方原币税额 | number(23,8) | Y |  |
| 43 | FROM_AMT_UNINCLUDE_TAX_BC | 调出方本币未税金额 | number(23,8) | Y |  |
| 44 | FROM_TAX_BC | 调出方本币税额 | number(23,8) | Y |  |
| 45 | TO_AMT_UNINCLUDE_TAX_BC | 调入方本币未税金额 | number(23,8) | Y |  |
| 46 | TO_TAX_BC | 调入方本币税额 | number(23,8) | Y |  |
| 47 | PIECES |  | number | Y |  |
| 48 | REMARK | 备注 | string(510) | Y |  |
| 49 | FROM_PRICE | 调出单价 | number(23,8) | Y |  |
| 50 | TO_PRICE | 调入单价 | number(23,8) | Y |  |
| 51 | PROJECT_ID | 项目 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 71 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 72 | ApproveDate | 修改日期 | date | Y |  |
| 73 | ApproveBy | 修改人 | GUID | Y |  |
| 74 | CreateDate | 创建日期 | date | Y |  |
| 75 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 76 | ModifiedDate | 修改日期 | date | Y |  |
| 77 | CreateBy | 创建者 | GUID | Y |  |
| 78 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 79 | ModifiedBy | 修改者 | GUID | Y |  |
| 80 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 81 | SOURCE_ID_ROid |  | GUID | Y |  |
| 82 | INNER_ORDER_DOC_ID |  | GUID | Y |  |
| 83 | CLIENT_ITEM_ID | 委托方品号 | GUID | Y |  |
| 84 | CLIENT_ITEM_DESCRIPTION | 委托方品名 | string(120) | Y |  |
| 85 | CLIENT_ITEM_FEATURE_ID | 委托方特征码 | GUID | Y |  |
| 86 | CLIENT_ITEM_SPECIFICATION | 委托方规格 | string(510) | Y |  |
| 87 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 88 | NOT_INCLUDE_PLAN | 不纳入计划 | number(0/1) | Y |  |

### INNER_ORDER_DOC_SD (内部订单子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INNER_ORDER_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | RECEIPT_WAREHOUSE_ID | 收货仓库 | GUID | Y |  |
| 4 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 5 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 6 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 9 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 13 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 14 | PLAN_SHIP_DATE | 预发货日 | date | Y |  |
| 15 | DELIVERY_TYPE | 供货类型 | string(40) | Y |  |
| 16 | DELIVERY_PLANT_ID | 发货工厂/储运 | GUID | Y |  |
| 17 | DELIVERY_WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 18 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 19 | SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 20 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 21 | DIRECT_SHIP | 直运 | number(0/1) | Y |  |
| 22 | PIECES |  | number | Y |  |
| 23 | DELIVERED_BUSINESS_QTY | 已调出业务数量 | number(16,6) | Y |  |
| 24 | RECEIPTED_BUSINESS_QTY | 已调入业务数量 | number(16,6) | Y |  |
| 25 | DELIVERED_PRICE_QTY | 已调出计价数量 | number(16,6) | Y |  |
| 26 | RECEIPTED_PRICE_QTY | 已调入计价数量 | number(16,6) | Y |  |
| 27 | CLOSE | 结束码 | string(40) | Y |  |
| 28 | PURCHASED_BUSINESS_QTY | 已转采业务数量 | number(16,6) | Y |  |
| 29 | PURCHASED_PRICE_QTY | 已转采计价数量 | number(16,6) | Y |  |
| 30 | TRANSFER_PURCHASE_STATUS | 转采结束码 | string(40) | Y |  |
| 31 | PLAN_STATUS | 计划状态 | string(40) | Y |  |
| 32 | REMARK | 备注 | string(510) | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | DELIVERY_PARTNER_ID_RTK |  | string(400) | Y |  |
| 62 | DELIVERY_PARTNER_ID_ROid |  | GUID | Y |  |
| 63 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 64 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 65 | INNER_ORDER_DOC_D_ID |  | GUID | Y |  |
| 66 | AMOUNT | 金额 | number(23,8) | Y |  |
| 67 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 68 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 69 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 70 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 71 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 72 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 73 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |

### INNER_SETTLEMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | INNER_SETTLEMENT_ID | 主键 | GUID | Y | Y |
| 7 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 8 | SERVICE_SITE_ID | 站点 | GUID | Y |  |
| 9 | SETTLEMENT_COMPANY1_ID | 收款公司 | GUID | Y |  |
| 10 | SETTLEMENT_COMPANY2_ID | 付款公司 | GUID | Y |  |
| 11 | CURRENCY_ID | 币种 | GUID | Y |  |
| 12 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 13 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 14 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 15 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 16 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 17 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 18 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 19 | TAX_BC | 本币税额 | number(23,8) | Y |  |
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

### INNER_SETTLEMENT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INNER_SETTLEMENT_D_ID | 主键 | GUID | Y | Y |
| 3 | SETTLEMENT_TYPE | 类别 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | SN | 序列号 | string(510) | Y |  |
| 9 | QUANTITY | 数量 | number(16,6) | Y |  |
| 10 | PRICE | 单价 | number(23,8) | Y |  |
| 11 | AMOUNT | 金额 | number(23,8) | Y |  |
| 12 | TAX_ID | 税种 | GUID | Y |  |
| 13 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 14 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | UNIT_ID | 单位 | GUID | Y |  |
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
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | INNER_SETTLEMENT_ID |  | GUID | Y |  |

### INNER_SETTLEMENT_DOC (内部结算单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | INNER_SETTLEMENT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 9 | CURRENCY_ID | 交易原币 | GUID | Y |  |
| 10 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 11 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 12 | TO_PLANT_ID | 调入工厂/储运 | GUID | Y |  |
| 13 | TO_COMPANY_ID | 调入公司 | GUID | Y |  |
| 14 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 15 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 16 | BUYER_ID | 采购员 | GUID | Y |  |
| 17 | PURCHASE_DEPT_ID | 采购部门 | GUID | Y |  |
| 18 | FROM_PLANT_ID | 调出工厂/储运 | GUID | Y |  |
| 19 | FROM_COMPANY_ID | 调出公司 | GUID | Y |  |
| 20 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 21 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 22 | SALES_ID | 业务员 | GUID | Y |  |
| 23 | SALES_DEPT_ID | 销售部门 | GUID | Y |  |
| 24 | TO_CURRENCY_BC_ID | 调入方本币 | GUID | Y |  |
| 25 | TO_EXCHANGE_RATE | 调入方汇率 | number(18,9) | Y |  |
| 26 | FROM_CURRENCY_BC_ID | 调出方本币 | GUID | Y |  |
| 27 | FROM_EXCHANGE_RATE | 调出方汇率 | number(18,9) | Y |  |
| 28 | REMARK | 备注 | string(510) | Y |  |
| 29 | REMARK_FROM | 备注（调出方） | string(510) | Y |  |
| 30 | REMARK_TO | 备注（调入方） | string(510) | Y |  |
| 31 | TO_TAX_INVOICE_CATEGORY_ID | 调入方发票种类 | GUID | Y |  |
| 32 | FROM_TAX_INVOICE_CATEGORY_ID | 调出方发票种类 | GUID | Y |  |
| 33 | TO_AMT_UNINCLUDE_TAX_OC | 调入方原币未税金额 | number(23,8) | Y |  |
| 34 | TO_TAX_OC | 调入方原币税额 | number(23,8) | Y |  |
| 35 | FROM_AMT_UNINCLUDE_TAX_OC | 调出方原币未税金额 | number(23,8) | Y |  |
| 36 | FROM_TAX_OC | 调出方原币税额 | number(23,8) | Y |  |
| 37 | TO_AMT_UNINCLUDE_TAX_BC | 调入方本币未税金额 | number(23,8) | Y |  |
| 38 | TO_TAX_BC | 调入方本币税额 | number(23,8) | Y |  |
| 39 | FROM_AMT_UNINCLUDE_TAX_BC | 调出方本币未税金额 | number(23,8) | Y |  |
| 40 | FROM_TAX_BC | 调出方本币税额 | number(23,8) | Y |  |
| 41 | TO_TAX_DEDUCTIBLE_INDICATOR | 调入方可抵扣VAT标识 | number(0/1) | Y |  |
| 42 | FROM_TAX_ID | 调出方税种 | GUID | Y |  |
| 43 | TO_TAX_ID | 调入方税种 | GUID | Y |  |
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Attachments | 附件 | string | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 71 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 72 | ApproveDate | 修改日期 | date | Y |  |
| 73 | ApproveBy | 修改人 | GUID | Y |  |
| 74 | PrintCount | 打印次数 | number | Y |  |
| 75 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 76 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 77 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 78 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 79 | Owner_Org_RTK |  | string(400) | Y |  |
| 80 | Owner_Org_ROid |  | GUID | Y |  |
| 81 | SYNERGY_ID_RTK |  | string(400) | Y |  |
| 82 | SYNERGY_ID_ROid |  | GUID | Y |  |
| 83 | SYNERGY_D_ID_RTK |  | string(400) | Y |  |
| 84 | SYNERGY_D_ID_ROid |  | GUID | Y |  |

### INNER_SETTLEMENT_DOC_D (内部结算单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INNER_SETTLEMENT_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 8 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 9 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 10 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 11 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 12 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 13 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 14 | PRICE_MODE | 取价方式 | string(40) | Y |  |
| 15 | PRICE_RATE | 比例 | number(5,4) | Y |  |
| 16 | PRICE | 单价 | number(23,8) | Y |  |
| 17 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 18 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 19 | AMOUNT |  | number(23,8) | Y |  |
| 20 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 21 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 22 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 23 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 24 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 25 | FROM_TAX_ID | 调出方税种 | GUID | Y |  |
| 26 | FROM_TAX_RATE | 调出方税率 | number(5,4) | Y |  |
| 27 | TO_TAX_ID | 调入方税种 | GUID | Y |  |
| 28 | TO_TAX_RATE | 调入方税率 | number(5,4) | Y |  |
| 29 | FROM_AMT_UNINCLUDE_TAX_OC | 调出方原币未税金额 | number(23,8) | Y |  |
| 30 | FROM_TAX_OC | 调出方原币税额 | number(23,8) | Y |  |
| 31 | TO_AMT_UNINCLUDE_TAX_OC | 调入方原币未税金额 | number(23,8) | Y |  |
| 32 | TO_TAX_OC | 调入方原币税额 | number(23,8) | Y |  |
| 33 | TO_AMT_UNINCLUDE_TAX_BC | 调入方本币未税金额 | number(23,8) | Y |  |
| 34 | TO_TAX_BC | 调入方本币税额 | number(23,8) | Y |  |
| 35 | FROM_AMT_UNINCLUDE_TAX_BC | 调出方本币未税金额 | number(23,8) | Y |  |
| 36 | FROM_TAX_BC | 调出方本币税额 | number(23,8) | Y |  |
| 37 | REMARK | 备注 | string(510) | Y |  |
| 38 | PROJECT_ID | 项目 | GUID | Y |  |
| 39 | OUT_PROJECT_ID | 调出方項目 | GUID | Y |  |
| 40 | FROM_DISCOUNT_UN_TAX_AMT_OC | 调出方原币未税折扣额 | number(23,8) | Y |  |
| 41 | FROM_DISCOUNT_IN_TAX_AMT_OC | 调出方原币含税折扣额 | number(23,8) | Y |  |
| 42 | FROM_DISCOUNT_UN_TAX_AMT_BC | 调出方本币未税折扣额 | number(23,8) | Y |  |
| 43 | FROM_DISCOUNT_IN_TAX_AMT_BC | 调出方本币含税折扣额 | number(23,8) | Y |  |
| 44 | FROM_SETTLEMENT_PRICE_QTY | 调出方已结算计价数量 | number(16,6) | Y |  |
| 45 | FROM_SETTLEMENT_AMT_UN_TAX_OC | 调出方已结算原币未税金额 | number(23,8) | Y |  |
| 46 | FROM_SETTLEMENT_TAX_OC | 调出方已结算原币税额 | number(23,8) | Y |  |
| 47 | FROM_SETTLEMENT_AMT_UN_TAX_BC | 调出方已结算本币未税金额 | number(23,8) | Y |  |
| 48 | FROM_SETTLEMENT_TAX_BC | 调出方已结算本币税额 | number(23,8) | Y |  |
| 49 | FROM_SETTLE_DISC_UN_TAX_AMT_OC | 调出方已结算原币未税折扣额 | number(23,8) | Y |  |
| 50 | FROM_SETTLE_DISC_IN_TAX_AMT_OC | 调出方已结算原币含税折扣额 | number(23,8) | Y |  |
| 51 | FROM_SETTLE_DISC_UN_TAX_AMT_BC | 调出方已结算本币未税折扣额 | number(23,8) | Y |  |
| 52 | FROM_SETTLE_DISC_IN_TAX_AMT_BC | 调出方已结算本币含税折扣额 | number(23,8) | Y |  |
| 53 | TO_SETTLEMENT_PRICE_QTY | 调入方已结算计价数量 | number(16,6) | Y |  |
| 54 | TO_SETTLEMENT_AMT_UN_TAX_OC | 调入方已结算原币未税金额 | number(23,8) | Y |  |
| 55 | TO_SETTLEMENT_TAX_OC | 调入方已结算原币税额 | number(23,8) | Y |  |
| 56 | TO_SETTLEMENT_AMT_UN_TAX_BC | 调入方已结算本币未税金额 | number(23,8) | Y |  |
| 57 | TO_SETTLEMENT_TAX_BC | 调入方已结算本币税额 | number(23,8) | Y |  |
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 66 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 67 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 68 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 69 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 70 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 71 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 72 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 73 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 74 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 75 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 76 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 77 | UDF041 | 自定义字段12 | date | Y |  |
| 78 | UDF042 | 自定义字段13 | date | Y |  |
| 79 | UDF051 | 自定义字段14 | GUID | Y |  |
| 80 | UDF052 | 自定义字段15 | GUID | Y |  |
| 81 | UDF053 | 自定义字段16 | GUID | Y |  |
| 82 | UDF054 | 自定义字段17 | GUID | Y |  |
| 83 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 84 | ApproveDate | 修改日期 | date | Y |  |
| 85 | ApproveBy | 修改人 | GUID | Y |  |
| 86 | FROM_SOURCE_ID_RTK |  | string(400) | Y |  |
| 87 | FROM_SOURCE_ID_ROid |  | GUID | Y |  |
| 88 | TO_SOURCE_ID_RTK |  | string(400) | Y |  |
| 89 | TO_SOURCE_ID_ROid |  | GUID | Y |  |
| 90 | INNER_SETTLEMENT_DOC_ID |  | GUID | Y |  |
| 91 | CLIENT_ITEM_ID | 委托方品号 | GUID | Y |  |
| 92 | CLIENT_ITEM_DESCRIPTION | 委托方品名 | string(120) | Y |  |
| 93 | CLIENT_ITEM_FEATURE_ID | 委托方特征码 | GUID | Y |  |
| 94 | CLIENT_ITEM_SPECIFICATION | 委托方规格 | string(510) | Y |  |
| 95 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |

### INNER_TRANSFER_DOC (内部调拨单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | INNER_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | TRANSFER_TYPE | 调拨类型 | string(40) | Y |  |
| 11 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 12 | FROM_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 13 | TO_PLANT_ID | 主鍵 | GUID | Y |  |
| 14 | FROM_COMPANY_ID | 委托方公司 | GUID | Y |  |
| 15 | TO_COMPANY_ID | 生产方公司 | GUID | Y |  |
| 16 | PrintCount | 打印次数 | number | Y |  |
| 17 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 18 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 19 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 20 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Attachments | 附件 | string | Y |  |
| 28 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 29 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 30 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 31 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 32 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 33 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 34 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 35 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 36 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 37 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 38 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 39 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 40 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 41 | UDF041 | 自定义字段12 | date | Y |  |
| 42 | UDF042 | 自定义字段13 | date | Y |  |
| 43 | UDF051 | 自定义字段14 | GUID | Y |  |
| 44 | UDF052 | 自定义字段15 | GUID | Y |  |
| 45 | UDF053 | 自定义字段16 | GUID | Y |  |
| 46 | UDF054 | 自定义字段17 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### INNER_TRANSFER_DOC_D (内部调拨单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INNER_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | MO_ID | 工单 | GUID | Y |  |
| 8 | MO_D_ID | 工单序号 | GUID | Y |  |
| 9 | FROM_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 10 | FROM_BIN_ID | 主键 | GUID | Y |  |
| 11 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 12 | TO_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 13 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 14 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 15 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 16 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 17 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
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
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | INNER_TRANSFER_DOC_ID |  | GUID | Y |  |