---
module: "DataLogConfig"
name_zh: "日志配置"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 23
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# DataLogConfig (日志配置)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 23

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


- **DataLogConfig_TypeKeysInfo (记录数据日志的TypeKey信息)**


---


---


> Tables: 2

### DataLogConfig (数据日志设置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DataLogConfigId | 主键 | GUID | Y | Y |
| 2 | Enabled | 是否启用 | number(0/1) | Y |  |
| 3 | MonthLimit | 备份阀值 | number | Y |  |
| 4 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 5 | Attachments | 附件 | string | Y |  |
| 6 | Version | 版本号，不要随意更改 | binary | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |

### DataLogConfig_TypeKeysInfo (记录数据日志的TypeKey信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Id | 主键 | GUID | Y | Y |
| 2 | ProgramId | 作业编号 | string(400) | Y |  |
| 3 | TypeKey | TypeKey | string(400) | Y |  |
| 4 | Version | 版本号，不要随意更改 | binary | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | DataLogConfigId |  | GUID | Y |  |