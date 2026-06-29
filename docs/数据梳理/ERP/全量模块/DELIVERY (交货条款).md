---
module: "DELIVERY"
name_zh: "交货条款"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 114
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# DELIVERY (交货条款)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 114

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]
- [[DISCOUNT (折扣表)|DISCOUNT (折扣表)]]

---

## Tables


- **DELIVERY_TERM (运输方式)**


---


---


> Tables: 2

### DELIVERY (维护计划底稿)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SequenceNumber |  | number | Y |  |
| 7 | DELIVERY_ID | 主键 | GUID | Y | Y |
| 8 | DATE1 | 配送日 | date | Y |  |
| 9 | FEATURE_VALUE | 物流分类 | string(120) | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 12 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 13 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 14 | QTY | 原配送量 | number(16,6) | Y |  |
| 15 | PLAN_DELIVERY_DATE | 预交货日 | date | Y |  |
| 16 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 17 | STOCK_UNIT_ID | 库存单位 | GUID | Y |  |
| 18 | SUG_QTY | 建议配送量 | number(16,6) | Y |  |
| 19 | CONT_MAN | 订货人 | string(20) | Y |  |
| 20 | CONT_TEL | 联系电话 | string(40) | Y |  |
| 21 | RECEIVE_ADDR | 收货地址 | string(510) | Y |  |
| 22 | GIVE | 是否发放 | number(0/1) | Y |  |
| 23 | PLAN_DISTRIBUTION_ID | 发放配送任务ID | GUID | Y |  |
| 24 | CATEGORY | 单据性质 | string(40) | Y |  |
| 25 | AVAILABLE_QTY | 可用量 | number(16,6) | Y |  |
| 26 | PLAN_QTY | 计划数量 | number(16,6) | Y |  |
| 27 | STORE_QTY | 库存分摊量 | number(16,6) | Y |  |
| 28 | MO_QTY | 工单量 | number(16,6) | Y |  |
| 29 | PURCHASE_QTY | 请购量 | number(16,6) | Y |  |
| 30 | RECEIPT_QTY | 采购量 | number(16,6) | Y |  |
| 31 | TRANSFERIN_QTY | 调拨量 | number(16,6) | Y |  |
| 32 | LOCK_PLAN_QTY | 锁定计划量 | number(16,6) | Y |  |
| 33 | EXAMINE_QTY | 采购待验量 | number(16,6) | Y |  |
| 34 | FORECAST_QTY | 预测量 | number(16,6) | Y |  |
| 35 | SALESDELIVERY_QTY | 订单量 | number(16,6) | Y |  |
| 36 | SAFE_STOCK_QTY | 安全存量 | number(16,6) | Y |  |
| 37 | STOCK_QTY | 库存量 | number(16,6) | Y |  |
| 38 | DISTRIBUTION_QTY | 预计配送量 | number(16,6) | Y |  |
| 39 | MOLOCATE_QTY | 工单领料量 | number(16,6) | Y |  |
| 40 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | Attachments | 附件 | string | Y |  |
| 48 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 49 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 50 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 51 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 52 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 53 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 54 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 55 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 56 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 57 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 58 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 59 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 60 | UDF041 | 自定义字段12 | date | Y |  |
| 61 | UDF042 | 自定义字段13 | date | Y |  |
| 62 | UDF051 | 自定义字段14 | GUID | Y |  |
| 63 | UDF052 | 自定义字段15 | GUID | Y |  |
| 64 | UDF053 | 自定义字段16 | GUID | Y |  |
| 65 | UDF054 | 自定义字段17 | GUID | Y |  |
| 66 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 67 | Version | 版本号，不要随意更改 | binary | Y |  |
| 68 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 69 | ApproveDate | 修改日期 | date | Y |  |
| 70 | ApproveBy | 修改人 | GUID | Y |  |
| 71 | Owner_Org_RTK |  | string(400) | Y |  |
| 72 | Owner_Org_ROid |  | GUID | Y |  |
| 73 | DISTRIBUTION_OBJECT_RTK |  | string(400) | Y |  |
| 74 | DISTRIBUTION_OBJECT_ROid |  | GUID | Y |  |
| 75 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 76 | SOURCE_ID_ROid |  | GUID | Y |  |

### DELIVERY_TERM (运输方式)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DELIVERY_TERM_ID | 主键 | GUID | Y | Y |
| 4 | DELIVERY_TERM_CODE | 运输方式编码 | string(8) | Y |  |
| 5 | DELIVERY_TERM_DESCRIPTION | 运输方式描述 | string(120) | Y |  |
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