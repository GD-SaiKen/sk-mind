---
module: "EQT"
name_zh: "设备管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 34
columns: 1497
category: asset
tags: ["ERP", "E10", "asset"]
created: 2026-06-25 10:52
---

# EQT (设备管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 34 | Columns: 1497

## Related Modules

- [[ASSET (固定资产)|ASSET (固定资产)]]
- [[EQUIPMENT (设备台账)|EQUIPMENT (设备台账)]]
- [[MAINTAIN (设备维护)|MAINTAIN (设备维护)]]

---

## Tables


- **EQT_ATTCHMENT**
- **EQT_BREAKDOWN (维护设备故障代码及类别)**
- **EQT_CATEGORY (设备类别)**
- **EQT_CHANGE (设备变更)**
- **EQT_CHANGE_D**
- **EQT_CHANGE_JOB**
- **EQT_CHANGE_PARTS**
- **EQT_CHANGE_PARTS_SN**
- **EQT_CHANGE_POOL_FEE**
- **EQT_CHANGE_SUB_EQT**
- **EQT_COMPOSITION**
- **EQT_COMPOSITION_LOG (设备组成台帐)**
- **EQT_COMPOSITION_PARTS**
- **EQT_COMPOSITION_PARTS_SN**
- **EQT_COMPOSITION_SUB_EQT**
- **EQT_DEPOSIT_INSTAL_OBJECT**
- **EQT_DOC**
- **EQT_DRAW**
- **EQT_KNOWLEDGE_BASE (知识库信息)**
- **EQT_LOC_LOG (设备位置台帐)**
- **EQT_MODEL (设备型号信息)**
- **EQT_MODEL_D (设备型号属性信息)**
- **EQT_PERIOD (周期)**
- **EQT_PERIOD_D (周期单身)**
- **EQT_REPAIR_LOG (设备维修台帐)**
- **EQT_RESULT (维护设备处理结果)**
- **EQT_SETTLEMENT_DOC (设备费用结算单)**
- **EQT_SETTLEMENT_DOC_D (设备费用结算单设备明细)**
- **EQT_SETTLEMENT_DOC_SD (设备费用结算单费用明细)**
- **EQT_SETTLEMENT_DOC_SUM (设备费用结算单结算汇总)**
- **EQT_STATUS (设备状态信息)**
- **EQT_TASK**
- **EQT_TRANSFER_DOC (设备收发单)**
- **EQT_TRANSFER_DOC_D (设备收发单设备明细)**


---


---


> Tables: 34

### EQT_ATTCHMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_ATTCHMENT_ID | 主键 | GUID | Y | Y |
| 3 | FILE | 文件档名 | string(40) | Y |  |
| 4 | DESCRIPTION | 文件说明 | string(510) | Y |  |
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
| 33 | EQT_CHANGE_ID |  | GUID | Y |  |

### EQT_BREAKDOWN (维护设备故障代码及类别)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_BREAKDOWN_ID | 主键 | GUID | Y | Y |
| 4 | EQT_BREAKDOWN_CODE | 故障编号 | string(80) | Y |  |
| 5 | EQT_BREAKDOWN_NAME | 故障名称 | string(160) | Y |  |
| 6 | BREAKDOWN_TYPE | 性质 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | PARENT_BREAKDOWN_ID | 上级故障 | GUID | Y |  |
| 9 | EQT_KNOWLEDGE_BASE_ID | 知识库分类 | GUID | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_CATEGORY (设备类别)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | EQT_CATEGORY_CODE | 设备类别编号 | string(80) | Y |  |
| 5 | EQT_CATEGORY_NAME | 设备类别名称 | string(160) | Y |  |
| 6 | PARENT_EQT_CATEGORY_ID | 母类别 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_CHANGE (设备变更)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | EQT_CHANGE_ID | 主键 | GUID | Y | Y |
| 7 | REASON_DESC | 变更說明 | string(510) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 10 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 11 | CHANGE_DATE | 审核日期 | date | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
| 19 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | PrintCount | 打印次数 | number | Y |  |
| 40 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 41 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 42 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 43 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_CHANGE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_CHANGE_D_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | REVIEW_PASS | 审查通过 | number(0/1) | Y |  |
| 6 | REVIEW_DATE | 审查日期 | date | Y |  |
| 7 | REVIEW_OPINIONS | 审查意见 | string(510) | Y |  |
| 8 | REVIEW_EMPLOYEE_ID | 审查人员 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | EQT_CHANGE_ID |  | GUID | Y |  |

### EQT_CHANGE_JOB

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_CHANGE_JOB_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 变更项目 | GUID | Y |  |
| 4 | IS_SUPPLIER | 委外 | number(0/1) | Y |  |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_NAME | 品名 | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 9 | CURRENCY_ID | 币种 | GUID | Y |  |
| 10 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 11 | PRICE | 单价 | number(23,8) | Y |  |
| 12 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 13 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 14 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 15 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 16 | TAX_ID | 税种 | GUID | Y |  |
| 17 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 18 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 19 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 20 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 21 | SETTLEMENT_STATUS | 结算状态 | string(40) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 24 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 25 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 26 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 27 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 28 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 29 | POOL_FEE | 公摊费用 | number(0/1) | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | EQT_CHANGE_D_ID |  | GUID | Y |  |

### EQT_CHANGE_PARTS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_CHANGE_PARTS_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | QTY | 业务数量 | number(16,6) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | TYPE | 变更类型 | string(40) | Y |  |
| 10 | ORG_QTY | 原数量 | number(16,6) | Y |  |
| 11 | FACT_ISSUE_RECEIPT_QTY | 已领/退数量 | number(16,6) | Y |  |
| 12 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 13 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 14 | STOCK_QTY | 库存数量 | number(16,6) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | EQT_CHANGE_D_ID |  | GUID | Y |  |

### EQT_CHANGE_PARTS_SN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_CHANGE_PARTS_SN_ID | 主键 | GUID | Y | Y |
| 3 | SN_NO | 序列号 | string(510) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | TYPE | 变更类型 | string(40) | Y |  |
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
| 34 | EQT_CHANGE_PARTS_ID |  | GUID | Y |  |

### EQT_CHANGE_POOL_FEE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_CHANGE_POOL_FEE_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 变更项目 | GUID | Y |  |
| 4 | IS_SUPPLIER | 委外 | number(0/1) | Y |  |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_NAME | 品名 | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 9 | CURRENCY_ID | 币种 | GUID | Y |  |
| 10 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 11 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 12 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 13 | TAX_ID | 税种 | GUID | Y |  |
| 14 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 15 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 16 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 17 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 18 | SETTLEMENT_STATUS | 结算状态 | string(40) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 21 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 22 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 23 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 24 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 25 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 26 | PRICE | 单价 | number(23,8) | Y |  |
| 27 | PRICE_QTY |  | number(16,6) | Y |  |
| 28 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | EQT_CHANGE_ID |  | GUID | Y |  |

### EQT_CHANGE_SUB_EQT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_CHANGE_SUB_EQT_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 子设备 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | TYPE | 变更类型 | string(40) | Y |  |
| 6 | EQT_MODEL_ID | 设备型号 | GUID | Y |  |
| 7 | EQT_CATEGORY_ID | 设备类别 | GUID | Y |  |
| 8 | ISSUED | 已领/退 | number(0/1) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | EQT_CHANGE_D_ID |  | GUID | Y |  |

### EQT_COMPOSITION

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_COMPOSITION_ID | 主键 | GUID | Y | Y |
| 4 | EQUIPMENT_ID | 主设备 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 31 | Attachments | 附件 | string | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_COMPOSITION_LOG (设备组成台帐)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_COMPOSITION_LOG_ID | 主键 | GUID | Y | Y |
| 4 | TYPE | 类型 | string(40) | Y |  |
| 5 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | QTY | 数量 | number(16,6) | Y |  |
| 8 | SN_NO | 序列号 | string(510) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | SUB_SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SUB_SOURCE_ID_ROid |  | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |

### EQT_COMPOSITION_PARTS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_COMPOSITION_PARTS_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | QTY | 库存单位数量 | number(16,6) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | EQT_COMPOSITION_ID |  | GUID | Y |  |

### EQT_COMPOSITION_PARTS_SN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_COMPOSITION_PARTS_SN_ID | 主键 | GUID | Y | Y |
| 3 | SN_NO | 序列号 | string(510) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | EQT_COMPOSITION_PARTS_ID |  | GUID | Y |  |

### EQT_COMPOSITION_SUB_EQT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_COMPOSITION_SUB_EQT_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 子设备 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | EQT_COMPOSITION_ID |  | GUID | Y |  |

### EQT_DEPOSIT_INSTAL_OBJECT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | EQT_DEPOSIT_INSTAL_OBJECT_ID | 主键 | GUID | Y | Y |
| 7 | BUSINESS_DATE | 业务日期 | date | Y |  |
| 8 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 9 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 10 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 11 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 12 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 13 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 14 | CURRENCY_ID | 货币 | GUID | Y |  |
| 15 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 16 | TAX_ID | 税种 | GUID | Y |  |
| 17 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 18 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 19 | PROJECT_ID | 项目 | GUID | Y |  |
| 20 | REMARK | 单头备注 | string(510) | Y |  |
| 21 | REMARK1 | 单身备注 | string(510) | Y |  |
| 22 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 23 | INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 24 | INSTALLMENT_NO | 分期期号 | number | Y |  |
| 25 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 26 | INSTALLMENT_NAME | 分期名称 | string(60) | Y |  |
| 27 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 28 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 29 | PREPAYMENT_AMT_OC | 原币预付金额 | number(23,8) | Y |  |
| 30 | SETTLEMENT_AMT_OC | 原币已结算金额 | number(23,8) | Y |  |
| 31 | VERIFICATION_AMT_OC | 原币已核销金额 | number(23,8) | Y |  |
| 32 | BALANCE_AMT_OC | 原币未付余额 | number(23,8) | Y |  |
| 33 | INSTALLMENT_DATE | 执行日 | date | Y |  |
| 34 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 35 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 36 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 37 | PAYMENT_TERM_REMARK | 付款条件说明 | string(510) | Y |  |
| 38 | PAYMENT_DATE | 付款日 | date | Y |  |
| 39 | CASHING_DATE | 兑现日 | date | Y |  |
| 40 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 41 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 42 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 43 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 44 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 45 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 46 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 47 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 48 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 49 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算原币未税金额 | number(23,8) | Y |  |
| 50 | PRE_SETTLEMENT_TAX_OC | 预结算原币税额 | number(23,8) | Y |  |
| 51 | OFFSETED_AMT_UN_TAX_OC | 已冲减原币未税金额 | number(23,8) | Y |  |
| 52 | OFFSETED_TAX_OC | 已冲减原币税额 | number(23,8) | Y |  |
| 53 | CreateDate | 创建日期 | date | Y |  |
| 54 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 55 | ModifiedDate | 修改日期 | date | Y |  |
| 56 | CreateBy | 创建者 | GUID | Y |  |
| 57 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 58 | ModifiedBy | 修改者 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 61 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 62 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 63 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 64 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 65 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 66 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 67 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 68 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 69 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 70 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 71 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 72 | UDF041 | 自定义字段12 | date | Y |  |
| 73 | UDF042 | 自定义字段13 | date | Y |  |
| 74 | UDF051 | 自定义字段14 | GUID | Y |  |
| 75 | UDF052 | 自定义字段15 | GUID | Y |  |
| 76 | UDF053 | 自定义字段16 | GUID | Y |  |
| 77 | UDF054 | 自定义字段17 | GUID | Y |  |
| 78 | Attachments | 附件 | string | Y |  |
| 79 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 80 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 81 | ApproveDate | 修改日期 | date | Y |  |
| 82 | ApproveBy | 修改人 | GUID | Y |  |
| 83 | Owner_Org_RTK |  | string(400) | Y |  |
| 84 | Owner_Org_ROid |  | GUID | Y |  |
| 85 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 86 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 87 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 88 | SOURCE_ID_ROid |  | GUID | Y |  |

### EQT_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_DOC_ID | 主键 | GUID | Y | Y |
| 3 | DESCRIPTION | 文件说明 | string(510) | Y |  |
| 4 | NEW_FILE | 文件档名 | string(40) | Y |  |
| 5 | NEW_VERSION | 新版本 | string(20) | Y |  |
| 6 | OLD_FILE | 原文件档名 | string(40) | Y |  |
| 7 | OLD_VERSION | 原版本 | string(20) | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | EQT_CHANGE_ID |  | GUID | Y |  |

### EQT_DRAW

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_DRAW_ID | 主键 | GUID | Y | Y |
| 3 | DESCRIPTION | 图纸说明 | string(510) | Y |  |
| 4 | NEW_FILE | 新图纸档名 | string(40) | Y |  |
| 5 | NEW_VERSION | 新版本 | string(20) | Y |  |
| 6 | OLD_FILE | 原图纸档名 | string(40) | Y |  |
| 7 | OLD_VERSION | 原版本 | string(20) | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | EQT_CHANGE_ID |  | GUID | Y |  |

### EQT_KNOWLEDGE_BASE (知识库信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_KNOWLEDGE_BASE_ID | 主键 | GUID | Y | Y |
| 4 | EQT_KNOWLEDGE_BASE_CODE | 知识库编号 | string(60) | Y |  |
| 5 | EQT_KNOWLEDGE_BASE_NAME | 知识库名称 | string(120) | Y |  |
| 6 | TYPE | 性质 | string(40) | Y |  |
| 7 | EQT_CATEGORY_ID | 设备类别 | GUID | Y |  |
| 8 | EQT_MODEL_ID | 设备型号 | GUID | Y |  |
| 9 | EQUIPMENT_ID | 设备编号 | GUID | Y |  |
| 10 | KEYWORDS | 关键字 | string(600) | Y |  |
| 11 | DESCRIPTION | 描述 | string(510) | Y |  |
| 12 | FILENAME | 文件名称 | string(510) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | PARENT_EQT_LEVEL_ID | 上阶知识库 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |
| 47 | SOURCE_DOC_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE_DOC_ID_ROid |  | GUID | Y |  |

### EQT_LOC_LOG (设备位置台帐)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_LOC_LOG_ID | 主键 | GUID | Y | Y |
| 4 | TYPE | 类型 | string(40) | Y |  |
| 5 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | Attachments | 附件 | string | Y |  |
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |
| 39 | SOURCE_LOC_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE_LOC_ID_ROid |  | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |

### EQT_MODEL (设备型号信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_MODEL_ID | 主键 | GUID | Y | Y |
| 4 | EQT_MODEL_CODE | 设备型号编号 | string(80) | Y |  |
| 5 | EQT_MODEL_NAME | 设备型号名称 | string(160) | Y |  |
| 6 | EQT_CATEGORY_ID | 设备类别 | GUID | Y |  |
| 7 | SPECIFICATION | 规格 | string(120) | Y |  |
| 8 | ABC_CATEGORY | ABC类别 | string(2) | Y |  |
| 9 | MANUFACTURER | 制造商 | string(160) | Y |  |
| 10 | USEFUL_LIFE | 使用年限 | number(11,1) | Y |  |
| 11 | STANDARD_OPERATING_QTY | 每日标准运行量 | number(16,6) | Y |  |
| 12 | OPERATING_QTY_UNIT_ID | 运行量单位 | GUID | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_MODEL_D (设备型号属性信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FEATURE_NAME | 属性名称 | string(80) | Y |  |
| 3 | FEATURE_VALUE | 默认属性值 | string(40) | Y |  |
| 4 | UNIT_ID | 单位 | GUID | Y |  |
| 5 | PRINT_EQT_CARD | 列印到设备卡 | number(0/1) | Y |  |
| 6 | MUST_INPUT | 必须输入 | number(0/1) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | EQT_MODEL_D_ID | 主键 | GUID | Y | Y |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | EQT_MODEL_ID |  | GUID | Y |  |

### EQT_PERIOD (周期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_PERIOD_ID | 主键 | GUID | Y | Y |
| 4 | EQT_PERIOD_CODE | 周期编号 | string(80) | Y |  |
| 5 | EQT_PERIOD_NAME | 周期名称 | string(160) | Y |  |
| 6 | PERIOD_TYPE | 类型 | string(40) | Y |  |
| 7 | PERIOD_QTY | 周期量 | number(16,6) | Y |  |
| 8 | PERIOD_UNIT | 周期单位 | string(40) | Y |  |
| 9 | PERIOD_DATE | 指定周期日 | string(40) | Y |  |
| 10 | CHANGE_TYPE | 变动周期类型 | string(40) | Y |  |
| 11 | OPERATING_QTY_UNIT_ID | 运行量单位 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 38 | Attachments | 附件 | string | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_PERIOD_D (周期单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | TIMES | 次数 | string(8) | Y |  |
| 2 | PERIOD_QTY | 周期量 | number(16,6) | Y |  |
| 3 | PERIOD_UNIT | 时间单位 | string(40) | Y |  |
| 4 | OPERATING_QTY_UNIT_ID | 运行量单位 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | EQT_PERIOD_D_ID | 主键 | GUID | Y | Y |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | EQT_PERIOD_ID |  | GUID | Y |  |

### EQT_REPAIR_LOG (设备维修台帐)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_REPAIR_LOG_ID | 主键 | GUID | Y | Y |
| 4 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 5 | EQT_BREAKDOWN_ID | 故障编号 | GUID | Y |  |
| 6 | BREAKDOWN_DESCRIPTION | 故障详细描述 | string(510) | Y |  |
| 7 | REPAIR_SITUATION | 维修情况说明 | string(510) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | SOURCE_LOC_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE_LOC_ID_ROid |  | GUID | Y |  |

### EQT_RESULT (维护设备处理结果)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_RESULT_ID | 主键 | GUID | Y | Y |
| 4 | EQT_RESULT_CODE | 处理结果编号 | string(80) | Y |  |
| 5 | EQT_RESULT_NAME | 处理结果名称 | string(160) | Y |  |
| 6 | EQT_STATUS_ID | 默认设备状态 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_SETTLEMENT_DOC (设备费用结算单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | EQT_SETTLEMENT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 8 | SUPPLIER_CONTACT_NAME | 供应商联系人名称 | string(72) | Y |  |
| 9 | SUPPLIER_CONTACT_ID | 供应商联系人 | GUID | Y |  |
| 10 | SUPPLIER_ADDR_NAME | 供应商地址名称 | string(510) | Y |  |
| 11 | SUPPLIER_ADDR_ID | 供应商地址 | GUID | Y |  |
| 12 | CURRENCY_ID | 币种 | GUID | Y |  |
| 13 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 14 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 15 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 16 | SUPPLIER_FULL_NAME | 结算供应商全称 | string(144) | Y |  |
| 17 | INVOICE_CONTACT_NAME | 结算供应商联系人名称 | string(72) | Y |  |
| 18 | INVOICE_CONTACT_ID | 结算供应商联系人 | GUID | Y |  |
| 19 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 20 | INVOICE_ADDR_ID | 结算供应商地址 | GUID | Y |  |
| 21 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 22 | INVOICE_DATE | 结算日期 | date | Y |  |
| 23 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 24 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 25 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 26 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 27 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 28 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 29 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 30 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 31 | DIRECT_INVOICING_INDICATOR | 随货附票 | number(0/1) | Y |  |
| 32 | GLOB_ESTI_JE_INDICATOR | 已生成运营账簿暂估分录 | number(0/1) | Y |  |
| 33 | GLOB_ESTI_JE_ID | 运营账簿暂估分录 | GUID | Y |  |
| 34 | GLOB_COST_JE_INDICATOR | 已生成运营账簿成本分录 | number(0/1) | Y |  |
| 35 | GLOB_COST_JE_ID | 运营账簿成本分录 | GUID | Y |  |
| 36 | GLMB_ESTI_JE_INDICATOR | 已生成管理账簿暂估分录 | number(0/1) | Y |  |
| 37 | GLMB_ESTI_JE_ID | 管理账簿暂估分录 | GUID | Y |  |
| 38 | GLMB_COST_JE_INDICATOR | 已生成管理账簿成本分录 | number(0/1) | Y |  |
| 39 | GLMB_COST_JE_ID | 管理账簿成本分录 | GUID | Y |  |
| 40 | REMARK | 备注 | string(510) | Y |  |
| 41 | PLANT_ID | 工厂 | GUID | Y |  |
| 42 | TAX_ID | 税种 | GUID | Y |  |
| 43 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 44 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 45 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 46 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 47 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | Attachments | 附件 | string | Y |  |
| 55 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 56 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 57 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 58 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 59 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 60 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 61 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 62 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 63 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 64 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 65 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 66 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 67 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 68 | UDF041 | 自定义字段12 | date | Y |  |
| 69 | UDF042 | 自定义字段13 | date | Y |  |
| 70 | UDF051 | 自定义字段14 | GUID | Y |  |
| 71 | UDF052 | 自定义字段15 | GUID | Y |  |
| 72 | UDF053 | 自定义字段16 | GUID | Y |  |
| 73 | UDF054 | 自定义字段17 | GUID | Y |  |
| 74 | Version | 版本号，不要随意更改 | binary | Y |  |
| 75 | PrintCount | 打印次数 | number | Y |  |
| 76 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 77 | ApproveDate | 修改日期 | date | Y |  |
| 78 | ApproveBy | 修改人 | GUID | Y |  |
| 79 | Owner_Org_RTK |  | string(400) | Y |  |
| 80 | Owner_Org_ROid |  | GUID | Y |  |
| 81 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 82 | SOURCE_ID_ROid |  | GUID | Y |  |

### EQT_SETTLEMENT_DOC_D (设备费用结算单设备明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_SETTLEMENT_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
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
| 33 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 34 | SOURCE_ID_ROid |  | GUID | Y |  |
| 35 | EQT_SETTLEMENT_DOC_ID |  | GUID | Y |  |

### EQT_SETTLEMENT_DOC_SD (设备费用结算单费用明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_SETTLEMENT_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 项目 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_NAME | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | TAX_ID | 税种 | GUID | Y |  |
| 8 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 9 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 10 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 11 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 12 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 13 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 14 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | PRICE | 单价 | number(23,8) | Y |  |
| 17 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 18 | PRICE_UNIT_ID | 主键 | GUID | Y |  |
| 19 | POOL_FEE | 公摊 | number(0/1) | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | EQT_SETTLEMENT_DOC_D_ID |  | GUID | Y |  |

### EQT_SETTLEMENT_DOC_SUM (设备费用结算单结算汇总)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_SETTLEMENT_DOC_SUM_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_NAME | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | TAX_ID | 税种 | GUID | Y |  |
| 8 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 9 | BENEFIT_DEPT | 受益部门 | GUID | Y |  |
| 10 | BENEFIT_EMP | 受益人员 | GUID | Y |  |
| 11 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 12 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 13 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 14 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 15 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | AMOUNT_UN_TAX_BC | 本币费用金额 | number(23,8) | Y |  |
| 20 | ESTIMATION_ITEMS | 暂估次数 | number | Y |  |
| 21 | ESTI_REVERSE_MODE | 暂估回冲方式 | number | Y |  |
| 22 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 23 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 24 | SETTLEMENT_AMT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 25 | SETTLEMENT_AMT_UN_TAX_BC | 已结算本币未税金额 | number(23,8) | Y |  |
| 26 | SETTLEMENT_AMT_TAX_BC | 已结算本币税额 | number(23,8) | Y |  |
| 27 | REMARK | 备注 | string(510) | Y |  |
| 28 | DOC_NO | 源单单号 | string(80) | Y |  |
| 29 | BUSINESS_DATE | 源单业务日期 | date | Y |  |
| 30 | DOC_ID | 源单单据类型 | GUID | Y |  |
| 31 | AMOUNT_UN_TAX_OC | 原币费用金额 | number(23,8) | Y |  |
| 32 | SETTLEMENT_AMT_OC | 已结算原币费用金额 | number(23,8) | Y |  |
| 33 | SETTLEMENT_AMT_BC | 已结算本币费用金额 | number(23,8) | Y |  |
| 34 | PLAN_SETTLEMENT_DATE | 预计结算日 | date | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 61 | ApproveDate | 修改日期 | date | Y |  |
| 62 | ApproveBy | 修改人 | GUID | Y |  |
| 63 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 64 | SOURCE_ID_ROid |  | GUID | Y |  |
| 65 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 67 | EQT_SETTLEMENT_DOC_ID |  | GUID | Y |  |

### EQT_STATUS (设备状态信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQT_STATUS_ID | 主键 | GUID | Y | Y |
| 4 | EQT_STATUS_CODE | 处理状态编号 | string(80) | Y |  |
| 5 | EQT_STATUS_NAME | 处理状态名称 | string(160) | Y |  |
| 6 | USEFUL | 允许使用 | number(0/1) | Y |  |
| 7 | AUTO_DOC | 允许自动生成维护单 | number(0/1) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### EQT_TASK

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_TASK_ID | 主键 | GUID | Y | Y |
| 3 | DEPARTMENT_ID | 部门 | GUID | Y |  |
| 4 | PERSON_ID | 主办人 | GUID | Y |  |
| 5 | TASK_ID | 工作 | GUID | Y |  |
| 6 | DESCRIPTION | 工作说明 | string(510) | Y |  |
| 7 | START_DATE | 开始日期 | date | Y |  |
| 8 | PLAN_DATE | 预计完成日 | date | Y |  |
| 9 | ACTUAL_DATE | 实际完成日 | date | Y |  |
| 10 | ACTION | 执行结果 | string(510) | Y |  |
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
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | EQT_CHANGE_ID |  | GUID | Y |  |

### EQT_TRANSFER_DOC (设备收发单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | EQT_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSFER_COMPLETE | 交接完成 | number(0/1) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | PrintCount | 打印次数 | number | Y |  |
| 10 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 11 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 12 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 13 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | RECEIVE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | RECEIVE_SOURCE_ID_ROid |  | GUID | Y |  |

### EQT_TRANSFER_DOC_D (设备收发单设备明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQT_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 4 | EQT_MODEL_ID | 设备型号 | GUID | Y |  |
| 5 | EQT_CATEGORY_ID | 设备类别 | GUID | Y |  |
| 6 | TRANSFER_STATUS | 收发状态 | string(40) | Y |  |
| 7 | RECEIVE_DEPT | 接收部门 | GUID | Y |  |
| 8 | RECEIVE_EMP | 接收人员 | GUID | Y |  |
| 9 | TRANSFER_DATE | 接收日期 | date | Y |  |
| 10 | EQT_STATUS_ID | 设备状态 | GUID | Y |  |
| 11 | EQT_EMP | 保管人 | GUID | Y |  |
| 12 | EQT_DEPT | 保管部门 | GUID | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |
| 44 | RECEIVE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | RECEIVE_SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | EQT_TRANSFER_DOC_ID |  | GUID | Y |  |