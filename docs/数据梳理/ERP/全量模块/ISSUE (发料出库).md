---
module: "ISSUE"
name_zh: "发料出库"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 16
columns: 703
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# ISSUE (发料出库)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 16 | Columns: 703

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


- **ISSUE_RECEIPT (领/退料单)**
- **ISSUE_RECEIPT_D (领/退料单单身)**
- **ISSUE_RECEIPT_MO (领/退料工单信息)**
- **ISSUE_RECEIPT_REQ**
- **ISSUE_RECEIPT_REQ_D**
- **ISSUE_RECEIPT_REQ_MO**
- **ISSUE_TREE (议题指标树信息)**
- **ISSUE_TREE_ATTENTION (ISSUE_TREE_ATTENTION)**
- **ISSUE_TREE_AUTHORITY (ISSUE_TREE_AUTHORITY)**
- **ISSUE_TREE_AUTHORITY_D (指标树权限议题明细)**
- **ISSUE_TREE_AUTHORITY_USER (指标树权限用户明细)**
- **ISSUE_TREE_D (议题指标树信息明细)**
- **ISSUE_TREE_INTERRELATED (议题指标树信息相关作业)**
- **ISSUE_TREE_SD (议题指标树信息子明细)**
- **ISSUE_TREE_SD2 (指标参数信息)**
- **ISSUE_TREE_VIEWSET (ISSUE_TREE_VIEWSET)**


---


---


> Tables: 16

### ISSUE_RECEIPT (领/退料单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ISSUE_RECEIPT_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质码 | string(400) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 10 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 11 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 12 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 13 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 14 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 15 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 24 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 25 | ApproveDate | 修改日期 | date | Y |  |
| 26 | ApproveBy | 修改人 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | PrintCount | 打印次数 | number | Y |  |
| 29 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 30 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 31 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 32 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 33 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 34 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 35 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 36 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 37 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 38 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 39 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 40 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 41 | UDF041 | 自定义字段12 | date | Y |  |
| 42 | UDF042 | 自定义字段13 | date | Y |  |
| 43 | UDF051 | 自定义字段14 | GUID | Y |  |
| 44 | UDF052 | 自定义字段15 | GUID | Y |  |
| 45 | UDF053 | 自定义字段16 | GUID | Y |  |
| 46 | UDF054 | 自定义字段17 | GUID | Y |  |
| 47 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 48 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 49 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 50 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |
| 53 | SOURCE_DOC_ID_RTK |  | string(400) | Y |  |
| 54 | SOURCE_DOC_ID_ROid |  | GUID | Y |  |
| 55 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE_ID_ROid |  | GUID | Y |  |
| 57 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 58 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |

### ISSUE_RECEIPT_D (领/退料单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_RECEIPT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 材料品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 材料规格 | string(510) | Y |  |
| 5 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 6 | ISSUE_RECEIPT_QTY | 领退料数量 | number(16,6) | Y |  |
| 7 | ACTUAL_ISSUE_RECEIPT_QTY | 实际数量 | number(16,6) | Y |  |
| 8 | SECOND_QTY | 领料第二数量 | number(16,6) | Y |  |
| 9 | ACTUAL_SECOND_QTY | 实际第二数量 | number(16,6) | Y |  |
| 10 | INVENTORY_QTY | 领料库存数量 | number(16,6) | Y |  |
| 11 | ACTUAL_INVENTORY_QTY | 实际库存数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 13 | ACTUAL_PACKING_QTY1 | 实际大包装数量 | number(16,6) | Y |  |
| 14 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 15 | ACTUAL_PACKING_QTY2 | 实际中包装数量 | number(16,6) | Y |  |
| 16 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 17 | ACTUAL_PACKING_QTY3 | 实际小包装数量 | number(16,6) | Y |  |
| 18 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 19 | ACTUAL_PACKING_QTY4 | 实际最小包装数量 | number(16,6) | Y |  |
| 20 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 21 | ISSUE_COMMENT | 领料说明 | string(510) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | SOURCE_MO_ID | 源工单 | GUID | Y |  |
| 24 | VMI_SETTLED | VMI结算码 | string(40) | Y |  |
| 25 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 26 | MO_ID | 工单单号 | GUID | Y |  |
| 27 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 28 | ITEM_ID | 材料品号 | GUID | Y |  |
| 29 | ITEM_FEATURE_ID | 材料特征码 | GUID | Y |  |
| 30 | UNIT_ID | 单位 | GUID | Y |  |
| 31 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 32 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 33 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 34 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 35 | OPERATION_ID | 工艺 | GUID | Y |  |
| 36 | BIN_ID | 库位 | GUID | Y |  |
| 37 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 38 | ISSUE_RECEIPT_REQ_ID | 领料申请单 | GUID | Y |  |
| 39 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 40 | MO_D_ID | 工单单身 | GUID | Y |  |
| 41 | SOURCE_TYPE | 类别 | string(40) | Y |  |
| 42 | REPLACED_MO_D_ID | 被取替代工单单身 | GUID | Y |  |
| 43 | BC_CHECK_STATUS | 检核码 | string(40) | Y |  |
| 44 | PROJECT_ID | 项目 | GUID | Y |  |
| 45 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 46 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 58 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 59 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 60 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 61 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 62 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 63 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 64 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 65 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 66 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 67 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 68 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 69 | UDF041 | 自定义字段12 | date | Y |  |
| 70 | UDF042 | 自定义字段13 | date | Y |  |
| 71 | UDF051 | 自定义字段14 | GUID | Y |  |
| 72 | UDF052 | 自定义字段15 | GUID | Y |  |
| 73 | UDF053 | 自定义字段16 | GUID | Y |  |
| 74 | UDF054 | 自定义字段17 | GUID | Y |  |
| 75 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 76 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 77 | ISSUE_DESTINATION_RTK |  | string(400) | Y |  |
| 78 | ISSUE_DESTINATION_ROid |  | GUID | Y |  |
| 79 | ISSUE_RECEIPT_ID |  | GUID | Y |  |

