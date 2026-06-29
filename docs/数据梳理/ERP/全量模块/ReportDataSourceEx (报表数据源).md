---
module: "ReportDataSourceEx"
name_zh: "报表数据源"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 7
columns: 94
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# ReportDataSourceEx (报表数据源)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 7 | Columns: 94

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


- **ReportDataSourceEx_CalcColumn**
- **ReportDataSourceEx_Conditions**
- **ReportDataSourceEx_DataElement**
- **ReportDataSourceEx_GroupColumn**
- **ReportDataSourceEx_RefColumn**
- **ReportDataSourceEx_Relation**


---


---


> Tables: 7

### ReportDataSourceEx

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ReportDataSourceExId | 报表数据源扩展ID | GUID | Y | Y |
| 2 | TypeKey | 报表数据源扩展所属作业资源键 | string(200) |  |  |
| 3 | ReportDataSourceId | 扩展的报表数据源Id | string(200) |  |  |
| 4 | ReportDataSourceItemId | 扩展的报表数据源项Id，例如DataSet中的子表、DMQCombineQuery中的子查询 | string(400) |  |  |
| 5 | VersionNumber | 数据源扩展设置的版本号 | number |  |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |

### ReportDataSourceEx_CalcColumn

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ColumnId | 列Id | GUID | Y | Y |
| 2 | ColumnAlias | 别名 | string(400) |  |  |
| 3 | DisplayName | 显示名称 | string(400) |  |  |
| 4 | Description | 描述 | string(400) |  |  |
| 5 | DataType | 数据类型，对应GeneralDBType | string(40) |  |  |
| 6 | Sequence | 列的顺序 | number |  |  |
| 7 | Expression | 计算列的表达式 | string(4000) |  |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | ReportDataSourceExId |  | GUID | Y |  |

### ReportDataSourceEx_Conditions

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | RelationConditionExtensionId | 条件ID | GUID | Y | Y |
| 2 | LeftValueType | 条件的左值类型，例如字段、表达式 | string(40) |  |  |
| 3 | LeftValue | 条件的左值 | string(400) |  |  |
| 4 | RightValueType | 条件的右值类型，例如字段、表达式 | string(40) |  |  |
| 5 | RightValue | 条件的右值 | string(400) |  |  |
| 6 | CompareOperator | 条件的操作符 | string(40) |  |  |
| 7 | ConditionType | 条件的类型 | string(40) |  |  |
| 8 | Script | 条件表达式 | string(2000) |  |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | DataElementRelationExtensionId |  | GUID | Y |  |

### ReportDataSourceEx_DataElement

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DataElementExtensionId | 关联表的Id | GUID | Y | Y |
| 2 | DataElementId | 数据元素Id | string(400) |  |  |
| 3 | DataEntityTypeName | 关联的实体名称 | string(400) |  |  |
| 4 | DisplayName | 关联表外显名称 | string(400) |  |  |
| 5 | Description | 关联表描述 | string(400) |  |  |
| 6 | Disabled | 数据源扩展是否禁用 | number(0/1) |  |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | ReportDataSourceExId |  | GUID | Y |  |

### ReportDataSourceEx_GroupColumn

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ColumnId | 列Id | GUID | Y | Y |
| 2 | ColumnAlias | 别名 | string(400) |  |  |
| 3 | DisplayName | 显示名称 | string(400) |  |  |
| 4 | Description | 描述 | string(400) |  |  |
| 5 | DataType | 数据类型，对应GeneralDBType | string(40) |  |  |
| 6 | Sequence | 列的顺序 | number |  |  |
| 7 | ReferenceDataElementId | 关联的数据元素 | string(400) |  |  |
| 8 | ReferenceDataElementColumnId | 关联的实体属性名 | string(400) |  |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | ReportDataSourceExId |  | GUID | Y |  |

### ReportDataSourceEx_RefColumn

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ColumnId | 列Id | GUID | Y | Y |
| 2 | ColumnAlias | 别名 | string(400) |  |  |
| 3 | DisplayName | 显示名称 | string(400) |  |  |
| 4 | Description | 描述 | string(400) |  |  |
| 5 | DataType | 数据类型，对应GeneralDBType | string(40) |  |  |
| 6 | Sequence | 列的顺序 | number |  |  |
| 7 | ReferenceDataElementId | 关联的数据元素 | string(400) |  |  |
| 8 | ReferenceDataElementColumnId | 关联的实体属性名 | string(400) |  |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | ReportDataSourceExId |  | GUID | Y |  |

### ReportDataSourceEx_Relation

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DataElementRelationExtensionId | 引用的数据元素Id | GUID | Y | Y |
| 2 | ParentDataElementId | 关联的左表 | string(400) |  |  |
| 3 | ChildDataElementId | 关联的右表 | string(400) |  |  |
| 4 | RelationType | 关联类型 | string(40) |  |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | ReportDataSourceExId |  | GUID | Y |  |