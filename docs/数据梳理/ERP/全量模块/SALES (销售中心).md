---
module: "SALES"
name_zh: "销售中心"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 23
columns: 1776
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52

---

# SALES (销售中心)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 23 | Columns: 1776

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]

---

## Tables


- **SALES_CENTER (销售域信息)**
- **SALES_CENTER_DEPT (销售域销售部门信息)**
- **SALES_CENTER_PLANT (销售域服务工厂/储运信息)**
- **SALES_DELIVERY**
- **SALES_DELIVERY_D**
- **SALES_DELIVERY_OFFSETDEP (销货单订金冲减单身)**
- **SALES_FACT_TABLE (销售统计分析表)**
- **SALES_FINANCE_INFO (销售出入库业务财务信息)**
- **SALES_ISSUE (销货出库单)**
- **SALES_ISSUE_D (销货出库明细)**
- **SALES_ORDER_DOC (销售订单)**
- **SALES_ORDER_DOC_D (订单明细)**
- **SALES_ORDER_DOC_EXPENSE (订单费用组成)**
- **SALES_ORDER_DOC_INSTAL (订单分期)**
- **SALES_ORDER_DOC_SD (发货计划)**
- **SALES_RECEIVABLE_BALANCE (销货应收余额档)**
- **SALES_RETURN (销退单)**
- **SALES_RETURN_D (销退单身)**
- **SALES_RETURN_RECEIPT (销退入库单)**
- **SALES_RETURN_RECEIPT_D (销退入库单单身)**
- **SALES_SYNERGY (销售协同关系信息)**
- **SALES_SYNERGY_FI_D (销售协同结算路径明细)**
- **SALES_SYNERGY_SD (销售协同关系信息)**


---


---


> Tables: 23

### SALES_CENTER (销售域信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALES_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | SALES_CENTER_CODE | 销售域编号 | string(20) | Y |  |
| 5 | SALES_CENTER_NAME | 销售域名称 | string(40) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Attachments | 附件 | string | Y |  |
| 8 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### SALES_CENTER_DEPT (销售域销售部门信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALES_CENTER_DEPT_ID | 主键 | GUID | Y | Y |
| 2 | MAIN | 主要 | number(0/1) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | DEPT_ID | 销售部门 | GUID | Y |  |
| 5 | SALES_ID | 业务员 | GUID | Y |  |
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
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | SALES_CENTER_ID |  | GUID | Y |  |

### SALES_CENTER_PLANT (销售域服务工厂/储运信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALES_CENTER_PLANT_ID | 主键 | GUID | Y | Y |
| 2 | MAIN | 主要 | number(0/1) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 5 | KIT_DISTRIBUTION | 使用零组件配送 | number(0/1) | Y |  |
| 6 | KIT_WAREHOUSE_ID | 零组件接收仓库 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
| 8 | MO_DOC_ID | 工单 | GUID | Y |  |
| 9 | IR_DOC_ID | 领料单 | GUID | Y |  |
| 10 | MR_DOC_ID | 生产入库单 | GUID | Y |  |
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
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SALES_CENTER_ID |  | GUID | Y |  |

### SALES_DELIVERY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALES_DELIVERY_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_DATE | 销货日期 | date | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | CURRENCY_ID | 币种 | GUID | Y |  |
| 11 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 14 | PLANT_ID | 出货工厂/储运 | GUID | Y |  |
| 15 | WAREHOUSE_ID | 限定仓库 | GUID | Y |  |
| 16 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 17 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 18 | SHIP_TO_ADDR_NAME | 收货地址 | string(510) | Y |  |
| 19 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 20 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 21 | TELEPHONE | 收货电话 | string(40) | Y |  |
| 22 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 23 | ADVANCED_DELIVERY | 允许早交 | number(0/1) | Y |  |
| 24 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 25 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 26 | INVOICE_CUSTOMER_FULL_NAME | 结算客户全称 | string(144) | Y |  |
| 27 | INVOICE_ADDR_ID | 发票邮寄地址 | GUID | Y |  |
| 28 | INVOICE_ADDR_NAME | 发票邮寄地址名称 | string(510) | Y |  |
| 29 | INVOICE_CONTACT_ID | 发票邮寄联系人 | GUID | Y |  |
| 30 | INVOICE_CONTACT_NAME | 发票邮寄人名称 | string(72) | Y |  |
| 31 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 32 | RECEIVER_ID | 收款业务员 | GUID | Y |  |
| 33 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 34 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 35 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 36 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 37 | PIECES | 件数 | number | Y |  |
| 38 | REMARK | 备注 | string(510) | Y |  |
| 39 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 40 | SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 41 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 42 | DIRECT_INVOICING_INDICATOR | 直接开票 | number(0/1) | Y |  |
| 43 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 44 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 45 | OFFSET_DEPOSIT_INDICATOR | 订金冲减 | number(0/1) | Y |  |
| 46 | ISSUED_STATUS | 出库状态 | string(80) | Y |  |
| 47 | SETTLEMENT_INDICATOR | 当前可结算 | number(0/1) | Y |  |
| 48 | SIGN_REQUIRED | 需签收 | number(0/1) | Y |  |
| 49 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 50 | LETTER_CREDIT_ID | 信用证 | GUID | Y |  |
| 51 | CUSTOMER_SHIPPING_MARK_ID | 客户唛头 | GUID | Y |  |
| 52 | FRONT_MARK | 正唛 | string(510) | Y |  |
| 53 | FRONT_MARK_IS_PIC | 正唛用图片 | number(0/1) | Y |  |
| 54 | FRONT_MARK_PIC | 正唛图片 | string(120) | Y |  |
| 55 | SIDE_MARK | 侧唛 | string(510) | Y |  |
| 56 | SIDE_MARK_IS_PIC | 侧唛用图片 | number(0/1) | Y |  |
| 57 | SIDE_MARK_PIC | 侧唛图片 | string(120) | Y |  |
| 58 | INVOICE_REMARK | INVOICE备注 | string(510) | Y |  |
| 59 | PACKING_LIST_REMARK | PACKINGLIST备注 | string(510) | Y |  |
| 60 | LICENSE_NO | 出口许可证号 | string(40) | Y |  |
| 61 | MASTER_BL | 大提单单号 | string(40) | Y |  |
| 62 | HOUSE_BL | 小提单单号 | string(40) | Y |  |
| 63 | NOTIFY_CUSTOMER_ID | 进口方通知对象信息 | GUID | Y |  |
| 64 | CUSTOMS_DECLARATION_NO | 报单号码 | string(40) | Y |  |
| 65 | INVOICE_NO | INVOCIE单号 | string(40) | Y |  |
| 66 | CUSTOMS_HANDBOOK | 海关手册 | string(40) | Y |  |
| 67 | INSPECTION_SUPPLIER_ID | 验货公司 | GUID | Y |  |
| 68 | BROKERS_SUPPLIER_ID | 报关行 | GUID | Y |  |
| 69 | FORWARDER_SUPPLIER_ID | 货运代理公司 | GUID | Y |  |
| 70 | CUSTOMS_SEAL | 海关封签 | string(40) | Y |  |
| 71 | ETA | ETA | date | Y |  |
| 72 | ETD | ETD | date | Y |  |
| 73 | CONTAINER_NO | 货柜号码 | string(40) | Y |  |
| 74 | CONTAINER_SIZE | 货柜尺寸 | string(40) | Y |  |
| 75 | CONTAINER_GROUND | 货柜场 | string(40) | Y |  |
| 76 | BL_CONTENT | 提单内容 | string(40) | Y |  |
| 77 | LOADING_PORT | 起始港口 | string(120) | Y |  |
| 78 | DESTINATION_PORT | 目的港口 | string(120) | Y |  |
| 79 | DESTINATION | 目的地 | string(120) | Y |  |
| 80 | SHIP_NAME | 船名 | string(80) | Y |  |
| 81 | VOYAGE_NO | 船次 | string(40) | Y |  |
| 82 | SI_NO | SI NO | string(40) | Y |  |
| 83 | SHIPPING_DATE | 装船日 | date | Y |  |
| 84 | LOADING_DATE | 装货日 | date | Y |  |
| 85 | CLOSING_DATE | 截关日 | date | Y |  |
| 86 | PALLET_UNIT | 货盘单位 | string(40) | Y |  |
| 87 | PRICE_TERMS_ID | 价格条款 | GUID | Y |  |
| 88 | UNLIMITED_RELEASE | 超限放行 | number(0/1) | Y |  |
| 89 | TAX_ID | 税种 | GUID | Y |  |
| 90 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 91 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 92 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 93 | PROJECT_ID | 限用项目 | GUID | Y |  |
| 94 | Attachments | 附件 | string | Y |  |
| 95 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 96 | Version | 版本号，不要随意更改 | binary | Y |  |
| 97 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 98 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 99 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 100 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 101 | PrintCount | 打印次数 | number | Y |  |
| 102 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 103 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 104 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 105 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 106 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 107 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 108 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 109 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 110 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 111 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 112 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 113 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 114 | UDF041 | 自定义字段12 | date | Y |  |
| 115 | UDF042 | 自定义字段13 | date | Y |  |
| 116 | UDF051 | 自定义字段14 | GUID | Y |  |
| 117 | UDF052 | 自定义字段15 | GUID | Y |  |
| 118 | UDF053 | 自定义字段16 | GUID | Y |  |
| 119 | UDF054 | 自定义字段17 | GUID | Y |  |
| 120 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 121 | ApproveDate | 修改日期 | date | Y |  |
| 122 | ApproveBy | 修改人 | GUID | Y |  |
| 123 | CreateDate | 创建日期 | date | Y |  |
| 124 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 125 | ModifiedDate | 修改日期 | date | Y |  |
| 126 | CreateBy | 创建者 | GUID | Y |  |
| 127 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 128 | ModifiedBy | 修改者 | GUID | Y |  |
| 129 | Owner_Org_RTK |  | string(400) | Y |  |
| 130 | Owner_Org_ROid |  | GUID | Y |  |
| 131 | FINANCING_FLAG | 融资标识 | number(0/1) | Y |  |
| 132 | FINANCING_SEQNO | 融资序号 | number | Y |  |
| 133 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 134 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 135 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 136 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 137 | DOC_Sequence | 单据顺序 | number | Y |  |
| 138 | SOURCE_CUSTOMER_ID | 最终客户 | GUID | Y |  |
| 139 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 140 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |

### SALES_DELIVERY_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_DELIVERY_D_ID | GUID | GUID | Y | Y |
| 3 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
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
| 19 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 20 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 21 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 22 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 23 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 24 | PRICE | 单价 | number(23,8) | Y |  |
| 25 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 26 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 27 | AMOUNT | 金额 | number(23,8) | Y |  |
| 28 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 29 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 30 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 31 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 32 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 33 | TAX_ID | 税种 | GUID | Y |  |
| 34 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 35 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 36 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 37 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 38 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 39 | PIECES | 件数 | number | Y |  |
| 40 | REMARK | 备注 | string(510) | Y |  |
| 41 | WAREHOUSE_ID | 出货仓库 | GUID | Y |  |
| 42 | BIN_ID | 库位 | GUID | Y |  |
| 43 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 44 | SALES_TYPE | 销货类型 | string(40) | Y |  |
| 45 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 46 | ISSUED_QTY | 已出库业务数量 | number(16,6) | Y |  |
| 47 | ISSUED_PRICE_QTY | 已出库计价数量 | number(16,6) | Y |  |
| 48 | ISSUED | 已出库 | string(40) | Y |  |
| 49 | DELIVERY_NOTICED | 已通知 | number(0/1) | Y |  |
| 50 | PICKED | 已拣货 | number(0/1) | Y |  |
| 51 | PURCHASE_ARRIVALED | 已内部到货 | number(0/1) | Y |  |
| 52 | PRINT_TIMES_1 | 出货通知单打印次数 | number | Y |  |
| 53 | PRINT_TIMES_2 | 拣货单打印次数 | number | Y |  |
| 54 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 55 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 56 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 57 | SIGN_DIFF_PRICE_QTY | 签收差异计价数量 | number(16,6) | Y |  |
| 58 | SIGN_DIFF_AMT_UN_TAX_OC | 签收差异原币未税金额 | number(23,8) | Y |  |
| 59 | SIGN_DIFF_TAX_OC | 签收差异原币税额 | number(23,8) | Y |  |
| 60 | SALES_ORDER_DOC_ID | 销售订单主键 | GUID | Y |  |
| 61 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 62 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 63 | ISSUED_CHANGE_PRICE | 出库变更单价 | number(0/1) | Y |  |
| 64 | SHOULD_SETTLE_PRICE_QTY | 应结算计价数量 | number(16,6) | Y |  |
| 65 | PROJECT_ID | 项目 | GUID | Y |  |
| 66 | GROSS_WEIGHT | 毛重 | number(16,6) | Y |  |
| 67 | VOLUME | 材积 | number(16,6) | Y |  |
| 68 | DELIVERY_ITEM_DESC | 出货商品描述 | string(4000) | Y |  |
| 69 | FORECAST_QTY | 预计出货数量 | number(16,6) | Y |  |
| 70 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 71 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 72 | Version | 版本号，不要随意更改 | binary | Y |  |
| 73 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 74 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 75 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 76 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 77 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 78 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 79 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 80 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 81 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 82 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 83 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 84 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 85 | UDF041 | 自定义字段12 | date | Y |  |
| 86 | UDF042 | 自定义字段13 | date | Y |  |
| 87 | UDF051 | 自定义字段14 | GUID | Y |  |
| 88 | UDF052 | 自定义字段15 | GUID | Y |  |
| 89 | UDF053 | 自定义字段16 | GUID | Y |  |
| 90 | UDF054 | 自定义字段17 | GUID | Y |  |
| 91 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 92 | ApproveDate | 修改日期 | date | Y |  |
| 93 | ApproveBy | 修改人 | GUID | Y |  |
| 94 | CreateDate | 创建日期 | date | Y |  |
| 95 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 96 | ModifiedDate | 修改日期 | date | Y |  |
| 97 | CreateBy | 创建者 | GUID | Y |  |
| 98 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 99 | ModifiedBy | 修改者 | GUID | Y |  |
| 100 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 101 | SOURCE_ID_ROid |  | GUID | Y |  |
| 102 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 103 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 104 | SALES_DELIVERY_ID |  | GUID | Y |  |
| 105 | REFERENCE_PRICE1 | 参考单价一 | number(23,8) | Y |  |
| 106 | REFERENCE_PRICE2 | 参考单价二 | number(23,8) | Y |  |
| 107 | REFERENCE_AMOUNT1 | 参考金额一 | number(23,8) | Y |  |
| 108 | REFERENCE_AMOUNT2 | 参考金额二 | number(23,8) | Y |  |
| 109 | BORROW_DOC_ID | 借出单ID | GUID | Y |  |
| 110 | PRODUCT_SUB_GROUP_ID | 替代群组主键 | GUID | Y |  |
| 111 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |
| 112 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 113 | SOURCE_ORDER_ROid |  | GUID | Y |  |
| 114 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 115 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |

### SALES_DELIVERY_OFFSETDEP (销货单订金冲减单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_DELIVERY_OFFSETDEP_ID | 主键 | GUID | Y | Y |
| 3 | RECEIVABLE_DOC_ID | 应收单号 | GUID | Y |  |
| 4 | RECEIVABLE_DOC_D_ID | 应收单序号 | GUID | Y |  |
| 5 | OFFSET_AMT_UN_TAX_OC | 冲减原币未税金额 | number(23,8) | Y |  |
| 6 | OFFSET_TAX_OC | 冲减原币税额 | number(23,8) | Y |  |
| 7 | OFFSET_TAX_BC | 冲减本币税额 | number(23,8) | Y |  |
| 8 | SETTLE_OFFSET_AMT_UN_TAX_OC | 已结算冲减原币未税金额 | number(23,8) | Y |  |
| 9 | SETTLE_OFFSET_TAX_OC | 已结算冲减原币税额 | number(23,8) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | SOURCE1_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE1_ID_ROid |  | GUID | Y |  |
| 41 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 43 | SALES_DELIVERY_ID |  | GUID | Y |  |

### SALES_FACT_TABLE (销售统计分析表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALES_FACT_TABLE_ID | 主键 | GUID | Y | Y |
| 4 | DATE | 日期 | date | Y |  |
| 5 | ACC_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACC_PERIOD | 会计期间 | string(20) | Y |  |
| 7 | CUSTOMER_ID | 客户ID | GUID | Y |  |
| 8 | CUSTOMER_CODE | 客户 | string(20) | Y |  |
| 9 | CUSTOMER_NAME | 客户名称 | string(40) | Y |  |
| 10 | ITEM_ID | 品号ID | GUID | Y |  |
| 11 | ITEM_CODE | 品号 | string(80) | Y |  |
| 12 | ITEM_NAME | 品名 | string(120) | Y |  |
| 13 | ITEM_SPEC | 规格 | string(510) | Y |  |
| 14 | ITEM_FEATURE_ID | 特征码ID | GUID | Y |  |
| 15 | ITEM_FEATURE_CODE | 特征码 | string(120) | Y |  |
| 16 | ITEM_FEATURE_SPEC | 特征码规格 | string(510) | Y |  |
| 17 | ADMIN_UNIT_CODE | 部门 | string(20) | Y |  |
| 18 | ADMIN_UNIT_NAME | 部门名称 | string(40) | Y |  |
| 19 | EMPLOYEE_CODE | 业务员 | string(20) | Y |  |
| 20 | EMPLOYEE_NAME | 业务员名称 | string(40) | Y |  |
| 21 | SALES_CENTER_CODE | 销售域 | string(20) | Y |  |
| 22 | SALES_CENTER_NAME | 销售域名称 | string(40) | Y |  |
| 23 | SO_RECORDS | 接单笔数 | number | Y |  |
| 24 | SO_AMT | 接单金额 | number(23,8) | Y |  |
| 25 | SO_QTY | 接单数量 | number(16,6) | Y |  |
| 26 | SO_QTY2 | 接单第二数量 | number(16,6) | Y |  |
| 27 | SD_RECORDS | 销货笔数 | number | Y |  |
| 28 | SD_AMT | 销货金额 | number(23,8) | Y |  |
| 29 | SD_QTY | 销货数量 | number(16,6) | Y |  |
| 30 | SD_QTY2 | 销货第二数量 | number(16,6) | Y |  |
| 31 | RT_RECORDS | 销退笔数 | number | Y |  |
| 32 | RT_QTY | 销退数量 | number(16,6) | Y |  |
| 33 | RT_QTY2 | 销退第二数量 | number(16,6) | Y |  |
| 34 | RT_AMT | 销退金额 | number(23,8) | Y |  |
| 35 | IN_AMT | 应收金额 | number(23,8) | Y |  |
| 36 | IN_QTY | 应收数量 | number(16,6) | Y |  |
| 37 | UNIT_ID | 存货单位ID | GUID | Y |  |
| 38 | UNIT_NAME | 存货单位名称 | string(20) | Y |  |
| 39 | UNIT_CODE | 存货单位编号 | string(8) | Y |  |
| 40 | UNIT2_ID | 第二存货单位ID | GUID | Y |  |
| 41 | UNIT2_CODE | 第二存货单位编号 | string(8) | Y |  |
| 42 | UNIT2_NAME | 第二存货单位名称 | string(20) | Y |  |
| 43 | CURRENCY_ID | 币种ID | GUID | Y |  |
| 44 | CURRENCY_NAME | 币种名称 | string(40) | Y |  |
| 45 | CURRENCY_CODE | 币种编号 | string(12) | Y |  |
| 46 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 47 | TYPE | 类型 | string(40) | Y |  |
| 48 | SO_LARGESS_QTY | 订单赠品量 | number(16,6) | Y |  |
| 49 | SO_LARGESS_QTY2 | 订单赠品第二数量 | number(16,6) | Y |  |
| 50 | SO_SPARE_QTY | 订单备品量 | number(16,6) | Y |  |
| 51 | SO_SPARE_QTY2 | 订单备品第二数量 | number(16,6) | Y |  |
| 52 | SD_LARGESS_QTY | 销货出库赠品量 | number(16,6) | Y |  |
| 53 | SD_LARGESS_QTY2 | 销货出库赠品第二数量 | number(16,6) | Y |  |
| 54 | SD_SPARE_QTY | 销货出库备品量 | number(16,6) | Y |  |
| 55 | SD_SPARE_QTY2 | 销货出库备品第二数量 | number(16,6) | Y |  |
| 56 | RT_LARGESS_QTY | 销退入库赠品量 | number(16,6) | Y |  |
| 57 | RT_LARGESS_QTY2 | 销退入库赠品第二数量 | number(16,6) | Y |  |
| 58 | RT_SPARE_QTY | 销退入库备品量 | number(16,6) | Y |  |
| 59 | RT_SPARE_QTY2 | 销退入库备品第二数量 | number(16,6) | Y |  |
| 60 | COMPANY_ID | 公司主键 | GUID | Y |  |
| 61 | COMPANY_CODE | 公司编号 | string(20) | Y |  |
| 62 | COMPANY_NAME | 公司名称 | string(40) | Y |  |
| 63 | SD_COST_AMT | 销货出库成本金额 | number(23,8) | Y |  |
| 64 | RT_COST_AMT | 销退入库成本金额 | number(23,8) | Y |  |
| 65 | YEAR | 年份 | number | Y |  |
| 66 | MONTH | 月份 | number | Y |  |
| 67 | SO_AMT_UT | 接单未税金额 | number(23,8) | Y |  |
| 68 | SD_AMT_UT | 销货未税金额 | number(23,8) | Y |  |
| 69 | RT_AMT_UT | 销退未税金额 | number(23,8) | Y |  |
| 70 | IN_AMT_UT | 应收未税金额 | number(23,8) | Y |  |
| 71 | CreateDate | 创建日期 | date | Y |  |
| 72 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 73 | ModifiedDate | 修改日期 | date | Y |  |
| 74 | CreateBy | 创建者 | GUID | Y |  |
| 75 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 76 | ModifiedBy | 修改者 | GUID | Y |  |
| 77 | Attachments | 附件 | string | Y |  |
| 78 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 79 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 80 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 81 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 82 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 83 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 84 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 85 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 86 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 87 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 88 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 89 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 90 | UDF041 | 自定义字段12 | date | Y |  |
| 91 | UDF042 | 自定义字段13 | date | Y |  |
| 92 | UDF051 | 自定义字段14 | GUID | Y |  |
| 93 | UDF052 | 自定义字段15 | GUID | Y |  |
| 94 | UDF053 | 自定义字段16 | GUID | Y |  |
| 95 | UDF054 | 自定义字段17 | GUID | Y |  |
| 96 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 97 | Version | 版本号，不要随意更改 | binary | Y |  |
| 98 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 99 | ApproveDate | 修改日期 | date | Y |  |
| 100 | ApproveBy | 修改人 | GUID | Y |  |
| 101 | Owner_Org_RTK |  | string(400) | Y |  |
| 102 | Owner_Org_ROid |  | GUID | Y |  |

### SALES_FINANCE_INFO (销售出入库业务财务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALES_FINANCE_INFO_ID | 主键 | GUID | Y | Y |
| 4 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 5 | ORDER_CUSTOMER_ID | 订货客户 | GUID | Y |  |
| 6 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 7 | EMPLOYEE_ID | 业务员 | GUID | Y |  |
| 8 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 9 | COLLECTION_EMPLOYEE_ID | 收款业务员 | GUID | Y |  |
| 10 | COLLECTION_ADMIN_UNIT_ID | 收款业务部门 | GUID | Y |  |
| 11 | CURRENCY_ID | 货币 | GUID | Y |  |
| 12 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 13 | TAX_ID | 税种 | GUID | Y |  |
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

### SALES_ISSUE (销货出库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALES_ISSUE_ID |  | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | STOCK_ACTION | 库存影响 | number | Y |  |
| 12 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 13 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 14 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 15 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 16 | COMPANY_ID | 公司 | GUID | Y |  |
| 17 | SOURCE_UNCONFIRM | 源单撤审 | number(0/1) | Y |  |
| 18 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 19 | SIGN_REQUIRED | 需签收 | number(0/1) | Y |  |
| 20 | SIGN_DATE | 签收日期 | date | Y |  |
| 21 | SIGN_ACCOUNT_YEAR | 签收会计年度 | string(8) | Y |  |
| 22 | SIGN_ACCOUNT_PERIOD_SEQNO | 签收会计期间序号 | number | Y |  |
| 23 | SIGN_ACCOUNT_PERIOD_CODE | 签收会计期间期号 | string(20) | Y |  |
| 24 | GLOB_REVENUE_JE_INDICATOR | 已生成运营账簿收入分录 | number(0/1) | Y |  |
| 25 | GLOB_COST_JE_INDICATOR | 已生成运营账簿成本分录 | number(0/1) | Y |  |
| 26 | GLMB_REVENUE_JE_INDICATOR | 已生成管理账簿收入分录 | number(0/1) | Y |  |
| 27 | GLMB_COST_JE_INDICATOR | 已生成管理账簿成本分录 | number(0/1) | Y |  |
| 28 | GLOB_REVENUE_JE_ID | 运营账簿收入分录 | GUID | Y |  |
| 29 | GLOB_COST_JE_ID | 运营账簿成本分录 | GUID | Y |  |
| 30 | GLMB_REVENUE_JE_ID | 管理账簿收入分录 | GUID | Y |  |
| 31 | GLMB_COST_JE_ID | 管理账簿成本分录 | GUID | Y |  |
| 32 | VIEW_DOC_NO | 显示单号 | string(40) | Y |  |
| 33 | SUM_BUSINESS_QTY | 业务数量合计 | number(16,6) | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | PrintCount | 打印次数 | number | Y |  |
| 38 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 39 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 40 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 41 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 42 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 43 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 44 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 45 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 46 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 47 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 48 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 49 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 50 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 51 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 52 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 53 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 54 | UDF041 | 自定义字段12 | date | Y |  |
| 55 | UDF042 | 自定义字段13 | date | Y |  |
| 56 | UDF051 | 自定义字段14 | GUID | Y |  |
| 57 | UDF052 | 自定义字段15 | GUID | Y |  |
| 58 | UDF053 | 自定义字段16 | GUID | Y |  |
| 59 | UDF054 | 自定义字段17 | GUID | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
| 69 | Owner_Org_RTK |  | string(400) | Y |  |
| 70 | Owner_Org_ROid |  | GUID | Y |  |
| 71 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 72 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 73 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 74 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 75 | DOC_Sequence | 单据顺序 | number | Y |  |
| 76 | SOURCE_CUSTOMER_ID | 最终客户 | GUID | Y |  |
| 77 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 78 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |

### SALES_ISSUE_D (销货出库明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_ISSUE_D_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PIECES |  | number | Y |  |
| 14 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 15 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 16 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 17 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 18 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 19 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 20 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 21 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 22 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 23 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 24 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 25 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 26 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 27 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 28 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 29 | BIN_ID | 库位 | GUID | Y |  |
| 30 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 31 | SYNERGY_ID | 协同关系ID | GUID | Y |  |
| 32 | SYNERGY_D_ID | 协同序号ID | GUID | Y |  |
| 33 | PLAN_SETTLEMENT_DATE | 预计结算日期 | date | Y |  |
| 34 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 35 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 36 | VMI_SETTLED | VMI结算码 | string(80) | Y |  |
| 37 | SETTLEMENT_BUSINESS_QTY | 已结算业务数量 | number(16,6) | Y |  |
| 38 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 39 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额(原币) | number(23,8) | Y |  |
| 40 | SETTLEMENT_TAX_OC | 已结算税额(原币) | number(23,8) | Y |  |
| 41 | SETTLEMENT_AMT_UN_TAX_BC | 已结算无税金额(本币) | number(23,8) | Y |  |
| 42 | SETTLEMENT_TAX_BC | 已结算税额(本币) | number(23,8) | Y |  |
| 43 | DISCOUNT_UN_TAX_AMT_OC | 无税折扣额(原币) | number(23,8) | Y |  |
| 44 | DISCOUNT_IN_TAX_AMT_OC | 含税折扣额(原币) | number(23,8) | Y |  |
| 45 | DISCOUNT_UN_TAX_AMT_BC | 无税折扣额(本币) | number(23,8) | Y |  |
| 46 | DISCOUNT_IN_TAX_AMT_BC | 含税折扣额(本币) | number(23,8) | Y |  |
| 47 | SETTLE_DISC_UN_TAX_AMT_OC | 已结算无税折扣额(原币) | number(23,8) | Y |  |
| 48 | SETTLE_DISC_IN_TAX_AMT_OC | 已结算含税折扣额(原币) | number(23,8) | Y |  |
| 49 | SETTLE_DISC_UN_TAX_AMT_BC | 已结算无税折扣额(本币) | number(23,8) | Y |  |
| 50 | SETTLE_DISC_IN_TAX_AMT_BC | 已结算含税折扣额(本币) | number(23,8) | Y |  |
| 51 | PRICE |  | number(23,8) | Y |  |
| 52 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 53 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 54 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 55 | TAX_ID | 税种 | GUID | Y |  |
| 56 | TAX_RATE |  | number(5,4) | Y |  |
| 57 | AMOUNT |  | number(23,8) | Y |  |
| 58 | SIGN_TYPE | 签收状态 | string(40) | Y |  |
| 59 | SIGN_BUSINESS_QTY | 签收业务数量 | number(16,6) | Y |  |
| 60 | SIGN_PRICE_QTY | 签收计价数量 | number(16,6) | Y |  |
| 61 | RETURN_REASON_ID | 差异原因 | GUID | Y |  |
| 62 | LOSS_BUSINESS_QTY | 损耗认赔业务数量 | number(16,6) | Y |  |
| 63 | LOSS_PRICE_QTY | 损耗认赔计价数量 | number(16,6) | Y |  |
| 64 | CUST_INDEM_BUSINESS_QTY | 客户认赔业务数量 | number(16,6) | Y |  |
| 65 | CUST_INDEM_PRICE_QTY | 客户认赔计价数量 | number(16,6) | Y |  |
| 66 | RETURN_BUSINESS_QTY | 销退业务数量 | number(16,6) | Y |  |
| 67 | RETURN_PRICE_QTY | 销退计价数量 | number(16,6) | Y |  |
| 68 | SHOULD_SETTLE_COST_ACC | 应结算成本占比 | number(16,6) | Y |  |
| 69 | SHOULD_SETTLE_PRICE_QTY | 应结算计价数量 | number(16,6) | Y |  |
| 70 | SUBSEQUENT_PROCESSING | 后续处理 | string(510) | Y |  |
| 71 | PURCHASE_ARRIVALED | 已内部到货 | number(0/1) | Y |  |
| 72 | SYNERGY_TYPE | 协同关系类型 | number | Y |  |
| 73 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 74 | RE_SETTLEMENT_PATH_TYPE | 退货结算路径类型 | number | Y |  |
| 75 | SETTLEMENT_START_INDICATOR | 结算起点 | number(0/1) | Y |  |
| 76 | BC_CHECK_STATUS | 检核码 | string(40) | Y |  |
| 77 | PROJECT_ID | 项目 | GUID | Y |  |
| 78 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 79 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 80 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 81 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 82 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 83 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 84 | ApproveDate | 修改日期 | date | Y |  |
| 85 | ApproveBy | 修改人 | GUID | Y |  |
| 86 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 87 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 88 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 89 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 90 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 91 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 92 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 93 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 94 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 95 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 96 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 97 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 98 | UDF041 | 自定义字段12 | date | Y |  |
| 99 | UDF042 | 自定义字段13 | date | Y |  |
| 100 | UDF051 | 自定义字段14 | GUID | Y |  |
| 101 | UDF052 | 自定义字段15 | GUID | Y |  |
| 102 | UDF053 | 自定义字段16 | GUID | Y |  |
| 103 | UDF054 | 自定义字段17 | GUID | Y |  |
| 104 | CreateDate | 创建日期 | date | Y |  |
| 105 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 106 | ModifiedDate | 修改日期 | date | Y |  |
| 107 | CreateBy | 创建者 | GUID | Y |  |
| 108 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 109 | ModifiedBy | 修改者 | GUID | Y |  |
| 110 | Version | 版本号，不要随意更改 | binary | Y |  |
| 111 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 112 | SOURCE_ID_ROid |  | GUID | Y |  |
| 113 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 114 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
| 115 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 116 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 117 | ORDER_SOURCE_ID_RTK |  | string(400) | Y |  |
| 118 | ORDER_SOURCE_ID_ROid |  | GUID | Y |  |
| 119 | SALES_ISSUE_ID |  | GUID | Y |  |
| 120 | SYNERGY_SETTLEMENT_GROUP | 协同结算组号 | number | Y |  |
| 121 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 122 | SOURCE_ORDER_ROid |  | GUID | Y |  |

### SALES_ORDER_DOC (销售订单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALES_ORDER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ORDER_DATE | 订单日期 | date | Y |  |
| 8 | CATEGORY | 单据性质 | string(40) | Y |  |
| 9 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 10 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 11 | EARNEST_RATE |  | number(5,4) | Y |  |
| 12 | EARNEST | 订金 | number(23,8) | Y |  |
| 13 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 14 | IS_INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 15 | INSTALLMENT_SOURCE | 分期源单 | string(40) | Y |  |
| 16 | MULTI_DELIVERY | 多收货地址 | number(0/1) | Y |  |
| 17 | CUSTOMER_ADDR_NAME | 客户地址名称 | string(510) | Y |  |
| 18 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 19 | INVOICE_ADDR_NAME | 发票邮寄地址名称 | string(510) | Y |  |
| 20 | CUSTOMER_CONTACT_NAME | 客户联系人名称 | string(72) | Y |  |
| 21 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 22 | INVOICE_CONTACT_NAME | 发票邮寄联系人名称 | string(72) | Y |  |
| 23 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 24 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 25 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 26 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 27 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 28 | PIECES |  | number | Y |  |
| 29 | REMARK1 | 备注-业务 | string(510) | Y |  |
| 30 | REMARK2 | 备注-物流 | string(510) | Y |  |
| 31 | REMARK3 | 备注-财务 | string(510) | Y |  |
| 32 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算原币未税金额 | number(23,8) | Y |  |
| 33 | PRE_SETTLEMENT_TAX_OC | 预结算原币税额 | number(23,8) | Y |  |
| 34 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 35 | CUSTOMER_ADDR_ID | 客户地址 | GUID | Y |  |
| 36 | CUSTOMER_CONTACT_ID | 客户联系人 | GUID | Y |  |
| 37 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 38 | CURRENCY_ID | 币种 | GUID | Y |  |
| 39 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 40 | CONTRACT_ID | 销售合同 | GUID | Y |  |
| 41 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 42 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 43 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 44 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 45 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 46 | INVOICE_ADDR_ID | 发票邮寄地址 | GUID | Y |  |
| 47 | INVOICE_CONTACT_ID | 发票邮寄联系人 | GUID | Y |  |
| 48 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 49 | OFFSETED_AMT_UN_TAX_OC | 已冲减原币未税金额 | number(23,8) | Y |  |
| 50 | OFFSETED_TAX_OC | 已冲减原币税额 | number(23,8) | Y |  |
| 51 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 52 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 53 | ISSUED_AMT_UN_TAX_OC | 需结算已出库原币未税金额 | number(23,8) | Y |  |
| 54 | ISSUED_TAX_OC | 需结算已出库原币税额 | number(23,8) | Y |  |
| 55 | UNSETTLE_POFFSET_AMT_UN_TAX_OC | 未结算预冲减原币未税金额 | number(23,8) | Y |  |
| 56 | UNSETTLE_POFFSET_TAX_OC | 未结算预冲减原币税额 | number(23,8) | Y |  |
| 57 | UNSETTLE_DELY_AMT_UN_TAX_OC | 未结算已销货原币未税金额 | number(23,8) | Y |  |
| 58 | UNSETTLE_DELY_TAX_OC | 未结算已销货原币税额 | number(23,8) | Y |  |
| 59 | LETTER_CREDIT_ID | 信用证号码 | GUID | Y |  |
| 60 | AGENT_CUSTOMER_ID | 代理商 | GUID | Y |  |
| 61 | BROKERS_SUPPLIER_ID | 报关行 | GUID | Y |  |
| 62 | LOADING_PORT | 起始港口 | string(120) | Y |  |
| 63 | DESTINATION_PORT | 目的港口 | string(120) | Y |  |
| 64 | DESTINATION | 目的地 | string(120) | Y |  |
| 65 | INSPECTION_SUPPLIER_ID | 验货公司 | GUID | Y |  |
| 66 | TRANSPORT_SUPPLIER_ID | 运输公司 | GUID | Y |  |
| 67 | CONSIGNEE_CUSTOMER_ID | 进口方收货人信息 | GUID | Y |  |
| 68 | NOTIFY_CUSTOMER_ID | 进口方通知对象信息 | GUID | Y |  |
| 69 | CORRESPONDING_BANK_ID | 往来银行 | GUID | Y |  |
| 70 | NEGOTIATING_BANK_ID | 押汇银行 | GUID | Y |  |
| 71 | COMMISSION_RATE | 佣金比率 | number(5,4) | Y |  |
| 72 | INVOICE_REMARK | INVOICE备注 | string(510) | Y |  |
| 73 | PACKING_LIST_REMARK | PACKINGLIST备注 | string(510) | Y |  |
| 74 | CUSTOMER_SHIPPING_MARK_ID | 客户唛头 | GUID | Y |  |
| 75 | FRONT_MARK | 正唛 | string(510) | Y |  |
| 76 | FRONT_MARK_IS_PIC | 正唛用图片 | number(0/1) | Y |  |
| 77 | FRONT_MARK_PIC | 正唛图片 | string(120) | Y |  |
| 78 | SIDE_MARK | 侧唛 | string(510) | Y |  |
| 79 | SIDE_MARK_IS_PIC | 侧唛用图片 | number(0/1) | Y |  |
| 80 | SIDE_MARK_PIC | 侧唛图片 | string(120) | Y |  |
| 81 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 82 | PRICE_TERMS_ID | 价格条款 | GUID | Y |  |
| 83 | UNLIMITED_RELEASE | 超限放行 | number(0/1) | Y |  |
| 84 | TAX_ID | 税种 | GUID | Y |  |
| 85 | CLOSE | 结束码 | string(40) | Y |  |
| 86 | PROJECT_ID | 限用项目 | GUID | Y |  |
| 87 | CreateDate | 创建日期 | date | Y |  |
| 88 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 89 | ModifiedDate | 修改日期 | date | Y |  |
| 90 | CreateBy | 创建者 | GUID | Y |  |
| 91 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 92 | ModifiedBy | 修改者 | GUID | Y |  |
| 93 | Attachments | 附件 | string | Y |  |
| 94 | Version | 版本号，不要随意更改 | binary | Y |  |
| 95 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 96 | PrintCount | 打印次数 | number | Y |  |
| 97 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 98 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 99 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 100 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 101 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 102 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 103 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 104 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 105 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 106 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 107 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 108 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 109 | UDF041 | 自定义字段12 | date | Y |  |
| 110 | UDF042 | 自定义字段13 | date | Y |  |
| 111 | UDF051 | 自定义字段14 | GUID | Y |  |
| 112 | UDF052 | 自定义字段15 | GUID | Y |  |
| 113 | UDF053 | 自定义字段16 | GUID | Y |  |
| 114 | UDF054 | 自定义字段17 | GUID | Y |  |
| 115 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 116 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 117 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 118 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 119 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 120 | ApproveDate | 修改日期 | date | Y |  |
| 121 | ApproveBy | 修改人 | GUID | Y |  |
| 122 | Owner_Org_RTK |  | string(400) | Y |  |
| 123 | Owner_Org_ROid |  | GUID | Y |  |
| 124 | SO_EXPENSE_LOCK | 费用组成锁定 | number(0/1) | Y |  |
| 125 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 126 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 127 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 128 | DOC_Sequence | 单据顺序 | number | Y |  |
| 129 | SOURCE_CUSTOMER_ID | 最终客户 | GUID | Y |  |
| 130 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 131 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 132 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |
| 133 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 134 | SOURCE_ORDER_ROid |  | GUID | Y |  |

### SALES_ORDER_DOC_D (订单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_ORDER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | PLAN_DELIVERY_DATE | 预交货日 | date | Y |  |
| 13 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 14 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 16 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 17 | TAX_RATE |  | number(5,4) | Y |  |
| 18 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 19 | PIECES |  | number | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 22 | PRE_SETTLEMENT_PRICE_QTY | 预结算计价数量 | number(16,6) | Y |  |
| 23 | PRE_SETTLEMENT_BUSINESS_QTY | 预结算业务数量 | number(16,6) | Y |  |
| 24 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算无税金额 | number(23,8) | Y |  |
| 25 | PRE_SETTLEMENT_TAX_OC | 预结算税额 | number(23,8) | Y |  |
| 26 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 27 | SETTLEMENT_BUSINESS_QTY | 已结算业务数量 | number(16,6) | Y |  |
| 28 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额 | number(23,8) | Y |  |
| 29 | SETTLEMENT_TAX_OC | 已结算税额 | number(23,8) | Y |  |
| 30 | ISSUED_PRICE_QTY | 需结算已出库计价数量 | number(16,6) | Y |  |
| 31 | ITEM_ID | 品号 | GUID | Y |  |
| 32 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 33 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 34 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 35 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 36 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 37 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 38 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 39 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 40 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 41 | TAX_ID | 税种 | GUID | Y |  |
| 42 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 43 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 44 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 45 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 46 | PRICE |  | number(23,8) | Y |  |
| 47 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 48 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 49 | AMOUNT |  | number(23,8) | Y |  |
| 50 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 51 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 52 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 53 | OFFSETED_PRICE_QTY | 已冲减计价数量 | number(16,6) | Y |  |
| 54 | ORDER_PIC | 订单图片 | string(4000) | Y |  |
| 55 | KIT_DISTRIBUTION | 零组件配送 | number(0/1) | Y |  |
| 56 | PROJECT_ID | 项目 | GUID | Y |  |
| 57 | GROSS_WEIGHT | 毛重 | number(16,6) | Y |  |
| 58 | VOLUME | 材积 | number(16,6) | Y |  |
| 59 | DELIVER_AMOUNT | 已销货金额 | number(23,8) | Y |  |
| 60 | DELIVER_AMT_UN_TAX_OC | 已销货原币未税金额 | number(23,8) | Y |  |
| 61 | DELIVER_TAX_OC | 已销货原币税额 | number(23,8) | Y |  |
| 62 | DELIVER_AMT_UN_TAX_BC | 已销货本币未税金额 | number(23,8) | Y |  |
| 63 | DELIVER_TAX_BC | 已销货本币税额 | number(23,8) | Y |  |
| 64 | CreateDate | 创建日期 | date | Y |  |
| 65 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 66 | ModifiedDate | 修改日期 | date | Y |  |
| 67 | CreateBy | 创建者 | GUID | Y |  |
| 68 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 69 | ModifiedBy | 修改者 | GUID | Y |  |
| 70 | Version | 版本号，不要随意更改 | binary | Y |  |
| 71 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 72 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 73 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 74 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 75 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 76 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 77 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 78 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 79 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 80 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 81 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 82 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 83 | UDF041 | 自定义字段12 | date | Y |  |
| 84 | UDF042 | 自定义字段13 | date | Y |  |
| 85 | UDF051 | 自定义字段14 | GUID | Y |  |
| 86 | UDF052 | 自定义字段15 | GUID | Y |  |
| 87 | UDF053 | 自定义字段16 | GUID | Y |  |
| 88 | UDF054 | 自定义字段17 | GUID | Y |  |
| 89 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 90 | ApproveDate | 修改日期 | date | Y |  |
| 91 | ApproveBy | 修改人 | GUID | Y |  |
| 92 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 93 | SOURCE_ID_ROid |  | GUID | Y |  |
| 94 | SALES_ORDER_DOC_ID |  | GUID | Y |  |
| 95 | MFG_DESCRIPTION | 生产信息 | string(400) | Y |  |
| 96 | SALES_DESCRIPTION | 销售信息 | string(400) | Y |  |
| 97 | DEL_SO_D_ID | 原删除序号 | GUID | Y |  |
| 98 | PRODUCT_SUB_GROUP_ID | 替代群组主键 | GUID | Y |  |
| 99 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |
| 100 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 101 | SOURCE_ORDER_ROid |  | GUID | Y |  |

### SALES_ORDER_DOC_EXPENSE (订单费用组成)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_ORDER_DOC_EXPENSE_ID | 主键 | GUID | Y | Y |
| 3 | PRICE_TERMS_D_ID | 价格条款明细 | GUID | Y |  |
| 4 | AMOUNT |  | number(23,8) | Y |  |
| 5 | CALC_RATE | 比率 | number(5,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额(原币) | number(23,8) | Y |  |
| 8 | SETTLEMENT_TAX_OC | 已结算税额(原币) | number(23,8) | Y |  |
| 9 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
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
| 38 | SALES_ORDER_DOC_ID |  | GUID | Y |  |
| 39 | CURRENCY_ID | 币种 | GUID | Y |  |

### SALES_ORDER_DOC_INSTAL (订单分期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_ORDER_DOC_INSTAL_ID | 主键 | GUID | Y | Y |
| 3 | INSTALLMENT_NAME |  | string(60) | Y |  |
| 4 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 5 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 6 | ADV_RECEIVABLE_AMT_OC | 原币预收金额 | number(23,8) | Y |  |
| 7 | SETTLEMENT_AMT_OC | 原币已结算金额 | number(23,8) | Y |  |
| 8 | VERIFICATION_AMT_OC | 原币已核销金额 | number(23,8) | Y |  |
| 9 | BALANCE_AMT_OC | 原币未收余额 | number(23,8) | Y |  |
| 10 | CARRY_OUT_DATE | 执行日期 | date | Y |  |
| 11 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 12 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 13 | PAYMENT_DATE | 付款日 | date | Y |  |
| 14 | CASHING_DATE | 兑现日 | date | Y |  |
| 15 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 16 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 17 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 18 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 19 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 20 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 21 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 22 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 23 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 24 | TAX_ID | 税种 | GUID | Y |  |
| 25 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 26 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 27 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 28 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 29 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算原币未税金额 | number(23,8) | Y |  |
| 30 | PRE_SETTLEMENT_TAX_OC | 预结算原币税额 | number(23,8) | Y |  |
| 31 | OFFSETED_AMT_UN_TAX_OC | 已冲减原币未税金额 | number(23,8) | Y |  |
| 32 | OFFSETED_TAX_OC | 已冲减原币税额 | number(23,8) | Y |  |
| 33 | REMARK | 备注 | string(510) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | SALES_ORDER_DOC_ID |  | GUID | Y |  |

### SALES_ORDER_DOC_SD (发货计划)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_ORDER_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 4 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 5 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 13 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 14 | PLAN_DELIVERY_DATE | 预交货日 | date | Y |  |
| 15 | PLAN_SHIP_DATE | 预发货日 | date | Y |  |
| 16 | DELIVERY_TYPE | 供货类型 | string(40) | Y |  |
| 17 | DELIVERED_BUSINESS_QTY | 已交业务数量 | number(16,6) | Y |  |
| 18 | DELIVERED_PRICE_QTY | 已交计价数量 | number(16,6) | Y |  |
| 19 | CLOSE | 结束码 | string(40) | Y |  |
| 20 | PURCHASED_BUSINESS_QTY | 已转采业务数量 | number(16,6) | Y |  |
| 21 | PURCHASED_PRICE_QTY | 已转采计价数量 | number(16,6) | Y |  |
| 22 | TRANSFER_PURCHASE_STATUS | 转采结束码 | string(40) | Y |  |
| 23 | PLAN_STATUS | 计划状态 | string(40) | Y |  |
| 24 | RESERVED_BUSINESS_QTY | 已保留业务数量 | number(16,6) | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | PIECES |  | number | Y |  |
| 27 | DIRECT_SHIP | 直运 | number(0/1) | Y |  |
| 28 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 29 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 30 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 31 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 32 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 33 | DELIVERY_WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 34 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 35 | DELIVERY_PLANT_ID | 发货工厂/储运 | GUID | Y |  |
| 36 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
| 37 | DELIVER_BUSINESS_QTY | 已销货业务数量 | number(16,6) | Y |  |
| 38 | DELIVER_PRICE_QTY | 已销货计价数量 | number(16,6) | Y |  |
| 39 | KIT_WAREHOUSE_ID | 零组件接收仓库 | GUID | Y |  |
| 40 | BIN_ID | 库位 | GUID | Y |  |
| 41 | DISTRIBUTED_BUS_QTY | 已配送业务数量 | number(16,6) | Y |  |
| 42 | SETT_COMPANY_ID | 采购结算公司 | GUID | Y |  |
| 43 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 44 | PROJECT_ID | 项目 | GUID | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 70 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 71 | ApproveDate | 修改日期 | date | Y |  |
| 72 | ApproveBy | 修改人 | GUID | Y |  |
| 73 | DELIVERY_PARTNER_ID_RTK |  | string(400) | Y |  |
| 74 | DELIVERY_PARTNER_ID_ROid |  | GUID | Y |  |
| 75 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 76 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
| 77 | SALES_ORDER_DOC_D_ID |  | GUID | Y |  |
| 78 | INCLUDE_PLAN | 纳入计划 | number(0/1) | Y |  |
| 79 | TRANSACTION_PLANT_ID | 交易工厂 | GUID | Y |  |

### SALES_RECEIVABLE_BALANCE (销货应收余额档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALES_RECEIVABLE_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | LINE_TYPE | 行类型 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 8 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 9 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 10 | ORDER_CUSTOMER_ID | 订货客户 | GUID | Y |  |
| 11 | CURRENCY_ID | 货币 | GUID | Y |  |
| 12 | BALANCE_AMT_TC | 应收余额(原币) | number(23,8) | Y |  |
| 13 | BALANCE_AMT_FC | 应收余额(本币) | number(23,8) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 50 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE3_ID_ROid |  | GUID | Y |  |

### SALES_RETURN (销退单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALES_RETURN_ID | 主键 | GUID | Y | Y |
| 7 | SHIP_TO_ADDR_NAME | 收货地址 | string(510) | Y |  |
| 8 | TELEPHONE | 收货电话 | string(40) | Y |  |
| 9 | INVOICE_ADDR_NAME | 发票邮寄地址 | string(510) | Y |  |
| 10 | EXCHANGE_RATE | 匯率 | number(18,9) | Y |  |
| 11 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 12 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 13 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 14 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | PIECES |  | number | Y |  |
| 17 | TRANSACTION_DATE | 销退日期 | date | Y |  |
| 18 | CATEGORY | 单据性质 | string(40) | Y |  |
| 19 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 20 | INVOICE_CUSTOMER_FULL_NAME | 结算客户全称 | string(144) | Y |  |
| 21 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 22 | INVOICE_CONTACT_NAME | 发票邮寄联系人名称 | string(72) | Y |  |
| 23 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 24 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 25 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 26 | PLAN_SETTLEMENT_DATE | 预计结算日期 | date | Y |  |
| 27 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 28 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 29 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 30 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 31 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 32 | CURRENCY_ID | 币种 | GUID | Y |  |
| 33 | PLANT_ID | 退货工厂/储运 | GUID | Y |  |
| 34 | WAREHOUSE_ID | 限定仓库 | GUID | Y |  |
| 35 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 36 | RECEIVER_ID | 收款业务员 | GUID | Y |  |
| 37 | SHIP_TO_ADDR_ID | 收货地址编号 | GUID | Y |  |
| 38 | INVOICE_ADDR_ID | 发票邮寄地址编号 | GUID | Y |  |
| 39 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 40 | INVOICE_COMPANY_ID |  | GUID | Y |  |
| 41 | INVOICE_CONTACT_ID |  | GUID | Y |  |
| 42 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 43 | SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 44 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 45 | DIRECT_INVOICING_INDICATOR | 直接开票 | number(0/1) | Y |  |
| 46 | RECEIPTED_STATUS | 入库状态 | string(40) | Y |  |
| 47 | SETTLEMENT_INDICATOR | 当前可结算 | number(0/1) | Y |  |
| 48 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 49 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 50 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 51 | JOURNAL_ENTRY_ID | 运营账簿分录 | GUID | Y |  |
| 52 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 53 | INSPECT_MODE | 质检模式 | string(40) | Y |  |
| 54 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 55 | TAX_ID | 税种 | GUID | Y |  |
| 56 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 57 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 58 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 59 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 69 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 70 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 71 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 72 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 73 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 74 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 75 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 76 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 77 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 78 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 79 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 80 | UDF041 | 自定义字段12 | date | Y |  |
| 81 | UDF042 | 自定义字段13 | date | Y |  |
| 82 | UDF051 | 自定义字段14 | GUID | Y |  |
| 83 | UDF052 | 自定义字段15 | GUID | Y |  |
| 84 | UDF053 | 自定义字段16 | GUID | Y |  |
| 85 | UDF054 | 自定义字段17 | GUID | Y |  |
| 86 | Version | 版本号，不要随意更改 | binary | Y |  |
| 87 | PrintCount | 打印次数 | number | Y |  |
| 88 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 89 | ApproveDate | 修改日期 | date | Y |  |
| 90 | ApproveBy | 修改人 | GUID | Y |  |
| 91 | Owner_Org_RTK |  | string(400) | Y |  |
| 92 | Owner_Org_ROid |  | GUID | Y |  |
| 93 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 94 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 95 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 96 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 97 | DOC_Sequence | 单据顺序 | number | Y |  |
| 98 | SOURCE_CUSTOMER_ID | 最终客户 | GUID | Y |  |
| 99 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 100 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |

### SALES_RETURN_D (销退单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_RETURN_D_ID | 主键 | GUID | Y | Y |
| 3 | SALES_RETURN_TYPE | 销退类型 | string(40) | Y |  |
| 4 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 10 | PRICE |  | number(23,8) | Y |  |
| 11 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 12 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 13 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 14 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 15 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 16 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 17 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 18 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 20 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 21 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 22 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 23 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 24 | PRICE_TABLE_ID | 价格表编号 | GUID | Y |  |
| 25 | DISCOUNT_TABLE_ID | 折扣表编号 | GUID | Y |  |
| 26 | TAX_ID | 税种 | GUID | Y |  |
| 27 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 28 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 29 | TAX_RATE |  | number(5,4) | Y |  |
| 30 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 31 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 32 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 33 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 34 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 35 | REMARK | 备注 | string(510) | Y |  |
| 36 | DEDUCT_QTY | 扣已交量 | number(0/1) | Y |  |
| 37 | PIECES |  | number | Y |  |
| 38 | RECEIPTED_BUSINESS_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 39 | SALES_BUSINESS_QTY | 已换业务数量 | number(16,6) | Y |  |
| 40 | RECEIPTED | 已入库 | string(40) | Y |  |
| 41 | AMOUNT |  | number(23,8) | Y |  |
| 42 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额(原币) | number(23,8) | Y |  |
| 43 | SETTLEMENT_TAX_OC | 已结算税额(原币) | number(23,8) | Y |  |
| 44 | SETTLEMENT_AMT_UN_TAX_BC | 已结算无税金额(本币) | number(23,8) | Y |  |
| 45 | SETTLEMENT_TAX_BC | 已结算税额(本币) | number(23,8) | Y |  |
| 46 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 47 | RECEIPTED_PRICE_QTY | 已入库计价数量 | number(16,6) | Y |  |
| 48 | ORDER_SOURCE_ID | 来源订单 | GUID | Y |  |
| 49 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 50 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 51 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 52 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 53 | RETURN_REASON_ID | 退货原因 | GUID | Y |  |
| 54 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 55 | WAREHOUSE_ID | 退货仓库 | GUID | Y |  |
| 56 | BIN_ID | 库位 | GUID | Y |  |
| 57 | ITEM_LOT_ID | 主键 | GUID | Y |  |
| 58 | SALES_ORDER_DOC_ID | 销售订单主键 | GUID | Y |  |
| 59 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 60 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 61 | INSPECT_MODE | 质检模式 | string(40) | Y |  |
| 62 | ACCEPTED_BUSINESS_QTY | 允收业务数量 | number(16,6) | Y |  |
| 63 | SCRAP_BUSINESS_QTY | 报废业务数量 | number(16,6) | Y |  |
| 64 | SP_RECEIPT_BUSINESS_QTY | 让步接收业务数量 | number(16,6) | Y |  |
| 65 | QUALIFIED_BUSINESS_QTY | 合格业务数量 | number(16,6) | Y |  |
| 66 | UNQUALIFIED_BUSINESS_QTY | 不合格业务数量 | number(16,6) | Y |  |
| 67 | IN_DESTROYED_BUSINESS_QTY | 检验破坏业务数量 | number(16,6) | Y |  |
| 68 | INSPECTION_STATUS | 检验状态 | string(40) | Y |  |
| 69 | JUDGED_QTY | 已判定业务数量 | number(16,6) | Y |  |
| 70 | SCRAPED_BUSINESS_QTY | 已报废业务数量 | number(16,6) | Y |  |
| 71 | INSPECTED_QTY | 已检验业务数量 | number(16,6) | Y |  |
| 72 | PROJECT_ID | 项目 | GUID | Y |  |
| 73 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 74 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 75 | CreateDate | 创建日期 | date | Y |  |
| 76 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 77 | ModifiedDate | 修改日期 | date | Y |  |
| 78 | CreateBy | 创建者 | GUID | Y |  |
| 79 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 80 | ModifiedBy | 修改者 | GUID | Y |  |
| 81 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 82 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 83 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 84 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 85 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 86 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 87 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 88 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 89 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 90 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 91 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 92 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 93 | UDF041 | 自定义字段12 | date | Y |  |
| 94 | UDF042 | 自定义字段13 | date | Y |  |
| 95 | UDF051 | 自定义字段14 | GUID | Y |  |
| 96 | UDF052 | 自定义字段15 | GUID | Y |  |
| 97 | UDF053 | 自定义字段16 | GUID | Y |  |
| 98 | UDF054 | 自定义字段17 | GUID | Y |  |
| 99 | Version | 版本号，不要随意更改 | binary | Y |  |
| 100 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 101 | ApproveDate | 修改日期 | date | Y |  |
| 102 | ApproveBy | 修改人 | GUID | Y |  |
| 103 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 104 | SOURCE_ID_ROid |  | GUID | Y |  |
| 105 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 106 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 107 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 108 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 109 | SALES_RETURN_ID |  | GUID | Y |  |
| 110 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 111 | SOURCE_ORDER_ROid |  | GUID | Y |  |
| 112 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 113 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |

### SALES_RETURN_RECEIPT (销退入库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALES_RETURN_RECEIPT_ID |  | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | STOCK_ACTION | 库存影响 | number | Y |  |
| 12 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 13 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 14 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 15 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 16 | COMPANY_ID | 公司 | GUID | Y |  |
| 17 | GLOB_REVENUE_JE_INDICATOR | 已生成运营账簿收入分录 | number(0/1) | Y |  |
| 18 | GLOB_REVENUE_JE_ID | 运营账簿收入分录 | GUID | Y |  |
| 19 | GLOB_COST_JE_INDICATOR | 已生成运营账簿成本分录 | number(0/1) | Y |  |
| 20 | GLOB_COST_JE_ID | 运营账簿成本分录 | GUID | Y |  |
| 21 | GLMB_REVENUE_JE_INDICATOR | 已生成管理账簿收入分录 | number(0/1) | Y |  |
| 22 | GLMB_REVENUE_JE_ID | 管理账簿收入分录 | GUID | Y |  |
| 23 | GLMB_COST_JE_INDICATOR | 已生成管理账簿成本分录 | number(0/1) | Y |  |
| 24 | GLMB_COST_JE_ID | 管理账簿成本分录 | GUID | Y |  |
| 25 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 26 | SOURCE_UNCONFIRM | 源单撒审 | number(0/1) | Y |  |
| 27 | VIEW_DOC_NO | 显示单号 | string(40) | Y |  |
| 28 | SUM_BUSINESS_QTY | 业务数量合计 | number(16,6) | Y |  |
| 29 | PrintCount | 打印次数 | number | Y |  |
| 30 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 31 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 32 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 33 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 43 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 44 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 45 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 46 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 47 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 48 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 49 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 50 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 51 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 52 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 53 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 54 | UDF041 | 自定义字段12 | date | Y |  |
| 55 | UDF042 | 自定义字段13 | date | Y |  |
| 56 | UDF051 | 自定义字段14 | GUID | Y |  |
| 57 | UDF052 | 自定义字段15 | GUID | Y |  |
| 58 | UDF053 | 自定义字段16 | GUID | Y |  |
| 59 | UDF054 | 自定义字段17 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |
| 66 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 67 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 68 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 69 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 70 | DOC_Sequence | 单据顺序 | number | Y |  |
| 71 | SOURCE_CUSTOMER_ID | 最终客户 | GUID | Y |  |
| 72 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 73 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |

### SALES_RETURN_RECEIPT_D (销退入库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_RETURN_RECEIPT_D_ID |  | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 8 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | PIECES |  | number | Y |  |
| 15 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 16 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 17 | PLAN_SETTLEMENT_DATE | 预计结算日期 | date | Y |  |
| 18 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 19 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 20 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 21 | SYNERGY_ID | 协同关系ID | GUID | Y |  |
| 22 | SYNERGY_D_ID | 协同序号ID | GUID | Y |  |
| 23 | VMI_SETTLED | VMI结算码 | string(40) | Y |  |
| 24 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 25 | DISCOUNT_IN_TAX_AMT_BC | 含税折扣额(本币) | number(23,8) | Y |  |
| 26 | DISCOUNT_IN_TAX_AMT_OC | 含税折扣额(原币) | number(23,8) | Y |  |
| 27 | DISCOUNT_UN_TAX_AMT_BC | 无税折扣额(本币) | number(23,8) | Y |  |
| 28 | DISCOUNT_UN_TAX_AMT_OC | 无税折扣额(原币) | number(23,8) | Y |  |
| 29 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额(原币) | number(23,8) | Y |  |
| 30 | SETTLEMENT_BUSINESS_QTY | 已结算业务数量 | number(16,6) | Y |  |
| 31 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 32 | SETTLEMENT_TAX_OC | 已结算税额(原币) | number(23,8) | Y |  |
| 33 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 34 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 35 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 36 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 37 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 38 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 39 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 40 | ITEM_ID | 品号 | GUID | Y |  |
| 41 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 42 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 43 | BIN_ID | 库位 | GUID | Y |  |
| 44 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 45 | SETTLE_DISC_UN_TAX_AMT_OC | 已结算无税折扣额(原币) | number(23,8) | Y |  |
| 46 | SETTLE_DISC_IN_TAX_AMT_OC | 已结算含税折扣额(原币) | number(23,8) | Y |  |
| 47 | SETTLE_DISC_UN_TAX_AMT_BC | 已结算无税折扣额(本币) | number(23,8) | Y |  |
| 48 | SETTLE_DISC_IN_TAX_AMT_BC | 已结算含税折扣额(本币) | number(23,8) | Y |  |
| 49 | SETTLEMENT_AMT_UN_TAX_BC | 已结算无税金额(本币) | number(23,8) | Y |  |
| 50 | SETTLEMENT_TAX_BC | 已结算税额(本币) | number(23,8) | Y |  |
| 51 | SYNERGY_TYPE | 协同关系类型 | number | Y |  |
| 52 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 53 | RE_SETTLEMENT_PATH_TYPE | 退货结算路径类型 | number | Y |  |
| 54 | SETTLEMENT_START_INDICATOR | 结算起点 | number(0/1) | Y |  |
| 55 | PROJECT_ID | 项目 | GUID | Y |  |
| 56 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 57 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 58 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 59 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 60 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 61 | CreateDate | 创建日期 | date | Y |  |
| 62 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 63 | ModifiedDate | 修改日期 | date | Y |  |
| 64 | CreateBy | 创建者 | GUID | Y |  |
| 65 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 66 | ModifiedBy | 修改者 | GUID | Y |  |
| 67 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 68 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 69 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 70 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 71 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 72 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 73 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 74 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 75 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 76 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 77 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 78 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 79 | UDF041 | 自定义字段12 | date | Y |  |
| 80 | UDF042 | 自定义字段13 | date | Y |  |
| 81 | UDF051 | 自定义字段14 | GUID | Y |  |
| 82 | UDF052 | 自定义字段15 | GUID | Y |  |
| 83 | UDF053 | 自定义字段16 | GUID | Y |  |
| 84 | UDF054 | 自定义字段17 | GUID | Y |  |
| 85 | Version | 版本号，不要随意更改 | binary | Y |  |
| 86 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 87 | ApproveDate | 修改日期 | date | Y |  |
| 88 | ApproveBy | 修改人 | GUID | Y |  |
| 89 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 90 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
| 91 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 92 | SOURCE_ID_ROid |  | GUID | Y |  |
| 93 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 94 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 95 | ORDER_SOURCE_ID_RTK |  | string(400) | Y |  |
| 96 | ORDER_SOURCE_ID_ROid |  | GUID | Y |  |
| 97 | SALES_RETURN_RECEIPT_ID |  | GUID | Y |  |
| 98 | SYNERGY_SETTLEMENT_GROUP | 协同结算组号 | number | Y |  |
| 99 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 100 | SOURCE_ORDER_ROid |  | GUID | Y |  |

### SALES_SYNERGY (销售协同关系信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALES_SYNERGY_ID | 主键 | GUID | Y | Y |
| 4 | SALES_SYNERGY_CODE | 协同关系编号 | string(20) | Y |  |
| 5 | SALES_SYNERGY_NAME | 协同关系名称 | string(40) | Y |  |
| 6 | SALES_TYPE | 销售协同类型 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 9 | DELIVERY_PLANT_ID | 发货工厂/储运 | GUID | Y |  |
| 10 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 11 | SETTLEMENT_SOURCE | 一段式立账发起方 | number | Y |  |
| 12 | INDEPENDENT_SETTLEMENT | 结算公司对外独立立账 | number(0/1) | Y |  |
| 13 | RECEIVABLE_DOC_ID | 结算公司应收单类型 | GUID | Y |  |
| 14 | MAIN | 主要协同关系 | number(0/1) | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |
| 47 | GENERATE_DIRE | 抛转方向,1正抛;2逆抛 | string(40) | Y |  |
| 48 | GENERATE_AUTO | 自动抛转 | number(0/1) | Y |  |
| 49 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 50 | OUT_SD_ID | 对外销货单 | GUID | Y |  |
| 51 | OUT_SR_ID | 对外销退单 | GUID | Y |  |

### SALES_SYNERGY_FI_D (销售协同结算路径明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_SYNERGY_FI_D_ID | 主键 | GUID | Y | Y |
| 3 | PRICE_RATE | 比例 | number(5,4) | Y |  |
| 4 | PRICE_MODE | 取价方式 | string(40) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 7 | SETTLEMENT_SOURCE | 内部结算发起方 | string(80) | Y |  |
| 8 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 11 | TO_PLANT_ID | 调入工厂/储运 | GUID | Y |  |
| 12 | TO_COMPANY_ID | 调入公司 | GUID | Y |  |
| 13 | TO_WAREHOUSE_ID | 调入仓库 | GUID | Y |  |
| 14 | FROM_PLANT_ID | 调出工厂/储运 | GUID | Y |  |
| 15 | FROM_COMPANY_ID | 调出公司 | GUID | Y |  |
| 16 | FROM_WAREHOUSE_ID | 调出仓库 | GUID | Y |  |
| 17 | CURRENCY_ID | 币种 | GUID | Y |  |
| 18 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 19 | PURCHASE_RECEIPT_DOC_ID | 调入工厂/储运采购入库单 | GUID | Y |  |
| 20 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 21 | SALES_ISSUE_DOC_ID | 调入工厂/储运销售出库单 | GUID | Y |  |
| 22 | RE_PURCHASE_RECEIPT_DOC_ID | 调入工厂/储运采购退货出库单 | GUID | Y |  |
| 23 | RE_SALES_ISSUE_DOC_ID | 调入工厂/储运销售销退入库单 | GUID | Y |  |
| 24 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 25 | RE_SETTLEMENT_PATH_TYPE | 退货结算路径类型 | number | Y |  |
| 26 | RECEIVABLE_DOC_ID | 应收单类型 | GUID | Y |  |
| 27 | PAYABLE_DOC_ID | 应付单类型 | GUID | Y |  |
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
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | SALES_SYNERGY_ID |  | GUID | Y |  |
| 57 | TO_PR_ID | 调入方采购退货单 | GUID | Y |  |
| 58 | FROM_SR_ID | 调出方销退单 | GUID | Y |  |
| 59 | TO_PO_ID | 调入方采购订单 | GUID | Y |  |
| 60 | FROM_SO_ID | 调出方销售订单 | GUID | Y |  |
| 61 | TO_PA_ID | 调入方到货单 | GUID | Y |  |
| 62 | FROM_SD_ID | 调出方销货单 | GUID | Y |  |

### SALES_SYNERGY_SD (销售协同关系信息)

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
| 9 | SALES_SYNERGY_SD_ID | 主键 | GUID | Y | Y |
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
| 38 | SALES_SYNERGY_FI_D_ID |  | GUID | Y |  |