---
module: "PACKING"
name_zh: "包装清单"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 186
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# PACKING (包装清单)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 186

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


- **PACKING_LIST**
- **PACKING_LIST_D**
- **PACKING_LIST_SD**
- **PACKING_MODE (品号包装信息)**


---


---


> Tables: 4

### PACKING_LIST

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PACKING_LIST_ID | 主键 | GUID | Y | Y |
| 4 | PALLET_UNIT | 货盘单位 | string(40) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SALES_DELIVERY_ID | 出货通知单 | GUID | Y |  |
| 7 | PACKING_DATE | PACKING日期 | date | Y |  |
| 8 | TRANSACTION_DATE | 审核日期 | date | Y |  |
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
| 27 | PrintCount | 打印次数 | number | Y |  |
| 28 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 29 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 30 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 31 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Attachments | 附件 | string | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | DOC_NO | 单号 | string(40) | Y |  |
| 47 | DOC_DATE | 单据日期 | date | Y |  |
| 48 | DOC_ID | 单据类型 | GUID | Y |  |
| 49 | MERGE_PACKING | 合并包装 | number(0/1) | Y |  |

### PACKING_LIST_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PACKING_LIST_D_ID | 主键 | GUID | Y | Y |
| 3 | PALLET_NO | 货盘号 | string(8) | Y |  |
| 4 | START_CARTON_NO | 起始箱号 | string(8) | Y |  |
| 5 | END_CARTON_NO | 截止箱号 | string(8) | Y |  |
| 6 | CARTON_QTY | 箱数 | number | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | PACKING_LIST_QTY | 数量 | number(16,6) | Y |  |
| 10 | UNIT_ID | 单位 | GUID | Y |  |
| 11 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 12 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 13 | GROSS_WEIGHT | 毛重 | number(16,6) | Y |  |
| 14 | VOLUMN | 材积 | number(16,6) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | PIECES | 件数 | number | Y |  |
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
| 42 | PACKING_LIST_ID |  | GUID | Y |  |
| 43 | CARTON_TYPE | 装箱类型 | string(2) | Y |  |

### PACKING_LIST_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PACKING_LIST_SD_ID | 主键 | GUID | Y | Y |
| 2 | SALES_DELIVERY_D_ID | 通知单序号 | GUID | Y |  |
| 3 | SALES_ORDER_DOC_D_ID | 销售订单 | GUID | Y |  |
| 4 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 5 | DELIVERY_QTY | 出货数量 | number(16,6) | Y |  |
| 6 | UNIT_ID | 单位 | GUID | Y |  |
| 7 | WAREHOUSE_ID | 出货仓库 | GUID | Y |  |
| 8 | BIN_ID | 库位 | GUID | Y |  |
| 9 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | ISSUED_QTY | 已出库业务数量 | number(16,6) | Y |  |
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
| 37 | PACKING_LIST_D_ID |  | GUID | Y |  |

### PACKING_MODE (品号包装信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PACKING_MODE_ID | 主键 | GUID | Y | Y |
| 2 | PACKING_CODE | 包装方式 | string(8) | Y |  |
| 3 | DESCRIPTION | 描述 | string(160) | Y |  |
| 4 | INC_PACKING3_QTY | 小包装容量 | number(16,6) | Y |  |
| 5 | PACKING4_WEIGHT | 最小包装重量 | number(16,6) | Y |  |
| 6 | INC_PACKING2_QTY | 中包装容量 | number(16,6) | Y |  |
| 7 | PACKING3_WEIGHT | 小包装重量 | number(16,6) | Y |  |
| 8 | INC_PACKING1_QTY | 大包装容量 | number(16,6) | Y |  |
| 9 | PACKING2_WEIGHT | 中包装重量 | number(16,6) | Y |  |
| 10 | PER_NET_WEIGHT | 包装净重 | number(16,6) | Y |  |
| 11 | PER_GROSS_WEIGHT | 包装毛重 | number(16,6) | Y |  |
| 12 | LEHTH | 长 | number(6,1) | Y |  |
| 13 | WIDTH | 宽 | number(16,6) | Y |  |
| 14 | HEIGTH | 高 | number(16,6) | Y |  |
| 15 | PER_VOLUMN | 包装材积 | number(16,6) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | PACKING1_WEIGHT | 大包装重量 | number(16,6) | Y |  |
| 18 | MAIN_PACKING_MODE | 是否主要包装方式 | number(0/1) | Y |  |
| 19 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 20 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 21 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 22 | PACKING1_UNIT_ID | 外包装单位 | GUID | Y |  |
| 23 | INC_PACKING4_QTY | 最小包装容量 | number(16,6) | Y |  |
| 24 | PACKING_QTY | 包装数量 | number(16,6) | Y |  |
| 25 | PACKING_WEIGHT_UNIT_ID | 包装重量单位 | GUID | Y |  |
| 26 | LENTH_UNIT_ID | 长度单位 | GUID | Y |  |
| 27 | VOLUMN_UNIT_ID | 体积单位 | GUID | Y |  |
| 28 | LENTH | 长 | number(16,6) | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 37 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 38 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 39 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 40 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 41 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 42 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 43 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 44 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 45 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 46 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 47 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 48 | UDF041 | 自定义字段12 | date | Y |  |
| 49 | UDF042 | 自定义字段13 | date | Y |  |
| 50 | UDF051 | 自定义字段14 | GUID | Y |  |
| 51 | UDF052 | 自定义字段15 | GUID | Y |  |
| 52 | UDF053 | 自定义字段16 | GUID | Y |  |
| 53 | UDF054 | 自定义字段17 | GUID | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | ITEM_BUSINESS_ID |  | GUID | Y |  |