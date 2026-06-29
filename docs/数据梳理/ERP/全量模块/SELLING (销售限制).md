---
module: "SELLING"
name_zh: "销售限制"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 195
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# SELLING (销售限制)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 5 | Columns: 195

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


- **SELLING_LIMIT**
- **SELLING_LIMIT_ITEM**
- **SELLING_LIMIT_LOT**
- **SELLING_LIMIT_PARTNER**
- **SELLING_LIMIT_STAFF**


---


---


> Tables: 5

### SELLING_LIMIT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SELLING_LIMIT_ID | 主键 | GUID | Y | Y |
| 4 | SELLING_LIMIT_CODE | 允限销方案编号 | string(20) | Y |  |
| 5 | SELLING_LIMIT_NAME | 允限销方案名称 | string(80) | Y |  |
| 6 | DOC_DATE | 建立日期 | date | Y |  |
| 7 | LIMIT_CATEGORY | 允限销类别 | string(40) | Y |  |
| 8 | LIMIT_PARTNER | 允限销对象 | string(40) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | LIMIT_TYPE | 允限销类型 | string(40) | Y |  |
| 11 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 12 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 31 | Attachments | 附件 | string | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### SELLING_LIMIT_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SELLING_LIMIT_ITEM_ID | 主键 | GUID | Y | Y |
| 3 | FEATURE_VALUE | 品号属性值 | string(120) | Y |  |
| 4 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | FEATURE_ID | 品号属性项 | GUID | Y |  |
| 8 | ITEM_ID | 品号 | GUID | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
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
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SELLING_LIMIT_ID |  | GUID | Y |  |

### SELLING_LIMIT_LOT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SELLING_LIMIT_LOT_ID | 主键 | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 4 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 5 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 6 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 7 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 8 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 9 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 10 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 11 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 12 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 13 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 14 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 15 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 16 | UDF041 | 自定义字段12 | date | Y |  |
| 17 | UDF042 | 自定义字段13 | date | Y |  |
| 18 | UDF051 | 自定义字段14 | GUID | Y |  |
| 19 | UDF052 | 自定义字段15 | GUID | Y |  |
| 20 | UDF053 | 自定义字段16 | GUID | Y |  |
| 21 | UDF054 | 自定义字段17 | GUID | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | SELLING_LIMIT_ITEM_ID |  | GUID | Y |  |

### SELLING_LIMIT_PARTNER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SELLING_LIMIT_PARTNER_ID | 主键 | GUID | Y | Y |
| 3 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 4 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | BP_PROPERTY_VALUE1 | 客户属性值1 | string(80) | Y |  |
| 7 | BP_PROPERTY_VALUE2 | 客户属性值2 | string(80) | Y |  |
| 8 | BP_PROPERTY_VALUE3 | 客户属性值3 | string(80) | Y |  |
| 9 | BP_PROPERTY_VALUE4 | 客户属性值4 | string(80) | Y |  |
| 10 | BP_PROPERTY_VALUE5 | 客户属性值5 | string(80) | Y |  |
| 11 | BP_PROPERTY_VALUE6 | 客户属性值6 | string(80) | Y |  |
| 12 | BP_PROPERTY1_ID | 客户属性项1 | GUID | Y |  |
| 13 | BP_PROPERTY2_ID | 客户属性项2 | GUID | Y |  |
| 14 | BP_PROPERTY3_ID | 客户属性项3 | GUID | Y |  |
| 15 | BP_PROPERTY4_ID | 客户属性项4 | GUID | Y |  |
| 16 | BP_PROPERTY5_ID | 客户属性项5 | GUID | Y |  |
| 17 | BP_PROPERTY6_ID | 客户属性项6 | GUID | Y |  |
| 18 | CUSTOMER_ID | 客户 | GUID | Y |  |
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
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | SELLING_LIMIT_ID |  | GUID | Y |  |

### SELLING_LIMIT_STAFF

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SELLING_LIMIT_PARTNER_ID | 主键 | GUID | Y | Y |
| 2 | EMPLOYEE_ID | 业务员 | GUID | Y |  |
| 3 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 4 | INEFFECTIVE_DATE | 失效日期 | date | Y |  |
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
| 34 | SELLING_LIMIT_ID |  | GUID | Y |  |