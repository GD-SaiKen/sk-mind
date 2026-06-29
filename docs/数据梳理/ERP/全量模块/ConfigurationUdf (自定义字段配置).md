---
module: "ConfigurationUdf"
name_zh: "自定义字段配置"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 30
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# ConfigurationUdf (自定义字段配置)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 30

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


- **ConfigurationUdf_RH (UDF级别的差量对象变更历史)**


---


---


> Tables: 2

### ConfigurationUdf (UDF级别的差量对象)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConfigurationUdfId | 主键 | GUID | Y | Y |
| 2 | ServiceTypeKey | 服务实例的TypeKey，例如Customer | string(400) | Y |  |
| 3 | SubHead | 视图名称 | string(400) | Y |  |
| 4 | AssignmentType | 0为全部用户，全部用户时ConfigurationUDFAssignedUsers无记录，1为指定用户 | number | Y |  |
| 5 | ProjectName | 方案名称 | string(400) | Y |  |
| 6 | Description | 方案描述 | string(1200) | Y |  |
| 7 | ReleaseDateTime | 发布时间 | date | Y |  |
| 8 | PublishStatus | 是否已发布 | string(20) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 17 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 18 | ApproveDate | 修改日期 | date | Y |  |
| 19 | ApproveBy | 修改人 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |

### ConfigurationUdf_RH (UDF级别的差量对象变更历史)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConfigurationUdf_RH_ID | 主键 | GUID | Y | Y |
| 2 | ServiceTypeKey | 服务实例的TypeKey，例如Customer | string(400) |  |  |
| 3 | SubHead | 视图名称 | string(400) |  |  |
| 4 | AssignmentType | 0为全部用户，全部用户时ConfigurationUDFAssignedUsers无记录，1为指定用户 | number |  |  |
| 5 | ProjectName | 方案名称 | string(400) |  |  |
| 6 | Description | 方案描述 | string(1200) |  |  |
| 7 | ReleaseDateTime | 发布时间 | date |  |  |
| 8 | ExpireDateTime | 失效时间 | date |  |  |
| 9 | PublishStatus | 是否已发布 | string(20) |  |  |
| 10 | ConfigurationUdfId | 记录发布历史对应的ConfigurationUdf表主键 | GUID |  |  |