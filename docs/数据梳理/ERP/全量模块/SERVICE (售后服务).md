---
module: "SERVICE"
name_zh: "售后服务"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 30
columns: 1407
category: crm
tags: ["ERP", "E10", "crm"]
created: 2026-06-25 10:52
---

# SERVICE (售后服务)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 30 | Columns: 1407

## Related Modules

- [[BP (业务伙伴)|BP (业务伙伴)]]
- [[CARD (卡券管理)|CARD (卡券管理)]]
- [[CRM (客户关系)|CRM (客户关系)]]
- [[CUSTOMER (客户管理)|CUSTOMER (客户管理)]]
- [[MEMBER (会员管理)|MEMBER (会员管理)]]
- [[REPAIR (维修管理)|REPAIR (维修管理)]]
- [[REPLACE (替换管理)|REPLACE (替换管理)]]
- [[TICKET (票券管理)|TICKET (票券管理)]]

---

## Tables


- **SERVICE_CENTER (服务域)**
- **SERVICE_CONTRACT (维护合同)**
- **SERVICE_CONTRACT_D (服务产品)**
- **SERVICE_CONTRACT_SD**
- **SERVICE_DOC (服务处理单)**
- **SERVICE_DOC_D (服务产品单身)**
- **SERVICE_DOC_SD1 (故障信息子单身)**
- **SERVICE_DOC_SD2 (服务项目子单身)**
- **SERVICE_DOC_SD3 (零配件更换单身)**
- **SERVICE_DOC_SD4 (换货子单)**
- **SERVICE_EMPLOYEE**
- **SERVICE_ITEM (服务项目)**
- **SERVICE_ITEM_D (服务项目--结果单身)**
- **SERVICE_PERIOD**
- **SERVICE_PERIOD_D**
- **SERVICE_QUOTATION**
- **SERVICE_QUOTATION_D**
- **SERVICE_QUOTATION_SD**
- **SERVICE_REQUEST (服务请求单)**
- **SERVICE_REQUEST_D (服务请求单单身)**
- **SERVICE_REQUEST_SD (故障信息子单身)**
- **SERVICE_REQUEST_SD2 (部门反馈子单身)**
- **SERVICE_REQUEST_SD3 (历史处理状态)**
- **SERVICE_SETTLEMENT**
- **SERVICE_SETTLEMENT_D**
- **SERVICE_SITE**
- **SERVICE_SITE_EMPLOYEE**
- **SERVICE_SITE_WAREHOUSE**
- **SERVICE_TYPE (服务类型)**
- **SERVICE_URGENCY (服务紧急度)**


---


---


> Tables: 30

### SERVICE_CENTER (服务域)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | SERVICE_CENTER_CODE | 编号 | string(20) | Y |  |
| 5 | SERVICE_CENTER_NAME | 名称 | string(40) | Y |  |
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

### SERVICE_CONTRACT (维护合同)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SERVICE_CONTRACT_ID | 主键 | GUID | Y | Y |
| 7 | SIGN_DATE | 签订日期 | date | Y |  |
| 8 | ITEM_ID | 服务品号 | GUID | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 11 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 12 | CONTRACT_NO | 合同编号 | string(80) | Y |  |
| 13 | CONTRACT_NAME | 合同名称 | string(80) | Y |  |
| 14 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 15 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 16 | CONTRACT_DESCRIBE | 合同描述 | string(160) | Y |  |
| 17 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 18 | TAX_ID | 税种 | GUID | Y |  |
| 19 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 20 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 21 | CURRENCY_ID | 币种 | GUID | Y |  |
| 22 | CUSTOMER_ADDR_NAME | 客户地址 | string(510) | Y |  |
| 23 | CUSTOMER_CONTACT_NAME | 客户联系人 | string(72) | Y |  |
| 24 | INPUT_MODE | 服务费用录入方式 | string(40) | Y |  |
| 25 | QUANTITY | 数量 | number(16,6) | Y |  |
| 26 | UNIT_ID | 单位 | GUID | Y |  |
| 27 | PRICE | 单价 | number(23,8) | Y |  |
| 28 | AMOUNT | 金额 | number(23,8) | Y |  |
| 29 | TAX_RATE | 稅率 | number(5,4) | Y |  |
| 30 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 31 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 32 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 33 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 34 | REMARK | 备注 | string(510) | Y |  |
| 35 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 36 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 37 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 38 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 39 | PrintCount | 打印次数 | number | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 66 | Version | 版本号，不要随意更改 | binary | Y |  |
| 67 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 68 | ApproveDate | 修改日期 | date | Y |  |
| 69 | ApproveBy | 修改人 | GUID | Y |  |
| 70 | Owner_Org_RTK |  | string(400) | Y |  |
| 71 | Owner_Org_ROid |  | GUID | Y |  |

### SERVICE_CONTRACT_D (服务产品)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_CONTRACT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | AS_SN | 序列号管理 | number(0/1) | Y |  |
| 7 | SN | 序列号 | string(510) | Y |  |
| 8 | QUANTITY | 数量 | number(16,6) | Y |  |
| 9 | UNIT_ID | 单位 | GUID | Y |  |
| 10 | TAX_ID | 税种 | GUID | Y |  |
| 11 | TAX_RATE | 稅率 | number(5,4) | Y |  |
| 12 | PRICE | 单价 | number(23,8) | Y |  |
| 13 | AMOUNT | 金额 | number(23,8) | Y |  |
| 14 | PERIOD_TYPE | 维护周期类型 | string(40) | Y |  |
| 15 | SERVICE_PERIOD_ID | 维护周期编号 | GUID | Y |  |
| 16 | NEXT_DATE | 下次维护日期 | date | Y |  |
| 17 | ORIG_EXPIRY_DATE | 原保修截止日期 | date | Y |  |
| 18 | ORIG_EXPIRY_DATE2 | 原有偿保修截止日 | date | Y |  |
| 19 | UPDATE_DATE | 更新保修期 | number(0/1) | Y |  |
| 20 | UPDATE_MAIN | 仅更新主机 | number(0/1) | Y |  |
| 21 | UPDATETYPE | 更新保修期方式 | string(40) | Y |  |
| 22 | DELAY_NUM | 顺延数 | number | Y |  |
| 23 | DELAY_UNIT | 顺延单位 | string(40) | Y |  |
| 24 | NEW_EXPIRY_DATE | 保修截止日 | date | Y |  |
| 25 | NEW_EXPIRY_DATE2 | 有偿保修截止日 | date | Y |  |
| 26 | PRODUCT_ID | 成品识别码 | string(510) | Y |  |
| 27 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 28 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 29 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 30 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 31 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 32 | REMARK | 备注 | string(510) | Y |  |
| 33 | ITEM_ID | 品号 | GUID | Y |  |
| 34 | ORIG_PERIOD_TYPE | 原维护周期类型 | string(40) | Y |  |
| 35 | ORIG_SERVICE_PERIOD_ID | 原维护周期编号 | GUID | Y |  |
| 36 | ORIG_NEXT_DATE | 原下次维护日期 | date | Y |  |
| 37 | ORIG_BEGIN_DATE | 原维护开始日期 | date | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 45 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 46 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 47 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 48 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 49 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 50 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 51 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 52 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 53 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 54 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 55 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 56 | UDF041 | 自定义字段12 | date | Y |  |
| 57 | UDF042 | 自定义字段13 | date | Y |  |
| 58 | UDF051 | 自定义字段14 | GUID | Y |  |
| 59 | UDF052 | 自定义字段15 | GUID | Y |  |
| 60 | UDF053 | 自定义字段16 | GUID | Y |  |
| 61 | UDF054 | 自定义字段17 | GUID | Y |  |
| 62 | Version | 版本号，不要随意更改 | binary | Y |  |
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 67 | SOURCE_ID_ROid |  | GUID | Y |  |
| 68 | SERVICE_CONTRACT_ID |  | GUID | Y |  |

### SERVICE_CONTRACT_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_CONTRACT_SD_ID | 主键 | GUID | Y | Y |
| 3 | QUANTITY | 数量 | number(16,6) | Y |  |
| 4 | UNIT_ID | 单位 | GUID | Y |  |
| 5 | PRICE | 单价 | number(23,8) | Y |  |
| 6 | AMOUNT | 金额 | number(23,8) | Y |  |
| 7 | TAX_RATE | 稅率 | number(5,4) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 10 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 11 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 12 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 13 | TAX_ID | 税种 | GUID | Y |  |
| 14 | SERVICE_ITEM_ID | 服务项目 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | SERVICE_CONTRACT_D_ID |  | GUID | Y |  |

### SERVICE_DOC (服务处理单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SERVICE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 8 | SETTLEMENT_CUST_ID | 结算客户 | GUID | Y |  |
| 9 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 10 | ASSISTANT | 协助处理人员 | string(510) | Y |  |
| 11 | STATUS | 结案 | number(0/1) | Y |  |
| 12 | SERVICE_TYPE_ID | 服务类型 | GUID | Y |  |
| 13 | SERVICE_CONTRACT_D_ID | 维护合同 | GUID | Y |  |
| 14 | SERVICE_MODE | 服务方式 | string(40) | Y |  |
| 15 | CONTACT | 联系人 | string(120) | Y |  |
| 16 | CONTACT_PHONE | 联系电话 | string(100) | Y |  |
| 17 | ADDRESS | 地址 | string(200) | Y |  |
| 18 | DESCRIPTION | 内容描述 | string(510) | Y |  |
| 19 | SATISFACTION | 满意度 | string(40) | Y |  |
| 20 | GRADE | 客户打分 | string(6) | Y |  |
| 21 | COMMENT | 客户评价 | string(510) | Y |  |
| 22 | INPUT_MODE | 生成方式 | string(40) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | COMPANY_ID | 公司 | GUID | Y |  |
| 25 | REVIEW_PASS | 审查通过 | number(0/1) | Y |  |
| 26 | REVIEW_OPINIONS | 审查意见 | string(510) | Y |  |
| 27 | REVIEW_EMPLOYEE_ID | 审查人员 | GUID | Y |  |
| 28 | REVIEW_DATE | 审查日期 | date | Y |  |
| 29 | PLANT_ID | 工厂 | GUID | Y |  |
| 30 | SERVICE_EMPLOYEE1_ID | 实际处理人员 | GUID | Y |  |
| 31 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 32 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 52 | PrintCount | 打印次数 | number | Y |  |
| 53 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 54 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 55 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 56 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 57 | CreateDate | 创建日期 | date | Y |  |
| 58 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 59 | ModifiedDate | 修改日期 | date | Y |  |
| 60 | CreateBy | 创建者 | GUID | Y |  |
| 61 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 62 | ModifiedBy | 修改者 | GUID | Y |  |
| 63 | Attachments | 附件 | string | Y |  |
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |
| 68 | Owner_Org_RTK |  | string(400) | Y |  |
| 69 | Owner_Org_ROid |  | GUID | Y |  |
| 70 | SITE_SUPPLIER_ID_RTK |  | string(400) | Y |  |
| 71 | SITE_SUPPLIER_ID_ROid |  | GUID | Y |  |

### SERVICE_DOC_D (服务产品单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SERVICE_REQUEST_ID | 服务请求单 | GUID | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | SN | 序列号 | string(510) | Y |  |
| 9 | QUANTITY | 数量 | number(16,6) | Y |  |
| 10 | UNIT_ID | 单位 | GUID | Y |  |
| 11 | UNDER_WARRANTY | 保修期内 | number(0/1) | Y |  |
| 12 | UNDER_WARRANTY2 | 有偿保修期内 | number(0/1) | Y |  |
| 13 | SERVICE_URGENCY_ID | 紧急度 | GUID | Y |  |
| 14 | PROCESS_DATE | 处理日期 | date | Y |  |
| 15 | PROCESS_DESC | 处理情况描述 | string(510) | Y |  |
| 16 | UPDATE_SERVICE | 更新主动服务信息 | number(0/1) | Y |  |
| 17 | UPDATE_INSTALLATION | 更新安装信息 | number(0/1) | Y |  |
| 18 | ACCEPTANCE | 需验收 | number(0/1) | Y |  |
| 19 | ACCEPTANCE_INSTANT | 直接验收 | number(0/1) | Y |  |
| 20 | ACCEPTED | 验收否 | number(0/1) | Y |  |
| 21 | ACCEPTED_DATE | 验收日期 | date | Y |  |
| 22 | BEGIN_DATE | 计划开始处理日期 | date | Y |  |
| 23 | END_DATE | 计划完成处理日期 | date | Y |  |
| 24 | TASK_TIME | 计划工时 | number(16,1) | Y |  |
| 25 | ACTUAL_BEGIN_DATE | 实际开始时间 | date | Y |  |
| 26 | ACTUAL_END_DATE | 实际结束时间 | date | Y |  |
| 27 | ACTUAL_TASK_TIME | 实际工时 | number(16,1) | Y |  |
| 28 | SERVICE_STATE | 处理状态 | string(40) | Y |  |
| 29 | PRODUCT_ID | 成品识别码 | string(510) | Y |  |
| 30 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 31 | RMA | RMA号 | string(120) | Y |  |
| 32 | ACCEPTANCE_DOC_ID | 验收单别 | GUID | Y |  |
| 33 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 34 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 35 | DISPATCH_DESP | 派工说明 | string(510) | Y |  |
| 36 | ACCEPTED_EMPLOYEE | 验收人员 | string(120) | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 56 | CreateDate | 创建日期 | date | Y |  |
| 57 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 58 | ModifiedDate | 修改日期 | date | Y |  |
| 59 | CreateBy | 创建者 | GUID | Y |  |
| 60 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 61 | ModifiedBy | 修改者 | GUID | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | SERVICE_DOC_ID |  | GUID | Y |  |

### SERVICE_DOC_SD1 (故障信息子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_DOC_SD1_ID | 主键 | GUID | Y | Y |
| 2 | BREAKDOWN_ID | 故障 | GUID | Y |  |
| 3 | PROCESS_DESC | 处理说明 | string(510) | Y |  |
| 4 | PROCESS_STATE | 处理状态 | string(40) | Y |  |
| 5 | INSERT_KM | 加入知识库 | number(0/1) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | BREAKDOWN_DESC | 故障描述 | string(510) | Y |  |
| 8 | Version | 版本号，不要随意更改 | binary | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | SERVICE_DOC_D_ID |  | GUID | Y |  |

### SERVICE_DOC_SD2 (服务项目子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_DOC_SD2_ID | 主键 | GUID | Y | Y |
| 2 | SERVICE_ITEM_ID | 服务项目 | GUID | Y |  |
| 3 | SERVICE_RESULT | 服务结果 | string(510) | Y |  |
| 4 | PROCESS_DESC | 处理说明 | string(510) | Y |  |
| 5 | INSERT_KM | 加入知识库 | number(0/1) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | SERVICE_DOC_D_ID |  | GUID | Y |  |

### SERVICE_DOC_SD3 (零配件更换单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_DOC_SD3_ID | 主键 | GUID | Y | Y |
| 3 | ORIG_ITEM_ID | 原品号 | GUID | Y |  |
| 4 | ORIG_ITEM_DESC | 原品名 | string(120) | Y |  |
| 5 | ORIG_ITEM_SPEC | 原规格 | string(510) | Y |  |
| 6 | ORIG_ITEM_FEATURE_ID | 原特征码 | GUID | Y |  |
| 7 | ORIG_SN | 原序列号 | string(510) | Y |  |
| 8 | ORIG_EXPIRY_DATE | 新品号原保修截止日期 | date | Y |  |
| 9 | ORIG_EXPIRY_DATE2 | 新品号原有偿保修截止日期 | date | Y |  |
| 10 | ORIG_UNDER_WARRANTY | 原保修期内 | number(0/1) | Y |  |
| 11 | ORIG_UNDER_WARRANTY2 | 原有偿保修期内 | number(0/1) | Y |  |
| 12 | ORIG_QTY | 原数量 | number(16,6) | Y |  |
| 13 | PRODUCT_ID | 成品识别码 | string(510) | Y |  |
| 14 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 17 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 18 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 19 | AS_SN | 序列号管理 | number(0/1) | Y |  |
| 20 | SN | 序列号 | string(510) | Y |  |
| 21 | QTY | 更换数量 | number(16,2) | Y |  |
| 22 | UNIT_ID | 单位 | GUID | Y |  |
| 23 | UPDATE_DATE | 更新保修期 | number(0/1) | Y |  |
| 24 | UPDATETYPE | 更新保修期方式 | string(40) | Y |  |
| 25 | EXPIRY_DATE | 保修截止日期 | date | Y |  |
| 26 | EXPIRY_DATE2 | 有偿保修截止日期 | date | Y |  |
| 27 | RETURN_QTY | 旧件返回数量 | number(16,2) | Y |  |
| 28 | RETURNED | 已返回 | number(0/1) | Y |  |
| 29 | ORIG_PRODUCT_ID | 原成品识别码 | string(510) | Y |  |
| 30 | ORIG_LEVEL_CODE | 原层级码 | string(200) | Y |  |
| 31 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 32 | ORIG_ITEM_LOT_ID | 原批号 | GUID | Y |  |
| 33 | DELAY_NUM | 顺延数 | number(16,0) | Y |  |
| 34 | DELAY_UNIT | 顺延单位 | string(40) | Y |  |
| 35 | UPDATE_MAIN | 仅更新主机 | number(0/1) | Y |  |
| 36 | RETURN_ITEM | 需返回 | number(0/1) | Y |  |
| 37 | FROM_WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 38 | FROM_BIN_ID | 库位 | GUID | Y |  |
| 39 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 40 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 41 | REMARK | 备注 | string(510) | Y |  |
| 42 | ORIG_EXPIRY_DATEOLD | 原保修截止日期 | date | Y |  |
| 43 | ORIG_EXPIRY_DATEOLD2 | 原有偿保修截止日期 | date | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 63 | CreateDate | 创建日期 | date | Y |  |
| 64 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 65 | ModifiedDate | 修改日期 | date | Y |  |
| 66 | CreateBy | 创建者 | GUID | Y |  |
| 67 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 68 | ModifiedBy | 修改者 | GUID | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 73 | SOURCE_ID_ROid |  | GUID | Y |  |
| 74 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 75 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 76 | SERVICE_DOC_D_ID |  | GUID | Y |  |

### SERVICE_DOC_SD4 (换货子单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_DOC_SD4_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 新品号 | GUID | Y |  |
| 3 | ITEM_DESCRIPTION | 新品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 新规格 | string(510) | Y |  |
| 5 | ITEM_FEATURE_ID | 新特征码 | GUID | Y |  |
| 6 | SN | 新序列号 | string(510) | Y |  |
| 7 | ITEM_LOT_ID | 新批号 | GUID | Y |  |
| 8 | UPDATE_DATE | 更新保修期 | number(0/1) | Y |  |
| 9 | UPDATE_MAIN | 仅更新主机 | number(0/1) | Y |  |
| 10 | UPDATETYPE | 更新保修期方式 | string(40) | Y |  |
| 11 | DELAY_NUM | 顺延数 | number(16,0) | Y |  |
| 12 | DELAY_UNIT | 顺延单位 | string(40) | Y |  |
| 13 | EXPIRY_DATE | 保修截止日期 | date | Y |  |
| 14 | EXPIRY_DATE2 | 有偿保修截止日期 | date | Y |  |
| 15 | PRODUCT_ID | 成品识别码 | string(510) | Y |  |
| 16 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | ORIG_EXPIRY_DATE | 原保修截止日期 | date | Y |  |
| 19 | ORIG_EXPIRY_DATE2 | 原有偿保修截止日 | date | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | SERVICE_DOC_D_ID |  | GUID | Y |  |

### SERVICE_EMPLOYEE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_EMPLOYEE_ID | 主键 | GUID | Y | Y |
| 4 | SC_EMPLOYEE | 服务域直属人员 | number(0/1) | Y |  |
| 5 | EMPLOYEE_ID | 服务人员 | GUID | Y |  |
| 6 | SERVICE_SITE_ID | 服务站点 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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

### SERVICE_ITEM (服务项目)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | SERVICE_ITEM_CODE | 项目编号 | string(80) | Y |  |
| 5 | SERVICE_ITEM_NAME | 项目内容 | string(510) | Y |  |
| 6 | RESULT_TYPE | 结果类型 | string(2) | Y |  |
| 7 | RESULT_UNIT_ID | 维护结果单位 | GUID | Y |  |
| 8 | TOP_LIMIT | 默认数值上限 | number(16,0) | Y |  |
| 9 | LOWER_LIMIT | 默认数值下限 | number(16,0) | Y |  |
| 10 | KNOWLEDGE_BASE_ID | 知识库分类 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
| 13 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### SERVICE_ITEM_D (服务项目--结果单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_ITEM_D_ID | 主键 | GUID | Y | Y |
| 3 | RESULT | 服务结果 | string(510) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
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
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | SERVICE_ITEM_ID |  | GUID | Y |  |

### SERVICE_PERIOD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_PERIOD_ID | 主键 | GUID | Y | Y |
| 4 | PERIOD_CODE | 周期编号 | string(80) | Y |  |
| 5 | PERIOD_NAME | 周期名称 | string(160) | Y |  |
| 6 | PERIOD_TYPE | 类型 | string(2) | Y |  |
| 7 | PERIOD_DATE | 指定周期日 | string(4) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | PERIOD_QTY | 周期量 | number(16,6) | Y |  |
| 10 | PERIOD_UNIT | 周期单位 | string(40) | Y |  |
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

### SERVICE_PERIOD_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_PERIOD_D_ID | 主键 | GUID | Y | Y |
| 2 | TIMES | 次数 | string(8) | Y |  |
| 3 | PERIOD_QTY | 周期量 | number(16,6) | Y |  |
| 4 | PERIOD_UNIT | 时间单位 | string(2) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
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
| 31 | SERVICE_PERIOD_ID |  | GUID | Y |  |

### SERVICE_QUOTATION

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SERVICE_QUOTATION_ID | 主键 | GUID | Y | Y |
| 7 | QUOTATION_DATE | 报价日期 | date | Y |  |
| 8 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 9 | EXPIRY_TIME | 有效期间 | string(100) | Y |  |
| 10 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 11 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 12 | CURRENCY_ID | 币种 | GUID | Y |  |
| 13 | AMOUNT_UNINCLUDE_TAX | 未税金额 | number(23,8) | Y |  |
| 14 | TAX | 税额 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
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
| 34 | PrintCount | 打印次数 | number | Y |  |
| 35 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 36 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 37 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 38 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### SERVICE_QUOTATION_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_QUOTATION_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | QUANTITY | 数量 | number(16,6) | Y |  |
| 8 | UNIT_ID | 单位 | GUID | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | PRODUCT_ID | 成品识别码 | string(510) | Y |  |
| 11 | LEVEL_CODE | 层级码 | string(200) | Y |  |
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
| 39 | SERVICE_QUOTATION_ID |  | GUID | Y |  |

### SERVICE_QUOTATION_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_QUOTATION_SD_ID | 主键 | GUID | Y | Y |
| 3 | SERVICE_CHARGE | 服务费用 | number(0/1) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | QUANTITY | 数量 | number(16,6) | Y |  |
| 9 | UNIT_ID | 单位 | GUID | Y |  |
| 10 | PRICE | 单价 | number(23,8) | Y |  |
| 11 | AMOUNT | 金额 | number(23,8) | Y |  |
| 12 | TAX_ID | 税种 | GUID | Y |  |
| 13 | TAX_RATE | 稅率 | number(5,4) | Y |  |
| 14 | AMOUNT_UNINCLUDE_TAX | 未税金额 | number(23,8) | Y |  |
| 15 | TAX | 税额 | number(23,8) | Y |  |
| 16 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 17 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
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
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | SERVICE_QUOTATION_D_ID |  | GUID | Y |  |

### SERVICE_REQUEST (服务请求单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SERVICE_REQUEST_ID | 主键 | GUID | Y | Y |
| 7 | RECEIVE_TIME | 接单时间 | time | Y |  |
| 8 | SERVICE_TYPE_ID | 服务类型 | GUID | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | CONTACT_PHONE | 联系电话 | string(100) | Y |  |
| 11 | DESCRIPTION | 内容描述 | string(510) | Y |  |
| 12 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 13 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 14 | SERVICE_MODE | 服务方式 | string(40) | Y |  |
| 15 | STATE | 结案 | number(0/1) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | CONTACT | 联系人 | string(120) | Y |  |
| 18 | ADDRESS | 地址 | string(200) | Y |  |
| 19 | RECEIVE_DATE | 接单日期 | date | Y |  |
| 20 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 21 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 22 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 23 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 24 | PrintCount | 打印次数 | number | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Attachments | 附件 | string | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | Owner_Org_RTK |  | string(400) | Y |  |
| 56 | Owner_Org_ROid |  | GUID | Y |  |

### SERVICE_REQUEST_D (服务请求单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_REQUEST_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | SN | 序列号 | string(510) | Y |  |
| 8 | QUANTITY | 数量 | number(16,6) | Y |  |
| 9 | UNIT_ID | 单位 | GUID | Y |  |
| 10 | DESCRIPTION | 请求内容 | string(510) | Y |  |
| 11 | UNDER_WARRANTY | 保修期内 | number(0/1) | Y |  |
| 12 | UNDER_WARRANTY2 | 有偿保修期内 | number(0/1) | Y |  |
| 13 | DEADLINE | 要求完成期限 | date | Y |  |
| 14 | RECEIVE_MODE | 收件方式 | string(40) | Y |  |
| 15 | RECEIVE_STATE | 收件状态 | string(40) | Y |  |
| 16 | SERVICE_RECEIPT_ID | 收件单号 | GUID | Y |  |
| 17 | SEND_MODE | 发件方式 | string(40) | Y |  |
| 18 | SEND_STATE | 发件状态 | string(40) | Y |  |
| 19 | SERVICE_ISSUE_ID | 发件单号 | GUID | Y |  |
| 20 | SERVICE_URGENCY_ID | 紧急度 | GUID | Y |  |
| 21 | DISPATCH_DATE1 | 派到站点日期 | date | Y |  |
| 22 | DISPATCH_DATE2 | 派到人员日期 | date | Y |  |
| 23 | SERVICE_EMPLOYEE1_ID | 派到人员 | GUID | Y |  |
| 24 | SERVICE_EMPLOYEE2_ID | 派给站点人员 | GUID | Y |  |
| 25 | SERVICE_EMPLOYEE_ID | 处理人员 | GUID | Y |  |
| 26 | ASSISTANT | 协助处理人员 | string(510) | Y |  |
| 27 | DISPATCH_DESP | 派工说明 | string(510) | Y |  |
| 28 | BEGIN_DATE | 计划开始处理日期 | date | Y |  |
| 29 | END_DATE | 计划完成处理日期 | date | Y |  |
| 30 | TASK_TIME | 计划工时 | number(16,1) | Y |  |
| 31 | ACTUAL_BEGIN_DATE | 实际开始日期 | date | Y |  |
| 32 | ACTUAL_END_DATE | 实际结束日期 | date | Y |  |
| 33 | ACTUAL_TASK_TIME | 实际工时 | number(16,1) | Y |  |
| 34 | REQUEST_STATE | 请求单状态 | string(40) | Y |  |
| 35 | SERVICE_STATE | 处理状态 | string(40) | Y |  |
| 36 | PRODUCT_ID | 成品识别码 | string(510) | Y |  |
| 37 | REMARK | 备注 | string(510) | Y |  |
| 38 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 39 | RMA | RMA号 | string(120) | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |
| 68 | SITE_SUPPLIER_ID_RTK |  | string(400) | Y |  |
| 69 | SITE_SUPPLIER_ID_ROid |  | GUID | Y |  |
| 70 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 71 | SOURCE_ID_ROid |  | GUID | Y |  |
| 72 | SERVICE_REQUEST_ID |  | GUID | Y |  |

### SERVICE_REQUEST_SD (故障信息子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_REQUEST_SD_ID | 主键 | GUID | Y | Y |
| 3 | BREAKDOWN_ID | 故障编号 | GUID | Y |  |
| 4 | BREAKDOWN_DESC | 故障描述 | string(510) | Y |  |
| 5 | PROCESS_DATE | 处理日期 | date | Y |  |
| 6 | PROCESS_EMPLOYEE_ID | 处理人员 | GUID | Y |  |
| 7 | PROCESS_STATE | 处理状态 | string(40) | Y |  |
| 8 | PROCESS_DESC | 处理情况描述 | string(510) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
| 17 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 18 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 19 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 20 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 21 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 22 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 23 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 24 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 25 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 26 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 27 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 28 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 29 | UDF041 | 自定义字段12 | date | Y |  |
| 30 | UDF042 | 自定义字段13 | date | Y |  |
| 31 | UDF051 | 自定义字段14 | GUID | Y |  |
| 32 | UDF052 | 自定义字段15 | GUID | Y |  |
| 33 | UDF053 | 自定义字段16 | GUID | Y |  |
| 34 | UDF054 | 自定义字段17 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | SERVICE_REQUEST_D_ID |  | GUID | Y |  |

### SERVICE_REQUEST_SD2 (部门反馈子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_REQUEST_SD2_ID | 主键 | GUID | Y | Y |
| 3 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 4 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 5 | DATE | 反馈日期 | date | Y |  |
| 6 | OPINION | 反馈意见 | string(510) | Y |  |
| 7 | REMARK | 备注 | string(400) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | SERVICE_REQUEST_D_ID |  | GUID | Y |  |

### SERVICE_REQUEST_SD3 (历史处理状态)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_REQUEST_SD3_ID | 主键 | GUID | Y | Y |
| 2 | PROCESS_DATE | 处理日期 | date | Y |  |
| 3 | PROCESS_STATE | 状态 | string(40) | Y |  |
| 4 | SERVICE_TYPE_ID | 服务类型 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 35 | SOURCE_ID_ROid |  | GUID | Y |  |
| 36 | SERVICE_REQUEST_D_ID |  | GUID | Y |  |

