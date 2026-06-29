---
module: "TAX"
name_zh: "税务管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 13
columns: 588
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# TAX (税务管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 13 | Columns: 588

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


- **TAX_CATEGORY (税目信息)**
- **TAX_INV_CATEGORY_RATE (税务发票种类税率)**
- **TAX_INV_CATEGORY_RATE_D (税务发票种类税率单身)**
- **TAX_INVOICE (税务发票)**
- **TAX_INVOICE_APPDISC (税务发票折扣分摊)**
- **TAX_INVOICE_BASEDATA (税务发票基础数据)**
- **TAX_INVOICE_CATEGORY (税务发票种类)**
- **TAX_INVOICE_D (税务发票单身)**
- **TAX_ITEM (税务品号)**
- **TAX_ITEM_MATRIX (税务品号关系)**
- **TAX_MATRIX (税分类矩阵)**
- **TAX_REGION (税区)**


---


---


> Tables: 13

### TAX (税种税率)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_ID | 主键 | GUID | Y | Y |
| 4 | TAX_CODE | 税种编号 | string(12) | Y |  |
| 5 | TAX_NAME | 税种名称 | string(60) | Y |  |
| 6 | TAX_RATE |  | number(5,4) | Y |  |
| 7 | VAT_INDICATOR | 增值税 | number(0/1) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | TAX_CALCULATE_MODE | 计税方式 | number | Y |  |
| 10 | TAX_REGION_ID | 税区 | GUID | Y |  |
| 11 | TAXABLE_CATEGORY | 课税类别 | number | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
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
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_CATEGORY (税目信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | TAX_CATEGORY_CODE | 编号 | string(8) | Y |  |
| 5 | TAX_CATEGORY_NAME | 名称 | string(60) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | TAX_REGION_ID | 税区 | GUID | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
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
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_INV_CATEGORY_RATE (税务发票种类税率)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_INV_CATEGORY_RATE_ID | 主键 | GUID | Y | Y |
| 4 | CEILING_INDICATOR | 税务发票限额标识 | number(0/1) | Y |  |
| 5 | CEILING_AMT | 税务发票限额 | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | MAXLINE_INDICATOR | 税务发票行数控制标识 | number(0/1) | Y |  |
| 8 | MAXLINE | 税务发票行数 | number | Y |  |
| 9 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 10 | SINGLE_TAX_INDICATOR | 统一税种税率标识 | number(0/1) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_INV_CATEGORY_RATE_D (税务发票种类税率单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TAX_INV_CATEGORY_RATE_D_ID | 主键 | GUID | Y | Y |
| 3 | TRANS_AREA | 业务范围 | number | Y |  |
| 4 | DEFAULT_INDICATOR | 默认标识 | number(0/1) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | TAX_ID | 税种税率 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | TAX_INV_CATEGORY_RATE_ID |  | GUID | Y |  |

### TAX_INVOICE (税务发票)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TAX_INVOICE_ID | 主键 | GUID | Y | Y |
| 7 | INVOICE_CODE | 发票类别代码 | string(20) | Y |  |
| 8 | INVOICE_DATE | 税控开票日期 | date | Y |  |
| 9 | INVOICE_NO | 税控发票号 | string(20) | Y |  |
| 10 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 11 | TAX_RATE |  | number(5,4) | Y |  |
| 12 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 13 | INVOICE_LIST_INDICATOR | 发票清单 | number(0/1) | Y |  |
| 14 | POSITIVE_INVOICE_CODE | 正数发票代码 | string(20) | Y |  |
| 15 | POSITIVE_INVOICE_NO | 正数发票号 | string(20) | Y |  |
| 16 | NEGATIVE_INVOICE_NOTICE_NO | 负数发票通知单号 | string(40) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | SELLER_NAME | 销货单位名称 | string(100) | Y |  |
| 19 | CUSTOMER_NAME | 购货单位名称 | string(100) | Y |  |
| 20 | CUSTOMER_TAX_REGISTER_NO | 购货单位纳税人识别号 | string(40) | Y |  |
| 21 | CUSTOMER_ADDRESS_TEL |  | string(100) | Y |  |
| 22 | CUSTOMER_BANK_BANKACCOUNT |  | string(100) | Y |  |
| 23 | SELLER_TAX_REGISTER_NO | 销货单位纳税人识别号 | string(40) | Y |  |
| 24 | SELLER_ADDRESS_TEL | 销货单位纳税地址和电话 | string(100) | Y |  |
| 25 | SELLER_BANK_BANKACCOUNT | 销货单位纳税开户行和银行账号 | string(100) | Y |  |
| 26 | ADJ_RECEIVABLE_INDICATOR | 生成税务调整应收单标识 | number(0/1) | Y |  |
| 27 | INVOICE_TYPE | 发票类型 | number | Y |  |
| 28 | EXPORT_INDICATOR | 导入税控标识 | number(0/1) | Y |  |
| 29 | INVOICE_PRINT_INDICATOR | 发票打印标识(税控) | number(0/1) | Y |  |
| 30 | INVOICE_LIST_PRINT_INDICATOR | 发票清单打印标识(税控) | number(0/1) | Y |  |
| 31 | INSTALLMENT_INDICATOR | 分期标识 | number(0/1) | Y |  |
| 32 | APP_DIFF_INDICATOR | 分摊差异 | number(0/1) | Y |  |
| 33 | INVOICE_APPROVE_NDICATOR | 税控作废标识 | number(0/1) | Y |  |
| 34 | BASE_GEN_AMT_UNTAX_FC |  | number(23,8) | Y |  |
| 35 | BASE_GEN_TAX_FC | 基础数据-一般商品-税额合计 | number(23,8) | Y |  |
| 36 | BASE_DISC_AMT_UNTAX_FC | 基础数据-折扣类型-无税金额合计 | number(23,8) | Y |  |
| 37 | BASE_DISC_TAX_FC | 基础数据-折扣类型-税额合计 | number(23,8) | Y |  |
| 38 | INV_GEN_AMT_UNTAX_FC | 发票信息-一般商品-无税金额合计 | number(23,8) | Y |  |
| 39 | INV_GEN_TAX_FC | 发票信息-一般商品-税额合计 | number(23,8) | Y |  |
| 40 | INV_DISC_AMT_UNTAX_FC | 发票信息-折扣类型-无税金额合计 | number(23,8) | Y |  |
| 41 | INV_DISC_TAX_FC | 发票信息-折扣类型-税额合计 | number(23,8) | Y |  |
| 42 | TC_AMT_UNTAX_FC | 税控-无税金额总计 | number(23,8) | Y |  |
| 43 | TC_TAX_FC | 税控-税额总计 | number(23,8) | Y |  |
| 44 | RECEIVABLE_DOC_ID | 应收单单号 | GUID | Y |  |
| 45 | CURRENCY_ID | 币种 | GUID | Y |  |
| 46 | TAX_ID | 税种税率 | GUID | Y |  |
| 47 | CUSTOMER_ID | 购货单位编码 | GUID | Y |  |
| 48 | ADJ_RECEIVABLE_ID | 税务调整应收单单号 | GUID | Y |  |
| 49 | PrintCount | 打印次数 | number | Y |  |
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
| 68 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 69 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 70 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 71 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 72 | CreateDate | 创建日期 | date | Y |  |
| 73 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 74 | ModifiedDate | 修改日期 | date | Y |  |
| 75 | CreateBy | 创建者 | GUID | Y |  |
| 76 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 77 | ModifiedBy | 修改者 | GUID | Y |  |
| 78 | Attachments | 附件 | string | Y |  |
| 79 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 80 | Version | 版本号，不要随意更改 | binary | Y |  |
| 81 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 82 | ApproveDate | 修改日期 | date | Y |  |
| 83 | ApproveBy | 修改人 | GUID | Y |  |
| 84 | Owner_Org_RTK |  | string(400) | Y |  |
| 85 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_INVOICE_APPDISC (税务发票折扣分摊)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TAX_INVOICE_APPDISC_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_INVOICE_TYPE | 品号发票类型 | number | Y |  |
| 4 | TAX_ITEM_NAME | 税务品名 | string(120) | Y |  |
| 5 | TAX_ITEM_SPECIFICATION |  | string(510) | Y |  |
| 6 | QTY |  | number(16,6) | Y |  |
| 7 | PRICE | 單價 | number(23,8) | Y |  |
| 8 | TISSUE_INVOICE_AMT_UNTAX_TC | 基础数据-品号发票类型-开票无税金额汇总(原币) | number(23,8) | Y |  |
| 9 | TISSUE_INVOICE_TAX_TC | 基础数据-品号发票类型-开票税额汇总(原币) | number(23,8) | Y |  |
| 10 | TISSUE_INVOICE_AMT_TC | 基础数据-品号发票类型-开票价税合计汇总(原币) | number(23,8) | Y |  |
| 11 | TISSUE_INVOICE_AMT_UNTAX_FC | 基础数据-品号发票类型-开票无税金额汇总(本币) | number(23,8) | Y |  |
| 12 | TISSUE_INVOICE_TAX_FC | 基础数据-品号发票类型-开票税额汇总(本币) | number(23,8) | Y |  |
| 13 | TISSUE_INVOICE_AMT_FC | 基础数据-品号发票类型-开票价税合计汇总(本币) | number(23,8) | Y |  |
| 14 | DISC_AMT_UNTAX_FC | 分摊的折扣类型-无税金额 | number(23,8) | Y |  |
| 15 | DISC_TAX_FC | 分摊的折扣类型-税额 | number(23,8) | Y |  |
| 16 | DISC_AMT_FC | 分摊的折扣类型-价税合计 | number(23,8) | Y |  |
| 17 | APPORTIONMENT_RATE | 分摊比率 | number(5,4) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | UNIT_ID | 单位 | GUID | Y |  |
| 20 | TAX_CATEGORY_ID | 主键 | GUID | Y |  |
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
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | TAX_INVOICE_ID |  | GUID | Y |  |

### TAX_INVOICE_BASEDATA (税务发票基础数据)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TAX_INVOICE_BASEDATA_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 类型 | number | Y |  |
| 4 | RECEIVABLE_LINE_SEQNO | 应收单单身序号 | number | Y |  |
| 5 | ITEM_TRANS_TYPE | 品号交易类型 | string(40) | Y |  |
| 6 | ITEM_INVOICE_TYPE | 品号发票类型 | number | Y |  |
| 7 | ITEM_NAME |  | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | QTY |  | number(16,6) | Y |  |
| 10 | PRICE |  | number(23,8) | Y |  |
| 11 | ISSUE_INVOICE_AMT_UNTAX_TC | 开票无税金额(原币) | number(23,8) | Y |  |
| 12 | ISSUE_INVOICE_TAX_TC | 开票税额(原币) | number(23,8) | Y |  |
| 13 | ISSUE_INVOICE_AMT_TC | 开票价税合计(原币) | number(23,8) | Y |  |
| 14 | ISSUE_INVOICE_AMT_UNTAX_FC | 开票无税金额(本币) | number(23,8) | Y |  |
| 15 | ISSUE_INVOICE_TAX_FC | 开票税额(本币) | number(23,8) | Y |  |
| 16 | ISSUE_INVOICE_AMT_FC | 开票价税合计(本币) | number(23,8) | Y |  |
| 17 | TAX_ITEM_SOURCE | 税务品号来源 | number | Y |  |
| 18 | TAX_ITEM_NAME | 税务品名 | string(120) | Y |  |
| 19 | TAX_ITEM_SPECIFICATION | 税务规格型号 | string(510) | Y |  |
| 20 | TCDIFF_AMT_UNTAX_FC | 分摊的税控差异-无税金额 | number(23,8) | Y |  |
| 21 | TCDIFF_TAX_FC | 分摊的税控差异-税额 | number(23,8) | Y |  |
| 22 | TCDIFF_AMT_FC | 分摊的税控差异-价税合计 | number(23,8) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | ITEM_ID | 品号 | GUID | Y |  |
| 25 | UNIT_ID | 单位 | GUID | Y |  |
| 26 | TAX_CATEGORY_ID | 税目 | GUID | Y |  |
| 27 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 28 | RECEIVABLE_DOC_D_ID | 应收单单身主键 | GUID | Y |  |
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
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | TAX_INVOICE_ID |  | GUID | Y |  |

### TAX_INVOICE_CATEGORY (税务发票种类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_INVOICE_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | TAX_INVOICE_CATEGORY_CODE | 税务发票种类编号 | string(12) | Y |  |
| 5 | TAX_INVOICE_CATEGORY_NAME | 税务发票种类名称 | string(60) | Y |  |
| 6 | TRANS_AREA | 业务范围 | number | Y |  |
| 7 | DEDUCTIBLE_INDICATOR | 可抵扣VAT标识 | number(0/1) | Y |  |
| 8 | EPD_INDICATOR | 费用应付单专用 | number(0/1) | Y |  |
| 9 | TAX_REGION_ID | 税区 | GUID | Y |  |
| 10 | TAX_INVOICE_NATURE | 性质 | string(40) | Y |  |
| 11 | TAX_INVOICE_CATEGORY_DISC_ID | 折让税务发票种类 | GUID | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
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
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_INVOICE_D (税务发票单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TAX_INVOICE_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_INVOICE_TYPE | 品号发票类型 | number | Y |  |
| 4 | TAX_ITEM_NAME | 税务品名 | string(120) | Y |  |
| 5 | TAX_ITEM_SPECIFICATION | 税务规格型号 | string(510) | Y |  |
| 6 | QTY |  | number(16,6) | Y |  |
| 7 | TAX_RATE |  | number(5,4) | Y |  |
| 8 | PRICE_UNTAX | 无税单价 | number(23,11) | Y |  |
| 9 | PRICE_INTAX | 含税单价 | number(23,11) | Y |  |
| 10 | AMT_UNTAX_FC | 无税金额 | number(23,8) | Y |  |
| 11 | TAX_FC | 税额 | number(23,8) | Y |  |
| 12 | AMT_FC | 价税合计 | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | TAX_CATEGORY_ID | 税目 | GUID | Y |  |
| 15 | UNIT_ID | 单位 | GUID | Y |  |
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
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | TAX_INVOICE_ID |  | GUID | Y |  |

### TAX_ITEM (税务品号)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | TAX_ITEM_CODE | 税务品号 | string(80) | Y |  |
| 5 | TAX_ITEM_NAME | 税务品名 | string(120) | Y |  |
| 6 | TAX_ITEM_SPECIFICATION | 税务规格型号 | string(510) | Y |  |
| 7 | TAX_ITEM_TYPE | 税务品号类型 | number | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_ITEM_MATRIX (税务品号关系)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_ITEM_MATRIX_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | MATRIX_TYPE | 类型 | number | Y |  |
| 6 | TAX_ITEM_ID | 税务品号 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
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
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |
| 39 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE_ID_ROid |  | GUID | Y |  |

### TAX_MATRIX (税分类矩阵)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_MATRIX_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_TAX_CLASSIFICATION_ID | 存货/服务税分类编号 | GUID | Y |  |
| 6 | CS_TAX_CLASSIFICATION_ID | 客户/供应商税分类编号 | GUID | Y |  |
| 7 | TAX_ID | 税种编号 | GUID | Y |  |
| 8 | TAX_REGION_ID | 税区 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### TAX_REGION (税区)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TAX_REGION_ID | 主键 | GUID | Y | Y |
| 4 | TAX_REGION_CODE | 税区编号 | string(12) | Y |  |
| 5 | TAX_REGION_NAME | 税区名称 | string(60) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
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
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | Owner_Org_RTK |  | string(400) | Y |  |
| 34 | Owner_Org_ROid |  | GUID | Y |  |