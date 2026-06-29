---
module: "TRANSFER"
name_zh: "调拨管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 478
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# TRANSFER (调拨管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 8 | Columns: 478

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


- **TRANSFER_DOC (调拨单)**
- **TRANSFER_DOC_D (调拨单单身)**
- **TRANSFER_GOODS (调拨单)**
- **TRANSFER_GOODS_D (调拨单单身)**
- **TRANSFER_IN_DOC (拨入单)**
- **TRANSFER_IN_DOC_D (拨入单单身)**
- **TRANSFER_REQUISITION (调拨申请单)**
- **TRANSFER_REQUISITION_D (调拨申请单单身)**


---


---


> Tables: 8

### TRANSFER_DOC (调拨单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | TO_PLANT_ID | 转入工厂 | GUID | Y |  |
| 12 | FROM_WAREHOUSE_ID | 限用转出仓库 | GUID | Y |  |
| 13 | TO_WAREHOUSE_ID | 限用转入仓库 | GUID | Y |  |
| 14 | COMPANY_ID |  | GUID | Y |  |
| 15 | IN_WAREHOUSE_ID | 在途仓 | GUID | Y |  |
| 16 | TRANSFER_IN_DATE | 预计拨入日期 | date | Y |  |
| 17 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 18 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 19 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 20 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 21 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 22 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 23 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 24 | PrintCount | 打印次数 | number | Y |  |
| 25 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 26 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 27 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 28 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Attachments | 附件 | string | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 41 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 42 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 43 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 44 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 45 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 46 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 47 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 48 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 49 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 50 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 51 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 52 | UDF041 | 自定义字段12 | date | Y |  |
| 53 | UDF042 | 自定义字段13 | date | Y |  |
| 54 | UDF051 | 自定义字段14 | GUID | Y |  |
| 55 | UDF052 | 自定义字段15 | GUID | Y |  |
| 56 | UDF053 | 自定义字段16 | GUID | Y |  |
| 57 | UDF054 | 自定义字段17 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |
| 61 | INNER_TRANSFER_DOC_ID | 内部调拨单 | GUID | Y |  |

### TRANSFER_DOC_D (调拨单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 15 | TRANSFERED_BUSINESS_QTY | 已调拨业务数量 | number(16,6) | Y |  |
| 16 | PIECES |  | number | Y |  |
| 17 | CLOSE | 结束 | string(40) | Y |  |
| 18 | PACKING1_UNIT_ID | 大包裝單位 | GUID | Y |  |
| 19 | PACKING2_UNIT_ID | 中包裝單位 | GUID | Y |  |
| 20 | PACKING3_UNIT_ID | 小包裝單位 | GUID | Y |  |
| 21 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 22 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 23 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 24 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 25 | FROM_BIN_ID | 转出库位 | GUID | Y |  |
| 26 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 27 | ITEM_LOT_ID |  | GUID | Y |  |
| 28 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 29 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 30 | BC_CHECK_STATUS | 检核码 | string(40) | Y |  |
| 31 | PROJECT_ID | 项目 | GUID | Y |  |
| 32 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 33 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 44 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 45 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 46 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 47 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 48 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 49 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 50 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 51 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 52 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 53 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 54 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 55 | UDF041 | 自定义字段12 | date | Y |  |
| 56 | UDF042 | 自定义字段13 | date | Y |  |
| 57 | UDF051 | 自定义字段14 | GUID | Y |  |
| 58 | UDF052 | 自定义字段15 | GUID | Y |  |
| 59 | UDF053 | 自定义字段16 | GUID | Y |  |
| 60 | UDF054 | 自定义字段17 | GUID | Y |  |
| 61 | Version | 版本号，不要随意更改 | binary | Y |  |
| 62 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 63 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 64 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 65 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 66 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 67 | SOURCE_ID_ROid |  | GUID | Y |  |
| 68 | TRANSFER_DOC_ID |  | GUID | Y |  |
| 69 | MO_D_ID | 工单序号 | GUID | Y |  |
| 70 | MO_ID | 工单 | GUID | Y |  |

### TRANSFER_GOODS (调拨单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | TRANSFER_GOODS_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANS_DATE | 调拨日期 | date | Y |  |
| 9 | OUT_SHOP_ID | 调出门店 | GUID | Y |  |
| 10 | OUT_WAREHOUSE_ID | 调出仓库 | GUID | Y |  |
| 11 | IN_SHOP_ID | 调入门店 | GUID | Y |  |
| 12 | IN_WAREHOUSE_ID | 调入仓库 | GUID | Y |  |
| 13 | OUT_DOC_NO | 调出单号 | string(40) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | POS_ID | POS机号 | GUID | Y |  |
| 16 | CLASS_ID | 班次 | number | Y |  |
| 17 | PrintCount | 打印次数 | number | Y |  |
| 18 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 19 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 20 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 21 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |
| 54 | OUT_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 55 | OUT_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 56 | IN_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 57 | IN_COST_DOMAIN_ID_ROid |  | GUID | Y |  |

### TRANSFER_GOODS_D (调拨单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TRANSFER_GOODS_D_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | UNIT_ID | 物流单位 | GUID | Y |  |
| 8 | OUT_QTY | 调出数量 | number(16,6) | Y |  |
| 9 | OUT_INVENTORY_QTY | 调出库存单位数量 | number(16,6) | Y |  |
| 10 | OUT_SECOND_QTY | 调出第二数量 | number(16,6) | Y |  |
| 11 | IN_QTY | 调入数量 | number(16,6) | Y |  |
| 12 | IN_INVENTORY_QTY | 调入库存单位数量 | number(16,6) | Y |  |
| 13 | IN_SECOND_QTY | 调入第二数量 | number(16,6) | Y |  |
| 14 | COST | 单位成本 | number(23,8) | Y |  |
| 15 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 18 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 19 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 20 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 21 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 22 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 23 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 24 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 25 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 26 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 27 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 28 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 29 | UDF041 | 自定义字段12 | date | Y |  |
| 30 | UDF042 | 自定义字段13 | date | Y |  |
| 31 | UDF051 | 自定义字段14 | GUID | Y |  |
| 32 | UDF052 | 自定义字段15 | GUID | Y |  |
| 33 | UDF053 | 自定义字段16 | GUID | Y |  |
| 34 | UDF054 | 自定义字段17 | GUID | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |
| 44 | TRANSFER_GOODS_ID |  | GUID | Y |  |

### TRANSFER_IN_DOC (拨入单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | TRANSFER_IN_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 10 | PIECES | 件数 | number | Y |  |
| 11 | FROM_PLANT_ID | 转出工厂 | GUID | Y |  |
| 12 | FROM_WAREHOUSE_ID | 限用转出仓库 | GUID | Y |  |
| 13 | TO_WAREHOUSE_ID | 限用转入仓库 | GUID | Y |  |
| 14 | COMPANY_ID |  | GUID | Y |  |
| 15 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 16 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 17 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 18 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 19 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 20 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 21 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | PrintCount | 打印次数 | number | Y |  |
| 45 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 46 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 47 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 48 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | Attachments | 附件 | string | Y |  |
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | Owner_Org_RTK |  | string(400) | Y |  |
| 58 | Owner_Org_ROid |  | GUID | Y |  |

### TRANSFER_IN_DOC_D (拨入单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TRANSFER_IN_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 11 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PIECES | 件数 | number | Y |  |
| 14 | PACKING1_UNIT_ID | 大包裝單位 | GUID | Y |  |
| 15 | PACKING2_UNIT_ID | 中包裝單位 | GUID | Y |  |
| 16 | PACKING3_UNIT_ID | 小包裝單位 | GUID | Y |  |
| 17 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 18 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 19 | ITEM_ID | 品号 | GUID | Y |  |
| 20 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 21 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 22 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 23 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 24 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 25 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 26 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 27 | SOURCE_ID | 源单ID | GUID | Y |  |
| 28 | PROJECT_ID | 项目 | GUID | Y |  |
| 29 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 30 | SN_COLLECTED_STATUS | 序列号检核状态 | string(40) | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 33 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 34 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 35 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 36 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 37 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 38 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 39 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 40 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 41 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 42 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 43 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 44 | UDF041 | 自定义字段12 | date | Y |  |
| 45 | UDF042 | 自定义字段13 | date | Y |  |
| 46 | UDF051 | 自定义字段14 | GUID | Y |  |
| 47 | UDF052 | 自定义字段15 | GUID | Y |  |
| 48 | UDF053 | 自定义字段16 | GUID | Y |  |
| 49 | UDF054 | 自定义字段17 | GUID | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | CreateDate | 创建日期 | date | Y |  |
| 54 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 55 | ModifiedDate | 修改日期 | date | Y |  |
| 56 | CreateBy | 创建者 | GUID | Y |  |
| 57 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 58 | ModifiedBy | 修改者 | GUID | Y |  |
| 59 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 60 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 61 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 62 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 63 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 64 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 65 | TRANSFER_IN_DOC_ID |  | GUID | Y |  |
| 66 | MO_D_ID | 工单序号 | GUID | Y |  |
| 67 | MO_ID | 工单 | GUID | Y |  |

### TRANSFER_REQUISITION (调拨申请单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TRANSFER_REQUISITION_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质码 | string(400) | Y |  |
| 8 | FROM_PLANT_ID | 主鍵 | GUID | Y |  |
| 9 | PIECES |  | number | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | TRANSACTION_DATE | 申请日期 | date | Y |  |
| 12 | COMPANY_ID | 主键 | GUID | Y |  |
| 13 | FROM_WAREHOUSE_ID | 限用转出仓库 | GUID | Y |  |
| 14 | TO_WAREHOUSE_ID | 限用转入仓库 | GUID | Y |  |
| 15 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 16 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 17 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 18 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 19 | PrintCount | 打印次数 | number | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
| 27 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 28 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 29 | ApproveDate | 修改日期 | date | Y |  |
| 30 | ApproveBy | 修改人 | GUID | Y |  |
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
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |
| 52 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 53 | IS_INNER | 集团内委外 | number(0/1) | Y |  |

### TRANSFER_REQUISITION_D (调拨申请单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 8 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 10 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 11 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 13 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 14 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 15 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 16 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 17 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 18 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 19 | REQUISITION_DATE | 需求日期 | date | Y |  |
| 20 | PIECES |  | number | Y |  |
| 21 | CLOSE | 结束码 | string(40) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | TRANS_OUT_BUSINESS_QTY | 已调出业务数量 | number(16,6) | Y |  |
| 24 | TRANS_IN_BUSINESS_QTY | 已拨入业务数量 | number(16,6) | Y |  |
| 25 | PRE_TRANS_IN_BUSINESS_QTY | 预计拨入业务数量 | number(16,6) | Y |  |
| 26 | TRANSFER_REQUISITION_D_ID | 主键 | GUID | Y | Y |
| 27 | PLAN_STATUS | 计划状态 | string(40) | Y |  |
| 28 | PROJECT_ID | 项目 | GUID | Y |  |
| 29 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 30 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 41 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 42 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 43 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 44 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 45 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 46 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 47 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 48 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 49 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 50 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 51 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 52 | UDF041 | 自定义字段12 | date | Y |  |
| 53 | UDF042 | 自定义字段13 | date | Y |  |
| 54 | UDF051 | 自定义字段14 | GUID | Y |  |
| 55 | UDF052 | 自定义字段15 | GUID | Y |  |
| 56 | UDF053 | 自定义字段16 | GUID | Y |  |
| 57 | UDF054 | 自定义字段17 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE_ID_ROid |  | GUID | Y |  |
| 61 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 62 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 63 | TRANSFER_REQUISITION_ID |  | GUID | Y |  |
| 64 | CLIENT_ITEM_ID | 委托方品号 | GUID | Y |  |
| 65 | CLIENT_ITEM_DESCRIPTION | 委托方品名 | string(120) | Y |  |
| 66 | CLIENT_ITEM_FEATURE_ID | 委托方特征码 | GUID | Y |  |
| 67 | CLIENT_ITEM_SPECIFICATION | 委托方规格 | string(510) | Y |  |
| 68 | TRANSFER_TYPE | 调拨类型 | string(40) | Y |  |