### SERVICE_SETTLEMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SERVICE_SETTLEMENT_ID | 主键 | GUID | Y | Y |
| 7 | SETTLEMENT_DATE | 结算日期 | date | Y |  |
| 8 | SERVICE_SITE_ID | 站点 | GUID | Y |  |
| 9 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 10 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 11 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 12 | CURRENCY_ID | 币种 | GUID | Y |  |
| 13 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 14 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 15 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 16 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 17 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 18 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 19 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | PrintCount | 打印次数 | number | Y |  |
| 24 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 25 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 26 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 27 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 37 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 38 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 39 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 40 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 41 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 42 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 43 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 44 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 45 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 46 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 47 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 48 | UDF041 | 自定义字段12 | date | Y |  |
| 49 | UDF042 | 自定义字段13 | date | Y |  |
| 50 | UDF051 | 自定义字段14 | GUID | Y |  |
| 51 | UDF052 | 自定义字段15 | GUID | Y |  |
| 52 | UDF053 | 自定义字段16 | GUID | Y |  |
| 53 | UDF054 | 自定义字段17 | GUID | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | Owner_Org_RTK |  | string(400) | Y |  |
| 58 | Owner_Org_ROid |  | GUID | Y |  |

### SERVICE_SETTLEMENT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SERVICE_SETTLEMENT_D_ID | 主键 | GUID | Y | Y |
| 3 | SETTLEMENT_TYPE | 类别 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | SN | 序列号 | string(510) | Y |  |
| 8 | QUANTITY | 数量 | number(16,6) | Y |  |
| 9 | UNIT_ID | 单位 | GUID | Y |  |
| 10 | PRICE | 单价 | number(23,8) | Y |  |
| 11 | AMOUNT | 金额 | number(23,8) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 16 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 17 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 18 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 19 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 20 | TAX_ID | 税种 | GUID | Y |  |
| 21 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | SERVICE_SETTLEMENT_ID |  | GUID | Y |  |

### SERVICE_SITE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_SITE_ID | 主键 | GUID | Y | Y |
| 4 | SERVICE_SITE_CODE | 编号 | string(40) | Y |  |
| 5 | SERVICE_SITE_NAME | 名称 | string(120) | Y |  |
| 6 | SERVICE_SITE_SHORTNAME | 简称 | string(40) | Y |  |
| 7 | PLANT_ID | 工厂 | GUID | Y |  |
| 8 | ADDRESS1 | 地址一 | string(200) | Y |  |
| 9 | ADDRESS2 | 地址二 | string(200) | Y |  |
| 10 | TEL_NO1 | 电话一 | string(80) | Y |  |
| 11 | TEL_NO2 | 电话二 | string(80) | Y |  |
| 12 | FAX_NO | 传真 | string(80) | Y |  |
| 13 | E_MAIL | 邮箱 | string(80) | Y |  |
| 14 | POST_CODE | 邮编 | string(20) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### SERVICE_SITE_EMPLOYEE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_SITE_EMPLOYEE_ID | 主键 | GUID | Y | Y |
| 2 | EMPLOYEE_ID | 主键 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | SERVICE_SITE_ID |  | GUID | Y |  |

### SERVICE_SITE_WAREHOUSE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SERVICE_SITE_WAREHOUSE_ID |  | GUID | Y | Y |
| 2 | WAREHOUSE_ID | 主键 | GUID | Y |  |
| 3 | REMARK |  | string(510) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | SERVICE_SITE_ID |  | GUID | Y |  |

### SERVICE_TYPE (服务类型)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_TYPE_ID | 主键 | GUID | Y | Y |
| 4 | SERVICE_TYPE_CODE | 编号 | string(40) | Y |  |
| 5 | SERVICE_TYPE_NAME | 名称 | string(120) | Y |  |
| 6 | UPDATE_SERVICE | 更新主动服务信息 | number(0/1) | Y |  |
| 7 | UPDATE_INSTALLATION | 更新安装信息 | number(0/1) | Y |  |
| 8 | ACCEPTANCE | 需验收 | number(0/1) | Y |  |
| 9 | ACCEPTANCE_INSTANT | 直接验收 | number(0/1) | Y |  |
| 10 | FUNCTION_SET | 可用功能单元设置 | string(120) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
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

### SERVICE_URGENCY (服务紧急度)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SERVICE_URGENCY_ID | 主键 | GUID | Y | Y |
| 4 | SERVICE_URGENCY_CODE | 编号 | string(400) | Y |  |
| 5 | SERVICE_URGENCY_NAME | 名称 | string(400) | Y |  |
| 6 | PROCESS_HOURS | 默认处理小时 | number | Y |  |
| 7 | REMARK | 备注 | string(400) | Y |  |
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