---
module: "FIL"
name_zh: "货位管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 248
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# FIL (货位管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 248

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[ISSUE (发料出库)|ISSUE (发料出库)]]

---

## Tables


- **FIL_ARRIVAL (送货单信息)**
- **FIL_ARRIVAL_D (送货单单身)**
- **FIL_BIN (库位信息)**
- **FIL_INTEGRATE (FIL_INTEGRATE)**
- **FIL_ITEM_BC_REG (FIL_ITEM_BC_REG)**
- **FIL_WAREHOUSE (FIL_WAREHOUSE)**


---


---


> Tables: 6

### FIL_ARRIVAL (送货单信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | FIL_ARRIVAL_ID | 主键 | GUID | Y | Y |
| 2 | BOOK_CODE |  | string(10) | Y |  |
| 3 | PLANT_CODE |  | string(20) | Y |  |
| 4 | DOC_NO |  | string(40) | Y |  |
| 5 | DOC_DATE |  | date | Y |  |
| 6 | COMPANY_CODE |  | string(20) | Y |  |
| 7 | CATEGORY |  | string(40) | Y |  |
| 8 | ADDR_NAME |  | string(510) | Y |  |
| 9 | ARRIVAL_NO |  | string(40) | Y |  |
| 10 | PRINT |  | number | Y |  |
| 11 | REMARK |  | string(510) | Y |  |
| 12 | STATUS |  | string(400) | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
| 14 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |

### FIL_ARRIVAL_D (送货单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FIL_ARRIVAL_D_ID |  | GUID | Y | Y |
| 3 | BOOK_CODE |  | string(10) | Y |  |
| 4 | PLANT_CODE |  | string(20) | Y |  |
| 5 | DOC_NO |  | string(40) | Y |  |
| 6 | ORDER_NO |  | string(40) | Y |  |
| 7 | ORDER_SE |  | number | Y |  |
| 8 | ORDER_SE_SE |  | number | Y |  |
| 9 | ORDER_SE_SE_SE |  | number | Y |  |
| 10 | ITEM_CODE |  | string(80) | Y |  |
| 11 | ITEM_NAME |  | string(510) | Y |  |
| 12 | ITEM_DESCRIPTION |  | string(510) | Y |  |
| 13 | WAREHOUSE_CODE |  | string(20) | Y |  |
| 14 | UNIT_CODE |  | string(20) | Y |  |
| 15 | PU_QTY |  | number(20,6) | Y |  |
| 16 | UNARR_QTY |  | number(20,6) | Y |  |
| 17 | ACTUAL_QTY |  | number(20,6) | Y |  |
| 18 | RECEIPT_QTY |  | number(20,6) | Y |  |
| 19 | TAX_INVOICE_NO |  | string(40) | Y |  |
| 20 | PACKING_QTY |  | number(20,6) | Y |  |
| 21 | BC_TYPE |  | string(20) | Y |  |
| 22 | COMPANY_CODE |  | string(20) | Y |  |
| 23 | PURCHASE_ARRIVAL_ID |  | GUID | Y |  |
| 24 | PURCHASE_ARRIVAL_D_ID |  | GUID | Y |  |
| 25 | CHECK_NO |  | string(20) | Y |  |
| 26 | PRICE_UNIT_CODE |  | string(20) | Y |  |
| 27 | PRICE_QTY |  | number(20,6) | Y |  |
| 28 | RECEIPT_OVER_RATE |  | number(20,6) | Y |  |
| 29 | ITEM_FEATURE_CODE |  | string(512) | Y |  |
| 30 | STATUS |  | string(20) | Y |  |
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
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | FIL_ARRIVAL_ID |  | GUID | Y |  |

### FIL_BIN (库位信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | FIL_BIN_ID |  | GUID | Y | Y |
| 2 | BIN_ID |  | GUID | Y |  |
| 3 | GENERATE_BIN_CHANGE |  | number(0/1) | Y |  |
| 4 | SINGLE_BATCH_STORAGE |  | number(0/1) | Y |  |
| 5 | REMARK |  | string(510) | Y |  |
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
| 34 | FIL_WAREHOUSE_ID |  | GUID | Y |  |

### FIL_INTEGRATE (FIL_INTEGRATE)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | FIL_INTEGRATE_ID | 主键 | GUID | Y | Y |
| 2 | Version | 版本号，不要随意更改 | binary | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
| 9 | Attachments | 附件 | string | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### FIL_ITEM_BC_REG (FIL_ITEM_BC_REG)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 4 | ApproveDate | 修改日期 | date | Y |  |
| 5 | ApproveBy | 修改人 | GUID | Y |  |
| 6 | FIL_ITEM_BC_REG_ID | 主键 | GUID | Y | Y |
| 7 | ITEM_ID |  | GUID | Y |  |
| 8 | ITEM_FEATURE_ID |  | GUID | Y |  |
| 9 | BC_MANAGEMENT |  | number(0/1) | Y |  |
| 10 | BC_REG_ID |  | GUID | Y |  |
| 11 | BARCODE_TYPE |  | string(400) | Y |  |
| 12 | QTY |  | number(16,6) | Y |  |
| 13 | FIFO_TYPE |  | string(400) | Y |  |
| 14 | LOT_AUTO |  | number(0/1) | Y |  |
| 15 | MAIN |  | number(0/1) | Y |  |
| 16 | REMARK |  | string(510) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |

### FIL_WAREHOUSE (FIL_WAREHOUSE)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | FIL_WAREHOUSE_ID | 主键 | GUID | Y | Y |
| 4 | WAREHOUSE_ID |  | GUID | Y |  |
| 5 | NEGATIVE_INVENTORY_ALLOWED |  | number(0/1) | Y |  |
| 6 | FIFO_TYPE |  | string(400) | Y |  |
| 7 | BIN_CONTROL |  | string(400) | Y |  |
| 8 | REMARK |  | string(510) | Y |  |
| 9 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | Attachments | 附件 | string | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |