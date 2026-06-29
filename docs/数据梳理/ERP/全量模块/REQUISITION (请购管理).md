---
module: "REQUISITION"
name_zh: "请购管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 174
category: purchase
tags: ["ERP", "E10", "purchase"]
created: 2026-06-25 10:52

---

# REQUISITION (请购管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 3 | Columns: 174

## Related Modules

- [[IMPORT (进口管理)|IMPORT (进口管理)]]
- [[NEGOTIATE (议价管理)|NEGOTIATE (议价管理)]]
- [[PO (采购订单)|PO (采购订单)]]
- [[PURCHASE (采购管理)|PURCHASE (采购管理)]]
- [[SUPPLIER (供应商)|SUPPLIER (供应商)]]
- [[SUPPLY (供应中心)|SUPPLY (供应中心)]]

---

## Tables


- **REQUISITION_D (请购单明细)**
- **REQUISITION_SD**


---


---


> Tables: 3

### REQUISITION (请购单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | REQUISITION_ID | 主键 | GUID | Y | Y |
| 7 | REQUISITION_DATE | 请购日期 | date | Y |  |
| 8 | REQUISITION_TYPE | 请购类型 | string(40) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CATEGORY | 单据性质 | string(40) | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | PrintCount | 打印次数 | number | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 36 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 37 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 38 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### REQUISITION_D (请购单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | REQUISITION_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | REQUISITION_QTY | 请购数量 | number(16,6) | Y |  |
| 8 | REQUIREMENT_DATE | 需求日期 | date | Y |  |
| 9 | URGENCY | 紧急 | number(0/1) | Y |  |
| 10 | MANUFACTURER | 品牌信息 | string(80) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | PURCHASED_QTY | 已采数量 | number(16,6) | Y |  |
| 13 | APPLY_QTY | 已分配数量 | number(16,6) | Y |  |
| 14 | DISPATCH_STATUS | 分配状态 | string(40) | Y |  |
| 15 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 16 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 17 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 18 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 20 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 21 | ITEM_ID | 品号 | GUID | Y |  |
| 22 | REQUISITION_UNIT_ID | 请购单位 | GUID | Y |  |
| 23 | SUPPLIER_ID | 参考供应商 | GUID | Y |  |
| 24 | ITEM_CERTIFICATION_D_ID | 认可文号 | GUID | Y |  |
| 25 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 26 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 27 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 28 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 29 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 30 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 31 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 32 | PROJECT_ID | 项目 | GUID | Y |  |
| 33 | DEMAND_NO | 需求单号 | string(8000) | Y |  |
| 34 | SUPPLY_DATE | 预计入库日 | date | Y |  |
| 35 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 65 | SOURCE_ID_ROid |  | GUID | Y |  |
| 66 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 67 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 68 | REQUISITION_ID |  | GUID | Y |  |
| 69 | PRICE | 单价 | number(23,8) | Y |  |
| 70 | AMOUNT | 金额 | number(23,8) | Y |  |
| 71 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 72 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 73 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 74 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 75 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 76 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 77 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |

### REQUISITION_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | REQUISITION_SD_ID | 主键 | GUID | Y | Y |
| 3 | DEMAND_NO | 需求单号 | string(510) | Y |  |
| 4 | DEMAND_QTY | 需求数量 | number(16,6) | Y |  |
| 5 | DEMAND_DATE | 需求日期 | date | Y |  |
| 6 | PURCHASED_QTY | 已采数量 | number(16,6) | Y |  |
| 7 | ARRIVED_QTY | 已到货数量 | number(16,6) | Y |  |
| 8 | RECEIPTED_QTY | 已入库数量 | number(16,6) | Y |  |
| 9 | PURCHASE_SEQUENCE | 采购核销顺序 | number | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE_ID_ROid |  | GUID | Y |  |
| 41 | REQUISITION_D_ID |  | GUID | Y |  |
| 42 | REQ_DISPATCHED_ID | 分配请购信息主键 | GUID | Y |  |
| 43 | PLAN_SHIP_DATE | 销售订单预发货日 | date | Y |  |
| 44 | LOCKED_FLAG | 供需关连锁定 | number(0/1) | Y |  |
| 45 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 46 | SOURCE_DEMAND_QTY | 源单本阶需求数量 | number(16,6) | Y |  |
| 47 | REQUISITION_D_DATE | 单身需求日期 | date | Y |  |
| 48 | PUR_INVENTORY_QTY | 已采库存单位数量 | number(16,6) | Y |  |
| 49 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |