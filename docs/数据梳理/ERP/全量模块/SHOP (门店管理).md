---
module: "SHOP"
name_zh: "门店管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 18
columns: 787
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# SHOP (门店管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 18 | Columns: 787

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]

---

## Tables


- **SHOP_DAY_END (门店日结档)**
- **SHOP_DAY_END_D (门店日结档单身)**
- **SHOP_DAY_END_INV (门店日结档库存单身)**
- **SHOP_DAY_END_INV2 (日结品号仓库信息)**
- **SHOP_DAY_END_LINE (交易明细信息)**
- **SHOP_DAY_END_LINE_D (交易明细单身)**
- **SHOP_DAY_SALE (门店日销售单)**
- **SHOP_DAY_SALE_D**
- **SHOP_EMPLOYEE**
- **SHOP_EMPLOYEE_D**
- **SHOP_FLOOR_ACTION_LOG (维护工艺操作记录)**
- **SHOP_GROUP (门店组信息)**
- **SHOP_ITEM**
- **SHOP_ITEM_D**
- **SHOP_LEVEL**
- **SHOP_SALE_PAYTYPE**
- **SHOP_SALE_PAYTYPE_D**


---


---


> Tables: 18

### SHOP (门店基本信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_ID | 主键 | GUID | Y | Y |
| 4 | SHOP_CODE | 门店编号 | string(80) | Y |  |
| 5 | SHOP_NAME | 门店名称 | string(200) | Y |  |
| 6 | SHOP_TYPE | 门店属性 | string(40) | Y |  |
| 7 | EMPLOYEE_COUNT | 员工数 | number | Y |  |
| 8 | CONSTRACTION_AREA | 建筑面积 | number(12,2) | Y |  |
| 9 | WORK_AREA | 营业面积 | number(12,2) | Y |  |
| 10 | SHOW_AREA | 陈列面积 | number(12,2) | Y |  |
| 11 | BEGIN_DATE | 开业日期 | date | Y |  |
| 12 | END_DATE | 停业日期 | date | Y |  |
| 13 | MANAGER | 负责人 | string(40) | Y |  |
| 14 | CONTACT | 联系人 | string(40) | Y |  |
| 15 | TELEPHONE | 联系电话 | string(40) | Y |  |
| 16 | FAX | 传真 | string(40) | Y |  |
| 17 | EMAIL | 电子邮箱 | string(100) | Y |  |
| 18 | POSTCODE | 邮编 | string(20) | Y |  |
| 19 | ADDRESS | 地址 | string(200) | Y |  |
| 20 | SELF_DILIVER_RATE | 本店发货定金比例 | number(5,4) | Y |  |
| 21 | OTHER_DILIVER_RATE | 他店发货定金比例 | number(5,4) | Y |  |
| 22 | STORE_DILIVER_RATE | 仓库发货定金比例 | number(5,4) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | SHOP_GROUP_ID1 | 主键 | GUID | Y |  |
| 25 | SHOP_GROUP_ID2 | 主键 | GUID | Y |  |
| 26 | SHOP_LEVEL | 主键 | GUID | Y |  |
| 27 | AREA_ID | 地区 | GUID | Y |  |
| 28 | PROVINCE_ID | 省份 | GUID | Y |  |
| 29 | CITY_ID | 城市 | GUID | Y |  |
| 30 | RANGE_ID | 区/县 | GUID | Y |  |
| 31 | MARKET_ID | 入驻商场 | GUID | Y |  |
| 32 | BUSINESS_CIRCLE_ID | 商圈 | GUID | Y |  |
| 33 | COMPANY_ID | 所属公司 | GUID | Y |  |
| 34 | PLANT_ID | 上级储运机构 | GUID | Y |  |
| 35 | SALE_PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 36 | EXPENSES_TO | 费用归属 | string(40) | Y |  |
| 37 | EXPENSE_ID | 费用编号 | GUID | Y |  |
| 38 | EXPENSE_COMPANY_ID |  | GUID | Y |  |
| 39 | COST_DOMAIN_ID | 成本域 | GUID | Y |  |
| 40 | NEWSHOP | 是否新开店 | number(0/1) | Y |  |
| 41 | SN | 排序号 | number | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | Attachments | 附件 | string | Y |  |
| 49 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 50 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 51 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 52 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 53 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 54 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 55 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 56 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 57 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 58 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 59 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 60 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 61 | UDF041 | 自定义字段12 | date | Y |  |
| 62 | UDF042 | 自定义字段13 | date | Y |  |
| 63 | UDF051 | 自定义字段14 | GUID | Y |  |
| 64 | UDF052 | 自定义字段15 | GUID | Y |  |
| 65 | UDF053 | 自定义字段16 | GUID | Y |  |
| 66 | UDF054 | 自定义字段17 | GUID | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |

### SHOP_DAY_END (门店日结档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_DAY_END_ID | 主键 | GUID | Y | Y |
| 4 | DAY_END_DATE | 日结日期 | date | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SHOP_ID | 门店 | GUID | Y |  |
| 7 | POS_ID | POS机 | GUID | Y |  |
| 8 | DAY_END_FLAG | 日结标志 | number(0/1) | Y |  |
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

### SHOP_DAY_END_D (门店日结档单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOP_DAY_END_D_ID |  | GUID | Y | Y |
| 3 | DAY_END_DATE | 日结日期 | date | Y |  |
| 4 | DATA_TYPE | 数据类型 | string(200) | Y |  |
| 5 | DATA_NAME | 数据名称 | string(200) | Y |  |
| 6 | DATA_COUNT | 笔数 | number | Y |  |
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
| 33 | SHOP_DAY_END_ID |  | GUID | Y |  |

### SHOP_DAY_END_INV (门店日结档库存单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | ITEM_WAREHOUSE_BIN_ID | 品号 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 8 | BIN_ID | 库位 | GUID | Y |  |
| 9 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 10 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 11 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | LAST_COUNT_DATE | 上次盘点日 | date | Y |  |
| 14 | LAST_RECEIPT_DATE | 最后入库日 | date | Y |  |
| 15 | LAST_ISSUE_DATE | 最后出库日 | date | Y |  |
| 16 | SHOP_DAY_END_INV_ID |  | GUID | Y | Y |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |
| 44 | BO_ID_RTK |  | string(400) | Y |  |
| 45 | BO_ID_ROid |  | GUID | Y |  |
| 46 | SHOP_DAY_END_ID |  | GUID | Y |  |

### SHOP_DAY_END_INV2 (日结品号仓库信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | ITEM_WAREHOUSE_ID | 品号仓库 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 8 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 9 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 10 | ORIGINIAL_RECEIPT_DATE | 首次入库日 | date | Y |  |
| 11 | LAST_RECEIPT_DATE | 最后入库日 | date | Y |  |
| 12 | LAST_ISSUE_DATE | 最后出库日 | date | Y |  |
| 13 | SAFE_STOCK | 安全存量 | number(16,6) | Y |  |
| 14 | REORDER_POINT | 补货点 | number(16,6) | Y |  |
| 15 | ECONOMIC_ORDER_QTY | 经济批量 | number(16,6) | Y |  |
| 16 | STANDARD_INVENTORY | 标准存货量 | number(16,6) | Y |  |
| 17 | STANDARD_TURNOVER_RATE | 标准周转率 | number(5,4) | Y |  |
| 18 | BIN_ID | 最近入库库位 | GUID | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | SHOP_DAY_END_INV2_ID |  | GUID | Y | Y |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |
| 48 | SHOP_DAY_END_ID |  | GUID | Y |  |

### SHOP_DAY_END_LINE (交易明细信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | DOC_NO | 单号 | string(40) | Y |  |
| 5 | DOC_DATE | 单据日期 | date | Y |  |
| 6 | DOC_ID | 单据类型 | GUID | Y |  |
| 7 | TRANSACTION_LINE_ID | 交易明细 | GUID | Y |  |
| 8 | SEQUENCE_NO | 来源序号 | number | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 11 | STOCK_ACTION | 影响库存 | number | Y |  |
| 12 | ITEM_ID | 品号 | GUID | Y |  |
| 13 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 14 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 15 | BIN_ID | 库位 | GUID | Y |  |
| 16 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 17 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 18 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 19 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 20 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | COMPANY_ID | 公司 | GUID | Y |  |
| 23 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 24 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 25 | COST_CODE | 成本码 | string(40) | Y |  |
| 26 | SOURCE_ID_RTK | 源单RTK | string(200) | Y |  |
| 27 | SOURCE_ID_ROID | 源单ROID | GUID | Y |  |
| 28 | REFERENCE_SOURCE_ID_RTK | 参考源单RTK | string(200) | Y |  |
| 29 | REFERENCE_SOURCE_ID_ROID | 参考源单ROID | GUID | Y |  |
| 30 | SHOP_DAY_END_LINE_ID |  | GUID | Y | Y |
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 38 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 39 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 40 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 41 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 42 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 43 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 44 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 45 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 46 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 47 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 48 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 49 | UDF041 | 自定义字段12 | date | Y |  |
| 50 | UDF042 | 自定义字段13 | date | Y |  |
| 51 | UDF051 | 自定义字段14 | GUID | Y |  |
| 52 | UDF052 | 自定义字段15 | GUID | Y |  |
| 53 | UDF053 | 自定义字段16 | GUID | Y |  |
| 54 | UDF054 | 自定义字段17 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |
| 58 | BO_ID_RTK |  | string(400) | Y |  |
| 59 | BO_ID_ROid |  | GUID | Y |  |
| 60 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 61 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 62 | SHOP_DAY_END_ID |  | GUID | Y |  |

### SHOP_DAY_END_LINE_D (交易明细单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | TRANSACTION_LINE_D_ID | 品号明细 | GUID | Y |  |
| 5 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 6 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 7 | COMPANY_ID | 公司 | GUID | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 11 | TRANSACTION_LINE_ID | 父主键 | GUID | Y |  |
| 12 | SHOP_DAY_END_LINE_D_ID |  | GUID | Y | Y |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |
| 40 | SHOP_DAY_END_ID |  | GUID | Y |  |

### SHOP_DAY_SALE (门店日销售单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SHOP_DAY_SALE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SHOP_ID | 门店 | GUID | Y |  |
| 9 | QTY | 数量 | number(16,6) | Y |  |
| 10 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 11 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 12 | SALT_TAX | 销项税 | number(23,8) | Y |  |
| 13 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 14 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 15 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | PrintCount | 打印次数 | number | Y |  |
| 18 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 19 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 20 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 21 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### SHOP_DAY_SALE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SHOP_DAY_SALE_D_ID | 主键 | GUID | Y | Y |
| 2 | SequenceNumber | 序号 | number | Y |  |
| 3 | ITEM_ID | 商品编码 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | COST_TAX_RATE | 进项税率 | number(5,4) | Y |  |
| 6 | SALE_TAX_RATE | 销项税率 | number(5,4) | Y |  |
| 7 | QTY | 数量 | number(16,6) | Y |  |
| 8 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 9 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 10 | SALT_TAX | 销项税 | number(23,8) | Y |  |
| 11 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 12 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 13 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 14 | PROM_AMT | 优惠额 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
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
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | SHOP_DAY_SALE_ID |  | GUID | Y |  |

### SHOP_EMPLOYEE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_EMPLOYEE_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Attachments | 附件 | string | Y |  |
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
| 30 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | Owner_Org_RTK |  | string(400) | Y |  |
| 36 | Owner_Org_ROid |  | GUID | Y |  |

### SHOP_EMPLOYEE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 2 | ApproveDate | 修改日期 | date | Y |  |
| 3 | ApproveBy | 修改人 | GUID | Y |  |
| 4 | SHOP_EMPLOYEE_D_ID | 主键 | GUID | Y | Y |
| 5 | EMPLOYEE_ID | 员工编号 | GUID | Y |  |
| 6 | SALES | 营业员 | number(0/1) | Y |  |
| 7 | CASHIER | 收银员 | number(0/1) | Y |  |
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
| 34 | SHOP_EMPLOYEE_ID |  | GUID | Y |  |

### SHOP_FLOOR_ACTION_LOG (维护工艺操作记录)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | SHOP_FLOOR_ACTION_LOG_ID | 主键 | GUID | Y | Y |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | QTY | 数量 | number(16,6) | Y |  |
| 7 | UNIT_ID | 单位 | GUID | Y |  |
| 8 | RELATION_MO_ROUTING_D_ID | 来源工单 | GUID | Y |  |
| 9 | ACTION_TYPE | 类型 | string(40) | Y |  |
| 10 | ACTION_DATE | 作业日期 | date | Y |  |
| 11 | MO_ROUTING_D_ID | 工单工艺 | GUID | Y |  |
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
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |
| 44 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 45 | SOURCE_ID_ROid |  | GUID | Y |  |
| 46 | RELATION_SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | RELATION_SOURCE_ID_ROid |  | GUID | Y |  |

### SHOP_GROUP (门店组信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | SHOP_GROUP_CODE | 门店组编号 | string(80) | Y |  |
| 5 | SHOP_GROUP_NAME | 门店组名称 | string(80) | Y |  |
| 6 | SHOP_GROUP_TYPE | 门店组类型 | string(40) | Y |  |
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

### SHOP_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | SHOP_ID | 门店 | GUID | Y |  |
| 5 | PLANT_ID | 主要储运机构 | GUID | Y |  |
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

### SHOP_ITEM_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SHOP_ITEM_D_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | SALE | 零售 | number(0/1) | Y |  |
| 4 | ORDER | 零售订单 | number(0/1) | Y |  |
| 5 | CALL | 可否要货 | number(0/1) | Y |  |
| 6 | KEEP_SAME | 与营运中心同步修改 | number(0/1) | Y |  |
| 7 | CALL_STRATEGY_ID | 要货策略 | GUID | Y |  |
| 8 | MIN_CALL_QTY | 最小要货量 | number(16,6) | Y |  |
| 9 | SUBMULTIPLE_QTY | 要货倍量 | number(16,6) | Y |  |
| 10 | KEEP_DAYS | 要货支持天数 | number | Y |  |
| 11 | CALL_POINT_QTY | 要货点 | number(16,6) | Y |  |
| 12 | EOQ | 要货经济批量 | number(16,6) | Y |  |
| 13 | BEST_STORE_QTY | 最优库存 | number(16,6) | Y |  |
| 14 | CALL_PERIOD | 要货周期码 | string(40) | Y |  |
| 15 | TAX_ID | 税种 | GUID | Y |  |
| 16 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 17 | PLANT_ID | 储运机构 | GUID | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | SHOP_ITEM_ID |  | GUID | Y |  |

### SHOP_LEVEL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_LEVEL_ID | 主键 | GUID | Y | Y |
| 4 | SHOP_LEVEL_CODE | 门店等级编号 | string(40) | Y |  |
| 5 | SHOP_LEVEL_NAME | 门店等级名称 | string(100) | Y |  |
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

### SHOP_SALE_PAYTYPE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOP_SALE_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Attachments | 附件 | string | Y |  |
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
| 30 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | Owner_Org_RTK |  | string(400) | Y |  |
| 36 | Owner_Org_ROid |  | GUID | Y |  |

### SHOP_SALE_PAYTYPE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SHOP_SALE_PAYTYPE_D_ID | 主键 | GUID | Y | Y |
| 2 | SALE_PAYTYPE_ID | 收款方式ID | GUID | Y |  |
| 3 | ALLOW_SALE | 能否用于销售 | number(0/1) | Y |  |
| 4 | ALLOW_RET | 能否用于退货 | number(0/1) | Y |  |
| 5 | ALLOW_RECHARGE | 能否用于充值 | number(0/1) | Y |  |
| 6 | ALLOW_SALE_CARD | 能否用于售卡 | number(0/1) | Y |  |
| 7 | ALLOW_SALE_TICKET | 能否用于售券 | number(0/1) | Y |  |
| 8 | ALOW_OTHER_CHARGEIN | 用于杂收 | number(0/1) | Y |  |
| 9 | ALOW_OTHER_CHARGEOUT | 用于杂支 | number(0/1) | Y |  |
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
| 36 | SHOP_SALE_PAYTYPE_ID |  | GUID | Y |  |