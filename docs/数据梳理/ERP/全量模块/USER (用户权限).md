---
module: "USER"
name_zh: "用户权限"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 0
columns: 0
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# USER (用户权限)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 0 | Columns: 0

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]

---

# USER (用户权限)

> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
 | Server: .\\SQLEXPRESS | Tables: 6 | Generated: 2026-06-25 10:52

---


> Tables: 6

### USER - 登陆用户

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | USER_ID | 主键 | GUID | Y | Y |
| 4 | LOGONNAME | 登陆名 | string(80) | Y |  |
| 5 | USER_NAME | 用户名 | string(400) | Y |  |
| 6 | USER_TYPE | 类型 | string(40) | Y |  |
| 7 | SECURITYIDENTITY | 用户标识 | string(400) | Y |  |
| 8 | DOMAINUSERNAME | 域用户名 | string(400) | Y |  |
| 9 | SECURITYDOMAINUSERNAME | 域用户标识 | string(400) | Y |  |
| 10 | LOGONTIME | 登陆时间 | date | Y |  |
| 11 | AVAILABLE_DATE | 生效日期 | date | Y |  |
| 12 | UNAVAILABLE_DATE | 失效日期 | date | Y |  |
| 13 | REMARK | 备注 | string(400) | Y |  |
| 14 | DEF_LANGUAGE | 默认语言别 | string(40) | Y |  |
| 15 | ITEM_SHORTCUT | 品号快捷码 | string(40) | Y |  |
| 16 | CUSTOMER_SHORTCUT | 客户快捷码 | string(40) | Y |  |
| 17 | SUPPLIER_SHORTCUT | 供货商快捷码 | string(40) | Y |  |
| 18 | DATE_FORMAT | 日期格式 | string(40) | Y |  |
| 19 | DATE_AREA | 日期区域 | string(40) | Y |  |
| 20 | FIRST_DAY_OF_WEEK | 一周的第一天 | string(40) | Y |  |
| 21 | DEF_COMPANY_ID | 默认公司 | GUID | Y |  |
| 22 | DEF_PLANT_ID | 默认工厂 | GUID | Y |  |
| 23 | DEF_SALES_CENTER_ID | 默认销售域 | GUID | Y |  |
| 24 | DEF_SERVICE_CENTER_ID | 默认服务域 | GUID | Y |  |
| 25 | DEF_SUPPLY_CENTER_ID | 默认采购域 | GUID | Y |  |
| 26 | DEF_OPERATION_CENTER_ID | 默认营运域 | GUID | Y |  |
| 27 | DEF_USER_MENU_ID | 个人默认选定的菜单MenuId | string(80) | Y |  |
| 28 | DEF_SHOTCUT_MENU_ID | 个人快捷菜单MenuId集合，以","分隔 | string(1600) | Y |  |
| 29 | DEF_SHOTCUT_PROGRAMID | 个人快捷菜单作业ID，以"`"分隔 | string(1600) | Y |  |
| 30 | DEF_SHOTCUT_DISPLAYNAME | 个人快捷菜单显示名称，以"`"分隔 | string(1600) | Y |  |
| 31 | DEF_SHOTCUT_HELPID | 个人快捷菜单帮助文件名，以"`"分隔 | string(1600) | Y |  |
| 32 | EMPLOYEE_ID | 关联员工 | GUID | Y |  |
| 33 | SOURCE_TYPE | 来源 | string(40) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |

### USER_AUTH_ORG_CONDITIONS

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
| 11 | SEQUENCE | 顺序编号 | number | Y |  |
| 12 | DATA_TYPE | 数据类型 | string(60) | Y |  |
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
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | USER_AUTH_ORG_ROLE_ID |  | GUID | Y |  |

### USER_AUTH_ORG_ROLE - 用户扩展组织权限单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | USER_AUTH_ORG_ROLE_ID | 主键 | GUID | Y | Y |
| 2 | PROGRAM_ID |  | string(160) | Y |  |
| 3 | ENTITY_NAME |  | string(160) | Y |  |
| 4 | SEQUENCE | 序号 | number | Y |  |
| 5 | REMARK | 备注 | string(400) | Y |  |
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
| 34 | USER_ID |  | GUID | Y |  |

### USER_EMPLOYEE_RELATED - 员工关系人

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | USER_EMPLOYEE_RELATED_ID | 主键 | GUID | Y | Y |
| 2 | USER_EMPLOYEE_RELATED_NAME | 关系名称 | string(80) | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 29 | ApproveDate | 修改日期 | date | Y |  |
| 30 | ApproveBy | 修改人 | GUID | Y |  |
| 31 | TYPE_RTK |  | string(400) | Y |  |
| 32 | TYPE_ROid |  | GUID | Y |  |
| 33 | USER_ID |  | GUID | Y |  |

### USER_ORG - 用户组织单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | USER_ORG_ID | 主键 | GUID | Y | Y |
| 2 | CreateDate | 创建日期 | date | Y |  |
| 3 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 4 | ModifiedDate | 修改日期 | date | Y |  |
| 5 | CreateBy | 创建者 | GUID | Y |  |
| 6 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 7 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
| 27 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 28 | ApproveDate | 修改日期 | date | Y |  |
| 29 | ApproveBy | 修改人 | GUID | Y |  |
| 30 | ORG_RTK |  | string(400) | Y |  |
| 31 | ORG_ROid |  | GUID | Y |  |
| 32 | USER_ID |  | GUID | Y |  |

### USER_ROLE - 用户权限单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | USER_ROLE_ID | 主键 | GUID | Y | Y |
| 2 | REMARK | 备注 | string(400) | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 29 | ApproveDate | 修改日期 | date | Y |  |
| 30 | ApproveBy | 修改人 | GUID | Y |  |
| 31 | ROLE_RTK |  | string(400) | Y |  |
| 32 | ROLE_ROid |  | GUID | Y |  |
| 33 | USER_ID |  | GUID | Y |  |