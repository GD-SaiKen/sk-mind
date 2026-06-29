---
module: "TRANSACTION"
name_zh: "交易记录"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 247
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# TRANSACTION (交易记录)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 247

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


- **TRANSACTION_DOC (库存交易单)**
- **TRANSACTION_DOC_D (库存交易单单身)**
- **TRANSACTION_DOC_SD (库存交易单成本明细)**
- **TRANSACTION_LINE (存货交易明细)**


---


---


> Tables: 4

### TRANSACTION_DOC (库存交易单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | TRANSACTION_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | STOCK_ACTION | 库存影响 | number | Y |  |
| 12 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 13 | COMPANY_ID | 公司 | GUID | Y |  |
| 14 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 15 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 16 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 17 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 18 | GLOB_JE_ID | 主键 | GUID | Y |  |
| 19 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 20 | PPV_ROUTING_INDICATOR | 工艺委外价差调整 | number(0/1) | Y |  |
| 21 | POST_GL_INDICATOR | 需生成分录 | number(0/1) | Y |  |
| 22 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 23 | PLANT_ID | 限用工厂/储运 | GUID | Y |  |
| 24 | BEGINNING_ACCOUNT | 期初开账 | number(0/1) | Y |  |
| 25 | SUM_BUSINESS_QTY | 业务数量合计 | number(16,6) | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
| 27 | PrintCount | 打印次数 | number | Y |  |
| 28 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 29 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 30 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 31 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 61 | Owner_Org_RTK |  | string(400) | Y |  |
| 62 | Owner_Org_ROid |  | GUID | Y |  |
| 63 | INNER_TRANSFER_DOC_ID | 内部调拨单 | GUID | Y |  |
| 64 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 65 | SOURCE_ID_ROid |  | GUID | Y |  |

### TRANSACTION_DOC_D (库存交易单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TRANSACTION_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | PIECES |  | number | Y |  |
| 7 | VMI_SETTLED | VMI结算码 | string(40) | Y |  |
| 8 | ITEM_ID | 品号 | GUID | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 11 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 12 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 13 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 14 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 15 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 16 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 17 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 18 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 19 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 20 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 21 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 22 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 23 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 24 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 25 | BIN_ID | 库位 | GUID | Y |  |
| 26 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 27 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 28 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 29 | PPV_INVENTORY_QTY | 价差库存数量 | number(16,6) | Y |  |
| 30 | ADJUSTING_TYPE | 成本调整类型 | string(40) | Y |  |
| 31 | POST_GL_INDICATOR | 需生成分录 | number(0/1) | Y |  |
| 32 | MO_ID | 工单ID | GUID | Y |  |
| 33 | PROJECT_ID | 项目 | GUID | Y |  |
| 34 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 35 | SN_COLLECTED_QTY | 序列号已采集量 | number(16,6) | Y |  |
| 36 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 48 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 49 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 50 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 51 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 52 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 53 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 54 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 55 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 56 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 57 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 58 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 59 | UDF041 | 自定义字段12 | date | Y |  |
| 60 | UDF042 | 自定义字段13 | date | Y |  |
| 61 | UDF051 | 自定义字段14 | GUID | Y |  |
| 62 | UDF052 | 自定义字段15 | GUID | Y |  |
| 63 | UDF053 | 自定义字段16 | GUID | Y |  |
| 64 | UDF054 | 自定义字段17 | GUID | Y |  |
| 65 | BO_ID_RTK |  | string(400) | Y |  |
| 66 | BO_ID_ROid |  | GUID | Y |  |
| 67 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 68 | SOURCE_ID_ROid |  | GUID | Y |  |
| 69 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 70 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 71 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 72 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 73 | TRANSACTION_DOC_ID |  | GUID | Y |  |
| 74 | TO_ASSET_STATUS | 转资状态 | number | Y |  |
| 75 | TO_ASSET_SOURCE_ID_RTK |  | string(400) | Y |  |
| 76 | TO_ASSET_SOURCE_ID_ROid |  | GUID | Y |  |
| 77 | EQT_SOURCE_ID_RTK |  | string(400) | Y |  |
| 78 | EQT_SOURCE_ID_ROid |  | GUID | Y |  |

### TRANSACTION_DOC_SD (库存交易单成本明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TRANSACTION_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 4 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 5 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 9 | ApproveDate | 修改日期 | date | Y |  |
| 10 | ApproveBy | 修改人 | GUID | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 35 | TRANSACTION_DOC_D_ID |  | GUID | Y |  |

### TRANSACTION_LINE (存货交易明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TRANSACTION_LINE_ID | 主键 | GUID | Y | Y |
| 4 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 5 | STOCK_ACTION | 影响库存 | number | Y |  |
| 6 | CATEGORY | 单据性质 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 9 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 10 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 11 | TRANSACTION_CATEGORY | 交易别 | string(40) | Y |  |
| 12 | DOC_NO | 来源单号 | string(40) | Y |  |
| 13 | SEQUENCE_NO | 来源序号 | number | Y |  |
| 14 | COMPANY_ID | 公司代号 | GUID | Y |  |
| 15 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 16 | BIN_ID | 库位 | GUID | Y |  |
| 17 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 18 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 19 | ITEM_ID | 品号 | GUID | Y |  |
| 20 | DOC_ID | 单据类型 | GUID | Y |  |
| 21 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 22 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 23 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 24 | COST_CODE | 成本码 | string(40) | Y |  |
| 25 | MO_ID | 主键 | GUID | Y |  |
| 26 | COST_LOCK_FLAG | 成本锁定标识 | number(0/1) | Y |  |
| 27 | VMI_SETTLED | VMI结算码 | string(40) | Y |  |
| 28 | TRANSACTION_TIME | 交易时间 | time | Y |  |
| 29 | PROJECT_ID | 项目 | GUID | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Attachments | 附件 | string | Y |  |
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
| 55 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | Owner_Org_RTK |  | string(400) | Y |  |
| 61 | Owner_Org_ROid |  | GUID | Y |  |
| 62 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 63 | SOURCE_ID_ROid |  | GUID | Y |  |
| 64 | BO_ID_RTK |  | string(400) | Y |  |
| 65 | BO_ID_ROid |  | GUID | Y |  |
| 66 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 67 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 68 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 69 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |