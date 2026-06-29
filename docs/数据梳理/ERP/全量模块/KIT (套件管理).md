---
module: "KIT"
name_zh: "套件管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 196
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# KIT (套件管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 196

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


- **KIT_DISTRIBUTION (零组件配送单)**
- **KIT_DISTRIBUTION_D (零组件配送单单身)**
- **KIT_LIST (零组件清单)**
- **KIT_LIST_D (零组件清单单身)**


---


---


> Tables: 4

### KIT_DISTRIBUTION (零组件配送单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | KIT_DISTRIBUTION_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 9 | SOURCE_ID | 发货计划ID | GUID | Y |  |
| 10 | FROM_WAREHOUSE_ID | 限用转出仓库 | GUID | Y |  |
| 11 | TO_WAREHOUSE_ID | 零组件接收仓库 | GUID | Y |  |
| 12 | TO_BIN_ID | 库位 | GUID | Y |  |
| 13 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 14 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 15 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 16 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 17 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 18 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 19 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 20 | COMPANY_ID | 公司 | GUID | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | BUSINESS_QTY | 本次配送业务数量 | number(16,6) | Y |  |
| 23 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 24 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 25 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 26 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 27 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | PrintCount | 打印次数 | number | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |
| 61 | PROJECT_ID | 项目 | GUID | Y |  |

### KIT_DISTRIBUTION_D (零组件配送单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | KIT_DISTRIBUTION_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 零组件品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 零组件品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 零组件特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION | 零组件规格 | string(510) | Y |  |
| 7 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 8 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 9 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 10 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 13 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 14 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 15 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 16 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 17 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 18 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 19 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 20 | PLAN_SHIP_DATE | 预发货日 | date | Y |  |
| 21 | PIECES | 件数 | number | Y |  |
| 22 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 23 | FROM_BIN_ID | 转出库位 | GUID | Y |  |
| 24 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | SOURCE_ID | 配送清单序号 | GUID | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 56 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 57 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 58 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 59 | KIT_DISTRIBUTION_ID |  | GUID | Y |  |

### KIT_LIST (零组件清单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | KIT_LIST_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | VERSION_TIMES | 版次 | string(8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
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
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Attachments | 附件 | string | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### KIT_LIST_D (零组件清单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | KIT_LIST_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 零组件品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 零组件品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 零组件特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION | 零组件规格 | string(510) | Y |  |
| 7 | COMPOSE_QTY | 数量 | number(16,6) | Y |  |
| 8 | DISTRIBUTION_GROUP | 配送群组 | string(60) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
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
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | KIT_LIST_ID |  | GUID | Y |  |