### ISSUE_RECEIPT_MO (领/退料工单信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ISSUE_RECEIPT_MO_ID | 主键 | GUID | Y | Y |
| 2 | ISSUE_MODE | 领料方式 | string(40) | Y |  |
| 3 | ISSUE_RECEIPT_SETS | 领退料套数 | number(16,6) | Y |  |
| 4 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 5 | PLAN_ISSUE_DATE | 预计领料日期 | date | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | SOURCE_MO_ID | 源工单 | GUID | Y |  |
| 8 | MO_ID | 工单 | GUID | Y |  |
| 9 | ISSUE_TYPE | 领料码 | string(40) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 17 | ApproveDate | 修改日期 | date | Y |  |
| 18 | ApproveBy | 修改人 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 38 | ISSUE_DESTINATION_RTK |  | string(400) | Y |  |
| 39 | ISSUE_DESTINATION_ROid |  | GUID | Y |  |
| 40 | ISSUE_RECEIPT_ID |  | GUID | Y |  |

### ISSUE_RECEIPT_REQ

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ISSUE_RECEIPT_REQ_ID | 主键 | GUID | Y | Y |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CLOSE | 结束码 | string(40) | Y |  |
| 9 | TRANSACTION_DATE | 审核日期 | date | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
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
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | PrintCount | 打印次数 | number | Y |  |
| 35 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 36 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 37 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 38 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |
| 47 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE_ID_ROid |  | GUID | Y |  |
| 49 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |

### ISSUE_RECEIPT_REQ_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_RECEIPT_REQ_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 材料品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 材料规格 | string(510) | Y |  |
| 5 | ITEM_TYPE | 材料类型 | string(40) | Y |  |
| 6 | REQUEST_QTY | 申请数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 申请第二数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 13 | ISSUE_RECEIPT_QTY | 已领料量 | number(16,6) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | ITEM_ID | 材料品号 | GUID | Y |  |
| 16 | ITEM_FEATURE_ID | 材料特征码 | GUID | Y |  |
| 17 | UNIT_ID | 单位 | GUID | Y |  |
| 18 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 19 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 20 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 21 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 22 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 23 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 24 | BIN_ID | 库位 | GUID | Y |  |
| 25 | LOT_ID | 批号 | GUID | Y |  |
| 26 | OPERATION_ID | 工艺 | GUID | Y |  |
| 27 | MO_ID | 工单单号 | GUID | Y |  |
| 28 | LOT_MO_ID | 批工单 | GUID | Y |  |
| 29 | INVENTORY_QTY | 领料库存数量 | number(16,6) | Y |  |
| 30 | REPLACED_QTY | 被取替代数量 | number(16,6) | Y |  |
| 31 | MO_D_ID | 工单单身主键 | GUID | Y |  |
| 32 | CLOSE | 结束码 | string(40) | Y |  |
| 33 | ASSIGN_FINISH_PERSON | 指定完工人员 | GUID | Y |  |
| 34 | SOURCE_TYPE | 类型 | string(40) | Y |  |
| 35 | REPLACED_MO_D_ID | 被替代工单备料 | GUID | Y |  |
| 36 | PROJECT_ID | 项目 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 39 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 40 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 41 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 42 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 43 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 44 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 45 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 46 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 47 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 48 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 49 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 50 | UDF041 | 自定义字段12 | date | Y |  |
| 51 | UDF042 | 自定义字段13 | date | Y |  |
| 52 | UDF051 | 自定义字段14 | GUID | Y |  |
| 53 | UDF052 | 自定义字段15 | GUID | Y |  |
| 54 | UDF053 | 自定义字段16 | GUID | Y |  |
| 55 | UDF054 | 自定义字段17 | GUID | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | CreateDate | 创建日期 | date | Y |  |
| 60 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 61 | ModifiedDate | 修改日期 | date | Y |  |
| 62 | CreateBy | 创建者 | GUID | Y |  |
| 63 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 64 | ModifiedBy | 修改者 | GUID | Y |  |
| 65 | ISSUE_DESTINATION_RTK |  | string(400) | Y |  |
| 66 | ISSUE_DESTINATION_ROid |  | GUID | Y |  |
| 67 | ISSUE_RECEIPT_REQ_ID |  | GUID | Y |  |

### ISSUE_RECEIPT_REQ_MO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ISSUE_RECEIPT_REQ_MO_ID | 主键 | GUID | Y | Y |
| 2 | REQUEST_SETS | 申请套数 | number(16,6) | Y |  |
| 3 | ITEM_TYPE | 材料类型 | string(40) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | MO_ID | 工单 | GUID | Y |  |
| 6 | LOT_MO_ID | 批工单 | GUID | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 27 | ApproveDate | 修改日期 | date | Y |  |
| 28 | ApproveBy | 修改人 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | ISSUE_DESTINATION_RTK |  | string(400) | Y |  |
| 36 | ISSUE_DESTINATION_ROid |  | GUID | Y |  |
| 37 | ISSUE_RECEIPT_REQ_ID |  | GUID | Y |  |

### ISSUE_TREE (议题指标树信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ISSUE_TREE_ID | 主键 | GUID | Y | Y |
| 4 | PUBLIC_VERSION | 公版 | number(0/1) | Y |  |
| 5 | ISSUE_NAME | 议题名称 | string(120) | Y |  |
| 6 | LEVEL_CODE | 阶层编码 | string(80) | Y |  |
| 7 | SUPER_ISSUE_TREE_ID | 上级名称 | GUID | Y |  |
| 8 | FOCUS_ABILITY | 重点能力 | number(0/1) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | ABILITY_NAME | 能力名称 | string(120) | Y |  |
| 11 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 12 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 13 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 14 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 15 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 16 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 17 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 18 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 19 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 20 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 21 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 22 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 23 | UDF041 | 自定义字段12 | date | Y |  |
| 24 | UDF042 | 自定义字段13 | date | Y |  |
| 25 | UDF051 | 自定义字段14 | GUID | Y |  |
| 26 | UDF052 | 自定义字段15 | GUID | Y |  |
| 27 | UDF053 | 自定义字段16 | GUID | Y |  |
| 28 | UDF054 | 自定义字段17 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |
| 43 | KPI_CYCLE |  | number | Y |  |
| 44 | ISSUE_GROUP |  | string(200) | Y |  |

### ISSUE_TREE_ATTENTION (ISSUE_TREE_ATTENTION)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_TREE_ATTENTION_ID | 主键 | GUID | Y | Y |
| 3 | DISPLAY_SEQ |  | number | Y |  |
| 4 | USER_ID |  | GUID | Y |  |
| 5 | ISSUE_TREE_D_ID |  | GUID | Y |  |
| 6 | REMARK |  | string(510) | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | PrintCount | 打印次数 | number | Y |  |
| 26 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 27 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 28 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 29 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |

### ISSUE_TREE_AUTHORITY (ISSUE_TREE_AUTHORITY)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ISSUE_TREE_AUTHORITY_ID | 主键 | GUID | Y | Y |
| 4 | TREE_GROUP_NO |  | string(40) | Y |  |
| 5 | TREE_GROUP_NAME |  | string(120) | Y |  |
| 6 | REMARK |  | string(510) | Y |  |
| 7 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 15 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 16 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 17 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 18 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 19 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 20 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 21 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 22 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 23 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 24 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 25 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 26 | UDF041 | 自定义字段12 | date | Y |  |
| 27 | UDF042 | 自定义字段13 | date | Y |  |
| 28 | UDF051 | 自定义字段14 | GUID | Y |  |
| 29 | UDF052 | 自定义字段15 | GUID | Y |  |
| 30 | UDF053 | 自定义字段16 | GUID | Y |  |
| 31 | UDF054 | 自定义字段17 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### ISSUE_TREE_AUTHORITY_D (指标树权限议题明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_TREE_AUTHORITY_D_ID |  | GUID | Y | Y |
| 3 | ISSUE_TREE_ID |  | GUID | Y |  |
| 4 | REMARK |  | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 12 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 13 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 14 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 15 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 16 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 17 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 18 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 19 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 20 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 21 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 22 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 23 | UDF041 | 自定义字段12 | date | Y |  |
| 24 | UDF042 | 自定义字段13 | date | Y |  |
| 25 | UDF051 | 自定义字段14 | GUID | Y |  |
| 26 | UDF052 | 自定义字段15 | GUID | Y |  |
| 27 | UDF053 | 自定义字段16 | GUID | Y |  |
| 28 | UDF054 | 自定义字段17 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | ISSUE_TREE_AUTHORITY_ID |  | GUID | Y |  |

### ISSUE_TREE_AUTHORITY_USER (指标树权限用户明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_TREE_AUTHORITY_USER_ID |  | GUID | Y | Y |
| 3 | OBJECT_TYPE |  | string(40) | Y |  |
| 4 | REMARK |  | string(510) | Y |  |
| 5 | OBJECT_ID |  | GUID | Y |  |
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
| 34 | ISSUE_TREE_AUTHORITY_ID |  | GUID | Y |  |

### ISSUE_TREE_D (议题指标树信息明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ISSUE_TREE_D_ID | 主键 | GUID | Y | Y |
| 2 | TARGET_ID | 公版指标ID | GUID | Y |  |
| 3 | TARGET_NAME | 指标名称 | string(120) | Y |  |
| 4 | TARGET_TYPE | 指标种类 | string(40) | Y |  |
| 5 | ADMIN_UNIT_ID | 归属部门 | GUID | Y |  |
| 6 | TARGET_UNIT | 指标值单位 | string(8) | Y |  |
| 7 | TARGET_FORMAT | 指标值格式 | string(40) | Y |  |
| 8 | USE_COMMA | 使用千分位(,)符号 | number(0/1) | Y |  |
| 9 | TARGET_DECIMAL | 指标值小数位数 | number | Y |  |
| 10 | USE_FORMAT | 自定义格式 | string(40) | Y |  |
| 11 | TARGET_TREND | 指标趋势 | string(40) | Y |  |
| 12 | TARGET_SOURCE | 指标值来源 | string(40) | Y |  |
| 13 | TARGET_SQL | 指标值SQL | string | Y |  |
| 14 | TARGET_DETAIL_SQL | 明细指标SQL | string | Y |  |
| 15 | TARGET_DETAIL_FIELD_NAME | 明细字段名称 | string | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | SOURCE_TYPE | 来源类别 | string(40) | Y |  |
| 18 | RELATE_TASK | 串查作业 | string(80) | Y |  |
| 19 | RELATE_FIELD | 串查字段 | number | Y |  |
| 20 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
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
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | ISSUE_TREE_ID |  | GUID | Y |  |
| 47 | KPI_CYCLE |  | number | Y |  |
| 48 | TARGET_DETAIL_FUNCTION_ID |  | GUID | Y |  |
| 49 | TARGET_DESCRIPTION |  | string(2000) | Y |  |
| 50 | ISSUE_TREE_ROOT_ID |  | GUID | Y |  |

### ISSUE_TREE_INTERRELATED (议题指标树信息相关作业)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_TREE_INTERRELATED_ID | 主键 | GUID | Y | Y |
| 3 | TYPE_KEY_CODE | 视图编号 | string(80) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | ISSUE_TREE_D_ID |  | GUID | Y |  |

### ISSUE_TREE_SD (议题指标树信息子明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ISSUE_TREE_SD_ID | 主键 | GUID | Y | Y |
| 2 | BEGIN_VALUE | 值>= | number(23,6) | Y |  |
| 3 | END_VALUE | 值< | number(23,6) | Y |  |
| 4 | LEVER | 等级 | string(4) | Y |  |
| 5 | COLOR | 颜色 | string(80) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | ISSUE_TREE_D_ID |  | GUID | Y |  |

### ISSUE_TREE_SD2 (指标参数信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ISSUE_TREE_SD2_ID |  | GUID | Y | Y |
| 3 | FUNCTION_INFO_ID |  | GUID | Y |  |
| 4 | FUNCTION_INFO_PARAMETER_ID |  | GUID | Y |  |
| 5 | CONDITIONS |  | string(400) | Y |  |
| 6 | VALUETYPE |  | string(400) | Y |  |
| 7 | VALUE1 |  | string(2000) | Y |  |
| 8 | VALUE2 |  | string(120) | Y |  |
| 9 | REMARK |  | string(510) | Y |  |
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
| 35 | ISSUE_TREE_D_ID |  | GUID | Y |  |

### ISSUE_TREE_VIEWSET (ISSUE_TREE_VIEWSET)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ISSUE_TREE_VIEWSET_ID | 主键 | GUID | Y | Y |
| 2 | USER_ID |  | GUID | Y |  |
| 3 | VIEWTYPE |  | string(400) | Y |  |
| 4 | VIEWTYPE_VALUE |  | string(400) | Y |  |
| 5 | REMARK |  | string(510) | Y |  |
| 6 | Attachments | 附件 | string | Y |  |
| 7 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |