---
module: "NRV"
name_zh: "可变现净值"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 95
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# NRV (可变现净值)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 95

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


- **NRV_D (净变现价值逆推明细档)**


---


---


> Tables: 2

### NRV (净变现价值)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | NRV_ID | 主键 | GUID | Y | Y |
| 2 | COMPANY_ID | 公司代号 | GUID | Y |  |
| 3 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 4 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | PRICE_SOURCE | 单价来源 | string(40) | Y |  |
| 8 | PRICE | 净变现单价 | number(23,8) | Y |  |
| 9 | VALUE | 净变现价值 | number(23,8) | Y |  |
| 10 | COST_SOURCE | 成本来源 | string(400) | Y |  |
| 11 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 12 | INVENTORY_AMT | 库存金额 | number(23,8) | Y |  |
| 13 | INVENTORY_QTY | 库存数量 | number(16,6) | Y |  |
| 14 | APPRECIATE_DEPRECIATE | 溢(跌)价 | number(23,8) | Y |  |
| 15 | RATE | 溢(跌)价比率 | number(5,4) | Y |  |
| 16 | AVERAGE_PRODUCT_RATE | 平均成品溢(跌)价比率 | number(5,4) | Y |  |
| 17 | REFERENCE_DATE_START | 参考日期(起) | date | Y |  |
| 18 | REFERENCE_DATE_END | 参考日期(迄) | date | Y |  |
| 19 | SALES_EXPENSE_RATE | 直接销售费用率 | number(5,4) | Y |  |
| 20 | DOC_NO | 来源单号 | string(40) | Y |  |
| 21 | SALES_QTY | 销售数量 | number(16,6) | Y |  |
| 22 | SALES_AMT | 销售金额 | number(23,8) | Y |  |
| 23 | INVENTORY_TYPE | 存货类型 | number | Y |  |
| 24 | DESCRIPTION | 溢(跌)价说明 | number | Y |  |
| 25 | IDLE_COST | 呆滞成本 | number(23,8) | Y |  |
| 26 | IDLE_QTY | 呆滞数量 | number(16,6) | Y |  |
| 27 | SEQUENCE_NO | 来源序号 | number | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 53 | Attachments | 附件 | string | Y |  |
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 59 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 60 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 61 | SOURCE_ID_ROid |  | GUID | Y |  |

### NRV_D (净变现价值逆推明细档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | NRV_D_ID | 主键 | GUID | Y | Y |
| 2 | PRODUCT_ITEM_ID | 成品品号 | GUID | Y |  |
| 3 | PRODUCT_ITEM_FEATURE_ID | 成品特征码 | GUID | Y |  |
| 4 | QTY_PER | 组成用量 | number(16,6) | Y |  |
| 5 | PRODUCT_RATE | 成品溢(跌)价比率 | number(5,4) | Y |  |
| 6 | PRODUCTION_DATE | 生产日期 | date | Y |  |
| 7 | SOURCE | 来源 | number | Y |  |
| 8 | CLCOST_AMT | 本阶成本 | number(23,8) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | NRV_ID |  | GUID | Y |  |