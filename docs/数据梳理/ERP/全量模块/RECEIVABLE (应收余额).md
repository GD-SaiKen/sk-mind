---
module: "RECEIVABLE"
name_zh: "应收余额"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 9
columns: 783
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52

---

# RECEIVABLE (应收余额)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 9 | Columns: 783

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

- **RECEIVABLE_BALANCE**
- **RECEIVABLE_DOC**
- **RECEIVABLE_DOC_D**
- **RECEIVABLE_DOC_INSTAL**
- **RECEIVABLE_DOC_TAXINV**
- **RECEIVABLE_HISTORY**
- **RECEIVABLE_NOTE**
- **RECEIVABLE_OBJECT**
- **RECEIVABLE_OBJECT_CHANGE**

---


---


> Tables: 9

### RECEIVABLE_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | RECEIVABLE_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | OPENING_RECEIVABLE_AMT_TC | 应收期初余额(原币) | number(23,8) | Y |  |
| 8 | OPENING_RECEIVABLE_AMT_FC | 应收期初余额(本币) | number(23,8) | Y |  |
| 9 | INITIAL_AMT_TC | 应收原始金额-本期应收发生额(原币) | number(23,8) | Y |  |
| 10 | INITIAL_AMT_FC | 应收原始金额-本期应收发生额(本币) | number(23,8) | Y |  |
| 11 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 12 | TRANSFER_AMT_TC | 本期转销金额(原币) | number(23,8) | Y |  |
| 13 | TRANSFER_AMT_FC | 本期转销金额(本币) | number(23,8) | Y |  |
| 14 | BAD_DEBT_AMT_TC | 本期坏账金额(原币) | number(23,8) | Y |  |
| 15 | BAD_DEBT_AMT_FC | 本期坏账金额(本币) | number(23,8) | Y |  |
| 16 | RECOVERY_AMT_TC | 本期坏账收回金额(原币) | number(23,8) | Y |  |
| 17 | RECOVERY_AMT_FC | 本期坏账收回金额(本币) | number(23,8) | Y |  |
| 18 | VERIFICATION_AMT_TC | 本期已核销金额(原币) | number(23,8) | Y |  |
| 19 | VERIFICATION_AMT_FC | 本期已核销金额(本币) | number(23,8) | Y |  |
| 20 | OPENING_PROVISION_AMT | 坏账准备期初余额 | number(23,8) | Y |  |
| 21 | PROVISION_ADDED_AMT | 本期坏账准备-补提金额 | number(23,8) | Y |  |
| 22 | PROVISION_BAD_AMT | 本期坏账准备-坏账金额 | number(23,8) | Y |  |
| 23 | PROVISION_RECOVERY_AMT | 本期坏账准备-坏账收回金额 | number(23,8) | Y |  |
| 24 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 25 | DEPOSIT_TAX_OPENING_TC | 定金税额期初余额(原币) | number(23,8) | Y |  |
| 26 | DEPOSIT_TAX_OPENING_FC | 定金税额期初余额(本币) | number(23,8) | Y |  |
| 27 | DEPOSIT_TAX_INITIAL_TC | 定金税额原始金额-本期发生额(原币) | number(23,8) | Y |  |
| 28 | DEPOSIT_TAX_INITIAL_FC | 定金税额原始金额-本期发生额(本币) | number(23,8) | Y |  |
| 29 | DEPOSIT_TAX_OFFSETED_TC | 定金税额本期已冲减金额(原币) | number(23,8) | Y |  |
| 30 | DEPOSIT_TAX_OFFSETED_FC | 定金税额本期已冲减金额(本币) | number(23,8) | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Attachments | 附件 | string | Y |  |
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
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |

### RECEIVABLE_DOC - 应收单

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | RECEIVABLE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 12 | TAX_CONTROL_INDICATOR | 税务发票控制 | number(0/1) | Y |  |
| 13 | TRANS_TYPE | 业务类型 | number | Y |  |
| 14 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | PAYMENT_DATE | 付款日 | date | Y |  |
| 17 | CASHING_DATE | 兑现日 | date | Y |  |
| 18 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 19 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 20 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 21 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 22 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 23 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 24 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 25 | AMT_UNTAX_TC | 无税金额合计(原币) | number(23,8) | Y |  |
| 26 | TAX_TC | 税额合计(原币) | number(23,8) | Y |  |
| 27 | AMT_UNTAX_FC | 无税金额合计(功能币) | number(23,8) | Y |  |
| 28 | TAX_FC | 税额合计(功能币) | number(23,8) | Y |  |
| 29 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 30 | INSTALLMENT_SOURDOC_TYPE | 分期源单类型 | number | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | TRANS_NATURE | 业务性质 | number | Y |  |
| 33 | DETAIL_TRANS_TYPE | 明细业务类型 | number | Y |  |
| 34 | INNER_SYNERGY_INDICATOR | 内部协同标识(作废) | number(0/1) | Y |  |
| 35 | TAX_INVOICE_TYPE | 税务发票类型 | number | Y |  |
| 36 | ISSUE_INVOICE_STATUS | 传入税管状态 | number | Y |  |
| 37 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 38 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 39 | VAT_INDICATOR | VAT标识 | number(0/1) | Y |  |
| 40 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 41 | INNER_SETTLEMENT_DOC_ID | 内部结算单号 | GUID | Y |  |
| 42 | COLLECTION_DOC_ID | 现结收款单号 | GUID | Y |  |
| 43 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 44 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 45 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 46 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 47 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 48 | CURRENCY_ID | 货币 | GUID | Y |  |
| 49 | REVERSE_SOURCE_DOC_ID | 红冲原始单号 | GUID | Y |  |
| 50 | REVERSE_DOC_ID | 红冲单号 | GUID | Y |  |
| 51 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 52 | ORDER_CUSTOMER_ID | 订货客户 | GUID | Y |  |
| 53 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 54 | TAX_ID | 税种税率 | GUID | Y |  |
| 55 | GLOB_REVENUE_JE_INDICATOR | 已生成运营账簿收入分录 | number(0/1) | Y |  |
| 56 | GLOB_COST_JE_INDICATOR | 已生成运营账簿成本分录 | number(0/1) | Y |  |
| 57 | GLOB_REVENUE_JE_ID | 运营账簿收入分录 | GUID | Y |  |
| 58 | GLOB_COST_JE_ID | 运营账簿成本分录 | GUID | Y |  |
| 59 | GLMB_REVENUE_JE_INDICATOR | 已生成管理账簿收入分录 | number(0/1) | Y |  |
| 60 | GLMB_COST_JE_INDICATOR | 已生成管理账簿成本分录 | number(0/1) | Y |  |
| 61 | GLMB_REVENUE_JE_ID | 管理账簿收入分录 | GUID | Y |  |
| 62 | GLMB_COST_JE_ID | 管理账簿成本分录 | GUID | Y |  |
| 63 | REVERSE_STATUS | 红冲状态 | number | Y |  |
| 64 | TAX_INVOICE_SOURCE | 税务发票来源 | number | Y |  |
| 65 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 66 | TAX_INVOICE_CATEGORY_DISC_ID | 折让税务发票种类 | GUID | Y |  |
| 67 | INSTAL_AMT_TC | 分期结算金额(原币) | number(23,8) | Y |  |
| 68 | INSTAL_AMT_FC | 分期结算金额(本币) | number(23,8) | Y |  |
| 69 | SETTLEMENT_PATH_TYPE | 结算路径类型 | number | Y |  |
| 70 | FROM_PAYABLE_DOC_ID | 来源应付单 | GUID | Y |  |
| 71 | TO_PAYABLE_DOC_ID | 抛转应付单 | GUID | Y |  |
| 72 | SYNERGY_SETTLEMENT_STATUS | 协同抛转状态 | number | Y |  |
| 73 | TAX_MODE | 税额计算方式 | string(40) | Y |  |
| 74 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 75 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 76 | SETTLEMENT_NO | 结算号 | string(60) | Y |  |
| 77 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 78 | PROJECT_ID | 项目 | GUID | Y |  |
| 79 | CreateDate | 创建日期 | date | Y |  |
| 80 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 81 | ModifiedDate | 修改日期 | date | Y |  |
| 82 | CreateBy | 创建者 | GUID | Y |  |
| 83 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 84 | ModifiedBy | 修改者 | GUID | Y |  |
| 85 | Attachments | 附件 | string | Y |  |
| 86 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 87 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 88 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 89 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 90 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 91 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 92 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 93 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 94 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 95 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 96 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 97 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 98 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 99 | UDF041 | 自定义字段12 | date | Y |  |
| 100 | UDF042 | 自定义字段13 | date | Y |  |
| 101 | UDF051 | 自定义字段14 | GUID | Y |  |
| 102 | UDF052 | 自定义字段15 | GUID | Y |  |
| 103 | UDF053 | 自定义字段16 | GUID | Y |  |
| 104 | UDF054 | 自定义字段17 | GUID | Y |  |
| 105 | PrintCount | 打印次数 | number | Y |  |
| 106 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 107 | ApproveDate | 修改日期 | date | Y |  |
| 108 | ApproveBy | 修改人 | GUID | Y |  |
| 109 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 110 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 111 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 112 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 113 | Version | 版本号，不要随意更改 | binary | Y |  |
| 114 | Owner_Org_RTK |  | string(400) | Y |  |
| 115 | Owner_Org_ROid |  | GUID | Y |  |
| 116 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 117 | SOURCE_ID_ROid |  | GUID | Y |  |
| 118 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 119 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 120 | SYNERGY_ID_RTK |  | string(400) | Y |  |
| 121 | SYNERGY_ID_ROid |  | GUID | Y |  |
| 122 | SYNERGY_D_ID_RTK |  | string(400) | Y |  |
| 123 | SYNERGY_D_ID_ROid |  | GUID | Y |  |
| 124 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 125 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 126 | R_INNER_SETTLEMENT_FLAG | 需内部结算标识 | number(0/1) | Y |  |

### RECEIVABLE_DOC_D - 应收单单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | RECEIVABLE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 应收来源单据类型 | number | Y |  |
| 4 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 5 | ITEM_NAME | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 8 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 9 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 10 | VAT_INDICATOR | 增值税 | number(0/1) | Y |  |
| 11 | PRICE | 商业折扣前单价 | number(23,8) | Y |  |
| 12 | DISCOUNT_RATE | 商业折扣率 | number(5,4) | Y |  |
| 13 | DISCOUNTED_PRICE_UNTAX | 折扣后无税单价 | number(23,8) | Y |  |
| 14 | DISCOUNTED_PRICE_INTAX | 折扣后含税单价 | number(23,8) | Y |  |
| 15 | AMT_UNTAX_TC | 无税金额(原币) | number(23,8) | Y |  |
| 16 | TAX_TC | 税额(原币) | number(23,8) | Y |  |
| 17 | AMT_TC | 价税合计(原币) | number(23,8) | Y |  |
| 18 | AMT_UNTAX_FC | 无税金额(本币) | number(23,8) | Y |  |
| 19 | TAX_FC | 税额(本币) | number(23,8) | Y |  |
| 20 | AMT_FC | 价税合计(本币) | number(23,8) | Y |  |
| 21 | AMT_UNTAX_OFFSETED_TC | 已冲减无税金额(原币) | number(23,8) | Y |  |
| 22 | TAX_OFFSETED_TC | 已冲减税额(原币) | number(23,8) | Y |  |
| 23 | AMT_OFFSETED_TC | 已冲减价税合计(原币) | number(23,8) | Y |  |
| 24 | QTY_OFFSETED | 已冲减数量 | number(16,6) | Y |  |
| 25 | CLOSE_OFFSET_INDICATOR | 已冲减结束码 | number(0/1) | Y |  |
| 26 | SALES_TYPE | 销售类型 | number | Y |  |
| 27 | DISCOUNT_UNTAX_AMT_TC | 商业无税折扣额（原币） | number(23,8) | Y |  |
| 28 | DISCOUNT_INTAX_AMT_TC | 商业含税折扣额（原币） | number(23,8) | Y |  |
| 29 | DISCOUNT_UNTAX_AMT_FC | 商业无税折扣额（本币） | number(23,8) | Y |  |
| 30 | DISCOUNT_INTAX_AMT_FC | 商业含税折扣额（本币） | number(23,8) | Y |  |
| 31 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 32 | SALES_ID | 业务人员 | GUID | Y |  |
| 33 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 34 | ITEM_ID | 品号 | GUID | Y |  |
| 35 | TAX_ID | 税种税率 | GUID | Y |  |
| 36 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 37 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 38 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 39 | DISC_UNTAX_AMT_OFFSETED_TC | 已冲减商业无税折扣额(原币) | number(23,8) | Y |  |
| 40 | DISC_INTAX_AMT_OFFSETED_TC | 已冲减商业含税折扣额(原币) | number(23,8) | Y |  |
| 41 | EQUAL_TRANS_AMT_UNTAX_TC | 等价值业务无税金额(原币) | number(23,8) | Y |  |
| 42 | EQUAL_TRANS_TAX_TC | 等价值业务税额(原币) | number(23,8) | Y |  |
| 43 | EQUAL_TRANS_AMT_TC | 等价值业务价税合计(原币) | number(23,8) | Y |  |
| 44 | EQUAL_TRANS_AMT_UNTAX_FC | 等价值业务无税金额(本币) | number(23,8) | Y |  |
| 45 | EQUAL_TRANS_TAX_FC | 等价值业务税额(本币) | number(23,8) | Y |  |
| 46 | EQUAL_TRANS_AMT_FC | 等价值业务价税合计(本币) | number(23,8) | Y |  |
| 47 | EQUAL_TRANS_DISC_UNTAX_AMT_TC | 等价值业务商业无税折扣额(原币) | number(23,8) | Y |  |
| 48 | EQUAL_TRANS_DISC_INTAX_AMT_TC | 等价值业务商业含税折扣额(原币) | number(23,8) | Y |  |
| 49 | EQUAL_TRANS_DISC_UNTAX_AMT_FC | 等价值业务商业无税折扣额(本币) | number(23,8) | Y |  |
| 50 | EQUAL_TRANS_DISC_INTAX_AMT_FC | 等价值业务商业含税折扣额(本币) | number(23,8) | Y |  |
| 51 | EQUAL_TRANS_EXG | 等价值业务汇率 | number(18,9) | Y |  |
| 52 | REMARK | 备注 | string(510) | Y |  |
| 53 | ISSUE_INVOICE_STATUS | 传入税管状态 | number | Y |  |
| 54 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 55 | TAX_OFFSETED_FC | 未结算销货预冲减无税金额(原币) | number(23,8) | Y |  |
| 56 | RESERVED_AMT_UNTAX_TC | 未结算销货预冲减税额(原币) | number(23,8) | Y |  |
| 57 | RESERVED_TAX_TC | 保留税额(原币) | number(23,8) | Y |  |
| 58 | EXCHANGE_LOSS_TAX | 税额汇兑损失 | number(23,8) | Y |  |
| 59 | RESERVED_TAX_FC | 保留税额(本币) | number(23,8) | Y |  |
| 60 | INNER_SETTLEMENT_DOC_ID | 内部结算单号 | GUID | Y |  |
| 61 | INNER_SETTLEMENT_DOC_D_ID | 内部结算单序号 | GUID | Y |  |
| 62 | TO_PAYABLE_DOC_ID | 抛转应付单号 | GUID | Y |  |
| 63 | TO_PAYABLE_DOC_D_ID | 抛转应付单序号 | GUID | Y |  |
| 64 | REVERSE_SOURCE_DOC_LINE_ID | 红冲原始单据行 | GUID | Y |  |
| 65 | PROJECT_ID | 项目 | GUID | Y |  |
| 66 | CreateDate | 创建日期 | date | Y |  |
| 67 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 68 | ModifiedDate | 修改日期 | date | Y |  |
| 69 | CreateBy | 创建者 | GUID | Y |  |
| 70 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 71 | ModifiedBy | 修改者 | GUID | Y |  |
| 72 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 73 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 74 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 75 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 76 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 77 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 78 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 79 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 80 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 81 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 82 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 83 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 84 | UDF041 | 自定义字段12 | date | Y |  |
| 85 | UDF042 | 自定义字段13 | date | Y |  |
| 86 | UDF051 | 自定义字段14 | GUID | Y |  |
| 87 | UDF052 | 自定义字段15 | GUID | Y |  |
| 88 | UDF053 | 自定义字段16 | GUID | Y |  |
| 89 | UDF054 | 自定义字段17 | GUID | Y |  |
| 90 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 91 | ApproveDate | 修改日期 | date | Y |  |
| 92 | ApproveBy | 修改人 | GUID | Y |  |
| 93 | Version | 版本号，不要随意更改 | binary | Y |  |
| 94 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 95 | SOURCE_ID_ROid |  | GUID | Y |  |
| 96 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 97 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 98 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 99 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 100 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 101 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 102 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 103 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 104 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 105 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 106 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 107 | SOURCE7_ID_ROid |  | GUID | Y |  |
| 108 | SOURCE8_ID_RTK |  | string(400) | Y |  |
| 109 | SOURCE8_ID_ROid |  | GUID | Y |  |
| 110 | SOURCE9_ID_RTK |  | string(400) | Y |  |
| 111 | SOURCE9_ID_ROid |  | GUID | Y |  |
| 112 | SOURCE10_ID_RTK |  | string(400) | Y |  |
| 113 | SOURCE10_ID_ROid |  | GUID | Y |  |
| 114 | RECEIVABLE_DOC_ID |  | GUID | Y |  |
| 115 | SYNERGY_SETTLEMENT_GROUP | 协同结算组号 | number | Y |  |
| 116 | SOURCE11_ID_RTK |  | string(400) | Y |  |
| 117 | SOURCE11_ID_ROid |  | GUID | Y |  |
| 118 | SOURCE12_ID_RTK |  | string(400) | Y |  |
| 119 | SOURCE12_ID_ROid |  | GUID | Y |  |

