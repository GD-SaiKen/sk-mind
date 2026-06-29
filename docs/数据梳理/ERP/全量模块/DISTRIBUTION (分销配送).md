---
module: "DISTRIBUTION"
name_zh: "分销配送"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 9
columns: 440
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# DISTRIBUTION (分销配送)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 9 | Columns: 440

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


- **DISTRIBUTION_D (配送单身)**
- **DISTRIBUTION_LIST (配送清单)**
- **DISTRIBUTION_OBJECT (配送对象信息)**
- **DISTRIBUTION_OBJECT_D (配送对象信息单身)**
- **DISTRIBUTION_OBJECT_SD (品号群组配送信息)**
- **DISTRIBUTION_RECEIPT (配送/退配入库单)**
- **DISTRIBUTION_RECEIPT_D (配送/退配入库单单身)**
- **DISTRIBUTION_SD (门店订单签收)**


---


---


> Tables: 9

### DISTRIBUTION (配送单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | DISTRIBUTION_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PLANT_ID | 主鍵 | GUID | Y |  |
| 9 | DELIVEYR_RESOURCE_ID | 配送资源 | GUID | Y |  |
| 10 | DISTRIBUTION_DATE | 配送日期 | date | Y |  |
| 11 | PLAN_DELIVERY_DATE | 预交货日期 | date | Y |  |
| 12 | TEMP_DISTRIBUTION | 临时配送 | number(0/1) | Y |  |
| 13 | LAST_DISTRIBUTION | 上次配送日 | date | Y |  |
| 14 | EXPENSE_ID | 费用编号 | GUID | Y |  |
| 15 | CURRENCY_ID | 币种 | GUID | Y |  |
| 16 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 17 | EXPENSE_AMOUNT_TC | 费用金额（原币） | number(23,8) | Y |  |
| 18 | EXPENSE_AMOUNT_BC | 费用金额（本币） | number(23,8) | Y |  |
| 19 | SUPPLIER_ID | 承运商 | GUID | Y |  |
| 20 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 21 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 22 | RECEIVE_ADDR | 收货地址 | string(510) | Y |  |
| 23 | SAME_LEGAL | 同法人 | number(0/1) | Y |  |
| 24 | TRANSPORTER | 运输方 | string(40) | Y |  |
| 25 | EXPENSES_TO | 费用归属 | string(40) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 28 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Attachments | 附件 | string | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 59 | PrintCount | 打印次数 | number | Y |  |
| 60 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 61 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 62 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 63 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |
| 66 | OBJECT_TYPE_RTK |  | string(400) | Y |  |
| 67 | OBJECT_TYPE_ROid |  | GUID | Y |  |

### DISTRIBUTION_D (配送单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISTRIBUTION_D_ID |  | GUID | Y | Y |
| 3 | DIRECTOR | 直供发起方 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 8 | FEATURE_VALUE | 物流分类 | string(120) | Y |  |
| 9 | WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 10 | BIN_ID | 发货库位 | GUID | Y |  |
| 11 | TRANSIT_WAREHOUSE_ID | 在途仓 | GUID | Y |  |
| 12 | DISTRIBUTION_QTY | 配送数量 | number(16,6) | Y |  |
| 13 | STORAGE_QTY | 已入库量 | number(16,6) | Y |  |
| 14 | DIFF_QTY | 差异数量 | number(16,6) | Y |  |
| 15 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 16 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 17 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 18 | COST | 单位成本 | number(23,8) | Y |  |
| 19 | CLOSED | 结束码 | string(40) | Y |  |
| 20 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 21 | REMARK |  | string(510) | Y |  |
| 22 | INVENTORY_QTY1 | 入库库存单位数量 | number(16,6) | Y |  |
| 23 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 24 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 25 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 26 | DISTRIBUTION_PRICE | 供配价 | number(23,8) | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 55 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 56 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 57 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 58 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 59 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE_ID_ROid |  | GUID | Y |  |
| 61 | SOURCE_ID1_RTK |  | string(400) | Y |  |
| 62 | SOURCE_ID1_ROid |  | GUID | Y |  |
| 63 | DISTRIBUTION_ID |  | GUID | Y |  |

