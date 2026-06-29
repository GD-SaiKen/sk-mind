---
module: "MENU"
name_zh: "菜单管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 74
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# MENU (菜单管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 74

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]
- [[PARA (参数设置)|PARA (参数设置)]]

---

## Tables


- **MENU_D**
- **MENU_D_LANGUAGE**
- **MENU_LANGUAGE**


---


---


> Tables: 4

### MENU

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MENU_ID |  | GUID | Y | Y |
| 4 | MENU_CODE |  | string(40) | Y |  |
| 5 | MENU_TYPE |  | string(40) | Y |  |
| 6 | APPLICATION_TYPE | 用于区分标准菜单对应的版本类型（专业、集团、流通） | number | Y |  |
| 7 | REMARK |  | string(160) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
| 15 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
| 17 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 18 | ApproveDate | 修改日期 | date | Y |  |
| 19 | ApproveBy | 修改人 | GUID | Y |  |
| 20 | Owner_Org_RTK |  | string(400) | Y |  |
| 21 | Owner_Org_ROid |  | GUID | Y |  |

### MENU_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MENU_D_ID | 主键 | GUID | Y | Y |
| 2 | MENU_D_NAME | 作业名称 | string(160) | Y |  |
| 3 | MENU_CONTENT | 可以是ProgramID、Web链接地址等 | string(200) | Y |  |
| 4 | MENU_TYPE | 1:目录;2:平台作业;3:Web链接;4:其它(未定) | number | Y |  |
| 5 | SORT_INDEX | 索引序号 | number | Y |  |
| 6 | PROGRAM_STRATEGY | 作业类型 | number | Y |  |
| 7 | REMARK |  | string(160) | Y |  |
| 8 | LEVEL | Menu层阶 | number | Y |  |
| 9 | PARENT_MENU_D_ID | Parent主键 | GUID | Y |  |
| 10 | EXTEND_HTML | 点击目录节点时链接到的URL(在ExtendHtml Webpart中显示) | string(200) | Y |  |
| 11 | PARAMETERS | 参数 | string(400) | Y |  |
| 12 | IS_PROVIDE_HELP | 是否提供帮助 | number(0/1) | Y |  |
| 13 | HELP_ID | 帮助文件名 | string(200) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
| 21 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 22 | ApproveDate | 修改日期 | date | Y |  |
| 23 | ApproveBy | 修改人 | GUID | Y |  |
| 24 | MENU_ID |  | GUID | Y |  |
| 25 | Image | 对应图片库中的图标 | string(40) | Y |  |

### MENU_D_LANGUAGE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MENU_D_LANGUAGE_ID | 主键 | GUID | Y | Y |
| 2 | MENU_NAME | 作业名称 | string(160) | Y |  |
| 3 | LANGUAGE | 语言别 | string(160) | Y |  |
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
| 14 | MENU_D_ID |  | GUID | Y |  |

### MENU_LANGUAGE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MENU_LANGUAGE_ID | 主键 | GUID | Y | Y |
| 2 | MENU_NAME | 作业名称 | string(160) | Y |  |
| 3 | LANGUAGE | 语言别 | string(160) | Y |  |
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
| 14 | MENU_ID |  | GUID | Y |  |