### RECEIVABLE_DOC_INSTAL - 应收单分期

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | RECEIVABLE_DOC_INSTAL_ID | 主键 | GUID | Y | Y |
| 3 | INSTALLMENT_NAME | 分期名称 | string(60) | Y |  |
| 4 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 5 | SETTLEMENT_AMT_TC | 结算金额(原币) | number(23,8) | Y |  |
| 6 | SETTLEMENT_AMT_FC | 结算金额(本币) | number(23,8) | Y |  |
| 7 | PAYMENT_BASE_DATE_SOURCE | 基准日来源 | number | Y |  |
| 8 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 9 | PAYMENT_DATE | 付款日 | date | Y |  |
| 10 | CASHING_DATE | 兑现日 | date | Y |  |
| 11 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 12 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 13 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 14 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 15 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 16 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 17 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 18 | ACCUM_SETTLED_AMT_TC | 累计已结算金额(原币) | number(23,8) | Y |  |
| 19 | ACCUM_UNSETTLED_AMT_TC | 累计未结算金额(原币) | number(23,8) | Y |  |
| 20 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 51 | SOURCE_ID_ROid |  | GUID | Y |  |
| 52 | RECEIVABLE_DOC_ID |  | GUID | Y |  |

### RECEIVABLE_DOC_TAXINV - 应收单税务发票

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | RECEIVABLE_DOC_TAXINV_ID | 主键 | GUID | Y | Y |
| 3 | TAX_INVOICE_NO | 税务发票号码 | string(28) | Y |  |
| 4 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 5 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 6 | REVERSE_DOC_ID | 主键 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | TW_TAXREGISTRATION_ID | 销售营业人 | GUID | Y |  |
| 9 | TW_INVOICE_BOOK_D_ID | 税务发票簿 | GUID | Y |  |
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
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 39 | SOURCE_ID_ROid |  | GUID | Y |  |
| 40 | RECEIVABLE_DOC_ID |  | GUID | Y |  |

