---
module: "PROGRAM"
name_zh: "程序角色"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 114
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# PROGRAM (程序角色)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 114

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


- **PROGRAM_FOOTER_SIGN (作业注脚签核)**
- **PROGRAM_ROLE (作业角色实体)**
- **PROGRAM_ROLE_AUTHORIZATIONS (作业角色实体单身（每支作业的对应操作权限）)**
- **PROGRAM_USER_OPTION (作业用户选项)**


---


---


> Tables: 4

### PROGRAM_FOOTER_SIGN (作业注脚签核)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PROGRAM_FOOTER_SIGN_ID | 主键 | GUID | Y | Y |
| 4 | PROGRAM_ID | 作业 | string(120) | Y |  |
| 5 | PROGRAM_FOOTER_ID | 注脚 | GUID | Y |  |
| 6 | MODIFY_FOOTER_WHEN_PRINTING | 打印时更改注脚 | number(0/1) | Y |  |
| 7 | PROGRAM_SING_ID | 签核 | GUID | Y |  |
| 8 | MODIFY_SIGN_WHEN_PRINTING | 打印时更改签核 | number(0/1) | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### PROGRAM_ROLE (作业角色实体)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PROGRAM_ROLE_ID | 主键 | GUID | Y | Y |
| 4 | CODE |  | string(80) | Y |  |
| 5 | NAME | 角色名称 | string(80) | Y |  |
| 6 | DESCRIPTION |  | string(160) | Y |  |
| 7 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 8 | Attachments | 附件 | string | Y |  |
| 9 | Version | 版本号，不要随意更改 | binary | Y |  |
| 10 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 11 | ApproveDate | 修改日期 | date | Y |  |
| 12 | ApproveBy | 修改人 | GUID | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Owner_Org_RTK |  | string(400) | Y |  |
| 20 | Owner_Org_ROid |  | GUID | Y |  |

### PROGRAM_ROLE_AUTHORIZATIONS (作业角色实体单身（每支作业的对应操作权限）)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PROGRAM_ROLE_AUTHORIZATION_ID | 主键 | GUID | Y | Y |
| 2 | PROGRAM_ID | 作业ID | string(80) | Y |  |
| 3 | ACTIONS | 作业可用操作 | string(4000) | Y |  |
| 4 | SORT_INDEX | 排序序号 | number | Y |  |
| 5 | Version | 版本号，不要随意更改 | binary | Y |  |
| 6 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 7 | ApproveDate | 修改日期 | date | Y |  |
| 8 | ApproveBy | 修改人 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | PROGRAM_ROLE_ID |  | GUID | Y |  |

### PROGRAM_USER_OPTION (作业用户选项)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PROGRAM_USER_OPTION_ID | 主键 | GUID | Y | Y |
| 4 | USER_ID | 用户 | GUID | Y |  |
| 5 | PARENT_VIEW_CODE | 父视图编号 | string(80) | Y |  |
| 6 | USER_OPTION | 用户选项 | string | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | Attachments | 附件 | string | Y |  |
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |