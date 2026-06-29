---
module: "INSPECTION"
name_zh: "检验管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 7
columns: 305
category: quality
tags: ["ERP", "E10", "quality"]
created: 2026-06-25 10:52

---

# INSPECTION (检验管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 7 | Columns: 305

## Related Modules

- [[ACCEPTANCE (验收管理)|ACCEPTANCE (验收管理)]]
- [[DEFECTIVE (不良品)|DEFECTIVE (不良品)]]
- [[INSP (检验单据)|INSP (检验单据)]]

---

## Tables


- **INSPECTION_ITEM (检验项目)**
- **INSPECTION_ITEM_TYPE (检验项目类别)**
- **INSPECTION_JOB (维护/巡检项目定义實體)**
- **INSPECTION_JOB_D (巡检维护项目定义单身實體)**
- **INSPECTION_PLAN (质检方案)**
- **INSPECTION_PLAN_D (质检方案计数单身)**
- **INSPECTION_PLAN_D1 (质检方案计量单身)**


---


---


> Tables: 7

### INSPECTION_ITEM (检验项目)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | INSPECTION_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | INSPECTION_ITEM_CODE | 检验项目编号 | string(40) | Y |  |
| 5 | INSPECTION_ITEM_NAME | 检验项目名称 | string(40) | Y |  |
| 6 | INSPECTION_TYPE | 类型 | string(40) | Y |  |
| 7 | INSPECTION_ITEM_TYPE_ID | 检验项目类别 | GUID | Y |  |
| 8 | DEFAULT_DEFECT_CLASS | 默认缺点等级 | string(40) | Y |  |
| 9 | DEFAULT_IL | 默认检验水平 | string(40) | Y |  |
| 10 | DEFAULT_DL | 默认判别水平 | string(40) | Y |  |
| 11 | ITEM_DESCRIPTION | 检验项目说明 | string(510) | Y |  |
| 12 | REMARK |  | string(510) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 21 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 22 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 23 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 24 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 25 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 26 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 27 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 28 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 29 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 30 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 31 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 32 | UDF041 | 自定义字段12 | date | Y |  |
| 33 | UDF042 | 自定义字段13 | date | Y |  |
| 34 | UDF051 | 自定义字段14 | GUID | Y |  |
| 35 | UDF052 | 自定义字段15 | GUID | Y |  |
| 36 | UDF053 | 自定义字段16 | GUID | Y |  |
| 37 | UDF054 | 自定义字段17 | GUID | Y |  |
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### INSPECTION_ITEM_TYPE (检验项目类别)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | INSPECTION_ITEM_TYPE_ID | 主键 | GUID | Y | Y |
| 4 | INSPECTION_ITEM_TYPE_CODE | 检验项目类别编号 | string(40) | Y |  |
| 5 | INSPECTION_ITEM_TYPE_NAME | 检验项目类别名称 | string(40) | Y |  |
| 6 | REMARK |  | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
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
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### INSPECTION_JOB (维护/巡检项目定义實體)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | INSPECTION_JOB_ID | 主键 | GUID | Y | Y |
| 4 | INSPECTION_JOB_CODE | 项目编号 | string(80) | Y |  |
| 5 | INSPECTION_JOB_NAME | 项目名称 | string(510) | Y |  |
| 6 | RESULT_UNIT_ID | 维护结果单位 | GUID | Y |  |
| 7 | RESULT_TYPE | 结果类型 | string(40) | Y |  |
| 8 | TOP_LIMIT | 默认数值上限 | number(16,6) | Y |  |
| 9 | LOWER_LIMIT | 默认数值下限 | number(16,6) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | ISMAINTENANCE_JOB | 维护项目 | number(0/1) | Y |  |
| 12 | ISINSPECTION_JOB | 巡检项目 | number(0/1) | Y |  |
| 13 | REPAIR_JOB | 维修项目 | number(0/1) | Y |  |
| 14 | IS_SUPPLIER | 可否委外 | number(0/1) | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | ITEM_NAME | 品名 | string(120) | Y |  |
| 17 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 18 | DEFAULT_SUPPLIER_ID | 默认供应商 | GUID | Y |  |
| 19 | KNOWLEDGE_BASE_ID | 知识库分类 | GUID | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
| 27 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 28 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 29 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 30 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 31 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 32 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 33 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 34 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 35 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 36 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 37 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 38 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 39 | UDF041 | 自定义字段12 | date | Y |  |
| 40 | UDF042 | 自定义字段13 | date | Y |  |
| 41 | UDF051 | 自定义字段14 | GUID | Y |  |
| 42 | UDF052 | 自定义字段15 | GUID | Y |  |
| 43 | UDF053 | 自定义字段16 | GUID | Y |  |
| 44 | UDF054 | 自定义字段17 | GUID | Y |  |
| 45 | Attachments | 附件 | string | Y |  |
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### INSPECTION_JOB_D (巡检维护项目定义单身實體)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | RESULT | 项目维护结果 | string(510) | Y |  |
| 3 | IS_DEFAULT | 默认 | number(0/1) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | INSPECTION_JOB_D_ID | 主键 | GUID | Y | Y |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
| 13 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 14 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 15 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 16 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 17 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 18 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 19 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 20 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 21 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 22 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 23 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 24 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 25 | UDF041 | 自定义字段12 | date | Y |  |
| 26 | UDF042 | 自定义字段13 | date | Y |  |
| 27 | UDF051 | 自定义字段14 | GUID | Y |  |
| 28 | UDF052 | 自定义字段15 | GUID | Y |  |
| 29 | UDF053 | 自定义字段16 | GUID | Y |  |
| 30 | UDF054 | 自定义字段17 | GUID | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | INSPECTION_JOB_ID |  | GUID | Y |  |