### DISTRIBUTION_LIST (配送清单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DISTRIBUTION_LIST_ID | 主键 | GUID | Y | Y |
| 2 | SEQUENCE_NUMBER | 序号 | number | Y |  |
| 3 | ITEM_ID | 零组件品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 零组件品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 零组件特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION | 零组件规格 | string(510) | Y |  |
| 7 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 8 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 9 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 10 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 11 | PLAN_SHIP_DATE | 预发货日 | date | Y |  |
| 12 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 13 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 14 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 15 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 16 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 17 | DISTRIBUTED_BUS_QTY | 已配送业务数量 | number(16,6) | Y |  |
| 18 | PLAN_STATUS | 计划状态 | string(40) | Y |  |
| 19 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
| 20 | RESERVED_BUSINESS_QTY | 已保留业务数量 | number(16,6) | Y |  |
| 21 | DISTRIBUTION_GROUP | 配送群组 | string(60) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | PIECES | 件数 | number | Y |  |
| 24 | SOURCE_ID | 发货计划ID | GUID | Y |  |
| 25 | REFERENCE_SOURCE_ID | 销售订单单身ID | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
| 33 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 34 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 35 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 36 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 37 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 38 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 39 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 40 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 41 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 42 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 43 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 44 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 45 | UDF041 | 自定义字段12 | date | Y |  |
| 46 | UDF042 | 自定义字段13 | date | Y |  |
| 47 | UDF051 | 自定义字段14 | GUID | Y |  |
| 48 | UDF052 | 自定义字段15 | GUID | Y |  |
| 49 | UDF053 | 自定义字段16 | GUID | Y |  |
| 50 | UDF054 | 自定义字段17 | GUID | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |

### DISTRIBUTION_OBJECT (配送对象信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DISTRIBUTION_OBJECT_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | FOR_DISTRIBUTION | 按配送对象 | number(0/1) | Y |  |
| 6 | ENABLED_PERIOD |  | number(0/1) | Y |  |
| 7 | FOR_DISTRIBUTION_FD | 按配送对象+物流分类 | number(0/1) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
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
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### DISTRIBUTION_OBJECT_D (配送对象信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISTRIBUTION_OBJECT_D_ID | 主键 | GUID | Y | Y |
| 3 | LAST_DISTRIBUTION | 上次配送日 | date | Y |  |
| 4 | PERIOD_DISTRIBUTION_DAYS | 配送周期 | number | Y |  |
| 5 | TRANSPORTION_DAYS | 在途天数 | number | Y |  |
| 6 | PRIORITY_DISTRIBUTION | 配送优先级 | string(10) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | SUPPLY_SYNERGY_ID | 主键 | GUID | Y |  |
| 9 | IS_DIRECT | 直供 | number(0/1) | Y |  |
| 10 | PLANT_ID | 主鍵 | GUID | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | DISTRIBUTION_OBJECT_RTK |  | string(400) | Y |  |
| 37 | DISTRIBUTION_OBJECT_ROid |  | GUID | Y |  |
| 38 | DISTRIBUTION_OBJECT_ID |  | GUID | Y |  |

### DISTRIBUTION_OBJECT_SD (品号群组配送信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISTRIBUTION_OBJECT_SD_ID | 主键 | GUID | Y | Y |
| 3 | LAST_DISTRIBUTION | 上次配送日 | date | Y |  |
| 4 | PERIOD_DISTRIBUTION_DAYS | 配送周期 | number | Y |  |
| 5 | FEATURE_VALUE | 物流分类 | GUID | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | DISTRIBUTION_OBJECT_D_ID |  | GUID | Y |  |

### DISTRIBUTION_RECEIPT (配送/退配入库单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | DISTRIBUTION_RECEIPT_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | RECEIPT_DATE | 入库日期 | date | Y |  |
| 9 | PLANT_ID | 发货/接收储运机构 | GUID | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | COMPANY_ID | 公司 | GUID | Y |  |
| 12 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 13 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 14 | PrintCount | 打印次数 | number | Y |  |
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
| 33 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 34 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 35 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 36 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |
| 51 | OBJECT_TYPE_RTK |  | string(400) | Y |  |
| 52 | OBJECT_TYPE_ROid |  | GUID | Y |  |

### DISTRIBUTION_RECEIPT_D (配送/退配入库单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISTRIBUTION_RECEIPT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME |  | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | TRANSIT_WAREHOUSE_ID | 在途仓 | GUID | Y |  |
| 8 | WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 9 | BIN_ID | 入库库位 | GUID | Y |  |
| 10 | UNIT_ID | 物流单位 | GUID | Y |  |
| 11 | DILIVER_QTY | 配送数量 | number(16,6) | Y |  |
| 12 | QTY | 入库数量 | number(16,6) | Y |  |
| 13 | DIFFERENCE_QTY | 差异数量 | number(16,6) | Y |  |
| 14 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 15 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | LOSS_DISTRIBUTION_ID |  | GUID | Y |  |
| 18 | COST | 单位成本 | number(23,8) | Y |  |
| 19 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 20 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 21 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 22 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 23 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 24 | DISTRIBUTION_PRICE | 供配价 | number(23,8) | Y |  |
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
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 54 | SOURCE_ID_ROid |  | GUID | Y |  |
| 55 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 56 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 57 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 58 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 59 | DISTRIBUTION_RECEIPT_ID |  | GUID | Y |  |

### DISTRIBUTION_SD (门店订单签收)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISTRIBUTION_SD_ID |  | GUID | Y | Y |
| 3 | SALE_PAYTYPE_ID | 收款方式编号 | GUID | Y |  |
| 4 | BANK_NO | 银行卡号 | string(40) | Y |  |
| 5 | SALE_AMT | 收款金额 | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | DISTRIBUTION_D_ID |  | GUID | Y |  |