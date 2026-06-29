---
module: "CUSTOMER"
name_zh: "客户管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 24
columns: 1142
category: crm
tags: ["ERP", "E10", "crm"]
created: 2026-06-25 10:52

---

# CUSTOMER (客户管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 24 | Columns: 1142

## Related Modules

- [[BP (业务伙伴)|BP (业务伙伴)]]
- [[CARD (卡券管理)|CARD (卡券管理)]]
- [[CRM (客户关系)|CRM (客户关系)]]
- [[MEMBER (会员管理)|MEMBER (会员管理)]]
- [[REPAIR (维修管理)|REPAIR (维修管理)]]
- [[REPLACE (替换管理)|REPLACE (替换管理)]]
- [[SERVICE (售后服务)|SERVICE (售后服务)]]
- [[TICKET (票券管理)|TICKET (票券管理)]]

---

## Tables


- **CUSTOMER_ADDRESS (客户地址信息)**
- **CUSTOMER_BANK (客户银行信息)**
- **CUSTOMER_CONTACT (客户联系人信息)**
- **CUSTOMER_CREDIT (客户信用)**
- **CUSTOMER_CREDIT_D (客户信用-客户群)**
- **CUSTOMER_CREDIT_LINE (客户信用信息)**
- **CUSTOMER_CREDIT_RATING (客户信用等级信息)**
- **CUSTOMER_CREDIT_TEMPORARY (客户信用-临时额度)**
- **CUSTOMER_FI (客户财务信息)**
- **CUSTOMER_FICATEGORY (客户会计分类)**
- **CUSTOMER_ITEM (客户品号)**
- **CUSTOMER_PRICE_STRATEGY (客户取价策略使用记录)**
- **CUSTOMER_PROPERTY**
- **CUSTOMER_PROPERTY_VIEW (CPV)**
- **CUSTOMER_RECEIVE (客户赊销收款单)**
- **CUSTOMER_RECEIVE_D (客户赊销收款单身)**
- **CUSTOMER_RECEIVEABLE (客户赊销应收总帐)**
- **CUSTOMER_RECEIVEABLE_D (客户赊销应收明细帐)**
- **CUSTOMER_SALES (客户业务信息)**
- **CUSTOMER_SETTLE (客户赊销结算单)**
- **CUSTOMER_SETTLE_D (客户赊销结算单单身)**
- **CUSTOMER_SHIPPING_MARK (客户唛头信息)**
- **CUSTOMER_SUPPLIER (客户供应商关系)**


---


---


> Tables: 24

### CUSTOMER (客户通用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | CUSTOMER_CODE | 客户编号 | string(20) | Y |  |
| 5 | CUSTOMER_NAME | 客户简称 | string(40) | Y |  |
| 6 | SHORTCUT |  | string(40) | Y |  |
| 7 | CAPITAL | 注册资金 | number(23,8) | Y |  |
| 8 | TURNOVER | 年营业额 | number(23,8) | Y |  |
| 9 | STAFFS | 员工人数 | number | Y |  |
| 10 | SETUP_DATE | 开业日期 | date | Y |  |
| 11 | SHUTOUT_DATE | 停业日期 | date | Y |  |
| 12 | BRANCHES | 分店数 | number | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CUSTOMER_FULL_NAME | 客户全称 | string(144) | Y |  |
| 15 | PRINCIPAL | 负责人 | string(40) | Y |  |
| 16 | REG_ADDRESS | 注册地址 | string(510) | Y |  |
| 17 | INNER_CUSTOMER | 内部客户 | number(0/1) | Y |  |
| 18 | BP_CLUSTER_ID | 客户群组 | GUID | Y |  |
| 19 | CAPITAL_CURRENCY_ID | 注册资金币种 | GUID | Y |  |
| 20 | TURNOVER_CURRENCY_ID | 年营业额币种 | GUID | Y |  |
| 21 | INNER_COMPANY_ID | 內部公司 | GUID | Y |  |
| 22 | GENERAL_CURRENCY_ID | 通用币种 | GUID | Y |  |
| 23 | CRM_CUSTOMER_WEBSITE | 网址 | string(144) | Y |  |
| 24 | CRM_PARENT_CUSTOMER_ID | 上级客户 | GUID | Y |  |
| 25 | CRM_POTENTIAL_CUSTOMER | 潜客 | number(0/1) | Y |  |
| 26 | CRM_POTEN_CUSTOMER_CODE | 潜客编号 | string(20) | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 35 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 36 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 37 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 38 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 39 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 40 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 41 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 42 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 43 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 44 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 45 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 46 | UDF041 | 自定义字段12 | date | Y |  |
| 47 | UDF042 | 自定义字段13 | date | Y |  |
| 48 | UDF051 | 自定义字段14 | GUID | Y |  |
| 49 | UDF052 | 自定义字段15 | GUID | Y |  |
| 50 | UDF053 | 自定义字段16 | GUID | Y |  |
| 51 | UDF054 | 自定义字段17 | GUID | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | Owner_Org_RTK |  | string(400) | Y |  |
| 58 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_ADDRESS (客户地址信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_ADDRESS_ID | 主键 | GUID | Y | Y |
| 2 | ADDRESS |  | string(510) | Y |  |
| 3 | MAIN_ORDER_ADDR | 主要订单地址 | number(0/1) | Y |  |
| 4 | MAIN_SHIP_TO_ADDR | 主要收货地址 | number(0/1) | Y |  |
| 5 | MAIN_INVOICE_ADDR | 主要发票邮寄地址 | number(0/1) | Y |  |
| 6 | MAIN_PAY_ADDR | 主要付款地址 | number(0/1) | Y |  |
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
| 39 | CUSTOMER_BUSINESS_ID |  | GUID | Y |  |

### CUSTOMER_BANK (客户银行信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_BANK_ID | 主键 | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | ACCOUNT_CODE | 账号 | string(60) | Y |  |
| 4 | ACCOUNT_NAME | 账户名 | string(80) | Y |  |
| 5 | MAIN | 主要 | number(0/1) | Y |  |
| 6 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 7 | REMITTANCE_NOTICE_MODE | 汇款通知方式 | number | Y |  |
| 8 | NOTICE_FAX | 通知传真号 | string(40) | Y |  |
| 9 | NOTICE_EMAIL | 通知电子邮件 | string(72) | Y |  |
| 10 | NOTIC_IDENTIFY_TYPE | 通知识别类型 | number | Y |  |
| 11 | NOTIC_IDENTIFY_NO | 通知识别编号 | string(20) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | CUSTOMER_FI_ID |  | GUID | Y |  |

### CUSTOMER_CONTACT (客户联系人信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_CONTACT_ID | 主键 | GUID | Y | Y |
| 4 | CONTACT | 联系人 | string(72) | Y |  |
| 5 | MAIN_ORDER_CONTACT | 主要订单联系人 | number(0/1) | Y |  |
| 6 | MAIN_SHIP_TO_CONTACT | 主要收货联系人 | number(0/1) | Y |  |
| 7 | MAIN_INVOICE_CONTACT | 主要发票邮寄联系人 | number(0/1) | Y |  |
| 8 | MAIN_PAY_CONTACT | 主要付款联系人 | number(0/1) | Y |  |
| 9 | POSITION | 职务 | string(40) | Y |  |
| 10 | DEPARTMENT | 部门 | string(120) | Y |  |
| 11 | OFFICE_PHONE | 办公电话 | string(40) | Y |  |
| 12 | MOBILE_PHONE | 移动电话 | string(40) | Y |  |
| 13 | FAX | 传真 | string(40) | Y |  |
| 14 | EMAIL | 电子邮箱 | string(120) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | CRM_ROLE | 角色 | string(80) | Y |  |
| 17 | CRM_TITLE | 称谓 | string(80) | Y |  |
| 18 | CRM_SEX | 性别 | string(40) | Y |  |
| 19 | CRM_SD_AVAILABLE | 销售系统可见 | number(0/1) | Y |  |
| 20 | CRM_MAIN_CONTACT | 主联系人 | number(0/1) | Y |  |
| 21 | CRM_HOME_PHONE | 家庭电话 | string(40) | Y |  |
| 22 | CRM_QQ_MSN | QQ_MSN | string(120) | Y |  |
| 23 | CRM_BIRTHDAY | 生日 | date | Y |  |
| 24 | CRM_HOBBY | 爱好 | string(160) | Y |  |
| 25 | CRM_FAMILY_INFO | 家庭信息 | string(510) | Y |  |
| 26 | CUSTOMER_BUSINESS_ID | 客户业务信息主键 | GUID | Y |  |
| 27 | CRM_CUSTOMER_ID | 客户 | GUID | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_CREDIT (客户信用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_CREDIT_ID | 主键 | GUID | Y | Y |
| 4 | CREDIT_MODE | 设置模式 | string(40) | Y |  |
| 5 | CREDIT_AMT | 信用额度 | number(23,8) | Y |  |
| 6 | CREDIT_PAY | 已用额度 | number(23,8) | Y |  |
| 7 | ALARM_LINE | 预警线 | number(23,8) | Y |  |
| 8 | OVERFLOW_RATE | 超限比率 | number(5,4) | Y |  |
| 9 | OVERFLOW_AMT | 超限金额 | number(23,8) | Y |  |
| 10 | CO_RATE | 未订货的合同金额比率 | number(5,4) | Y |  |
| 11 | SO_RATE | 未销货的订单金额比率 | number(5,4) | Y |  |
| 12 | SD_RATE | 未结算的销货金额比率 | number(5,4) | Y |  |
| 13 | AR_RATE | 应收账款比率 | number(5,4) | Y |  |
| 14 | BR_RATE | 应收票据比率 | number(5,4) | Y |  |
| 15 | ADV_RATE | 预收款比率 | number(5,4) | Y |  |
| 16 | CO_SAVE_CHECK | 合同保存时信用检查 | string(40) | Y |  |
| 17 | CO_APPROVE_CHECK | 合同审核时信用检查 | string(40) | Y |  |
| 18 | SO_SAVE_CHECK | 订单保存时信用检查 | string(40) | Y |  |
| 19 | SO_APPROVE_CHECK | 订单审核时信用检查 | string(40) | Y |  |
| 20 | SD_SAVE_CHECK | 销货保存时信用检查 | string(40) | Y |  |
| 21 | SD_APPROVE_CHECK | 销货审核时信用检查 | string(40) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | CREDIT_OBJECT | 信控对象 | string(40) | Y |  |
| 24 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 25 | CREDIT_RULE_ID | 信控策略 | GUID | Y |  |
| 26 | CURRENCY_ID | 币种 | GUID | Y |  |
| 27 | CREDIT_AREA_ID | 信控区域 | GUID | Y |  |
| 28 | INCLUDE_BAD_DEBT | 包括坏账 | number(0/1) | Y |  |
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
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_CREDIT_D (客户信用-客户群)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_CREDIT_D_ID | 主键 | GUID | Y | Y |
| 2 | CREDIT_PAY | 已用额度 | number(23,8) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CUSTOMER_ID | 客户 | GUID | Y |  |
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
| 24 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 25 | ApproveDate | 修改日期 | date | Y |  |
| 26 | ApproveBy | 修改人 | GUID | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | CUSTOMER_CREDIT_ID |  | GUID | Y |  |

### CUSTOMER_CREDIT_LINE (客户信用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_CREDIT_LINE_ID | 主键 | GUID | Y | Y |
| 4 | CO_AMT | 未订货的合同金额 | number(23,8) | Y |  |
| 5 | SO_AMT | 未销货的订单金额 | number(23,8) | Y |  |
| 6 | SD_AMT | 未结算的销货单金额 | number(23,8) | Y |  |
| 7 | AR_AMT | 应收账款金额 | number(23,8) | Y |  |
| 8 | BR_AMT | 应收票据金额 | number(23,8) | Y |  |
| 9 | ADV_AMT | 预收款金额 | number(23,8) | Y |  |
| 10 | SR_AMT | 未结算的销退单金额 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CREDIT_MODE | 信用类型 | string(40) | Y |  |
| 13 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 14 | COMPANY_ID | 主键 | GUID | Y |  |
| 15 | CURRENCY_ID | 主键 | GUID | Y |  |
| 16 | BD_AMT | 坏账金额 | number(23,8) | Y |  |
| 17 | ADV_TAX | 预收款税金 | number(23,8) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
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
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_CREDIT_RATING (客户信用等级信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_CREDIT_RATING_ID | 主键 | GUID | Y | Y |
| 4 | CREDIT_RATING_CODE | 客户信用等级编号 | string(12) | Y |  |
| 5 | CREDIT_RATING_NAME | 客户信用等级名称 | string(40) | Y |  |
| 6 | PROVISION_INDICATOR | 计提坏账准备标识(应收账款余额百分比法) | number(0/1) | Y |  |
| 7 | PROVISION_ACCRUED_RATE | 坏账准备计提比率 | number(5,4) | Y |  |
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

### CUSTOMER_CREDIT_TEMPORARY (客户信用-临时额度)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_CREDIT_TEMPORARY_ID | 主键 | GUID | Y | Y |
| 2 | FUND_DESC | 款项描述 | string(40) | Y |  |
| 3 | CREDIT_AMT | 信用额度 | number(23,8) | Y |  |
| 4 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 5 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
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
| 26 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 27 | ApproveDate | 修改日期 | date | Y |  |
| 28 | ApproveBy | 修改人 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | CUSTOMER_CREDIT_ID |  | GUID | Y |  |

### CUSTOMER_FI (客户财务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_FI_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | INVOICE_INFO1 | 税籍发票信息1 | string(200) | Y |  |
| 6 | INVOICE_INFO2 | 税籍发票信息2 | string(200) | Y |  |
| 7 | INVOICE_INFO3 | 税籍发票信息3 | string(200) | Y |  |
| 8 | INVOICE_INFO4 | 税籍发票信息4 | string(200) | Y |  |
| 9 | INVOICE_INFO5 | 税籍发票信息5 | string(200) | Y |  |
| 10 | INVOICE_INFO6 | 税籍发票信息6 | string(200) | Y |  |
| 11 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 12 | SETTLEMENT_METHOD_ID | 结算方式 | GUID | Y |  |
| 13 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 14 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 15 | RECEIVER_ID | 收款业务员 | GUID | Y |  |
| 16 | CUSTOMER_CREDIT_RATING_ID | 信用等级 | GUID | Y |  |
| 17 | CUSTOMER_FICATEGORY_ID | 会计分类 | GUID | Y |  |
| 18 | OTHER_CLEARING_HOUSE_FLAG | 外埠交换所 | number(0/1) | Y |  |
| 19 | CURRENCY_ID | 货币 | GUID | Y |  |
| 20 | ROLE_REMARK | 买方营业人角色注记 | string(510) | Y |  |
| 21 | CSWARR_CATEGORY_ID | 客户销售保修分类 | GUID | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | Attachments | 附件 | string | Y |  |
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
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_FICATEGORY (客户会计分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_FICATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | CUSTOMER_FICATEGORY_CODE | 分类编号 | string(12) | Y |  |
| 5 | CUSTOMER_FICATEGORY_NAME | 分类名称 | string(40) | Y |  |
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

### CUSTOMER_ITEM (客户品号)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | CUSTOMER_ITEM_CODE | 客户品号 | string(80) | Y |  |
| 5 | CUSTOMER_ITEM_NAME | 客户品名 | string(120) | Y |  |
| 6 | CUSTOMER_ITEM_SPECIFICATION | 客户规格 | string(510) | Y |  |
| 7 | CUSTOMER_ITEM_DESCRIPTION | 客户商品描述 | string(510) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
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
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_PRICE_STRATEGY (客户取价策略使用记录)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_PRICE_STRATEGY_ID | 主键 | GUID | Y | Y |
| 4 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 7 | PRICE_STRATEGY_ID | 策略编号 | GUID | Y |  |
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

### CUSTOMER_PROPERTY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_PROPERTY_ID | 主键 | GUID | Y | Y |
| 2 | PROPERTY_VALUE | 属性值 | string(20) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | BP_PROPERTY_ID | 属性 | GUID | Y |  |
| 5 | PARENT_CUSTOMER_ID | 客户 | GUID | Y |  |
| 6 | PROPERTY_VALUE_ID | 属性值ID | GUID | Y |  |
| 7 | PROPERTY_VALUE_DESC | 属性值描述 | string(120) | Y |  |
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
| 36 | ORG_ID_RTK |  | string(400) | Y |  |
| 37 | ORG_ID_ROid |  | GUID | Y |  |
| 38 | CUSTOMER_BUSINESS_ID |  | GUID | Y |  |

### CUSTOMER_PROPERTY_VIEW (CPV)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_PROPERTY_VIEW_ID | 主键 | GUID | Y | Y |
| 2 | CUSTOMER_ID |  | GUID | Y |  |
| 3 | P1 |  | string(80) | Y |  |
| 4 | P2 |  | string(80) | Y |  |
| 5 | P3 |  | string(80) | Y |  |
| 6 | P4 |  | string(80) | Y |  |
| 7 | P5 |  | string(80) | Y |  |
| 8 | P6 |  | string(80) | Y |  |
| 9 | P7 |  | string(80) | Y |  |
| 10 | P8 |  | string(80) | Y |  |
| 11 | P9 |  | string(80) | Y |  |
| 12 | P10 |  | string(80) | Y |  |
| 13 | P11 |  | string(80) | Y |  |
| 14 | P12 |  | string(80) | Y |  |
| 15 | P13 |  | string(80) | Y |  |
| 16 | P14 |  | string(80) | Y |  |
| 17 | P15 |  | string(80) | Y |  |
| 18 | P16 |  | string(80) | Y |  |
| 19 | P17 |  | string(80) | Y |  |
| 20 | P18 |  | string(80) | Y |  |
| 21 | P19 |  | string(80) | Y |  |
| 22 | P20 |  | string(80) | Y |  |
| 23 | P21 |  | string(80) | Y |  |
| 24 | P22 |  | string(80) | Y |  |
| 25 | P23 |  | string(80) | Y |  |
| 26 | P24 |  | string(80) | Y |  |
| 27 | P25 |  | string(80) | Y |  |
| 28 | P26 |  | string(80) | Y |  |
| 29 | P27 |  | string(80) | Y |  |
| 30 | P28 |  | string(80) | Y |  |
| 31 | P29 |  | string(80) | Y |  |
| 32 | P30 |  | string(80) | Y |  |
| 33 | P31 |  | string(80) | Y |  |
| 34 | P32 |  | string(80) | Y |  |
| 35 | P33 |  | string(80) | Y |  |
| 36 | P34 |  | string(80) | Y |  |
| 37 | P35 |  | string(80) | Y |  |
| 38 | P36 |  | string(80) | Y |  |
| 39 | P37 |  | string(80) | Y |  |
| 40 | P38 |  | string(80) | Y |  |
| 41 | P39 |  | string(80) | Y |  |
| 42 | P40 |  | string(80) | Y |  |
| 43 | P41 |  | string(80) | Y |  |
| 44 | P42 |  | string(80) | Y |  |
| 45 | P43 |  | string(80) | Y |  |
| 46 | P44 |  | string(80) | Y |  |
| 47 | P45 |  | string(80) | Y |  |
| 48 | P46 |  | string(80) | Y |  |
| 49 | P47 |  | string(80) | Y |  |
| 50 | P48 |  | string(80) | Y |  |
| 51 | P49 |  | string(80) | Y |  |
| 52 | P50 |  | string(80) | Y |  |
| 53 | P51 |  | string(80) | Y |  |
| 54 | P52 |  | string(80) | Y |  |
| 55 | P53 |  | string(80) | Y |  |
| 56 | P54 |  | string(80) | Y |  |
| 57 | P55 |  | string(80) | Y |  |
| 58 | P56 |  | string(80) | Y |  |
| 59 | P57 |  | string(80) | Y |  |
| 60 | P58 |  | string(80) | Y |  |
| 61 | P59 |  | string(80) | Y |  |
| 62 | P60 |  | string(80) | Y |  |
| 63 | P61 |  | number(23,8) | Y |  |
| 64 | P62 |  | number(23,8) | Y |  |
| 65 | P63 |  | number(23,8) | Y |  |
| 66 | P64 |  | number(23,8) | Y |  |
| 67 | P65 |  | number(23,8) | Y |  |
| 68 | P66 |  | number(23,8) | Y |  |
| 69 | P67 |  | number(23,8) | Y |  |
| 70 | P68 |  | number(23,8) | Y |  |
| 71 | P69 |  | number(23,8) | Y |  |
| 72 | P70 |  | number(23,8) | Y |  |
| 73 | P71 |  | number(23,8) | Y |  |
| 74 | P72 |  | number(23,8) | Y |  |
| 75 | P73 |  | number(23,8) | Y |  |
| 76 | P74 |  | number(23,8) | Y |  |
| 77 | P75 |  | number(23,8) | Y |  |
| 78 | P76 |  | number(23,8) | Y |  |
| 79 | P77 |  | number(23,8) | Y |  |
| 80 | P78 |  | number(23,8) | Y |  |
| 81 | P79 |  | number(23,8) | Y |  |
| 82 | P80 |  | number(23,8) | Y |  |
| 83 | P81 |  | number(23,8) | Y |  |
| 84 | P82 |  | number(23,8) | Y |  |
| 85 | P83 |  | number(23,8) | Y |  |
| 86 | P84 |  | number(23,8) | Y |  |
| 87 | P85 |  | number(23,8) | Y |  |
| 88 | P86 |  | number(23,8) | Y |  |
| 89 | P87 |  | number(23,8) | Y |  |
| 90 | P88 |  | number(23,8) | Y |  |
| 91 | P89 |  | number(23,8) | Y |  |
| 92 | P90 |  | number(23,8) | Y |  |
| 93 | P91 |  | number(23,8) | Y |  |
| 94 | P92 |  | number(23,8) | Y |  |
| 95 | P93 |  | number(23,8) | Y |  |
| 96 | P94 |  | number(23,8) | Y |  |
| 97 | P95 |  | number(23,8) | Y |  |
| 98 | P96 |  | number(23,8) | Y |  |
| 99 | P97 |  | number(23,8) | Y |  |
| 100 | P98 |  | number(23,8) | Y |  |
| 101 | P99 |  | number(23,8) | Y |  |
| 102 | P100 |  | number(23,8) | Y |  |
| 103 | CreateDate | 创建日期 | date | Y |  |
| 104 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 105 | ModifiedDate | 修改日期 | date | Y |  |
| 106 | CreateBy | 创建者 | GUID | Y |  |
| 107 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 108 | ModifiedBy | 修改者 | GUID | Y |  |
| 109 | Attachments | 附件 | string | Y |  |
| 110 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 111 | Version | 版本号，不要随意更改 | binary | Y |  |
| 112 | ORG_ID_RTK |  | string(400) | Y |  |
| 113 | ORG_ID_ROid |  | GUID | Y |  |

### CUSTOMER_RECEIVE (客户赊销收款单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CUSTOMER_RECEIVE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 9 | SETTLE_AMT | 结算金额 | number(23,8) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | PrintCount | 打印次数 | number | Y |  |
| 12 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 13 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 14 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 15 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_RECEIVE_D (客户赊销收款单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CUSTOMER_RECEIVE_D_ID | 主键 | GUID | Y | Y |
| 3 | CUSTOMER_SETTLE_D_ID | 结算明细ID | GUID | Y |  |
| 4 | SETTLE_AMT | 结算金额 | number(23,8) | Y |  |
| 5 | SETTLEABLE_AMT | 应收金额 | number(23,8) | Y |  |
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
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | CUSTOMER_RECEIVE_ID |  | GUID | Y |  |

### CUSTOMER_RECEIVEABLE (客户赊销应收总帐)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_RECEIVEABLE_ID | 主键 | GUID | Y | Y |
| 4 | RECEIVEABLE_AMT | 应收账款 | number(23,8) | Y |  |
| 5 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | PrintCount | 打印次数 | number | Y |  |
| 8 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 9 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 10 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 11 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_RECEIVEABLE_D (客户赊销应收明细帐)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 4 | DOC_DATE | 赊销日期 | date | Y |  |
| 5 | RECEIVEABLE_AMT | 应收账款 | number(23,8) | Y |  |
| 6 | SETTLE_AMT | 结算金额 | number(23,8) | Y |  |
| 7 | RECEIVE_AMT | 已收金额 | number(23,8) | Y |  |
| 8 | CUSTOMER_RECEIVEABLE_D_ID | 主键 | GUID | Y | Y |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |
| 40 | SOURCE_ORG_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ORG_ID_ROid |  | GUID | Y |  |
| 42 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 43 | SOURCE_ID_ROid |  | GUID | Y |  |
| 44 | SETTLE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SETTLE_SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | RECEIVE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | RECEIVE_SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | CUSTOMER_RECEIVEABLE_ID |  | GUID | Y |  |

### CUSTOMER_SALES (客户业务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 5 | EARNEST_RATE |  | number(5,4) | Y |  |
| 6 | SIGN_REQUIRED | 需签收 | number(0/1) | Y |  |
| 7 | INVOICE_BY_SIGN | 依签收数量开票 | number(0/1) | Y |  |
| 8 | ADVANCED_DELIVERY | 允许早交 | number(0/1) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | SETTLEMENT_BASE_DATE_TYPE | 结算起算日类型 | string(40) | Y |  |
| 11 | IS_MONTH_PLUS | 加月 | number(0/1) | Y |  |
| 12 | MONTHS | 月数 | number | Y |  |
| 13 | IS_DAY_PLUS | 加日 | number(0/1) | Y |  |
| 14 | DAYS | 日数 | number | Y |  |
| 15 | IS_EVERY_DAY | 逢 | number(0/1) | Y |  |
| 16 | EVERY_DAY | 逢某日 | number | Y |  |
| 17 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 18 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 19 | CURRENCY_ID | 币种 | GUID | Y |  |
| 20 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 21 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 22 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 23 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 24 | CS_TAX_CLASSIFICATION_ID | 税分类 | GUID | Y |  |
| 25 | DIRECT_SETTLEMENT_INDICATOR | 直接结账 | number(0/1) | Y |  |
| 26 | DIRECT_INVOICING_INDICATOR | 直接开票 | number(0/1) | Y |  |
| 27 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 28 | CRM_TRACK_STATUS | 跟进状态 | GUID | Y |  |
| 29 | BRAND | 品牌 | string(120) | Y |  |
| 30 | DESTINATION | 目的地 | string(120) | Y |  |
| 31 | SHIPPING_PORT | 海运港口 | string(120) | Y |  |
| 32 | AIR_PORT | 空运机场 | string(120) | Y |  |
| 33 | AGENT_CUSTOMER_ID | 代理商 | GUID | Y |  |
| 34 | BROKERS_SUPPLIER_ID | 报关行 | GUID | Y |  |
| 35 | INSPECTION_SUPPLIER_ID | 验货公司 | GUID | Y |  |
| 36 | COMMISSION_RATE | 佣金比率 | number(5,4) | Y |  |
| 37 | INSURANCE_RATE | 保险费率 | number(5,4) | Y |  |
| 38 | TRANSPORT_SUPPLIER_ID | 运输公司 | GUID | Y |  |
| 39 | PRICE_TERMS_ID | 价格条款 | GUID | Y |  |
| 40 | TAX_MODE | 税额计算方式 | string(40) | Y |  |
| 41 | TAX_ID | 税种 | GUID | Y |  |
| 42 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 43 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 44 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 45 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 46 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 47 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 48 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 49 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 50 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 51 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 52 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 53 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 54 | UDF041 | 自定义字段12 | date | Y |  |
| 55 | UDF042 | 自定义字段13 | date | Y |  |
| 56 | UDF051 | 自定义字段14 | GUID | Y |  |
| 57 | UDF052 | 自定义字段15 | GUID | Y |  |
| 58 | UDF053 | 自定义字段16 | GUID | Y |  |
| 59 | UDF054 | 自定义字段17 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | CreateDate | 创建日期 | date | Y |  |
| 62 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 63 | ModifiedDate | 修改日期 | date | Y |  |
| 64 | CreateBy | 创建者 | GUID | Y |  |
| 65 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 66 | ModifiedBy | 修改者 | GUID | Y |  |
| 67 | Attachments | 附件 | string | Y |  |
| 68 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 69 | ApproveDate | 修改日期 | date | Y |  |
| 70 | ApproveBy | 修改人 | GUID | Y |  |
| 71 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_SETTLE (客户赊销结算单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | CUSTOMER_SETTLE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SETTLE_AMT | 结算金额 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 11 | PrintCount | 打印次数 | number | Y |  |
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
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### CUSTOMER_SETTLE_D (客户赊销结算单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CUSTOMER_SETTLE_D_ID | 主键 | GUID | Y | Y |
| 3 | SETTLE_AMT | 结算金额 | number(23,8) | Y |  |
| 4 | RECEIVE_AMT | 收款金额 | number(23,8) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CUSTOMER_RECEIVEABLE_D_ID | 应收明细ID | GUID | Y |  |
| 7 | SETTLEABLE_AMT | 应收金额 | number(23,8) | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | CUSTOMER_SETTLE_ID |  | GUID | Y |  |

### CUSTOMER_SHIPPING_MARK (客户唛头信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CUSTOMER_SHIPPING_MARK_ID | 主键 | GUID | Y | Y |
| 2 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 3 | SHIPPING_MARK_CODE | 唛头编号 | string(20) | Y |  |
| 4 | SHIPPING_MARK_NAME | 唛头名称 | string(40) | Y |  |
| 5 | FRONT_MARK | 正唛 | string(510) | Y |  |
| 6 | FRONT_MARK_IS_PIC | 正唛用图片 | number(0/1) | Y |  |
| 7 | FRONT_MARK_PIC | 正唛图片 | string(120) | Y |  |
| 8 | SIDE_MARK | 侧唛 | string(510) | Y |  |
| 9 | SIDE_MARK_IS_PIC | 侧唛用图片 | number(0/1) | Y |  |
| 10 | SIDE_MARK_PIC | 侧唛图片 | string(120) | Y |  |
| 11 | FRONT_MARK_LAYOUT | 正唛样式 | string(400) | Y |  |
| 12 | SIDE_MARK_LAYOUT | 侧唛样式 | string(400) | Y |  |
| 13 | MAIN | 主要 | number(0/1) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
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
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |

### CUSTOMER_SUPPLIER (客户供应商关系)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CUSTOMER_SUPPLIER_ID | 主键 | GUID | Y | Y |
| 4 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
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