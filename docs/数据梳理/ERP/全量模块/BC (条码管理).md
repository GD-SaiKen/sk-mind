---
module: "BC"
name_zh: "条码管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 32
columns: 1276
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# BC (条码管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 32 | Columns: 1276

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]
- [[ISSUE (发料出库)|ISSUE (发料出库)]]

---

## Tables


- **BC_GEN_IR**
- **BC_GEN_IR_D**
- **BC_GEN_IR_SDOC**
- **BC_GEN_MR**
- **BC_GEN_MR_D**
- **BC_GEN_MR_SDOC**
- **BC_GEN_PR**
- **BC_GEN_PR_D**
- **BC_GEN_PR_PDOC**
- **BC_GEN_SI**
- **BC_GEN_SI_D**
- **BC_GEN_SI_SDOC**
- **BC_GEN_TI**
- **BC_GEN_TI_D**
- **BC_GEN_TI_SDOC**
- **BC_GEN_TO**
- **BC_GEN_TO_D**
- **BC_GEN_TO_SDOC**
- **BC_INVENTORY (BC_INVENTORY)**
- **BC_LINE (BC_LINE)**
- **BC_PACKINGLIST (BC_PACKINGLIST)**
- **BC_PACKINGLIST_D (维护装箱单单身信息)**
- **BC_PICK_CONFIRM**
- **BC_PICK_CONFIRM_D**
- **BC_PICK_CONFIRM_SDOC**
- **BC_PROPERTY**
- **BC_PROPERTY_BINDING**
- **BC_RECORD**
- **BC_RECORD_D**
- **BC_REG**
- **BC_REG_D**
- **BC_REG_SD**


---


---


> Tables: 32

### BC_GEN_IR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BC_GEN_IR_ID | 主键 | GUID | Y | Y |
| 2 | OPERATION_NO | 作业编号 | string(400) | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 6 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 7 | Owner_Emp | 领料人员 | GUID | Y |  |
| 8 | Owner_Dept | 领料部门 | GUID | Y |  |
| 9 | BC_REG_ID | 条码编码规则 | GUID | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 12 | BIN_ID | 库位 | GUID | Y |  |
| 13 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 14 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 39 | Attachments | 附件 | string | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |
| 47 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 49 | WS_SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | WS_SOURCE_ID_ROid |  | GUID | Y |  |

### BC_GEN_IR_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BARCODE_NO | 条码 | string(400) | Y |  |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 6 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
| 8 | SCAN_COUNT | 扫描次数 | number(16,6) | Y |  |
| 9 | INV_QTY | 库存单位数量 | number(16,6) | Y |  |
| 10 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 11 | BC_GEN_IR_D_ID |  | string(400) | Y | Y |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | BC_GEN_IR_ID |  | GUID | Y |  |

### BC_GEN_IR_SDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 3 | SCANED_INV_REPLACE_QTY | 已扫描取替代库存单位数量 | number(16,6) | Y |  |
| 4 | BC_GEN_IR_SDOC_ID |  | string(400) | Y | Y |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 31 | SOURCE_ID_ROid |  | GUID | Y |  |
| 32 | BC_GEN_IR_ID |  | GUID | Y |  |

### BC_GEN_MR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BC_GEN_MR_ID | 主键 | GUID | Y | Y |
| 2 | OPERATION_NO | 作业编号 | string(400) | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 6 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 7 | WAREHOUSE_ID | 限定仓库 | GUID | Y |  |
| 8 | ADMIN_UNIT_ID | 生产部门 | GUID | Y |  |
| 9 | Owner_Emp | 入库人员 | GUID | Y |  |
| 10 | Owner_Dept | 入库部门 | GUID | Y |  |
| 11 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 12 | BC_REG_ID | 条码编码规则ID | GUID | Y |  |
| 13 | ITEM_ID | 品号 | GUID | Y |  |
| 14 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 15 | BIN_ID | 库位 | GUID | Y |  |
| 16 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE_ID_ROid |  | GUID | Y |  |
| 49 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE2_ID_ROid |  | GUID | Y |  |

