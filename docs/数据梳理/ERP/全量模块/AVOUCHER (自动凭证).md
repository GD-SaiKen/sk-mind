---
module: "AVOUCHER"
name_zh: "自动凭证"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 141
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# AVOUCHER (自动凭证)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 141

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


- **AVOUCHER_TEMPLATE (自动凭证模板)**
- **AVOUCHER_TEMPLATE_D (自动凭证模板单身)**
- **AVOUCHER_TEMPLATE_SD (自动凭证模板子单身)**


---


---


> Tables: 3

### AVOUCHER_TEMPLATE (自动凭证模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | AVOUCHER_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | TEMPLATE_CODE | 模板编号 | string(12) | Y |  |
| 5 | TEMPLATE_NAME | 模板名称 | string(40) | Y |  |
| 6 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 9 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 10 | PRIORITY | 优先级 | number | Y |  |
| 11 | GROUP_NO | 分组 | string(20) | Y |  |
| 12 | VOUCHER_TYPE_ID | 凭证类型 | GUID | Y |  |
| 13 | CONSOLIDATED_FLAG | 合并相同的转入类分录 | number(0/1) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
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
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |

### AVOUCHER_TEMPLATE_D (自动凭证模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ABSTRACT_DESCRIPTION | 摘要信息 | string(510) | Y |  |
| 3 | TFO_ACCOUNT_CODE_ID | 转出科目 | GUID | Y |  |
| 4 | TFO_RATE | 转出金额比率 | number(5,4) | Y |  |
| 5 | ALLOC_RATE_TYPE | 分摊比率类型 | number | Y |  |
| 6 | ALLOC_RATE | 分摊比率合计 | number(5,4) | Y |  |
| 7 | TFO_DIRECTION | 转出方向 | number | Y |  |
| 8 | TFO_FORMULA | 取数公式 | string | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | ATFO_AUXILIARY_ITEM | 转出科目辅助核算项目 | string(20) | Y |  |
| 11 | ATFO_BALANCE_DIRECTION | 转出科目余额方向 | number | Y |  |
| 12 | AVOUCHER_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
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
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | AVOUCHER_TEMPLATE_ID |  | GUID | Y |  |

### AVOUCHER_TEMPLATE_SD (自动凭证模板子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TFI_ACCOUNT_CODE_ID | 转入科目 | GUID | Y |  |
| 3 | TFI_CURRENCY | 转入货币 | number | Y |  |
| 4 | FIXED_ALLOC_RATE | 固定分摊比率 | number(5,4) | Y |  |
| 5 | VARIABLE_ALLOC_FACTOR | 变动分摊比率因子 | string | Y |  |
| 6 | TFI_DIRECTION | 转入方向 | number | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | TFI_ADMIN_UNIT_AREA | 转入部门范围 | number | Y |  |
| 9 | TFI_EMPLOYEE_AREA | 转入人员范围 | number | Y |  |
| 10 | TFI_CUSTOMER_AREA | 转入客户范围 | number | Y |  |
| 11 | TFI_SUPPLIER_AREA | 转入供应商范围 | number | Y |  |
| 12 | TFI_SALES_CENTER_AREA | 转入销售域范围 | number | Y |  |
| 13 | TFI_SUPPLY_CENTER_AREA | 转入采购域范围 | number | Y |  |
| 14 | TFI_PLANT_AREA | 转入工厂/储运范围 | number | Y |  |
| 15 | TFI_AUXILIARY_ITEM1_AREA | 转入自定义辅助核算项目1范围 | number | Y |  |
| 16 | TFI_AUXILIARY_ITEM2_AREA | 转入自定义辅助核算项目2范围 | number | Y |  |
| 17 | TFI_ADMIN_UNIT_ID | 转入部门 | GUID | Y |  |
| 18 | TFI_EMPLOYEE_ID | 转入人员 | GUID | Y |  |
| 19 | TFI_CUSTOMER_ID | 转入客户 | GUID | Y |  |
| 20 | TFI_SUPPLIER_ID | 转入供应商 | GUID | Y |  |
| 21 | TFI_SALES_CENTER_ID | 转入销售域 | GUID | Y |  |
| 22 | TFI_SUPPLY_CENTER_ID | 转入采购域 | GUID | Y |  |
| 23 | TFI_PLANT_ID | 转入工厂/储运 | GUID | Y |  |
| 24 | ATFI_AUXILIARY_ITEM | 转入科目辅助核算项目 | string(20) | Y |  |
| 25 | ATFI_CURRENCY_AREA | 转入科目核算货币范围 | number | Y |  |
| 26 | ATFI_CURRENCY_ID | 转入科目核算货币 | GUID | Y |  |
| 27 | AVOUCHER_TEMPLATE_SD_ID | 主键 | GUID | Y | Y |
| 28 | TFI_AUXILIARY_ITEM1_ID | 转入自定义辅助核算项目1 | GUID | Y |  |
| 29 | TFI_AUXILIARY_ITEM2_ID | 转入自定义辅助核算项目2 | GUID | Y |  |
| 30 | CALCULATE_FLAG | 金额转换 | number | Y |  |
| 31 | TFI_PROJECT_AREA | 转入项目范围 | number | Y |  |
| 32 | TFI_PROJECT_ID | 转入项目 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | AVOUCHER_TEMPLATE_D_ID |  | GUID | Y |  |