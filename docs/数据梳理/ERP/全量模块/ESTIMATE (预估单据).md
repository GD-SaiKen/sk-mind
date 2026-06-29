---
module: "ESTIMATE"
name_zh: "预估单据"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 159
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# ESTIMATE (预估单据)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 159

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


- **ESTIMATE_DOC (暂估单)**
- **ESTIMATE_DOC_D (暂估单单身)**
- **ESTIMATE_DOC_SD (暂估单子单身)**


---


---


> Tables: 3

### ESTIMATE_DOC (暂估单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ESTIMATE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 11 | AP_ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 12 | ESTI_QTY | 暂估数量合计 | number(16,6) | Y |  |
| 13 | ESTI_AMT | 暂估账款合计 | number(23,8) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 16 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 17 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 18 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
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
| 37 | PrintCount | 打印次数 | number | Y |  |
| 38 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 39 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 40 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 41 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | Attachments | 附件 | string | Y |  |
| 49 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
| 51 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 52 | ApproveDate | 修改日期 | date | Y |  |
| 53 | ApproveBy | 修改人 | GUID | Y |  |
| 54 | Owner_Org_RTK |  | string(400) | Y |  |
| 55 | Owner_Org_ROid |  | GUID | Y |  |

### ESTIMATE_DOC_D (暂估单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ESTIMATE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 暂估来源单据类型 | number | Y |  |
| 4 | PURCHASE_TYPE | 采购类型 | number | Y |  |
| 5 | TRANSACTION_DATE | 交易日期 | date | Y |  |
| 6 | ITEM_NAME |  | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 8 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 9 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 10 | SETTLED_QTY | 已结算数量 | number(16,6) | Y |  |
| 11 | ESTI_QTY | 暂估数量 | number(16,6) | Y |  |
| 12 | ESTI_PRICE | 暂估价款单价 | number(23,8) | Y |  |
| 13 | ESTI_PUR_AMT_TC | 暂估价款金额(原币) | number(23,8) | Y |  |
| 14 | ESTI_PUR_AMT_FC | 暂估价款金额(本币) | number(23,8) | Y |  |
| 15 | ESTI_EXPENSE_AMT | 暂估费用金额 | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | ITEM_ID | 品号 | GUID | Y |  |
| 18 | CURRENCY_ID | 主键 | GUID | Y |  |
| 19 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 20 | BUYER_ID | 采购人员 | GUID | Y |  |
| 21 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 22 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 23 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 24 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 25 | BIN_ID | 库位 | GUID | Y |  |
| 26 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 27 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 28 | ADMIN_UNIT_ID | 采购部门 | GUID | Y |  |
| 29 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 30 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 49 | CreateDate | 创建日期 | date | Y |  |
| 50 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 51 | ModifiedDate | 修改日期 | date | Y |  |
| 52 | CreateBy | 创建者 | GUID | Y |  |
| 53 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 54 | ModifiedBy | 修改者 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 60 | SOURCE_ID_ROid |  | GUID | Y |  |
| 61 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 62 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 63 | ESTIMATE_DOC_ID |  | GUID | Y |  |

### ESTIMATE_DOC_SD (暂估单子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ESTIMATE_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 4 | ESTI_EXPENSE_AMT_TC | 暂估费用金额(原币) | number(23,8) | Y |  |
| 5 | ESTI_EXPENSE_AMT_FC | 暂估费用金额(本币) | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | EXPENSE_ID | 费用项目 | GUID | Y |  |
| 8 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 9 | CURRENCY_ID | 货币 | GUID | Y |  |
| 10 | EXPENSES_BY_RECEIPT_ID | 来源单据费用行 | GUID | Y |  |
| 11 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 12 | PROJECT_ID | 项目 | GUID | Y |  |
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
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | ESTIMATE_DOC_D_ID |  | GUID | Y |  |