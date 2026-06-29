---
module: "INTEGRATE"
name_zh: "模具集成"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 11
columns: 464
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# INTEGRATE (模具集成)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 11 | Columns: 464

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


- **INTEGRATE_MOULD**
- **INTEGRATE_MOULD_CON**
- **INTEGRATE_MOULD_D**
- **INTEGRATE_MOULD_FORMUL**
- **INTEGRATE_MOULD_SD**
- **INTEGRATE_MOULD_SDD**
- **INTEGRATE_TEMPLATE (配置集成模板)**
- **INTEGRATE_TEMPLATE_CON (导入模板字段条件)**
- **INTEGRATE_TEMPLATE_D (集成模板单身)**
- **INTEGRATE_TEMPLATE_FORMUL (集成字段公式)**
- **INTEGRATE_TEMPLATE_SD (集成模板子单身)**


---


---


> Tables: 11

### INTEGRATE_MOULD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | INTEGRATE_MOULD_ID | 主键 | GUID | Y | Y |
| 4 | PROGRAM_NO | 作业编号 | string(80) | Y |  |
| 5 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
| 6 | PROGRAM_CHSNAME | 作业简体名称 | string(400) | Y |  |
| 7 | PROGRAM_CHTNAME | 作业繁体名称 | string(400) | Y |  |
| 8 | TEMPLATE_FILE_NAME | 导入作业名称 | string(400) | Y |  |
| 9 | TYPEKEY | TYPEKEY编号 | string(80) | Y |  |
| 10 | INTEGRATION_TYPE | 集成产品别 | number | Y |  |
| 11 | IMPORT_EXPORT | 导入导出类型 | string(40) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PROGRAM_TYPE | 作业类型 | number | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 22 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 23 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 24 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 25 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 26 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 27 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 28 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 29 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 30 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 31 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 32 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 33 | UDF041 | 自定义字段12 | date | Y |  |
| 34 | UDF042 | 自定义字段13 | date | Y |  |
| 35 | UDF051 | 自定义字段14 | GUID | Y |  |
| 36 | UDF052 | 自定义字段15 | GUID | Y |  |
| 37 | UDF053 | 自定义字段16 | GUID | Y |  |
| 38 | UDF054 | 自定义字段17 | GUID | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | PROGRAM_ENUNAME | 作业英文名称 | string(400) | Y |  |

### INTEGRATE_MOULD_CON

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INTEGRATE_MOULD_CON_ID | 主键 | GUID | Y | Y |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | SOURCE_TABLE | 来源表 | string(400) | Y |  |
| 5 | OUT_CON | 导出查找条件 | string(1200) | Y |  |
| 6 | IN_CON | 表达式 | string(1200) | Y |  |
| 7 | CON_CODE | 带值编号 | string(80) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | INTEGRATE_MOULD_ID |  | GUID | Y |  |

### INTEGRATE_MOULD_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PATH | 路径 | string(2000) | Y |  |
| 2 | SequenceNumber |  | number | Y |  |
| 3 | INTEGRATE_MOULD_D_ID | 主键 | GUID | Y | Y |
| 4 | TABLE_SNAME | 实体代号 | string(400) | Y |  |
| 5 | TABLE_DISNAME1 | 实体名称 | string(400) | Y |  |
| 6 | TABLE_DISNAME2 | 实体繁体名称 | string(400) | Y |  |
| 7 | TABLE_DISNAME3 | 实体英文名称 | string(400) | Y |  |
| 8 | SHEET_NAME | 映射表名 | string(400) | Y |  |
| 9 | FATHER_TABLE_NAME | 主表 | string(400) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | INTEGRATE_MOULD_ID |  | GUID | Y |  |

### INTEGRATE_MOULD_FORMUL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INTEGRATE_MOULD_FORMUL_ID | 主键 | GUID | Y | Y |
| 3 | TARGET_FIELD | 目标字段 | string(400) | Y |  |
| 4 | PATH | 路径 | string(2400) | Y |  |
| 5 | EXPRESSION | 表达式 | string(2400) | Y |  |
| 6 | OUT_VARIABLE | 输出变量名 | string(1200) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | INTEGRATE_MOULD_ID |  | GUID | Y |  |

### INTEGRATE_MOULD_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COLUMN_NAME | 字段名称 | string(200) | Y |  |
| 3 | COLUMN_TYPE | 字段类型：1.实体字段；2.带值字段；3.计算字段 | string(2) | Y |  |
| 4 | EXPRESSION | 公式表达式 | string(2000) | Y |  |
| 5 | REFERENCE_COLUMN | 带值引用字段 | string(200) | Y |  |
| 6 | REFERENCE_SOURCE | 带值来源字段 | string(200) | Y |  |
| 7 | SOURCE_TYPE | 字段集成类型 | string(40) | Y |  |
| 8 | DISPLAY_CHTNAME | 字段繁体名称 | string(400) | Y |  |
| 9 | DISPLAY_ENGNAME | 字段英文名称 | string(400) | Y |  |
| 10 | DISPLAY_NAME | 字段简体名称 | string(400) | Y |  |
| 11 | FIELD_ID | 导入模板字段编号 | string(400) | Y |  |
| 12 | FIELD_NAME | 字段简体名称 | string(400) | Y |  |
| 13 | FIELD_NAME1 | 字段繁体名称 | string(400) | Y |  |
| 14 | FIELD_NAME2 | 字段英文名称 | string(400) | Y |  |
| 15 | FIELD_NAME3 | 字段名 | string(400) | Y |  |
| 16 | DEFAULT_VALUE | 默认值 | string(400) | Y |  |
| 17 | FIELD_LENGTH | 字段长度 | number | Y |  |
| 18 | FIELD_ACCURACY | 字段精度 | number | Y |  |
| 19 | FIELD_PROPERTY | 字段数据类型 | string(100) | Y |  |
| 20 | HIDE_FLAG | 隐藏 | number(0/1) | Y |  |
| 21 | OUT_PICKLISTTYPE | PICKLIST导出类型 | number | Y |  |
| 22 | MSOURCE_WHERE_FIELD | 多来源赋值标识 | number(0/1) | Y |  |
| 23 | NO_EMPTY | 不可空白 | string(40) | Y |  |
| 24 | INTEGRATE_MOULD_SD_ID | 主键 | GUID | Y | Y |
| 25 | SOURCE_FIELD | 带值字段 | string(400) | Y |  |
| 26 | IN_CON_CODE | 带值编号 | string(80) | Y |  |
| 27 | SERVICE_KEY_FLAG | 业务主键 | number(0/1) | Y |  |
| 28 | ENTITY_FLAG | 实体字段 | number(0/1) | Y |  |
| 29 | REFERENCE_FLAG | reference字段标识 | number(0/1) | Y |  |
| 30 | M_CONTROL | 字段更新控制 | number(0/1) | Y |  |
| 31 | UPDATE_STRATEGY | 字段更新逻辑 | string(40) | Y |  |
| 32 | PICKLISTTYPE | PICKLIST类型 | string(80) | Y |  |
| 33 | REMARK | 备注 | string(510) | Y |  |
| 34 | IMPORT_TEMPLATE_FLAG | 发布 | number(0/1) | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 61 | ApproveDate | 修改日期 | date | Y |  |
| 62 | ApproveBy | 修改人 | GUID | Y |  |
| 63 | INTEGRATE_MOULD_D_ID |  | GUID | Y |  |
| 64 | MAPPING_FIELD | 映射字段 | string(510) | Y |  |

### INTEGRATE_MOULD_SDD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | REFERENCE_SOURCE | 带值来源字段 | string(200) | Y |  |
| 3 | INTEGRATE_MOULD_SDD_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 12 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 13 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 14 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 15 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 16 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 17 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 18 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 19 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 20 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 21 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 22 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 23 | UDF041 | 自定义字段12 | date | Y |  |
| 24 | UDF042 | 自定义字段13 | date | Y |  |
| 25 | UDF051 | 自定义字段14 | GUID | Y |  |
| 26 | UDF052 | 自定义字段15 | GUID | Y |  |
| 27 | UDF053 | 自定义字段16 | GUID | Y |  |
| 28 | UDF054 | 自定义字段17 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | INTEGRATE_MOULD_SD_ID |  | GUID | Y |  |

### INTEGRATE_TEMPLATE (配置集成模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | INTEGRATE_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 4 | PROGRAM_NO | 作业编号 | string(400) | Y |  |
| 5 | TEMPLATE_FILE_NAME | 导入作业名 | string(400) | Y |  |
| 6 | PROGRAM_TYPE | 作业类型 | number | Y |  |
| 7 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
| 8 | REMARK | 备注 | string(400) | Y |  |
| 9 | PRODUCT | 集成产品别 | number | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### INTEGRATE_TEMPLATE_CON (导入模板字段条件)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INTEGRATE_TEMPLATE_CON_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_TABLE | 来源表 | string(400) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | OUT_CON | 导出查找条件 | string(1200) | Y |  |
| 6 | IN_CON | 表达式 | string(1200) | Y |  |
| 7 | CON_CODE | 带值编号 | string(80) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | INTEGRATE_TEMPLATE_ID |  | GUID | Y |  |

### INTEGRATE_TEMPLATE_D (集成模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TABLE_DISNAME1 | 实体名称 | string(400) | Y |  |
| 3 | TABLE_DISNAME2 | 繁体名称 | string(400) | Y |  |
| 4 | TABLE_DISNAME3 | 英文名称 | string(400) | Y |  |
| 5 | SHEET_NAME | 映射表名 | string(400) | Y |  |
| 6 | TABLE_SNAME | 实体代号 | string(400) | Y |  |
| 7 | FATHER_TABLE_NAME | 主表 | string(400) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | INTEGRATE_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | INTEGRATE_TEMPLATE_ID |  | GUID | Y |  |

### INTEGRATE_TEMPLATE_FORMUL (集成字段公式)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INTEGRATE_TEMPLATE_FORMUL_ID | 主键 | GUID | Y | Y |
| 3 | TARGET_FIELD | 目标字段 | string(400) | Y |  |
| 4 | PATH | 路径 | string(2400) | Y |  |
| 5 | EXPRESSION | 表达式 | string(2400) | Y |  |
| 6 | OUT_VARIABLE | 输出变量名 | string(1200) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | INTEGRATE_TEMPLATE_ID |  | GUID | Y |  |

### INTEGRATE_TEMPLATE_SD (集成模板子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INTEGRATE_TEMPLATE_SD_ID | 主键 | GUID | Y | Y |
| 3 | FIELD_NAME | 字段名称 | string(400) | Y |  |
| 4 | FIELD_NAME1 | 繁体名称 | string(400) | Y |  |
| 5 | FIELD_NAME2 | 英文名称 | string(400) | Y |  |
| 6 | FIELD_NAME3 | 字段名 | string(400) | Y |  |
| 7 | IMPORT_TEMPLATE_FLAG | 发布 | number(0/1) | Y |  |
| 8 | DEFAULT_VALUE | 默认值 | string(400) | Y |  |
| 9 | HIDE_FLAG | 隐藏 | number(0/1) | Y |  |
| 10 | SERVICE_KEY_FLAG | 业务主键 | number(0/1) | Y |  |
| 11 | FIELD_PROPERTY | 字段类型 | string(100) | Y |  |
| 12 | FIELD_LENGTH | 字段长度 | number | Y |  |
| 13 | FIELD_ACCURACY | 精度 | number | Y |  |
| 14 | REFERENCE_FLAG | reference字段标识 | number(0/1) | Y |  |
| 15 | SOURCE_TABLE | 来源表 | string(400) | Y |  |
| 16 | SOURCE_FIELD | 带值字段 | string(400) | Y |  |
| 17 | CONDITION_FIELD | 条件字段 | string(400) | Y |  |
| 18 | FORMULA_NO | 公式序号 | number | Y |  |
| 19 | FORMULA | 公式 | string(400) | Y |  |
| 20 | ENTITY_FLAG | 实体字段 | number(0/1) | Y |  |
| 21 | IN_CON_CODE | 带值编号 | string(80) | Y |  |
| 22 | OUT_CON_CODE | 导出查询编号 | string(80) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | SOURCE_TYPE | 集成类型 | string(40) | Y |  |
| 25 | NO_EMPTY | 不可空白 | string(40) | Y |  |
| 26 | M_CONTROL | 字段更新控制 | number(0/1) | Y |  |
| 27 | UPDATE_STRATEGY | 字段更新逻辑 | string(40) | Y |  |
| 28 | PICKLISTTYPE | PICKLIST类型 | string(80) | Y |  |
| 29 | FIELD_ID | 字段编号 | string(160) | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 37 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 38 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 39 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 40 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 41 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 42 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 43 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 44 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 45 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 46 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 47 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 48 | UDF041 | 自定义字段12 | date | Y |  |
| 49 | UDF042 | 自定义字段13 | date | Y |  |
| 50 | UDF051 | 自定义字段14 | GUID | Y |  |
| 51 | UDF052 | 自定义字段15 | GUID | Y |  |
| 52 | UDF053 | 自定义字段16 | GUID | Y |  |
| 53 | UDF054 | 自定义字段17 | GUID | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | INTEGRATE_TEMPLATE_D_ID |  | GUID | Y |  |
| 59 | MAPPING_FIELD | 映射字段 | string(510) | Y |  |