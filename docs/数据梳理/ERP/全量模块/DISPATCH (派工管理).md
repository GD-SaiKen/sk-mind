---
module: "DISPATCH"
name_zh: "派工管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 171
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# DISPATCH (派工管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 171

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


- **DISPATCH_D**
- **DISPATCH_LIST (DISPATCH_LIST)**


---


---


> Tables: 3

### DISPATCH

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DISPATCH_ID | 主键 | GUID | Y | Y |
| 7 | DELIVEYR_RESOURCE_ID | 车号 | GUID | Y |  |
| 8 | ROOT_ID | 配送路线 | GUID | Y |  |
| 9 | WEIGHT | 承载重量 | number(16,6) | Y |  |
| 10 | WEIGHT1 | 已调度重量 | number(16,6) | Y |  |
| 11 | BULK | 承载体积 | number(16,6) | Y |  |
| 12 | BULK1 | 已调度体积 | number(16,6) | Y |  |
| 13 | OVERLOAD | 超载 | number(0/1) | Y |  |
| 14 | OUT_DATE | 出车日期 | date | Y |  |
| 15 | OUT_MILEAGE | 出车里程 | number(16,6) | Y |  |
| 16 | PILOT_ID | 驾驶员 | GUID | Y |  |
| 17 | PILOT_TELE | 驾驶员手机号 | string(80) | Y |  |
| 18 | COPILOT_ID | 副驾驶 | GUID | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | CATEGORY | 单据性质 | string(40) | Y |  |
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
| 39 | PrintCount | 打印次数 | number | Y |  |
| 40 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 41 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 42 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 43 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |

### DISPATCH_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISPATCH_D_ID |  | GUID | Y | Y |
| 3 | RECEIVE_ADDR |  | string(510) | Y |  |
| 4 | DIRECTOR | 直供发起方 | GUID | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TEMP_DISTRIBUTION | 临时配送 | number(0/1) | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 11 | FEATURE_VALUE | 物流分类 | string(120) | Y |  |
| 12 | WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 13 | BIN_ID | 发货库位 | GUID | Y |  |
| 14 | TRANSIT_WAREHOUSE_ID | 在途仓 | GUID | Y |  |
| 15 | DISTRIBUTION_QTY | 配送数量 | number(16,6) | Y |  |
| 16 | STORAGE_QTY | 已入库量 | number(16,6) | Y |  |
| 17 | DIFF_QTY | 差异数量 | number(16,6) | Y |  |
| 18 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 19 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 20 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 21 | COST | 单位成本 | number(23,8) | Y |  |
| 22 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 23 | CLOSED | 结束码 | string(40) | Y |  |
| 24 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | INVENTORY_QTY1 | 入库库存单位数量 | number(16,6) | Y |  |
| 27 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 28 | BULK | 体积 | number(16,6) | Y |  |
| 29 | WEIGHT | 重量 | number(16,6) | Y |  |
| 30 | CONT_MAN | 订货人 | string(20) | Y |  |
| 31 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 32 | CONT_TEL | 联系电话 | string(40) | Y |  |
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
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | CreateDate | 创建日期 | date | Y |  |
| 53 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 54 | ModifiedDate | 修改日期 | date | Y |  |
| 55 | CreateBy | 创建者 | GUID | Y |  |
| 56 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 57 | ModifiedBy | 修改者 | GUID | Y |  |
| 58 | DISTRIBUTION_OBJECT_RTK |  | string(400) | Y |  |
| 59 | DISTRIBUTION_OBJECT_ROid |  | GUID | Y |  |
| 60 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE_ID_ROid |  | GUID | Y |  |
| 62 | SOURCE_ID1_RTK |  | string(400) | Y |  |
| 63 | SOURCE_ID1_ROid |  | GUID | Y |  |
| 64 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 65 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 66 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 67 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 68 | DISPATCH_ID |  | GUID | Y |  |

### DISPATCH_LIST (DISPATCH_LIST)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DISPATCH_LIST_ID | 主键 | GUID | Y | Y |
| 4 | ENTERPRISE_NO |  | number(5,0) | Y |  |
| 5 | SITE_NO |  | string(20) | Y |  |
| 6 | DOC_NO |  | string(40) | Y |  |
| 7 | PLOT_NO |  | string(80) | Y |  |
| 8 | ITEM_NO |  | string(80) | Y |  |
| 9 | ITEM_FEATURE_CODE |  | string(120) | Y |  |
| 10 | WORKSTATION_NO |  | string(20) | Y |  |
| 11 | MACHINE_NO |  | string(30) | Y |  |
| 12 | QTY |  | number(20,6) | Y |  |
| 13 | DISPATCH_DATE |  | date | Y |  |
| 14 | DISPATCH_TIME |  | string(16) | Y |  |
| 15 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 40 | Attachments | 附件 | string | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |