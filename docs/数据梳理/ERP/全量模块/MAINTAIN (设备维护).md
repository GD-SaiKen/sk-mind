---
module: "MAINTAIN"
name_zh: "设备维护"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 395
category: asset
tags: ["ERP", "E10", "asset"]
created: 2026-06-25 10:52
---

# MAINTAIN (设备维护)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 8 | Columns: 395

## Related Modules

- [[ASSET (固定资产)|ASSET (固定资产)]]
- [[EQT (设备管理)|EQT (设备管理)]]
- [[EQUIPMENT (设备台账)|EQUIPMENT (设备台账)]]

---

## Tables


- **MAINTAIN_DOC (设备维护单)**
- **MAINTAIN_DOC_D (维护单明细)**
- **MAINTAIN_DOC_MAT (料件需求明细)**
- **MAINTAIN_DOC_PARTS (零部件需求明细)**
- **MAINTAIN_DOC_PARTS_SN (零部件序列号明细)**
- **MAINTAIN_DOC_POOL_FEE (维护单公摊费用)**
- **MAINTAIN_DOC_SD (维护单项目明细)**
- **MAINTAIN_DOC_SUB_EQT (子设备需求明细)**


---


---


> Tables: 8

### MAINTAIN_DOC (设备维护单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MAINTAIN_DOC_ID | 主键 | GUID | Y | Y |
| 7 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | MAINTAIN_DATE | 审核日期 | date | Y |  |
| 10 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 11 | INVOICE_COMPANY_ID | 主键 | GUID | Y |  |
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
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |

### MAINTAIN_DOC_D (维护单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MAINTAIN_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 4 | PLAN_NAME | 维护方案名称 | string(160) | Y |  |
| 5 | PLAN_LEVEL | 维护级别 | string(4) | Y |  |
| 6 | JOB_EXE_DATE | 计划执行时间 | date | Y |  |
| 7 | JOB_FINISH_DATE | 计划完成时间 | date | Y |  |
| 8 | FACT_EXE_DATE | 实际执行时间 | date | Y |  |
| 9 | FACT_FINISH_DATE | 实际完成时间 | date | Y |  |
| 10 | REF_WORKHOURS | 参考作业时数 | number | Y |  |
| 11 | FACT_WORKHOURS | 实际作业时数 | number | Y |  |
| 12 | SHUTDOWN | 停机 | number(0/1) | Y |  |
| 13 | PRO_SHUTDOWN_HOURS | 计划停机时数 | number | Y |  |
| 14 | FACT_SHUTDOWN_HOURS | 实际停机时数 | number | Y |  |
| 15 | COMPLETION_STATUS | 完成状况 | string(40) | Y |  |
| 16 | EQT_RESULT_ID | 设备维护结果 | GUID | Y |  |
| 17 | MAINTAINING_STATUS_ID | 维护时设备状态 | GUID | Y |  |
| 18 | EQT_STATUS_ID | 完成后设备状态 | GUID | Y |  |
| 19 | EQT_PERIOD_ID | 周期编号 | GUID | Y |  |
| 20 | TIMES | 周期次数 | string(8) | Y |  |
| 21 | NEXT_DATE | 下次计划维护时间 | date | Y |  |
| 22 | PREPAY_RATE | 预付比率 | number(5,4) | Y |  |
| 23 | PREPAY_AMT | 预付金额 | number(23,8) | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
| 25 | ORIGINAL_STATUS_ID | 原设备状态 | GUID | Y |  |
| 26 | ORIGINAL_EXE_DATETIME | 原执行时间 | date | Y |  |
| 27 | ORIGINAL_EQT_PERIOD_ID | 原周期编号 | GUID | Y |  |
| 28 | ORIGINAL_CYCLE_QTY | 原周期次数 | string(8) | Y |  |
| 29 | ORIGINAL_NEXT_DATE | 原下次计划维护时间 | date | Y |  |
| 30 | ORG_TOT_QTY | 原本次累计运行量 | number(16,6) | Y |  |
| 31 | ORG_NEXT_QTY | 原下次计划维护运行量 | number(16,6) | Y |  |
| 32 | NEXT_QTY | 下次计划维护运行量 | number(16,6) | Y |  |
| 33 | REVIEW_PASS | 审查通过 | number(0/1) | Y |  |
| 34 | REVIEW_OPINIONS | 审查意见 | string(510) | Y |  |
| 35 | REVIEW_EMPLOYEE_ID | 审查人员 | GUID | Y |  |
| 36 | REVIEW_DATE | 审查日期 | date | Y |  |
| 37 | PLAN_ID | 维护方案 | GUID | Y |  |
| 38 | IS_PREPAY | 生成预付款 | number(0/1) | Y |  |
| 39 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 40 | CURRENCY_ID | 币种 | GUID | Y |  |
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
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |
| 69 | MAINTAIN_DOC_ID |  | GUID | Y |  |

### MAINTAIN_DOC_MAT (料件需求明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MAINTAIN_DOC_MAT_ID | 主键 | GUID | Y | Y |
| 3 | DEMANDTYPE | 需求料件类型 | string(40) | Y |  |
| 4 | INSTRUCTION | 料件需求说明 | string(510) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_NAME | 品名 | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | UNIT_ID | 业务单位 | GUID | Y |  |
| 9 | SUGGEST_QTY | 建议业务数量 | number(16,6) | Y |  |
| 10 | FACT_ISSUE_RECEIPT_QTY | 实际领料业务数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 13 | STOCK_QTY | 库存数量 | number(16,6) | Y |  |
| 14 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
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
| 43 | MAINTAIN_DOC_D_ID |  | GUID | Y |  |

### MAINTAIN_DOC_PARTS (零部件需求明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MAINTAIN_DOC_PARTS_ID | 主键 | GUID | Y | Y |
| 3 | TYPE | 维修类型 | string(40) | Y |  |
| 4 | INSTRUCTION | 需求说明 | string(510) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_NAME | 品名 | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | QTY | 业务数量 | number(16,6) | Y |  |
| 10 | FACT_ISSUE_RECEIPT_QTY | 已领/退数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 13 | STOCK_QTY | 库存数量 | number(16,6) | Y |  |
| 14 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
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
| 43 | MAINTAIN_DOC_D_ID |  | GUID | Y |  |

### MAINTAIN_DOC_PARTS_SN (零部件序列号明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MAINTAIN_DOC_PARTS_SN_ID | 主键 | GUID | Y | Y |
| 3 | SN_NO | 序列号 | string(510) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | TYPE | 维修类型 | string(40) | Y |  |
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
| 34 | MAINTAIN_DOC_PARTS_ID |  | GUID | Y |  |

### MAINTAIN_DOC_POOL_FEE (维护单公摊费用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MAINTAIN_DOC_POOL_FEE_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 维护项目 | GUID | Y |  |
| 4 | IS_SUPPLIER | 委外 | number(0/1) | Y |  |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | ITEM_NAME | 品名 | string(120) | Y |  |
| 9 | CURRENCY_ID | 币种 | GUID | Y |  |
| 10 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 11 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 12 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 13 | TAX_ID | 税种 | GUID | Y |  |
| 14 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 15 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 16 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 17 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 18 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | PRICE | 单价 | number(23,8) | Y |  |
| 21 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 22 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 23 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 24 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 25 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 26 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 27 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 35 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 36 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 37 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 38 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 39 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 40 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 41 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 42 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 43 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 44 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 45 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 46 | UDF041 | 自定义字段12 | date | Y |  |
| 47 | UDF042 | 自定义字段13 | date | Y |  |
| 48 | UDF051 | 自定义字段14 | GUID | Y |  |
| 49 | UDF052 | 自定义字段15 | GUID | Y |  |
| 50 | UDF053 | 自定义字段16 | GUID | Y |  |
| 51 | UDF054 | 自定义字段17 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | MAINTAIN_DOC_ID |  | GUID | Y |  |

### MAINTAIN_DOC_SD (维护单项目明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MAINTAIN_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 维护项目 | GUID | Y |  |
| 4 | CONTENT | 维护内容 | string(160) | Y |  |
| 5 | JOB_RESULT | 项目维护结果 | string(510) | Y |  |
| 6 | EXPLANATION | 维护情况说明 | string(510) | Y |  |
| 7 | ADD_KNOWLEDGE_BASE | 加入知识库 | number(0/1) | Y |  |
| 8 | IS_SUPPLIER | 委外 | number(0/1) | Y |  |
| 9 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_NAME | 品名 | string(120) | Y |  |
| 12 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 13 | CURRENCY_ID | 币种 | GUID | Y |  |
| 14 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 15 | PRICE | 单价 | number(23,8) | Y |  |
| 16 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 17 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 18 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 19 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 20 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 21 | TAX_ID | 税种 | GUID | Y |  |
| 22 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 23 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 24 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 25 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | SETTLEMENT_STATUS | 结算状态 | string(40) | Y |  |
| 28 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 29 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 30 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 31 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 32 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 33 | POOL_FEE | 公摊费用 | number(0/1) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | MAINTAIN_DOC_D_ID |  | GUID | Y |  |

### MAINTAIN_DOC_SUB_EQT (子设备需求明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TYPE | 维修类型 | string(40) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | MAINTAIN_DOC_SUB_EQT_ID | 主键 | GUID | Y | Y |
| 5 | EQUIPMENT_ID | 设备编号 | GUID | Y |  |
| 6 | EQT_MODEL_ID | 设备型号 | GUID | Y |  |
| 7 | EQT_CATEGORY_ID | 设备类别 | GUID | Y |  |
| 8 | INSTRUCTION | 需求说明 | string(510) | Y |  |
| 9 | ISSUED | 已领/退 | number(0/1) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | MAINTAIN_DOC_D_ID |  | GUID | Y |  |