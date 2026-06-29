---
module: "QUOTATION"
name_zh: "报价管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 242
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# QUOTATION (报价管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 5 | Columns: 242

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


- **QUOTATION_D (报价单单身)**
- **QUOTATION_PRICE_DETAILS (报价单价格明细)**
- **QUOTATION_PRICE_ITEMS (报价单价格组成)**
- **QUOTATION_SD (报价单子单身)**


---


---


> Tables: 5

### QUOTATION (报价单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | QUOTATION_ID | 主键 | GUID | Y | Y |
| 7 | EXPIRY_TIME | 有效期间 | string(100) | Y |  |
| 8 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 9 | CUSTOMER_CONFIRM | 客户确认 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CATEGORY | 单据性质 | string(40) | Y |  |
| 12 | QUOTATION_DATE | 报价日期 | date | Y |  |
| 13 | AMOUNT_UNINCLUDE_TAX | 未税金额 | number(23,8) | Y |  |
| 14 | TAX | 税额 | number(23,8) | Y |  |
| 15 | QUOTATION_DESC | 价格说明 | string(510) | Y |  |
| 16 | CLOSE | 结束码 | number(0/1) | Y |  |
| 17 | CUSTOMER_FULL_NAME | 客户全称 | string(144) | Y |  |
| 18 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 19 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 20 | CURRENCY_ID | 币种 | GUID | Y |  |
| 21 | TAX_REGION_ID |  | GUID | Y |  |
| 22 | PRICE_TERMS_ID | 价格条款 | GUID | Y |  |
| 23 | TAX_ID | 税种 | GUID | Y |  |
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
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |
| 61 | PRICE_TERMS1_ID | 价格条款一 | GUID | Y |  |
| 62 | PRICE_TERMS2_ID | 价格条款二 | GUID | Y |  |

### QUOTATION_D (报价单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | QUOTATION_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 6 | COMPONENT_PRICE | 分量计价 | number(0/1) | Y |  |
| 7 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 8 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 9 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 10 | PRICE | 單價 | number(23,8) | Y |  |
| 11 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 12 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 13 | TAX_RATE |  | number(5,4) | Y |  |
| 14 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 15 | COSTOMER_CONFIRM | 客户确认 | number(0/1) | Y |  |
| 16 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 17 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | AMOUNT_UNINCLUDE_TAX | 未税金额 | number(23,8) | Y |  |
| 20 | TAX | 税额 | number(23,8) | Y |  |
| 21 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 22 | AMOUNT |  | number(23,8) | Y |  |
| 23 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 24 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 25 | TAX_ID | 税种 | GUID | Y |  |
| 26 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 27 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 28 | ITEM_ID | 品号 | GUID | Y |  |
| 29 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 30 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 31 | PROJECT_ID | 项目 | GUID | Y |  |
| 32 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 33 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 34 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 35 | GROSS_WEIGHT | 毛重 | number(16,6) | Y |  |
| 36 | VOLUME | 材积 | number(16,6) | Y |  |
| 37 | PIECES | 件数 | number | Y |  |
| 38 | CLOSE | 结束码 | string(40) | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |
| 67 | QUOTATION_ID |  | GUID | Y |  |
| 68 | PRICE1 | 单价一 | number(23,8) | Y |  |
| 69 | PRICE2 | 单价二 | number(23,8) | Y |  |
| 70 | AMOUNT1 | 金额一 | number(23,8) | Y |  |
| 71 | AMOUNT2 | 金额二 | number(23,8) | Y |  |
| 72 | PRODUCT_SUB_GROUP_ID | 替代群组主键 | GUID | Y |  |
| 73 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |

### QUOTATION_PRICE_DETAILS (报价单价格明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | QUOTATION_PRICE_DETAILS_ID | 主键 | GUID | Y | Y |
| 3 | PRICE_TERMS_D_ID | 价格条款明细 | GUID | Y |  |
| 4 | PRICE | 价格 | number(23,8) | Y |  |
| 5 | CALC_RATE | 比率 | number(5,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | QUOTATION_D_ID |  | GUID | Y |  |
| 36 | PRICE_CODE | 单价类型 | string(40) | Y |  |

### QUOTATION_PRICE_ITEMS (报价单价格组成)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | QUOTATION_PRICE_ITEMS_ID | 主键 | GUID | Y | Y |
| 3 | PRICE_TERMS_D_ID | 价格条款明细 | GUID | Y |  |
| 4 | AMOUNT | 金额 | number(23,8) | Y |  |
| 5 | CALC_RATE | 比率 | number(5,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | QUOTATION_ID |  | GUID | Y |  |
| 36 | CURRENCY_ID | 币种 | GUID | Y |  |
| 37 | EXPENSE_SOURCE | 费用组成来源 | string(40) | Y |  |

### QUOTATION_SD (报价单子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | QUOTATION_SD_ID | 主键 | GUID | Y | Y |
| 2 | MIN_QTY | 最小数量 | number(16,6) | Y |  |
| 3 | MAX_QTY | 最大数量 | number(16,6) | Y |  |
| 4 | PRICE | 單價 | number(23,8) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | Version | 版本号，不要随意更改 | binary | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | QUOTATION_D_ID |  | GUID | Y |  |