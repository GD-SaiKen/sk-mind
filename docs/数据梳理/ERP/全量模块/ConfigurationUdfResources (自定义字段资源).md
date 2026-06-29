---
module: "ConfigurationUdfResources"
name_zh: "自定义字段资源"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 26
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# ConfigurationUdfResources (自定义字段资源)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 26

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


- **ConfigurationUdfResources_RH**


---


---


> Tables: 2

### ConfigurationUdfResources

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConfigurationUdfResourcesId |  | GUID | Y | Y |
| 2 | TypeKey | 服务实例的TypeKey，例如Customer | string(400) | Y |  |
| 3 | RunAt | 1 服务器端 2 客户端 3 公共 | number | Y |  |
| 4 | Culture | 配置的语言别 | string(40) | Y |  |
| 5 | ReleaseContent | 配置的正文描述。真正应用与系统的配置 | string | Y |  |
| 6 | DesignContent | 设计成果，生效时会将设计成果覆盖到ResourceContent | string | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 14 | ApproveDate | 修改日期 | date | Y |  |
| 15 | ApproveBy | 修改人 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
| 17 | ConfigurationUdfId |  | GUID | Y |  |
| 18 | SubHead | 视图名称。向导式批次作业时,该字段会记录配置所属的视图名称. | string(400) | Y |  |

### ConfigurationUdfResources_RH

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConfigurationUdfResourcesId |  | GUID | Y | Y |
| 2 | TypeKey | 服务实例的TypeKey，例如Customer | string(400) |  |  |
| 3 | SubHead | 视图名称。单身SubHead为空时，取单头的SubHead。 | string(400) |  |  |
| 4 | RunAt | 1 服务器端 2 客户端 3 公共 | number |  |  |
| 5 | Culture | 配置的语言别 | string(40) |  |  |
| 6 | ReleaseContent | 配置的正文描述。真正应用与系统的配置 | string |  |  |
| 7 | DesignContent | 设计成果，生效时会将设计成果覆盖到ResourceContent | string |  |  |
| 8 | ConfigurationUdf_RH_ID |  | GUID | Y |  |