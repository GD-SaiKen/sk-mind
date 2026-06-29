---
module: "ECN"
name_zh: "工程变更"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 12
columns: 612
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# ECN (工程变更)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 12 | Columns: 612

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[BOM (物料清单)|BOM (物料清单)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **ECN_ATTCHMENT (ECN附件)**
- **ECN_AUTO_CONFIG (ECN自动配置模板)**
- **ECN_AUTO_CONFIG_D (ECN自动配置模板单身)**
- **ECN_D (工程变更信息单身)**
- **ECN_DOC (ECN文件变更)**
- **ECN_DRAW (ECN图纸变更)**
- **ECN_ECR (ECN对应ECR)**
- **ECN_FACT_TABLE (工程变更分析表)**
- **ECN_PRODUCT (工程变更产出品信息)**
- **ECN_SD (工程变更信息子单身)**
- **ECN_TASK (ECN部门工作)**


---


---


> Tables: 12

### ECN (工程变更信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ECN_ID | 主键 | GUID | Y | Y |
| 7 | REASON_DESC | 变更原因说明 | string(510) | Y |  |
| 8 | CONTENT | 变更范围 | string(510) | Y |  |
| 9 | REASON_ID | 变更原因 | GUID | Y |  |
| 10 | PERSON_ID | 专案负责人 | GUID | Y |  |
| 11 | URGENT_ID | 紧急等级 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
| 13 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | PrintCount | 打印次数 | number | Y |  |
| 34 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 35 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 36 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 37 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | PostStatus |  | string(400) | Y |  |
| 42 | PostDate |  | date | Y |  |
| 43 | PostBy |  | GUID | Y |  |
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |
| 52 | PMC_STATUS | 任务执行状态 | string(40) | Y |  |

### ECN_ATTCHMENT (ECN附件)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_ATTCHMENT_ID | 主键 | GUID | Y | Y |
| 3 | FILE | 文件档名 | string(40) | Y |  |
| 4 | DESCRIPTION | 文件说明 | string(510) | Y |  |
| 5 | Version | 版本号，不要随意更改 | binary | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 25 | ApproveDate | 修改日期 | date | Y |  |
| 26 | ApproveBy | 修改人 | GUID | Y |  |
| 27 | PostStatus |  | string(400) | Y |  |
| 28 | PostDate |  | date | Y |  |
| 29 | PostBy |  | GUID | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | ECN_ID |  | GUID | Y |  |

### ECN_AUTO_CONFIG (ECN自动配置模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_AUTO_CONFIG_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | CODE_ID | 模板编号 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | FEATURE_GROUP_C | 条件变量 | string(2000) | Y |  |
| 7 | ROOT_ITEM | 最终产品 | string(2000) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | REASON_ID | 变更原因 | GUID | Y |  |
| 10 | ORIGINAL_ROOT_ITEM | 原最终产品 | string(2000) | Y |  |
| 11 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 12 | PLANT_ID | 工厂 | GUID | Y |  |
| 13 | FEATURE_CODE | 条件变量代号 | string(8000) | Y |  |
| 14 | SCRIPTS | 脚本 | string | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | PostStatus |  | string(400) | Y |  |
| 38 | PostDate |  | date | Y |  |
| 39 | PostBy |  | GUID | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | ECN_D_ID |  | GUID | Y |  |
| 47 | ORI_CODE_ID | 原模板编号 | GUID | Y |  |
| 48 | ORI_ITEM_ID | 原品号 | GUID | Y |  |
| 49 | ORI_FEATURE_GROUP_C | 原条件变量 | string(2000) | Y |  |
| 50 | ORI_REASON_ID | 原变更原因 | GUID | Y |  |
| 51 | ORI_PLANT_ID | 原工厂 | GUID | Y |  |
| 52 | ORI_FEATURE_CODE | 原条件变量代号 | string(8000) | Y |  |
| 53 | ORI_SCRIPTS | 原脚本 | string | Y |  |

### ECN_AUTO_CONFIG_D (ECN自动配置模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_AUTO_CONFIG_D_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | FEATURE | 主件变量值 | string(8000) | Y |  |
| 5 | FEATURE_NAME | 主件变量值名称 | string(8000) | Y |  |
| 6 | ITEM_ID | 元件品号 | GUID | Y |  |
| 7 | ITEM_FEATURE | 元件特征码 | string(120) | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 10 | QTY_PER | 用量 | number(16,6) | Y |  |
| 11 | PLAN_RATE | 计划比率 | number(5,4) | Y |  |
| 12 | FEATURE_ARRAY | 属性值数组 | string(8000) | Y |  |
| 13 | DENOMINATOR | 底数 | number | Y |  |
| 14 | FIXED_LOSS_RATE | 固定损耗量 | number(16,6) | Y |  |
| 15 | DYNAMIC_LOSS_RATE | 变动损耗 | number(5,4) | Y |  |
| 16 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 17 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 18 | OPERATION_ID | 工艺 | GUID | Y |  |
| 19 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 20 | EXPRITY_DATE | 失效日期 | date | Y |  |
| 21 | STANDARD_COST_ITEM | 模拟成本计算 | number(0/1) | Y |  |
| 22 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 23 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 24 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | SCRIPTS | 脚本 | string | Y |  |
| 27 | BOM_AUTO_CONFIG_D_ID | 自动配置模板单身主键 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 30 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 31 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 32 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 33 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 34 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 35 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 36 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 37 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 38 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 39 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 40 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 41 | UDF041 | 自定义字段12 | date | Y |  |
| 42 | UDF042 | 自定义字段13 | date | Y |  |
| 43 | UDF051 | 自定义字段14 | GUID | Y |  |
| 44 | UDF052 | 自定义字段15 | GUID | Y |  |
| 45 | UDF053 | 自定义字段16 | GUID | Y |  |
| 46 | UDF054 | 自定义字段17 | GUID | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | PostStatus |  | string(400) | Y |  |
| 51 | PostDate |  | date | Y |  |
| 52 | PostBy |  | GUID | Y |  |
| 53 | CreateDate | 创建日期 | date | Y |  |
| 54 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 55 | ModifiedDate | 修改日期 | date | Y |  |
| 56 | CreateBy | 创建者 | GUID | Y |  |
| 57 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 58 | ModifiedBy | 修改者 | GUID | Y |  |
| 59 | ECN_AUTO_CONFIG_ID |  | GUID | Y |  |
| 60 | REASON_ID | 变更原因 | GUID | Y |  |
| 61 | ORI_FEATURE | 原主件变量值 | string(8000) | Y |  |
| 62 | ORI_FEATURE_NAME | 原主件变量值名称 | string(8000) | Y |  |
| 63 | ORI_ITEM_ID | 原元件品号 | GUID | Y |  |
| 64 | ORI_ITEM_FEATURE | 原元件特征码 | string(120) | Y |  |
| 65 | ORI_ITEM_FEATURE_ID | 原特征码 | GUID | Y |  |
| 66 | ORI_ITEM_SPECIFICATION | 原规格 | string(510) | Y |  |
| 67 | ORI_QTY_PER | 原用量 | number(16,6) | Y |  |
| 68 | ORI_PLAN_RATE | 原计划比率 | number(5,4) | Y |  |
| 69 | ORI_FEATURE_ARRAY | 原属性值数组 | string(8000) | Y |  |
| 70 | ORI_DENOMINATOR | 原底数 | number | Y |  |
| 71 | ORI_FIXED_LOSS_RATE | 原固定损耗量 | number(16,6) | Y |  |
| 72 | ORI_DYNAMIC_LOSS_RATE | 原变动损耗 | number(5,4) | Y |  |
| 73 | ORI_ISSUE_OVERRUN_RATE | 原超领率 | number(5,4) | Y |  |
| 74 | ORI_ISSUE_SHORTAGE_RATE | 原缺领率 | number(5,4) | Y |  |
| 75 | ORI_OPERATION_ID | 原工艺 | GUID | Y |  |
| 76 | ORI_EFFECTIVE_DATE | 原生效日期 | date | Y |  |
| 77 | ORI_EXPRITY_DATE | 原失效日期 | date | Y |  |
| 78 | ORI_STANDARD_COST_ITEM | 原模拟成本计算 | number(0/1) | Y |  |
| 79 | ORI_ITEM_TYPE | 原供料方式 | string(40) | Y |  |
| 80 | ORI_ISSUE_MATERIAL_PERIOD | 原投料间距 | number | Y |  |
| 81 | ORI_COMPONENT_LOCATION | 原插件位置 | string | Y |  |
| 82 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 83 | ORI_SCRIPTS | 原脚本 | string | Y |  |

### ECN_D (工程变更信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_D_ID | 主键 | GUID | Y | Y |
| 3 | VERSION_TIMES | 版次 | string(8) | Y |  |
| 4 | STANDARD_BATCH_QTY | 标准批量 | number(16,6) | Y |  |
| 5 | YIELD_RATE | 产品良率 | number(5,4) | Y |  |
| 6 | SECRET_ITEM | 保密主件 | number(0/1) | Y |  |
| 7 | SECRET_LEVEL | 保密等级 | string(40) | Y |  |
| 8 | REASON_ID | 变更原因 | GUID | Y |  |
| 9 | ORIGINAL_VERSION_TIMES | 原版次 | string(8) | Y |  |
| 10 | ORIGINAL_STANDARD_BATCH_QTY | 原标准批量 | number(16,6) | Y |  |
| 11 | ORIGINAL_YIELD_RATE | 原产品良率 | number(5,4) | Y |  |
| 12 | ORIGINAL_SECRET_ITEM | 原保密主件 | number(0/1) | Y |  |
| 13 | ORIGINAL_SECRET_LEVEL | 原保密等级 | string(40) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 16 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 17 | PARENT_ITEM_ID | 主件品号 | GUID | Y |  |
| 18 | PARENT_ITEM_FEATURE_ID | 主件特征码 | GUID | Y |  |
| 19 | ORIGINAL_PARENT_ITEM_ID | 原主件 | GUID | Y |  |
| 20 | ORIGINAL_ORDER_ECN_ID | 原变更单别信息 | GUID | Y |  |
| 21 | PLANT_ID | 工厂 | GUID | Y |  |
| 22 | REFERENCE_PLANT_ID | 引用工厂 | GUID | Y |  |
| 23 | ORIGINAL_REFERENCE_PLANT_ID | 原引用工厂 | GUID | Y |  |
| 24 | OLD_PLM_DATAKEY | 旧PLM传输批次号 | string(80) | Y |  |
| 25 | NEW_PLM_DATAKEY | 新PLM传输批次号 | string(80) | Y |  |
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
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | PostStatus |  | string(400) | Y |  |
| 49 | PostDate |  | date | Y |  |
| 50 | PostBy |  | GUID | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | ECN_ID |  | GUID | Y |  |

### ECN_DOC (ECN文件变更)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_DOC_ID | 主键 | GUID | Y | Y |
| 3 | DESCRIPTION | 文件说明 | string(510) | Y |  |
| 4 | NEW_FILE | 文件档名 | string(40) | Y |  |
| 5 | NEW_VERION | 新版本 | string(20) | Y |  |
| 6 | OLD_FILE | 原文件档名 | string(40) | Y |  |
| 7 | OLD_VERSION | 原版本 | string(20) | Y |  |
| 8 | Version | 版本号，不要随意更改 | binary | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 28 | ApproveDate | 修改日期 | date | Y |  |
| 29 | ApproveBy | 修改人 | GUID | Y |  |
| 30 | PostStatus |  | string(400) | Y |  |
| 31 | PostDate |  | date | Y |  |
| 32 | PostBy |  | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | ECN_ID |  | GUID | Y |  |

### ECN_DRAW (ECN图纸变更)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_DRAW_ID | 主键 | GUID | Y | Y |
| 3 | DESCRIPTION | 图纸说明 | string(510) | Y |  |
| 4 | NEW_FILE | 新图纸档名 | string(40) | Y |  |
| 5 | NEW_VERSION | 新版本 | string(20) | Y |  |
| 6 | OLD_FILE | 原图纸档名 | string(40) | Y |  |
| 7 | OLD_VERSION | 原版本 | string(20) | Y |  |
| 8 | Version | 版本号，不要随意更改 | binary | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 28 | ApproveDate | 修改日期 | date | Y |  |
| 29 | ApproveBy | 修改人 | GUID | Y |  |
| 30 | PostStatus |  | string(400) | Y |  |
| 31 | PostDate |  | date | Y |  |
| 32 | PostBy |  | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | ECN_ID |  | GUID | Y |  |

### ECN_ECR (ECN对应ECR)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_ECR_ID | 主键 | GUID | Y | Y |
| 3 | ECR_ID | ECR编号 | GUID | Y |  |
| 4 | Version | 版本号，不要随意更改 | binary | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 24 | ApproveDate | 修改日期 | date | Y |  |
| 25 | ApproveBy | 修改人 | GUID | Y |  |
| 26 | PostStatus |  | string(400) | Y |  |
| 27 | PostDate |  | date | Y |  |
| 28 | PostBy |  | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | ECN_ID |  | GUID | Y |  |

### ECN_FACT_TABLE (工程变更分析表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ECN_ID | 工程变更信息 | GUID | Y |  |
| 4 | REASON_CODE | 变更原因编码 | string(8) | Y |  |
| 5 | REASON_NAME | 变更原因名称 | string(80) | Y |  |
| 6 | CHANGE_IMPACT_QTY | 变更影响数量 | number(16,6) | Y |  |
| 7 | ECN_FACT_TABLE_ID | 主键 | GUID | Y | Y |
| 8 | REASON_ID | 变更原因 | GUID | Y |  |
| 9 | DATE | 日期 | date | Y |  |
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
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### ECN_PRODUCT (工程变更产出品信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_PRODUCT_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | SEQ_NUMBER | 序号 | number | Y |  |
| 5 | PRODUCT_RATE | 产出比率 | number(5,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | ORIGINAL_PRODUCT_RATE | 原产出比率 | number(5,4) | Y |  |
| 8 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 9 | SEQ_ID | 序号 | GUID | Y |  |
| 10 | PARENT_ITEM_FEATURE_ID | 主件特征码 | GUID | Y |  |
| 11 | ITEM_ID | 联副产品品号 | GUID | Y |  |
| 12 | ITEM_FEATURE_ID | 联副产品特征码 | GUID | Y |  |
| 13 | ORIGINAL_SEQ_ID | 原序号 | GUID | Y |  |
| 14 | ORIGINAL_ITEM_ID | 原联副产品品号 | GUID | Y |  |
| 15 | ORIGINAL_ITEM_FEATURE_ID | 原联副产品特征码 | GUID | Y |  |
| 16 | PRODUCT_TYPE | 产出类型 | string(40) | Y |  |
| 17 | PRODUCT_QTY | 产出量 | number(16,6) | Y |  |
| 18 | ORIG_PARENT_ITEM_FEATURE_ID | 原主件特征码 | GUID | Y |  |
| 19 | PARENT_ITEM_ID | 主件品号 | GUID | Y |  |
| 20 | ORIGINAL_PRODUCT_TYPE | 原产出类型 | string(40) | Y |  |
| 21 | ORIGINAL_PRODUCT_QTY | 原产出量 | number(16,6) | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | PostStatus |  | string(400) | Y |  |
| 45 | PostDate |  | date | Y |  |
| 46 | PostBy |  | GUID | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | ECN_D_ID |  | GUID | Y |  |

### ECN_SD (工程变更信息子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_SD_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | BOM_SEQ_NUMBER | 序号 | number | Y |  |
| 5 | ITEM_CATEGORY | 类别 | string(40) | Y |  |
| 6 | QTY_PER | 組成用量 | number(16,6) | Y |  |
| 7 | DENOMINATOR | 底数 | number | Y |  |
| 8 | HANDLE | 处置 | string(40) | Y |  |
| 9 | FIXED_LOSS_RATE | 固定损耗量 | number(16,6) | Y |  |
| 10 | DYNAMIC_LOSS_RATE | 变动损耗 | number(5,4) | Y |  |
| 11 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 12 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 13 | ALTERNATIVE_REPLACE | 取替代方式 | string(40) | Y |  |
| 14 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 15 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 16 | STANDARD_COST_ITEM | 模拟成本计算 | number(0/1) | Y |  |
| 17 | REASON | 变更原因 | string(510) | Y |  |
| 18 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 19 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 20 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | ORIGINAL_ITEM_CATEGORY | 原类别 | string(40) | Y |  |
| 23 | ORIGINAL_QTY_PER | 原组成用量 | number(16,6) | Y |  |
| 24 | ORIGINAL_DENOMINATOR | 原底数 | number | Y |  |
| 25 | ORIGINAL_FIXED_LOSS_RATE | 原固定损耗量 | number(16,6) | Y |  |
| 26 | ORIGINAL_DYNAMIC_LOSS_RATE | 原变动损耗 | number(5,4) | Y |  |
| 27 | ORIGINAL_ISSUE_OVERRUN_RATE | 原超领率 | number(5,4) | Y |  |
| 28 | ORIGINAL_ISSUE_SHORTAGE_RATE | 原缺领率 | number(5,4) | Y |  |
| 29 | ORIGINAL_ALTERNATIVE_REPLACE | 原取替代方式 | string(40) | Y |  |
| 30 | ORIGINAL_EFFECTIVE_DATE | 原生效日期 | date | Y |  |
| 31 | ORIGINAL_EXPIRY_DATE | 原失效日期 | date | Y |  |
| 32 | ORIG_STANDARD_COST_ITEM | 原模拟成本计算 | number(0/1) | Y |  |
| 33 | ORIGINAL_ITEM_TYPE | 原供料方式 | string(40) | Y |  |
| 34 | ORIGINAL_ISSUE_MATERIAL_PERIOD | 原投料间距 | number | Y |  |
| 35 | ORIGINAL_COMPONENT_LOCATION | 原插件位置 | string | Y |  |
| 36 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 37 | BOM_SEQ_ID | BOM序号 | GUID | Y |  |
| 38 | SUB_ITEM_FEATURE_ID | 元件特征码 | GUID | Y |  |
| 39 | OPERATION_ID | 工艺 | GUID | Y |  |
| 40 | ORIGINAL_BOM_SEQ_ID | 原BOM序号 | GUID | Y |  |
| 41 | ORIGINAL_SUB_ITEM_FEATURE_ID | 原元件品号特征码 | GUID | Y |  |
| 42 | ORIGINAL_OPERATION_ID | 原工艺 | GUID | Y |  |
| 43 | SOURCE | BOM来源 | string(40) | Y |  |
| 44 | PLM_OUID | PLM _BOMKEY | string(80) | Y |  |
| 45 | SOURCE_TYPE | 来源类型 | string(40) | Y |  |
| 46 | SOURCE_CONFIG_ID | 来源编号 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 49 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 50 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 51 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 52 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 53 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 54 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 55 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 56 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 57 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 58 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 59 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 60 | UDF041 | 自定义字段12 | date | Y |  |
| 61 | UDF042 | 自定义字段13 | date | Y |  |
| 62 | UDF051 | 自定义字段14 | GUID | Y |  |
| 63 | UDF052 | 自定义字段15 | GUID | Y |  |
| 64 | UDF053 | 自定义字段16 | GUID | Y |  |
| 65 | UDF054 | 自定义字段17 | GUID | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |
| 69 | PostStatus |  | string(400) | Y |  |
| 70 | PostDate |  | date | Y |  |
| 71 | PostBy |  | GUID | Y |  |
| 72 | CreateDate | 创建日期 | date | Y |  |
| 73 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 74 | ModifiedDate | 修改日期 | date | Y |  |
| 75 | CreateBy | 创建者 | GUID | Y |  |
| 76 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 77 | ModifiedBy | 修改者 | GUID | Y |  |
| 78 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 79 | SOURCE_ID_ROid |  | GUID | Y |  |
| 80 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 81 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 82 | ECN_D_ID |  | GUID | Y |  |

### ECN_TASK (ECN部门工作)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ECN_TASK_ID | 主键 | GUID | Y | Y |
| 3 | DESCRIPTION | 工作说明 | string(510) | Y |  |
| 4 | START_DATE | 开始日期 | date | Y |  |
| 5 | PLAN_DATE | 预计完成日 | date | Y |  |
| 6 | ACTUAL_DATE | 实际完成日 | date | Y |  |
| 7 | ACTION | 执行结果 | string(510) | Y |  |
| 8 | DEPARTMENT_ID | 部门 | GUID | Y |  |
| 9 | PERSON_ID | 主办人 | GUID | Y |  |
| 10 | TASK_ID | 工作 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 13 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 14 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 15 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 16 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 17 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 18 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 19 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 20 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 21 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 22 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 23 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 24 | UDF041 | 自定义字段12 | date | Y |  |
| 25 | UDF042 | 自定义字段13 | date | Y |  |
| 26 | UDF051 | 自定义字段14 | GUID | Y |  |
| 27 | UDF052 | 自定义字段15 | GUID | Y |  |
| 28 | UDF053 | 自定义字段16 | GUID | Y |  |
| 29 | UDF054 | 自定义字段17 | GUID | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | PostStatus |  | string(400) | Y |  |
| 34 | PostDate |  | date | Y |  |
| 35 | PostBy |  | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | ECN_ID |  | GUID | Y |  |