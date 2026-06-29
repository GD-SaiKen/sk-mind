---
module: "VMI"
name_zh: "供应商寄售"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 254
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# VMI (供应商寄售)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 5 | Columns: 254

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


- **VMI_AREA (VMI业务范围)**
- **VMI_AREA_D (VMI业务范围明细)**
- **VMI_SETTLEMENT_DOC (VMI结算单)**
- **VMI_SETTLEMENT_DOC_D (VMI结算单消耗汇总)**
- **VMI_SETTLEMENT_DOC_SD (VMI结算单消耗明细)**


---


---


> Tables: 5

### VMI_AREA (VMI业务范围)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | VMI_AREA_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
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
| 30 | Attachments | 附件 | string | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |

### VMI_AREA_D (VMI业务范围明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | VMI_AREA_D_ID |  | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | WAREHOUSE_ID | VMI仓库 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
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
| 36 | VMI_AREA_ID |  | GUID | Y |  |

### VMI_SETTLEMENT_DOC (VMI结算单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | VMI_SETTLEMENT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 8 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 9 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 10 | INVOICE_ADDR | 结算供应商地址名称 | string(510) | Y |  |
| 11 | INVOICE_CONTACT | 结算供应商联系人名称 | string(72) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | CATEGORY | 单据性质 | string(40) | Y |  |
| 14 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 15 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 16 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 17 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 18 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 19 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 20 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 21 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 22 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 23 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 24 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 25 | CURRENCY_ID | 币种 | GUID | Y |  |
| 26 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 27 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 28 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 29 | INVOICE_ADDR_ID | 结算供应商地址 | GUID | Y |  |
| 30 | INVOICE_CONTACT_ID | 结算供应商联系人 | GUID | Y |  |
| 31 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 32 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 33 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 34 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 35 | TAX_ID | 税种 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
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
| 66 | PrintCount | 打印次数 | number | Y |  |
| 67 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 68 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 69 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 70 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 71 | Owner_Org_RTK |  | string(400) | Y |  |
| 72 | Owner_Org_ROid |  | GUID | Y |  |

### VMI_SETTLEMENT_DOC_D (VMI结算单消耗汇总)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | VMI_SETTLEMENT_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 6 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 8 | PRICE | 单价 | number(23,8) | Y |  |
| 9 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 10 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 11 | AMOUNT |  | number(23,8) | Y |  |
| 12 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 13 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 14 | TAX_RATE |  | number(5,4) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | ESTIMATION_TIMES | 暂估次数 | number | Y |  |
| 21 | AMOUNT_UN_TAX_OC | 货款原币金额 | number(23,8) | Y |  |
| 22 | AMOUNT_UN_TAX_BC | 货款本币金额 | number(23,8) | Y |  |
| 23 | SETTLEMENT_PRICE_QTY | 已结算计价数量 | number(16,6) | Y |  |
| 24 | SETTLEMENT_AMOUNT_OC | 已结算货款原币金额 | number(23,8) | Y |  |
| 25 | SETTLEMENT_AMOUNT_BC | 已结算货款本币金额 | number(23,8) | Y |  |
| 26 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 27 | ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 28 | ITEM_ID | 品号 | GUID | Y |  |
| 29 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 30 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 31 | TAX_ID | 税种 | GUID | Y |  |
| 32 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 33 | PLAN_SETTLEMENT_DATE | 预结算日 | date | Y |  |
| 34 | SUPPLIER_CONFIRMED | 供应商确认 | number(0/1) | Y |  |
| 35 | CONFIRMED_DATE | 确认日期 | date | Y |  |
| 36 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 37 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 38 | ESTIMATION_PRICE | 暂估单价 | number(23,8) | Y |  |
| 39 | SETTLEMENT_AMT_UN_TAX_OC | 已结算原币未税金额 | number(23,8) | Y |  |
| 40 | SETTLEMENT_TAX_OC | 已结算原币税额 | number(23,8) | Y |  |
| 41 | SETTLEMENT_AMT_UN_TAX_BC | 已结算本币未税金额 | number(23,8) | Y |  |
| 42 | SETTLEMENT_TAX_BC | 已结算本币税额 | number(23,8) | Y |  |
| 43 | PROJECT_ID | 项目 | GUID | Y |  |
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 54 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 55 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 56 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 57 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 58 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 59 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 60 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 61 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 62 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 63 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 64 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 65 | UDF041 | 自定义字段12 | date | Y |  |
| 66 | UDF042 | 自定义字段13 | date | Y |  |
| 67 | UDF051 | 自定义字段14 | GUID | Y |  |
| 68 | UDF052 | 自定义字段15 | GUID | Y |  |
| 69 | UDF053 | 自定义字段16 | GUID | Y |  |
| 70 | UDF054 | 自定义字段17 | GUID | Y |  |
| 71 | Version | 版本号，不要随意更改 | binary | Y |  |
| 72 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 73 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 74 | VMI_SETTLEMENT_DOC_ID |  | GUID | Y |  |

### VMI_SETTLEMENT_DOC_SD (VMI结算单消耗明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | VMI_SETTLEMENT_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | AMOUNT_UN_TAX_BC | 货款本币金额 | number(23,8) | Y |  |
| 5 | TRANSACTION_LINE_ID | 存货交易明细ID | GUID | Y |  |
| 6 | VMI_SETTLEMENT_DOC_D_ID | 汇总单身ID | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 14 | ApproveDate | 修改日期 | date | Y |  |
| 15 | ApproveBy | 修改人 | GUID | Y |  |
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
| 35 | VMI_SETTLEMENT_DOC_ID |  | GUID | Y |  |