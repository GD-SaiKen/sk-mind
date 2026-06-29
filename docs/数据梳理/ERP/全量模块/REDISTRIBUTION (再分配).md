---
module: "REDISTRIBUTION"
name_zh: "再分配"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 125
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# REDISTRIBUTION (再分配)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 125

## Related Modules

- [[ABTABAC (表格映射)|ABTABAC (表格映射)]]
- [[ABTABVC (表格方案)|ABTABVC (表格方案)]]
- [[ACCCODE (科目数据集)|ACCCODE (科目数据集)]]
- [[ACCESS (权限控制)|ACCESS (权限控制)]]
- [[ACCPERIOD (会计期间)|ACCPERIOD (会计期间)]]
- [[ALTER (变更)|ALTER (变更)]]
- [[AM (资产报表)|AM (资产报表)]]
- [[AU (辅助特性)|AU (辅助特性)]]

---

## Tables


- **REDISTRIBUTION_D**


---


---


> Tables: 2

### REDISTRIBUTION

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | REDISTRIBUTION_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PLANT_ID | 接收储运机构 | GUID | Y |  |
| 9 | DELIVEYR_RESOURCE_ID | 配送资源 | GUID | Y |  |
| 10 | DISTRIBUTION_DATE | 退配日期 | date | Y |  |
| 11 | EXPENSE_ID | 费用编号 | GUID | Y |  |
| 12 | CURRENCY_ID | 币种 | GUID | Y |  |
| 13 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 14 | EXPENSE_AMOUNT_TC | 费用金额（原币） | number(23,8) | Y |  |
| 15 | EXPENSE_AMOUNT_BC | 费用金额（本币） | number(23,8) | Y |  |
| 16 | SUPPLIER_ID | 承运商 | GUID | Y |  |
| 17 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 18 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 19 | RECEIVE_ADDR | 收货地址 | string(510) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | SAME_LEGAL | 同法人 | number(0/1) | Y |  |
| 22 | TRANSPORTER | 运输方 | string(40) | Y |  |
| 23 | EXPENSES_TO | 费用归属 | string(40) | Y |  |
| 24 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 25 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 26 | PrintCount | 打印次数 | number | Y |  |
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
| 45 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 46 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 47 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 48 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | Attachments | 附件 | string | Y |  |
| 56 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 59 | ApproveDate | 修改日期 | date | Y |  |
| 60 | ApproveBy | 修改人 | GUID | Y |  |
| 61 | Owner_Org_RTK |  | string(400) | Y |  |
| 62 | Owner_Org_ROid |  | GUID | Y |  |
| 63 | REDISTRIBUTION_TYPE_RTK |  | string(400) | Y |  |
| 64 | REDISTRIBUTION_TYPE_ROid |  | GUID | Y |  |

### REDISTRIBUTION_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | REDISTRIBUTION_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 7 | WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 8 | BIN_ID | 发货库位 | GUID | Y |  |
| 9 | TRANSIT_WAREHOUSE_ID | 在途仓 | GUID | Y |  |
| 10 | REDISTRIBUTION_QTY | 退配数量 | number(16,6) | Y |  |
| 11 | STORAGE_QTY | 已入库量 | number(16,6) | Y |  |
| 12 | DIFF_QTY | 差异数量 | number(16,6) | Y |  |
| 13 | LOGISTICS_UNIT_ID | 物流单位 | GUID | Y |  |
| 14 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 15 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 16 | COST | 单位成本 | number(23,8) | Y |  |
| 17 | CLOSED | 结束码 | string(40) | Y |  |
| 18 | SUPPLY_SYNERGY_ID | 协同关系 | GUID | Y |  |
| 19 | REORDER | 自动再补货 | number(0/1) | Y |  |
| 20 | REORDER_NO | 再补货单主键 | GUID | Y |  |
| 21 | INVENTORY_QTY1 | 入库库存单位数量 | number(16,6) | Y |  |
| 22 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 25 | INNER_SETTLEMENT_CLOSE | 内部结算码 | string(40) | Y |  |
| 26 | RETURN_REASON_ID | 退货原因 | GUID | Y |  |
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
| 51 | Version | 版本号，不要随意更改 | binary | Y |  |
| 52 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 53 | ApproveDate | 修改日期 | date | Y |  |
| 54 | ApproveBy | 修改人 | GUID | Y |  |
| 55 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE_ID_ROid |  | GUID | Y |  |
| 57 | FROM_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 58 | FROM_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 59 | TO_COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 60 | TO_COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 61 | REDISTRIBUTION_ID |  | GUID | Y |  |