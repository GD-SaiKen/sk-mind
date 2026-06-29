---
module: "MENUGROUP"
name_zh: "菜单组"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 40
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# MENUGROUP (菜单组)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 40

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


- **MENUGROUP_MENU**
- **MENUGROUP_USER**


---


---


> Tables: 3

### MENUGROUP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MENUGROUP_ID | 主键 | GUID | Y | Y |
| 2 | MENUGROUP_CODE | 群组代号 | string(20) | Y |  |
| 3 | MENUGROUP_NAME | 群组名称 | string(40) | Y |  |
| 4 | SHOW_STYLE | 菜单显示方式 | string(2) | Y |  |
| 5 | REMARK |  | string(510) | Y |  |
| 6 | Attachments | 附件 | string | Y |  |
| 7 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 8 | Version | 版本号，不要随意更改 | binary | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 16 | ApproveDate | 修改日期 | date | Y |  |
| 17 | ApproveBy | 修改人 | GUID | Y |  |

### MENUGROUP_MENU

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MENUGROUP_MENU_ID | 主键 | GUID | Y | Y |
| 2 | DEFAULT_MENU | 默认菜单 | number(0/1) | Y |  |
| 3 | REMARK |  | string(510) | Y |  |
| 4 | MENU_ID | 菜单代号 | GUID | Y |  |
| 5 | Version | 版本号，不要随意更改 | binary | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | MENUGROUP_ID |  | GUID | Y |  |

### MENUGROUP_USER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MENUGROUP_USER_ID |  | GUID | Y | Y |
| 2 | REMARK |  | string(510) | Y |  |
| 3 | EMPLOYEE_ID | 用户代号 | GUID | Y |  |
| 4 | Version | 版本号，不要随意更改 | binary | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | MENUGROUP_ID |  | GUID | Y |  |