### RECEIVABLE_HISTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | RECEIVABLE_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | LINE_TYPE | 行类型 | number | Y |  |
| 5 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 6 | CALCULATE_FLAG | 金额转换 | number | Y |  |
| 7 | PROVISION_TYPE | 坏账准备类型 | number | Y |  |
| 8 | TRANS_NATURE | 交易性质 | number | Y |  |
| 9 | TRANS_DATE | 业务日期 | date | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 12 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 13 | CLASSIFICATION_CODE | 分级码 | number | Y |  |
| 14 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 15 | VERIFICATION_TOTAL_AMT_TC | 核销金额合计(原币) | number(23,8) | Y |  |
| 16 | VERIFICATION_TOTAL_AMT_FC | 核销金额合计(本币) | number(23,8) | Y |  |
| 17 | VERIFICATION_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 18 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 19 | CASH_DISCOUNT_AMT_TC | 现金折扣(原币) | number(23,8) | Y |  |
| 20 | CASH_DISCOUNT_AMT_FC | 现金折扣(本币) | number(23,8) | Y |  |
| 21 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 22 | LOSS_AMT_TC | 财务损失(原币) | number(23,8) | Y |  |
| 23 | LOSS_AMT_FC | 财务损失(本币) | number(23,8) | Y |  |
| 24 | GAIN_AMT_TC | 利得(原币) | number(23,8) | Y |  |
| 25 | GAIN_AMT_FC | 利得(本币) | number(23,8) | Y |  |
| 26 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 27 | TRANS_DOC_LINE_SEQNO | 交易单据行序号 | number | Y |  |
| 28 | TRANS_SOURCE_DOC_NO | 交易来源单号 | string(80) | Y |  |
| 29 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
| 30 | TRANS_DOC_ID | 主键 | GUID | Y |  |
| 31 | CURRENCY_ID | 货币 | GUID | Y |  |
| 32 | DEPOSIT_TAX_TC | 定金税额(原币) | number(23,8) | Y |  |
| 33 | DEPOSIT_TAX_FC | 定金税额(本币) | number(23,8) | Y |  |
| 34 | DEPOSIT_TAX_OFFSETED_TC | 定金税额冲减金额(原币) | number(23,8) | Y |  |
| 35 | DEPOSIT_TAX_OFFSETED_FC | 定金税额冲减金额(本币) | number(23,8) | Y |  |
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

