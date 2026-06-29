---
module: "BORROW"
name_zh: "借入借出"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 273
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# BORROW (借入借出)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 273

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[CHECK (盘点调整)|CHECK (盘点调整)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]
- [[ISSUE (发料出库)|ISSUE (发料出库)]]

---

## Tables


- **BORROW_DOC (借出/入单)**
- **BORROW_DOC_D (借出/入单单身)**
- **BORROW_RETURN_DOC (借出/入归还单)**
- **BORROW_RETURN_DOC_D (借出/入归还单单身)**


---


---


> Tables: 4

### BORROW_DOC (借出/入单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | BORROW_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 9 | PARTNER_FULL_NAME | 对象全称 | string(144) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ADDRESS |  | string(510) | Y |  |
| 13 | FROM_WAREHOUSE_ID | 限用转出仓库编号 | GUID | Y |  |
| 14 | TO_WAREHOUSE_ID | 限用转入仓库编号 | GUID | Y |  |
| 15 | COMPANY_ID | 公司 | GUID | Y |  |
| 16 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 17 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 18 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 19 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 20 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 21 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 22 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 23 | CURRENCY_ID | 币种 | GUID | Y |  |
| 24 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 25 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 26 | SALES_CENTER_ID | 转销销售域 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 46 | PrintCount | 打印次数 | number | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 51 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 52 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 53 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 54 | CreateDate | 创建日期 | date | Y |  |
| 55 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 56 | ModifiedDate | 修改日期 | date | Y |  |
| 57 | CreateBy | 创建者 | GUID | Y |  |
| 58 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 59 | ModifiedBy | 修改者 | GUID | Y |  |
| 60 | Attachments | 附件 | string | Y |  |
| 61 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 62 | Owner_Org_RTK |  | string(400) | Y |  |
| 63 | Owner_Org_ROid |  | GUID | Y |  |
| 64 | BO_ID_RTK |  | string(400) | Y |  |
| 65 | BO_ID_ROid |  | GUID | Y |  |
| 66 | BORROW_INV_METHOD | 借入业务存货认定方式 | string(40) | Y |  |

### BORROW_DOC_D (借出/入单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BORROW_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | PRICING_QTY | 计价数量 | number(16,6) | Y |  |
| 6 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 13 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 14 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 15 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 16 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 17 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 18 | PLAN_RETURN_DATE | 预计归还日 | date | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | CLOSE | 结束 | string(40) | Y |  |
| 21 | PUR_SALE_INV_QTY | 转进销库存数量 | number(16,6) | Y |  |
| 22 | PUR_SALE_SECOND_QTY | 转进销第二数量 | number(16,6) | Y |  |
| 23 | RETURN_INV_QTY | 归还库存数量 | number(16,6) | Y |  |
| 24 | RETURN_SECOND_QTY | 归还第二数量 | number(16,6) | Y |  |
| 25 | PIECES |  | number | Y |  |
| 26 | RETURN_BUS_QTY | 归还业务数量 | number(16,6) | Y |  |
| 27 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 28 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 29 | ITEM_ID | 品号 | GUID | Y |  |
| 30 | PRICING_UNIT_ID | 计价单位 | GUID | Y |  |
| 31 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 32 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 33 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 34 | FROM_BIN_ID | 转出库位 | GUID | Y |  |
| 35 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 36 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 37 | PROJECT_ID | 项目 | GUID | Y |  |
| 38 | PRICE | 单价 | number(23,8) | Y |  |
| 39 | AMOUNT | 金额 | number(23,8) | Y |  |
| 40 | PUR_SALE_BUS_QTY | 转销业务数量 | number(16,6) | Y |  |
| 41 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 42 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 45 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 46 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 47 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 48 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 49 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 50 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 51 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 52 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 53 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 54 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 55 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 56 | UDF041 | 自定义字段12 | date | Y |  |
| 57 | UDF042 | 自定义字段13 | date | Y |  |
| 58 | UDF051 | 自定义字段14 | GUID | Y |  |
| 59 | UDF052 | 自定义字段15 | GUID | Y |  |
| 60 | UDF053 | 自定义字段16 | GUID | Y |  |
| 61 | UDF054 | 自定义字段17 | GUID | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | CreateDate | 创建日期 | date | Y |  |
| 66 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 67 | ModifiedDate | 修改日期 | date | Y |  |
| 68 | CreateBy | 创建者 | GUID | Y |  |
| 69 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 70 | ModifiedBy | 修改者 | GUID | Y |  |
| 71 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 72 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 73 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 74 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 75 | BORROW_DOC_ID |  | GUID | Y |  |
| 76 | PRODUCT_SUB_GROUP_ID | 替代群组主键 | GUID | Y |  |
| 77 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |

### BORROW_RETURN_DOC (借出/入归还单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | BORROW_RETURN_DOC_ID | 主键 | GUID | Y | Y |
| 7 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 8 | CATEGORY | 单据性质码 | string(40) | Y |  |
| 9 | PARTNER_FULL_NAME | 对象全称 | string(144) | Y |  |
| 10 | PIECES |  | number | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ADDRESS |  | string(510) | Y |  |
| 13 | FROM_WAREHOUSE_ID | 限用转出仓库编号 | GUID | Y |  |
| 14 | TO_WAREHOUSE_ID | 限用转入仓库编号 | GUID | Y |  |
| 15 | COMPANY_ID | 公司 | GUID | Y |  |
| 16 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 17 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 18 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 19 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 20 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 21 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 22 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 23 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | PrintCount | 打印次数 | number | Y |  |
| 47 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 48 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 49 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 50 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
| 52 | CreateDate | 创建日期 | date | Y |  |
| 53 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 54 | ModifiedDate | 修改日期 | date | Y |  |
| 55 | CreateBy | 创建者 | GUID | Y |  |
| 56 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 57 | ModifiedBy | 修改者 | GUID | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |
| 60 | BO_ID_RTK |  | string(400) | Y |  |
| 61 | BO_ID_ROid |  | GUID | Y |  |
| 62 | BORROW_INV_METHOD | 借入业务存货认定方式 | string(40) | Y |  |

### BORROW_RETURN_DOC_D (借出/入归还单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BORROW_RETURN_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 4 | PRICING_QTY | 计价数量 | number(16,6) | Y |  |
| 5 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 10 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 11 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 12 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 13 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 14 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 15 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | PIECES |  | number | Y |  |
| 18 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 19 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 20 | ITEM_ID | 品号 | GUID | Y |  |
| 21 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 22 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 23 | PRICING_UNIT_ID | 计价单位 | GUID | Y |  |
| 24 | SOURCE_ID | 源单ID | GUID | Y |  |
| 25 | TO_WAREHOUSE_ID | 转入仓库 | GUID | Y |  |
| 26 | FROM_WAREHOUSE_ID | 转出仓库 | GUID | Y |  |
| 27 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 28 | TO_BIN_ID | 转入库位 | GUID | Y |  |
| 29 | FROM_BIN_ID |  | GUID | Y |  |
| 30 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 31 | PROJECT_ID | 项目 | GUID | Y |  |
| 32 | SN_COLLECTED_QTY | 序列号已采集数量 | number(16,6) | Y |  |
| 33 | SN_COLLECTED_STATUS | 序列号检核码 | string(40) | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | CreateDate | 创建日期 | date | Y |  |
| 57 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 58 | ModifiedDate | 修改日期 | date | Y |  |
| 59 | CreateBy | 创建者 | GUID | Y |  |
| 60 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 61 | ModifiedBy | 修改者 | GUID | Y |  |
| 62 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 63 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 64 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 65 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 66 | BORROW_RETURN_DOC_ID |  | GUID | Y |  |
| 67 | ORI_OWNER_EMP | 原负责人 | GUID | Y |  |
| 68 | ORI_OWNER_DEPT | 原负责部门 | GUID | Y |  |