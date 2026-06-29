---
module: "FVOUCHER"
name_zh: "分摊凭证"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 127
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# FVOUCHER (分摊凭证)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 127

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


- **FVOUCHER_TEMPLATE (常用凭证模板)**
- **FVOUCHER_TEMPLATE_D (常用凭证模板单身)**
- **FVOUCHER_TEMPLATE_SD (常用凭证模板子单身)**


---


---


> Tables: 3

### FVOUCHER_TEMPLATE (常用凭证模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | FVOUCHER_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | TEMPLATE_CODE | 模板编号 | string(12) | Y |  |
| 5 | TEMPLATE_NAME | 模板名称 | string(40) | Y |  |
| 6 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 7 | VOUCHER_TYPE_ID | 凭证类型 | GUID | Y |  |
| 8 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 9 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 10 | DR_AMT | 借方本币合计 | number(23,8) | Y |  |
| 11 | CR_AMT | 贷方本币合计 | number(23,8) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### FVOUCHER_TEMPLATE_D (常用凭证模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FVOUCHER_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 3 | ABSTRACT_DESCRIPTION | 摘要 | string(510) | Y |  |
| 4 | ACCOUNT_CODE_ID | 科目 | GUID | Y |  |
| 5 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 6 | TRANS_CURRENCY_ID | 交易货币 | GUID | Y |  |
| 7 | EXG_SOURCE | 汇率来源 | number | Y |  |
| 8 | EXG_TYPE | 汇率类型 | number | Y |  |
| 9 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 10 | TRANS_QTY | 数量 | number(16,6) | Y |  |
| 11 | TRANS_PRICE | 单价 | number(23,8) | Y |  |
| 12 | AMT_TC | 原币金额 | number(23,8) | Y |  |
| 13 | AMT_FC | 本币金额 | number(23,8) | Y |  |
| 14 | ACCCODE_ROLE | 科目性质 | number | Y |  |
| 15 | AUXILIARY_ITEM | 辅助核算项目 | string(20) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 18 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 19 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 20 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 21 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 22 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 23 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 24 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 25 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 26 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 27 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | FVOUCHER_TEMPLATE_ID |  | GUID | Y |  |

### FVOUCHER_TEMPLATE_SD (常用凭证模板子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FVOUCHER_TEMPLATE_SD_ID | 主键 | GUID | Y | Y |
| 3 | CASHFLOW_AMT | 现金流量金额 | number(23,8) | Y |  |
| 4 | CASHFLOW_ITEM_ID | 现金流量项目 | GUID | Y |  |
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
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | FVOUCHER_TEMPLATE_D_ID |  | GUID | Y |  |