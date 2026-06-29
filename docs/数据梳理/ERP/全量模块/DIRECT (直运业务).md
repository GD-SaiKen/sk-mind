---
module: "DIRECT"
name_zh: "直运业务"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 99
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# DIRECT (直运业务)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 99

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DISCOUNT (折扣表)|DISCOUNT (折扣表)]]

---

## Tables


- **DIRECT_GOODS (直供需求单)**
- **DIRECT_GOODS_D (直供需求单明细)**


---


---


> Tables: 2

### DIRECT_GOODS (直供需求单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DIRECT_GOODS_ID | 主键 | GUID | Y | Y |
| 7 | PLANT_ID | 储运机构 | GUID | Y |  |
| 8 | CATEGORY | 单据性质 | string(40) | Y |  |
| 9 | DIRECT_DATE | 直供需求日期 | date | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | PrintCount | 打印次数 | number | Y |  |
| 12 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 13 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 14 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 15 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### DIRECT_GOODS_D (直供需求单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DIRECT_GOODS_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_BUSINESS_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | LOGISTICS_QTY | 物流数量 | number(16,6) | Y |  |
| 8 | PLAN_DISTRIBUTION_QTY | 已转配送任务量 | number(16,6) | Y |  |
| 9 | DISTRIBUTION_QTY | 已转配送量 | number(16,6) | Y |  |
| 10 | DRP_QTY | 已转DRP量 | number(16,6) | Y |  |
| 11 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 12 | ORDER_DISTRIBUTION | 直供机构 | GUID | Y |  |
| 13 | PLAN_DELIVERY_DATE | 预交货日期 | date | Y |  |
| 14 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 15 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 16 | RECEIVE_ADDR | 收货地址 | string(510) | Y |  |
| 17 | CLOSED | 结束码 | string(40) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | LAST_INVENTORY_QTY | 余量库存单位数量 | number(16,6) | Y |  |
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
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | DISTRIBUTION_OBJECT_RTK |  | string(400) | Y |  |
| 49 | DISTRIBUTION_OBJECT_ROid |  | GUID | Y |  |
| 50 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE_ID_ROid |  | GUID | Y |  |
| 52 | DIRECT_GOODS_ID |  | GUID | Y |  |