### INSPECTION_PLAN (质检方案)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | INSPECTION_PLAN_ID | 主键 | GUID | Y | Y |
| 4 | INSPECTION_PLAN_TYPE | 质检方案类别 | string(40) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 品号特征码 | GUID | Y |  |
| 7 | CR_AQL | AQL：CR（严重） | string(40) | Y |  |
| 8 | MA_AQL | AQL：MA（主要） | string(40) | Y |  |
| 9 | MI_AQL | AQL：MI（次要） | string(40) | Y |  |
| 10 | CR_LQ | LQ：CR（严重） | string(40) | Y |  |
| 11 | MA_LQ | LQ：MA（主要） | string(40) | Y |  |
| 12 | MI_LQ | LQ：MI（次要） | string(40) | Y |  |
| 13 | CR_RQL | RQL：CR（严重） | string(40) | Y |  |
| 14 | MA_RQL | RQL：MA（主要） | string(40) | Y |  |
| 15 | MI_RQL | RQL：MI（次要） | string(40) | Y |  |
| 16 | INSPECTION_METHOD | 抽样方式 | string(40) | Y |  |
| 17 | AI_STANDARD | 计数抽样检验标准 | string(40) | Y |  |
| 18 | VI_STANDARD | 计量抽样检验标准 | string(40) | Y |  |
| 19 | MODE | 模式 | string(40) | Y |  |
| 20 | QC_CATEGORY_ID | 品管类别编号 | GUID | Y |  |
| 21 | CUSTOM_STANDARD_ID | 自定义抽样标准 | GUID | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | INSPECTION_TIMES | 抽样次数 | string(40) | Y |  |
| 24 | OPERATION_ID | 工艺 | GUID | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Attachments | 附件 | string | Y |  |
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | Owner_Org_RTK |  | string(400) | Y |  |
| 56 | Owner_Org_ROid |  | GUID | Y |  |

### INSPECTION_PLAN_D (质检方案计数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | INSPECTION_PLAN_D_ID |  | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 4 | IL | 检验水平 | string(40) | Y |  |
| 5 | DL | 判别水平 | string(40) | Y |  |
| 6 | QS_DESCRIPTION | 检验标准说明 | string(510) | Y |  |
| 7 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 8 | REMARK |  | string(510) | Y |  |
| 9 | INSPECTION_ITEM_ID | 检验项目编号 | GUID | Y |  |
| 10 | OPERATION_ID | 后道工艺 | GUID | Y |  |
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
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | INSPECTION_PLAN_ID |  | GUID | Y |  |

### INSPECTION_PLAN_D1 (质检方案计量单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | INSPECTION_PLAN_D1_ID |  | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | QS_DESCRIPTION | 检验标准说明 | string(510) | Y |  |
| 4 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 5 | IL | 检验水平 | string(40) | Y |  |
| 6 | QUALITY_INDEX_TYPE | 质量指标类型 | string(40) | Y |  |
| 7 | INSPECTION_CASE | 检验方式 | string(40) | Y |  |
| 8 | VI_UPPER_DES_VALUE | U | number(16,6) | Y |  |
| 9 | VI_LOWER_DES_VALUE | LQ | number(16,6) | Y |  |
| 10 | U0L | μ0L | number(16,6) | Y |  |
| 11 | U0U | μ0U | number(16,6) | Y |  |
| 12 | UIL | μIL | number(16,6) | Y |  |
| 13 | UIU | μIU | number(16,6) | Y |  |
| 14 | P0 | P0 | number(16,6) | Y |  |
| 15 | P1 | P1 | number(16,6) | Y |  |
| 16 | SGM | δ | number(16,6) | Y |  |
| 17 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 18 | REMARK |  | string(510) | Y |  |
| 19 | INSPECTION_ITEM_ID | 检验项目编号 | GUID | Y |  |
| 20 | OPERATION_ID | 后道工艺 | GUID | Y |  |
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
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | INSPECTION_PLAN_ID |  | GUID | Y |  |