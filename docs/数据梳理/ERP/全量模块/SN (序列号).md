---
module: "SN"
name_zh: "序列号"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 11
columns: 525
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# SN (序列号)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 11 | Columns: 525

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]

---

## Tables


- **SN_COMBINE (主件元件序列号结合)**
- **SN_COMBINE_D (主件元件序列号结合明细)**
- **SN_ITEM_RECORD (品号序列号记录档)**
- **SN_ITEM_RECORD_MAX (品号序列号最大记录档)**
- **SN_PACK_RECORD (箱号序列号记录档)**
- **SN_PACK_RECORD_MAX (箱号序列号最大记录档)**
- **SN_PICK_CONFIRM**
- **SN_PICK_CONFIRM_D**
- **SN_PICK_CONFIRM_SD**
- **SN_TRANSACTION_LINE (品号序列号交易记录)**
- **SN_WS (采集点信息)**


---


---


> Tables: 11

### SN_COMBINE (主件元件序列号结合)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SN_COMBINE_ID | 主键 | GUID | Y | Y |
| 4 | FG_ID | 成品识别码 | string(510) | Y |  |
| 5 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 6 | MAIN_SN | 主件序列号 | string(510) | Y |  |
| 7 | REWORK_TIMES | 重工次数 | number | Y |  |
| 8 | PLANT_ID | 工厂 | GUID | Y |  |
| 9 | MO_ID | 工单 | GUID | Y |  |
| 10 | SALES_ORDER_DOC_D_ID | 订单 | GUID | Y |  |
| 11 | SALES_DELIVERY_D_ID | 销货单 | GUID | Y |  |
| 12 | SALES_ISSUE_D_ID | 销货出库单 | GUID | Y |  |
| 13 | SALES_RETURN_D_ID | 销退单 | GUID | Y |  |
| 14 | SALES_RETURN_RECEIPT_D_ID | 销退入库单 | GUID | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 17 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 18 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 19 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 20 | DOC_DATE | 单据日期 | date | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | LOT_CODE | 批号 | string(60) | Y |  |
| 23 | LOT_DESCRIPTION | 批号说明 | string(120) | Y |  |
| 24 | INSTALLATION_DATE | 安装调试日期 | date | Y |  |
| 25 | ACCEPTANCE_DATE | 安装调试验收日期 | date | Y |  |
| 26 | EXPIRY_DATE | 保修截止日期 | date | Y |  |
| 27 | EXPIRY_DATE2 | 有偿保修截止日期 | date | Y |  |
| 28 | ORIG_EXPIRY_DATE | 原保修截止日期 | date | Y |  |
| 29 | ORIG_EXPIRY_DATE2 | 原有偿保修截止日期 | date | Y |  |
| 30 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 31 | LOCATION | 使用地点 | string(510) | Y |  |
| 32 | PERIOD_TYPE | 维护周期类型 | string(40) | Y |  |
| 33 | BEGIN_DATE | 维护开始日期 | date | Y |  |
| 34 | SERVICE_PERIOD_ID | 维护周期编号 | GUID | Y |  |
| 35 | NEXT_DATE | 下次维护日期 | date | Y |  |
| 36 | ACT_SERVICE_TIMES | 实际维护次数 | number | Y |  |
| 37 | SERVICE_CENTER_ID | 默认服务域 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | CreateDate | 创建日期 | date | Y |  |
| 58 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 59 | ModifiedDate | 修改日期 | date | Y |  |
| 60 | CreateBy | 创建者 | GUID | Y |  |
| 61 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 62 | ModifiedBy | 修改者 | GUID | Y |  |
| 63 | Attachments | 附件 | string | Y |  |
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |
| 68 | Owner_Org_RTK |  | string(400) | Y |  |
| 69 | Owner_Org_ROid |  | GUID | Y |  |
| 70 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 71 | SOURCE_ID_ROid |  | GUID | Y |  |

### SN_COMBINE_D (主件元件序列号结合明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SUB_SN | 元件序列号 | string(510) | Y |  |
| 3 | ITEM_ID | 元件品号ID | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 元件品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 元件规格 | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 元件特征码ID | GUID | Y |  |
| 7 | ITEM_LOT_ID | 批号ID | GUID | Y |  |
| 8 | LOT_CODE | 批号 | string(60) | Y |  |
| 9 | LOT_DESCRIPTION | 批号说明 | string(120) | Y |  |
| 10 | STATUS | 生失效状态 | string(40) | Y |  |
| 11 | OP_DATETIME | 操作时间 | date | Y |  |
| 12 | FG_ID | 成品识别码 | string(510) | Y |  |
| 13 | UPLEVEL_CODE | 上阶层级码 | string(200) | Y |  |
| 14 | LEVEL_CODE | 本阶层级码 | string(200) | Y |  |
| 15 | INVENTORY_QTY | 库存单位用量 | number(16,6) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | SN_COMBINE_D_ID | 主键 | GUID | Y | Y |
| 18 | COMBINE_WS_ID | 元件采集点 | GUID | Y |  |
| 19 | REWORK_TIMES | 重工次数 | number | Y |  |
| 20 | SERVICE_SITE_ID | 服务站点 | GUID | Y |  |
| 21 | EXPIRY_DATE | 保修截止日期 | date | Y |  |
| 22 | EXPIRY_DATE2 | 有偿保修截止日期 | date | Y |  |
| 23 | ORIG_EXPIRY_DATE | 原保修截止日期 | date | Y |  |
| 24 | ORIG_EXPIRY_DATE2 | 原有偿保修截止日期 | date | Y |  |
| 25 | UPDATE | 更新日期 | date | Y |  |
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
| 56 | SN_COMBINE_ID |  | GUID | Y |  |

### SN_ITEM_RECORD (品号序列号记录档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SN_ITEM_RECORD_ID | 主键 | GUID | Y | Y |
| 4 | SN_NO | 序列号 | string(510) | Y |  |
| 5 | BC_REG_ID | 条码编码规则ID | GUID | Y |  |
| 6 | ITEM_ID | 品号 | GUID | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 9 | BIN_ID | 库位 | GUID | Y |  |
| 10 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 11 | STOCK_ACTION | 入出别 | number | Y |  |
| 12 | GENERATE_TYPE | 生成方式 | string(40) | Y |  |
| 13 | GENERATE_DATE | 生成日期 | date | Y |  |
| 14 | LABEL_LAYOUT | 标签样式 | string(400) | Y |  |
| 15 | PRINT_TIMES | 打印次数 | number | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | PROPERTY_CUSTOM | 自定义属性 | string(8000) | Y |  |
| 18 | PROPERTY_SYS_ITEM_CODE | 属性项-品号 | string(400) | Y |  |
| 19 | PROPERTY_SYS_ITEM_FEATURE | 属性项-特征码 | string(400) | Y |  |
| 20 | PROPERTY_SYS_LOT | 属性项-批号 | string(400) | Y |  |
| 21 | PROPERTY_SYS_INV_UNIT | 属性项-库存单位 | string(400) | Y |  |
| 22 | PROPERTY_SYS_INV_QTY | 属性项-库存单位数量 | string(400) | Y |  |
| 23 | PROPERTY_SYS_CONSTANT | 属性项-常量 | string(400) | Y |  |
| 24 | PROPERTY_SYS_YEAR | 属性项-年 | string(400) | Y |  |
| 25 | PROPERTY_SYS_MONTH | 属性项-月 | string(400) | Y |  |
| 26 | PROPERTY_SYS_DAY | 属性项-日 | string(400) | Y |  |
| 27 | PROPERTY_SYS_SN | 流水号 | string(400) | Y |  |
| 28 | PLANT_ID | 工厂 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Attachments | 附件 | string | Y |  |
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
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |
| 61 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 62 | SOURCE_ID_ROid |  | GUID | Y |  |

### SN_ITEM_RECORD_MAX (品号序列号最大记录档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SN_ITEM_RECORD_MAX_ID | 主键 | GUID | Y | Y |
| 2 | PREFIX | 前缀 | string(510) | Y |  |
| 3 | SUFFIX | 后缀 | string(510) | Y |  |
| 4 | MAX_SN | 最大流水号 | number | Y |  |
| 5 | BC_REG_ID | 条码编码规则ID | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
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

### SN_PACK_RECORD (箱号序列号记录档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SN_PACK_RECORD_ID | 主键 | GUID | Y | Y |
| 4 | SN_NO | 序列号 | string(510) | Y |  |
| 5 | BC_REG_ID | 条码编码规则ID | GUID | Y |  |
| 6 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 7 | BIN_ID | 库位 | GUID | Y |  |
| 8 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 9 | GENERATE_TYPE | 生成方式 | string(40) | Y |  |
| 10 | GENERATE_DATE | 生成日期 | date | Y |  |
| 11 | LABEL_LAYOUT | 标签样式 | string(400) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PRINT_TIMES | 打印次数 | number | Y |  |
| 14 | PROPERTY_SYS_ITEM_CODE | 属性项-品号 | string(400) | Y |  |
| 15 | PROPERTY_SYS_ITEM_FEATURE | 属性项-特征码 | string(400) | Y |  |
| 16 | PROPERTY_SYS_LOT | 属性项-批号 | string(400) | Y |  |
| 17 | PROPERTY_SYS_INV_UNIT | 属性项-库存单位 | string(400) | Y |  |
| 18 | PROPERTY_SYS_INV_QTY | 属性项-库存单位数量 | string(400) | Y |  |
| 19 | PROPERTY_SYS_CONSTANT | 属性项-常量 | string(400) | Y |  |
| 20 | PROPERTY_SYS_YEAR | 属性项-年 | string(400) | Y |  |
| 21 | PROPERTY_SYS_MONTH | 属性项-月 | string(400) | Y |  |
| 22 | PROPERTY_SYS_DAY | 属性项-日 | string(400) | Y |  |
| 23 | PROPERTY_SYS_SN | 流水号 | string(400) | Y |  |
| 24 | PROPERTY_CUSTOM | 自定义属性 | string(8000) | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Attachments | 附件 | string | Y |  |
| 32 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 33 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 34 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 35 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 36 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 37 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 38 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 39 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 40 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 41 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 42 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 43 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 44 | UDF041 | 自定义字段12 | date | Y |  |
| 45 | UDF042 | 自定义字段13 | date | Y |  |
| 46 | UDF051 | 自定义字段14 | GUID | Y |  |
| 47 | UDF052 | 自定义字段15 | GUID | Y |  |
| 48 | UDF053 | 自定义字段16 | GUID | Y |  |
| 49 | UDF054 | 自定义字段17 | GUID | Y |  |
| 50 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | Owner_Org_RTK |  | string(400) | Y |  |
| 56 | Owner_Org_ROid |  | GUID | Y |  |
| 57 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 58 | SOURCE_ID_ROid |  | GUID | Y |  |

### SN_PACK_RECORD_MAX (箱号序列号最大记录档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SN_PACK_RECORD_MAX_ID | 主键 | GUID | Y | Y |
| 2 | PREFIX | 前缀 | string(400) | Y |  |
| 3 | SUFFIX | 后缀 | string(400) | Y |  |
| 4 | MAX_SN | 最大流水号 | number | Y |  |
| 5 | BC_REG_ID | 条码编码规则ID | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
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

### SN_PICK_CONFIRM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SN_PICK_CONFIRM_ID | 主键 | GUID | Y | Y |
| 4 | DOC_NO | 来源单号 | string(400) | Y |  |
| 5 | SequenceNumber | 来源序号 | string(400) | Y |  |
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
| 24 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 38 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 39 | SOURCE_ID_ROid |  | GUID | Y |  |
| 40 | SOURCE_D_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_D_ID_ROid |  | GUID | Y |  |

### SN_PICK_CONFIRM_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SN_PICK_CONFIRM_D_ID |  | GUID | Y | Y |
| 3 | CURRENT_SCANED_QTY | 本次扫描数量 | number(16,6) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | INV_QTY | 库存数量 | number(16,6) | Y |  |
| 7 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 8 | BIN_ID | 库位 | GUID | Y |  |
| 9 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 10 | SCAN_QTY | 累计已扫描数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ITEM_NAME | 品名 | string(120) | Y |  |
| 13 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 14 | SEQ | 来源明细序号 | number | Y |  |
| 15 | STOCK_TYPE | 出入库别 | number | Y |  |
| 16 | DOC_ID | 来源单据性质 | GUID | Y |  |
| 17 | CATEGORY | 来源单据类型 | string(400) | Y |  |
| 18 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 19 | TO_BIN_ID | 转入库位 | GUID | Y |  |
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
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | SOURCE_D_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_D_ID_ROid |  | GUID | Y |  |
| 47 | SN_PICK_CONFIRM_ID |  | GUID | Y |  |

### SN_PICK_CONFIRM_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SN_PICK_CONFIRM_SD_ID |  | GUID | Y | Y |
| 3 | ITEM_SN_NO | 品号序列号 | string(510) | Y |  |
| 4 | PACK_SN_NO | 箱号序列号 | string(510) | Y |  |
| 5 | NOT_SYS_SNNO | 非系统中的序列号 | number(0/1) | Y |  |
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
| 31 | SN_PICK_CONFIRM_D_ID |  | GUID | Y |  |

### SN_TRANSACTION_LINE (品号序列号交易记录)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SN_TRANSACTION_LINE_ID | 主键 | GUID | Y | Y |
| 4 | SN_NO | 序列号 | string(510) | Y |  |
| 5 | CATEGORY | 单据性质 | string(40) | Y |  |
| 6 | DOC_NO | 来源单号 | string(40) | Y |  |
| 7 | SEQUENCE_NO | 来源序号 | number | Y |  |
| 8 | STOCK_ACTION | 入出别 | number | Y |  |
| 9 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 12 | DOC_ID | 单据类型 | GUID | Y |  |
| 13 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 14 | BIN_ID | 库位 | GUID | Y |  |
| 15 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 16 | PLANT_ID | 工厂 | GUID | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |

### SN_WS (采集点信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SN_WS_ID | 主键 | GUID | Y | Y |
| 4 | WS_CODE | 采集点编号 | string(20) | Y |  |
| 5 | WS_NAME | 采集点名称 | string(40) | Y |  |
| 6 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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