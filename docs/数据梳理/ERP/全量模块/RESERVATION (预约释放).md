---
module: "RESERVATION"
name_zh: "预约释放"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 115
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# RESERVATION (预约释放)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 115

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

## Tables


- **RESERVATION_RELEASE_DOC (保留释出单)**
- **RESERVATION_RELEASE_DOC_D (保留释出单单身)**


---


---


> Tables: 2

### RESERVATION_RELEASE_DOC (保留释出单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | RESERVATION_RELEASE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | WAREHOUSE_ID | 限用仓库编号 | GUID | Y |  |
| 12 | COMPANY_ID | 公司 | GUID | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 21 | Version | 版本号，不要随意更改 | binary | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | PrintCount | 打印次数 | number | Y |  |
| 44 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 45 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 46 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 47 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### RESERVATION_RELEASE_DOC_D (保留释出单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | RESERVATION_RELEASE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | PIECES |  | number | Y |  |
| 6 | CLOSE | 结束 | string(40) | Y |  |
| 7 | RESERVED_INEFFECTIVE_DATE | 保留失效日 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | ITEM_ID | 品号 | GUID | Y |  |
| 10 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 11 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 12 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 13 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 14 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 15 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 16 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 17 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 18 | RESERVATION_INVENTORY_QTY | 保留库存单位数量 | number(16,6) | Y |  |
| 19 | RESERVATION_SECOND_QTY | 保留第二数量 | number(16,6) | Y |  |
| 20 | RELEASE_INVENTORY_QTY | 释出库存单位数量 | number(16,6) | Y |  |
| 21 | RELEASE_SECOND_QTY | 释出第二数量 | number(16,6) | Y |  |
| 22 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 23 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 24 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 25 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 26 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 27 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 28 | BIN_ID | 库位 | GUID | Y |  |
| 29 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 30 | RESERVE_D_ID | 核销保留单身ID | GUID | Y |  |
| 31 | PROJECT_ID | 项目 | GUID | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE_ID_ROid |  | GUID | Y |  |
| 62 | ISSUE_D_ID_RTK |  | string(400) | Y |  |
| 63 | ISSUE_D_ID_ROid |  | GUID | Y |  |
| 64 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 65 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 66 | RESERVATION_RELEASE_DOC_ID |  | GUID | Y |  |