### BC_GEN_MR_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_MR_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | ACCEPT_INV_QTY | 允收库存单位数量 | number(16,6) | Y |  |
| 6 | ACCEPT_SECOND_QTY | 允收第二单位数量 | number(16,6) | Y |  |
| 7 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 8 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 9 | BIN_ID | 库位 | GUID | Y |  |
| 10 | SCAN_COUNT | 扫描次数 | number(16,6) | Y |  |
| 11 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 12 | BARCODE_NO | 条码 | string(400) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | BC_GEN_MR_ID |  | GUID | Y |  |

### BC_GEN_MR_SDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 3 | BC_GEN_MR_SDOC_ID | 主键 | string(400) | Y | Y |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 30 | SOURCE_ID_ROid |  | GUID | Y |  |
| 31 | BC_GEN_MR_ID |  | GUID | Y |  |

### BC_GEN_PR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | BC_GEN_PR_ID | 主键 | GUID | Y | Y |
| 7 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 8 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 9 | BIN_ID | 库位 | GUID | Y |  |
| 10 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 11 | BC_REG_ID | 条码规则 | GUID | Y |  |
| 12 | ITEM_ID | 品号 | GUID | Y |  |
| 13 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 14 | PURCHASE_RECEIPT_ID | 采购入库单 | GUID | Y |  |
| 15 | PURCHASE_ARRIVAL_ID | 到货单 | GUID | Y |  |
| 16 | PURCHASE_ARRIVAL_D_ID | 到货明细 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
| 18 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |

### BC_GEN_PR_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_PR_D_ID | 主键 | GUID | Y | Y |
| 3 | BARCODE_NO | 条码 | string(400) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | INV_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | BIN_ID | 库位 | GUID | Y |  |
| 10 | SCAN_COUNT | 扫描次数 | number | Y |  |
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
| 36 | BC_GEN_PR_ID |  | GUID | Y |  |

### BC_GEN_PR_PDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_PR_PDOC_ID | 主键 | GUID | Y | Y |
| 3 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 4 | PURCHASE_ARRIVAL_D_ID | 到货明细 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | BC_GEN_PR_ID |  | GUID | Y |  |

### BC_GEN_SI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | BC_GEN_SI_ID | 主键 | GUID | Y | Y |
| 7 | OPERATION_NO | 作业编号 | string(400) | Y |  |
| 8 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 9 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 10 | BIN_ID | 库位 | GUID | Y |  |
| 11 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 12 | BC_REG_ID | 条码规则 | GUID | Y |  |
| 13 | ITEM_ID | 品号 | GUID | Y |  |
| 14 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 15 | SALES_ISSUE_ID | 销货出库单 | GUID | Y |  |
| 16 | SOURCE_ID | 销货单 | GUID | Y |  |
| 17 | SOURCE2_ID | 销货明细 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
| 19 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### BC_GEN_SI_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_SI_D_ID | 主键 | GUID | Y | Y |
| 3 | BARCODE_NO | 条码 | string(400) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | INV_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | BIN_ID | 库位 | GUID | Y |  |
| 10 | SCAN_COUNT | 扫描次数 | number | Y |  |
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
| 36 | BC_GEN_SI_ID |  | GUID | Y |  |

### BC_GEN_SI_SDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_SI_SDOC_ID | 主键 | GUID | Y | Y |
| 3 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 4 | SOURCE_ID | 来源 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 8 | SALES_ORDER_DOC_SD_ID | 销售订单发货计划 | GUID | Y |  |
| 9 | SCANED_SECOND_QTY | 已扫描第二单位数量 | number(16,6) | Y |  |
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
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | BC_GEN_SI_ID |  | GUID | Y |  |

### BC_GEN_TI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BC_GEN_TI_ID | 主键 | GUID | Y | Y |
| 2 | OPERATION_NO | 作业编号 | string(400) | Y |  |
| 3 | SOURCE_ID | 主键 | GUID | Y |  |
| 4 | SOURCE2_ID | 主键 | GUID | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_DATE | 单据日期 | date | Y |  |
| 7 | TO_PLANT_ID | 转入工厂/储运 | GUID | Y |  |
| 8 | FROM_PLANT_ID | 主鍵 | GUID | Y |  |
| 9 | FROM_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 10 | TO_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 11 | TO_BIN_ID | 主键 | GUID | Y |  |
| 12 | Owner_Emp | 主键 | GUID | Y |  |
| 13 | Owner_Dept | 主键 | GUID | Y |  |
| 14 | ITEM_ID | 主键 | GUID | Y |  |
| 15 | ITEM_FEATURE_ID | 主键 | GUID | Y |  |
| 16 | BC_REG_ID | 主键 | GUID | Y |  |
| 17 | ITEM_LOT_ID | 主键 | GUID | Y |  |
| 18 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |

### BC_GEN_TI_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_TI_D_ID | 主键 | GUID | Y | Y |
| 3 | BARCODE_NO | 条码 | string(400) | Y |  |
| 4 | ITEM_ID | 主键 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 主键 | GUID | Y |  |
| 6 | ITEM_LOT_ID | 主键 | GUID | Y |  |
| 7 | INV_QTY | 库存单位数量 | number(16,6) | Y |  |
| 8 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 9 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 10 | TO_BIN_ID | 主键 | GUID | Y |  |
| 11 | SCAN_COUNT | 扫描次数 | number(16,6) | Y |  |
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
| 37 | BC_GEN_TI_ID |  | GUID | Y |  |

### BC_GEN_TI_SDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_TI_SDOC_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_ID | 主键 | GUID | Y |  |
| 4 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | BC_GEN_TI_ID |  | GUID | Y |  |

### BC_GEN_TO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BC_GEN_TO_ID | 主键 | GUID | Y | Y |
| 2 | OPERATION_NO | 作业编号 | string(400) | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | FROM_PLANT_ID | 主鍵 | GUID | Y |  |
| 6 | TO_PLANT_ID | 主鍵 | GUID | Y |  |
| 7 | FROM_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 8 | TO_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 9 | IN_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 10 | FROM_BIN_ID | 主键 | GUID | Y |  |
| 11 | TO_BIN_ID | 主键 | GUID | Y |  |
| 12 | Owner_Emp | 主键 | GUID | Y |  |
| 13 | Owner_Dept | 主键 | GUID | Y |  |
| 14 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 17 | BC_REG_ID | 条码编码规则 | GUID | Y |  |
| 18 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |
| 51 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 52 | SOURCE2_ID_ROid |  | GUID | Y |  |

### BC_GEN_TO_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_TO_D_ID | 主键 | GUID | Y | Y |
| 3 | BARCODE_NO | 条码 | string(400) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | INV_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 10 | FROM_WAREHOUSE_ID | 主键 | GUID | Y |  |
| 11 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 12 | FROM_BIN_ID | 主键 | GUID | Y |  |
| 13 | SCAN_COUNT | 扫描次数 | number(16,6) | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | BC_GEN_TO_ID |  | GUID | Y |  |

### BC_GEN_TO_SDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_GEN_TO_SDOC_ID | 主键 | GUID | Y | Y |
| 3 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 4 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 5 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 6 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 7 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 8 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 9 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 10 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 11 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 12 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 13 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 14 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 15 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 16 | UDF041 | 自定义字段12 | date | Y |  |
| 17 | UDF042 | 自定义字段13 | date | Y |  |
| 18 | UDF051 | 自定义字段14 | GUID | Y |  |
| 19 | UDF052 | 自定义字段15 | GUID | Y |  |
| 20 | UDF053 | 自定义字段16 | GUID | Y |  |
| 21 | UDF054 | 自定义字段17 | GUID | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 30 | SOURCE_ID_ROid |  | GUID | Y |  |
| 31 | BC_GEN_TO_ID |  | GUID | Y |  |

### BC_INVENTORY (BC_INVENTORY)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_INVENTORY_ID | 主键 | GUID | Y | Y |
| 4 | BARCODE_NO |  | string(400) | Y |  |
| 5 | WAREHOUSE_ID |  | GUID | Y |  |
| 6 | BIN_ID |  | GUID | Y |  |
| 7 | ITEM_ID |  | GUID | Y |  |
| 8 | ITEM_FEATURE_ID |  | GUID | Y |  |
| 9 | ITEM_LOT_ID |  | GUID | Y |  |
| 10 | QTY |  | number(16,6) | Y |  |
| 11 | TRANSACTION_FROZEN |  | number(0/1) | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
| 13 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### BC_LINE (BC_LINE)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_LINE_ID | 主键 | GUID | Y | Y |
| 4 | BARCODE_NO |  | string(400) | Y |  |
| 5 | QTY |  | number(16,6) | Y |  |
| 6 | WAREHOUSE_ID |  | GUID | Y |  |
| 7 | BIN_ID |  | GUID | Y |  |
| 8 | SOURCE_DOC_ID |  | GUID | Y |  |
| 9 | DOC_DATE |  | date | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
| 17 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |

### BC_PACKINGLIST (BC_PACKINGLIST)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_PACKINGLIST_ID | 主键 | GUID | Y | Y |
| 4 | PACK_BARCODE_NO |  | string(400) | Y |  |
| 5 | PACK_TIME |  | date | Y |  |
| 6 | STOCK_STATUS |  | number | Y |  |
| 7 | WAREHOUSE_ID |  | GUID | Y |  |
| 8 | BIN_ID |  | GUID | Y |  |
| 9 | REMARK |  | string(510) | Y |  |
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
| 28 | PrintCount | 打印次数 | number | Y |  |
| 29 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 30 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 31 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 32 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |

### BC_PACKINGLIST_D (维护装箱单单身信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_PACKINGLIST_D_ID |  | GUID | Y | Y |
| 3 | BARCODE_NO |  | string(400) | Y |  |
| 4 | ITEM_ID |  | GUID | Y |  |
| 5 | ITEM_NAME |  | string(120) | Y |  |
| 6 | ITEM_SPEC |  | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID |  | GUID | Y |  |
| 8 | ITEM_LOT_ID |  | GUID | Y |  |
| 9 | QTY |  | number(16,6) | Y |  |
| 10 | WAREHOUSE_ID |  | GUID | Y |  |
| 11 | BIN_ID |  | GUID | Y |  |
| 12 | BARCODE_TYPE |  | string(40) | Y |  |
| 13 | REMARK |  | string(510) | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | BC_PACKINGLIST_ID |  | GUID | Y |  |

### BC_PICK_CONFIRM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BC_PICK_CONFIRM_ID | 主键 | GUID | Y | Y |
| 2 | APPEND_TYPE | 添加方式 | string(40) | Y |  |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | BC_REG_ID | 条码规则 | GUID | Y |  |
| 6 | ITEM_LOT_ID | 批号 | GUID | Y |  |
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
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE2_ID_ROid |  | GUID | Y |  |

### BC_PICK_CONFIRM_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_PICK_CONFIRM_D_ID | 主键 | string(400) | Y | Y |
| 3 | BARCODE_NO | 条码 | string(400) | Y |  |
| 4 | INV_QTY | 库存单位数量 | number(16,6) | Y |  |
| 5 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 6 | SCAN_COUNT | 扫描次数 | number | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
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
| 34 | BC_PICK_CONFIRM_ID |  | GUID | Y |  |

### BC_PICK_CONFIRM_SDOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BC_PICK_CONFIRM_SDOC_ID | 主键 | GUID | Y | Y |
| 2 | SCANED_INV_QTY | 已扫描库存单位数量 | number(16,6) | Y |  |
| 3 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 4 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 5 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 6 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 7 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 8 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 9 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 10 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 11 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 12 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 13 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 14 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 15 | UDF041 | 自定义字段12 | date | Y |  |
| 16 | UDF042 | 自定义字段13 | date | Y |  |
| 17 | UDF051 | 自定义字段14 | GUID | Y |  |
| 18 | UDF052 | 自定义字段15 | GUID | Y |  |
| 19 | UDF053 | 自定义字段16 | GUID | Y |  |
| 20 | UDF054 | 自定义字段17 | GUID | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 29 | SOURCE_ID_ROid |  | GUID | Y |  |
| 30 | BC_PICK_CONFIRM_ID |  | GUID | Y |  |

### BC_PROPERTY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_PROPERTY_ID | 主键 | GUID | Y | Y |
| 4 | BC_PROPERTY_CODE | 属性项编码 | string(120) | Y |  |
| 5 | BC_PROPERTY_NAME | 属性项名称 | string(120) | Y |  |
| 6 | PROPERTY_VALUE_TYPE | 数据类型 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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

### BC_PROPERTY_BINDING

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_PROPERTY_BINDING_ID | 主键 | GUID | Y | Y |
| 4 | DOC_CODE | 单据名称 | string(400) | Y |  |
| 5 | BC_PROPERTY_ID | 条码规则属性项 | GUID | Y |  |
| 6 | BINDING_TXT | 绑定关系 | string | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | BINDING_COL_NAME | 交易单据属性名称 | string(510) | Y |  |
| 9 | BINDING_COL_CODE | 交易单据属性编号 | string(510) | Y |  |
| 10 | BINDING_COL_ID | 交易单据属性 | string(510) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### BC_RECORD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_RECORD_ID | 主键 | GUID | Y | Y |
| 4 | BARCODE_NO | 条码 | string(400) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | GENERATE_TYPE | 生成方式 | string(40) | Y |  |
| 8 | GENERATE_DATE | 生成日期 | date | Y |  |
| 9 | LABEL_LAYOUT | 标签样式 | string(400) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | BC_REG_ID | 条码编码规则 | GUID | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | BARCODE_TYPE |  | string(40) | Y |  |
| 47 | FROZEN_STATUS |  | string(2) | Y |  |
| 48 | SOURCE_D_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_D_ID_ROid |  | GUID | Y |  |

### BC_RECORD_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_RECORD_D_ID | 明细主键 | GUID | Y | Y |
| 3 | BC_PROPERTY_VALUE | 属性值 | string(400) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | BC_PROPERTY_ID | 属性项 | GUID | Y |  |
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
| 31 | BC_RECORD_ID |  | GUID | Y |  |
| 32 | BARCODE_VALUE |  | string(400) | Y |  |

### BC_REG

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BC_REG_ID | 主键 | GUID | Y | Y |
| 4 | BC_REG_CODE | 规则编号 | string(120) | Y |  |
| 5 | BC_REG_NAME | 规则名称 | string(120) | Y |  |
| 6 | BC_REG_SIZE | 编码总长 | number | Y |  |
| 7 | BC_REG_DATE_BY | 日期依据 | string(40) | Y |  |
| 8 | CODE_TYPE | 编码类型 | string(40) | Y |  |
| 9 | LABEL_LAYOUT | 标签样式 | string(400) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | LABEL_LAYOUT_NAME | 标签样式名称 | string(400) | Y |  |
| 12 | NOT_SYSTEM_GEN | 非系统生成编码 | number(0/1) | Y |  |
| 13 | BOX_NO_GEN_TYPE | 箱号生成方式 | string(40) | Y |  |
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
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | BARCODE_TYPE |  | string(400) | Y |  |

### BC_REG_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BC_PROPERTY_ID | 属性项ID | GUID | Y |  |
| 3 | INCLUDED_CODING | 纳入编码 | number(0/1) | Y |  |
| 4 | CODING_SIZE | 编码长度 | number | Y |  |
| 5 | SUBSTRING_TYPE | 取位方式 | string(40) | Y |  |
| 6 | SUBSTRING_START | 起始位 | number | Y |  |
| 7 | SUBSTRING_SIZE | 取位长度 | number | Y |  |
| 8 | COVER_DEFAULT | 不足位默认值 | string(400) | Y |  |
| 9 | NOTATION | 进制 | string(40) | Y |  |
| 10 | REPLACE_REG_ENABLE | 启用替换规则 | number(0/1) | Y |  |
| 11 | DATA_DEFAULT | 默认值 | string(400) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | BC_REG_D_ID | 主键 | GUID | Y | Y |
| 14 | COVER_TYPE | 补位方式 | string(40) | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | BC_REG_ID |  | GUID | Y |  |

### BC_REG_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | REPLACED_PRIORITY | 替换优先级 | number | Y |  |
| 4 | REPLACED_VALUE | 替换后值 | string(400) | Y |  |
| 5 | ORIGINAL_VALUE | 替换前值 | string(400) | Y |  |
| 6 | BC_REG_SD_ID | 主键 | GUID | Y | Y |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 27 | ApproveDate | 修改日期 | date | Y |  |
| 28 | ApproveBy | 修改人 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | BC_REG_D_ID |  | GUID | Y |  |