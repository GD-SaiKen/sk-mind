---
module: "STOCK"
name_zh: "库存请购"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 104
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# STOCK (库存请购)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 104

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


- **STOCK_REQUISITION (出库申请单)**
- **STOCK_REQUISITION_D (出库申请单单身)**


---


---


> Tables: 2

### STOCK_REQUISITION (出库申请单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | STOCK_REQUISITION_ID |  | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 12 | COMPANY_ID | 公司 | GUID | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 15 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 16 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 17 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
| 26 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 27 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 28 | ApproveDate | 修改日期 | date | Y |  |
| 29 | ApproveBy | 修改人 | GUID | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### STOCK_REQUISITION_D (出库申请单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 3 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 4 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 5 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | PIECES |  | number | Y |  |
| 9 | CLOSE | 结束码 | string(40) | Y |  |
| 10 | STOCK_REQUISITION_D_ID | 主键 | GUID | Y | Y |
| 11 | RELEASE_BUSINESS_QTY | 已出库业务数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 13 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 14 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 15 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 16 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 17 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 18 | ITEM_ID | 品号 | GUID | Y |  |
| 19 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 20 | WAREHOUSE_ID | 仓库编号 | GUID | Y |  |
| 21 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 22 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 23 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 24 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 25 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 26 | PROJECT_ID | 项目 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
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
| 55 | STOCK_REQUISITION_ID |  | GUID | Y |  |