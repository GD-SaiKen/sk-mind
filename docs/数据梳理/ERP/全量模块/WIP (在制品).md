---
module: "WIP"
name_zh: "在制品"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 0
columns: 0
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# WIP (在制品)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 0 | Columns: 0

## Related Modules

- [[ABTABAC (表格映射)|ABTABAC (表格映射)]]
- [[ABTABVC (表格方案)|ABTABVC (表格方案)]]
- [[ACCCODE (科目数据集)|ACCCODE (科目数据集)]]
- [[ACCESS (权限控制)|ACCESS (权限控制)]]
- [[ACCPERIOD (会计期间)|ACCPERIOD (会计期间)]]
- [[ALTER (变更)|ALTER (变更)]]
- [[AM (资产报表)|AM (资产报表)]]
- [[AU (辅助特性)|AU (辅助特性)]]

---

# WIP (在制品)

> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
 | Server: .\\SQLEXPRESS | Tables: 3 | Generated: 2026-06-25 10:52

---


> Tables: 3

### WIP_FACT_TABLE - 在制量分析表

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DATE | 日期 | date | Y |  |
| 4 | OPERATION_CODE | 工艺编码 | string(20) | Y |  |
| 5 | OPERATION_NAME | 工艺名称 | string(40) | Y |  |
| 6 | WIP_QTY | 在制品数量 | number(16,6) | Y |  |
| 7 | PRODUCTION_QTY | 产出数量 | number(16,6) | Y |  |
| 8 | WIP_FACT_TABLE_ID | 主键 | GUID | Y | Y |
| 9 | OPERATION_ID | 工艺 | GUID | Y |  |
| 10 | UNIT_ID | 单位 | GUID | Y |  |
| 11 | UNIT_CODE | 单位编码 | string(8) | Y |  |
| 12 | UNIT_NAME | 单位名称 | string(20) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### WIP_TRANSFER_DOC - 转移单信息

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | WIP_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 转移日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | FROM_ADMIN_UNIT_ID | 移出部门 | GUID | Y |  |
| 10 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 11 | PURCHASE_RECEIPT_ID | 采购入库单 | GUID | Y |  |
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
| 31 | PrintCount | 打印次数 | number | Y |  |
| 32 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 33 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 34 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 35 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |
| 51 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 52 | DISPATCH_DOC_SEQ | 派工序号 | string(400) | Y |  |

### WIP_TRANSFER_DOC_D - 转移单单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | WIP_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | TYPE | 类型 | string(40) | Y |  |
| 4 | ITEM_NAME | 产品品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 产品规格 | string(510) | Y |  |
| 6 | QTY |  | number(16,6) | Y |  |
| 7 | BONUS_QTY | 超入量 | number(16,6) | Y |  |
| 8 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 9 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | ITEM_ID | 产品品号 | GUID | Y |  |
| 12 | FROM_MO_ROUTING_D_ID | 移出工序 | GUID | Y |  |
| 13 | TO_MO_ROUTING_D_ID | 移入工序 | GUID | Y |  |
| 14 | UNIT_ID | 主键 | GUID | Y |  |
| 15 | TO_ADMIN_UNIT_ID | 移入部门 | GUID | Y |  |
| 16 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 17 | PURCHASE_DOC_ID | 采购单别 | GUID | Y |  |
| 18 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 19 | MO_ID | 主键 | GUID | Y |  |
| 20 | PURCHASE_ORDER_ID | 主键 | GUID | Y |  |
| 21 | BIN_ID | 库位 | GUID | Y |  |
| 22 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 23 | PROJECT_ID | 项目 | GUID | Y |  |
| 24 | SCRAPED_QTY | 已报废数量 | number(16,6) | Y |  |
| 25 | FIRST_CHECKIN_TIME | 最早上线时间 | date | Y |  |
| 26 | LAST_CHECKOUT_DATETIME | 最晚下线时间 | date | Y |  |
| 27 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 28 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 29 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 30 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 31 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 32 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 33 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 34 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 35 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 36 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 37 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 38 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 39 | UDF041 | 自定义字段12 | date | Y |  |
| 40 | UDF042 | 自定义字段13 | date | Y |  |
| 41 | UDF051 | 自定义字段14 | GUID | Y |  |
| 42 | UDF052 | 自定义字段15 | GUID | Y |  |
| 43 | UDF053 | 自定义字段16 | GUID | Y |  |
| 44 | UDF054 | 自定义字段17 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE_ID_ROid |  | GUID | Y |  |
| 57 | WIP_TRANSFER_DOC_ID |  | GUID | Y |  |
| 58 | MO_ROUTING_DISPATCH_D_ID | 派工单号 | GUID | Y |  |
| 59 | DISPATCH_AGAIN | 重新委外 | number(0/1) | Y |  |
| 60 | PURCHASE_RETURN_ID | 采购退货单号 | GUID | Y |  |
| 61 | PURCHASE_RETURN_DOC_ID | 采购退货单据类型 | GUID | Y |  |
| 62 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 63 | SCRAP_TYPE | 报废类型 | string(40) | Y |  |
| 64 | SOURCE_DOC_ID_RTK |  | string(400) | Y |  |
| 65 | SOURCE_DOC_ID_ROid |  | GUID | Y |  |
| 66 | TO_SOURCE_ID_RTK |  | string(400) | Y |  |
| 67 | TO_SOURCE_ID_ROid |  | GUID | Y |  |