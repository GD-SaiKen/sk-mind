---
module: "MATERIAL"
name_zh: "物料调拨"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 144
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# MATERIAL (物料调拨)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 144

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]

---

## Tables


- **MATERIAL_SHIFT (挪料单)**
- **MATERIAL_SHIFT_D (挪料单单身)**
- **MATERIAL_SHIFT_MO (挪料工单信息)**


---


---


> Tables: 3

### MATERIAL_SHIFT (挪料单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MATERIAL_SHIFT_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | ISSUE_DOC_ID | 领料单号 | GUID | Y |  |
| 10 | RECEIPT_DOC_ID | 退料单号 | GUID | Y |  |
| 11 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 12 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 13 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 14 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | PrintCount | 打印次数 | number | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### MATERIAL_SHIFT_D (挪料单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MATERIAL_SHIFT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 材料品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 材料规格 | string(510) | Y |  |
| 5 | SHIFT_QTY | 挪料数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | MO_FROM_ID | 挪出工单单号 | GUID | Y |  |
| 15 | MO_TO_ID | 挪入工单单号 | GUID | Y |  |
| 16 | ITEM_ID | 材料品号 | GUID | Y |  |
| 17 | ITEM_FEATURE_ID | 材料特征码 | GUID | Y |  |
| 18 | UNIT_ID | 业务单位 | GUID | Y |  |
| 19 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 20 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 21 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 22 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 23 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 24 | SHIFT_OUT_OPERATION_ID | 挪出工艺 | GUID | Y |  |
| 25 | SHIFT_IN_OPERATION_ID | 挪入工艺 | GUID | Y |  |
| 26 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 27 | BIN_ID | 库位 | GUID | Y |  |
| 28 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 29 | PROJECT_ID | 项目 | GUID | Y |  |
| 30 | OUT_PROJECT_ID | 挪出项目 | GUID | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 38 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 39 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 40 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 41 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 42 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 43 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 44 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 45 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 46 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 47 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 48 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 49 | UDF041 | 自定义字段12 | date | Y |  |
| 50 | UDF042 | 自定义字段13 | date | Y |  |
| 51 | UDF051 | 自定义字段14 | GUID | Y |  |
| 52 | UDF052 | 自定义字段15 | GUID | Y |  |
| 53 | UDF053 | 自定义字段16 | GUID | Y |  |
| 54 | UDF054 | 自定义字段17 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | MATERIAL_SHIFT_ID |  | GUID | Y |  |

### MATERIAL_SHIFT_MO (挪料工单信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MATERIAL_SHIFT_MO_ID | 主键 | GUID | Y | Y |
| 2 | SHIFT_SETS | 挪料套数 | number(16,6) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | MO_FROM_ID | 挪出工单单号 | GUID | Y |  |
| 5 | MO_TO_ID | 挪入工单单号 | GUID | Y |  |
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
| 34 | SHIFT_FROM_DESTINATION_RTK |  | string(400) | Y |  |
| 35 | SHIFT_FROM_DESTINATION_ROid |  | GUID | Y |  |
| 36 | SHIFT_TO_DESTINATION_RTK |  | string(400) | Y |  |
| 37 | SHIFT_TO_DESTINATION_ROid |  | GUID | Y |  |
| 38 | MATERIAL_SHIFT_ID |  | GUID | Y |  |