---
module: "LABEL"
name_zh: "标签设计"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 62
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# LABEL (标签设计)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 62

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


- **LABEL_DESIGNER**
- **LABEL_DESIGNER_SN**


---


---


> Tables: 2

### LABEL_DESIGNER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | LABEL_DESIGNER_ID | 主键 | GUID | Y | Y |
| 2 | CreateDate | 创建日期 | date | Y |  |
| 3 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 4 | ModifiedDate | 修改日期 | date | Y |  |
| 5 | CreateBy | 创建者 | GUID | Y |  |
| 6 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 7 | ModifiedBy | 修改者 | GUID | Y |  |
| 8 | Attachments | 附件 | string | Y |  |
| 9 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |

### LABEL_DESIGNER_SN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | LABEL_DESIGNER_SN_ID | 主键 | GUID | Y | Y |
| 2 | CreateDate | 创建日期 | date | Y |  |
| 3 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 4 | ModifiedDate | 修改日期 | date | Y |  |
| 5 | CreateBy | 创建者 | GUID | Y |  |
| 6 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 7 | ModifiedBy | 修改者 | GUID | Y |  |
| 8 | Attachments | 附件 | string | Y |  |
| 9 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |