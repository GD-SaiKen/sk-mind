---
module: "ITEM"
name_zh: "物料商品"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 51
columns: 2609
category: inventory
semantic_object: "Material/物料"
original_tables: 53
filtered_out: 1
tags: ["ERP", "E10", "inventory", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# ITEM (物料商品) - Material/物料

> [!info] Phase 1 Core Module
> Semantic Object: Material/物料
> Kept: 51 tables | Filtered out: 1 (templates/logs/backups)
> Missing CN filled: 0

## Related Modules

- [[../modules/INV (库存成本).md|INV (库存成本)]]
- [[../modules/SN (序列号).md|SN (序列号)]]
- [[../modules/TRANSFER (调拨管理).md|TRANSFER (调拨管理)]]
- [[../modules/BORROW (借入借出).md|BORROW (借入借出)]]

---

## Tables

- **ITEM_BARCODE (品号条码信息)**
- **ITEM_BARCODE_D (品号条码信息单身)**
- **ITEM_BC_REG (品号条码注册信息)**
- **ITEM_BENCHMARK_COST (维护品号基准成本)**
- **ITEM_BENCHMARK_COST_D (品号基准成本单身)**
- **ITEM_CERTIFICATION (品号认可信息)**
- **ITEM_CERTIFICATION_CHANGE (品号认可变更信息)**
- **ITEM_CERTIFICATION_D (品号认可信息单身)**
- **ITEM_COST (品号成本)**
- **ITEM_COST_D (品号成本单身)**
- **ITEM_FEATURE (通用品号特征码信息)**
- **ITEM_FEATURE_PLANT (品号特征工厂信息)**
- **ITEM_FEATURE_VALUE (通用品号属性值信息)**
- **ITEM_FINANCIAL (品号财务信息)**
- **ITEM_GROUP (品号群组通用信息)**
- **ITEM_GROUP_FEATURE_VALUE (品号群组属性值信息)**
- **ITEM_GROUP_FINANCIAL (品号群组财务信息)**
- **ITEM_GROUP_PLANT (品号群组工厂信息)**
- **ITEM_GROUP_PLANT_CSTAF (品号群组成本分配因子)**
- **ITEM_GROUP_PURCHASE (品号群组采购信息)**
- **ITEM_GROUP_SALES (品号群组销售信息)**
- **ITEM_GROUP_SUPPLIER (品号群组供应商信息)**
- **ITEM_LOT (品号批号信息)**
- **ITEM_MAPPING (品号映射信息)**
- **ITEM_MAPPING_D (品号映射信息单身)**
- **ITEM_OPERATION_CENTER (品号工序工作中心信息)**
- **ITEM_PLANT (品号工厂信息)**
- **ITEM_PLANT_CSTAF (品号成本分配因子)**
- **ITEM_PURCHASE (品号采购信息)**
- **ITEM_RESOURCE (品号资源信息)**
- **ITEM_RESOURCE_D (品号资源单身信息)**
- **ITEM_ROUTING (产品工艺路线信息)**
- **ITEM_ROUTING_D (产品工艺路线单身信息)**
- **ITEM_ROUTING_PATH (产品工艺路线路径)**
- **ITEM_ROUTING_SUB_OPERATION (产品工艺路线子工艺)**
- **ITEM_ROUTING_WORK_CENTER (产品工艺路线工作中心信息)**
- **ITEM_SALES (品号销售信息)**
- **ITEM_SERVICE (品号\品类服务信息)**
- **ITEM_SERVICE_AREA (品号\品类服务信息--区域单身)**
- **ITEM_SORT_VARIABLE (品号变量分类)**
- **ITEM_SORT_VARIABLE_D (品号变量分类单身)**
- **ITEM_STRI_DEGREE (宽严程度)**
- **ITEM_STRI_DEGREE_D (宽严程度明细)**
- **ITEM_SUPPLIER (品号供应商信息)**
- **ITEM_SUPPLIER_PRICE (品号供应商价格信息)**
- **ITEM_SUPPLIER_PRICE_D (品号供应商价格信息单身)**
- **ITEM_TAX_CLASSIFICATION (存货/服务税分类)**
- **ITEM_TRANSFER (过户信息)**
- **ITEM_UNITS_CONVERSION (通用品号单位换算信息)**
- **ITEM_WAREHOUSE (品号仓库信息)**
- **ITEM_WAREHOUSE_BIN (存货余额明细信息)**

## Filtered Out

> These 1 tables were excluded (templates, logs, history, backups, system):

- ~~ITEM_PLANT20181024~~ (history/backup)

---

## Table Details

### ITEM_BARCODE (品号条码信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_BARCODE_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 品号编号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 品号特征码 | GUID | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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


### ITEM_BARCODE_D (品号条码信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | ITEM_BARCODE_D_ID | 主键 | GUID | Y | Y |
| 5 | BARCODE | 条码 | string(60) | Y |  |
| 6 | UNIT_ID | 单位 | GUID | Y |  |
| 7 | ADDRESS | 产地 | string(60) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |
| 39 | ITEM_BARCODE_ID |  | GUID | Y |  |


### ITEM_BC_REG (品号条码注册信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_BC_REG_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | MAIN | 主要 | number(0/1) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | LABEL_LAYOUT | 标签样式 | string(400) | Y |  |
| 9 | BC_REG_ID | 规则编号ID | GUID | Y |  |
| 10 | LABEL_LAYOUT_NAME | 标签样式名称 | string(400) | Y |  |
| 11 | ITEM_DEFUALT | 是否通用品号预设 | number(0/1) | Y |  |
| 12 | CODE_TYPE | 编码类型 | string(40) | Y |  |
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
| 45 | FIFO_TYPE |  | string(400) | Y |  |
| 46 | QTY |  | number(16,6) | Y |  |
| 47 | LOT_AUTO |  | number(0/1) | Y |  |
| 48 | FEATURE_GROUP_ID |  | GUID | Y |  |


### ITEM_BENCHMARK_COST (维护品号基准成本)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_BENCHMARK_COST_ID | 主键 | GUID | Y | Y |
| 4 | PLANT_ID | 工厂 | GUID | Y |  |
| 5 | ITEM_NATURE | 品号性质 | number | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | CLCOST_AMT | 本阶成本合计 | number(23,8) | Y |  |
| 9 | LLCOST_AMT | 下阶成本合计 | number(23,8) | Y |  |
| 10 | COST_AMT | 成本合计 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | PROCESS_TYPE | 生产方式 | string(40) | Y |  |
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


### ITEM_BENCHMARK_COST_D (品号基准成本单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_BENCHMARK_COST_D_ID | 主键 | GUID | Y | Y |
| 3 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 4 | CLCOST_AMT | 本阶成本 | number(23,8) | Y |  |
| 5 | LLCOST_AMT | 下阶成本 | number(23,8) | Y |  |
| 6 | COST_AMT | 成本小计 | number(23,8) | Y |  |
| 7 | COST_CONSTITUENT_RATE | 构成比率 | number(5,4) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ITEM_BENCHMARK_COST_ID |  | GUID | Y |  |


### ITEM_CERTIFICATION (品号认可信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_CERTIFICATION_ID | 主键 | GUID | Y | Y |
| 4 | CERTIFICATION | 认可检查项 | number(0/1) | Y |  |
| 5 | ITEM_ID | 品号基本信息档 | GUID | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_CERTIFICATION_CHANGE (品号认可变更信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_CERTIFICATION_CHANGE_ID | 主键 | GUID | Y | Y |
| 4 | CERTIFICATION_MODEL | 认可型号 | string(40) | Y |  |
| 5 | CHANGE_TIMES | 更改次数 | string(8) | Y |  |
| 6 | REASON | 变更原因 | string(510) | Y |  |
| 7 | CERTIFICATION_STATUS | 认可状态 | number(0/1) | Y |  |
| 8 | MAJOR_SOURCE | 主要来源 | number(0/1) | Y |  |
| 9 | CERTIFICATION_NO | 认可文号 | string(40) | Y |  |
| 10 | SAMPLE_DATE | 送样日期 | date | Y |  |
| 11 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 12 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | ORIG_CERTIFICATION_MODEL | 原认可型号 | string(40) | Y |  |
| 15 | ORIGINAL_CERTIFICATION_STATUS | 原认可状态 | number(0/1) | Y |  |
| 16 | ORIGINAL_MAIN_SOURCE | 原主要来源 | number(0/1) | Y |  |
| 17 | ORIGINAL_CERTIFICATION_NO | 原认可文号 | string(40) | Y |  |
| 18 | ORIGINAL_SAMPLE_DATE | 原送样日期 | date | Y |  |
| 19 | ORIGINAL_EFFECTIVE_DATE | 原生效日期 | date | Y |  |
| 20 | ORIGINAL_EXPIRY_DATE | 原失效日期 | date | Y |  |
| 21 | ORIGINAL_REMARK | 原备注 | string(510) | Y |  |
| 22 | BRAND | 品牌信息 | string(80) | Y |  |
| 23 | ORIGINAL_BRAND | 原品牌信息 | string(80) | Y |  |
| 24 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 25 | SUPPLIER_ID | 建议供应商 | GUID | Y |  |
| 26 | ORIGINAL_SUPPLIER_ID | 原建议供应商 | GUID | Y |  |
| 27 | ITEM_ID | 品号 | GUID | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_CERTIFICATION_D (品号认可信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_CERTIFICATION_D_ID | 主键 | GUID | Y | Y |
| 2 | CERTIFICATION_MODEL | 认可型号 | string(40) | Y |  |
| 3 | CERTIFICATION_STATUS | 认可状态 | number(0/1) | Y |  |
| 4 | MAJOR_SOURCE | 主要来源 | number(0/1) | Y |  |
| 5 | CERTIFICATION_NO | 认可文号 | string(40) | Y |  |
| 6 | SAMPLE_DATE | 送样日期 | date | Y |  |
| 7 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 8 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | BRAND | 品牌信息 | string(80) | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 12 | SUPPLIER_ID | 供应商 | GUID | Y |  |
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
| 41 | ITEM_CERTIFICATION_ID |  | GUID | Y |  |


### ITEM_COST (品号成本)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_COST_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | PLANT_ID | 工厂 | GUID | Y |  |
| 8 | ITEM_NATURE | 品号性质 | number | Y |  |
| 9 | ITEM_ID | 品号 | GUID | Y |  |
| 10 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 11 | PROD_COMPLETED_QTY | 生产入库 | number(16,6) | Y |  |
| 12 | SUB_COMPLETED_QTY | 委外入库 | number(16,6) | Y |  |
| 13 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 14 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 15 | CLCOST_AMT | 本阶成本合计 | number(23,8) | Y |  |
| 16 | LLCOST_AMT | 下阶成本合计 | number(23,8) | Y |  |
| 17 | COST_AMT | 成本合计 | number(23,8) | Y |  |
| 18 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | PROCESS_TYPE | 生产方式 | string(40) | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Attachments | 附件 | string | Y |  |
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
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_COST_D (品号成本单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_COST_D_ID | 主键 | GUID | Y | Y |
| 3 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 4 | CLCOST_AMT | 本阶成本 | number(23,8) | Y |  |
| 5 | LLCOST_AMT | 下阶成本 | number(23,8) | Y |  |
| 6 | COST_AMT | 成本小计 | number(23,8) | Y |  |
| 7 | COST_CONSTITUENT_RATE | 构成比率 | number(23,8) | Y |  |
| 8 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 9 | UNIT_CLCOST | 单位本阶成本 | number(23,8) | Y |  |
| 10 | UNIT_LLCOST | 单位下阶成本 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ITEM_COST_ID |  | GUID | Y |  |


### ITEM_FEATURE (通用品号特征码信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_FEATURE_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_FEATURE_CODE | 特征码 | string(120) | Y |  |
| 3 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_PICTURE | 图片 | string(400) |  |  |
| 6 | FEATURE_ARRAY | 属性值数组 | string(8000) | Y |  |
| 7 | WEIGHT_PLU | 电子称PLU | string(20) | Y |  |
| 8 | ITEM_FEATURE_PIC | 特征码图片 | string(4000) | Y |  |
| 9 | ITEM_DESC2 | 特征码描述(作废) | string | Y |  |
| 10 | ITEM_DESC | 特征码描述 | string(4000) | Y |  |
| 11 | DRAWING_NO | 图号 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | ITEM_BUSINESS_ID |  | GUID | Y |  |


### ITEM_FEATURE_PLANT (品号特征工厂信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_FEATURE_PLANT_ID | 主键 | GUID | Y | Y |
| 2 | LOW_LEVEL_CODE |  | string(4) | Y |  |
| 3 | CUSTOMER_BOM_CONTROL | 已产生客戶BOM | number(0/1) | Y |  |
| 4 | CONFIG_HASH_CODE | 手动配置识别码 | string(510) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | PLANT_ID | 工厂 | GUID | Y |  |
| 7 | BOM_STATUS | 客户BOM状态 | string(40) | Y |  |
| 8 | STANDARD_ROUTING_ID | 标准工艺路线 | GUID | Y |  |
| 9 | BOM_VERSION_TIMES | 客户BOM版次 | string(8) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | ITEM_FEATURE_ID |  | GUID | Y |  |


### ITEM_FEATURE_VALUE (通用品号属性值信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_FEATURE_VALUE_ID | 主键 | GUID | Y | Y |
| 2 | FEATURE_CATEGORY | 类别 | string(40) | Y |  |
| 3 | FEATURE_VALUE | 品号特征值 | string(120) | Y |  |
| 4 | SECTION_NO | 自动编号内定值 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | FEATURE_CODE_TYPE | 编码类型 | string(40) | Y |  |
| 7 | FEATURE_VALUE_DESC | 属性值描述 | string(120) | Y |  |
| 8 | PARENT_ITEM_ID | 通用品号主键 | GUID | Y |  |
| 9 | FEATURE_GROUP_ID | 品号群组代码 | GUID | Y |  |
| 10 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 11 | FEATURE_ID | 属性代码 | GUID | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | ORG_ID_RTK |  | string(400) | Y |  |
| 41 | ORG_ID_ROid |  | GUID | Y |  |
| 42 | ITEM_BUSINESS_ID |  | GUID | Y |  |


### ITEM_FINANCIAL (品号财务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | TAX_CATEGORY_ID | 税目 | GUID | Y |  |
| 7 | IM_FICATEGORY_ID | 存货会计分类 | GUID | Y |  |
| 8 | IM_COST_CATEGORY_ID | 存货成本分类 | GUID | Y |  |
| 9 | ITEM_FEATURE_COST_FLAG | 按特征码区分成本 | number(0/1) | Y |  |
| 10 | IM_COST_CATEGORY2_ID | 在制约量估算分类 | GUID | Y |  |
| 11 | SOURCE | 品号来源 | string(40) | Y |  |
| 12 | PLM_DATAKEY | PLM传输批次号 | string(80) | Y |  |
| 13 | ISWARR_CATEGORY_ID | 品号销售保修分类 | GUID | Y |  |
| 14 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 39 | Attachments | 附件 | string | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | BUDGET_CTRL_CATEGORY_ID | 预算控制分类 | GUID | Y |  |
| 47 | IMPORT_TARIFF_CATEGORY | 进口关税分类 | GUID | Y |  |
| 48 | COMMODITY_TAX_CATEGORY | 进口货物税分类 | GUID | Y |  |


### ITEM_GROUP (品号群组通用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_GROUP_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | INVENTORY_MANAGEMENT | 存货管理 | number(0/1) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SHORTCUT | 快捷码 | string(40) | Y |  |
| 7 | LOT_CONTROL | 批号管理 | string(40) | Y |  |
| 8 | LOT_EXPIRE_DAY | 批号有效天数 | number | Y |  |
| 9 | LOT_WAITING_DAY | 批号等待天数 | number | Y |  |
| 10 | LOT_REINSPECTION_DAY | 批号复检天数 | number | Y |  |
| 11 | LOT_FAILURE_CONTROL | 修改批号有效日期 | string(40) | Y |  |
| 12 | UNIT_MODE | 计量体系 | string(40) | Y |  |
| 13 | INVENTORY_CHECK_BY | 库存检查方式 | string(40) | Y |  |
| 14 | ITEM_SN_MANAGEMENT | 序列号管理 | number(0/1) | Y |  |
| 15 | SN_ENTRY_MODE | 序列号输入模式 | string(40) | Y |  |
| 16 | ITEM_FEATURE_CONTROL | 启用特征码 | number(0/1) | Y |  |
| 17 | PACKING_UNIT | 以包装方式输入数量 | number(0/1) | Y |  |
| 18 | STATUS | 状态 | string(40) | Y |  |
| 19 | FEATURE_GENERATE_MODE | 特征码产生模式 | string(40) | Y |  |
| 20 | CKD | CKD母件 | number(0/1) | Y |  |
| 21 | JOINT_PRODUCT_CONTROL | 多产出 | number(0/1) | Y |  |
| 22 | NEED_CERTIFICATION | 认样检查 | number(0/1) | Y |  |
| 23 | LOT_NO_RULE_ID | 批号编码规则 | GUID | Y |  |
| 24 | SN_NO_RULE_ID | 序号编码规则 | GUID | Y |  |
| 25 | FEATURE_GROUP_ID | 品号群组 | GUID | Y |  |
| 26 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |
| 27 | STOCK_UNIT_ID | 库存单位 | GUID | Y |  |
| 28 | LIFECYCLE_ID | 生命周期 | GUID | Y |  |
| 29 | LOGISTIC_UNIT_ID | 物流单位 | GUID | Y |  |
| 30 | ISWEIGHT | 电子称重 | number(0/1) | Y |  |
| 31 | WEIGHT_PRICE | 电子称变价 | number(0/1) | Y |  |
| 32 | WEIGHT_PLU | 电子称PLU | string(20) | Y |  |
| 33 | WEIGHT_UNIT_ID | 电子称单位 | GUID | Y |  |
| 34 | CHANGE_ITEM_SPEC | 归类品 | number(0/1) | Y |  |
| 35 | DRAWING_NO | 图号 | string(510) | Y |  |
| 36 | DRAWING_NO_FROM | 图号取自 | string(40) | Y |  |
| 37 | SERVICE_ITEM | 服务品号 | number(0/1) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |
| 68 | Owner_Org_RTK |  | string(400) | Y |  |
| 69 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_GROUP_FEATURE_VALUE (品号群组属性值信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_GROUP_FEATURE_VALUE_ID | 主键 | GUID | Y | Y |
| 2 | FEATURE_CATEGORY | 类别 | string(40) | Y |  |
| 3 | FEATURE_VALUE | 属性值 | string(120) | Y |  |
| 4 | SECTION_NO | 段号 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | FEATURE_CODE_TYPE | 编码类型 | string(40) | Y |  |
| 7 | FEATURE_VALUE_DESC | 属性值描述 | string(120) | Y |  |
| 8 | FEATURE_GROUP_ID | 品号群组代码 | GUID | Y |  |
| 9 | FEATURE_ID | 属性代码 | GUID | Y |  |
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
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ORG_ID_RTK |  | string(400) | Y |  |
| 36 | ORG_ID_ROid |  | GUID | Y |  |
| 37 | ITEM_GROUP_BUSINESS_ID |  | GUID | Y |  |


### ITEM_GROUP_FINANCIAL (品号群组财务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_GROUP_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | TAX_CATEGORY_ID | 税目 | GUID | Y |  |
| 6 | IM_FICATEGORY_ID | 存货会计分类 | GUID | Y |  |
| 7 | IM_COST_CATEGORY_ID | 存货成本分类 | GUID | Y |  |
| 8 | ITEM_FEATURE_COST_FLAG | 按特征码区分成本 | number(0/1) | Y |  |
| 9 | IM_COST_CATEGORY2_ID | 在制约量估算分类 | GUID | Y |  |
| 10 | FEATURE_GROUP_ID | 品号群组 | GUID | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_GROUP_PLANT (品号群组工厂信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_GROUP_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | CYCLE_COUNT_CODE | 循环盘点码 | string(8) | Y |  |
| 5 | ITEM_PROPERTY | 品号类型 | string(40) | Y |  |
| 6 | ABC_CLASS | ABC等级 | string(2) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | ITEM_PICTURE | 图片 | string(400) |  |  |
| 9 | STORAGE_CONTROL | 储存控制 | string(40) | Y |  |
| 10 | WAREHOUSE_CONTROL | 出库控制 | string(40) | Y |  |
| 11 | ISSUE_DESTINATION_TYPE | 领料对象类型 | string(40) | Y |  |
| 12 | RECEIPT_OVERRUN_RATE | 超入率 | number(5,4) | Y |  |
| 13 | DYNAMIC_LEAD_TIME_M | 制造变动前置天数 | number(16,1) | Y |  |
| 14 | FIXED_LEAD_TIME_M | 制造固定前置天数 | number(16,1) | Y |  |
| 15 | ISSUE_MULTIPLE | 领用倍量 | number(16,6) | Y |  |
| 16 | INSPECT_MODE | 质检模式 | string(40) | Y |  |
| 17 | INSPECT_DAYS | 检验前置天数 | number(16,1) | Y |  |
| 18 | ROUTING_CONTROL | 工艺管理 | number(0/1) | Y |  |
| 19 | BATCH_QUANTITY_M | 前置天数计算批量 | number(16,6) | Y |  |
| 20 | MIN_ORDER_QTY | 最小补量 | number(16,6) | Y |  |
| 21 | ORDER_MULTIPLE | 补货倍量 | number(16,6) | Y |  |
| 22 | STRICTNESS_DEGREE | 严格程度 | string(80) | Y |  |
| 23 | YIELD_RATE | 产品良率 | number(5,4) | Y |  |
| 24 | RESERVED_RULE | 保留原则 | string(6) | Y |  |
| 25 | RESERVED_VALID_DAY | 保留有效天数 | number(16,1) | Y |  |
| 26 | RESERVED_CONTROL | 保留控制 | number(0/1) | Y |  |
| 27 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 28 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 29 | LOW_LEVEL_CODE | 低阶码 | string(4) | Y |  |
| 30 | IS_CRITICAL_ITEM | 关键料 | number(0/1) | Y |  |
| 31 | ORDER_POLICY | 补货政策 | string(40) | Y |  |
| 32 | SAFE_STOCK | 安全库存量 | number(16,6) | Y |  |
| 33 | PLAN_ORDER_RULE | 计划量开立规则 | string(40) | Y |  |
| 34 | MAX_ORDER_QTY | 最大补量 | number(16,6) | Y |  |
| 35 | IS_INTEGER | 整数规划 | number(0/1) | Y |  |
| 36 | IS_CONSOLIDATED | 是否并批开单 | number(0/1) | Y |  |
| 37 | CONSOLIDATE_DAY | 并单周期 | number | Y |  |
| 38 | LOT_MO_QTY | 批工单数量 | number(16,6) | Y |  |
| 39 | STORAGE_LIMIT_ID | 储存限制编号 | GUID | Y |  |
| 40 | MO_ISSUE_UNIT_ID | 领用单位 | GUID | Y |  |
| 41 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 42 | STANDARD_ROUTING_ID | 标准工艺路线编号 | GUID | Y |  |
| 43 | INBOUND_WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 44 | OUTBOUND_WAREHOUSE_ID | 出库仓库 | GUID | Y |  |
| 45 | MO_DOC_ID | 工单单据类型 | GUID | Y |  |
| 46 | SALES_CENTER_ID | 销售中心 | GUID | Y |  |
| 47 | MRP_TIME_BUCKET | MRP时距 | GUID | Y |  |
| 48 | REQUISITION_DOC_ID | 请购单单据类型 | GUID | Y |  |
| 49 | PLANNER_ID | 计划人员 | GUID | Y |  |
| 50 | ISSUE_TYPE | 领料模式 | string(40) | Y |  |
| 51 | REPLENISHMENT_CYCLE_ID | 补货周期 | GUID | Y |  |
| 52 | LOT_MO_LEAD_TIME | 移转批量所需天数 | number(16,1) | Y |  |
| 53 | REORDER_POINT | 补货点 | number(16,6) | Y |  |
| 54 | ECONOMIC_ORDER_QTY | 经济批量 | number(16,6) | Y |  |
| 55 | STANDARD_MAN_HOUR | 标准人时 | number | Y |  |
| 56 | STANDARD_MACHINE_HOUR | 标准机时 | number | Y |  |
| 57 | MULTIPURPOSE_CSTAF | 万能成本分配因子 | number(16,6) | Y |  |
| 58 | PRODUCTION_ADMIN_UNIT_ID | 主键 | GUID | Y |  |
| 59 | MIM_DISTRIBUTION_QTY | 最小配量 | number(16,6) | Y |  |
| 60 | DISTRIBUTION_MULTIPLE | 配送倍量 | number(16,6) | Y |  |
| 61 | BEST_STOCK | 最优库存量 | number(16,6) | Y |  |
| 62 | CYCLE_ORDER_CODE | 循环补货码 | string(8) | Y |  |
| 63 | ADD_DRP | 参与DRP计算 | number(0/1) | Y |  |
| 64 | ORDER_LEAD | 补货提前期 | number | Y |  |
| 65 | IS_DIRECT | 直供 | number(0/1) | Y |  |
| 66 | ORDER_SUPPLY_CENTER_ID | 补货采购域 | GUID | Y |  |
| 67 | ORDER_PLANT_ID | 补货机构 | GUID | Y |  |
| 68 | ORDER_SUPPLIER_ID | 补货参照供应商 | GUID | Y |  |
| 69 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 70 | LOT_CONTROL | 批号管理 | string(40) | Y |  |
| 71 | DISTRIBUTION_TYPE | 库存不足配送方案 | string(40) | Y |  |
| 72 | SUPPLY_CENTER_ID | 供应中心 | GUID | Y |  |
| 73 | ORDER_DOC_ID | 补货申请单单据类型 | GUID | Y |  |
| 74 | ISSUE_CRITICAL | 领料关键料 | number(0/1) | Y |  |
| 75 | IS_DISTRIBUTION | 配送机构否 | string(40) | Y |  |
| 76 | TRANSPORT_DAYS | 运输天数 | number(7,3) | Y |  |
| 77 | TRANSFER_OUT_PLANT_ID | 主鍵 | GUID | Y |  |
| 78 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
| 79 | TRANSFER_REQUISITION_ID | 调拨申请单单据类型 | GUID | Y |  |
| 80 | QC_CATEGORY_ID | 品管类别 | GUID | Y |  |
| 81 | INSPECTION_UNIT_ID | 品管单位 | GUID | Y |  |
| 82 | FEATURE_GROUP_ID | 品号群组 | GUID | Y |  |
| 83 | ITEM_ROUTING_CONTROL | 工艺管理 | string(40) | Y |  |
| 84 | TRANSACTION_UNIT_ID | 存货交易单位 | GUID | Y |  |
| 85 | SYNERGY_ID | 内部协同关系 | GUID | Y |  |
| 86 | INNER_ORDER_DOC_ID | 内部订单单据类型 | GUID | Y |  |
| 87 | PURCHASE_CONSIDER_ORDER | 采购件由计划考虑补货机制 | number(0/1) | Y |  |
| 88 | CreateDate | 创建日期 | date | Y |  |
| 89 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 90 | ModifiedDate | 修改日期 | date | Y |  |
| 91 | CreateBy | 创建者 | GUID | Y |  |
| 92 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 93 | ModifiedBy | 修改者 | GUID | Y |  |
| 94 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 95 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 96 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 97 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 98 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 99 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 100 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 101 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 102 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 103 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 104 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 105 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 106 | UDF041 | 自定义字段12 | date | Y |  |
| 107 | UDF042 | 自定义字段13 | date | Y |  |
| 108 | UDF051 | 自定义字段14 | GUID | Y |  |
| 109 | UDF052 | 自定义字段15 | GUID | Y |  |
| 110 | UDF053 | 自定义字段16 | GUID | Y |  |
| 111 | UDF054 | 自定义字段17 | GUID | Y |  |
| 112 | Attachments | 附件 | string | Y |  |
| 113 | Version | 版本号，不要随意更改 | binary | Y |  |
| 114 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 115 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 116 | ApproveDate | 修改日期 | date | Y |  |
| 117 | ApproveBy | 修改人 | GUID | Y |  |
| 118 | Owner_Org_RTK |  | string(400) | Y |  |
| 119 | Owner_Org_ROid |  | GUID | Y |  |
| 120 | CONSOLIDATED |  | string(40) | Y |  |
| 121 | MRP_CRITICAL_ITEM_TYPE |  | string(40) | Y |  |


### ITEM_GROUP_PLANT_CSTAF (品号群组成本分配因子)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_GROUP_PLANT_CSTAF_ID | 主键 | GUID | Y | Y |
| 3 | STANDARD_VALUE | 标准值 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | SF_DATA_LIST_ID | 生产报工项目 | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ITEM_GROUP_BUSINESS_ID |  | GUID | Y |  |


### ITEM_GROUP_PURCHASE (品号群组采购信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_GROUP_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | BATCH_QUANTITY_P | 批量 | number(16,6) | Y |  |
| 5 | DYNAMIC_LEAD_TIME_P | 采购变动前置天数 | number | Y |  |
| 6 | FIXED_LEAD_TIME_P | 采购固定前置天数 | number | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | SUPPLIER_POLICY | 供应商策略 | string(40) | Y |  |
| 9 | INQUIRIES_CYCLES | 询价周期天数 | number | Y |  |
| 10 | INQUIRIES_NUMBERS | 询价家数 | number | Y |  |
| 11 | INQUIRIES_POLICY | 询价策略 | string(40) | Y |  |
| 12 | PRICE_UPPER_LIMIT_RATE | 单价上限率 | number(5,4) | Y |  |
| 13 | PURCHASE_PRICE_CONTROL | 进价控制 | number(0/1) | Y |  |
| 14 | RECEIPT_AHEAD_CONTROL | 允许早收 | number(0/1) | Y |  |
| 15 | RECEIPT_OVER_CONTROL | 超收管理 | number(0/1) | Y |  |
| 16 | RECEIPT_OVER_RATE | 超收率 | number(5,4) | Y |  |
| 17 | CKD_ITEM_PRICE_PO | CKD品号价格 | string(40) | Y |  |
| 18 | CKD_PACKING_PO | CKD成套进货 | number(0/1) | Y |  |
| 19 | CKD_PACKING_PO_RETURN | CKD成套采购退货 | number(0/1) | Y |  |
| 20 | GENERAL_RECEIPT_SHORT_CTL | 商品允许短收 | number(0/1) | Y |  |
| 21 | GENERAL_RECEIPT_SHORT_RATE | 商品短收比例 | number(5,4) | Y |  |
| 22 | LARGESS_RECEIPT_SHORT_CTL | 赠备品允许短收 | number(0/1) | Y |  |
| 23 | LARGESS_RECEIPT_SHORT_RATE | 赠备品短收比例 | number(5,4) | Y |  |
| 24 | UNIT_DIFFER | 计价单位和采购单位须相同 | number(0/1) | Y |  |
| 25 | PUR_UNIT_ID | 采购单位 | GUID | Y |  |
| 26 | PUR_PRICE_UNIT_ID | 采购计价单位 | GUID | Y |  |
| 27 | ITEM_TAX_CLASSIFICATION_ID | 存货/服务税分类编号 | GUID | Y |  |
| 28 | MINIMUM_ORDER_QUANTITY | 最低补量 | number(16,6) | Y |  |
| 29 | ORDER_MULTIPLE | 采购倍量 | number(16,6) | Y |  |
| 30 | FEATURE_GROUP_ID | 品号群组 | GUID | Y |  |
| 31 | BUYER_ID | 采购员 | GUID | Y |  |
| 32 | CONSIDER_ORDER_RULE | 请转采考虑补货机制 | number(0/1) | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Attachments | 附件 | string | Y |  |
| 40 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 41 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 42 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 43 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 44 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 45 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 46 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 47 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 48 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 49 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 50 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 51 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 52 | UDF041 | 自定义字段12 | date | Y |  |
| 53 | UDF042 | 自定义字段13 | date | Y |  |
| 54 | UDF051 | 自定义字段14 | GUID | Y |  |
| 55 | UDF052 | 自定义字段15 | GUID | Y |  |
| 56 | UDF053 | 自定义字段16 | GUID | Y |  |
| 57 | UDF054 | 自定义字段17 | GUID | Y |  |
| 58 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | Version | 版本号，不要随意更改 | binary | Y |  |
| 63 | Owner_Org_RTK |  | string(400) | Y |  |
| 64 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_GROUP_SALES (品号群组销售信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_GROUP_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | CKD_SALES | CKD出货 | number(0/1) | Y |  |
| 5 | CKD_ITEM_PRICE | CKD品号价格 | string(40) | Y |  |
| 6 | CKD_PACKING_SALES | CKD成套出货 | number(0/1) | Y |  |
| 7 | CKD_PACKING_SALES_RETURN | CKD成套销退 | number(0/1) | Y |  |
| 8 | LARGESS_DEL_OVERRUN_CONTROL | 赠备品超交管理 | number(0/1) | Y |  |
| 9 | LARGESS_DEL_OVERRUN_RATE | 赠备品超交率 | number(5,4) | Y |  |
| 10 | GENERAL_DEL_OVERRUN_CONTROL | 一般商品超交管理 | number(0/1) | Y |  |
| 11 | GENERAL_DEL_OVERRUN_RATE | 赠备品超交率 | number(5,4) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | UNIT_DIFFER | 计价单位和业务单位必须相同 | number(0/1) | Y |  |
| 14 | SLS_UNIT_ID | 销售单位 | GUID | Y |  |
| 15 | SLS_PRICE_UNIT_ID | 销售计价单位 | GUID | Y |  |
| 16 | DELIVERY_PLANT_ID | 发货工厂/储运主键 | GUID | Y |  |
| 17 | ITEM_TAX_CLASSIFICATION_ID | 存货/服务税分类编号 | GUID | Y |  |
| 18 | FEATURE_GROUP_ID | 品号群组 | GUID | Y |  |
| 19 | LIMIT_CONTROL | 允限销管制品 | number(0/1) | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
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
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_GROUP_SUPPLIER (品号群组供应商信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_GROUP_SUPPLIER_ID | 主键 | GUID | Y | Y |
| 2 | PRIORITY | 优先级 | number | Y |  |
| 3 | PURCHASE_RATE | 采购比例 | number(5,4) | Y |  |
| 4 | MAX_QUANTITY | 单笔最大采购量 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | LAST_INQUIRIES_DATE | 最近询价日 | date | Y |  |
| 7 | MAIN | 主要 | number(0/1) | Y |  |
| 8 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | ITEM_GROUP_BUSINESS_ID |  | GUID | Y |  |


### ITEM_LOT (品号批号信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_LOT_ID | 主键 | GUID | Y | Y |
| 4 | ALLOW_ISSUE_DATE | 允许出库日 | date | Y |  |
| 5 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 6 | FIRST_RECEIPT_DATE | 首次入库日 | date | Y |  |
| 7 | LAST_RECEIPT_DATE | 最后入库日 | date | Y |  |
| 8 | LAST_ISSUE_DATE | 最后出库日 | date | Y |  |
| 9 | LAST_COUNT_DATE | 上次盘点日 | date | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | LOT_CODE | 批号 | string(60) | Y |  |
| 12 | INEFFECTIVE_DATE | 有效截止日期 | date | Y |  |
| 13 | LOT_DESCRIPTION | 批号说明 | string(510) | Y |  |
| 14 | ITEM_ID | 品号 | GUID | Y |  |
| 15 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |


### ITEM_MAPPING (品号映射信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_MAPPING_ID | 主键 | GUID | Y | Y |
| 4 | CLIENT_PLANT_ID | 委托方工厂/储运 | GUID | Y |  |
| 5 | PRODUCER_PLANT_ID | 生产方工厂/储运 | GUID | Y |  |
| 6 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_MAPPING_D (品号映射信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_MAPPING_D_ID | 主键 | GUID | Y | Y |
| 2 | CLIENT_ITEM_ID | 委托方品号 | GUID | Y |  |
| 3 | CLIENT_ITEM_DESCRIPTION | 委托方品名 | string(120) | Y |  |
| 4 | CLIENT_ITEM_FEATURE_ID | 委托方特征码 | GUID | Y |  |
| 5 | CLIENT_ITEM_SPECIFICATION | 委托方规格 | string(510) | Y |  |
| 6 | CLIENT_OPERATION_ID | 委托方工艺 | GUID | Y |  |
| 7 | PRODUCER_ITEM_ID | 生产方品号 | GUID | Y |  |
| 8 | PRODUCER_ITEM_DESCRIPTION | 生产方品名 | string(120) | Y |  |
| 9 | PRODUCER_ITEM_FEATURE_ID | 生产方特征码 | GUID | Y |  |
| 10 | PRODUCER_ITEM_SPECIFICATION | 生产方规格 | string(510) | Y |  |
| 11 | PRODUCER_OPERATION_ID | 生产方工艺 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | ITEM_MAPPING_ID |  | GUID | Y |  |


### ITEM_OPERATION_CENTER (品号工序工作中心信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_OPERATION_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | SALE_UNIT_ID | 主键 | GUID | Y |  |
| 5 | SALE | 允许零售 | number(0/1) | Y |  |
| 6 | CALL | 允许门店要货 | number(0/1) | Y |  |
| 7 | CALL_STRATEGY_ID | 要货策略 | GUID | Y |  |
| 8 | MIN_CALL_QTY | 最小要货量 | number(16,6) | Y |  |
| 9 | SUBMULTIPLE_QTY | 要货倍量 | number(16,6) | Y |  |
| 10 | KEEP_DAYS | 要货支持天数 | number | Y |  |
| 11 | CALL_POINT_QTY | 要货点 | number(16,6) | Y |  |
| 12 | EOQ | 要货经济批量 | number(16,6) | Y |  |
| 13 | BEST_STORE_QTY | 最优库存 | number(16,6) | Y |  |
| 14 | CALL_PERIOD | 要货周期码 | string(40) | Y |  |
| 15 | BEGIN_DATE | 引入日期 | date | Y |  |
| 16 | END_DATE | 淘汰日期 | date | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | ITEM_ID | 品号 | GUID | Y |  |
| 19 | TAX_ID | 税种 | GUID | Y |  |
| 20 | TAX_RATE |  | number(5,4) | Y |  |
| 21 | ORDER | 允许销售订单 | number(0/1) | Y |  |
| 22 | COST | 单位成本 | number(23,8) | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
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
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Owner_Org_RTK |  | string(400) | Y |  |
| 54 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_PLANT (品号工厂信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CYCLE_COUNT_CODE | 循环盘点码 | string(8) | Y |  |
| 4 | ITEM_PROPERTY | 品号类型 | string(40) | Y |  |
| 5 | ABC_CLASS | ABC等级 | string(2) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | ITEM_PICTURE | 图片 | string(400) |  |  |
| 8 | STORAGE_CONTROL | 储存控制 | string(40) | Y |  |
| 9 | WAREHOUSE_CONTROL | 出库控制 | string(40) | Y |  |
| 10 | ISSUE_DESTINATION_TYPE | 领料对象类型 | string(40) | Y |  |
| 11 | RECEIPT_OVERRUN_RATE | 超入率 | number(5,4) | Y |  |
| 12 | DYNAMIC_LEAD_TIME_M | 制造变动前置天数 | number(16,1) | Y |  |
| 13 | FIXED_LEAD_TIME_M | 制造固定前置天数 | number(16,1) | Y |  |
| 14 | ISSUE_MULTIPLE | 领用倍量 | number(16,6) | Y |  |
| 15 | INSPECT_MODE | 质检模式 | string(40) | Y |  |
| 16 | INSPECT_DAYS | 检验前置天数 | number(16,1) | Y |  |
| 17 | ROUTING_CONTROL | 工艺管理 | number(0/1) | Y |  |
| 18 | BATCH_QUANTITY_M | 批量 | number(16,6) | Y |  |
| 19 | MIN_ORDER_QTY | 最小补量 | number(16,6) | Y |  |
| 20 | ORDER_MULTIPLE | 补货倍量 | number(16,6) | Y |  |
| 21 | STRICTNESS_DEGREE | 严格程度 | string(80) | Y |  |
| 22 | YIELD_RATE | 产品良率 | number(5,4) | Y |  |
| 23 | RESERVED_RULE | 保留原则 | string(6) | Y |  |
| 24 | RESERVED_VALID_DAY | 保留有效天数 | number(16,1) | Y |  |
| 25 | RESERVED_CONTROL | 保留控制 | number(0/1) | Y |  |
| 26 | ISSUE_OVERRUN_RATE | 超领率 | number(5,4) | Y |  |
| 27 | ISSUE_SHORTAGE_RATE | 缺领率 | number(5,4) | Y |  |
| 28 | LOW_LEVEL_CODE | 低阶码 | string(4) | Y |  |
| 29 | IS_CRITICAL_ITEM | 关键料 | number(0/1) | Y |  |
| 30 | ORDER_POLICY | 补货政策 | string(40) | Y |  |
| 31 | SAFE_STOCK | 安全库存量 | number(16,6) | Y |  |
| 32 | PLAN_ORDER_RULE | 计划量开立规则 | string(40) | Y |  |
| 33 | MAX_ORDER_QTY | 最大补量 | number(16,6) | Y |  |
| 34 | IS_INTEGER | 整数规划 | number(0/1) | Y |  |
| 35 | IS_CONSOLIDATED | 是否并批开单 | number(0/1) | Y |  |
| 36 | CONSOLIDATE_DAY | 并单周期 | number | Y |  |
| 37 | LOT_MO_QTY | 批工单数量 | number(16,6) | Y |  |
| 38 | ITEM_ID | 品号 | GUID | Y |  |
| 39 | STORAGE_LIMIT_ID | 储存限制编号 | GUID | Y |  |
| 40 | MO_ISSUE_UNIT_ID | 领用单位 | GUID | Y |  |
| 41 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 42 | STANDARD_ROUTING_ID | 标准工艺路线编号 | GUID | Y |  |
| 43 | INBOUND_WAREHOUSE_ID | 入库仓库 | GUID | Y |  |
| 44 | OUTBOUND_WAREHOUSE_ID | 出库仓库 | GUID | Y |  |
| 45 | MO_DOC_ID | 工单单据类型 | GUID | Y |  |
| 46 | SALES_CENTER_ID | 销售中心 | GUID | Y |  |
| 47 | MRP_TIME_BUCKET | MRP时距 | GUID | Y |  |
| 48 | REQUISITION_DOC_ID | 请购单单据类型 | GUID | Y |  |
| 49 | PLANNER_ID | 计划人员 | GUID | Y |  |
| 50 | ISSUE_TYPE | 领料模式 | string(40) | Y |  |
| 51 | REPLENISHMENT_CYCLE_ID | 补货周期 | GUID | Y |  |
| 52 | LOT_MO_LEAD_TIME | 移转批量所需天数 | number(16,1) | Y |  |
| 53 | REORDER_POINT | 补货点 | number(16,6) | Y |  |
| 54 | ECONOMIC_ORDER_QTY | 经济批量 | number(16,6) | Y |  |
| 55 | STANDARD_MAN_HOUR | 标准人时 | number | Y |  |
| 56 | STANDARD_MACHINE_HOUR | 标准机时 | number | Y |  |
| 57 | MULTIPURPOSE_CSTAF | 万能成本分配因子 | number(16,6) | Y |  |
| 58 | PRODUCTION_ADMIN_UNIT_ID | 主键 | GUID | Y |  |
| 59 | MIM_DISTRIBUTION_QTY | 最小配量 | number(16,6) | Y |  |
| 60 | DISTRIBUTION_MULTIPLE | 配送倍量 | number(16,6) | Y |  |
| 61 | BEST_STOCK | 最优库存量 | number(16,6) | Y |  |
| 62 | CYCLE_ORDER_CODE | 循环补货码 | string(8) | Y |  |
| 63 | ADD_DRP | 参与DRP计算 | number(0/1) | Y |  |
| 64 | ORDER_LEAD | 补货提前期 | number | Y |  |
| 65 | IS_DIRECT | 直供 | number(0/1) | Y |  |
| 66 | ORDER_SUPPLY_CENTER_ID | 补货采购域 | GUID | Y |  |
| 67 | ORDER_PLANT_ID | 补货机构 | GUID | Y |  |
| 68 | ORDER_SUPPLIER_ID | 补货参照供应商 | GUID | Y |  |
| 69 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 70 | LOT_CONTROL | 批号管理 | string(40) | Y |  |
| 71 | DISTRIBUTION_TYPE | 库存不足配送方案 | string(40) | Y |  |
| 72 | SUPPLY_CENTER_ID | 供应中心 | GUID | Y |  |
| 73 | ORDER_DOC_ID | 补货申请单单据类型 | GUID | Y |  |
| 74 | ISSUE_CRITICAL | 领料关键料 | number(0/1) | Y |  |
| 75 | IS_DISTRIBUTION | 配送机构否 | string(40) | Y |  |
| 76 | TRANSPORT_DAYS | 运输天数 | number(7,3) | Y |  |
| 77 | TRANSFER_OUT_PLANT_ID | 主鍵 | GUID | Y |  |
| 78 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
| 79 | TRANSFER_REQUISITION_ID | 调拨单单据类型 | GUID | Y |  |
| 80 | QC_CATEGORY_ID | 品管类别 | GUID | Y |  |
| 81 | INSPECTION_UNIT_ID | 品管单位 | GUID | Y |  |
| 82 | SOURCE | 品号来源 | string(40) | Y |  |
| 83 | PLM_DATAKEY | PLM传输批次号 | string(80) | Y |  |
| 84 | WAREHOUSE_ID | 存放仓库 | GUID | Y |  |
| 85 | BIN_ID | 存放库位 | GUID | Y |  |
| 86 | UNIT1_ID | 长宽高计量单位 | GUID | Y |  |
| 87 | UNIT2_ID | 重量计量单位 | GUID | Y |  |
| 88 | LONG | 长 | number(16,6) | Y |  |
| 89 | HIGH | 高 | number(16,6) | Y |  |
| 90 | WIDE | 宽 | number(16,6) | Y |  |
| 91 | BULK | 体积 | number(16,6) | Y |  |
| 92 | WEIGHT | 重量 | number(16,6) | Y |  |
| 93 | WEIGHT1 | 物流单位重量 | number(16,6) | Y |  |
| 94 | PRODUCE_UNIT_ID | 制造单位 | GUID | Y |  |
| 95 | TRANSACTION_UNIT_ID | 存货交易单位 | GUID | Y |  |
| 96 | ITEM_BUSINESS_ID | 主键 | GUID | Y | Y |
| 97 | ITEM_ROUTING_CONTROL | 工艺管理 | string(40) | Y |  |
| 98 | DISTRIBUTION_PRICE | 供配价 | number(23,8) | Y |  |
| 99 | SYNERGY_ID | 内部协同关系 | GUID | Y |  |
| 100 | INNER_ORDER_DOC_ID | 内部订单单据类型 | GUID | Y |  |
| 101 | PURCHASE_CONSIDER_ORDER | 采购件由计划考虑补货机制 | number(0/1) | Y |  |
| 102 | RESERVED_PLAN_001 | 计划预留1 | string(40) | Y |  |
| 103 | RESERVED_PLAN_002 | 计划预留2 | string(40) | Y |  |
| 104 | RESERVED_PLAN_003 | 计划预留3 | number(0/1) | Y |  |
| 105 | Version | 版本号，不要随意更改 | binary | Y |  |
| 106 | CreateDate | 创建日期 | date | Y |  |
| 107 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 108 | ModifiedDate | 修改日期 | date | Y |  |
| 109 | CreateBy | 创建者 | GUID | Y |  |
| 110 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 111 | ModifiedBy | 修改者 | GUID | Y |  |
| 112 | Attachments | 附件 | string | Y |  |
| 113 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 114 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 115 | ApproveDate | 修改日期 | date | Y |  |
| 116 | ApproveBy | 修改人 | GUID | Y |  |
| 117 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 118 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 119 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 120 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 121 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 122 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 123 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 124 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 125 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 126 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 127 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 128 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 129 | UDF041 | 自定义字段12 | date | Y |  |
| 130 | UDF042 | 自定义字段13 | date | Y |  |
| 131 | UDF051 | 自定义字段14 | GUID | Y |  |
| 132 | UDF052 | 自定义字段15 | GUID | Y |  |
| 133 | UDF053 | 自定义字段16 | GUID | Y |  |
| 134 | UDF054 | 自定义字段17 | GUID | Y |  |
| 135 | Owner_Org_RTK |  | string(400) | Y |  |
| 136 | Owner_Org_ROid |  | GUID | Y |  |
| 137 | MRP_CRITICAL_ITEM_TYPE | 关键料类型 | string(40) | Y |  |
| 138 | CONSOLIDATED | 合并开单 | string(40) | Y |  |


### ITEM_PLANT_CSTAF (品号成本分配因子)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_PLANT_CSTAF_ID | 主键 | GUID | Y | Y |
| 3 | STANDARD_VALUE | 标准值 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | SF_DATA_LIST_ID | 生产报工项目 | GUID | Y |  |
| 6 | Version | 版本号，不要随意更改 | binary | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 14 | ApproveDate | 修改日期 | date | Y |  |
| 15 | ApproveBy | 修改人 | GUID | Y |  |
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
| 34 | ITEM_BUSINESS_ID |  | GUID | Y |  |


### ITEM_PURCHASE (品号采购信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | BATCH_QUANTITY_P | 批量 | number(16,6) | Y |  |
| 5 | DYNAMIC_LEAD_TIME_P | 采购变动前置天数 | number | Y |  |
| 6 | FIXED_LEAD_TIME_P | 采购固定前置天数 | number | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | SUPPLIER_POLICY | 供应商策略 | string(40) | Y |  |
| 9 | INQUIRIES_CYCLES | 询价周期天数 | number | Y |  |
| 10 | INQUIRIES_NUMBERS | 询价家数 | number | Y |  |
| 11 | INQUIRIES_POLICY | 询价策略 | string(40) | Y |  |
| 12 | PRICE_UPPER_LIMIT_RATE | 单价上限率 | number(5,4) | Y |  |
| 13 | PURCHASE_PRICE_CONTROL | 进价控制 | number(0/1) | Y |  |
| 14 | RECEIPT_AHEAD_CONTROL | 允许早收 | number(0/1) | Y |  |
| 15 | RECEIPT_OVER_CONTROL | 超收管理 | number(0/1) | Y |  |
| 16 | RECEIPT_OVER_RATE | 超收率 | number(5,4) | Y |  |
| 17 | CKD_ITEM_PRICE_PO | CKD品号价格 | string(40) | Y |  |
| 18 | CKD_PACKING_PO | CKD成套进货 | number(0/1) | Y |  |
| 19 | CKD_PACKING_PO_RETURN | CKD成套采购退货 | number(0/1) | Y |  |
| 20 | GENERAL_RECEIPT_SHORT_CTL | 商品允许短收 | number(0/1) | Y |  |
| 21 | GENERAL_RECEIPT_SHORT_RATE | 商品短收比例 | number(5,4) | Y |  |
| 22 | LARGESS_RECEIPT_SHORT_CTL | 赠备品允许短收 | number(0/1) | Y |  |
| 23 | LARGESS_RECEIPT_SHORT_RATE | 赠备品短收比例 | number(5,4) | Y |  |
| 24 | UNIT_DIFFER | 计价单位和采购单位须相同 | number(0/1) | Y |  |
| 25 | ITEM_ID | 品号 | GUID | Y |  |
| 26 | PUR_UNIT_ID | 采购单位 | GUID | Y |  |
| 27 | PUR_PRICE_UNIT_ID | 采购计价单位 | GUID | Y |  |
| 28 | ITEM_TAX_CLASSIFICATION_ID | 存货/服务税分类编号 | GUID | Y |  |
| 29 | MINIMUM_ORDER_QUANTITY | 最低补量 | number(16,6) | Y |  |
| 30 | ORDER_MULTIPLE | 采购倍量 | number(16,6) | Y |  |
| 31 | SOURCE | 品号来源 | string(40) | Y |  |
| 32 | PLM_DATAKEY | PLM传输批次号 | string(80) | Y |  |
| 33 | BUYER_ID | 采购员 | GUID | Y |  |
| 34 | CONSIDER_ORDER_RULE | 请转采考虑补货机制 | number(0/1) | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | CreateDate | 创建日期 | date | Y |  |
| 55 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 56 | ModifiedDate | 修改日期 | date | Y |  |
| 57 | CreateBy | 创建者 | GUID | Y |  |
| 58 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 59 | ModifiedBy | 修改者 | GUID | Y |  |
| 60 | Attachments | 附件 | string | Y |  |
| 61 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | Owner_Org_RTK |  | string(400) | Y |  |
| 66 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_RESOURCE (品号资源信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_RESOURCE_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_RESOURCE_D (品号资源单身信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_RESOURCE_D_ID | 主键 | GUID | Y | Y |
| 2 | PRIORITY_ORDER | 优先顺序 | number | Y |  |
| 3 | FIXED_CUNSUMED | 固定耗用 | number(8,2) | Y |  |
| 4 | DYNAMIC_CUNSUMED | 变动耗用 | number(8,2) | Y |  |
| 5 | CONSUMED_BATCH_QTY | 耗用批量 | number(16,6) | Y |  |
| 6 | AHEAD_OFFSET_TIME | 前置期 | number(8,2) | Y |  |
| 7 | BACK_OFFSET_TIME | 后置期 | number(8,2) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
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
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | ITEM_RESOURCE_ID |  | GUID | Y |  |


### ITEM_ROUTING (产品工艺路线信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_ROUTING_ID | 主键 | GUID | Y | Y |
| 4 | ROUTING_CODE | 工艺路线编号 | string(20) | Y |  |
| 5 | ROUTING_DES | 工艺路线名称 | string(240) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | LINEAR_ROUTING | 线性工艺 | number(0/1) | Y |  |
| 8 | OPERATION_RECEIPT_OVERRUN | 控制工序超入 | number(0/1) | Y |  |
| 9 | GRAPHIC_ATTRIBUTE | 位置 | binary |  |  |
| 10 | ITEM_FEATURE_ID | 工艺路线品号特徵码 | GUID | Y |  |
| 11 | ITEM_ID | 工艺路线品号 | GUID | Y |  |
| 12 | GRAPHIC_ATTRIBUTE_XML | 图形属性 | string | Y |  |
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
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_ROUTING_D (产品工艺路线单身信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_ROUTING_D_ID | 主键 | GUID | Y | Y |
| 3 | OPERATION_SEQ | 工序 | string(20) | Y |  |
| 4 | CHARACTER | 性质 | string(40) | Y |  |
| 5 | OPERATION_COMMENT | 工艺说明 | string(510) | Y |  |
| 6 | FIXED_MAN_HOUR | 固定人时(秒) | number | Y |  |
| 7 | DYNAMIC_MAN_HOUR | 变动人时(秒) | number | Y |  |
| 8 | FIXED_MACHINE_HOUR | 固定机时(秒) | number | Y |  |
| 9 | DYNAMIC_MACHINE_HOUR | 变动机时(秒) | number | Y |  |
| 10 | HOUR_BATCH_QTY | 工时批量 | number | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | POSITION_FLAG | 起讫标记 | string(40) | Y |  |
| 13 | WORK_CENTER_CONSTRAIN | 工作中心约束 | number(0/1) | Y |  |
| 14 | SPLIT_MERGE | 拆并方式 | string(40) | Y |  |
| 15 | CONVERSION_RATE | 转换率 | number(16,6) | Y |  |
| 16 | PECEIPT_OVERRUN_RATE | 超入率 | number(5,4) | Y |  |
| 17 | PIECE_PRICE | 计件单价 | number(23,8) | Y |  |
| 18 | LABOR_RATIO | 工时工资率 | number(16,6) | Y |  |
| 19 | DENOMINATOR | 底数 | number | Y |  |
| 20 | TRANSFER_BATCH_QTY | 转移批量 | number | Y |  |
| 21 | FIXED_LEAD_TIME | 固定前置天数 | number(7,3) | Y |  |
| 22 | DYNAMIC_LEAD_TIME | 变动前置天数 | number(7,3) | Y |  |
| 23 | LAGGED_TIME | 落后天数 | number(7,3) | Y |  |
| 24 | RESET_WORK_CENTER_CONSTRAIN | 重设工作中心约束 | number(0/1) | Y |  |
| 25 | OPERATION_ID | 工艺 | GUID | Y |  |
| 26 | PRE_PROCESSING_UNIT_ID | 主键 | GUID | Y |  |
| 27 | AFTER_PROCESSING_UNIT_ID | 主键 | GUID | Y |  |
| 28 | INSPECT_MODE | 质检模式 | string(40) | Y |  |
| 29 | AUTO_DECIDE | 自动判定 | number(0/1) | Y |  |
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
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | CreateDate | 创建日期 | date | Y |  |
| 53 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 54 | ModifiedDate | 修改日期 | date | Y |  |
| 55 | CreateBy | 创建者 | GUID | Y |  |
| 56 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 57 | ModifiedBy | 修改者 | GUID | Y |  |
| 58 | ITEM_ROUTING_ID |  | GUID | Y |  |


### ITEM_ROUTING_PATH (产品工艺路线路径)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_ROUTING_PATH_ID | 主键 | GUID | Y | Y |
| 2 | TO_SEQ | 后工序 | string(20) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CONVERSION_RATE | 转换率 | number(16,6) | Y |  |
| 5 | SUMMATION_CONVERSION_RATE | 累计转换率 | number(16,6) | Y |  |
| 6 | QTY_PER | 組成用量 | number(16,6) | Y |  |
| 7 | DENOMINATOR | 底数 | number | Y |  |
| 8 | PRE_PROCESSING_UNIT_ID | 主键 | GUID | Y |  |
| 9 | AFTER_PROCESSING_UNIT_ID | 主键 | GUID | Y |  |
| 10 | PATH_TYPE | 路径类型 | string(40) | Y |  |
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
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | ITEM_ROUTING_D_ID |  | GUID | Y |  |


### ITEM_ROUTING_SUB_OPERATION (产品工艺路线子工艺)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_ROUTING_SUB_OPERATION_ID | 主键 | GUID | Y | Y |
| 2 | SUB_OPERATION_SEQ | 子工序 | string(20) | Y |  |
| 3 | PIECE_PRICE | 计件单价 | number(23,8) | Y |  |
| 4 | LABOR_RATIO | 工时工资率 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | FIXED_MAN_HOUR | 固定人时(秒) | number | Y |  |
| 7 | DYNAMIC_MAN_HOUR | 变动人时(秒) | number | Y |  |
| 8 | FIXED_MACHINE_HOUR | 固定机时(秒) | number | Y |  |
| 9 | DYNAMIC_MACHINE_HOUR | 变动机时(秒) | number | Y |  |
| 10 | HOUR_BATCH_QTY | 工时批量 | number | Y |  |
| 11 | SUB_OPERATION_ID | 子工藝 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | ITEM_ROUTING_D_ID |  | GUID | Y |  |


### ITEM_ROUTING_WORK_CENTER (产品工艺路线工作中心信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_ROUTING_WORK_CENTER_ID | 主键 | GUID | Y | Y |
| 2 | MAIN_STATION | 主要 | number(0/1) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | ADMIN_UNIT_ID | 生产部门 | GUID | Y |  |
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
| 24 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 25 | ApproveDate | 修改日期 | date | Y |  |
| 26 | ApproveBy | 修改人 | GUID | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 34 | SOURCE_ID_ROid |  | GUID | Y |  |
| 35 | ITEM_ROUTING_D_ID |  | GUID | Y |  |
| 36 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |


### ITEM_SALES (品号销售信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_BUSINESS_ID | 主键 | GUID | Y | Y |
| 4 | CKD_SALES | CKD出货 | number(0/1) | Y |  |
| 5 | CKD_ITEM_PRICE | CKD品号价格 | string(40) | Y |  |
| 6 | CKD_PACKING_SALES | CKD成套出货 | number(0/1) | Y |  |
| 7 | CKD_PACKING_SALES_RETURN | CKD成套销退 | number(0/1) | Y |  |
| 8 | LARGESS_DEL_OVERRUN_CONTROL | 赠备品超交管理 | number(0/1) | Y |  |
| 9 | LARGESS_DEL_OVERRUN_RATE | 赠备品超交率 | number(5,4) | Y |  |
| 10 | GENERAL_DEL_OVERRUN_CONTROL | 一般商品超交管理 | number(0/1) | Y |  |
| 11 | GENERAL_DEL_OVERRUN_RATE | 赠备品超交率 | number(5,4) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | UNIT_DIFFER | 计价单位和业务单位必须相同 | number(0/1) | Y |  |
| 14 | ITEM_ID | 品号 | GUID | Y |  |
| 15 | SLS_UNIT_ID | 销售单位 | GUID | Y |  |
| 16 | SLS_PRICE_UNIT_ID | 销售计价单位 | GUID | Y |  |
| 17 | DELIVERY_PLANT_ID | 发货工厂/储运主键 | GUID | Y |  |
| 18 | ITEM_TAX_CLASSIFICATION_ID | 存货/服务税分类编号 | GUID | Y |  |
| 19 | SOURCE | 品号来源 | string(40) | Y |  |
| 20 | PLM_DATAKEY | PLM传输批次号 | string(80) | Y |  |
| 21 | LIMIT_CONTROL | 允限销管制品 | number(0/1) | Y |  |
| 22 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 47 | Attachments | 附件 | string | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_SERVICE (品号\品类服务信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_SERVICE_ID | 主键 | GUID | Y | Y |
| 4 | TYPE | 类别 | string(40) | Y |  |
| 5 | SERVICE_CATEGORY_ID | 服务品类 | GUID | Y |  |
| 6 | ITEM_ID | 服务品号 | GUID | Y |  |
| 7 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 8 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 9 | AREA_SETTING | 按区域设置服务信息 | number(0/1) | Y |  |
| 10 | AS_SN | 序号管理 | number(0/1) | Y |  |
| 11 | MAIN_ITEM | 服务主件 | number(0/1) | Y |  |
| 12 | PARTS_ITEM | 服务配件 | number(0/1) | Y |  |
| 13 | RETURN_ITEM | 旧件返回 | number(0/1) | Y |  |
| 14 | GUARANTEE_MONTH1 | 无偿保修月数 | number | Y |  |
| 15 | GUARANTEE_MONTH2 | 有偿保修月数 | number | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | SERVICE_CENTER_ID | 默认服务域 | GUID | Y |  |
| 18 | ITEM_CATEGORY_ID | 品号关联服务品类 | GUID | Y |  |
| 19 | CATEGORY_SETTING | 服务信息设置以服务品类为准 | number(0/1) | Y |  |
| 20 | SALES_ISSUE_UPDATE | 销货出库更新保修期 | number(0/1) | Y |  |
| 21 | SALES_SIGN_UPDATE | 销货签收更新保修期 | number(0/1) | Y |  |
| 22 | INST_UPDATE | 安装调试更新保修期 | number(0/1) | Y |  |
| 23 | ACCE_UPDATE | 安装验收更新保修期 | number(0/1) | Y |  |
| 24 | SALE_AUTO_SN | 销货出库更新产品档案 | number(0/1) | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 32 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 33 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 34 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 35 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 36 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 37 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 38 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 39 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 40 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 41 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 42 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 43 | UDF041 | 自定义字段12 | date | Y |  |
| 44 | UDF042 | 自定义字段13 | date | Y |  |
| 45 | UDF051 | 自定义字段14 | GUID | Y |  |
| 46 | UDF052 | 自定义字段15 | GUID | Y |  |
| 47 | UDF053 | 自定义字段16 | GUID | Y |  |
| 48 | UDF054 | 自定义字段17 | GUID | Y |  |
| 49 | Attachments | 附件 | string | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | Owner_Org_RTK |  | string(400) | Y |  |
| 56 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_SERVICE_AREA (品号\品类服务信息--区域单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_SERVICE_AREA_ID | 主键 | GUID | Y | Y |
| 2 | CUSTOMER_AREA_ID | 区域 | GUID | Y |  |
| 3 | GUARANTEE_MONTH1 | 无偿保修月数 | number | Y |  |
| 4 | GUARANTEE_MONTH2 | 有偿保修月数 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SERVICE_CENTER_ID | 默认服务域 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | ITEM_SERVICE_ID |  | GUID | Y |  |


### ITEM_SORT_VARIABLE (品号变量分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_SORT_VARIABLE_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
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
| 23 | Attachments | 附件 | string | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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


### ITEM_SORT_VARIABLE_D (品号变量分类单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_SORT_VARIABLE_D_ID | 主键 | GUID | Y | Y |
| 3 | SORT_NAME | 分类名称 | string(120) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | VARIABLE_ID | 属性 | GUID | Y |  |
| 6 | PREDEFINE_ITEM_SPEC | 默认规格 | number(0/1) | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
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
| 35 | ITEM_SORT_VARIABLE_ID |  | GUID | Y |  |


### ITEM_STRI_DEGREE (宽严程度)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_STRI_DEGREE_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
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
| 23 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 26 | ApproveDate | 修改日期 | date | Y |  |
| 27 | ApproveBy | 修改人 | GUID | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
| 35 | Owner_Org_RTK |  | string(400) | Y |  |
| 36 | Owner_Org_ROid |  | GUID | Y |  |
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |


### ITEM_STRI_DEGREE_D (宽严程度明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_STRI_DEGREE_D_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 4 | STRICTNESS_DEGREE | 宽严程度 | string(40) | Y |  |
| 5 | INSPECTION_RESULT | 检验记录 | string(60) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | ITEM_STRI_DEGREE_ID |  | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |


### ITEM_SUPPLIER (品号供应商信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_SUPPLIER_ID | 主键 | GUID | Y | Y |
| 2 | PRIORITY | 优先级 | number | Y |  |
| 3 | PURCHASE_RATE | 采购比例 | number(5,4) | Y |  |
| 4 | MAX_QUANTITY | 单笔最大采购量 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | LAST_INQUIRIES_DATE | 最近询价日 | date | Y |  |
| 7 | MAIN | 主要 | number(0/1) | Y |  |
| 8 | SUPPLIER_ID | 供应商 | GUID | Y |  |
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
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | ITEM_BUSINESS_ID |  | GUID | Y |  |


### ITEM_SUPPLIER_PRICE (品号供应商价格信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_SUPPLIER_PRICE_ID | 主键 | GUID | Y | Y |
| 4 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 5 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 6 | PRICE | 采购单价 | number(23,8) | Y |  |
| 7 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 8 | COMPONENT_PRICE | 分量计价 | number(0/1) | Y |  |
| 9 | APPROVAL_DATE | 核价日期 | date | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | PRICE_TYPE | 类型 | string(40) | Y |  |
| 12 | TAX_RATE |  | number(5,4) | Y |  |
| 13 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 14 | CURRENCY_ID | 币种 | GUID | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 17 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 18 | OPERATION_ID | 工艺 | GUID | Y |  |
| 19 | TAX_ID | 税种 | GUID | Y |  |
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
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_SUPPLIER_PRICE_D (品号供应商价格信息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ITEM_SUPPLIER_PRICE_D_ID | 主键 | GUID | Y | Y |
| 2 | BEGIN_QTY | 数量>= | number(16,6) | Y |  |
| 3 | END_QTY | 数量< | number(16,6) | Y |  |
| 4 | PRICE | 采购单价 | number(23,8) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
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
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | ITEM_SUPPLIER_PRICE_ID |  | GUID | Y |  |


### ITEM_TAX_CLASSIFICATION (存货/服务税分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_TAX_CLASSIFICATION_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_TAX_CLASSIFICATION_CODE | 存货/服务税分类编号 | string(6) | Y |  |
| 5 | ITEM_TAX_CLASSIFICATION_NAME | 存货/服务税分类名称 | string(60) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | TAX_REGION_ID | 税区 | GUID | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
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
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_TRANSFER (过户信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | ITEM_TRANSFER_ID | 主键 | GUID | Y | Y |
| 5 | SN_COMBINE_ID | 主件元件序列号结合主键 | GUID | Y |  |
| 6 | TRANSFER_DATE | 过户日期 | date | Y |  |
| 7 | ORIGINAL_CUSTOMEN_ID | 原客户编号 | GUID | Y |  |
| 8 | NEW_CUSTOMER_ID | 新客户编号 | GUID | Y |  |
| 9 | ORIG_EXPIRY_DATE | 原保修截止日期 | date | Y |  |
| 10 | NEW_EXPIRY_DATE | 新保修截止日期 | date | Y |  |
| 11 | ORIG_EXPIRY_DATE2 | 原有偿保修截止日期 | date | Y |  |
| 12 | NEW_EXPIRY_DATE2 | 新有偿保修截止日期 | date | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
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
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |


### ITEM_UNITS_CONVERSION (通用品号单位换算信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | QTY_BU | 库存单位数量 | number(16,6) | Y |  |
| 2 | QTY_CBU | 换算单位数量 | number(16,6) | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | ITEM_UNITS_CONVERSION_ID | 主键 | GUID | Y | Y |
| 5 | BASE_UNIT_ID | 库存单位 | GUID | Y |  |
| 6 | CONVERSION_UNIT_ID | 换算单位 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 35 | ITEM_BUSINESS_ID |  | GUID | Y |  |


### ITEM_WAREHOUSE (品号仓库信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_WAREHOUSE_ID | 主键 | GUID | Y | Y |
| 4 | ORIGINIAL_RECEIPT_DATE | 首次入库日 | date | Y |  |
| 5 | LAST_RECEIPT_DATE | 最后入库日 | date | Y |  |
| 6 | LAST_ISSUE_DATE | 最后出库日 | date | Y |  |
| 7 | SAFE_STOCK | 安全存量 | number(16,6) | Y |  |
| 8 | REORDER_POINT | 补货点 | number(16,6) | Y |  |
| 9 | ECONOMIC_ORDER_QTY | 经济批量 | number(16,6) | Y |  |
| 10 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 11 | STANDARD_INVENTORY | 标准存货量 | number(16,6) | Y |  |
| 12 | STANDARD_TURNOVER_RATE | 标准周转率 | number(5,4) | Y |  |
| 13 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 17 | BIN_ID | 主要库位 | GUID | Y |  |
| 18 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 19 | MAX_STOCK | 最高存量 | number(16,6) | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 44 | Attachments | 附件 | string | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |


### ITEM_WAREHOUSE_BIN (存货余额明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ITEM_WAREHOUSE_BIN_ID | 主键 | GUID | Y | Y |
| 4 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 5 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | LAST_COUNT_DATE | 上次盘点日 | date | Y |  |
| 7 | LAST_RECEIPT_DATE | 最后入库日 | date | Y |  |
| 8 | LAST_ISSUE_DATE | 最后出库日 | date | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 12 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 13 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 14 | BIN_ID | 库位 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |
| 47 | BO_ID_RTK |  | string(400) | Y |  |
| 48 | BO_ID_ROid |  | GUID | Y |  |
