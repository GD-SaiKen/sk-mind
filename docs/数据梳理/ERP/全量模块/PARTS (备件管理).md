---
module: "PARTS"
name_zh: "备件管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 150
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# PARTS (备件管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 150

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


- **PARTS_PRICE**
- **PARTS_TRANSFER_DOC**
- **PARTS_TRANSFER_DOC_D**


---


---


> Tables: 3

### PARTS_PRICE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARTS_PRICE_ID | 主键 | GUID | Y | Y |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | CURRENCY_ID | 币种 | GUID | Y |  |
| 8 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 9 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 10 | PRICE |  | number(23,8) | Y |  |
| 11 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 12 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | TAX_RATE |  | number(5,4) | Y |  |
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
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### PARTS_TRANSFER_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 7 | SERVICE_SITE_ID | 站点 | GUID | Y |  |
| 8 | PLANT_ID | 工厂 | GUID | Y |  |
| 9 | PIECES |  | number | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | PARTS_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 12 | COMPANY_ID | 公司 | GUID | Y |  |
| 13 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 14 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 15 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 16 | PrintCount | 打印次数 | number | Y |  |
| 17 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 18 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 19 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 20 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 21 | Version | 版本号，不要随意更改 | binary | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | Attachments | 附件 | string | Y |  |
| 29 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### PARTS_TRANSFER_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 7 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 8 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 9 | FROM_BIN_ID | 转出库位 | GUID | Y |  |
| 10 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 11 | FROM_EMPLOYEE_ID | 转出人员 | GUID | Y |  |
| 12 | TO_EMPLOYEE_ID | 转入人员 | GUID | Y |  |
| 13 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 14 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 15 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 16 | SECOND_UNIT_ID | 第二单位 | GUID | Y |  |
| 17 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 18 | INVENTORY_UNIT_ID | 库存单位 | GUID | Y |  |
| 19 | PIECES |  | number | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | PARTS_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 47 | F_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 48 | F_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 49 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 50 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 51 | PARTS_TRANSFER_DOC_ID |  | GUID | Y |  |