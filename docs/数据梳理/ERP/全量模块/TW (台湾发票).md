---
module: "TW"
name_zh: "台湾发票"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 17
columns: 1144
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# TW (台湾发票)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 17 | Columns: 1144

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]

---

## Tables


- **TW_INVOICE_AP (进项发票信息)**
- **TW_INVOICE_AR (销项发票信息)**
- **TW_INVOICE_AR_D (销项发票来源明细)**
- **TW_INVOICE_AR_DETAIL (开立发票明细)**
- **TW_INVOICE_AR_ISSUE (销项发票开立信息)**
- **TW_INVOICE_AR_ISSUE_D (销项发票开立信息单身)**
- **TW_INVOICE_AR_ISSUE_OBJ (销项发票开立对象)**
- **TW_INVOICE_AR_SUM (销项发票发票内容)**
- **TW_INVOICE_AR_SUMMARY (开立发票汇总)**
- **TW_INVOICE_BOOK (发票簿)**
- **TW_INVOICE_BOOK_D (发票簿单身)**
- **TW_INVOICE_BOOK_SD (发票簿子单身)**
- **TW_INVOICE_RETURN (退货折让证明单)**
- **TW_INVOICE_RETURN_D (退货折让单来源明细)**
- **TW_INVOICE_RETURN_SUM (退货折让单内容)**
- **TW_TAX_DECLARE**
- **TW_TAXREGISTRATION (营业人税籍)**


---


---


> Tables: 17

### TW_INVOICE_AP (进项发票信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PrintCount | 打印次数 | number | Y |  |
| 4 | TW_INVOICE_AP_ID | 主键 | GUID | Y | Y |
| 5 | TW_TAXREGISTRATION_ID | 营业人税籍 | GUID | Y |  |
| 6 | VAT_TAXPAYER | 申报营业人 | string(72) | Y |  |
| 7 | COMPANY_ID_NO | 统一编号 | string(16) | Y |  |
| 8 | TAX_REGISTRATION_NO | 税籍编号 | string(20) | Y |  |
| 9 | TAX_ID | 税种名称 | GUID | Y |  |
| 10 | INVOICE_RATE | 发票税率 | number(5,4) | Y |  |
| 11 | INVOICE_TRACK | 发票字轨 | string(4) | Y |  |
| 12 | INVOICE_NO | 发票号码 | string(16) | Y |  |
| 13 | INVOICE_DATE | 发票日期 | date | Y |  |
| 14 | DECLARE_TAX_CREDIT_CODE | 扣抵代号 | number | Y |  |
| 15 | GENERATE_MODE | 产生方式 | number | Y |  |
| 16 | OTHER_DOC | 其他来源凭证 | string(80) | Y |  |
| 17 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 18 | SUPPLIER_NAME | 供应商全名 | string(200) | Y |  |
| 19 | SUPPLIER_COMPANY_ID_NO | 供应商统一编号 | string(16) | Y |  |
| 20 | OTHER_CERTIFICATE_NO | 其他凭证号 | string(28) | Y |  |
| 21 | INV_UNTAX_AMT | 发票无税金额 | number(23,8) | Y |  |
| 22 | INV_TAX_AMT | 发票税额 | number(23,8) | Y |  |
| 23 | INV_AMT | 发票总金额 | number(23,8) | Y |  |
| 24 | DECLARE_INVOICE_FORM_CODE | 申报格式代号 | number | Y |  |
| 25 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 26 | DECLARE_STATUS | 申报状态 | number | Y |  |
| 27 | DECLARE_VAT_CODE | 申报课税别 | number | Y |  |
| 28 | SUMMARY_MARK | 汇总注记 | number(0/1) | Y |  |
| 29 | SUMMARY_SHEETS | 汇总张数 | number | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 32 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 33 | UNTAX_AMT_RETURNED | 已折让发票无税金额 | number(23,8) | Y |  |
| 34 | TAX_AMT_RETURNED | 已折让发票税额 | number(23,8) | Y |  |
| 35 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 36 | DESCRIPTION_NAME | 内容摘要名称 | string(120) | Y |  |
| 37 | DESCRIPTION_QTY | 内容摘要数量 | number(16,6) | Y |  |
| 38 | USE | 用途 | string(160) | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 60 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 61 | ApproveDate | 修改日期 | date | Y |  |
| 62 | ApproveBy | 修改人 | GUID | Y |  |
| 63 | CreateDate | 创建日期 | date | Y |  |
| 64 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 65 | ModifiedDate | 修改日期 | date | Y |  |
| 66 | CreateBy | 创建者 | GUID | Y |  |
| 67 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 68 | ModifiedBy | 修改者 | GUID | Y |  |
| 69 | Owner_Org_RTK |  | string(400) | Y |  |
| 70 | Owner_Org_ROid |  | GUID | Y |  |
| 71 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 72 | SOURCE_ID_ROid |  | GUID | Y |  |
| 73 | SOURCE1_ID_RTK |  | string(400) | Y |  |
| 74 | SOURCE1_ID_ROid |  | GUID | Y |  |

### TW_INVOICE_AR (销项发票信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PrintCount | 打印次数 | number | Y |  |
| 4 | TW_INVOICE_AR_ID | 主键 | GUID | Y | Y |
| 5 | SALE_TAXPAYER | 销售营业人 | string(72) | Y |  |
| 6 | COMPANY_ID_NO | 统一编号 | string(16) | Y |  |
| 7 | TW_INVOICE_BOOK_D_ID | 发票簿号 | GUID | Y |  |
| 8 | INVOICE_RATE | 发票税率 | number(5,4) | Y |  |
| 9 | TAX_ID | 税种名称 | GUID | Y |  |
| 10 | INVOICE_TRACK | 发票字轨 | string(4) | Y |  |
| 11 | INVOICE_NO | 发票号码 | string(16) | Y |  |
| 12 | INVOICE_DATE | 发票日期 | date | Y |  |
| 13 | CUSTOMER_ID | 客户信息 | GUID | Y |  |
| 14 | BUYER_COMPANY_ID_NO | 买受方统一编号 | string(16) | Y |  |
| 15 | BUYER_INVOICE_ADDRESS | 买受人地址 | string(510) | Y |  |
| 16 | DECLARE_INVOICE_FORM_CODE | 申报格式代号 | number | Y |  |
| 17 | DECLARE_VAT_CODE | 申报课税别 | number | Y |  |
| 18 | ALCOHOL_TOBACCO_MARK | 洋烟酒注记 | number(0/1) | Y |  |
| 19 | SUMMARY_MARK | 汇总码 | number(0/1) | Y |  |
| 20 | END_INVOICE_NO | 发票讫号 | string(16) | Y |  |
| 21 | OTHER_DOC | 其他凭证 | string(80) | Y |  |
| 22 | INV_UNTAX_AMT | 发票无税金额 | number(23,8) | Y |  |
| 23 | INV_TAX_AMT | 发票税额 | number(23,8) | Y |  |
| 24 | INV_AMT | 发票总金额 | number(23,8) | Y |  |
| 25 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 26 | DECLARE_STATUS | 申报年月 | number | Y |  |
| 27 | REMARK | 备注 | string(510) | Y |  |
| 28 | EXPORT_TYPE | 外销方式 | number | Y |  |
| 29 | CUSTOMS_CLEARANCE | 通关方式 | number | Y |  |
| 30 | PROVE_DOC_NAME | 证明文件名称 | string(80) | Y |  |
| 31 | PROVE_DOC_NO | 证明文件号码 | string(40) | Y |  |
| 32 | EXPORT_DOC_TYPE | 出口报单类别 | string(4) | Y |  |
| 33 | EXPORT_DOC_NO1 | 收单关别号 | string(4) | Y |  |
| 34 | EXPORT_DOC_NO2 | 出口关别号 | string(4) | Y |  |
| 35 | EXPORT_DOC_NO3 | 出口年度 | string(4) | Y |  |
| 36 | EXPORT_DOC_NO4 | 船或关代号 | string(8) | Y |  |
| 37 | EXPORT_DOC_NO5 | 装货单货收序号 | string(10) | Y |  |
| 38 | EXPORT_DATE | 输出报关日期 | date | Y |  |
| 39 | EXPORT_ITEM_NAME | 货物名称 | string(120) | Y |  |
| 40 | EXPORT_QTY | 数量 | number(16,6) | Y |  |
| 41 | EXPORT_AMT | 出口报单金额 | number(23,8) | Y |  |
| 42 | VOIDED_REASON | 作废原因 | string(510) | Y |  |
| 43 | BUYER_NAME | 买受人名称 | string(200) | Y |  |
| 44 | TAX_REGISTRATION_NO | 税籍编号 | string(20) | Y |  |
| 45 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 46 | TW_TAXREGISTRATION_ID | 营业人税籍 | GUID | Y |  |
| 47 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 48 | UNTAX_AMT_RETURNED | 已折让发票无税金额 | number(23,8) | Y |  |
| 49 | TAX_AMT_RETURNED | 已折让发票税额 | number(23,8) | Y |  |
| 50 | GENERATE_MODE | 产生方式 | number | Y |  |
| 51 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 52 | TAX_INVOICE_SUMMARY_MODE | 发票汇总方式 | number | Y |  |
| 53 | INVOICE_SEQNO | 发票序号 | number | Y |  |
| 54 | TW_INVOICE_AR_ISSUE_OBJ_ID | 开立对象 | GUID | Y |  |
| 55 | INVOICE_TIME | 开立时间 | time | Y |  |
| 56 | CANCEL_DATE | 作废日期 | date | Y |  |
| 57 | CANCEL_TIME | 作废时间 | time | Y |  |
| 58 | INVOICE_STATUS | 状态码 | number | Y |  |
| 59 | VOID_APPROVAL_NUMBER | 专案作废核准文号 | string(60) | Y |  |
| 60 | RECEIVE_DATE | 接收日期 | date | Y |  |
| 61 | RECEIVE_TIME | 接收时间 | time | Y |  |
| 62 | UPLOAD_METHOD | 上传方式 | number | Y |  |
| 63 | CreateDate | 创建日期 | date | Y |  |
| 64 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 65 | ModifiedDate | 修改日期 | date | Y |  |
| 66 | CreateBy | 创建者 | GUID | Y |  |
| 67 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 68 | ModifiedBy | 修改者 | GUID | Y |  |
| 69 | Attachments | 附件 | string | Y |  |
| 70 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 71 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 72 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 73 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 74 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 75 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 76 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 77 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 78 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 79 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 80 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 81 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 82 | UDF041 | 自定义字段12 | date | Y |  |
| 83 | UDF042 | 自定义字段13 | date | Y |  |
| 84 | UDF051 | 自定义字段14 | GUID | Y |  |
| 85 | UDF052 | 自定义字段15 | GUID | Y |  |
| 86 | UDF053 | 自定义字段16 | GUID | Y |  |
| 87 | UDF054 | 自定义字段17 | GUID | Y |  |
| 88 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 89 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 90 | ApproveDate | 修改日期 | date | Y |  |
| 91 | ApproveBy | 修改人 | GUID | Y |  |
| 92 | Version | 版本号，不要随意更改 | binary | Y |  |
| 93 | Owner_Org_RTK |  | string(400) | Y |  |
| 94 | Owner_Org_ROid |  | GUID | Y |  |
| 95 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 96 | SOURCE_ID_ROid |  | GUID | Y |  |

### TW_INVOICE_AR_D (销项发票来源明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_AR_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | SALES_ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | SALES_QTY | 数量 | number(16,6) | Y |  |
| 6 | CURRENCY_ID | 货币 | GUID | Y |  |
| 7 | PRICE_UNTAX_AMT_TC | 无税单价（原币） | number(23,8) | Y |  |
| 8 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 9 | SALES_UNTAX_AMT_TC | 销售无税金额（原币） | number(23,8) | Y |  |
| 10 | SALES_TAX_AMT_TC | 销售税额 | number(23,8) | Y |  |
| 11 | SALES_UNTAX_AMT_FC | 销售无税金额（本币） | number(23,8) | Y |  |
| 12 | SALES_TAX_AMT_FC | 销售税额（本币） | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | SALES_ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 15 | SALES_UNIT_ID | 单位 | GUID | Y |  |
| 16 | INVOICE_RATE |  | number(5,4) | Y |  |
| 17 | ITEM_TRANS_TYPE | 品号交易类型 | string(40) | Y |  |
| 18 | TAX_ID | 税种 | GUID | Y |  |
| 19 | INVOICE_AMT_TOTAL_TC | 价税合计(原币) | number(23,8) | Y |  |
| 20 | INVOICE_AMT_TOTAL_FC | 价税合计(本币) | number(23,8) | Y |  |
| 21 | INV_UNTAX_DIFF_AMT | 发票未税金额差异 | number(23,8) | Y |  |
| 22 | INV_TAX_DIFF_AMT | 发票税额差异 | number(23,8) | Y |  |
| 23 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 24 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 25 | CUSTOMER_ITEM_NAME | 客户品名 | string(120) | Y |  |
| 26 | CUSTOMER_ITEM_SPECIFICATION | 客户规格 | string(510) | Y |  |
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
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE_ID_ROid |  | GUID | Y |  |
| 57 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 58 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 59 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 61 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 62 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 63 | TW_INVOICE_AR_ID |  | GUID | Y |  |

### TW_INVOICE_AR_DETAIL (开立发票明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | TW_INVOICE_AR_DETAIL_ID | 主键 | GUID | Y | Y |
| 2 | ISSUE_OBJ_SEQNO | 开立对象序号 | number | Y |  |
| 3 | INVOICE_SEQNO | 发票序号 | number | Y |  |
| 4 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 5 | TRANS_DOC_NO | 源单单号 | string(40) | Y |  |
| 6 | TRANS_DATE | 业务日期 | date | Y |  |
| 7 | DOC_ID | 单据类型 | GUID | Y |  |
| 8 | TRANS_DOC_D_SEQNO | 源单单身序号 | number | Y |  |
| 9 | ITEM_TRANS_TYPE | 品号交易类型 | string(40) | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | SALES_ITEM_NAME | 品名 | string(120) | Y |  |
| 12 | SALES_ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 13 | SALES_QTY | 数量 | number(16,6) | Y |  |
| 14 | SALES_UNIT_ID | 单位 | GUID | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | CURRENCY_ID | 货币 | GUID | Y |  |
| 17 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 18 | PARENT_TAX_ID | 源单单头税种 | GUID | Y |  |
| 19 | TAX_ID | 税种 | GUID | Y |  |
| 20 | INVOICE_RATE | 税率 | number(5,4) | Y |  |
| 21 | SALES_TAX_AMT_TC | 销售税额（原币） | number(23,8) | Y |  |
| 22 | PRICE_UNTAX_AMT_TC | 无税单价（原币） | number(23,8) | Y |  |
| 23 | SALES_UNTAX_AMT_TC | 销售无税金额（原币） | number(23,8) | Y |  |
| 24 | INVOICE_AMT_TOTAL_TC | 价税合计(原币) | number(23,8) | Y |  |
| 25 | SALES_UNTAX_AMT_FC | 销售无税金额（本币） | number(23,8) | Y |  |
| 26 | SALES_TAX_AMT_FC | 销售税额（本币） | number(23,8) | Y |  |
| 27 | INVOICE_AMT_TOTAL_FC | 价税合计(本币) | number(23,8) | Y |  |
| 28 | INV_UNTAX_DIFF_AMT | 发票未税金额差异 | number(23,8) | Y |  |
| 29 | INV_TAX_DIFF_AMT | 发票税额差异 | number(23,8) | Y |  |
| 30 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 31 | CUSTOMER_ITEM_NAME | 客户品名 | string(120) | Y |  |
| 32 | CUSTOMER_ITEM_SPECIFICATION | 客户规格 | string(510) | Y |  |
| 33 | ORDER_DOC_NO | 订单号 | string(40) | Y |  |
| 34 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 35 | REMARK | 备注 | string(510) | Y |  |
| 36 | INVOICE_ITEM_SOURCE | 发票品号来源 | string(40) | Y |  |
| 37 | INVOICE_ITEM_CODE | 发票品号 | string(80) | Y |  |
| 38 | INVOICE_ITEM_OTHER | 其它发票品名 | string(120) | Y |  |
| 39 | INVOICE_ITEM_NAME | 发票品名 | string(120) | Y |  |
| 40 | INVOICE_ITEM_SPECIFICATION | 发票品号规格 | string(510) | Y |  |
| 41 | CURRENCY_CODE | 货币编号 | string(12) | Y |  |
| 42 | TAX_CODE | 税种编号 | string(12) | Y |  |
| 43 | BATCH_ID | 批次 | GUID | Y |  |
| 44 | UNIT_CODE | 单位编号 | string(8) | Y |  |
| 45 | INVOICE_DATE | 发票日期 | date | Y |  |
| 46 | S_SequenceNumber | 原始序号 | number | Y |  |
| 47 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | Attachments | 附件 | string | Y |  |
| 55 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 56 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 57 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 58 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 59 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 60 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 61 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 62 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 63 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 64 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 65 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 66 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 67 | UDF041 | 自定义字段12 | date | Y |  |
| 68 | UDF042 | 自定义字段13 | date | Y |  |
| 69 | UDF051 | 自定义字段14 | GUID | Y |  |
| 70 | UDF052 | 自定义字段15 | GUID | Y |  |
| 71 | UDF053 | 自定义字段16 | GUID | Y |  |
| 72 | UDF054 | 自定义字段17 | GUID | Y |  |
| 73 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 74 | Version | 版本号，不要随意更改 | binary | Y |  |
| 75 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 76 | ApproveDate | 修改日期 | date | Y |  |
| 77 | ApproveBy | 修改人 | GUID | Y |  |
| 78 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 79 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 80 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 81 | SOURCE_ID_ROid |  | GUID | Y |  |
| 82 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 83 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 84 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 85 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 86 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 87 | SOURCE5_ID_ROid |  | GUID | Y |  |
| 88 | SOURCE6_ID_RTK |  | string(400) | Y |  |
| 89 | SOURCE6_ID_ROid |  | GUID | Y |  |

### TW_INVOICE_AR_ISSUE (销项发票开立信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PrintCount | 打印次数 | number | Y |  |
| 4 | TW_INVOICE_AR_ISSUE_ID | 主键 | GUID | Y | Y |
| 5 | TW_TAXREGISTRATION_ID | 营业人税籍 | GUID | Y |  |
| 6 | COMPANY_ID_NO | 统一编号 | string(16) | Y |  |
| 7 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 8 | INVOICE_MAXLINE_INDICATOR | 发票行数控制标识 | number(0/1) | Y |  |
| 9 | INVOICE_MAXLINE | 发票最大行数 | number | Y |  |
| 10 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 11 | INVOICE_RATE | 发票税率 | number(5,4) | Y |  |
| 12 | TAX_INVOICE_SUMMARY_MODE | 发票内容汇总方式 | number | Y |  |
| 13 | SUMMARY_MARK | 汇总码 | number(0/1) | Y |  |
| 14 | ISSUE_DATE | 开立日期 | date | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | TAX_ID | 税种名称 | GUID | Y |  |
| 17 | TW_INVOICE_BOOK_D_ID | 发票簿名 | GUID | Y |  |
| 18 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 19 | GENERATE_MODE | 产生方式 | number | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Attachments | 附件 | string | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### TW_INVOICE_AR_ISSUE_D (销项发票开立信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_AR_ISSUE_D_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 4 | OTHER_DOC | 其他凭证号 | string(80) | Y |  |
| 5 | TW_INVOICE_AR_ID | 销项发票主键 | GUID | Y |  |
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
| 32 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 33 | SOURCE_ID_ROid |  | GUID | Y |  |
| 34 | TW_INVOICE_AR_ISSUE_ID |  | GUID | Y |  |

### TW_INVOICE_AR_ISSUE_OBJ (销项发票开立对象)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_AR_ISSUE_OBJ_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 4 | OTHER_DOC | 其他凭证号 | string(80) | Y |  |
| 5 | TRANS_DATE | 业务日期 | date | Y |  |
| 6 | INVOICE_DATE | 发票日期 | date | Y |  |
| 7 | INVOICE_COUNT | 发票张数 | number | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | END_INVOICE_TRACK | 发票讫号字轨 | string(4) | Y |  |
| 10 | END_INVOICE_NO | 发票讫号 | string(16) | Y |  |
| 11 | TAX_INVOICE_NO | 税务发票号码 | string(1024) | Y |  |
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
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | TW_INVOICE_AR_ISSUE_ID |  | GUID | Y |  |

### TW_INVOICE_AR_SUM (销项发票发票内容)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_AR_SUM_ID | 主键 | GUID | Y | Y |
| 3 | INVOICE_ITEM_NAME | 发票品名 | string(120) | Y |  |
| 4 | INVOICE_QTY | 数量 | number(16,6) | Y |  |
| 5 | PRICE_UNTAX_AMT_TC | 无税单价（原币） | number(23,8) | Y |  |
| 6 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 7 | INVOICE_UNTAX_AMT_TC | 发票无税金额（原币） | number(23,8) | Y |  |
| 8 | INVOICE_TAX_AMT_TC | 发票税额（原币） | number(23,8) | Y |  |
| 9 | INVOICE_UNTAX_AMT_FC | 发票无税金额（本币） | number(23,8) | Y |  |
| 10 | INVOICE_TAX_AMT_FC | 发票税额（本币） | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | INVOICE_ITEM_SPECIFICATION | 税务规格 | string(510) | Y |  |
| 13 | INVOICE_UNIT_ID | 单位 | GUID | Y |  |
| 14 | INVOICE_RATE | 税率 | number(5,4) | Y |  |
| 15 | TAX_ID | 税种名称 | GUID | Y |  |
| 16 | INVOICE_ITEM_SOURCE | 发票品号来源 | number | Y |  |
| 17 | CURRENCY_ID | 货币 | GUID | Y |  |
| 18 | INVOICE_ITEM_OTHER | 其它发票品名 | string(120) | Y |  |
| 19 | INVOICE_AMT_TOTAL_TC | 价税合计（原币） | number(23,8) | Y |  |
| 20 | INVOICE_AMT_TOTAL_FC | 价税合计（本币） | number(23,8) | Y |  |
| 21 | INV_UNTAX_DIFF_AMT | 发票未税金额差异 | number(23,8) | Y |  |
| 22 | INV_TAX_DIFF_AMT | 发票税额差异 | number(23,8) | Y |  |
| 23 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 24 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 25 | CUSTOMER_ITEM_NAME | 客户品名 | string(120) | Y |  |
| 26 | CUSTOMER_ITEM_SPECIFICATION | 客户规格 | string(510) | Y |  |
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
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE_ID_ROid |  | GUID | Y |  |
| 57 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 58 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 59 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 61 | TW_INVOICE_AR_ID |  | GUID | Y |  |

