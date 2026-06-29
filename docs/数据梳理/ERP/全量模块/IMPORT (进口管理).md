---
module: "IMPORT"
name_zh: "进口管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 10
columns: 455
category: purchase
tags: ["ERP", "E10", "purchase"]
created: 2026-06-25 10:52
---

# IMPORT (进口管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 10 | Columns: 455

## Related Modules

- [[NEGOTIATE (议价管理)|NEGOTIATE (议价管理)]]
- [[PO (采购订单)|PO (采购订单)]]
- [[PURCHASE (采购管理)|PURCHASE (采购管理)]]
- [[REQUISITION (请购管理)|REQUISITION (请购管理)]]
- [[SUPPLIER (供应商)|SUPPLIER (供应商)]]
- [[SUPPLY (供应中心)|SUPPLY (供应中心)]]

---

## Tables


- **IMPORT_EXPENSE (进口费用)**
- **IMPORT_EXPENSE_D (进口费用明细)**
- **IMPORT_EXPENSE_DATA (进口费用资料)**
- **IMPORT_TAX**
- **IMPORT_TEMPLATE**
- **IMPORT_TEMPLATE_CON**
- **IMPORT_TEMPLATE_D**
- **IMPORT_TEMPLATE_FORMULA**
- **IMPORT_TEMPLATE_SD**
- **IMPORT_TEMPLATE_SDD**


---


---


> Tables: 10

### IMPORT_EXPENSE (进口费用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | IMPORT_EXPENSE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 9 | IMPORT_EXPENSE_DATE | 进口费用日期 | date | Y |  |
| 10 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 11 | PLANT_ID | 收货机构 | GUID | Y |  |
| 12 | CURRENCY_ID | 币种 | GUID | Y |  |
| 13 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 14 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 15 | ALLOCATION_METHOD | 费用分摊方式 | string(40) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | EXPENSES_TRANS_CURR | 原币费用金额 | number(23,8) | Y |  |
| 18 | TAX_OC | 原币营业税额 | number(23,8) | Y |  |
| 19 | TT_EXPENSES_TRANS_CURR | 原币费用总计 | number(23,8) | Y |  |
| 20 | COST_TRANS_CURR | 原币成本金额 | number(23,8) | Y |  |
| 21 | EXPENSES_LOCAL_CURR | 本币费用金额 | number(23,8) | Y |  |
| 22 | TAX_BC | 本币营业税额 | number(23,8) | Y |  |
| 23 | TT_EXPENSES_LOCAL_CURR | 本币费用总计 | number(23,8) | Y |  |
| 24 | COST_LOCAL_CURR | 本币成本金额 | number(23,8) | Y |  |
| 25 | TAX_COST_TRANS_CURR | 原币成本税额 | number(23,8) | Y |  |
| 26 | TT_COST_TRANS_CURR | 原币成本总计 | number(23,8) | Y |  |
| 27 | TAX_COST_LOCAL_CURR | 本币成本税额 | number(23,8) | Y |  |
| 28 | TT_COST_LOCAL_CURR | 本币成本总计 | number(23,8) | Y |  |
| 29 | TT_BUSINESS_QTY | 业务数量合计 | number(16,6) | Y |  |
| 30 | TT_AMOUNT | 金额合计 | number(23,8) | Y |  |
| 31 | TT_GROSS_WEIGHT_KG | 毛重合计 | number(16,6) | Y |  |
| 32 | TT_VOLUME | 材积合计 | number(16,6) | Y |  |
| 33 | PrintCount | 打印次数 | number | Y |  |
| 34 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 35 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 36 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 37 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 47 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 48 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 49 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 50 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 51 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 52 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 53 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 54 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 55 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 56 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 57 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 58 | UDF041 | 自定义字段12 | date | Y |  |
| 59 | UDF042 | 自定义字段13 | date | Y |  |
| 60 | UDF051 | 自定义字段14 | GUID | Y |  |
| 61 | UDF052 | 自定义字段15 | GUID | Y |  |
| 62 | UDF053 | 自定义字段16 | GUID | Y |  |
| 63 | UDF054 | 自定义字段17 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |
| 68 | Owner_Org_RTK |  | string(400) | Y |  |
| 69 | Owner_Org_ROid |  | GUID | Y |  |

### IMPORT_EXPENSE_D (进口费用明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | IMPORT_EXPENSE_D_ID | 主键 | GUID | Y | Y |
| 3 | EXPENSE_RATE | 费用比率 | number(18,9) | Y |  |
| 4 | EXPENSE_EXCL_TAX_TRANS_CURR | 原币费用未税金额 | number(23,8) | Y |  |
| 5 | TAX_EXPENSE_TRANS_CURR | 原币费用税额 | number(23,8) | Y |  |
| 6 | EXPENSE_EXCL_TAX_LOCAL_CURR | 本币费用未税金额 | number(23,8) | Y |  |
| 7 | TAX_EXPENSE_LOCAL_CURR | 本币费用税额 | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | EXPENSE | 费用金额 | number(23,8) | Y |  |
| 10 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 11 | COST_EXCL_TAX_TRANS_CURR | 原币成本未税金额 | number(23,8) | Y |  |
| 12 | TAX_COST_TRANS_CURR | 原币成本税额 | number(23,8) | Y |  |
| 13 | COST_EXCL_TAX_LOCAL_CURR | 本币成本未税金额 | number(23,8) | Y |  |
| 14 | TAX_COST_LOCAL_CURR | 本币成本税额 | number(23,8) | Y |  |
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
| 40 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ID_ROid |  | GUID | Y |  |
| 42 | IMPORT_EXPENSE_ID |  | GUID | Y |  |

### IMPORT_EXPENSE_DATA (进口费用资料)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | IMPORT_EXPENSE_DATA_ID | 主键 | GUID | Y | Y |
| 3 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 4 | TAX_ID | 税种 | GUID | Y |  |
| 5 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 6 | CURRENCY_ID | 币种 | GUID | Y |  |
| 7 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 8 | EXPENSE_AMOUNT | 费用金额 | number(23,8) | Y |  |
| 9 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 10 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 11 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 12 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 13 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 14 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 15 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 16 | TAX_CODE | 税款码 | number(0/1) | Y |  |
| 17 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | IMPORT_EXPENSE_ID |  | GUID | Y |  |

### IMPORT_TAX

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | IMPORT_TAX_ID | 主键 | GUID | Y | Y |
| 4 | IMPORT_TAX_CODE | 进口税代号 | string(12) | Y |  |
| 5 | IMPORT_TAX_NAME | 进口税名称 | string(60) | Y |  |
| 6 | IMPORT_TAX_TYPE | 进口税分类 | string(40) | Y |  |
| 7 | IMPORT_TAX_RATE | 税率 | number(5,4) | Y |  |
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

### IMPORT_TEMPLATE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | IMPORT_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | PROGRAM_NO | 作业编号 | string(400) | Y |  |
| 5 | PROGRAM_TYPE | 作业类型 | number | Y |  |
| 6 | REMARK |  | string(510) | Y |  |
| 7 | DATA_TYPE | 数据类型 | number | Y |  |
| 8 | TYPEKEY_NAME | 实体 | string(80) | Y |  |
| 9 | IMPT_NO | 模板编号 | string(80) | Y |  |
| 10 | IMPT_DISNAME1 | 模板名称-简体 | string(400) | Y |  |
| 11 | IMPT_DISNAME2 | 模板名称-繁体 | string(400) | Y |  |
| 12 | IMPT_DISNAME3 | 模板名称-英文 | string(400) | Y |  |
| 13 | OUT_ORDER | 导出排序 | number | Y |  |
| 14 | OUT_LOT | 导出批量 | number | Y |  |
| 15 | IN_LOT | 导入批量 | number | Y |  |
| 16 | PROGRAM_NAME | 作业名称 | string(80) | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |

### IMPORT_TEMPLATE_CON

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | IMPORT_TEMPLATE_CON_ID | 主键 | GUID | Y | Y |
| 5 | CON_CODE | 查询编号 | string(80) | Y |  |
| 6 | SOURCE_TABLE | 来源表 | string(400) | Y |  |
| 7 | IN_CON | 查询条件 | string(1200) | Y |  |
| 8 | REMARK |  | string(510) | Y |  |
| 9 | RETURN_FIELD | 返回字段 | string(80) | Y |  |
| 10 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |
| 40 | IMPORT_TEMPLATE_ID |  | GUID | Y |  |

### IMPORT_TEMPLATE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | IMPORT_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 5 | TABLE_DISNAME1 | 数据表显示名称 | string(400) | Y |  |
| 6 | TABLE_DISNAME2 | 数据表显示名称 | string(400) | Y |  |
| 7 | TABLE_DISNAME3 | 数据表显示名称 | string(400) | Y |  |
| 8 | SHEET_NAME | 工作表名称 | string(400) | Y |  |
| 9 | TABLE_SNAME | 数据表名称 | string(400) | Y |  |
| 10 | FATHER_TABLE_NAME | 父表名称 | string(400) | Y |  |
| 11 | REMARK |  | string(510) | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | IMPORT_TEMPLATE_ID |  | GUID | Y |  |

### IMPORT_TEMPLATE_FORMULA

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | TARGET_FIELD | 目标字段 | string(400) | Y |  |
| 5 | PATH | 路径 | string(2400) | Y |  |
| 6 | EXPRESSION | 表达式 | string(2400) | Y |  |
| 7 | IMPORT_TEMPLATE_FORMULA_ID | 主键 | GUID | Y | Y |
| 8 | REMARK |  | string(510) | Y |  |
| 9 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |
| 39 | IMPORT_TEMPLATE_ID |  | GUID | Y |  |

### IMPORT_TEMPLATE_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | IMPORT_TEMPLATE_SD_ID | 主键 | GUID | Y | Y |
| 5 | FIELD_NAME | 字段名 | string(400) | Y |  |
| 6 | FIELD_NAME1 | 字段名1 | string(400) | Y |  |
| 7 | FIELD_NAME2 | 字段名2 | string(400) | Y |  |
| 8 | FIELD_ID | 字段ID | string(140) | Y |  |
| 9 | SERVICE_KEY_FLAG | 业务主键标识 | number(0/1) | Y |  |
| 10 | HIDE_FLAG | 隐藏标识 | number(0/1) | Y |  |
| 11 | SOURCE_TYPE | 导入赋值类型 | number | Y |  |
| 12 | DEFAULT_VALUE | 导入指定值 | string(400) | Y |  |
| 13 | IN_SOURCE_TYPE | 导出赋值类型 | number | Y |  |
| 14 | FIELD_PROPERTY | 字段属性 | string(100) | Y |  |
| 15 | PICKLISTTYPE | PICKLIST类型 | string(80) | Y |  |
| 16 | ENTITY_FLAG | 实体字段 | number(0/1) | Y |  |
| 17 | IN_CON_CODE | 查询编号 | string(400) | Y |  |
| 18 | REMARK |  | string(510) | Y |  |
| 19 | MSOURCE_ASSIGN_FLAG | 多来源赋值标识 | number(0/1) | Y |  |
| 20 | MSOURCE_WHERE_FIELD | 多来源条件字段 | string(80) | Y |  |
| 21 | FIELD_NAME3 | 字段名 | string(400) | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |
| 52 | IMPORT_TEMPLATE_D_ID |  | GUID | Y |  |

### IMPORT_TEMPLATE_SDD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | IMPORT_TEMPLATE_SDD_ID | 主键 | GUID | Y | Y |
| 5 | WHERE_VALUE | 条件值 | string(400) | Y |  |
| 6 | MSOURCE_ASSIGN_TYPE | 多来源赋值类型 | number | Y |  |
| 7 | CON_CODE | 查询编号 | string(80) | Y |  |
| 8 | DEFAULT_VALUE | 指定值 | string(400) | Y |  |
| 9 | REMARK |  | string(510) | Y |  |
| 10 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |
| 40 | IMPORT_TEMPLATE_SD_ID |  | GUID | Y |  |