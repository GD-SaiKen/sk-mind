---
module: "BOM"
name_zh: "物料清单"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 11
columns: 481
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52

---

# BOM (物料清单)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 11 | Columns: 481

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[FORECAST (需求预测)|FORECAST (需求预测)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **BOM_AUTO_CONFIG (BOM自动配置模板)**
- **BOM_AUTO_CONFIG_D (BOM自动配置模板单身)**
- **BOM_AUTO_CONFIG_D_V**
- **BOM_D (BOM产出品信息档)**
- **BOM_MANUAL_CONFIG (BOM手动配置)**
- **BOM_MANUAL_CONFIG_D (BOM手动配置单身)**
- **BOM_PRODUCT (BOM产出品信息)**
- **BOM_RULE (产品配置约束)**
- **BOM_RULE_D (产品配置约束单身)**
- **BOM_SD (BOM分量损耗)**


---


---


> Tables: 11

### BOM (BOM用量信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BOM_ID | 主键 | GUID | Y | Y |
| 4 | STANDARD_BATCH_QTY | 标准批量 | number(16,6) | Y |  |
| 5 | YIELD_RATE | 产品良率 | number(5,4) | Y |  |
| 6 | VERSION_TIMES | 版次 | string(8) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | SECRET_ITEM | 保密主件 | number(0/1) | Y |  |
| 9 | SECRET_LEVEL | 保密等级 | string(40) | Y |  |
| 10 | E_CODE | 工程码 | string(40) | Y |  |
| 11 | BOM_CHANGE_D_ID | 变更单信息 | GUID | Y |  |
| 12 | ITEM_ID | 主件品号信息 | GUID | Y |  |
| 13 | REFERENCE_PLANT_ID | 引用工厂 | GUID | Y |  |
| 14 | REMARK2 | 备注 | string(510) | Y |  |
| 15 | SOURCE | BOM来源 | string(40) | Y |  |
| 16 | PLM_DATAKEY | PLM传输批次号 | string(80) | Y |  |
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
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |

### BOM_AUTO_CONFIG (BOM自动配置模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BOM_AUTO_CONFIG_ID | 主键 | GUID | Y | Y |
| 4 | CODE | 模板编号 | string(80) | Y |  |
| 5 | NAME | 模板名称 | string(120) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | FEATURE_GROUP_D_ID | 条件变量 | string(8000) | Y |  |
| 8 | VERSION_TIMES | 版次 | string(8) | Y |  |
| 9 | FEATURE_CODE | 条件变量代号 | string(8000) | Y |  |
| 10 | SCRIPTS | 脚本 | string | Y |  |
| 11 | ROOT_ITEM | 最终产品 | string | Y |  |
| 12 | ITEM_ID | 品号 | GUID | Y |  |
| 13 | ROOT_ITEM_CODE | 最终产品 | string(2000) | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |

### BOM_AUTO_CONFIG_D (BOM自动配置模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BOM_AUTO_CONFIG_D_ID | 主键 | GUID | Y | Y |
| 2 | FEATURE | 模板特征码 | string(8000) | Y |  |
| 3 | QTY | 用量 | number(16,6) | Y |  |
| 4 | ITEM_FEATURE | 品号特征码 | string(120) | Y |  |
| 5 | FEATURE_ARRAY | 属性值数组 | string(8000) | Y |  |
| 6 | FEATURE_NAME | 主件属性值名称 | string(8000) | Y |  |
| 7 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 8 | PLAN_RATE | 计划比率 | number(5,4) | Y |  |
| 9 | DENOMINATOR | 底数 | number | Y |  |
| 10 | FIXED_LOSS_RATE | 固定损耗量 | number(16,6) | Y |  |
| 11 | DYNAMIC_LOSS_RATE | 变动损耗 | number(5,4) | Y |  |
| 12 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 13 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 14 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 15 | EXPRITY_DATE | 失效日期 | date | Y |  |
| 16 | STANDARD_COST_ITEM | 模拟成本计算 | number(0/1) | Y |  |
| 17 | ITEM_TYPE | 材料类型 | string(40) | Y |  |
| 18 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 19 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | SCRIPTS | 脚本 | string | Y |  |
| 22 | ALTERNATIVE_REPLACE | 取替代方式 | string(40) | Y |  |
| 23 | ITEM_ID | 元件品号 | GUID | Y |  |
| 24 | OPERATION_ID | 工艺 | GUID | Y |  |
| 25 | SCRIPTS_DES | 公式 | string | Y |  |
| 26 | PARAMETERS | 参数 | string(8000) | Y |  |
| 27 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | BOM_AUTO_CONFIG_ID |  | GUID | Y |  |

### BOM_AUTO_CONFIG_D_V

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BOM_AUTO_CONFIG_D_V_ID | 主键 | GUID | Y | Y |
| 3 | FEATURE | 主件变量值 | string(8000) | Y |  |
| 4 | FEATURE_NAME | 主件变量值名称 | string(8000) | Y |  |
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
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | BOM_AUTO_CONFIG_ID |  | GUID | Y |  |

### BOM_D (BOM产出品信息档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BOM_D_ID | 主键 | GUID | Y | Y |
| 3 | QTY_PER | 組成用量 | number(16,6) | Y |  |
| 4 | DENOMINATOR | 底数 | number | Y |  |
| 5 | FIXED_LOSS_RATE | 固定损耗量 | number(16,6) | Y |  |
| 6 | DYNAMIC_LOSS_RATE | 变动损耗 | number(5,4) | Y |  |
| 7 | ALTERNATIVE_REPLACE | 取替代方式 | string(40) | Y |  |
| 8 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 9 | EXPRITY_DATE | 失效日期 | date | Y |  |
| 10 | STANDARD_COST_ITEM | 模拟成本计算 | number(0/1) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ITEM_TYPE | 材料类型 | string(40) | Y |  |
| 13 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 14 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 15 | SOURCE_TYPE | 来源 | string(40) | Y |  |
| 16 | ITEM_CATEGORY | 元件类别 | string(40) | Y |  |
| 17 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 18 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 19 | SOURCE_CONFIG_ID | 公式编号 | GUID | Y |  |
| 20 | PARENT_ITEM_ID | 主件品号 | GUID | Y |  |
| 21 | ITEM_FEATURE_ID | 主件品号/特征码 | GUID | Y |  |
| 22 | SUB_ITEM_FEATURE_ID | 元件品号/特征码 | GUID | Y |  |
| 23 | OPERATION_ID | 工艺信息 | GUID | Y |  |
| 24 | SOURCE | BOM来源 | string(40) | Y |  |
| 25 | PLM_OUID | PLM _BOMKEY | string(80) | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | BOM_ID |  | GUID | Y |  |
| 57 | SCRAP_BY_QUANTITY | 分量损耗 | number(0/1) | Y |  |

### BOM_MANUAL_CONFIG (BOM手动配置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BOM_MANUAL_CONFIG_ID | 主键 | GUID | Y | Y |
| 4 | CODE | 配置编号 | string(40) | Y |  |
| 5 | NAME | 配置名称 | string(120) | Y |  |
| 6 | SUBITEMS_RELATION | 子件关系 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | VERSION_TIMES | 版次 | string(8) | Y |  |
| 9 | CONFIGURE_QTY_MODIFIED | 可更改配置件用量 | number(0/1) | Y |  |
| 10 | CONFIGURE_ITEM_MODIFIED | 可增加配置料件 | number(0/1) | Y |  |
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
| 29 | Attachments | 附件 | string | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### BOM_MANUAL_CONFIG_D (BOM手动配置单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BOM_MANUAL_CONFIG_D_ID | 主键 | GUID | Y | Y |
| 2 | QTY_PER | 組成用量 | number(16,6) | Y |  |
| 3 | DEFAULT | 默认选择 | number(0/1) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | DENOMINATOR | 底数 | number | Y |  |
| 6 | FIXED_LOSS_RATE | 固定损耗量 | number(16,6) | Y |  |
| 7 | DYNAMIC_LOSS_RATE | 变动损耗 | number(5,4) | Y |  |
| 8 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 9 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 10 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 11 | EXPRITY_DATE | 失效日期 | date | Y |  |
| 12 | STANDARD_COST_ITEM | 模拟成本计算 | number(0/1) | Y |  |
| 13 | ITEM_TYPE | 材料类型 | string(40) | Y |  |
| 14 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 15 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 16 | ALTERNATIVE_REPLACE | 取替代方式 | string(40) | Y |  |
| 17 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 18 | OPERATION_ID | 工艺 | GUID | Y |  |
| 19 | ITEM_CATEGORY | 类别 | string(40) | Y |  |
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
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | BOM_MANUAL_CONFIG_ID |  | GUID | Y |  |

### BOM_PRODUCT (BOM产出品信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BOM_PRODUCT_ID | 主键 | GUID | Y | Y |
| 3 | PRODUCT_RATE | 产量 | number(5,4) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | PARENT_ITEM_ID | 主件品号 | GUID | Y |  |
| 6 | PARENT_ITEM_FEATURE_ID | 主产品特征码 | GUID | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | ITEM_ID | 品号 | GUID | Y |  |
| 9 | PRODUCT_TYPE | 类型 | string(40) | Y |  |
| 10 | COST_CONV_COEFFICIENT | 标准数量换算系数 | number(16,6) | Y |  |
| 11 | PRODUCT_QTY | 产出量 | number(16,6) | Y |  |
| 12 | REMARK2 | 备注 | string(510) | Y |  |
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
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | BOM_ID |  | GUID | Y |  |

### BOM_RULE (产品配置约束)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BOM_RULE_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 主件品号 | GUID | Y |  |
| 5 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 24 | Attachments | 附件 | string | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | Owner_Org_RTK |  | string(400) | Y |  |
| 36 | Owner_Org_ROid |  | GUID | Y |  |

### BOM_RULE_D (产品配置约束单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | BOM_RULE_D_ID | 主键 | GUID | Y | Y |
| 2 | CODE | 约束编号 | string(80) | Y |  |
| 3 | NAME | 约束名称 | string(120) | Y |  |
| 4 | TYPE | 类型 | string(40) | Y |  |
| 5 | EXCEPT_ITEM | 排外品号 | string(2000) | Y |  |
| 6 | FORMULA | 公式 | string | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | FORMULA_VALUE | 公式内含 | string | Y |  |
| 9 | EXCEPT_ITEM_ID | 排外品号主键 | string(2000) | Y |  |
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
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | BOM_RULE_ID |  | GUID | Y |  |

### BOM_SD (BOM分量损耗)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BOM_SD_ID | 主键 | GUID | Y | Y |
| 3 | QUANTITY | 数量 | number(16,6) | Y |  |
| 4 | SCRAP_RATIO | 损耗率 | number(5,4) | Y |  |
| 5 | SCRAP_QUANTITY | 固定损耗量 | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | BOM_D_ID |  | GUID | Y |  |