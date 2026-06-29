---
module: "PAYABLE"
name_zh: "应付余额"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 9
columns: 795
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# PAYABLE (应付余额)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 9 | Columns: 795

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


- **PAYABLE_BALANCE (应付余额档)**
- **PAYABLE_DOC (应付单)**
- **PAYABLE_DOC_D (应付单单身)**
- **PAYABLE_DOC_INSTAL (应付单分期)**
- **PAYABLE_DOC_TAXINV (应付单税务发票)**
- **PAYABLE_HISTORY (应付交易历史)**
- **PAYABLE_NOTE (应付票据)**
- **PAYABLE_OBJECT (应付对象档)**
- **PAYABLE_OBJECT_CHANGE (应付对象变更历史)**


---


---


> Tables: 9

### PAYABLE_BALANCE (应付余额档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PAYABLE_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | PAYABLES_TYPE | 应付款类型 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | OPENING_PAYABLE_AMT_TC | 应付期初余额(原币) | number(23,8) | Y |  |
| 8 | OPENING_PAYABLE_AMT_FC | 应付期初余额(本币) | number(23,8) | Y |  |
| 9 | INITIAL_AMT_TC | 应付原始金额-本期应付发生额(原币) | number(23,8) | Y |  |
| 10 | INITIAL_AMT_FC | 应付原始金额-本期应付发生额(本币) | number(23,8) | Y |  |
| 11 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 12 | TRANSFER_AMT_TC | 本期转销金额(原币) | number(23,8) | Y |  |
| 13 | TRANSFER_AMT_FC | 本期转销金额(本币) | number(23,8) | Y |  |
| 14 | VERIFICATION_AMT_TC | 本期已核销金额(原币) | number(23,8) | Y |  |
| 15 | VERIFICATION_AMT_FC | 本期已核销金额(本币) | number(23,8) | Y |  |
| 16 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 17 | DEPOSIT_TAX_OPENING_TC | 定金税额期初余额(原币) | number(23,8) | Y |  |
| 18 | DEPOSIT_TAX_OPENING_FC | 定金税额期初余额(本币) | number(23,8) | Y |  |
| 19 | DEPOSIT_TAX_INITIAL_TC | 定金税额原始金额-本期发生额(原币) | number(23,8) | Y |  |
| 20 | DEPOSIT_TAX_INITIAL_FC | 定金税额原始金额-本期发生额(本币) | number(23,8) | Y |  |
| 21 | DEPOSIT_TAX_OFFSETED_TC | 定金税额本期已冲减金额(原币) | number(23,8) | Y |  |
| 22 | DEPOSIT_TAX_OFFSETED_FC | 定金税额本期已冲减金额(本币) | number(23,8) | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### PAYABLE_DOC (应付单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | PAYABLE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 12 | TAX_CONTROL_INDICATOR | 税务发票控制 | number(0/1) | Y |  |
| 13 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 14 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 15 | TRANS_TYPE | 业务类型 | number | Y |  |
| 16 | DETAIL_TRANS_TYPE | 明细业务类型 | number | Y |  |
| 17 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 18 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 19 | PAYMENT_DATE | 付款日 | date | Y |  |
| 20 | CASHING_DATE | 兑现日 | date | Y |  |
| 21 | INSTALLMENT_SOURDOC_TYPE | 分期源单类型 | number | Y |  |
| 22 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 23 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 24 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 25 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 26 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 27 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 28 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 29 | AMT_UNTAX_TC | 无税金额合计(原币) | number(23,8) | Y |  |
| 30 | TAX_TC | 税额合计(原币) | number(23,8) | Y |  |
| 31 | AMT_UNTAX_FC | 无税金额合计(本币) | number(23,8) | Y |  |
| 32 | TAX_FC | 税额合计(本币) | number(23,8) | Y |  |
| 33 | PPV | 价差合计 | number(23,8) | Y |  |
| 34 | TRANS_NATURE | 业务性质 | number | Y |  |
| 35 | INNER_SYNERGY_INDICATOR | 内部协同标识(作废) | number(0/1) | Y |  |
| 36 | REMARK | 备注 | string(510) | Y |  |
| 37 | TAX_INVOICE_TYPE | 税务发票类型 | number | Y |  |
| 38 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 39 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 40 | VAT_INDICATOR | VAT标识 | number(0/1) | Y |  |
| 41 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 42 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 43 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 44 | SETTLEMENT_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 45 | ORDER_SUPPLIER_ID | 采购供应商 | GUID | Y |  |
| 46 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 47 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 48 | CURRENCY_ID | 货币 | GUID | Y |  |
| 49 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 50 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 51 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 52 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 53 | PAYMENT_DOC_ID | 现结付款单号 | GUID | Y |  |
| 54 | INNER_SETTLEMENT_DOC_ID | 内部结算单号 | GUID | Y |  |
| 55 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 56 | TAX_ID | 税种税率 | GUID | Y |  |
| 57 | ESTI_REVERSE_AP_STATUS | 应付暂估冲回状态 | number | Y |  |
| 58 | ISSUE_INVOICE_STATUS | 传入税管状态 | number | Y |  |
| 59 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 60 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 61 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 62 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 63 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 64 | TAX_DEDUCTIBLE_INDICATOR | 税额抵扣标识 | number(0/1) | Y |  |
| 65 | TAX_INVOICE_SOURCE | 税务发票来源 | number | Y |  |
| 66 | TAX_INVOICE_CATEGORY_DISC_ID | 折让税务发票种类 | GUID | Y |  |
| 67 | INSTAL_AMT_TC | 分期结算金额(原币) | number(23,8) | Y |  |
| 68 | INSTAL_AMT_FC | 分期结算金额(本币) | number(23,8) | Y |  |
| 69 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 70 | FROM_RECEIVABLE_DOC_ID | 来源应收单 | GUID | Y |  |
| 71 | TO_RECEIVABLE_DOC_ID | 抛转应收单 | GUID | Y |  |
| 72 | SYNERGY_SETTLEMENT_STATUS | 协同抛转状态 | number | Y |  |
| 73 | TAX_MODE | 税额计算方式 | string(40) | Y |  |
| 74 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 75 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 76 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 77 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |
| 81 | CreateDate | 创建日期 | date | Y |  |
| 82 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 83 | ModifiedDate | 修改日期 | date | Y |  |
| 84 | CreateBy | 创建者 | GUID | Y |  |
| 85 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 86 | ModifiedBy | 修改者 | GUID | Y |  |
| 87 | Attachments | 附件 | string | Y |  |
| 88 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 89 | Version | 版本号，不要随意更改 | binary | Y |  |
| 90 | PrintCount | 打印次数 | number | Y |  |
| 91 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 92 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 93 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 94 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 95 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 96 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 97 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 98 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 99 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 100 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 101 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 102 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 103 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 104 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 105 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 106 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 107 | UDF041 | 自定义字段12 | date | Y |  |
| 108 | UDF042 | 自定义字段13 | date | Y |  |
| 109 | UDF051 | 自定义字段14 | GUID | Y |  |
| 110 | UDF052 | 自定义字段15 | GUID | Y |  |
| 111 | UDF053 | 自定义字段16 | GUID | Y |  |
| 112 | UDF054 | 自定义字段17 | GUID | Y |  |
| 113 | Owner_Org_RTK |  | string(400) | Y |  |
| 114 | Owner_Org_ROid |  | GUID | Y |  |
| 115 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 116 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 117 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 118 | SOURCE_ID_ROid |  | GUID | Y |  |
| 119 | SYNERGY_ID_RTK |  | string(400) | Y |  |
| 120 | SYNERGY_ID_ROid |  | GUID | Y |  |
| 121 | SYNERGY_D_ID_RTK |  | string(400) | Y |  |
| 122 | SYNERGY_D_ID_ROid |  | GUID | Y |  |
| 123 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 124 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 125 | SOURDOC_TYPE | 源单类型 | number | Y |  |
| 126 | R_INNER_SETTLEMENT_FLAG | 需内部结算标识 | number(0/1) | Y |  |
| 127 | PROJECT_ID | 项目 | GUID | Y |  |
| 128 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 129 | SOURCE4_ID_ROid |  | GUID | Y |  |

### PAYABLE_DOC_D (应付单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYABLE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 应付来源单据类型 | number | Y |  |
| 4 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 5 | ITEM_NAME | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 8 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 9 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 10 | VAT_INDICATOR | VAT标识 | number(0/1) | Y |  |
| 11 | PRICE | 商业折扣前单价 | number(23,8) | Y |  |
| 12 | DISCOUNT_RATE | 商业折扣率 | number(5,4) | Y |  |
| 13 | DISCOUNT_AMT | 商业折扣额 | number(23,8) | Y |  |
| 14 | DISCOUNTED_PRICE_UNTAX | 折扣后无税单价 | number(23,8) | Y |  |
| 15 | DISCOUNTED_PRICE_INTAX | 折扣后含税单价 | number(23,8) | Y |  |
| 16 | AMT_UNTAX_TC | 无税金额(原币) | number(23,8) | Y |  |
| 17 | TAX_TC | 税额(原币) | number(23,8) | Y |  |
| 18 | AMT_TC | 价税合计(原币) | number(23,8) | Y |  |
| 19 | AMT_UNTAX_FC | 无税金额(本币) | number(23,8) | Y |  |
| 20 | TAX_FC | 税额(本币) | number(23,8) | Y |  |
| 21 | AMT_FC | 价税合计(本币) | number(23,8) | Y |  |
| 22 | TAX_DEDUCTIBLE_INDICATOR | 税额抵扣标识 | number(0/1) | Y |  |
| 23 | AMT_UNTAX_OFFSETED_TC | 已冲减无税金额(原币) | number(23,8) | Y |  |
| 24 | TAX_OFFSETED_TC | 已冲减税额(原币) | number(23,8) | Y |  |
| 25 | AMT_OFFSETED_TC | 已冲减价税合计(原币) | number(23,8) | Y |  |
| 26 | QTY_OFFSETED | 已冲减数量 | number(16,6) | Y |  |
| 27 | CLOSE_OFFSET_INDICATOR | 已冲减结束码 | number(0/1) | Y |  |
| 28 | PURCHASE_TYPE | 采购类型 | number | Y |  |
| 29 | ESTI_REVERSE_AP_EXG | 应付暂估冲回汇率 | number(18,9) | Y |  |
| 30 | ESTI_REVERSE_AP_AMT_TC | 应付暂估冲回金额(原币) | number(23,8) | Y |  |
| 31 | ESTI_REVERSE_AP_AMT_FC | 应付暂估冲回金额(本币) | number(23,8) | Y |  |
| 32 | ESTI_REVERSE_AP_EXG_LOSS_AMT | 应付暂估冲回汇兑损失 | number(23,8) | Y |  |
| 33 | PPV | 价差 | number(23,8) | Y |  |
| 34 | RECEIPT_HISTORY_AMT_TC | 入库历史成本金额(原币) | number(23,8) | Y |  |
| 35 | RECEIPT_HISTORY_AMT_FC | 入库历史成本金额(本币) | number(23,8) | Y |  |
| 36 | REMARK | 备注 | string(510) | Y |  |
| 37 | ITEM_ID | 品号 | GUID | Y |  |
| 38 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 39 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 40 | TAX_ID | 税种税率 | GUID | Y |  |
| 41 | ADJUSTMENT_DOC_D_ID | 调整单行 | GUID | Y |  |
| 42 | BUYER_ID | 采购人员 | GUID | Y |  |
| 43 | ADMIN_UNIT_ID | 采购部门 | GUID | Y |  |
| 44 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 45 | ADJUSTMENT_DOC_ID | 调整单号 | GUID | Y |  |
| 46 | ESTI_PAYABLE_OBJECT_ID | 暂估应付对象 | GUID | Y |  |
| 47 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 48 | BIN_ID | 库位 | GUID | Y |  |
| 49 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 50 | DISCOUNT_AMT_OFFSETED_TC | 已冲减折扣额原币 | number(23,8) | Y |  |
| 51 | ISSUE_INVOICE_STATUS | 传入税管状态 | number | Y |  |
| 52 | TAX_OFFSETED_FC | 已冲减税额(本币) | number(23,8) | Y |  |
| 53 | RESERVED_AMT_UNTAX_TC | 保留无税金额(原币) | number(23,8) | Y |  |
| 54 | RESERVED_TAX_TC | 保留税额(原币) | number(23,8) | Y |  |
| 55 | RESERVED_TAX_FC | 保留税额(本币) | number(23,8) | Y |  |
| 56 | EXCHANGE_LOSS_TAX | 税额汇兑损失 | number(23,8) | Y |  |
| 57 | EQUAL_TRANS_AMT_UNTAX_TC | 等价值业务无税金额(原币) | number(23,8) | Y |  |
| 58 | EQUAL_TRANS_TAX_TC | 等价值业务税额(原币) | number(23,8) | Y |  |
| 59 | EQUAL_TRANS_AMT_UNTAX_FC | 等价值业务无税金额(本币) | number(23,8) | Y |  |
| 60 | EQUAL_TRANS_TAX_FC | 等价值业务税额(本币) | number(23,8) | Y |  |
| 61 | EQUAL_TRANS_EXG | 等价值业务汇率 | number(18,9) | Y |  |
| 62 | RERAP_INDICATOR | 需处理应付暂估冲回标识 | number(0/1) | Y |  |
| 63 | INNER_SETTLEMENT_DOC_ID | 内部结算单号 | GUID | Y |  |
| 64 | INNER_SETTLEMENT_DOC_D_ID | 内部结算单序号 | GUID | Y |  |
| 65 | TO_RECEIVABLE_DOC_ID | 抛转应收单号 | GUID | Y |  |
| 66 | TO_RECEIVABLE_DOC_D_ID | 抛转应收单序号 | GUID | Y |  |
| 67 | REVERSE_SOURCE_DOC_LINE_ID | 红冲原始单据行 | GUID | Y |  |
| 68 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 69 | ApproveDate | 修改日期 | date | Y |  |
| 70 | ApproveBy | 修改人 | GUID | Y |  |
| 71 | CreateDate | 创建日期 | date | Y |  |
| 72 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 73 | ModifiedDate | 修改日期 | date | Y |  |
| 74 | CreateBy | 创建者 | GUID | Y |  |
| 75 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 76 | ModifiedBy | 修改者 | GUID | Y |  |
| 77 | Version | 版本号，不要随意更改 | binary | Y |  |
| 78 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 79 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 80 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 81 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 82 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 83 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 84 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 85 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 86 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 87 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 88 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 89 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 90 | UDF041 | 自定义字段12 | date | Y |  |
| 91 | UDF042 | 自定义字段13 | date | Y |  |
| 92 | UDF051 | 自定义字段14 | GUID | Y |  |
| 93 | UDF052 | 自定义字段15 | GUID | Y |  |
| 94 | UDF053 | 自定义字段16 | GUID | Y |  |
| 95 | UDF054 | 自定义字段17 | GUID | Y |  |
| 96 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 97 | SOURCE_ID_ROid |  | GUID | Y |  |
| 98 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 99 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 100 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 101 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 102 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 103 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 104 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 105 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 106 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 107 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 108 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 109 | SOURCE7_ID_ROid |  | GUID | Y |  |
| 110 | SOURCE8_ID_RTK |  | string(400) | Y |  |
| 111 | SOURCE8_ID_ROid |  | GUID | Y |  |
| 112 | SOURCE9_ID_RTK |  | string(400) | Y |  |
| 113 | SOURCE9_ID_ROid |  | GUID | Y |  |
| 114 | SOURCE10_ID_RTK |  | string(400) | Y |  |
| 115 | SOURCE10_ID_ROid |  | GUID | Y |  |
| 116 | PAYABLE_DOC_ID |  | GUID | Y |  |
| 117 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 118 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 119 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 120 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 121 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 122 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 123 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 124 | PROJECT_ID | 项目 | GUID | Y |  |
| 125 | SYNERGY_SETTLEMENT_GROUP | 协同结算组号 | number | Y |  |
| 126 | SOURCE11_ID_RTK |  | string(400) | Y |  |
| 127 | SOURCE11_ID_ROid |  | GUID | Y |  |
| 128 | SOURCE12_ID_RTK |  | string(400) | Y |  |
| 129 | SOURCE12_ID_ROid |  | GUID | Y |  |

### PAYABLE_DOC_INSTAL (应付单分期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYABLE_DOC_INSTAL_ID | 主键 | GUID | Y | Y |
| 3 | INSTALLMENT_NAME | 分期名称 | string(60) | Y |  |
| 4 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 5 | PAYMENT_BASE_DATE_SOURCE | 基准日来源 | number | Y |  |
| 6 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 7 | PAYMENT_DATE | 付款日 | date | Y |  |
| 8 | CASHING_DATE | 兑现日 | date | Y |  |
| 9 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 10 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 11 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 12 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 13 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 14 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 15 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 16 | ACCUM_SETTLED_AMT_TC | 累计已结算金额(原币) | number(23,8) | Y |  |
| 17 | ACCUM_UNSETTLED_AMT_TC | 累计未结算金额(原币) | number(23,8) | Y |  |
| 18 | SETTLEMENT_AMT_TC | 本次结算金额(原币) | number(23,8) | Y |  |
| 19 | SETTLEMENT_AMT_FC | 本次结算金额(本币) | number(23,8) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 22 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 23 | ApproveDate | 修改日期 | date | Y |  |
| 24 | ApproveBy | 修改人 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 50 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE_ID_ROid |  | GUID | Y |  |
| 52 | PAYABLE_DOC_ID |  | GUID | Y |  |

### PAYABLE_DOC_TAXINV (应付单税务发票)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INV_CERTIFICATE_TYPE | 发票凭证类型 | number | Y |  |
| 3 | TAX_INVOICE_NO | 税务发票号码 | string(28) | Y |  |
| 4 | PAYABLE_DOC_TAXINV_ID | 主键 | GUID | Y | Y |
| 5 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 6 | TAX_ID | 税种税率 | GUID | Y |  |
| 7 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 8 | AMT_UNTAX_FC | 无税金额(本币) | number(23,8) | Y |  |
| 9 | TAX_FC | 税额(本币) | number(23,8) | Y |  |
| 10 | AMT_FC | 价税合计(本币) | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 13 | ApproveDate | 修改日期 | date | Y |  |
| 14 | ApproveBy | 修改人 | GUID | Y |  |
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
| 40 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ID_ROid |  | GUID | Y |  |
| 42 | PAYABLE_DOC_ID |  | GUID | Y |  |

### PAYABLE_HISTORY (应付交易历史)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PAYABLE_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | LINE_TYPE | 行类型 | number | Y |  |
| 5 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 6 | CALCULATE_FLAG | 金额转换 | number | Y |  |
| 7 | TRANS_NATURE | 交易性质 | number | Y |  |
| 8 | TRANS_DATE | 记账日期 | date | Y |  |
| 9 | BOOKKEEPING_DATE | 业务日期 | date | Y |  |
| 10 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 11 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 12 | CLASSIFICATION_CODE | 分级码 | number | Y |  |
| 13 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 14 | VERIFICATION_TOTAL_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 15 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 16 | VERIFICATION_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 17 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 18 | CASH_DISCOUNT_AMT_TC | 现金折扣-原币 | number(23,8) | Y |  |
| 19 | CASH_DISCOUNT_AMT_FC | 现金折扣-本币 | number(23,8) | Y |  |
| 20 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 21 | LOSS_AMT_TC | 财务损失(原币) | number(23,8) | Y |  |
| 22 | LOSS_AMT_FC | 财务损失(本币) | number(23,8) | Y |  |
| 23 | GAIN_AMT_TC | 利得(原币) | number(23,8) | Y |  |
| 24 | GAIN_AMT_FC | 利得(本币) | number(23,8) | Y |  |
| 25 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 26 | TRANS_DOC_LINE_SEQNO | 交易单据行序号 | number | Y |  |
| 27 | TRANS_SOURCE_DOC_NO | 交易来源单号 | string(80) | Y |  |
| 28 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 29 | TRANS_DOC_ID | 交易单据类型 | GUID | Y |  |
| 30 | CURRENCY_ID | 货币 | GUID | Y |  |
| 31 | DEPOSIT_TAX_TC | 定金税额(原币) | number(23,8) | Y |  |
| 32 | DEPOSIT_TAX_FC | 定金税额(本币) | number(23,8) | Y |  |
| 33 | DEPOSIT_TAX_OFFSETED_TC | 定金税额冲减金额(原币) | number(23,8) | Y |  |
| 34 | DEPOSIT_TAX_OFFSETED_FC | 定金税额冲减金额(本币) | number(23,8) | Y |  |
| 35 | ESTI_RENP_FLAG | 月初冲回暂估标识 | number(0/1) | Y |  |
| 36 | REMARK | 备注 | string(510) | Y |  |
| 37 | REMARK2 | 行备注 | string(510) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
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
| 63 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | Owner_Org_RTK |  | string(400) | Y |  |
| 66 | Owner_Org_ROid |  | GUID | Y |  |
| 67 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 68 | SOURCE_ID_ROid |  | GUID | Y |  |
| 69 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 70 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 71 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 72 | SOURCE7_ID_ROid |  | GUID | Y |  |

### PAYABLE_NOTE (应付票据)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PAYABLE_NOTE_ID | 主键 | GUID | Y | Y |
| 4 | NOTE_NO | 票据号码 | string(60) | Y |  |
| 5 | NOTE_TYPE_ID | 票据类型 | GUID | Y |  |
| 6 | ELECTRONIC_FLAG | 电子版标识 | number(0/1) | Y |  |
| 7 | NOTE_NATURE | 票据性质 | number | Y |  |
| 8 | ISSUE_DATE | 出票日期 | date | Y |  |
| 9 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 10 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 11 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 12 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 13 | INITIALIZED_FLAG | 初始化标识 | number(0/1) | Y |  |
| 14 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 15 | SETTLEMENT_OBJECT_NAME | 结算对象名称 | string(144) | Y |  |
| 16 | DUE_DATE | 到期日 | date | Y |  |
| 17 | NON_NEGOTIABLE_FLAG | 出票人禁止转让标识 | number(0/1) | Y |  |
| 18 | FACE_CURRENCY_ID | 票面货币 | GUID | Y |  |
| 19 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 20 | FACE_AMT_TC | 票面金额(原币) | number(23,8) | Y |  |
| 21 | FACE_AMT_FC | 票面金额(本币) | number(23,8) | Y |  |
| 22 | INTEREST_BEARING_FLAG | 带息票据标识 | number(0/1) | Y |  |
| 23 | FACE_APR | 票面年利率 | number(6,5) | Y |  |
| 24 | MATURITY_AMT_TC | 到期金额(原币) | number(23,8) | Y |  |
| 25 | MATURITY_AMT_FC | 到期金额(本币) | number(23,8) | Y |  |
| 26 | THIRD_ACCEPTANCE_FLAG | 第三方承兑标识 | number(0/1) | Y |  |
| 27 | ACCEPTOR_TYPE | 承兑人类型 | number | Y |  |
| 28 | ACCEPTOR | 承兑人 | string(144) | Y |  |
| 29 | ACCEPTANCE_AGREEMENT | 承兑协议 | string(80) | Y |  |
| 30 | ACCEPTED_FLAG | 已承兑标识 | number(0/1) | Y |  |
| 31 | ACCEPTANCE_DATE | 承兑日期 | date | Y |  |
| 32 | TRANS_CONTRACT | 交易合同 | string(80) | Y |  |
| 33 | DRAWER | 出票人 | string(144) | Y |  |
| 34 | NOTE_STATUS | 票据状态 | number | Y |  |
| 35 | PREV_NOTE_STATUS | 上次票据状态 | number | Y |  |
| 36 | STATUS_TRANS_DATE | 状态业务日期 | date | Y |  |
| 37 | STATUS_BOOKKEEPING_DATE | 状态记账日期 | date | Y |  |
| 38 | PREV_STATUS_TRANS_DATE | 上次状态业务日期 | date | Y |  |
| 39 | PREV_STATUS_BOOKKEEPING_DATE | 上次状态记账日期 | date | Y |  |
| 40 | PAYMENT_CURRENCY_ID | 兑付货币 | GUID | Y |  |
| 41 | PAYING_BANK_ACCOUNT_ID | 付款行账号 | GUID | Y |  |
| 42 | PAYING_BANK_ID | 付款银行 | GUID | Y |  |
| 43 | PAYING_BANK_FULLNAME | 付款行全称 | string(144) | Y |  |
| 44 | PAYING_BANK_NO | 付款行行号 | string(40) | Y |  |
| 45 | PAYING_BANK_ADDRESS | 付款行地址 | string(510) | Y |  |
| 46 | COLLECTING_BANK_ACCOUNT_NO | 收款行账号 | string(60) | Y |  |
| 47 | COLLECTING_BANK_FULLNAME | 收款行全称 | string(144) | Y |  |
| 48 | COLLECTING_BANK_NO | 收款行行号 | string(40) | Y |  |
| 49 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 50 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 51 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 52 | OTHER_ARAP_ITEM_ID | 收付项目 | GUID | Y |  |
| 53 | CARRYING_FACE_EXG | 账面票面汇率 | number(18,9) | Y |  |
| 54 | CARRYING_FACE_AMT_TC | 账面票面金额(原币) | number(23,8) | Y |  |
| 55 | CARRYING_FACE_AMT_FC | 账面票面金额(本币) | number(23,8) | Y |  |
| 56 | CARRYING_FACE_EXG_LOSS_AMT | 账面票面汇兑损失 | number(23,8) | Y |  |
| 57 | ACCRUED_INTEREST_EXG | 已计利息汇率 | number(18,9) | Y |  |
| 58 | ACCRUED_INTEREST_AMT_TC | 已计利息金额(原币) | number(23,8) | Y |  |
| 59 | ACCRUED_INTEREST_AMT_FC | 已计利息金额(本币) | number(23,8) | Y |  |
| 60 | FI_EXPENSE_INTEREST_AMT | 已计财务费用利息支出 | number(23,8) | Y |  |
| 61 | INTEREST_EXG_LOSS_AMT | 已计利息汇兑损失 | number(23,8) | Y |  |
| 62 | CARRYING_EXG | 账面价值汇率 | number(18,9) | Y |  |
| 63 | CARRYING_AMT_TC | 账面价值金额(原币) | number(23,8) | Y |  |
| 64 | CARRYING_AMT_FC | 账面价值金额(本币) | number(23,8) | Y |  |
| 65 | CARRYING_EXG_LOSS_AMT | 账面价值汇兑损失 | number(23,8) | Y |  |
| 66 | ACCOUNTS_SYS_FLAG | 需往来系统核销标识 | number(0/1) | Y |  |
| 67 | TO_ACCOUNTS_SYS_FLAG | 已转往来系统标识 | number(0/1) | Y |  |
| 68 | ACCOUNTS_SYS_TRANSDOC_TYPE | 往来系统业务单据类型 | number | Y |  |
| 69 | LOCK_FLAG | 锁定标识 | number(0/1) | Y |  |
| 70 | REMARK | 备注 | string(510) | Y |  |
| 71 | LAST_ACT_TRANS_DATE | 最近行为业务日期 | date | Y |  |
| 72 | LAST_ACT_BOOKKEEPING_DATE | 最近行为记账日期 | date | Y |  |
| 73 | CreateDate | 创建日期 | date | Y |  |
| 74 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 75 | ModifiedDate | 修改日期 | date | Y |  |
| 76 | CreateBy | 创建者 | GUID | Y |  |
| 77 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 78 | ModifiedBy | 修改者 | GUID | Y |  |
| 79 | Attachments | 附件 | string | Y |  |
| 80 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 81 | Version | 版本号，不要随意更改 | binary | Y |  |
| 82 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 83 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 84 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 85 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 86 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 87 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 88 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 89 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 90 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 91 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 92 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 93 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 94 | UDF041 | 自定义字段12 | date | Y |  |
| 95 | UDF042 | 自定义字段13 | date | Y |  |
| 96 | UDF051 | 自定义字段14 | GUID | Y |  |
| 97 | UDF052 | 自定义字段15 | GUID | Y |  |
| 98 | UDF053 | 自定义字段16 | GUID | Y |  |
| 99 | UDF054 | 自定义字段17 | GUID | Y |  |
| 100 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 101 | ApproveDate | 修改日期 | date | Y |  |
| 102 | ApproveBy | 修改人 | GUID | Y |  |
| 103 | PrintCount | 打印次数 | number | Y |  |
| 104 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 105 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 106 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 107 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 108 | Owner_Org_RTK |  | string(400) | Y |  |
| 109 | Owner_Org_ROid |  | GUID | Y |  |
| 110 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 111 | SOURCE_ID_ROid |  | GUID | Y |  |
| 112 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 113 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 114 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 115 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 116 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 117 | SOURCE3_ID_ROid |  | GUID | Y |  |