### RECEIVABLE_NOTE - 应收票据

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | RECEIVABLE_NOTE_ID | 主键 | GUID | Y | Y |
| 4 | NOTE_TYPE_ID | 票据类型 | GUID | Y |  |
| 5 | NOTE_NO | 票据号码 | string(60) | Y |  |
| 6 | ELECTRONIC_FLAG | 电子版标识 | number(0/1) | Y |  |
| 7 | NOTE_NATURE | 票据性质 | number | Y |  |
| 8 | TRANS_DATE | 收票日期 | date | Y |  |
| 9 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 10 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 11 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 12 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 13 | INITIALIZED_FLAG | 初始化标识 | number(0/1) | Y |  |
| 14 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 15 | SETTLEMENT_OBJECT_NAME | 结算对象名称 | string(144) | Y |  |
| 16 | ISSUE_DATE | 出票日期 | date | Y |  |
| 17 | DUE_DATE | 到期日 | date | Y |  |
| 18 | FACE_CURRENCY_ID | 票面货币 | GUID | Y |  |
| 19 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 20 | FACE_AMT_TC | 票面金额(原币) | number(23,8) | Y |  |
| 21 | FACE_AMT_FC | 票面金额(本币) | number(23,8) | Y |  |
| 22 | INTEREST_BEARING_FLAG | 带息票据标识 | number(0/1) | Y |  |
| 23 | FACE_APR | 票面年利率 | number(6,5) | Y |  |
| 24 | MATURITY_AMT_TC | 到期金额(原币) | number(23,8) | Y |  |
| 25 | MATURITY_AMT_FC | 到期金额(本币) | number(23,8) | Y |  |
| 26 | ACCEPTOR | 承兑人 | string(144) | Y |  |
| 27 | DRAWER | 出票人 | string(144) | Y |  |
| 28 | ACCEPTANCE_AGREEMENT | 承兑协议 | string(80) | Y |  |
| 29 | TRANS_CONTRACT | 交易合同 | string(80) | Y |  |
| 30 | NOTE_STATUS | 票据状态 | number | Y |  |
| 31 | PREV_NOTE_STATUS | 上次票据状态 | number | Y |  |
| 32 | NOTE_STATUS_DETAIL | 票据状态明细 | number | Y |  |
| 33 | PREV_NOTE_STATUS_DETAIL | 上次票据状态明细 | number | Y |  |
| 34 | STATUS_TRANS_DATE | 状态业务日期 | date | Y |  |
| 35 | STATUS_BOOKKEEPING_DATE | 状态记账日期 | date | Y |  |
| 36 | PREV_STATUS_TRANS_DATE | 上次状态业务日期 | date | Y |  |
| 37 | PREV_STATUS_BOOKKEEPING_DATE | 上次状态记账日期 | date | Y |  |
| 38 | PAYING_BANK_ACCOUNT_NO | 付款行账号 | string(60) | Y |  |
| 39 | PAYING_BANK_FULLNAME | 付款行全称 | string(144) | Y |  |
| 40 | PAYING_BANK_NO | 付款行行号 | string(40) | Y |  |
| 41 | PAYING_BANK_ADDRESS | 付款行地址 | string(510) | Y |  |
| 42 | PAYMENT_CURRENCY_ID | 兑付货币 | GUID | Y |  |
| 43 | COLLECTING_BANK_ACCOUNT_ID | 收款行账号 | GUID | Y |  |
| 44 | COLLECTING_BANK_FULLNAME | 收款行全称 | string(144) | Y |  |
| 45 | COLLECTING_BANK_NO | 收款行行号 | string(40) | Y |  |
| 46 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 47 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 48 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 49 | OTHER_ARAP_ITEM_ID | 收付项目 | GUID | Y |  |
| 50 | PLEDGE_DATE | 质押日期 | date | Y |  |
| 51 | PLEDGEE | 质权人 | string(144) | Y |  |
| 52 | PLEDGE_RESCISSION_DATE | 质押解除日期 | date | Y |  |
| 53 | CARRYING_FACE_EXG | 账面票面汇率 | number(18,9) | Y |  |
| 54 | CARRYING_FACE_AMT_TC | 账面票面金额(原币) | number(23,8) | Y |  |
| 55 | CARRYING_FACE_AMT_FC | 账面票面金额(本币) | number(23,8) | Y |  |
| 56 | CARRYING_FACE_EXG_LOSS_AMT | 账面票面汇兑损失 | number(23,8) | Y |  |
| 57 | ACCRUED_INTEREST_EXG | 已计利息汇率 | number(18,9) | Y |  |
| 58 | ACCRUED_INTEREST_AMT_TC | 已计利息金额(原币) | number(23,8) | Y |  |
| 59 | ACCRUED_INTEREST_AMT_FC | 已计利息金额(本币) | number(23,8) | Y |  |
| 60 | FI_EXPENSE_INTEREST_AMT | 已计财务费用利息收入 | number(23,8) | Y |  |
| 61 | INTEREST_EXG_LOSS_AMT | 已计利息汇兑损失 | number(23,8) | Y |  |
| 62 | CARRYING_EXG | 账面价值汇率 | number(18,9) | Y |  |
| 63 | CARRYING_AMT_TC | 账面价值金额(原币) | number(23,8) | Y |  |
| 64 | CARRYING_AMT_FC | 账面价值金额(本币) | number(23,8) | Y |  |
| 65 | CARRYING_EXG_LOSS_AMT | 账面价值汇兑损失 | number(23,8) | Y |  |
| 66 | ACCOUNTS_SYS_FLAG | 需往来系统核销标识 | number(0/1) | Y |  |
| 67 | TO_ACCOUNTS_SYS_FLAG | 已转往来系统标识 | number(0/1) | Y |  |
| 68 | ACCOUNTS_SYS_TRANSDOC_TYPE | 往来系统业务单据类型 | number | Y |  |
| 69 | LOCK_FLAG | 锁定标识 | number(0/1) | Y |  |
| 70 | PLEDGE_REMARK | 质押备注 | string(510) | Y |  |
| 71 | PLEDGE_RESCISSION_REMARK | 质押解除备注 | string(510) | Y |  |
| 72 | REMARK | 备注 | string(510) | Y |  |
| 73 | LAST_ACT_TRANS_DATE | 最近行为业务日期 | date | Y |  |
| 74 | LAST_ACT_BOOKKEEPING_DATE | 最近行为记账日期 | date | Y |  |
| 75 | CreateDate | 创建日期 | date | Y |  |
| 76 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 77 | ModifiedDate | 修改日期 | date | Y |  |
| 78 | CreateBy | 创建者 | GUID | Y |  |
| 79 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 80 | ModifiedBy | 修改者 | GUID | Y |  |
| 81 | Attachments | 附件 | string | Y |  |
| 82 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 83 | Version | 版本号，不要随意更改 | binary | Y |  |
| 84 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 85 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 86 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 87 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 88 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 89 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 90 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 91 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 92 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 93 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 94 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 95 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 96 | UDF041 | 自定义字段12 | date | Y |  |
| 97 | UDF042 | 自定义字段13 | date | Y |  |
| 98 | UDF051 | 自定义字段14 | GUID | Y |  |
| 99 | UDF052 | 自定义字段15 | GUID | Y |  |
| 100 | UDF053 | 自定义字段16 | GUID | Y |  |
| 101 | UDF054 | 自定义字段17 | GUID | Y |  |
| 102 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 103 | ApproveDate | 修改日期 | date | Y |  |
| 104 | ApproveBy | 修改人 | GUID | Y |  |
| 105 | PrintCount | 打印次数 | number | Y |  |
| 106 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 107 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 108 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 109 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 110 | Owner_Org_RTK |  | string(400) | Y |  |
| 111 | Owner_Org_ROid |  | GUID | Y |  |
| 112 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 113 | SOURCE_ID_ROid |  | GUID | Y |  |
| 114 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 115 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 116 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 117 | SOURCE3_ID_ROid |  | GUID | Y |  |

### RECEIVABLE_OBJECT - 应收对象档

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | RECEIVABLE_OBJECT_ID | 主键 | GUID | Y | Y |
| 4 | RECEIVABLES_TYPE | 应收款类型 | number | Y |  |
| 5 | CREDIT_INDICATOR | 贷项标识-应收/其他应收款 | number(0/1) | Y |  |
| 6 | DISCOUNT_ALLOWANCE_INDICATOR | 商业折扣/折让标识 | number(0/1) | Y |  |
| 7 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 8 | STD_INDICATOR | 标准预收标识 | number(0/1) | Y |  |
| 9 | OBJECT_TRANSDOC_LINE_ID | 应收对象-业务单据行 | GUID | Y |  |
| 10 | TRANS_DATE | 业务日期 | date | Y |  |
| 11 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 12 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 13 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 14 | PAYMENT_DATE | 付款日 | date | Y |  |
| 15 | CASHING_DATE | 兑现日 | date | Y |  |
| 16 | CASH_DISCOUNT_BASE_DATE | 现金折扣基准日 | date | Y |  |
| 17 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 18 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 19 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 20 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 21 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 22 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 23 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 24 | INITIAL_AMT_TC | 应收原始金额(原币) | number(23,8) | Y |  |
| 25 | INITIAL_AMT_FC | 应收原始金额(功能币) | number(23,8) | Y |  |
| 26 | ADJUSTMENT_EXG | 调整汇率 | number(18,9) | Y |  |
| 27 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 28 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 29 | TRANSFER_AMT_TC | 转销(原币) | number(23,8) | Y |  |
| 30 | TRANSFER_AMT_FC | 转销(功能币) | number(23,8) | Y |  |
| 31 | BAD_DEBT_AMT_TC | 坏账(原币) | number(23,8) | Y |  |
| 32 | BAD_DEBT_AMT_FC | 坏账(功能币) | number(23,8) | Y |  |
| 33 | RECOVERY_AMT_TC | 坏账收回金额(原币) | number(23,8) | Y |  |
| 34 | RECOVERY_AMT_FC | 坏账收回金额(功能币) | number(23,8) | Y |  |
| 35 | VERIFICATION_AMT_FC | 已核销(功能币) | number(23,8) | Y |  |
| 36 | BALANCE_AMT_TC | 应收余额(原币) | number(23,8) | Y |  |
| 37 | BALANCE_AMT_FC | 应收余额(功能币) | number(23,8) | Y |  |
| 38 | VERIFICATION_AMT_TC | 已核销(原币) | number(23,8) | Y |  |
| 39 | PROVISION_ADDED_AMT | 坏账准备 | number(23,8) | Y |  |
| 40 | PROVISION_BAD_AMT | 坏账准备-坏账金额 | number(23,8) | Y |  |
| 41 | PROVISION_RECOVERY_AMT | 坏账准备-坏账收回金额 | number(23,8) | Y |  |
| 42 | PROVISION_BALANCE_AMT | 坏账准备-余额 | number(23,8) | Y |  |
| 43 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 44 | TRANS_DOC_LINE_SEQNO | 交易单据行序号 | number | Y |  |
| 45 | OBJECT_TRANSDOC_NO | 应收对象-业务单据单号 | string(40) | Y |  |
| 46 | OBJECT_INSTAL_SOURDOC_NO | 应收对象-分期源单单号 | string(40) | Y |  |
| 47 | ITEM_NAME |  | string(120) | Y |  |
| 48 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 49 | ITEM_ID | 品号(作废) | GUID | Y |  |
| 50 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 51 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 52 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 53 | CURRENCY_ID | 货币 | GUID | Y |  |
| 54 | TRANS_DOC_ID | 交易单据类型 | GUID | Y |  |
| 55 | REMARK | 备注 | string(510) | Y |  |
| 56 | REVERSE_INDICATOR | 红冲标识 | number(0/1) | Y |  |
| 57 | DEPOSIT_TAX_INITIAL_TC | 定金税额原始金额(原币) | number(23,8) | Y |  |
| 58 | DEPOSIT_TAX_INITIAL_FC | 定金税额原始金额(本币) | number(23,8) | Y |  |
| 59 | DEPOSIT_TAX_OFFSETED_TC | 定金税额已冲减金额(原币) | number(23,8) | Y |  |
| 60 | DEPOSIT_TAX_OFFSETED_FC | 定金税额已冲减金额(本币) | number(23,8) | Y |  |
| 61 | DEPOSIT_TAX_BALANCE_TC | 定金税额余额(原币) | number(23,8) | Y |  |
| 62 | DEPOSIT_TAX_BALANCE_FC | 定金税额余额(本币) | number(23,8) | Y |  |
| 63 | FROZEN_AMT_TC | 冻结金额(原币) | number(23,8) | Y |  |
| 64 | PAYMENT_BASE_DATE_SOURCE | 基准日来源 | number | Y |  |
| 65 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 66 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 67 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 68 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 69 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
| 70 | TAX_INVOICE_DATE | 税务发票日期 | date | Y |  |
| 71 | OBJECT_TRANSDOC_ID | 应收对象-业务单据类型 | GUID | Y |  |
| 72 | OBJECT_TRANSDOC_DATE | 应收对象-业务单据日期 | date | Y |  |
| 73 | REF61_DOC_ID | 参考单据1_类型 | GUID | Y |  |
| 74 | REF61_DOC_NO | 参考单据1_单号 | string(80) | Y |  |
| 75 | REF61_DOC_DATE | 参考单据1_日期 | date | Y |  |
| 76 | REF62_DOC_ID | 参考单据2_类型 | GUID | Y |  |
| 77 | REF62_DOC_NO | 参考单据2_单号 | string(80) | Y |  |
| 78 | REF62_DOC_DATE | 参考单据2_日期 | date | Y |  |
| 79 | REMARK2 | 行备注 | string(510) | Y |  |
| 80 | PROJECT_ID | 项目 | GUID | Y |  |
| 81 | CreateDate | 创建日期 | date | Y |  |
| 82 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 83 | ModifiedDate | 修改日期 | date | Y |  |
| 84 | CreateBy | 创建者 | GUID | Y |  |
| 85 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 86 | ModifiedBy | 修改者 | GUID | Y |  |
| 87 | Attachments | 附件 | string | Y |  |
| 88 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 89 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 90 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 91 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 92 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 93 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 94 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 95 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 96 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 97 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 98 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 99 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 100 | UDF041 | 自定义字段12 | date | Y |  |
| 101 | UDF042 | 自定义字段13 | date | Y |  |
| 102 | UDF051 | 自定义字段14 | GUID | Y |  |
| 103 | UDF052 | 自定义字段15 | GUID | Y |  |
| 104 | UDF053 | 自定义字段16 | GUID | Y |  |
| 105 | UDF054 | 自定义字段17 | GUID | Y |  |
| 106 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 107 | Version | 版本号，不要随意更改 | binary | Y |  |
| 108 | Owner_Org_RTK |  | string(400) | Y |  |
| 109 | Owner_Org_ROid |  | GUID | Y |  |
| 110 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 111 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 112 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 113 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 114 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 115 | SOURCE_ID_ROid |  | GUID | Y |  |
| 116 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 117 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 118 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 119 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 120 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 121 | SOURCE6_ID_ROid |  | GUID | Y |  |
| 122 | SOURCE7_ID_RTK |  | string(400) | Y |  |
| 123 | SOURCE7_ID_ROid |  | GUID | Y |  |
| 124 | SOURCE8_ID_RTK |  | string(400) | Y |  |
| 125 | SOURCE8_ID_ROid |  | GUID | Y |  |
| 126 | SOURCE9_ID_RTK |  | string(400) | Y |  |
| 127 | SOURCE9_ID_ROid |  | GUID | Y |  |
| 128 | SOURCE10_ID_RTK |  | string(400) | Y |  |
| 129 | SOURCE10_ID_ROid |  | GUID | Y |  |
| 130 | SOURCE11_ID_RTK |  | string(400) | Y |  |
| 131 | SOURCE11_ID_ROid |  | GUID | Y |  |
| 132 | SOURCE61_ID_RTK |  | string(400) | Y |  |
| 133 | SOURCE61_ID_ROid |  | GUID | Y |  |
| 134 | SOURCE611_ID_RTK |  | string(400) | Y |  |
| 135 | SOURCE611_ID_ROid |  | GUID | Y |  |
| 136 | SOURCE62_ID_RTK |  | string(400) | Y |  |
| 137 | SOURCE62_ID_ROid |  | GUID | Y |  |
| 138 | SOURCE621_ID_RTK |  | string(400) | Y |  |
| 139 | SOURCE621_ID_ROid |  | GUID | Y |  |

### RECEIVABLE_OBJECT_CHANGE - 应收对象变更历史

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | RECEIVABLE_OBJECT_CHANGE_ID | 主键 | GUID | Y | Y |
| 5 | RECEIVABLE_OBJECT_ID | 应收对象 | GUID | Y |  |
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