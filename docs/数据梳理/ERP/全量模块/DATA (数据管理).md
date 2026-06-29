---
module: "DATA"
name_zh: "数据管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 162
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# DATA (数据管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 162

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]
- [[PARA (参数设置)|PARA (参数设置)]]

---

## Tables


- **DATA_EXCHANGE_LOG (数据交换日志)**
- **DATA_PRINT_LAYOUT**
- **DATA_PRINT_LAYOUT_D**
- **DATA_ROLE**
- **DATA_ROLE_AUTHORIZATIONS**
- **DATA_ROLE_BASE_AUTHORIZATIONS**


---


---


> Tables: 6

### DATA_EXCHANGE_LOG (数据交换日志)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DATA_EXCHANGE_LOG_ID | 主键 | GUID | Y | Y |
| 4 | EXCHANGE_RTK | 来源 | string(120) | Y |  |
| 5 | DATA_EXCHANGE_RTK | 实体来源 | string(80) | Y |  |
| 6 | DATA_EXCHANGE_ROid | 实体来源Id | GUID | Y |  |
| 7 | E10_DOC_CODE | E10单据类型 | string(80) | Y |  |
| 8 | E10_DOC_NO | E10单号/编号 | string(80) | Y |  |
| 9 | CRM_DOC_CODE | CRM单别 | string(80) | Y |  |
| 10 | CRM_DOC_NO | CRM单号/编号 | string(80) | Y |  |
| 11 | EXCHANGE_STATUS | 状态 | string(40) | Y |  |
| 12 | EXCHANGE_CODE | 传输码 | string(40) | Y |  |
| 13 | COMPANY_CODE | 公司 | string(80) | Y |  |
| 14 | SOURCE_TYPE | CRM来源单据 | string(6) | Y |  |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |

### DATA_PRINT_LAYOUT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DATA_PRINT_LAYOUT_ID | 主键 | GUID | Y | Y |
| 2 | PROGRAM_TYPKEY | 作业 | string(60) | Y |  |
| 3 | PROGRAM_VIEWNAME | 作业视图 | string(120) | Y |  |
| 4 | REPORT_TYPEKEY | 报表 | string(60) | Y |  |
| 5 | PRINT_LAYOUT_DEFAULT | 默认样式 | string(200) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | PROGRAM_ID | 作业ID | string(120) | Y |  |
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

### DATA_PRINT_LAYOUT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DATA_PRINT_LAYOUT_D_ID | 主键 | GUID | Y | Y |
| 2 | PRINT_LAYOUT_DEFAULT | 默认样式 | string(200) | Y |  |
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
| 29 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 30 | SOURCE_ID_ROid |  | GUID | Y |  |
| 31 | DATA_PRINT_LAYOUT_ID |  | GUID | Y |  |

### DATA_ROLE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DATA_ROLE_ID |  | GUID | Y | Y |
| 4 | CODE |  | string(40) | Y |  |
| 5 | NAME | 角色名称 | string(80) | Y |  |
| 6 | DESCRIPTION |  | string(160) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
| 14 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
| 16 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 17 | ApproveDate | 修改日期 | date | Y |  |
| 18 | ApproveBy | 修改人 | GUID | Y |  |
| 19 | Owner_Org_RTK |  | string(400) | Y |  |
| 20 | Owner_Org_ROid |  | GUID | Y |  |

### DATA_ROLE_AUTHORIZATIONS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DATA_ROLE_AUTHORIZATION_ID |  | GUID | Y | Y |
| 2 | TYPE_KEY |  | string(200) | Y |  |
| 3 | BASE_FILTER_TYPEKEYS |  | string(600) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Version | 版本号，不要随意更改 | binary | Y |  |
| 11 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 12 | ApproveDate | 修改日期 | date | Y |  |
| 13 | ApproveBy | 修改人 | GUID | Y |  |
| 14 | DATA_ROLE_ID |  | GUID | Y |  |

### DATA_ROLE_BASE_AUTHORIZATIONS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BASE_AUTHORIZATION_ID |  | GUID | Y | Y |
| 2 | NAME |  | string(200) | Y |  |
| 3 | FILTER_MESSAGE |  | string(400) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Version | 版本号，不要随意更改 | binary | Y |  |
| 11 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 12 | ApproveDate | 修改日期 | date | Y |  |
| 13 | ApproveBy | 修改人 | GUID | Y |  |
| 14 | DATA_ROLE_ID |  | GUID | Y |  |