---
module: "HISTORY"
name_zh: "历史记录"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 169
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# HISTORY (历史记录)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 169

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]
- [[PARA (参数设置)|PARA (参数设置)]]

---

## Tables


- **HISTORY_BOM_D (BOM用量单身历史信息)**
- **HISTORY_FEATURE_PLANT (品号特征码工厂历史信息)**
- **HISTORY_FEATURE_VALUE (品号属性值历史信息)**
- **HISTORY_ITEM_FEATURE (品号特征码历史信息)**


---


---


> Tables: 4

### HISTORY_BOM_D (BOM用量单身历史信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | HISTORY_BOM_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_FEATURE_ID | 主件特征码 | GUID | Y |  |
| 4 | ITEM_CATEGORY | 类别 | string(40) | Y |  |
| 5 | SOURCE_ID | 元件品号 | GUID | Y |  |
| 6 | SUB_ITEM_FEATURE_ID | 元件特征码 | GUID | Y |  |
| 7 | QTY_PER |  | number(16,6) | Y |  |
| 8 | DENOMINATOR | 底数 | number | Y |  |
| 9 | FIXED_LOSS_RATE | 固定损耗量 | number(16,6) | Y |  |
| 10 | DYNAMIC_LOSS_RATE | 变动损耗 | number(5,4) | Y |  |
| 11 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 12 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 13 | OPERATION_ID | 工艺 | GUID | Y |  |
| 14 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 15 | EXPRITY_DATE | 失效日期 | date | Y |  |
| 16 | STANDARD_COST_ITEM | 标准成本计算 | number(0/1) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | ITEM_TYPE | 供料方式 | string(40) | Y |  |
| 19 | ISSUE_MATERIAL_PERIOD | 投料间距 | number | Y |  |
| 20 | COMPONENT_LOCATION | 插件位置 | string | Y |  |
| 21 | SOURCE_TYPE | 来源类别 | string(40) | Y |  |
| 22 | SOURCE_CONFIG_ID | 来源编号 | GUID | Y |  |
| 23 | PARENT_ITEM_ID | 主件品号 | GUID | Y |  |
| 24 | BOM_ID | BOM主键 | GUID | Y |  |
| 25 | BOM_D_ID | 原主键 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
| 33 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 34 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 35 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 36 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 37 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 38 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 39 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 40 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 41 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 42 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 43 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 44 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 45 | UDF041 | 自定义字段12 | date | Y |  |
| 46 | UDF042 | 自定义字段13 | date | Y |  |
| 47 | UDF051 | 自定义字段14 | GUID | Y |  |
| 48 | UDF052 | 自定义字段15 | GUID | Y |  |
| 49 | UDF053 | 自定义字段16 | GUID | Y |  |
| 50 | UDF054 | 自定义字段17 | GUID | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |

### HISTORY_FEATURE_PLANT (品号特征码工厂历史信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | HISTORY_FEATURE_PLANT_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_FEATURE_PLANT_ID | 原主键 | GUID | Y |  |
| 3 | LOW_LEVEL_CODE |  | string(4) | Y |  |
| 4 | CUSTOMER_BOM_CONTROL | 已产生客戶BOM | number(0/1) | Y |  |
| 5 | CONFIG_HASH_CODE | 手动配置识别码 | string(510) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | BOM_STATUS | 客户BOM状态 | string(40) | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码主键 | GUID | Y |  |
| 9 | PLANT_ID | 工厂 | GUID | Y |  |
| 10 | STANDARD_ROUTING_ID | 标准工艺路线 | GUID | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |

### HISTORY_FEATURE_VALUE (品号属性值历史信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | HISTORY_FEATURE_VALUE_ID | 主键 | GUID | Y | Y |
| 2 | FEATURE_CATEGORY | 类别 | string(40) | Y |  |
| 3 | FEATURE_VALUE | 属性值 | string(120) | Y |  |
| 4 | SECTION_NO | 段号 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | FEATURE_CODE_TYPE | 编码类型 | string(40) | Y |  |
| 7 | FEATURE_VALUE_DESC | 属性值描述 | string(120) | Y |  |
| 8 | PARENT_ITEM_ID | 通用品号主键 | GUID | Y |  |
| 9 | ORG_ID_RTK | 组织单元来源码 | string(40) | Y |  |
| 10 | ORG_ID_ROID | 组织单元 | GUID | Y |  |
| 11 | FEATURE_GROUP_ID | 品号群组代码 | GUID | Y |  |
| 12 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 13 | FEATURE_ID | 属性代码 | GUID | Y |  |
| 14 | ITEM_BUSINESS_ID | 品号主键 | GUID | Y |  |
| 15 | ITEM_FEATURE_VALUE_ID | 原主键 | GUID | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
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
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |

### HISTORY_ITEM_FEATURE (品号特征码历史信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | HISTORY_ITEM_FEATURE_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_BUSINESS_ID | 通用品号主键 | GUID | Y |  |
| 3 | ITEM_FEATURE_CODE |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | ITEM_PICTURE | 图片 | string(400) |  |  |
| 6 | FEATURE_ARRAY | 属性值数组 | string(8000) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | ITEM_FEATURE_ID | 原主键 | GUID | Y |  |
| 9 | WEIGHT_PLU | 电子称PLU | string(20) | Y |  |
| 10 | ITEM_FEATURE_PIC | 特征码图片 | string(4000) | Y |  |
| 11 | ITEM_DESC2 | 特征码描述(作废) | string | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |