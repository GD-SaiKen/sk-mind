---
module: "QueryAdvanced"
name_zh: "高级查询"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 58
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# QueryAdvanced (高级查询)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 58

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


- **QueryAdvanced_Conditions**
- **QueryAdvanced_OrderColumns**
- **QueryAdvanced_ViewColumns**


---


---


> Tables: 4

### QueryAdvanced

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | QueryAdvancedId | 查询方案ID | string(400) | Y | Y |
| 2 | Name | 查询方案名称 | string(400) |  |  |
| 3 | QueryProjectId | 限定方案ID，用以确定查询方案挂在哪个限定方案下 | string(400) |  |  |
| 4 | QueryProjectType | 限定方案类型 0,为出厂限定方案；1，为自定义限定方案 | number |  |  |
| 5 | OwnerId | 查询方案的所属者ID | GUID |  |  |
| 6 | TypeKey | 查询方案的所属作业资源键 | string(400) |  |  |
| 7 | IndentColumnCount | 查询方案的从左至右的可缩排列数,用户可设置 | number |  |  |
| 8 | GridLineStyle | 查询方案的表格线风格(只有横线:0、只有纵线:1、都有:2),用户可设置 | number |  |  |
| 9 | HorzLineColor | 查询方案的表格横线的颜色,用户可设置 | string(400) |  |  |
| 10 | VertLineColor | 查询方案的表格坚线的颜色,用户可设置 | string(400) |  |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |

### QueryAdvanced_Conditions

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | QueryAdvancedConditionItemId | 条件ID | string(400) | Y | Y |
| 2 | LeftBracket | 条件的左括弧 | string(400) |  |  |
| 3 | Field | 条件列的属性全路径 | string(400) |  |  |
| 4 | Operator | 条件列的操作符 | number |  |  |
| 5 | Value | 条件列的值 | string(400) |  |  |
| 6 | RightBracket | 条件的右括弧 | string(400) |  |  |
| 7 | Logic | 条件组的连接逻辑符 | number |  |  |
| 8 | DataType | 该条件列的数据类型冗余列 | number |  |  |
| 9 | Order | 该条件列的顺序 | number |  |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | QueryAdvancedId |  | string(400) | Y |  |

### QueryAdvanced_OrderColumns

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | OrderColumnId | 排序列ID | string(400) | Y | Y |
| 2 | PropertyPath | 查询视图内所含数据列的属性全路径 | string(400) |  |  |
| 3 | IsAsc | 查询视图中数据列数据的排序方式 1升序 0降序 | number(0/1) |  |  |
| 4 | SortSequence | 查询视图中数据列数据的排序顺序 | number |  |  |
| 5 | DisplayName | 查询视图内排序列的显示名称 | string(400) |  |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | QueryAdvancedId |  | string(400) | Y |  |

### QueryAdvanced_ViewColumns

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ViewColumnId | 视图列ID | string(400) | Y | Y |
| 2 | PropertyPath | 查询视图内所含数据列的属性全路径 | string(400) |  |  |
| 3 | DisplayName | 查询视图内所含数据列的显示名称 | string(400) |  |  |
| 4 | Width | 查询视图内所含数据列在浏览时显示的宽度 | number |  |  |
| 5 | IsFixed | 查询视图内所含数据列在浏览时是否靠左固定，目前仅提供靠左固定，列的固定顺序根据显示顺序排列 | number(0/1) |  |  |
| 6 | AutoHeight | 查询视图内所在列是否自动行高（自动折行显示全部内容） | number(0/1) |  |  |
| 7 | ColumnSequence | 查询视图内所含数据列的序号 | number |  |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | QueryAdvancedId |  | string(400) | Y |  |