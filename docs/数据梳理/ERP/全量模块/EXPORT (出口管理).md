---
module: "EXPORT"
name_zh: "出口管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 381
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# EXPORT (出口管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 8 | Columns: 381

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]

---

## Tables


- **EXPORT_COST_DOC (出口费用单)**
- **EXPORT_COST_DOC_D (出口费用单明细)**
- **EXPORT_SHIPPING_INST (出口货运通知单)**
- **EXPORT_SHIPPING_INST_D (出口货运通知单明细)**
- **EXPORT_TEMPLATE**
- **EXPORT_TEMPLATE_D**
- **EXPORT_TEMPLATE_SD**
- **EXPORT_TEMPLATE_SDD**


---


---


> Tables: 8

### EXPORT_COST_DOC (出口费用单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | EXPORT_COST_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_DATE | 费用日期 | date | Y |  |
| 9 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 10 | CURRENCY_ID | 币种 | GUID | Y |  |
| 11 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 14 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 15 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 16 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 17 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 18 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 19 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 20 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 21 | REMARK | 备注意见 | string(510) | Y |  |
| 22 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 23 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 24 | SYNERGY_D_ID | 协同关系 | GUID | Y |  |
| 25 | TAX_ID | 税种 | GUID | Y |  |
| 26 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 27 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 28 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 29 | PrintCount | 打印次数 | number | Y |  |
| 30 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 31 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 32 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 33 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |

### EXPORT_COST_DOC_D (出口费用单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPORT_COST_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SALES_DELIVERY_ID | 出货通知单号 | GUID | Y |  |
| 4 | INVOICE_NO | INVOCIE单号 | string(40) | Y |  |
| 5 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 6 | EXPENSE_AMOUNT | 费用金额 | number(23,8) | Y |  |
| 7 | TAX_ID | 税种 | GUID | Y |  |
| 8 | TAX_RATE | 稅率 | number(5,4) | Y |  |
| 9 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 10 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 11 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 12 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 13 | MASTER_BL | 大提单单号 | string(40) | Y |  |
| 14 | HOUSE_BL | 小提单单号 | string(40) | Y |  |
| 15 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 16 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 17 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 18 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | PLAN_SETTLEMENT_DATE | 预计结算日 | date | Y |  |
| 21 | ESTI_REVERSE_MODE | 暂估冲回方式 | string(40) | Y |  |
| 22 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 23 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 24 | SETTLEMENT_AMT_UN_TAX_BC | 已结算本币未税金额 | number(23,8) | Y |  |
| 25 | SETTLEMENT_TAX_BC | 已结算本币金额 | number(23,8) | Y |  |
| 26 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 27 | SETTLEMENT_DIFF_AMT_BC | 当期结算差异调整本币金额 | number(23,8) | Y |  |
| 28 | AMOUNT |  | number(23,8) | Y |  |
| 29 | PROJECT_ID | 项目 | GUID | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 55 | EXPORT_COST_DOC_ID |  | GUID | Y |  |

### EXPORT_SHIPPING_INST (出口货运通知单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | EXPORT_SHIPPING_INST_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_DATE | 运货日期 | date | Y |  |
| 9 | CONTAINER_GROUND | 货柜场 | string(510) | Y |  |
| 10 | CONTAINER_NO | 货柜号码 | string(510) | Y |  |
| 11 | CONTAINER_SIZE | 货柜尺寸 | string(510) | Y |  |
| 12 | SHIP_NAME | 船名 | string(510) | Y |  |
| 13 | VOYAGE_NO | 船次 | string(510) | Y |  |
| 14 | WEIGHT | 重量 | number(16,6) | Y |  |
| 15 | VOLUME | 材积 | number(16,6) | Y |  |
| 16 | PIECES | 件数 | number | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | TRANSPORT_SUPPLIER_ID | 运输公司 | GUID | Y |  |
| 19 | WEIGHT_UNIT_ID | 重量单位 | GUID | Y |  |
| 20 | VOLUMN_UNIT_ID | 材积单位 | GUID | Y |  |
| 21 | PrintCount | 打印次数 | number | Y |  |
| 22 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 23 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 24 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 25 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Attachments | 附件 | string | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |

### EXPORT_SHIPPING_INST_D (出口货运通知单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EXPORT_SHIPPING_INST_D_ID | 主键 | GUID | Y | Y |
| 3 | INVOICE_NO | INVOCIE单号 | string(40) | Y |  |
| 4 | TAX_INVOICE_NO | 税务发票号码 | string(510) | Y |  |
| 5 | WEIGHT | 重量 | number(16,6) | Y |  |
| 6 | PIECES | 件数 | number | Y |  |
| 7 | REMARK_NO | 注记号 | string(510) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | SALES_DELIVERY_ID | 出货通知单 | GUID | Y |  |
| 10 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 11 | VOLUME | 材积 | number(16,6) | Y |  |
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
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | EXPORT_SHIPPING_INST_ID |  | GUID | Y |  |

### EXPORT_TEMPLATE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EXPORT_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | PROGRAM_NO | 作业编号 | string(400) | Y |  |
| 5 | PROGRAM_TYPE | 作业类型 | number | Y |  |
| 6 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
| 7 | QUANTITY | 分包笔数 | number | Y |  |
| 8 | PRODUCT | 集成产品别 | number | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | TYPEKEY_NO | TYPEKEY编号 | string(400) | Y |  |
| 11 | Attachments | 附件 | string | Y |  |
| 12 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### EXPORT_TEMPLATE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PATH | 路径 | string(2000) | Y |  |
| 3 | EXPORT_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 4 | TABLE_DISNAME1 | 实体名称 | string(400) | Y |  |
| 5 | TABLE_DISNAME2 | 繁体名称 | string(400) | Y |  |
| 6 | TABLE_DISNAME3 | 英文名称 | string(400) | Y |  |
| 7 | SHEET_NAME | 映射表名 | string(400) | Y |  |
| 8 | TABLE_SNAME | 实体代号 | string(400) | Y |  |
| 9 | FATHER_TABLE_NAME | 主表 | string(400) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
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
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | EXPORT_TEMPLATE_ID |  | GUID | Y |  |

### EXPORT_TEMPLATE_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | COLUMN_NAME | 字段名称 | string(200) | Y |  |
| 2 | COLUMN_TYPE | 字段类型：1.实体字段；2.带值字段；3.计算字段 | string(2) | Y |  |
| 3 | EXPRESSION | 公式表达式 | string(2000) | Y |  |
| 4 | REFERENCE_COLUMN | 带值引用字段 | string(200) | Y |  |
| 5 | REFERENCE_SOURCE | 带值来源字段 | string(200) | Y |  |
| 6 | SequenceNumber |  | number | Y |  |
| 7 | EXPORT_TEMPLATE_SD_ID |  | GUID | Y | Y |
| 8 | FIELD_NAME | 字段名称 | string(400) | Y |  |
| 9 | FIELD_ID | 字段编号 | string(80) | Y |  |
| 10 | IMPORT_TEMPLATE_FLAG | 发布 | number(0/1) | Y |  |
| 11 | DEFAULT_VALUE | 默认值 | string(400) | Y |  |
| 12 | HIDE_FLAG | 隐藏 | number(0/1) | Y |  |
| 13 | SERVICE_KEY_FLAG | 业务主键 | number(0/1) | Y |  |
| 14 | FIELD_PROPERTY | 字段类型 | string(100) | Y |  |
| 15 | FIELD_LENGTH | 字段长度 | number | Y |  |
| 16 | FIELD_ACCURACY | 字段精度 | number | Y |  |
| 17 | SOURCE_FIELD | 带值字段 | string(400) | Y |  |
| 18 | ENTITY_FLAG | 实体字段 | number(0/1) | Y |  |
| 19 | IN_CON_CODE | 带值编号 | string(80) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | SOURCE_TYPE | 集成类型 | string(40) | Y |  |
| 22 | OUT_PICKLISTTYPE | PICKLIST导出类型 | number | Y |  |
| 23 | MSOURCE_ASSIGN_FLAG | 多来源赋值标识 | number(0/1) | Y |  |
| 24 | PICKLISTTYPE | PICKLIST类型 | string(400) | Y |  |
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
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | EXPORT_TEMPLATE_D_ID |  | GUID | Y |  |

### EXPORT_TEMPLATE_SDD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | REFERENCE_SOURCE | 带值来源字段 | string(200) | Y |  |
| 3 | EXPORT_TEMPLATE_SDD_ID |  | GUID | Y | Y |
| 4 | REMARK |  | string(510) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | EXPORT_TEMPLATE_SD_ID |  | GUID | Y |  |