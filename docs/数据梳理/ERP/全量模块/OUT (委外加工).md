---
module: "OUT"
name_zh: "委外加工"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 7
columns: 369
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# OUT (委外加工)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 7 | Columns: 369

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[BOM (物料清单)|BOM (物料清单)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **OUT_EXPENSE_DOC**
- **OUT_EXPENSE_DOC_D**
- **OUT_REPAIR_DOC (委外维修单)**
- **OUT_REPAIR_DOC_D (委外维修明细)**
- **OUT_REPAIR_DOC_JOB (委外维修项目明细)**
- **OUT_REPAIR_DOC_POOL_FEE (委外维修单公摊费用)**
- **OUT_REPAIR_DOC_SD (委外维修故障明细)**


---


---


> Tables: 7

### OUT_EXPENSE_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | OUT_EXPENSE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 8 | SETTLEMENT_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 9 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 10 | CURRENCY_ID | 币种 | GUID | Y |  |
| 11 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 14 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | SERVICE_SITE_ID | 站点 | GUID | Y |  |
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

### OUT_EXPENSE_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OUT_EXPENSE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SETTLEMENT_TYPE | 类别 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | SN | 序列号 | string(510) | Y |  |
| 9 | QUANTITY |  | number(16,6) | Y |  |
| 10 | UNIT_ID | 单位 | GUID | Y |  |
| 11 | PRICE |  | number(23,8) | Y |  |
| 12 | AMOUNT |  | number(23,8) | Y |  |
| 13 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 14 | TAX_RATE |  | number(5,4) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | TAX_ID | 税种 | GUID | Y |  |
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
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |
| 51 | OUT_EXPENSE_DOC_ID |  | GUID | Y |  |

### OUT_REPAIR_DOC (委外维修单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | OUT_REPAIR_DOC_ID | 主键 | GUID | Y | Y |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | APPLY_DATE | 申请日期 | date | Y |  |
| 9 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 10 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 11 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 12 | REPAIR_DATE | 审核日期 | date | Y |  |
| 13 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
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
| 41 | PrintCount | 打印次数 | number | Y |  |
| 42 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 43 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 44 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 45 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |

### OUT_REPAIR_DOC_D (委外维修明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OUT_REPAIR_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | EQUIPMENT_ID | 设备 | GUID | Y |  |
| 4 | EQT_STATUS_ID | 设备状态 | GUID | Y |  |
| 5 | ERGENCY | 紧急 | number(0/1) | Y |  |
| 6 | REPAIR_REASON | 维修原因 | string(3000) | Y |  |
| 7 | REQUEST_DATE | 需求日期 | date | Y |  |
| 8 | PLAN_DATE | 预计完成日期 | date | Y |  |
| 9 | REPAIR_STATUS | 维修状态 | string(40) | Y |  |
| 10 | EQT_RESULT_ID | 维修结果 | GUID | Y |  |
| 11 | COMPLETE_STATUS_ID | 完成后设备状态 | GUID | Y |  |
| 12 | ACTUAL_DATE | 实际完成日期 | date | Y |  |
| 13 | EXPECTED_FEE | 维修供应商预计金额 | number(23,8) | Y |  |
| 14 | PREPAY_RATE | 预付比率 | number(5,4) | Y |  |
| 15 | PREPAY_AMT | 预付金额 | number(23,8) | Y |  |
| 16 | CURRENCY_ID | 币种 | GUID | Y |  |
| 17 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 18 | REPAIR_REQUESTION_ID | 报修单 | GUID | Y |  |
| 19 | SIGNED |  | number(0/1) | Y |  |
| 20 | SIGN_EMPLOYEE_ID | 签收人 | GUID | Y |  |
| 21 | SIGN_SUGGESTION | 签收意见 | string(510) | Y |  |
| 22 | SIGN_DATE | 签收日期 | date | Y |  |
| 23 | REPAIR_SITUATION | 维修情况说明 | string(510) | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
| 25 | OLD_REPAIR_STATUS | 报修单维修状态 | string(40) | Y |  |
| 26 | ORIGINAL_STATUS_ID | 原设备状态 | GUID | Y |  |
| 27 | IS_PREPAY | 生成预付款 | number(0/1) | Y |  |
| 28 | REVIEW_PASS | 审查通过 | number(0/1) | Y |  |
| 29 | REVIEW_OPINIONS | 审查意见 | string(510) | Y |  |
| 30 | REVIEW_EMPLOYEE_ID | 审查人员 | GUID | Y |  |
| 31 | REVIEW_DATE | 审查日期 | date | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | OUT_REPAIR_DOC_ID |  | GUID | Y |  |

### OUT_REPAIR_DOC_JOB (委外维修项目明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OUT_REPAIR_DOC_JOB_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 维修项目 | GUID | Y |  |
| 4 | JOB_RESULT | 项目维修结果 | string(510) | Y |  |
| 5 | EXPLANATION | 维护情况说明 | string(510) | Y |  |
| 6 | IS_SUPPLIER | 委外 | number(0/1) | Y |  |
| 7 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 8 | ITEM_ID | 品号 | GUID | Y |  |
| 9 | ITEM_NAME | 品名 | string(120) | Y |  |
| 10 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 11 | CURRENCY_ID | 币种 | GUID | Y |  |
| 12 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 13 | PRICE | 单价 | number(23,8) | Y |  |
| 14 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 15 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 16 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 17 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 18 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 19 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 20 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 21 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 22 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 23 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 24 | TAX_ID | 税种 | GUID | Y |  |
| 25 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 26 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 27 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 28 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 29 | SETTLEMENT_STATUS | 结算状态 | string(40) | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | POOL_FEE | 公摊费用 | number(0/1) | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | OUT_REPAIR_DOC_D_ID |  | GUID | Y |  |

### OUT_REPAIR_DOC_POOL_FEE (委外维修单公摊费用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OUT_REPAIR_DOC_POOL_FEE_ID | 主键 | GUID | Y | Y |
| 3 | INSPECTION_JOB_ID | 维修项目 | GUID | Y |  |
| 4 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_NAME | 品名 | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | CURRENCY_ID | 币种 | GUID | Y |  |
| 9 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 10 | PRICE | 单价 | number(23,8) | Y |  |
| 11 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 12 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 13 | AMT_EXPECTED | 预计金额 | number(23,8) | Y |  |
| 14 | AMT_FACT | 实际金额 | number(23,8) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_EXPECTED | 预计未税金额 | number(23,8) | Y |  |
| 16 | TAX_EXPECTED | 预计税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_FACT | 实际未税金额 | number(23,8) | Y |  |
| 18 | TAX_FACT | 实际税额 | number(23,8) | Y |  |
| 19 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 20 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 21 | TAX_ID | 税种 | GUID | Y |  |
| 22 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 23 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 24 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 25 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
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
| 55 | OUT_REPAIR_DOC_ID |  | GUID | Y |  |

### OUT_REPAIR_DOC_SD (委外维修故障明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | OUT_REPAIR_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | EQT_BREAKDOWN_ID | 故障编号 | GUID | Y |  |
| 4 | BREAKDOWN_DESCRIPTION | 故障详细描述 | string(510) | Y |  |
| 5 | REPAIR_SITUATION | 维修情况说明 | string(510) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | ADD_KNOWLEDGE_BASE | 加入知识库 | number(0/1) | Y |  |
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
| 36 | OUT_REPAIR_DOC_D_ID |  | GUID | Y |  |