---
module: "CONSIGN"
name_zh: "寄售管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 5
columns: 356
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# CONSIGN (寄售管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 5 | Columns: 356

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]
- [[ISSUE (发料出库)|ISSUE (发料出库)]]

---

## Tables


- **CONSIGN_TRANSFER_IN (寄售退回单)**
- **CONSIGN_TRANSFER_IN_D (寄售退回单单身)**
- **CONSIGN_TRANSFER_OUT (寄售调拨单)**
- **CONSIGN_TRANSFER_OUT_D (寄售调拨单单身)**


---


---


> Tables: 5

### CONSIGN (维护寄售关系)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CONSIGN_ID | 主键 | GUID | Y | Y |
| 4 | PLANT_ID | 工厂 | GUID | Y |  |
| 5 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 6 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 7 | WAREHOUSE_ID | 主键 | GUID | Y |  |
| 8 | WAREHOUSE_OUT_ID | 出库仓库 | GUID | Y |  |
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

### CONSIGN_TRANSFER_IN (寄售退回单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CONSIGN_TRANSFER_IN_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 退回日期 | date | Y |  |
| 8 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 9 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CATEGORY | 单据性质 | string(40) | Y |  |
| 12 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 13 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 14 | PIECES | 件数 | number | Y |  |
| 15 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 16 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 17 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 18 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 19 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 20 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 21 | CURRENCY_ID | 币种 | GUID | Y |  |
| 22 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 23 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 24 | CONSIGN_WAREHOUSE_ID | 寄售仓 | GUID | Y |  |
| 25 | SHIP_TO_ADDR_ID | 收货地址编号 | GUID | Y |  |
| 26 | COMPANY_ID | 公司 | GUID | Y |  |
| 27 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 28 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 29 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 30 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | PrintCount | 打印次数 | number | Y |  |
| 33 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 34 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 35 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 36 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | Owner_Org_RTK |  | string(400) | Y |  |
| 67 | Owner_Org_ROid |  | GUID | Y |  |
| 68 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 69 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 70 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 71 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 72 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |

### CONSIGN_TRANSFER_IN_D (寄售退回单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CONSIGN_TRANSFER_IN_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 8 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 9 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 10 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 11 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 12 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 13 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 14 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 21 | PRICE | 单价 | number(23,8) | Y |  |
| 22 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 23 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 24 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 25 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 26 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 27 | AMOUNT | 金额 | number(23,8) | Y |  |
| 28 | PIECES |  | number | Y |  |
| 29 | TAX_ID | 税种 | GUID | Y |  |
| 30 | ITEM_ID | 品号 | GUID | Y |  |
| 31 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 32 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 33 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 34 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 35 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 36 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 37 | WAREHOUSE_ID | 主键 | GUID | Y |  |
| 38 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 39 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 40 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 41 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 42 | BIN_ID | 库位 | GUID | Y |  |
| 43 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 44 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 45 | PROJECT_ID | 项目 | GUID | Y |  |
| 46 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 47 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 56 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 57 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 58 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 59 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 60 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 61 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 62 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 63 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 64 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 65 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 66 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 67 | UDF041 | 自定义字段12 | date | Y |  |
| 68 | UDF042 | 自定义字段13 | date | Y |  |
| 69 | UDF051 | 自定义字段14 | GUID | Y |  |
| 70 | UDF052 | 自定义字段15 | GUID | Y |  |
| 71 | UDF053 | 自定义字段16 | GUID | Y |  |
| 72 | UDF054 | 自定义字段17 | GUID | Y |  |
| 73 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 74 | ApproveDate | 修改日期 | date | Y |  |
| 75 | ApproveBy | 修改人 | GUID | Y |  |
| 76 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 77 | SOURCE_ID_ROid |  | GUID | Y |  |
| 78 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 79 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 80 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 81 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 82 | CONSIGN_TRANSFER_IN_ID |  | GUID | Y |  |

### CONSIGN_TRANSFER_OUT (寄售调拨单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 7 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 8 | CONSIGN_TRANSFER_OUT_ID | 主键 | GUID | Y | Y |
| 9 | TRANSACTION_DATE | 调拨日期 | date | Y |  |
| 10 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 11 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | CATEGORY | 单据性质 | string(40) | Y |  |
| 14 | PIECES |  | number | Y |  |
| 15 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 16 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 17 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 18 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 19 | COMPANY_ID | 公司 | GUID | Y |  |
| 20 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 21 | CURRENCY_ID | 币种 | GUID | Y |  |
| 22 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 23 | WAREHOUSE_ID | 限用仓库 | GUID | Y |  |
| 24 | CONSIGN_WAREHOUSE_ID | 寄售仓 | GUID | Y |  |
| 25 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 26 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 27 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 28 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 29 | SIGN_REQUIRED | 需签收 | number(0/1) | Y |  |
| 30 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 31 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | PrintCount | 打印次数 | number | Y |  |
| 34 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 35 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 36 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 37 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 38 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 39 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 40 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 41 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 42 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 43 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 44 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 45 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 46 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 47 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 48 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 49 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 50 | UDF041 | 自定义字段12 | date | Y |  |
| 51 | UDF042 | 自定义字段13 | date | Y |  |
| 52 | UDF051 | 自定义字段14 | GUID | Y |  |
| 53 | UDF052 | 自定义字段15 | GUID | Y |  |
| 54 | UDF053 | 自定义字段16 | GUID | Y |  |
| 55 | UDF054 | 自定义字段17 | GUID | Y |  |
| 56 | CreateDate | 创建日期 | date | Y |  |
| 57 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 58 | ModifiedDate | 修改日期 | date | Y |  |
| 59 | CreateBy | 创建者 | GUID | Y |  |
| 60 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 61 | ModifiedBy | 修改者 | GUID | Y |  |
| 62 | Attachments | 附件 | string | Y |  |
| 63 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |
| 67 | Owner_Org_RTK |  | string(400) | Y |  |
| 68 | Owner_Org_ROid |  | GUID | Y |  |
| 69 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 70 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 71 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 72 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 73 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |

### CONSIGN_TRANSFER_OUT_D (寄售调拨单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CONSIGN_TRANSFER_OUT_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 5 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 7 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 8 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 9 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 10 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 11 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 12 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 13 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 14 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 15 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 16 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 17 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 18 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 21 | PRICE | 单价 | number(23,8) | Y |  |
| 22 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 23 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 24 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 25 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 26 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 27 | AMOUNT |  | number(23,8) | Y |  |
| 28 | PIECES |  | number | Y |  |
| 29 | TAX_ID | 税种 | GUID | Y |  |
| 30 | ITEM_ID | 品号 | GUID | Y |  |
| 31 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 32 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 33 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 34 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 35 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 36 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 37 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 38 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 39 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 40 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 41 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 42 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 43 | BIN_ID | 库位 | GUID | Y |  |
| 44 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 45 | CUSTOMER_SIGNED | 签收状态 | string(40) | Y |  |
| 46 | CUSTOMER_SIGNED_QTY | 业务签收数量 | number(16,6) | Y |  |
| 47 | CONSIGN_TRANSFER_IN_ID | 退回单号 | GUID | Y |  |
| 48 | RETURN_REASON_ID | 签收差异原因 | GUID | Y |  |
| 49 | BC_CHECK_STATUS | 检核码 | string(40) | Y |  |
| 50 | PROJECT_ID | 项目 | GUID | Y |  |
| 51 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 52 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 53 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 54 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 57 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 58 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 59 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 60 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 61 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 62 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 63 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 64 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 65 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 66 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 67 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 68 | UDF041 | 自定义字段12 | date | Y |  |
| 69 | UDF042 | 自定义字段13 | date | Y |  |
| 70 | UDF051 | 自定义字段14 | GUID | Y |  |
| 71 | UDF052 | 自定义字段15 | GUID | Y |  |
| 72 | UDF053 | 自定义字段16 | GUID | Y |  |
| 73 | UDF054 | 自定义字段17 | GUID | Y |  |
| 74 | CreateDate | 创建日期 | date | Y |  |
| 75 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 76 | ModifiedDate | 修改日期 | date | Y |  |
| 77 | CreateBy | 创建者 | GUID | Y |  |
| 78 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 79 | ModifiedBy | 修改者 | GUID | Y |  |
| 80 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 81 | ApproveDate | 修改日期 | date | Y |  |
| 82 | ApproveBy | 修改人 | GUID | Y |  |
| 83 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 84 | SOURCE_ID_ROid |  | GUID | Y |  |
| 85 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 86 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 87 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 88 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 89 | CONSIGN_TRANSFER_OUT_ID |  | GUID | Y |  |