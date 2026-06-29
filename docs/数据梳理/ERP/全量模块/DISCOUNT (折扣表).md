---
module: "DISCOUNT"
name_zh: "折扣表"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 171
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# DISCOUNT (折扣表)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 171

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


- **DISCOUNT_TABLE (折扣表)**
- **DISCOUNT_TABLE_CUSTOMER (折扣表客户)**
- **DISCOUNT_TABLE_D (折扣表品号折扣设置)**
- **DISCOUNT_TABLE_SD (折扣表分量计折)**


---


---


> Tables: 4

### DISCOUNT_TABLE (折扣表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DISCOUNT_TABLE_ID | 主键 | GUID | Y | Y |
| 4 | DISCOUNT_TABLE_CODE | 折扣表编号 | string(40) | Y |  |
| 5 | DISCOUNT_TABLE_NAME | 折扣表名称 | string(240) | Y |  |
| 6 | DISCOUNT_TYPE | 折扣类型 | string(40) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | TAX_ID | 税种 | GUID | Y |  |
| 9 | CURRENCY_ID | 币种 | GUID | Y |  |
| 10 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |

### DISCOUNT_TABLE_CUSTOMER (折扣表客户)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DISCOUNT_TABLE_CUSTOMER_ID |  | GUID | Y | Y |
| 3 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 4 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 5 | DISCOUNT |  | number(5,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CUST_FEATURE_VALUE1 | 客户属性值1 | string(80) | Y |  |
| 8 | CUST_FEATURE_VALUE2 | 客户属性值2 | string(80) | Y |  |
| 9 | CUST_FEATURE_VALUE3 | 客户属性值3 | string(80) | Y |  |
| 10 | CUST_FEATURE_VALUE4 | 客户属性值4 | string(80) | Y |  |
| 11 | CUST_FEATURE_VALUE5 | 客户属性值5 | string(80) | Y |  |
| 12 | CUST_FEATURE_VALUE6 | 客户属性值6 | string(80) | Y |  |
| 13 | CUSTOMER_FEATURE1_ID | 客户属性项1 | GUID | Y |  |
| 14 | CUSTOMER_FEATURE2_ID | 客户属性项2 | GUID | Y |  |
| 15 | CUSTOMER_FEATURE3_ID | 客户属性项3 | GUID | Y |  |
| 16 | CUSTOMER_FEATURE4_ID | 客户属性项4 | GUID | Y |  |
| 17 | CUSTOMER_FEATURE5_ID | 客户属性项5 | GUID | Y |  |
| 18 | CUSTOMER_FEATURE6_ID | 客户属性项6 | GUID | Y |  |
| 19 | CUSTOMER_ID | 客户 | GUID | Y |  |
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
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | DISCOUNT_TABLE_ID |  | GUID | Y |  |

### DISCOUNT_TABLE_D (折扣表品号折扣设置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DISCOUNT_TABLE_D_ID |  | GUID | Y | Y |
| 2 | ITEM_NAME |  | string(120) | Y |  |
| 3 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 4 | DISCOUNT |  | number(5,4) | Y |  |
| 5 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 6 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 7 | COMPONENT_DISCOUNT | 分量计折 | number(0/1) | Y |  |
| 8 | DEFINED_DISCOUNT | 可自定折扣 | number(0/1) | Y |  |
| 9 | UPPER_DISCOUNT | 上限折扣 | number(5,4) | Y |  |
| 10 | LOWER_DISCOUNT | 下限折扣 | number(5,4) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | FEATURE_VALUE | 品号属性值 | string(40) | Y |  |
| 13 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 14 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 15 | ITEM_ID | 品号 | GUID | Y |  |
| 16 | FEATURE_ID | 品号属性项 | GUID | Y |  |
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
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | DISCOUNT_TABLE_ID |  | GUID | Y |  |

### DISCOUNT_TABLE_SD (折扣表分量计折)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DISCOUNT_TABLE_SD_ID |  | GUID | Y | Y |
| 2 | BEGIN_QTY | 数量>= | number(16,6) | Y |  |
| 3 | END_QTY | 数量< | number(16,6) | Y |  |
| 4 | DISCOUNT |  | number(5,4) | Y |  |
| 5 | DEFINED_DISCOUNT | 可自定折扣 | number(0/1) | Y |  |
| 6 | UPPER_DISCOUNT | 上限折扣 | number(5,4) | Y |  |
| 7 | LOWER_DISCOUNT | 下限折扣 | number(5,4) | Y |  |
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
| 37 | DISCOUNT_TABLE_D_ID |  | GUID | Y |  |