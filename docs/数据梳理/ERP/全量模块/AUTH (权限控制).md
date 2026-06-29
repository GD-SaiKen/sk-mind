---
module: "AUTH"
name_zh: "权限控制"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 123
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# AUTH (权限控制)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 123

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]
- [[PARA (参数设置)|PARA (参数设置)]]

---

## Tables


- **AUTH_BASE_CONDITIONS**
- **AUTH_CONFIDENTIALITY_FIELDS**
- **AUTH_CONSTRAINT_CONDITIONS**
- **AUTH_CONSTRAINT_FILTERS**
- **AUTH_ENTITY_CONDITIONS**
- **AUTH_ENTITY_FILTERS**


---


---


> Tables: 6

### AUTH_BASE_CONDITIONS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AUTH_FILTER_CONDITION_ID |  | GUID | Y | Y |
| 2 | LEFT_BRACKET |  | string(400) | Y |  |
| 3 | TYPE_KEY |  | string(400) | Y |  |
| 4 | PATH |  | string(400) | Y |  |
| 5 | PROPERTY_NAME |  | string(400) | Y |  |
| 6 | COMPARE |  | number | Y |  |
| 7 | VALUE | 值 | string(2000) | Y |  |
| 8 | IS_CONTEXT_VALUE | VALUE是否是运行时解析的上下文。例如，当前用户，当前组织等。否则根据属性的实体定义获取值类型 | number(0/1) | Y |  |
| 9 | RIGHT_BRACKET |  | string(400) | Y |  |
| 10 | LOGIC |  | number | Y |  |
| 11 | SEQUENCE | 从0开始的条件顺序编号 | number | Y |  |
| 12 | DATA_TYPE | 数据类型 | string(60) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
| 20 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 21 | ApproveDate | 修改日期 | date | Y |  |
| 22 | ApproveBy | 修改人 | GUID | Y |  |
| 23 | BASE_AUTHORIZATION_ID |  | GUID | Y |  |

### AUTH_CONFIDENTIALITY_FIELDS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AUTH_CONFIDENTIALITY_FIELD_ID |  | GUID | Y | Y |
| 2 | PATH |  | string(400) | Y |  |
| 3 | PROPERTY_NAME |  | string(200) | Y |  |
| 4 | STYLE |  | number | Y |  |
| 5 | SUBHEAD |  | string(200) | Y |  |
| 6 | STRATEGY |  | string(80) | Y |  |
| 7 | SEQUENCE | 从0开始的条件顺序编号 | number | Y |  |
| 8 | DESCRIPTION |  | string(160) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
| 16 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 17 | ApproveDate | 修改日期 | date | Y |  |
| 18 | ApproveBy | 修改人 | GUID | Y |  |
| 19 | DATA_ROLE_AUTHORIZATION_ID |  | GUID | Y |  |

### AUTH_CONSTRAINT_CONDITIONS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AUTH_FILTER_CONDITION_ID |  | GUID | Y | Y |
| 2 | LEFT_BRACKET |  | string(400) | Y |  |
| 3 | TYPE_KEY |  | string(400) | Y |  |
| 4 | PATH |  | string(400) | Y |  |
| 5 | PROPERTY_NAME |  | string(400) | Y |  |
| 6 | COMPARE |  | number | Y |  |
| 7 | VALUE | 值 | string(2000) | Y |  |
| 8 | IS_CONTEXT_VALUE | VALUE是否是运行时解析的上下文。例如，当前用户，当前组织等。否则根据属性的实体定义获取值类型 | number(0/1) | Y |  |
| 9 | RIGHT_BRACKET |  | string(400) | Y |  |
| 10 | LOGIC |  | number | Y |  |
| 11 | SEQUENCE | 从0开始的条件顺序编号 | number | Y |  |
| 12 | DATA_TYPE | 数据类型 | string(60) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
| 20 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 21 | ApproveDate | 修改日期 | date | Y |  |
| 22 | ApproveBy | 修改人 | GUID | Y |  |
| 23 | AUTH_CONSTRAINT_FILTER_ID |  | GUID | Y |  |

### AUTH_CONSTRAINT_FILTERS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AUTH_CONSTRAINT_FILTER_ID |  | GUID | Y | Y |
| 2 | PATH | 属性路径（复杂属性请在PROPERTY_NAME中设置） | string(400) | Y |  |
| 3 | PROPERTY_NAME |  | string(400) | Y |  |
| 4 | FILTER_NAME |  | string(4000) | Y |  |
| 5 | DESCRIPTION |  | string(4000) | Y |  |
| 6 | SEQUENCE | 从0开始的条件顺序编号 | number | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
| 14 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 15 | ApproveDate | 修改日期 | date | Y |  |
| 16 | ApproveBy | 修改人 | GUID | Y |  |
| 17 | DATA_ROLE_AUTHORIZATION_ID |  | GUID | Y |  |

### AUTH_ENTITY_CONDITIONS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AUTH_FILTER_CONDITION_ID |  | GUID | Y | Y |
| 2 | LEFT_BRACKET |  | string(400) | Y |  |
| 3 | TYPE_KEY |  | string(400) | Y |  |
| 4 | PATH |  | string(400) | Y |  |
| 5 | PROPERTY_NAME |  | string(400) | Y |  |
| 6 | COMPARE |  | number | Y |  |
| 7 | VALUE | 值 | string(2000) | Y |  |
| 8 | IS_CONTEXT_VALUE | VALUE是否是运行时解析的上下文。例如，当前用户，当前组织等。否则根据属性的实体定义获取值类型 | number(0/1) | Y |  |
| 9 | RIGHT_BRACKET |  | string(400) | Y |  |
| 10 | LOGIC |  | number | Y |  |
| 11 | SEQUENCE | 从0开始的条件顺序编号 | number | Y |  |
| 12 | DATA_TYPE | 数据类型 | string(60) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
| 20 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 21 | ApproveDate | 修改日期 | date | Y |  |
| 22 | ApproveBy | 修改人 | GUID | Y |  |
| 23 | AUTH_ENTITY_FILTER_ID |  | GUID | Y |  |

### AUTH_ENTITY_FILTERS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AUTH_ENTITY_FILTER_ID |  | GUID | Y | Y |
| 2 | ACTIONS | 如果为空，则不作权限控管；否则，代表用户有指定操作的权限。如：Read,Save | string(400) | Y |  |
| 3 | FILTER_NAME |  | string(600) | Y |  |
| 4 | SUBHEAD |  | string(200) | Y |  |
| 5 | STRATEGY |  | string(80) | Y |  |
| 6 | DESCRIPTION |  | string(160) | Y |  |
| 7 | SEQUENCE | 从0开始的条件顺序编号 | number | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 16 | ApproveDate | 修改日期 | date | Y |  |
| 17 | ApproveBy | 修改人 | GUID | Y |  |
| 18 | DATA_ROLE_AUTHORIZATION_ID |  | GUID | Y |  |