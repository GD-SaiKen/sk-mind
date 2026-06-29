---
module: "FISTATEMENT"
name_zh: "财务报表"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 91
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# FISTATEMENT (财务报表)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 91

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


- **FISTATEMENT_TEMPLATE**
- **FISTATEMENT_TEMPLATE_D**


---


---


> Tables: 2

### FISTATEMENT_TEMPLATE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | FISTATEMENT_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | FISTATEMENT_TEMPLATE_CODE | 报表编号 | string(12) | Y |  |
| 6 | FISTATEMENT_TEMPLATE_NAME | 报表名称 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | FISTATEMENT_NATURE | 报表性质 | number | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 17 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 18 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 19 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 20 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 21 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 22 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 23 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 24 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 25 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 26 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 27 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 28 | UDF041 | 自定义字段12 | date | Y |  |
| 29 | UDF042 | 自定义字段13 | date | Y |  |
| 30 | UDF051 | 自定义字段14 | GUID | Y |  |
| 31 | UDF052 | 自定义字段15 | GUID | Y |  |
| 32 | UDF053 | 自定义字段16 | GUID | Y |  |
| 33 | UDF054 | 自定义字段17 | GUID | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### FISTATEMENT_TEMPLATE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FISTATEMENT_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 3 | PRINT_CODE1 | 列印码1 | number | Y |  |
| 4 | PRINT_CODE2 | 列印码2 | number | Y |  |
| 5 | PRINT_CODE3 | 列印码3 | number | Y |  |
| 6 | SPACE | 空格 | number | Y |  |
| 7 | DATA_SOURCE | 数据来源 | number | Y |  |
| 8 | FISTATEMENT_ITEM_NAME1 | 报表项目名称1 | string(100) | Y |  |
| 9 | FISTATEMENT_ITEM_NAME2 | 报表项目名称2 | string(840) | Y |  |
| 10 | DATA_TYPE | 数据类型 | number | Y |  |
| 11 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 12 | ABS_FLAG | 绝对 | number(0/1) | Y |  |
| 13 | COMPUTE1 | 第1项合计值 | number | Y |  |
| 14 | COMPUTE2 | 第2项合计值 | number | Y |  |
| 15 | COMPUTE3 | 第3项合计值 | number | Y |  |
| 16 | COMPUTE4 | 第4项合计值 | number | Y |  |
| 17 | COMPUTE5 | 第5项合计值 | number | Y |  |
| 18 | COMPUTE6 | 第6项合计值 | number | Y |  |
| 19 | COMPUTE7 | 第7项合计值 | number | Y |  |
| 20 | COMPUTE8 | 第8项合计值 | number | Y |  |
| 21 | COMPUTE9 | 第9项合计值 | number | Y |  |
| 22 | COMPUTE10 | 第10项合计值 | number | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |
| 51 | FISTATEMENT_TEMPLATE_ID |  | GUID | Y |  |