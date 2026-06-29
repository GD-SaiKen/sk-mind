---
module: "CUSTOMS"
name_zh: "海关申报"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 168
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# CUSTOMS (海关申报)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 168

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


- **CUSTOMS_DECLARATION (报关赎单)**
- **CUSTOMS_DECLARATION_D (报关赎单明細)**


---


---


> Tables: 2

### CUSTOMS_DECLARATION (报关赎单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CUSTOMS_DECLARATION_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 9 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 10 | DECLARATION_NO | 报单号码 | string(40) | Y |  |
| 11 | DECLARATION_DATE | 报关日期 | date | Y |  |
| 12 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 13 | MASTER_BL_NO | 大提单号 | string(40) | Y |  |
| 14 | DO_NO | 小提单号 | string(40) | Y |  |
| 15 | BL_DATE | 提单日期 | date | Y |  |
| 16 | AMIVAL_DATE | 到港日期 | date | Y |  |
| 17 | ETD | ETD | date | Y |  |
| 18 | ETA | ETA | date | Y |  |
| 19 | ARRIVAL_UPDATE_CODE | 到货单更新码 | number(0/1) | Y |  |
| 20 | SHIPPING_COMPANY_SUPPLIER_ID | 船公司 | GUID | Y |  |
| 21 | CONTAINER_YARD | 货柜场 | string(80) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | FREE_STORE_RENTAL_DATE | 免费仓租日期 | date | Y |  |
| 24 | IMPORT_EXPENSE_UPDATE_CODE | 费用单更新码 | number(0/1) | Y |  |
| 25 | NEGOTIATION_DATE | 押汇日期 | date | Y |  |
| 26 | CURRENCY_ID | 币种 | GUID | Y |  |
| 27 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 28 | FORWARD_DAYS | 远期天数 | number | Y |  |
| 29 | YEARLY_INTEREST_RATE | 年利率 | number(5,4) | Y |  |
| 30 | BANK_INTEREST_TRANS_CURR | 本币银行利息 | number(23,8) | Y |  |
| 31 | PAYABLE_DATE | 应还款日 | date | Y |  |
| 32 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 33 | BROKER_SUPPLIER_ID | 报关行 | GUID | Y |  |
| 34 | SHIP_NAME | 船名 | string(80) | Y |  |
| 35 | VESSEL_NO | 船次 | string(80) | Y |  |
| 36 | SHIPPING_INSTRUCTION_ID | SI单号 | GUID | Y |  |
| 37 | TAX_PAYMENT_CERTIFICATE_NO | 税款缴纳证号 | string(28) | Y |  |
| 38 | FREIGHT_TRANS_CURR | 原币运费 | number(23,8) | Y |  |
| 39 | PREMIUM_TRANS_CURR | 原币保险费 | number(23,8) | Y |  |
| 40 | IN_DE_EXP_TRANS_CURR | 原币增减费用 | number(23,8) | Y |  |
| 41 | TAX_RATE | 增值稅率 | number(5,4) | Y |  |
| 42 | DEDUCTIBLE_INDICATOR | 可扣抵VTA标示 | number(0/1) | Y |  |
| 43 | TAX_BASIS_LOCAL_CURR | 本币营业税基 | number(23,8) | Y |  |
| 44 | TAX_BC | 本币营业税额 | number(23,8) | Y |  |
| 45 | BILL_RETIRED_AMT_TRANS_CURR | 原币赎单金额 | number(23,8) | Y |  |
| 46 | BILL_RETIRED_AMT_LOCAL_CURR | 本币赎单金额 | number(23,8) | Y |  |
| 47 | SELF_FUNDING_OFFSET_TRANS_CURR | 原币冲自筹额 | number(23,8) | Y |  |
| 48 | SELF_FUNDING_OFFSET_LOCAL_CURR | 本币冲自筹额 | number(23,8) | Y |  |
| 49 | AMT_REPAYABLE_TRANS_CURR | 原币应还款额 | number(23,8) | Y |  |
| 50 | AMT_REPAYABLE_LOCAL_CURR | 本币应还款额 | number(23,8) | Y |  |
| 51 | TT_PRICE_INCL_TAX_TRANS_CURR | 原币完税价格合计 | number(23,8) | Y |  |
| 52 | TT_PRICE_INCL_TAX_LOCAL_CURR | 本币完税价格合计 | number(23,8) | Y |  |
| 53 | TT_TARIFF_TRANS_CURR | 原币关税合计 | number(23,8) | Y |  |
| 54 | TT_TARIFF_LOCAL_CURR | 本币关税合计 | number(23,8) | Y |  |
| 55 | TT_PROMOTION_EXPENSE | 推广贸易费合计 | number(23,8) | Y |  |
| 56 | TT_COMMODITY_TAX | 货物税合计 | number(23,8) | Y |  |
| 57 | ALLOCATION_METHOD | 费用分摊方式 | number | Y |  |
| 58 | TT_LC_EXPENSE | LC费用合计 | number(23,8) | Y |  |
| 59 | TT_BL_EXPENSE | BL费用总计 | number(23,8) | Y |  |
| 60 | TT_BL_COST | BL成本合计 | number(23,8) | Y |  |
| 61 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 62 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 63 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 64 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 65 | CreateDate | 创建日期 | date | Y |  |
| 66 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 67 | ModifiedDate | 修改日期 | date | Y |  |
| 68 | CreateBy | 创建者 | GUID | Y |  |
| 69 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 70 | ModifiedBy | 修改者 | GUID | Y |  |
| 71 | Attachments | 附件 | string | Y |  |
| 72 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 73 | PrintCount | 打印次数 | number | Y |  |
| 74 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 75 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 76 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 77 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 78 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 79 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 80 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 81 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 82 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 83 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 84 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 85 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 86 | UDF041 | 自定义字段12 | date | Y |  |
| 87 | UDF042 | 自定义字段13 | date | Y |  |
| 88 | UDF051 | 自定义字段14 | GUID | Y |  |
| 89 | UDF052 | 自定义字段15 | GUID | Y |  |
| 90 | UDF053 | 自定义字段16 | GUID | Y |  |
| 91 | UDF054 | 自定义字段17 | GUID | Y |  |
| 92 | Version | 版本号，不要随意更改 | binary | Y |  |
| 93 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 94 | ApproveDate | 修改日期 | date | Y |  |
| 95 | ApproveBy | 修改人 | GUID | Y |  |
| 96 | Owner_Org_RTK |  | string(400) | Y |  |
| 97 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMS_DECLARATION_D (报关赎单明細)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PURCHASE_ORDER_ID | 采购订单ID | GUID | Y |  |
| 3 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 4 | RECEIVED_QTY | 实收数量 | number(16,6) | Y |  |
| 5 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | SECOND_RECEIVED_QTY | 第二实收数量 | number(16,6) | Y |  |
| 8 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 9 | PRICE | 单价 | number(23,8) | Y |  |
| 10 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 11 | AMOUNT | 金额 | number(23,8) | Y |  |
| 12 | SELF_FUNDING_OFFSET | 冲自筹额 | number(23,8) | Y |  |
| 13 | PRICE_INCL_TAX_TRANS_CURR | 原币完税价格 | number(23,8) | Y |  |
| 14 | PRICE_INCL_TAX_LOCAL_CURR | 本币完税价格 | number(23,8) | Y |  |
| 15 | TARIFF_RATE | 关税率 | number(5,4) | Y |  |
| 16 | TARIFF_TRANS_CURR | 原币关税 | number(23,8) | Y |  |
| 17 | TARIFF_LOCAL_CURR | 本币关税 | number(23,8) | Y |  |
| 18 | PROMOTION_TRADE_RATE | 推广贸易费率 | number(5,4) | Y |  |
| 19 | TRADE_PROMOTION_CHARGES | 推广贸易费 | number(23,8) | Y |  |
| 20 | CARGO_TAX_RATE | 货物税率 | number(5,4) | Y |  |
| 21 | COMMODITY_TAX | 货物税额 | number(23,8) | Y |  |
| 22 | TAX_BASIS_LOCAL_CURR | 本币营业税基 | number(23,8) | Y |  |
| 23 | TAX_BC | 本币营业税额 | number(23,8) | Y |  |
| 24 | COUNTER_NO | 柜号 | string(40) | Y |  |
| 25 | PIECES | 件数 | number | Y |  |
| 26 | CONTAINER_CATEGORY | 柜别 | string(20) | Y |  |
| 27 | GROSS_WEIGHT_KG | 毛重Kg | number(16,6) | Y |  |
| 28 | VOLUME | 材积Volume | number(16,6) | Y |  |
| 29 | INVOICE_NO | INVOICE_NO | string(40) | Y |  |
| 30 | BL_EXPENSES_ALLOCATION | BL费用分摊 | number(23,8) | Y |  |
| 31 | LC_EXPENSES_ALLOCATION | LC费用分摊 | number(23,8) | Y |  |
| 32 | IMPORT_EXPENSE_UPDATE_CODE | 费用单更新码 | number(0/1) | Y |  |
| 33 | REMARK | 备注 | string(510) | Y |  |
| 34 | CUSTOMS_DECLARATION_D_ID | 主键 | GUID | Y | Y |
| 35 | ITEM_ID | 品号 | GUID | Y |  |
| 36 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 37 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 38 | BIN_ID | 库位 | GUID | Y |  |
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | Version | 版本号，不要随意更改 | binary | Y |  |
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |
| 67 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 68 | SOURCE_ID_ROid |  | GUID | Y |  |
| 69 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 70 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 71 | CUSTOMS_DECLARATION_ID |  | GUID | Y |  |