### PAYABLE_OBJECT (应付对象档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PAYABLE_OBJECT_ID | 主键 | GUID | Y | Y |
| 4 | PAYABLES_TYPE | 应付款类型 | number | Y |  |
| 5 | CREDIT_INDICATOR | 贷项标识-应付/其他应付款 | number(0/1) | Y |  |
| 6 | DISCOUNT_ALLOWANCE_INDICATOR | 商业折扣/折让标识 | number(0/1) | Y |  |
| 7 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 8 | STD_INDICATOR | 标准预付标识 | number(0/1) | Y |  |
| 9 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 10 | TRANS_DOC_LINE_SEQNO | 交易单据行序号 | number | Y |  |
| 11 | OBJECT_TRANSDOC_NO | 应付对象-业务单据单号 | string(40) | Y |  |
| 12 | OBJECT_TRANSDOC_LINE_ID | 应付对象-业务单据行 | GUID | Y |  |
| 13 | OBJECT_INSTAL_SOURDOC_NO | 应付对象-分期源单单号 | string(40) | Y |  |
| 14 | TRANS_DATE | 业务日期 | date | Y |  |
| 15 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 16 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 17 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 18 | PAYMENT_DATE | 付款日 | date | Y |  |
| 19 | CASHING_DATE | 兑现日 | date | Y |  |
| 20 | CASH_DISCOUNT_BASE_DATE | 现金折扣基准日 | date | Y |  |
| 21 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 22 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 23 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 24 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 25 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 26 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 27 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 28 | INITIAL_AMT_TC | 应付原始金额(原币) | number(23,8) | Y |  |
| 29 | INITIAL_AMT_FC | 应付原始金额(本币) | number(23,8) | Y |  |
| 30 | ADJUSTMENT_EXG | 调整汇率 | number(18,9) | Y |  |
| 31 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 32 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 33 | TRANSFER_AMT_TC | 转销金额(原币) | number(23,8) | Y |  |
| 34 | TRANSFER_AMT_FC | 转销金额(本币) | number(23,8) | Y |  |
| 35 | VERIFICATION_AMT_TC | 已核销金额(原币) | number(23,8) | Y |  |
| 36 | VERIFICATION_AMT_FC | 已核销金额(本币) | number(23,8) | Y |  |
| 37 | BALANCE_AMT_TC | 应付余额(原币) | number(23,8) | Y |  |
| 38 | BALANCE_AMT_FC | 应付余额(本币) | number(23,8) | Y |  |
| 39 | ITEM_NAME |  | string(120) | Y |  |
| 40 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 41 | BIN_ID | 库位 | GUID | Y |  |
| 42 | ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 43 | ESTI_COST_TYPE | 存货暂估成本类型 | number | Y |  |
| 44 | ESTI_INITIAL_QTY | 存货暂估原始数量 | number(16,6) | Y |  |
| 45 | ESTI_QTY_BALANCE | 存货暂估数量余额 | number(16,6) | Y |  |
| 46 | ESTI_CST_BALANCE | 存货暂估成本余额 | number(23,8) | Y |  |
| 47 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 48 | TRANS_DOC_ID | 交易单据类型 | GUID | Y |  |
| 49 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 50 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 51 | CURRENCY_ID | 货币 | GUID | Y |  |
| 52 | ITEM_ID | 品号(作废) | GUID | Y |  |
| 53 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 54 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 55 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 56 | REMARK | 备注 | string(510) | Y |  |
| 57 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 58 | DEPOSIT_TAX_INITIAL_TC | 定金税额原始金额(原币) | number(23,8) | Y |  |
| 59 | DEPOSIT_TAX_INITIAL_FC | 定金税额原始金额(本币) | number(23,8) | Y |  |
| 60 | DEPOSIT_TAX_OFFSETED_TC | 定金税额已冲减金额(原币) | number(23,8) | Y |  |
| 61 | DEPOSIT_TAX_OFFSETED_FC | 定金税额已冲减金额(本币) | number(23,8) | Y |  |
| 62 | DEPOSIT_TAX_BALANCE_TC | 定金税额余额(原币) | number(23,8) | Y |  |
| 63 | DEPOSIT_TAX_BALANCE_FC | 定金税额余额(本币) | number(23,8) | Y |  |
| 64 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 65 | PAYMENT_BASE_DATE_SOURCE | 基准日来源 | number | Y |  |
| 66 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 67 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 68 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 69 | SUPPLIER_ORDER_NO | 供应商单号 | string(510) | Y |  |
| 70 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 71 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 72 | OBJECT_TRANSDOC_ID | 应付对象-业务单据类型 | GUID | Y |  |
| 73 | OBJECT_TRANSDOC_DATE | 应付对象-业务单据日期 | date | Y |  |
| 74 | REF61_DOC_ID | 参考单据1_类型 | GUID | Y |  |
| 75 | REF61_DOC_NO | 参考单据1_单号 | string(80) | Y |  |
| 76 | REF61_DOC_DATE | 参考单据1_日期 | date | Y |  |
| 77 | REF62_DOC_ID | 参考单据2_类型 | GUID | Y |  |
| 78 | REF62_DOC_NO | 参考单据2_单号 | string(80) | Y |  |
| 79 | REF62_DOC_DATE | 参考单据2_日期 | date | Y |  |
| 80 | REMARK2 | 行备注 | string(510) | Y |  |
| 81 | PROJECT_ID | 项目 | GUID | Y |  |
| 82 | CreateDate | 创建日期 | date | Y |  |
| 83 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 84 | ModifiedDate | 修改日期 | date | Y |  |
| 85 | CreateBy | 创建者 | GUID | Y |  |
| 86 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 87 | ModifiedBy | 修改者 | GUID | Y |  |
| 88 | Attachments | 附件 | string | Y |  |
| 89 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 90 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 91 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 92 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 93 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 94 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 95 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 96 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 97 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 98 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 99 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 100 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 101 | UDF041 | 自定义字段12 | date | Y |  |
| 102 | UDF042 | 自定义字段13 | date | Y |  |
| 103 | UDF051 | 自定义字段14 | GUID | Y |  |
| 104 | UDF052 | 自定义字段15 | GUID | Y |  |
| 105 | UDF053 | 自定义字段16 | GUID | Y |  |
| 106 | UDF054 | 自定义字段17 | GUID | Y |  |
| 107 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 108 | Version | 版本号，不要随意更改 | binary | Y |  |
| 109 | Owner_Org_RTK |  | string(400) | Y |  |
| 110 | Owner_Org_ROid |  | GUID | Y |  |
| 111 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 112 | SOURCE_ID_ROid |  | GUID | Y |  |
| 113 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 114 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 115 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 116 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 117 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 118 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 119 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 120 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 121 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 122 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 123 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 124 | SOURCE7_ID_ROid |  | GUID | Y |  |
| 125 | SOURCE8_ID_RTK |  | string(400) | Y |  |
| 126 | SOURCE8_ID_ROid |  | GUID | Y |  |
| 127 | SOURCE10_ID_RTK |  | string(400) | Y |  |
| 128 | SOURCE10_ID_ROid |  | GUID | Y |  |
| 129 | SOURCE11_ID_RTK |  | string(400) | Y |  |
| 130 | SOURCE11_ID_ROid |  | GUID | Y |  |
| 131 | SOURCE61_ID_RTK |  | string(400) | Y |  |
| 132 | SOURCE61_ID_ROid |  | GUID | Y |  |
| 133 | SOURCE611_ID_RTK |  | string(400) | Y |  |
| 134 | SOURCE611_ID_ROid |  | GUID | Y |  |
| 135 | SOURCE62_ID_RTK |  | string(400) | Y |  |
| 136 | SOURCE62_ID_ROid |  | GUID | Y |  |
| 137 | SOURCE621_ID_RTK |  | string(400) | Y |  |
| 138 | SOURCE621_ID_ROid |  | GUID | Y |  |
| 139 | DEPOSIT_INDICATOR | 订金标识 | number(0/1) | Y |  |
| 140 | OFFSET_DEPOSIT_INDICATOR | 订金冲减标识 | number(0/1) | Y |  |

