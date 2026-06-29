---
module: "COMPANY"
name_zh: "公司设置"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 129
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# COMPANY (公司设置)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 129

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


- **COMPANY_ACCPERIOD_INFO (公司会计期间信息)**
- **COMPANY_ACCPERIOD_INFO_D (公司会计期间信息单身)**


---


---


> Tables: 3

### COMPANY (公司信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COMPANY_ID | 主键 | GUID | Y | Y |
| 4 | COMPANY_CODE | 公司编号 | string(20) | Y |  |
| 5 | COMPANY_NAME | 简称 | string(40) | Y |  |
| 6 | COMPANY_FULL_NAME | 全称 | string(144) | Y |  |
| 7 | TELEPHONE | 电话 | string(40) | Y |  |
| 8 | FAX | 传真 | string(40) | Y |  |
| 9 | TAX_ID | 税号 | string(40) | Y |  |
| 10 | PRINCIPAL | 负责人 | string(72) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | REGISTERED_ADDRESS1 | 注册地址一 | string(510) | Y |  |
| 13 | COMPANY_ENG_FULL_NME | 英文公司全称 | string(144) | Y |  |
| 14 | COMPANY_ENGLISH_ADDRESS1 | 英文公司地址一 | string(510) | Y |  |
| 15 | CORPORATION | 法人 | string(40) | Y |  |
| 16 | PRODUCTION_OPERATION_LICENSES | 生产/经营许可证 | string(40) | Y |  |
| 17 | LICENSE | 营业执照 | string(40) | Y |  |
| 18 | WEBSITE | 公司网站 | string(100) | Y |  |
| 19 | POSTCODE | 邮政编码 | string(40) | Y |  |
| 20 | ORGANIZATION_CODE | 组织机构代码 | string(40) | Y |  |
| 21 | COMPANY_NATURE | 公司性质 | string(100) | Y |  |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | Attachments | 附件 | string | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |
| 54 | IWC_TURN | 抛转 | number(0/1) | Y |  |
| 55 | IWC_USER | 用户名 | string(512) | Y |  |
| 56 | IWC_PASSWORD | 密码 | string(512) | Y |  |
| 57 | IWC_PHONE | 手机号 | string(40) | Y |  |
| 58 | IWC_GROUP_NO | 群组编号 | string(72) | Y |  |
| 59 | IWC_GROUP_NAME |  | string(200) | Y |  |

### COMPANY_ACCPERIOD_INFO (公司会计期间信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COMPANY_ACCPERIOD_INFO_ID | 主键 | GUID | Y | Y |
| 4 | EFFECT_AREA | 期间作用范围 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCPERIOD_DATASET_ID | 会计期间表编号 | GUID | Y |  |
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
| 34 | Owner_Org_RTK |  | string(400) | Y |  |
| 35 | Owner_Org_ROid |  | GUID | Y |  |

### COMPANY_ACCPERIOD_INFO_D (公司会计期间信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COMPANY_ACCPERIOD_INFO_D_ID | 主键 | GUID | Y | Y |
| 3 | ACCOUNT_PERIOD_CODE | 期号 | string(20) | Y |  |
| 4 | START_DATE | 开始日期 | date | Y |  |
| 5 | CUTOFF_DATE | 结束日期 | date | Y |  |
| 6 | QUARTER | 季度 | number | Y |  |
| 7 | ADJUSTING_INDICATOR | 调整期标识 | number(0/1) | Y |  |
| 8 | ADJUSTING_TYPE | 调整期类型 | number | Y |  |
| 9 | ACCOUNT_PERIOD_STATUS | 调整期状态 | number | Y |  |
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
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | COMPANY_ACCPERIOD_INFO_ID |  | GUID | Y |  |