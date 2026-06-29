---
module: "SUPPLIER"
name_zh: "供应商"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 7
columns: 361
category: purchase
semantic_object: "Supplier/供应商"
original_tables: 8
filtered_out: 0
tags: ["ERP", "E10", "purchase", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# SUPPLIER (供应商) - Supplier/供应商

> [!info] Phase 1 Core Module
> Semantic Object: Supplier/供应商
> Kept: 7 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 0

## Related Modules

- [[../modules/PURCHASE (采购管理).md|PURCHASE (采购管理)]]
- [[../modules/PO (采购订单).md|PO (采购订单)]]
- [[../modules/REQUISITION (请购管理).md|REQUISITION (请购管理)]]
- [[../modules/IMPORT (进口管理).md|IMPORT (进口管理)]]

---

## Tables

- **SUPPLIER_ADDRESS (供应商地址)**
- **SUPPLIER_BANK (供应商银行)**
- **SUPPLIER_CONTACT (供应商联系人)**
- **SUPPLIER_FI (供应商财务)**
- **SUPPLIER_FICATEGORY (供应商会计分类)**
- **SUPPLIER_PROPERTY (供应商扩展属性)**
- **SUPPLIER_PURCHASE (供应商采购信息)**

---

## Table Details

### SUPPLIER_ADDRESS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SUPPLIER_ADDRESS_ID | 主键 | GUID | Y | Y |
| 2 | ADDRESS |  | string(510) | Y |  |
| 3 | MAIN_ORDER_ADDR | 主要接单地址 | number(0/1) | Y |  |
| 4 | MAIN_DELIVERY_ADDR | 主要发货地址 | number(0/1) | Y |  |
| 5 | MAIN_INVOICE_ADDR | 主要结算地址 | number(0/1) | Y |  |
| 6 | MAIN_RECEIVE_ADDR | 主要收款地址 | number(0/1) | Y |  |
| 7 | POSTCODE | 邮编 | string(40) | Y |  |
| 8 | TELEPHONE | 电话 | string(40) | Y |  |
| 9 | FAX | 传真 | string(40) | Y |  |
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
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SUPPLIER_BUSINESS_ID |  | GUID | Y |  |


### SUPPLIER_BANK

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SUPPLIER_BANK_ID | 主键 | GUID | Y | Y |
| 2 | ACCOUNT_CODE | 账号 | string(60) | Y |  |
| 3 | ACCOUNT_NAME | 账户名 | string(80) | Y |  |
| 4 | MAIN | 主要 | number(0/1) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | BANK | 开户银行简称 | string(200) | Y |  |
| 7 | BANK_FULLNAME | 开户银行全称 | string(400) | Y |  |
| 8 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 9 | REMITTANCE_NOTICE_MODE | 汇款通知方式 | number | Y |  |
| 10 | NOTICE_FAX | 通知传真号 | string(40) | Y |  |
| 11 | NOTICE_EMAIL | 通知电子邮件 | string(72) | Y |  |
| 12 | NOTIC_IDENTIFY_TYPE | 通知识别类型 | number | Y |  |
| 13 | NOTIC_IDENTIFY_NO | 通知识别编号 | string(20) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | SUPPLIER_FI_ID |  | GUID | Y |  |


### SUPPLIER_CONTACT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SUPPLIER_CONTACT_ID | 主键 | GUID | Y | Y |
| 2 | CONTACT | 联系人 | string(72) | Y |  |
| 3 | MIAN_ORDER_CONTACT | 主要接单人 | number(0/1) | Y |  |
| 4 | MAIN_DELIVERY_CONTACT | 主要发货人 | number(0/1) | Y |  |
| 5 | MAIN_INVOICE_CONTACT | 主要结算人 | number(0/1) | Y |  |
| 6 | MAIN_RECEIVE_CONTACT | 主要收款人 | number(0/1) | Y |  |
| 7 | MOBILE_PHONE |  | string(40) | Y |  |
| 8 | TELEPHONE | 电话 | string(40) | Y |  |
| 9 | FAX | 传真 | string(40) | Y |  |
| 10 | EMAIL | 电子邮箱 | string(120) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | SUPPLIER_BUSINESS_ID |  | GUID | Y |  |


### SUPPLIER_FI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SUPPLIER_FI_ID | 主键 | GUID | Y | Y |
| 4 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 7 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 8 | CURRENCY_ID | 货币 | GUID | Y |  |
| 9 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 10 | SUPPLIER_FICATEGORY_ID | 主键 | GUID | Y |  |
| 11 | DRAWEE_ID | 付款业务员 | GUID | Y |  |
| 12 | NOTE_RECEIPT_MODE | 票据寄领方式 | number | Y |  |
| 13 | CHARGE_BURDEN_MODE | 手续费负担方式 | number | Y |  |
| 14 | NOTE_FULL_NAME | 票据抬头全称 | string(80) | Y |  |
| 15 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 16 | OTHER_CLEARING_HOUSE_FLAG | 外埠交换所 | number(0/1) | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |


### SUPPLIER_FICATEGORY (供应商会计分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SUPPLIER_FICATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | SUPPLIER_FICATEGORY_CODE | SUPPLIER_FICATEGORY_CODE | string(12) | Y |  |
| 5 | SUPPLIER_FICATEGORY_NAME | 分类名称 | string(40) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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


### SUPPLIER_PROPERTY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SUPPLIER_PROPERTY_ID | 主键 | GUID | Y | Y |
| 2 | PROPERTY_VALUE | 属性值 | string(20) | Y |  |
| 3 | REMARK |  | string(510) | Y |  |
| 4 | PARENT_SUPPLIER_ID | 供应商 | GUID | Y |  |
| 5 | BP_PROPERTY_ID | 属性 | GUID | Y |  |
| 6 | PROPERTY_VALUE_ID | 属性值ID | GUID | Y |  |
| 7 | PROPERTY_VALUE_DESC | 属性值描述 | string(400) | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ORG_ID_RTK |  | string(400) | Y |  |
| 37 | ORG_ID_ROid |  | GUID | Y |  |
| 38 | SUPPLIER_BUSINESS_ID |  | GUID | Y |  |


### SUPPLIER_PURCHASE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SUPPLIER_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 5 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 6 | DEPOSIT_RATE | 订金比例 | number(5,4) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | VMI | VMI业务 | number(0/1) | Y |  |
| 9 | SETTLEMENT_BASE_DATE_TYPE | 结算起算日类型 | string(40) | Y |  |
| 10 | IS_MONTH_PLUS | 加月 | number(0/1) | Y |  |
| 11 | MONTHS | 月数 | number | Y |  |
| 12 | IS_DAY_PLUS | 加日 | number(0/1) | Y |  |
| 13 | DAYS | 日数 | number | Y |  |
| 14 | IS_EVERY_DAY | 逢 | number(0/1) | Y |  |
| 15 | EVERY_DAY | 逢某日 | number | Y |  |
| 16 | DESTROYED_PRICE_CONTROL | 破坏量计价 | number(0/1) | Y |  |
| 17 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 18 | CURRENCY_ID | 币种 | GUID | Y |  |
| 19 | CS_TAX_CLASSIFICATION_ID | 税分类 | GUID | Y |  |
| 20 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 21 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 22 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 23 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 24 | DIRECT_INVOICING_INDICATOR | 随货附票 | number(0/1) | Y |  |
| 25 | DEL_CLASS | 交期等级 | string(2) | Y |  |
| 26 | QUL_CLASS | 质量等级 | string(2) | Y |  |
| 27 | ABC_CLASS | ABC等级 | string(2) | Y |  |
| 28 | TAX_MODE | 税额计算方式 | string(40) | Y |  |
| 29 | TAX_ID | 税种 | GUID | Y |  |
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
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | Attachments | 附件 | string | Y |  |
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | Owner_Org_RTK |  | string(400) | Y |  |
| 61 | Owner_Org_ROid |  | GUID | Y |  |