### PAYABLE_OBJECT_CHANGE (应付对象变更历史)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | PAYABLE_OBJECT_CHANGE_ID | 主键 | GUID | Y | Y |
| 5 | PAYABLE_OBJECT_ID | 应付对象 | GUID | Y |  |
| 6 | CHANGE_NATURE | 变更性质 | number | Y |  |
| 7 | CHANGE_TYPE | 变更类型 | number | Y |  |
| 8 | CHANGE_DATE | 变更日期 | date | Y |  |
| 9 | CHANGE_USER_ID | 变更人员 | GUID | Y |  |
| 10 | CHANGE_REASON | 变更原因 | string(510) | Y |  |
| 11 | CHANGE_AMT_TC | 变更金额(原币) | number(23,8) | Y |  |
| 12 | PAYMENT_BASE_DATE_SOURCE | 基准日来源 | number | Y |  |
| 13 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 14 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 15 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 16 | PAYMENT_DATE | 付款日 | date | Y |  |
| 17 | CASHING_DATE | 兑现日 | date | Y |  |
| 18 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 19 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 20 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 21 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 22 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 23 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Attachments | 附件 | string | Y |  |
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
| 49 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | Owner_Org_RTK |  | string(400) | Y |  |
| 55 | Owner_Org_ROid |  | GUID | Y |  |
| 56 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 57 | SOURCE_ID_ROid |  | GUID | Y |  |
| 58 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 60 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 62 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 63 | SOURCE4_ID_ROid |  | GUID | Y |  |