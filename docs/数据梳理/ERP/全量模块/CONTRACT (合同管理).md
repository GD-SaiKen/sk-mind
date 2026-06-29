---
module: "CONTRACT"
name_zh: "合同管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 318
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# CONTRACT (合同管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 5 | Columns: 318

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]
- [[DISCOUNT (折扣表)|DISCOUNT (折扣表)]]

---

## Tables


- **CONTRACT_D (销售合同明细)**
- **CONTRACT_INSTAL (销售合同分期)**
- **CONTRACT_SCOPE (合同控制范围)**
- **CONTRACT_SD (销售合同发货计划)**


---


---


> Tables: 5

### CONTRACT (销售合同)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CONTRACT_ID | 主键 | GUID | Y | Y |
| 7 | APPROVE_DATE | 审核日期 | date | Y |  |
| 8 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
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
| 24 | ORDERED_AMT | 已订原币总金额 | number(23,8) | Y |  |
| 25 | ORDERED_BUSINESS_QTY | 已订业务数量 | number(16,6) | Y |  |
| 26 | PIECES |  | number | Y |  |
| 27 | QTY_UPPER_LIMIT | 上限总数量 | number(16,6) | Y |  |
| 28 | CUSTOMER_ADDR_NAME | 客户地址 | string(510) | Y |  |
| 29 | CUSTOMER_CONTACT_NAME | 客户联系人 | string(72) | Y |  |
| 30 | CUSTOMER_FULL_NAME | 客户全称 | string(144) | Y |  |
| 31 | CONTRACT_DESCRIPTION | 合同名称 | string(144) | Y |  |
| 32 | IS_INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 33 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 34 | INVOICE_CONTACT_NAME | 结算联系人 | string(72) | Y |  |
| 35 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 36 | MULTI_DELIVERY | 多收货地址 | number(0/1) | Y |  |
| 37 | INVOICE_CUSTOMER_FULL_NAME | 结算客户全称 | string(144) | Y |  |
| 38 | SHIP_TO_CUSTOMER_ADDR_NAME | 收货地址 | string(510) | Y |  |
| 39 | SHIP_TO_CUSTOMER_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 40 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 41 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 42 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 43 | CURRENCY_ID | 币种 | GUID | Y |  |
| 44 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 45 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 46 | CUSTOMER_ADDR_ID | 地址编码 | GUID | Y |  |
| 47 | CUSTOMER_CONTACT_ID | 联系人编码 | GUID | Y |  |
| 48 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 49 | INVOICE_ADDR_ID | 结算地址编码 | GUID | Y |  |
| 50 | INVOICE_CONTACT_ID | 结算联系人编码 | GUID | Y |  |
| 51 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 52 | SHIP_TO_CUSTOMER_ADDR_ID | 收货地址ID | GUID | Y |  |
| 53 | SHIP_TO_CUSTOMER_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 54 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 55 | TAX_ID | 税种 | GUID | Y |  |
| 56 | PROJECT_ID | 项目 | GUID | Y |  |
| 57 | PrintCount | 打印次数 | number | Y |  |
| 58 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 59 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 60 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 61 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 62 | CreateDate | 创建日期 | date | Y |  |
| 63 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 64 | ModifiedDate | 修改日期 | date | Y |  |
| 65 | CreateBy | 创建者 | GUID | Y |  |
| 66 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 67 | ModifiedBy | 修改者 | GUID | Y |  |
| 68 | Attachments | 附件 | string | Y |  |
| 69 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 70 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 71 | ApproveDate | 修改日期 | date | Y |  |
| 72 | ApproveBy | 修改人 | GUID | Y |  |
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
| 91 | Version | 版本号，不要随意更改 | binary | Y |  |
| 92 | Owner_Org_RTK |  | string(400) | Y |  |
| 93 | Owner_Org_ROid |  | GUID | Y |  |

### CONTRACT_D (销售合同明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CONTRACT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 6 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 7 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 10 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 11 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 12 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 13 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 14 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 21 | PRICE | 单价 | number(23,8) | Y |  |
| 22 | ORDERED_BUSINESS_QTY | 已订业务数量 | number(16,6) | Y |  |
| 23 | QTY_LIMIT | 数量限制 | number(0/1) | Y |  |
| 24 | AMT_LIMIT | 金额限制 | number(0/1) | Y |  |
| 25 | BUSINESS_QTY_UPPER_LIMIT | 业务数量上限 | number(16,6) | Y |  |
| 26 | AMT_OC_UPPER_LIMIT | 原币金额上限 | number(23,8) | Y |  |
| 27 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 28 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 29 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 30 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 31 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 32 | AMOUNT |  | number(23,8) | Y |  |
| 33 | ORDERED_AMT | 已订原币金额 | number(23,8) | Y |  |
| 34 | CLOSE | 结束码 | string(40) | Y |  |
| 35 | PRICE_LIMIT | 单价控制 | number(0/1) | Y |  |
| 36 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 37 | FEATURE_VALUE | 品类值属性值 | string(40) | Y |  |
| 38 | FEATURE_VALUE_DESC | 品类描述属性值描述 | string(120) | Y |  |
| 39 | PIECES |  | number | Y |  |
| 40 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 41 | DELIVERY_DATE | 预交货日 | date | Y |  |
| 42 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 43 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 44 | ORDERED_PRICE_QTY | 已订计价数量 | number(16,6) | Y |  |
| 45 | TAX_ID | 税种 | GUID | Y |  |
| 46 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 47 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 48 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 49 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 50 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 51 | FEATURE_ID | 品类属性项ID | GUID | Y |  |
| 52 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 53 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 54 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 55 | PROJECT_ID | 项目 | GUID | Y |  |
| 56 | CreateDate | 创建日期 | date | Y |  |
| 57 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 58 | ModifiedDate | 修改日期 | date | Y |  |
| 59 | CreateBy | 创建者 | GUID | Y |  |
| 60 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 61 | ModifiedBy | 修改者 | GUID | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
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
| 83 | Version | 版本号，不要随意更改 | binary | Y |  |
| 84 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 85 | SOURCE_ID_ROid |  | GUID | Y |  |
| 86 | CONTRACT_ID |  | GUID | Y |  |
| 87 | PRODUCT_SUB_GROUP_ID | 替代群组主键 | GUID | Y |  |
| 88 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |

### CONTRACT_INSTAL (销售合同分期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INSTALLMENT_NAME |  | string(60) | Y |  |
| 3 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 4 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 5 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 6 | PAYMENT_DATE | 付款日 | date | Y |  |
| 7 | CASHING_DATE | 兑现日 | date | Y |  |
| 8 | DISCOUNT_INDICATOR | 取得折扣标识 | number(0/1) | Y |  |
| 9 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 10 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 11 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 12 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 13 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 14 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 15 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 16 | CONTRACT_INSTAL_ID | 主键 | GUID | Y | Y |
| 17 | ADV_RECEIVABLE_AMT_OC | 原币预收金额 | number(23,8) | Y |  |
| 18 | BALANCE_AMT_OC | 原币未收余额 | number(23,8) | Y |  |
| 19 | CARRY_OUT_DATE | 执行日期 | date | Y |  |
| 20 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 21 | SETTLEMENT_AMT_OC | 原币已结算金额 | number(23,8) | Y |  |
| 22 | VERIFICATION_AMT_OC | 原币已核销金额 | number(23,8) | Y |  |
| 23 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
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
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | CONTRACT_ID |  | GUID | Y |  |

### CONTRACT_SCOPE (合同控制范围)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CONTRACT_SCOPE_ID | 主键 | GUID | Y | Y |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 5 | COMPANY_ID | 公司 | GUID | Y |  |
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
| 34 | PURCHASE_CONTRACT_ID |  | GUID | Y |  |

### CONTRACT_SD (销售合同发货计划)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CONTRACT_SD_ID | 主键 | GUID | Y | Y |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | ORDERED_BUSINESS_QTY | 已订业务数量 | number(16,6) | Y |  |
| 5 | ORDERED_PRICE_QTY | 已订计价数量 | number(16,6) | Y |  |
| 6 | DELIVERY_DATE | 预交货日 | date | Y |  |
| 7 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 13 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 14 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 15 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 16 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 17 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 18 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 19 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 20 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 21 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 29 | ApproveDate | 修改日期 | date | Y |  |
| 30 | ApproveBy | 修改人 | GUID | Y |  |
| 31 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 32 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 33 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 34 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 35 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 36 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 37 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 38 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 39 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 40 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 41 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 42 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 43 | UDF041 | 自定义字段12 | date | Y |  |
| 44 | UDF042 | 自定义字段13 | date | Y |  |
| 45 | UDF051 | 自定义字段14 | GUID | Y |  |
| 46 | UDF052 | 自定义字段15 | GUID | Y |  |
| 47 | UDF053 | 自定义字段16 | GUID | Y |  |
| 48 | UDF054 | 自定义字段17 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | CONTRACT_D_ID |  | GUID | Y |  |