### TW_INVOICE_AR_SUMMARY (开立发票汇总)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_AR_SUMMARY_ID | 主键 | GUID | Y | Y |
| 3 | ISSUE_OBJ_SEQNO | 开立对象序号 | number | Y |  |
| 4 | INVOICE_SEQNO | 发票序号 | number | Y |  |
| 5 | INVOICE_LINE_SEQNO | 发票子序号 | number | Y |  |
| 6 | BATCH_ID | 批次 | GUID | Y |  |
| 7 | TRANS_DOC_NO | 源单单号 | string(40) | Y |  |
| 8 | TRANS_DATE | 业务日期 | date | Y |  |
| 9 | INVOICE_DATE | 发票日期 | date | Y |  |
| 10 | DOC_ID | 单据类型 | GUID | Y |  |
| 11 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 12 | INVOICE_ITEM_SOURCE | 发票品号来源 | number | Y |  |
| 13 | INVOICE_ITEM_OTHER | 其它发票品名 | string(120) | Y |  |
| 14 | INVOICE_ITEM_NAME | 发票品名 | string(120) | Y |  |
| 15 | INVOICE_ITEM_SPECIFICATION | 发票品号规格 | string(510) | Y |  |
| 16 | INVOICE_UNIT_ID | 单位 | GUID | Y |  |
| 17 | INVOICE_QTY | 数量 | number(16,6) | Y |  |
| 18 | CURRENCY_ID | 货币 | GUID | Y |  |
| 19 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 20 | PRICE_UNTAX_AMT_TC | 无税单价（原币） | number(23,8) | Y |  |
| 21 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 22 | PARENT_TAX_ID | 源单单头税种 | GUID | Y |  |
| 23 | TAX_ID | 税种 | GUID | Y |  |
| 24 | TAX_CODE | 税种编号 | string(12) | Y |  |
| 25 | INVOICE_RATE | 税率 | number(5,4) | Y |  |
| 26 | INVOICE_UNTAX_AMT_TC | 发票无税金额（原币） | number(23,8) | Y |  |
| 27 | INVOICE_TAX_AMT_TC | 发票税额（原币） | number(23,8) | Y |  |
| 28 | INVOICE_AMT_TOTAL_TC | 价税合计（原币） | number(23,8) | Y |  |
| 29 | INVOICE_UNTAX_AMT_FC | 发票无税金额（本币） | number(23,8) | Y |  |
| 30 | INVOICE_TAX_AMT_FC | 发票税额（本币） | number(23,8) | Y |  |
| 31 | INVOICE_AMT_TOTAL_FC | 价税合计（本币） | number(23,8) | Y |  |
| 32 | INV_UNTAX_DIFF_AMT | 发票未税金额差异 | number(23,8) | Y |  |
| 33 | INV_TAX_DIFF_AMT | 发票税额差异 | number(23,8) | Y |  |
| 34 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 35 | CUSTOMER_ITEM_NAME | 客户品名 | string(120) | Y |  |
| 36 | CUSTOMER_ITEM_SPECIFICATION | 客户规格 | string(510) | Y |  |
| 37 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 38 | REMARK | 备注 | string(510) | Y |  |
| 39 | S_SequenceNumber |  | number | Y |  |
| 40 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | Attachments | 附件 | string | Y |  |
| 48 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 49 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 50 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 51 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 52 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 53 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 54 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 55 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 56 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 57 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 58 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 59 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 60 | UDF041 | 自定义字段12 | date | Y |  |
| 61 | UDF042 | 自定义字段13 | date | Y |  |
| 62 | UDF051 | 自定义字段14 | GUID | Y |  |
| 63 | UDF052 | 自定义字段15 | GUID | Y |  |
| 64 | UDF053 | 自定义字段16 | GUID | Y |  |
| 65 | UDF054 | 自定义字段17 | GUID | Y |  |
| 66 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 67 | Version | 版本号，不要随意更改 | binary | Y |  |
| 68 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 69 | ApproveDate | 修改日期 | date | Y |  |
| 70 | ApproveBy | 修改人 | GUID | Y |  |
| 71 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 72 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 73 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 74 | SOURCE_ID_ROid |  | GUID | Y |  |
| 75 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 76 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 77 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 78 | SOURCE3_ID_ROid |  | GUID | Y |  |

### TW_INVOICE_BOOK (发票簿)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TW_INVOICE_BOOK_ID | 主键 | GUID | Y | Y |
| 4 | TAX_REGISTRATION_NAME | 营利事业税籍名称 | string(144) | Y |  |
| 5 | COMPANY_ID_NO | 营利事业统一编号 | string(16) | Y |  |
| 6 | INVOICE_MAXLINE | 发票最大行数 | number | Y |  |
| 7 | DECLARE_START_YM | 起始年月 | string(12) | Y |  |
| 8 | DECLARE_END_YM | 截止年月 | string(12) | Y |  |
| 9 | INVOICE_TRACK | 发票字轨 | string(4) | Y |  |
| 10 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | TW_TAXREGISTRATION_ID | 主键 | GUID | Y |  |
| 13 | INVOICE_MAXLINE_INDICATOR | 发票行数控制标识 | number(0/1) | Y |  |
| 14 | TAX_INVOICE_CATEGORY_ID | 主键 | GUID | Y |  |
| 15 | TAX_INVOICE_NATURE | 发票种类性质 | string(10) | Y |  |
| 16 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 17 | E_INVOICE_FLAG | 电子发票标识 | number(0/1) | Y |  |
| 18 | INVOICE_TYPE | 发票类别 | number | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
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
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |

### TW_INVOICE_BOOK_D (发票簿单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_BOOK_D_ID | 主键 | GUID | Y | Y |
| 3 | BOOK_NO | 簿名 | string(6) | Y |  |
| 4 | AUTHORIZED_USERS | 限定使用者 | number(0/1) | Y |  |
| 5 | START_NO | 起始号码 | string(16) | Y |  |
| 6 | END_NO | 截止号码 | string(16) | Y |  |
| 7 | BOOK_QTY | 张数 | number | Y |  |
| 8 | USED_NO | 已使用号码 | string(16) | Y |  |
| 9 | AUTO_OPEN | 自动开立 | number(0/1) | Y |  |
| 10 | AVAILABLE_DATE | 生效日 | date | Y |  |
| 11 | UNAVAILABLE_DATE | 失效日 | date | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PRINT_LAYOUT_DEFAULT | 默认打印样式编号 | string(400) | Y |  |
| 14 | REPORT_TYPEKEY | 报表编号 | string(400) | Y |  |
| 15 | USE_SEQUENTIAL_CODE | 使用顺序码 | number | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 44 | TW_INVOICE_BOOK_ID |  | GUID | Y |  |

### TW_INVOICE_BOOK_SD (发票簿子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_BOOK_SD_ID | 主键 | GUID | Y | Y |
| 3 | EMPLOYEE_ID | 主键 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | BOOK_NO | 簿号 | string(6) | Y |  |
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
| 34 | TW_INVOICE_BOOK_D_ID |  | GUID | Y |  |

### TW_INVOICE_RETURN (退货折让证明单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PrintCount | 打印次数 | number | Y |  |
| 4 | TW_INVOICE_RETURN_ID | 主键 | GUID | Y | Y |
| 5 | TW_TAXREGISTRATION_ID | 营业人税籍 | GUID | Y |  |
| 6 | VAT_TAXPAYER | 申报营业人 | string(72) | Y |  |
| 7 | COMPANY_ID_NO | 统一编号 | string(16) | Y |  |
| 8 | TAX_REGISTRATION_NO | 税籍编号 | string(20) | Y |  |
| 9 | INV_RETURN_TYPE | 折让单类型 | number | Y |  |
| 10 | TW_INVOICE_BOOK_D_ID | 簿号 | GUID | Y |  |
| 11 | INVOICE_RATE | 发票税率 | number(5,4) | Y |  |
| 12 | INVOICE_RETURN_NO1 | 折让单编号1 | string(4) | Y |  |
| 13 | INVOICE_RETURN_MAXLINE | 折让单最大行数 | number | Y |  |
| 14 | INVOICE_RETURN_NO2 | 折让单编号2 | string(16) | Y |  |
| 15 | INVOICE_DATE | 折让单日期 | date | Y |  |
| 16 | GENERATE_MODE | 产生方式 | number | Y |  |
| 17 | OTHER_DOC | 其他来源凭证 | string(80) | Y |  |
| 18 | DECLARE_INVOICE_FORM_CODE | 申报格式代号 | number | Y |  |
| 19 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 20 | DECLARE_STATUS | 申报状态 | number | Y |  |
| 21 | DECLARE_VAT_CODE | 申报课税别 | number | Y |  |
| 22 | CUSTOMER_ID | 客户信息 | GUID | Y |  |
| 23 | BUYER_NAME | 买受人名称 | string(200) | Y |  |
| 24 | BUYER_COMPANY_ID_NO | 买方统一编号 | string(16) | Y |  |
| 25 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 26 | SUPPLIER_NAME | 供应商全名 | string(200) | Y |  |
| 27 | SUPPLIER_COMPANY_ID_NO | 供应商统一编号 | string(16) | Y |  |
| 28 | INV_RETURN_UNTAX_AMT | 折让无税金额 | number(23,8) | Y |  |
| 29 | INV_RETURN_TAX_AMT | 折让税额 | number(23,8) | Y |  |
| 30 | INV_RETURN_AMT | 折让总金额 | number(23,8) | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 33 | DECLARE_TAX_CREDIT_CODE | 扣抵代号 | number | Y |  |
| 34 | TAX_ID | 税种 | GUID | Y |  |
| 35 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 36 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 37 | CUSTOMS_PAY_CERTIFICATE_NO | 海关代征缴纳证号 | string(28) | Y |  |
| 38 | CANCEL_DATE | 作废日期 | date | Y |  |
| 39 | CANCEL_TIME | 作废时间 | time | Y |  |
| 40 | CANCEL_REASON | 作废原因 | string(510) | Y |  |
| 41 | INVOICE_STATUS | 状态码 | number | Y |  |
| 42 | RECEIVE_DATE | 接收日期 | date | Y |  |
| 43 | RECEIVE_TIME | 接收时间 | time | Y |  |
| 44 | UPLOAD_METHOD | 上传方式 | number | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
| 52 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 53 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 54 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 55 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 56 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 57 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 58 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 59 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 60 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 61 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 62 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 63 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 64 | UDF041 | 自定义字段12 | date | Y |  |
| 65 | UDF042 | 自定义字段13 | date | Y |  |
| 66 | UDF051 | 自定义字段14 | GUID | Y |  |
| 67 | UDF052 | 自定义字段15 | GUID | Y |  |
| 68 | UDF053 | 自定义字段16 | GUID | Y |  |
| 69 | UDF054 | 自定义字段17 | GUID | Y |  |
| 70 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 71 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 72 | ApproveDate | 修改日期 | date | Y |  |
| 73 | ApproveBy | 修改人 | GUID | Y |  |
| 74 | Version | 版本号，不要随意更改 | binary | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |
| 77 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 78 | SOURCE_ID_ROid |  | GUID | Y |  |

### TW_INVOICE_RETURN_D (退货折让单来源明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_RETURN_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | INV_RETURN_ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | INV_RETURN_ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | INV_RETURN_UNIT_ID | 单位 | GUID | Y |  |
| 7 | INV_RETURN_QTY | 数量 | number(16,6) | Y |  |
| 8 | CURRENCY_ID | 主键 | GUID | Y |  |
| 9 | INVOICE_RATE | 税率 | number(5,4) | Y |  |
| 10 | PRICE_UNTAX_AMT_TC | 无税单价（原币） | number(23,8) | Y |  |
| 11 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 12 | UNTAX_AMT_TC | 无税金额（原币） | number(23,8) | Y |  |
| 13 | TAX_AMT_TC | 税额（原币） | number(23,8) | Y |  |
| 14 | UNTAX_AMT_FC | 无税金额（本币） | number(23,8) | Y |  |
| 15 | TAX_AMT_FC | 税额（本币） | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | TAX_ID | 税种税率 | GUID | Y |  |
| 18 | ITEM_TRANS_TYPE | 商品类型 | string(40) | Y |  |
| 19 | INVOICE_AMT_TOTAL_TC | 价税合计（原币） | number(23,8) | Y |  |
| 20 | INVOICE_AMT_TOTAL_FC | 价税合计（本币） | number(23,8) | Y |  |
| 21 | EXPENSE_ID | 费用项目 | GUID | Y |  |
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
| 52 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 54 | TW_INVOICE_RETURN_ID |  | GUID | Y |  |

### TW_INVOICE_RETURN_SUM (退货折让单内容)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TW_INVOICE_RETURN_SUM_ID | 主键 | GUID | Y | Y |
| 3 | INVOICE_ITEM_SPECIFICATION | 税务规格 | string(510) | Y |  |
| 4 | INVOICE_UNIT_ID | 单位 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | INVOICE_QTY | 数量 | number(16,6) | Y |  |
| 7 | TAX_ID | 税种 | GUID | Y |  |
| 8 | INVOICE_RATE | 税率 | number(5,4) | Y |  |
| 9 | PRICE_UNTAX_AMT_TC | 无税单价（原币） | number(23,8) | Y |  |
| 10 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 11 | INVOICE_RETURN_UNTAX_AMT_TC | 折让无税金额（原币） | number(23,8) | Y |  |
| 12 | INVOICE_RETURN_TAX_AMT_TC | 折让税额（原币） | number(23,8) | Y |  |
| 13 | INVOICE_RETURN_UNTAX_AMT_FC | 折让无税金额（本币） | number(23,8) | Y |  |
| 14 | INVOICE_RETURN_TAX_AMT_FC | 折让税额（本币） | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | FORMER_INVOICE_TRACK | 原发票字轨 | string(4) | Y |  |
| 17 | FORMER_INVOICE_NO | 原发票号码 | string(16) | Y |  |
| 18 | FORMER_INVOICE_DATE | 原发票日期 | date | Y |  |
| 19 | FORMER_INV_TAX_AMT | 原发票税额 | number(23,8) | Y |  |
| 20 | FORMER_INV_UNTAX_AMT | 原发票无税金额 | number(23,8) | Y |  |
| 21 | INVOICE_ITEM_SOURCE | 退货折让品号来源 | number | Y |  |
| 22 | INVOICE_ITEM_NAME | 退货折让品名 | string(120) | Y |  |
| 23 | INVOICE_ITEM_OTHER | 其它退货折让品名 | string(120) | Y |  |
| 24 | INVOICE_AMT_TOTAL_TC | 价税合计（原币） | number(23,8) | Y |  |
| 25 | INVOICE_AMT_TOTAL_FC | 价税合计（本币) | number(23,8) | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | SOURCE1_ID_RTK |  | string(400) | Y |  |
| 57 | SOURCE1_ID_ROid |  | GUID | Y |  |
| 58 | TW_INVOICE_RETURN_ID |  | GUID | Y |  |

### TW_TAX_DECLARE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TW_TAX_DECLARE_ID | 主键 | GUID | Y | Y |
| 4 | DECLARE_YM | 申报年月 | string(12) | Y |  |
| 5 | TEL | 申报人电话 | string(62) | Y |  |
| 6 | COMPANY_PRINCIPAL | 负责人姓名 | string(72) | Y |  |
| 7 | REGISTRATION_ADDRESS | 营业地址 | string(510) | Y |  |
| 8 | DECLARE_MODE | 申报方式 | number | Y |  |
| 9 | TW_TAXREGISTRATION_ID | 申报营业人 | GUID | Y |  |
| 10 | DECLARE_PAY_TYPE | 申报缴税方式 | number | Y |  |
| 11 | AGENT_NAME | (代理)申报人姓名 | string(72) | Y |  |
| 12 | AGENT_PERSONAL_ID_NO | (代理)申报人身份证编号 | string(20) | Y |  |
| 13 | AGENT_REGISTRATION_NO | 代理人证书登录字号 | string(100) | Y |  |
| 14 | ASSET_AMT | 销售固定资产金额 | number(23,8) | Y |  |
| 15 | IMPORT_DUTY_FREE_GOODS_AMT | 进口免税货物 | number(23,8) | Y |  |
| 16 | PURCHASE_FOREIGN_LABOR_AMT | 购买国外劳务 | number(23,8) | Y |  |
| 17 | LAST_PERIOD_REMAINING_TAX_AMT | 上期(月)累计留抵税额 | number(23,8) | Y |  |
| 18 | DRAWBACK_MODE | 退税方式 | number | Y |  |
| 19 | INVOICE_REPORT_COPY | 发票明细表(份) | number | Y |  |
| 20 | AP_CERTIFICATE_COPY1 | 进项凭证(册) | number | Y |  |
| 21 | AP_CERTIFICATE_COPY2 | 进项凭证(份) | number | Y |  |
| 22 | CUSTOMS_COPY | 海关代徵营业税缴纳证(份) | number | Y |  |
| 23 | CREDIT_COPY | 退回(出)及折让证明单(份) | number | Y |  |
| 24 | TAX_PAYMENT_COPY | 营业税缴款书申报联(份) | number | Y |  |
| 25 | ZERO_TAX_COPY | 零税率销售额清单(份) | number | Y |  |
| 26 | FOREIGNER_SUMMARY_COPY | 外籍旅客代垫税款及汇总表(份) | number | Y |  |
| 27 | FOREIGNER_DEDUCTION_LIST_COPY | 外籍旅客扣减清册(份) | number | Y |  |
| 28 | FOREIGNER_TAX_PAID_COPY | 外籍旅客代为缴纳税款清册(份) | number | Y |  |
| 29 | FLOW_STATUS | 流程状态 | number | Y |  |
| 30 | DECLARE_COMPLETE_FLAG | 申报完成标识 | number(0/1) | Y |  |
| 31 | SPECIAL_DIET_AMT1 | 特种饮食金额1 | number(23,8) | Y |  |
| 32 | SPECIAL_DIET_TAX_AMT1 | 特种饮食税额1 | number(23,8) | Y |  |
| 33 | SPECIAL_DIET_AMT2 | 特种饮食金额2 | number(23,8) | Y |  |
| 34 | SPECIAL_DIET_TAX_AMT2 | 特种饮食税额2 | number(23,8) | Y |  |
| 35 | FINANCE_INCOME_AMT | 金融业本业收入金额 | number(23,8) | Y |  |
| 36 | FINANCE_INCOME_TAX_AMT | 金融业本业收入税额 | number(23,8) | Y |  |
| 37 | EXCEPT_FINANCE_INCOME_AMT | 前项以外金融业本业收入金额 | number(23,8) | Y |  |
| 38 | EXCEPT_FINANCE_INCOME_TAX_AMT | 前项以外金融业本业收入税额 | number(23,8) | Y |  |
| 39 | REINSURANCE_INCOME_AMT | 再保收入金额 | number(23,8) | Y |  |
| 40 | REINSURANCE_INCOME_TAX_AMT | 再保收入税额 | number(23,8) | Y |  |
| 41 | DUTY_FREE_INCOME_AMT | 免税收入金额 | number(23,8) | Y |  |
| 42 | RETURN_CREDIT_AMT | 退回及折让金额 | number(23,8) | Y |  |
| 43 | RETURN_CREDIT_TAX_AMT | 退回及折让税额 | number(23,8) | Y |  |
| 44 | SALES_LAND_AMT | 销售土地金额 | number(23,8) | Y |  |
| 45 | CONTRIBUTE_TAX_AMT | 应缴税额 | number(23,8) | Y |  |
| 46 | RETURN_TAX_AMT | 应退税额 | number(23,8) | Y |  |
| 47 | UNVAT_RATE | 不得扣抵比例 | number(5,4) | Y |  |
| 48 | INV_FEE_AMT1 | 统一发票(费用)-进项税额合计(代号29) | number(23,8) | Y |  |
| 49 | INV_FEE_AMT2 | 统一发票(费用)-专供课税得扣抵 | number(23,8) | Y |  |
| 50 | INV_FEE_AMT3 | 统一发票(费用)-共同使用-小计 | number(23,8) | Y |  |
| 51 | INV_FEE_AMT4 | 统一发票(费用)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 52 | INV_FEE_AMT5 | 统一发票(费用)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 53 | INV_FEE_AMT6 | 统一发票(费用)-专供免税不得扣抵 | number(23,8) | Y |  |
| 54 | INV_ASSET_AMT1 | 统一发票(固资)-进项税额合计(代号31) | number(23,8) | Y |  |
| 55 | INV_ASSET_AMT2 | 统一发票(固资)-专供课税得扣抵 | number(23,8) | Y |  |
| 56 | INV_ASSET_AMT3 | 统一发票(固资)-共同使用-小计 | number(23,8) | Y |  |
| 57 | INV_ASSET_AMT4 | 统一发票(固资)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 58 | INV_ASSET_AMT5 | 统一发票(固资)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 59 | INV_ASSET_AMT6 | 统一发票(固资)-专供免税不得扣抵 | number(23,8) | Y |  |
| 60 | COPY3_FEE_AMT1 | 三联式(费用)-进项税额合计(代号33) | number(23,8) | Y |  |
| 61 | COPY3_FEE_AMT2 | 三联式(费用)-专供课税得扣抵 | number(23,8) | Y |  |
| 62 | COPY3_FEE_AMT3 | 三联式(费用)-共同使用-小计 | number(23,8) | Y |  |
| 63 | COPY3_FEE_AMT4 | 三联式(费用)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 64 | COPY3_FEE_AMT5 | 三联式(费用)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 65 | COPY3_FEE_AMT6 | 三联式(费用)-专供免税不得扣抵 | number(23,8) | Y |  |
| 66 | COPY3_ASSET_AMT1 | 三联式(固资)-进项税额合计(代号35) | number(23,8) | Y |  |
| 67 | COPY3_ASSET_AMT2 | 三联式(固资)-专供课税得扣抵 | number(23,8) | Y |  |
| 68 | COPY3_ASSET_AMT3 | 三联式(固资)-共同使用-小计 | number(23,8) | Y |  |
| 69 | COPY3_ASSET_AMT4 | 三联式(固资)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 70 | COPY3_ASSET_AMT5 | 三联式(固资)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 71 | COPY3_ASSET_AMT6 | 三联式(固资)-专供免税不得扣抵 | number(23,8) | Y |  |
| 72 | WITHTAX_FEE_AMT1 | 载有税额(费用)-进项税额合计(代号37) | number(23,8) | Y |  |
| 73 | WITHTAX_FEE_AMT2 | 载有税额(费用)-专供课税得扣抵 | number(23,8) | Y |  |
| 74 | WITHTAX_FEE_AMT3 | 载有税额(费用)-共同使用-小计 | number(23,8) | Y |  |
| 75 | WITHTAX_FEE_AMT4 | 载有税额(费用)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 76 | WITHTAX_FEE_AMT5 | 载有税额(费用)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 77 | WITHTAX_FEE_AMT6 | 载有税额(费用)-专供免税不得扣抵 | number(23,8) | Y |  |
| 78 | WITHTAX_ASSET_AMT1 | 载有税额(固资)-进项税额合计(代号39) | number(23,8) | Y |  |
| 79 | WITHTAX_ASSET_AMT2 | 载有税额(固资)-专供课税得扣抵 | number(23,8) | Y |  |
| 80 | WITHTAX_ASSET_AMT3 | 载有税额(固资)-共同使用-小计 | number(23,8) | Y |  |
| 81 | WITHTAX_ASSET_AMT4 | 载有税额(固资)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 82 | WITHTAX_ASSET_AMT5 | 载有税额(固资)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 83 | WITHTAX_ASSET_AMT6 | 载有税额(固资)-专供免税不得扣抵 | number(23,8) | Y |  |
| 84 | CUSTOMS_FEE_AMT1 | 海关代徵(费用)-进项税额合计(代号79) | number(23,8) | Y |  |
| 85 | CUSTOMS_FEE_AMT2 | 海关代徵(费用)-专供课税得扣抵 | number(23,8) | Y |  |
| 86 | CUSTOMS_FEE_AMT3 | 海关代徵(费用)-共同使用-小计 | number(23,8) | Y |  |
| 87 | CUSTOMS_FEE_AMT4 | 海关代徵(费用)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 88 | CUSTOMS_FEE_AMT5 | 海关代徵(费用)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 89 | CUSTOMS_FEE_AMT6 | 海关代徵(费用)-专供免税不得扣抵 | number(23,8) | Y |  |
| 90 | CUSTOMS_ASSET_AMT1 | 海关代徵(固资)-进项税额合计(代号81) | number(23,8) | Y |  |
| 91 | CUSTOMS_ASSET_AMT2 | 海关代徵(固资)-专供课税得扣抵 | number(23,8) | Y |  |
| 92 | CUSTOMS_ASSET_AMT3 | 海关代徵(固资)-共同使用-小计 | number(23,8) | Y |  |
| 93 | CUSTOMS_ASSET_AMT4 | 海关代徵(固资)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 94 | CUSTOMS_ASSET_AMT5 | 海关代徵(固资)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 95 | CUSTOMS_ASSET_AMT6 | 海关代徵(固资)-专供免税不得扣抵 | number(23,8) | Y |  |
| 96 | CREDIT_FEE_AMT1 | 退出及折让(费用)-进项税额合计(代号41) | number(23,8) | Y |  |
| 97 | CREDIT_FEE_AMT2 | 退出及折让(费用)-专供课税得扣抵 | number(23,8) | Y |  |
| 98 | CREDIT_FEE_AMT3 | 退出及折让(费用)-共同使用-小计 | number(23,8) | Y |  |
| 99 | CREDIT_FEE_AMT4 | 退出及折让(费用)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 100 | CREDIT_FEE_AMT5 | 退出及折让(费用)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 101 | CREDIT_FEE_AMT6 | 退出及折让(费用)-专供免税不得扣抵 | number(23,8) | Y |  |
| 102 | CREDIT_ASSET_AMT1 | 退出及折让(固资)-进项税额合计(代号43) | number(23,8) | Y |  |
| 103 | CREDIT_ASSET_AMT2 | 退出及折让(固资)-专供课税得扣抵 | number(23,8) | Y |  |
| 104 | CREDIT_ASSET_AMT3 | 退出及折让(固资)-共同使用-小计 | number(23,8) | Y |  |
| 105 | CREDIT_ASSET_AMT4 | 退出及折让(固资)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 106 | CREDIT_ASSET_AMT5 | 退出及折让(固资)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 107 | CREDIT_ASSET_AMT6 | 退出及折让(固资)-专供免税不得扣抵 | number(23,8) | Y |  |
| 108 | TOTAL_FEE_AMT1 | 合计(费用)-进项税额合计(代号45) | number(23,8) | Y |  |
| 109 | TOTAL_FEE_AMT2 | 合计(费用)-专供课税得扣抵 | number(23,8) | Y |  |
| 110 | TOTAL_FEE_AMT3 | 合计(费用)-共同使用-小计 | number(23,8) | Y |  |
| 111 | TOTAL_FEE_AMT4 | 合计(费用)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 112 | TOTAL_FEE_AMT5 | 合计(费用)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 113 | TOTAL_FEE_AMT6 | 合计(费用)-专供免税不得扣抵 | number(23,8) | Y |  |
| 114 | TOTAL_ASSET_AMT1 | 合计(固资)-进项税额合计(代号47) | number(23,8) | Y |  |
| 115 | TOTAL_ASSET_AMT2 | 合计(固资)-专供课税得扣抵 | number(23,8) | Y |  |
| 116 | TOTAL_ASSET_AMT3 | 合计(固资)-共同使用-小计 | number(23,8) | Y |  |
| 117 | TOTAL_ASSET_AMT4 | 合计(固资)-共同使用-比例得扣抵 | number(23,8) | Y |  |
| 118 | TOTAL_ASSET_AMT5 | 合计(固资)-共同使用-比例不得扣抵 | number(23,8) | Y |  |
| 119 | TOTAL_ASSET_AMT6 | 合计(固资)-专供免税不得扣抵 | number(23,8) | Y |  |
| 120 | AP_TAX_TOTAL | 得扣抵之进项税额合计(代号51) | number(23,8) | Y |  |
| 121 | FOREIGN_LABOR_AMT1 | 国外劳务合计(代号74) | number(23,8) | Y |  |
| 122 | FOREIGN_LABOR_AMT2 | 国外劳务-免税a | number(23,8) | Y |  |
| 123 | FOREIGN_LABOR_AMT2b | 国外劳务-免税b | number(23,8) | Y |  |
| 124 | FOREIGN_LABOR_AMT2c | 国外劳务-免税c | number(23,8) | Y |  |
| 125 | FOREIGN_LABOR_AMT3 | 国外劳务-共同使用d | number(23,8) | Y |  |
| 126 | FOREIGN_LABOR_AMT3e | 国外劳务-共同使用e | number(23,8) | Y |  |
| 127 | FOREIGN_LABOR_AMT3f | 国外劳务-共同使用f | number(23,8) | Y |  |
| 128 | FOREIGN_LABOR_AMT4 | 国外劳务-课税 | number(23,8) | Y |  |
| 129 | TAX_LIABILITY_AMT1 | 应纳税额合计(代号76) | number(23,8) | Y |  |
| 130 | TAX_LIABILITY_AMT2 | 应纳税额-免税g | number(23,8) | Y |  |
| 131 | TAX_LIABILITY_AMT2h | 应纳税额-免税h | number(23,8) | Y |  |
| 132 | TAX_LIABILITY_AMT2i | 应纳税额-免税i | number(23,8) | Y |  |
| 133 | TAX_LIABILITY_AMT3 | 应纳税额-共同使用j | number(23,8) | Y |  |
| 134 | TAX_LIABILITY_AMT3k | 应纳税额-共同使用k | number(23,8) | Y |  |
| 135 | TAX_LIABILITY_AMT3l | 应纳税额-共同使用l | number(23,8) | Y |  |
| 136 | CreateDate | 创建日期 | date | Y |  |
| 137 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 138 | ModifiedDate | 修改日期 | date | Y |  |
| 139 | CreateBy | 创建者 | GUID | Y |  |
| 140 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 141 | ModifiedBy | 修改者 | GUID | Y |  |
| 142 | Attachments | 附件 | string | Y |  |
| 143 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 144 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 145 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 146 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 147 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 148 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 149 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 150 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 151 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 152 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 153 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 154 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 155 | UDF041 | 自定义字段12 | date | Y |  |
| 156 | UDF042 | 自定义字段13 | date | Y |  |
| 157 | UDF051 | 自定义字段14 | GUID | Y |  |
| 158 | UDF052 | 自定义字段15 | GUID | Y |  |
| 159 | UDF053 | 自定义字段16 | GUID | Y |  |
| 160 | UDF054 | 自定义字段17 | GUID | Y |  |
| 161 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 162 | Version | 版本号，不要随意更改 | binary | Y |  |
| 163 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 164 | ApproveDate | 修改日期 | date | Y |  |
| 165 | ApproveBy | 修改人 | GUID | Y |  |
| 166 | Owner_Org_RTK |  | string(400) | Y |  |
| 167 | Owner_Org_ROid |  | GUID | Y |  |

### TW_TAXREGISTRATION (营业人税籍)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TW_TAXREGISTRATION_ID | 主键 | GUID | Y | Y |
| 4 | TAX_REGISTRATION_NAME | 营利事业税籍名称 | string(144) | Y |  |
| 5 | TAX_REGISTRATION_NO | 营利事业税籍编号 | string(20) | Y |  |
| 6 | COMPANY_ID_NO | 营利事业统一编号 | string(16) | Y |  |
| 7 | COMPANY_PRINCIPAL | 负责人 | string(72) | Y |  |
| 8 | REGISTRATION_AREA | 营业区域 | string(40) | Y |  |
| 9 | REGISTRATION_ADDRESS | 营业地址 | string(510) | Y |  |
| 10 | DECLARE_PERIOD_TYPE | 申报种类 | number | Y |  |
| 11 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 12 | INVALID_DATE | 注销日期 | date | Y |  |
| 13 | DECLARE_PAY_TYPE | 申报缴税方式 | number | Y |  |
| 14 | HEAD_OFFICE | 总机构 | number(0/1) | Y |  |
| 15 | HEAD_OFFICE_ID_NO | 总机构统一编号 | string(16) | Y |  |
| 16 | DIRECT_DEDUCTION_INDICATOR | 直接扣抵法 | number(0/1) | Y |  |
| 17 | DECLARE_SALES_DATA_INDICATOR | 进销资料并总公司申报 | number(0/1) | Y |  |
| 18 | DECLARE_MODE | 申报方式 | string(40) | Y |  |
| 19 | AGENT_REGISTRATION_NO | 代理人证书登录字号 | string(100) | Y |  |
| 20 | AGENT_COMPANY_ID_NO | 代理人统一编号 | string(16) | Y |  |
| 21 | AGENT_NAME | (代理)申报人姓名 | string(72) | Y |  |
| 22 | AGENT_TEL_AREA_CODE | (代理)申报人电话联络电话区码 | string(8) | Y |  |
| 23 | AGENT_TEL_NO | (代理)申报人联络电话 | string(40) | Y |  |
| 24 | AGENT_TEL_EXT | (代理)申报人联络电话分机 | string(10) | Y |  |
| 25 | AGENT_PERSONAL_ID_NO | (代理)申报人身份证编号 | string(20) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | AGENT_REGISTRATION_AREA | 代理人营业区域 | string(40) | Y |  |
| 28 | AGENT_REGISTRATION_ADDRESS | 代理人营业地址 | string(510) | Y |  |
| 29 | TAX_CENTER | 税捐稽征处名称 | string(400) | Y |  |
| 30 | TELEPHONE_NUMBER | 卖方电话 | string(30) | Y |  |
| 31 | FACSIMILE_NUMBER | 卖方传真 | string(30) | Y |  |
| 32 | EMAIL_ADDRESS | 卖方电子邮件 | string(80) | Y |  |
| 33 | ROLE_REMARK | 卖方营业人角色注记 | string(80) | Y |  |
| 34 | APPROVAL_DATE | 核准日 | date | Y |  |
| 35 | APPROVAL_WORD | 核准文 | string(80) | Y |  |
| 36 | APPROVAL_NO | 核准号 | string(40) | Y |  |
| 37 | AGENT_EMAIL_ADDRESS | (代理)申报人电子邮件 | string(72) | Y |  |
| 38 | UNDERTAKER_NAME | 承办联络人姓名 | string(72) | Y |  |
| 39 | UNDERTAKER_TEL_AREA_CODE | 承办联络人联络电话区码 | string(8) | Y |  |
| 40 | UNDERTAKER_TEL_NO | 承办联络人联络电话 | string(40) | Y |  |
| 41 | UNDERTAKER_TEL_EXT | 承办联络人电话分机 | string(10) | Y |  |
| 42 | UNDERTAKER_EMAIL_ADDRESS | 承办联络人电子邮件 | string(72) | Y |  |
| 43 | CreateDate | 创建日期 | date | Y |  |
| 44 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 45 | ModifiedDate | 修改日期 | date | Y |  |
| 46 | CreateBy | 创建者 | GUID | Y |  |
| 47 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 48 | ModifiedBy | 修改者 | GUID | Y |  |
| 49 | Attachments | 附件 | string | Y |  |
| 50 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 51 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 52 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 53 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 54 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 55 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 56 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 57 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 58 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 59 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 60 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 61 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 62 | UDF041 | 自定义字段12 | date | Y |  |
| 63 | UDF042 | 自定义字段13 | date | Y |  |
| 64 | UDF051 | 自定义字段14 | GUID | Y |  |
| 65 | UDF052 | 自定义字段15 | GUID | Y |  |
| 66 | UDF053 | 自定义字段16 | GUID | Y |  |
| 67 | UDF054 | 自定义字段17 | GUID | Y |  |
| 68 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 69 | Version | 版本号，不要随意更改 | binary | Y |  |
| 70 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 71 | ApproveDate | 修改日期 | date | Y |  |
| 72 | ApproveBy | 修改人 | GUID | Y |  |
| 73 | Owner_Org_RTK |  | string(400) | Y |  |
| 74 | Owner_Org_ROid |  | GUID | Y |  |