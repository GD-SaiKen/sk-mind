---
module: "COUNTING"
name_zh: "盘点计划"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 220
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# COUNTING (盘点计划)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 220

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]
- [[ISSUE (发料出库)|ISSUE (发料出库)]]

---

## Tables


- **COUNTING_PLAN**
- **COUNTING_PLAN_BARCODE (COUNTING_PLAN_BARCODE)**
- **COUNTING_PLAN_CONDITION**


---


---


> Tables: 4

### COUNTING (实盘数量)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | COUNTING_ID | 主键 | GUID | Y | Y |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 10 | BIN_ID | 库位编号 | GUID | Y |  |
| 11 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 12 | COUNT_TYPE | 盘点类型 | string(20) | Y |  |
| 13 | COUNTING_QTY | 实盘数量 | number(16,6) | Y |  |
| 14 | SECOND_QTY | 实盘第二数量 | number(16,6) | Y |  |
| 15 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 16 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 17 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 18 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 20 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 21 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 22 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 23 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 24 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | PLAN_DATE | 计划盘点日期 | date | Y |  |
| 27 | COUNTING_DATE | 实盘日期 | date | Y |  |
| 28 | COMPANY_ID | 公司 | GUID | Y |  |
| 29 | COUNTING_PLAN_ID | 盘点计划编号ID | GUID | Y |  |
| 30 | DOC_NO | 盘点计划编号 | string(40) | Y |  |
| 31 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 32 | BUSINESS_QTY | 实盘业务数量 | number(16,6) | Y |  |
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
| 56 | CreateDate | 创建日期 | date | Y |  |
| 57 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 58 | ModifiedDate | 修改日期 | date | Y |  |
| 59 | CreateBy | 创建者 | GUID | Y |  |
| 60 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 61 | ModifiedBy | 修改者 | GUID | Y |  |
| 62 | Attachments | 附件 | string | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |
| 65 | BO_ID_RTK |  | string(400) | Y |  |
| 66 | BO_ID_ROid |  | GUID | Y |  |

### COUNTING_PLAN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | COUNTING_PLAN_ID | 主键 | GUID | Y | Y |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 10 | BIN_ID | 库位编号 | GUID | Y |  |
| 11 | COUNTING_QTY | 实盘数量 | number(16,6) | Y |  |
| 12 | BOOK_QTY | 账面数量 | number(16,6) | Y |  |
| 13 | SECOND_QTY | 实盘第二数量 | number(16,6) | Y |  |
| 14 | BOOK_SECOND_QTY | 账面第二数量 | number(16,6) | Y |  |
| 15 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 16 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 17 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 18 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 20 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 21 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 22 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 23 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 24 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | PLAN_DATE | 计划盘点日期 | date | Y |  |
| 27 | COUNTING_DATE | 实盘日期 | date | Y |  |
| 28 | COUNT_ID | 盘点调整单号 | GUID | Y |  |
| 29 | COMPANY_ID | 公司 | GUID | Y |  |
| 30 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 31 | DOC_NO | 盘点计划编号 | string(40) | Y |  |
| 32 | PrintCount | 打印次数 | number | Y |  |
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
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | CreateDate | 创建日期 | date | Y |  |
| 55 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 56 | ModifiedDate | 修改日期 | date | Y |  |
| 57 | CreateBy | 创建者 | GUID | Y |  |
| 58 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 59 | ModifiedBy | 修改者 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | Attachments | 附件 | string | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |
| 65 | BO_ID_RTK |  | string(400) | Y |  |
| 66 | BO_ID_ROid |  | GUID | Y |  |

### COUNTING_PLAN_BARCODE (COUNTING_PLAN_BARCODE)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COUNTING_PLAN_BARCODE_ID | 主键 | GUID | Y | Y |
| 3 | DOC_NO |  | string(40) | Y |  |
| 4 | COUNTING_TYPE |  | string(40) | Y |  |
| 5 | BARCODE_NO |  | string(400) | Y |  |
| 6 | ITEM_ID |  | GUID | Y |  |
| 7 | ITEM_FEATURE_ID |  | GUID | Y |  |
| 8 | ITEM_LOT_ID |  | GUID | Y |  |
| 9 | WAREHOUSE_ID |  | GUID | Y |  |
| 10 | BIN_ID |  | GUID | Y |  |
| 11 | QTY |  | number(16,6) | Y |  |
| 12 | PLANT_ID |  | GUID | Y |  |
| 13 | COUNTING_QTY | 实盘数量 | number(16,6) | Y |  |
| 14 | BOOK_QTY | 账面数量 | number(16,6) | Y |  |
| 15 | COUNTING_DIFF_QTY |  | number(16,6) | Y |  |
| 16 | COUNT_ID | 盘点调整单号 | GUID | Y |  |
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
| 47 | BO_ID_RTK |  | string(400) | Y |  |
| 48 | BO_ID_ROid |  | GUID | Y |  |

### COUNTING_PLAN_CONDITION

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COUNTING_PLAN_CONDITION_ID | 主键 | GUID | Y | Y |
| 4 | DOC_NO | 盘点计划编号 | string(40) | Y |  |
| 5 | PLAN_DATE | 计划盘点日期 | date | Y |  |
| 6 | ZERO_BIN_LOT_INCLUD | 生成账面库存数量为零品号 | number(0/1) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | COMPANY_ID | 主键 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |