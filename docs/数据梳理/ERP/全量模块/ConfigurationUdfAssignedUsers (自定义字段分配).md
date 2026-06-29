---
module: "ConfigurationUdfAssignedUsers"
name_zh: "自定义字段分配"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 18
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# ConfigurationUdfAssignedUsers (自定义字段分配)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 18

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


- **ConfigurationUdfAssignedUsers_RH (UDF分配用户信息)**


---


---


> Tables: 2

### ConfigurationUdfAssignedUsers (UDF分配用户信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConfigurationUdfUsersId |  | GUID | Y | Y |
| 2 | UserId |  | GUID | Y |  |
| 3 | ConfigurationUdfId | 配置主键，引用ConfigurationUdf表主键 | GUID | Y |  |
| 4 | Attachments | 附件 | string | Y |  |
| 5 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
| 13 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 14 | ApproveDate | 修改日期 | date | Y |  |
| 15 | ApproveBy | 修改人 | GUID | Y |  |

### ConfigurationUdfAssignedUsers_RH (UDF分配用户信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConfigurationUdfUsersId |  | GUID | Y | Y |
| 2 | UserId |  | GUID |  |  |
| 3 | ConfigurationUdfId | 配置主键，引用ConfigurationUdf表主键 | GUID |  |  |