---
module: "ACCOUNT"
name_zh: "会计科目"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 10
columns: 885
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# ACCOUNT (会计科目)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 10 | Columns: 885

## Related Modules

- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]
- [[CLOSE (关账检查)|CLOSE (关账检查)]]

---

## Tables


- **ACCOUNT_BALANCE**
- **ACCOUNT_CATEGORY (会计分类信息)**
- **ACCOUNT_CODE (科目信息)**
- **ACCOUNT_CODE_DIFFA (会计科目差量档A)**
- **ACCOUNT_CODE_DIFFB (会计科目差量B)**
- **ACCOUNT_GROUP (科目组)**
- **ACCOUNT_GROUP_D (科目组单身)**
- **ACCOUNT_INITIAL (科目初始数据)**
- **ACCOUNT_INITIAL_D (科目初始数据单身)**
- **ACCOUNT_INITIAL_SD (科目初始数据子单身)**


---


---


> Tables: 10

### ACCOUNT_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ACCOUNT_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 8 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 9 | DEBIT_QTY | 借方数量 | number(16,6) | Y |  |
| 10 | CREDIT_QTY | 贷方数量 | number(16,6) | Y |  |
| 11 | DEBIT_TRANS_CURRENCY_AMT | 借方金额—原币 | number(23,8) | Y |  |
| 12 | CREDIT_TRANS_CURRENCY_AMT | 贷方金额—原币 | number(23,8) | Y |  |
| 13 | DEBIT_FUNCTION_CURRENCY_AMT | 借方金额—本币 | number(23,8) | Y |  |
| 14 | CREDIT_FUNCTION_CURRENCY_AMT | 贷方金额—本币 | number(23,8) | Y |  |
| 15 | ACCOUNT_CODE_ID | 科目编号 | GUID | Y |  |
| 16 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 17 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 18 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 19 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 20 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 21 | SUPPLY_CENTER_ID | 供应域 | GUID | Y |  |
| 22 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 23 | TRANS_CURRENCY_ID | 交易货币 | GUID | Y |  |
| 24 | PROJECT_ID | 项目 | GUID | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
| 33 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 34 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 35 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 36 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 37 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 38 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 39 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 40 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 41 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 42 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 43 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 44 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 45 | UDF041 | 自定义字段12 | date | Y |  |
| 46 | UDF042 | 自定义字段13 | date | Y |  |
| 47 | UDF051 | 自定义字段14 | GUID | Y |  |
| 48 | UDF052 | 自定义字段15 | GUID | Y |  |
| 49 | UDF053 | 自定义字段16 | GUID | Y |  |
| 50 | UDF054 | 自定义字段17 | GUID | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### ACCOUNT_CATEGORY (会计分类信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ACCOUNT_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_CATEGORY_CODE | 会计分类编号 | string(20) | Y |  |
| 5 | ACCOUNT_CATEGORY_NAME | 会计分类名称 | string(40) | Y |  |
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

### ACCOUNT_CODE (科目信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ACCOUNT_CODE_ID | 主键 | GUID | Y | Y |
| 4 | ACCCODE |  | string(60) | Y |  |
| 5 | ACCCODE_NAME |  | string(80) | Y |  |
| 6 | ACCCODE_AREA | 科目范围 | number | Y |  |
| 7 | ACCCODE_FULL_NAME | 科目全称 | string(840) | Y |  |
| 8 | ACCCODE_ALIAS | 科目别名 | string(840) | Y |  |
| 9 | BALANCE_DIRECTION | 科目余额方向 | number | Y |  |
| 10 | ACCCODE_ROLE | 科目性质 | number | Y |  |
| 11 | ACCCODE_LEVEL | 科目层级 | number | Y |  |
| 12 | ALLOW_ADDACCCODE_INDICATOR | 允许增加下级科目 | number(0/1) | Y |  |
| 13 | ACCCODE_DATASET_ID | 科目表编号 | GUID | Y |  |
| 14 | ACCCODE_CATEGORY_ID | 科目所属类别 | GUID | Y |  |
| 15 | ACCCODE_ANALYSIS_PROPERTY_ID | 科目分析属性 | GUID | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
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
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |

### ACCOUNT_CODE_DIFFA (会计科目差量档A)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ACCOUNT_CODE_DIFFA_ID | 主键 | GUID | Y | Y |
| 2 | SHORTCUT_CODE | 快捷码 | string(60) | Y |  |
| 3 | ACCOUNT_CODE_ID | 主键 | GUID | Y |  |
| 4 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |
| 34 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 35 | SOURCE_ID_ROid |  | GUID | Y |  |

### ACCOUNT_CODE_DIFFB (会计科目差量B)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ACCOUNT_CODE_DIFFB_ID | 主键 | GUID | Y | Y |
| 2 | ACCOUNT_BOOK | 账簿编号 | number | Y |  |
| 3 | EXCHANGE_INDICATOR | 调汇 | number(0/1) | Y |  |
| 4 | CASHFLOW_INDICATOR | 现金流量 | number(0/1) | Y |  |
| 5 | QUANTITY_INDICATOR | 数量核算 | number(0/1) | Y |  |
| 6 | UNIT | 单位 | string(8) | Y |  |
| 7 | CARRY_OVER_INDICATOR | 损益结转 | number(0/1) | Y |  |
| 8 | SUMMARY_PRINT_INDICATOR | 汇总打印 | number(0/1) | Y |  |
| 9 | SUMMARY_PRINT_LEVEL | 汇总打印级次 | number | Y |  |
| 10 | AUXILIARY_ITEM |  | string(20) | Y |  |
| 11 | CURRENCY_AREA | 货币范围 | number | Y |  |
| 12 | ALTER_ACCOUNT_CODE_ID | 备选科目编号 | GUID | Y |  |
| 13 | ACCOUNT_CODE_DIFFA_ID | 父主键 | GUID | Y |  |
| 14 | CURRENCY_ID | 货币编号 | GUID |  |  |
| 15 | CASHFLOW_ITEM_IN_ID | 现金流量项目-流入 | GUID | Y |  |
| 16 | CASHFLOW_ITEM_OUT_ID | 主键 | GUID | Y |  |
| 17 | OIM_FLAG | 立冲账标识 | number(0/1) | Y |  |
| 18 | FSI_CODE | 公告项目编号 | string(60) | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
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
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### ACCOUNT_GROUP (科目组)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ACCOUNT_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | ACCOUNT_GROUP_CODE | 科目组编号 | string(12) | Y |  |
| 6 | ACCOUNT_GROUP_NAME | 科目组名称 | string(40) | Y |  |
| 7 | ACCOUNT_GROUP_TYPE | 科目组类型 | number | Y |  |
| 8 | CURRENCY_FLAG | 限定条件标识-货币 | number(0/1) | Y |  |
| 9 | CUSTOMER_FICATEGORY_FLAG | 限定条件标识-客户会计分类 | number(0/1) | Y |  |
| 10 | SUPPLIER_FICATEGORY_FLAG | 限定条件标识-供应商会计分类 | number(0/1) | Y |  |
| 11 | INVENTORY_FICATEGORY_FLAG | 限定条件标识-存货会计分类 | number(0/1) | Y |  |
| 12 | OTHER_ARAP_ITEM_FLAG | 限定条件标识-其他收付项目 | number(0/1) | Y |  |
| 13 | SETTLEMENT_EXPENSE_FLAG | 限定条件标识-结算费用 | number(0/1) | Y |  |
| 14 | ADMIN_UNIT_FLAG | 限定条件标识-部门 | number(0/1) | Y |  |
| 15 | SETTLEMENT_OBJECT_TYPE_FLAG | 限定条件标识-结算对象类型 | number(0/1) | Y |  |
| 16 | WAREHOUSE_FLAG | 限定条件标识-仓库 | number(0/1) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | PURCHASE_EXPENSE_FLAG | 限定条件标识-采购费用 | number(0/1) | Y |  |
| 19 | TAX_FLAG | 限定条件标识-税种税率 | number(0/1) | Y |  |
| 20 | PLANT_FLAG | 限定条件标识-工厂/储运 | number(0/1) | Y |  |
| 21 | COST_ELEMENT_FLAG | 限定条件标识-成本要素 | number(0/1) | Y |  |
| 22 | EXGGL_TYPE_FLAG | 限定条件标识-汇兑损益类型 | number(0/1) | Y |  |
| 23 | NOTE_ITEM_FLAG | 限定条件标识-票据收付项目 | number(0/1) | Y |  |
| 24 | DEP_WD_ITEM_FLAG | 限定条件标识-银行存提项目 | number(0/1) | Y |  |
| 25 | TRANS_OBJECT_FICATEGORY_FLAG | 限定条件标识-交易对象会计分类 | number(0/1) | Y |  |
| 26 | BANK_ACCOUNT_FLAG | 限定条件标识-银行账号 | number(0/1) | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Attachments | 附件 | string | Y |  |
| 34 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 35 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 36 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 37 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 38 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 39 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 40 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 41 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 42 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 43 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 44 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 45 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 46 | UDF041 | 自定义字段12 | date | Y |  |
| 47 | UDF042 | 自定义字段13 | date | Y |  |
| 48 | UDF051 | 自定义字段14 | GUID | Y |  |
| 49 | UDF052 | 自定义字段15 | GUID | Y |  |
| 50 | UDF053 | 自定义字段16 | GUID | Y |  |
| 51 | UDF054 | 自定义字段17 | GUID | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | Owner_Org_RTK |  | string(400) | Y |  |
| 58 | Owner_Org_ROid |  | GUID | Y |  |
| 59 | ASSET_NATURE_FLAG | 限定条件标识-资产性质 | number(0/1) | Y |  |
| 60 | FIN_INSTITUTION_FLAG | 限定条件标识-金融机构 | number(0/1) | Y |  |
| 61 | LOAN_PURPOSE_FLAG | 限定条件标识-借款用途 | number(0/1) | Y |  |
| 62 | ORDER_CUSTOMER_FLAG | 订货客户标识 | number(0/1) | Y |  |

### ACCOUNT_GROUP_D (科目组单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ACCOUNT_GROUP_D_ID |  | GUID | Y | Y |
| 3 | CURRENCY_ID | 货币 | GUID | Y |  |
| 4 | OTHER_ARAP_ITEM_ID | 其他收付项目 | GUID | Y |  |
| 5 | SETTLEMENT_EXPENSE_ID | 结算费用项目 | GUID | Y |  |
| 6 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 7 | SETTLEMENT_OBJECT_TYPE | 结算对象类型 | number | Y |  |
| 8 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 9 | ACCOUNT_CODE_ID | 科目 | GUID | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CUSTOMER_FICATEGORY_ID | 客户会计分类 | GUID | Y |  |
| 12 | SUPPLIER_FICATEGORY_ID | 供应商会计分类 | GUID | Y |  |
| 13 | INVENTORY_FICATEGORY_ID | 存货会计分类 | GUID | Y |  |
| 14 | PURCHASE_EXPENSE_ID | 采购费用项目 | GUID | Y |  |
| 15 | TAX_ID | 税种税率 | GUID | Y |  |
| 16 | COST_ELEMENT_ID | 主键 | GUID | Y |  |
| 17 | COST_ATTRIBUTION | 成本归属 | number | Y |  |
| 18 | TRANS_TYPE | 业务类型 | number | Y |  |
| 19 | PLANT_ID | 主鍵 | GUID | Y |  |
| 20 | EXGGL_TYPE | 汇兑损益类型 | number | Y |  |
| 21 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 22 | TWNM_ITEM_ID | 票据管理收付项目 | GUID | Y |  |
| 23 | TRANS_OBJECT_TYPE | 交易对象类型 | number | Y |  |
| 24 | ACCOUNT_CODE2_ID | 科目2 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 54 | SOURCE_ID_ROid |  | GUID | Y |  |
| 55 | ACCOUNT_GROUP_ID |  | GUID | Y |  |
| 56 | ASSET_NATURE | 资产性质 | number | Y |  |
| 57 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 58 | LOAN_PURPOSE_ID | 借款用途 | GUID | Y |  |

### ACCOUNT_INITIAL (科目初始数据)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ACCOUNT_INITIAL_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | START_YEAR | 启用期间_年 | string(8) | Y |  |
| 6 | START_PERIOD_CODE | 启用期间_期号 | string(20) | Y |  |
| 7 | START_PERIOD_SEQNO | 启用期间_序号 | number | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Owner_Org_RTK |  | string(400) | Y |  |
| 33 | Owner_Org_ROid |  | GUID | Y |  |

### ACCOUNT_INITIAL_D (科目初始数据单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ACCOUNT_INITIAL_D_ID | 主键 | GUID | Y | Y |
| 2 | ACCOUNT_CODE_ID | 科目 | GUID | Y |  |
| 3 | TRANS_CURRENCY_ID | 货币 | GUID | Y |  |
| 4 | BALANCE_DIRECTION | 平衡方向(借/贷) | number | Y |  |
| 5 | YEAR_OPENING_QTY | 年初余额-数量 | number(16,6) | Y |  |
| 6 | YEAR_OPENING_TRANS_AMT | 年初余额-原币 | number(23,8) | Y |  |
| 7 | YEAR_OPENING_FUNCTION_AMT | 年初余额-本币 | number(23,8) | Y |  |
| 8 | P01_DR_QTY | 期间1-借方数量 | number(16,6) | Y |  |
| 9 | P01_DR_TRANS_AMT | 期间1-借方金额-原币 | number(23,8) | Y |  |
| 10 | P01_DR_FUNCTION_AMT | 期间1-借方金额-本币 | number(23,8) | Y |  |
| 11 | P01_CR_QTY | 期间1-贷方数量 | number(16,6) | Y |  |
| 12 | P01_CR_TRANS_AMT | 期间1-贷方金额-原币 | number(23,8) | Y |  |
| 13 | P01_CR_FUNCTION_AMT | 期间1-贷方金额-本币 | number(23,8) | Y |  |
| 14 | P02_DR_QTY | 期间2-借方数量 | number(16,6) | Y |  |
| 15 | P02_DR_TRANS_AMT | 期间2-借方金额-原币 | number(23,8) | Y |  |
| 16 | P02_DR_FUNCTION_AMT | 期间2-借方金额-本币 | number(23,8) | Y |  |
| 17 | P02_CR_QTY | 期间2-贷方数量 | number(16,6) | Y |  |
| 18 | P02_CR_TRANS_AMT | 期间2-贷方金额-原币 | number(23,8) | Y |  |
| 19 | P02_CR_FUNCTION_AMT | 期间2-贷方金额-本币 | number(23,8) | Y |  |
| 20 | P03_DR_QTY | 期间3-借方数量 | number(16,6) | Y |  |
| 21 | P03_DR_TRANS_AMT | 期间3-借方金额-原币 | number(23,8) | Y |  |
| 22 | P03_DR_FUNCTION_AMT | 期间3-借方金额-本币 | number(23,8) | Y |  |
| 23 | P03_CR_QTY | 期间3-贷方数量 | number(16,6) | Y |  |
| 24 | P03_CR_TRANS_AMT | 期间3-贷方金额-原币 | number(23,8) | Y |  |
| 25 | P03_CR_FUNCTION_AMT | 期间3-贷方金额-本币 | number(23,8) | Y |  |
| 26 | P04_DR_QTY | 期间4-借方数量 | number(16,6) | Y |  |
| 27 | P04_DR_TRANS_AMT | 期间4-借方金额-原币 | number(23,8) | Y |  |
| 28 | P04_DR_FUNCTION_AMT | 期间4-借方金额-本币 | number(23,8) | Y |  |
| 29 | P04_CR_QTY | 期间4-贷方数量 | number(16,6) | Y |  |
| 30 | P04_CR_TRANS_AMT | 期间4-贷方金额-原币 | number(23,8) | Y |  |
| 31 | P04_CR_FUNCTION_AMT | 期间4-贷方金额-本币 | number(23,8) | Y |  |
| 32 | P05_DR_QTY | 期间5-借方数量 | number(16,6) | Y |  |
| 33 | P05_DR_TRANS_AMT | 期间5-借方金额-原币 | number(23,8) | Y |  |
| 34 | P05_DR_FUNCTION_AMT | 期间5-借方金额-本币 | number(23,8) | Y |  |
| 35 | P05_CR_QTY | 期间5-贷方数量 | number(16,6) | Y |  |
| 36 | P05_CR_TRANS_AMT | 期间5-贷方金额-原币 | number(23,8) | Y |  |
| 37 | P05_CR_FUNCTION_AMT | 期间5-贷方金额-本币 | number(23,8) | Y |  |
| 38 | P06_DR_QTY | 期间6-借方数量 | number(16,6) | Y |  |
| 39 | P06_DR_TRANS_AMT | 期间6-借方金额-原币 | number(23,8) | Y |  |
| 40 | P06_DR_FUNCTION_AMT | 期间6-借方金额-本币 | number(23,8) | Y |  |
| 41 | P06_CR_QTY | 期间6-贷方数量 | number(16,6) | Y |  |
| 42 | P06_CR_TRANS_AMT | 期间6-贷方金额-原币 | number(23,8) | Y |  |
| 43 | P06_CR_FUNCTION_AMT | 期间6-贷方金额-本币 | number(23,8) | Y |  |
| 44 | P07_DR_QTY | 期间7-借方数量 | number(16,6) | Y |  |
| 45 | P07_DR_TRANS_AMT | 期间7-借方金额-原币 | number(23,8) | Y |  |
| 46 | P07_DR_FUNCTION_AMT | 期间7-借方金额-本币 | number(23,8) | Y |  |
| 47 | P07_CR_QTY | 期间7-贷方数量 | number(16,6) | Y |  |
| 48 | P07_CR_TRANS_AMT | 期间7-贷方金额-原币 | number(23,8) | Y |  |
| 49 | P07_CR_FUNCTION_AMT | 期间7-贷方金额-本币 | number(23,8) | Y |  |
| 50 | P08_DR_QTY | 期间8-借方数量 | number(16,6) | Y |  |
| 51 | P08_DR_TRANS_AMT | 期间8-借方金额-原币 | number(23,8) | Y |  |
| 52 | P08_DR_FUNCTION_AMT | 期间8-借方金额-本币 | number(23,8) | Y |  |
| 53 | P08_CR_QTY | 期间8-贷方数量 | number(16,6) | Y |  |
| 54 | P08_CR_TRANS_AMT | 期间8-贷方金额-原币 | number(23,8) | Y |  |
| 55 | P08_CR_FUNCTION_AMT | 期间8-贷方金额-本币 | number(23,8) | Y |  |
| 56 | P09_DR_QTY | 期间9-借方数量 | number(16,6) | Y |  |
| 57 | P09_DR_TRANS_AMT | 期间9-借方金额-原币 | number(23,8) | Y |  |
| 58 | P09_DR_FUNCTION_AMT | 期间9-借方金额-本币 | number(23,8) | Y |  |
| 59 | P09_CR_QTY | 期间9-贷方数量 | number(16,6) | Y |  |
| 60 | P09_CR_TRANS_AMT | 期间9-贷方金额-原币 | number(23,8) | Y |  |
| 61 | P09_CR_FUNCTION_AMT | 期间9-贷方金额-本币 | number(23,8) | Y |  |
| 62 | P10_DR_QTY | 期间10-借方数量 | number(16,6) | Y |  |
| 63 | P10_DR_TRANS_AMT | 期间10-借方金额-原币 | number(23,8) | Y |  |
| 64 | P10_DR_FUNCTION_AMT | 期间10-借方金额-本币 | number(23,8) | Y |  |
| 65 | P10_CR_QTY | 期间10-贷方数量 | number(16,6) | Y |  |
| 66 | P10_CR_TRANS_AMT | 期间10-贷方金额-原币 | number(23,8) | Y |  |
| 67 | P10_CR_FUNCTION_AMT | 期间10-贷方金额-本币 | number(23,8) | Y |  |
| 68 | P11_DR_QTY | 期间11-借方数量 | number(16,6) | Y |  |
| 69 | P11_DR_TRANS_AMT | 期间11-借方金额-原币 | number(23,8) | Y |  |
| 70 | P11_DR_FUNCTION_AMT | 期间11-借方金额-本币 | number(23,8) | Y |  |
| 71 | P11_CR_QTY | 期间11-贷方数量 | number(16,6) | Y |  |
| 72 | P11_CR_TRANS_AMT | 期间11-贷方金额-原币 | number(23,8) | Y |  |
| 73 | P11_CR_FUNCTION_AMT | 期间11-贷方金额-本币 | number(23,8) | Y |  |
| 74 | P12_DR_QTY | 期间12-借方数量 | number(16,6) | Y |  |
| 75 | P12_DR_TRANS_AMT | 期间12-借方金额-原币 | number(23,8) | Y |  |
| 76 | P12_DR_FUNCTION_AMT | 期间12-借方金额-本币 | number(23,8) | Y |  |
| 77 | P12_CR_QTY | 期间12-贷方数量 | number(16,6) | Y |  |
| 78 | P12_CR_TRANS_AMT | 期间12-贷方金额-原币 | number(23,8) | Y |  |
| 79 | P12_CR_FUNCTION_AMT | 期间12-贷方金额-本币 | number(23,8) | Y |  |
| 80 | P13_DR_QTY | 期间13-借方数量 | number(16,6) | Y |  |
| 81 | P13_DR_TRANS_AMT | 期间13-借方金额-原币 | number(23,8) | Y |  |
| 82 | P13_DR_FUNCTION_AMT | 期间13-借方金额-本币 | number(23,8) | Y |  |
| 83 | P13_CR_QTY | 期间13-贷方数量 | number(16,6) | Y |  |
| 84 | P13_CR_TRANS_AMT | 期间13-贷方金额-原币 | number(23,8) | Y |  |
| 85 | P13_CR_FUNCTION_AMT | 期间13-贷方金额-本币 | number(23,8) | Y |  |
| 86 | P14_DR_QTY | 期间14-借方数量 | number(16,6) | Y |  |
| 87 | P14_DR_TRANS_AMT | 期间14-借方金额-原币 | number(23,8) | Y |  |
| 88 | P14_DR_FUNCTION_AMT | 期间14-借方金额-本币 | number(23,8) | Y |  |
| 89 | P14_CR_QTY | 期间14-贷方数量 | number(16,6) | Y |  |
| 90 | P14_CR_TRANS_AMT | 期间14-贷方金额-原币 | number(23,8) | Y |  |
| 91 | P14_CR_FUNCTION_AMT | 期间14-贷方金额-本币 | number(23,8) | Y |  |
| 92 | P15_DR_QTY | 期间15-借方数量 | number(16,6) | Y |  |
| 93 | P15_DR_TRANS_AMT | 期间15-借方金额-原币 | number(23,8) | Y |  |
| 94 | P15_DR_FUNCTION_AMT | 期间15-借方金额-本币 | number(23,8) | Y |  |
| 95 | P15_CR_QTY | 期间15-贷方数量 | number(16,6) | Y |  |
| 96 | P15_CR_TRANS_AMT | 期间15-贷方金额-原币 | number(23,8) | Y |  |
| 97 | P15_CR_FUNCTION_AMT | 期间15-贷方金额-本币 | number(23,8) | Y |  |
| 98 | P16_DR_QTY | 期间16-借方数量 | number(16,6) | Y |  |
| 99 | P16_DR_TRANS_AMT | 期间16-借方金额-原币 | number(23,8) | Y |  |
| 100 | P16_DR_FUNCTION_AMT | 期间16-借方金额-本币 | number(23,8) | Y |  |
| 101 | P16_CR_QTY | 期间16-贷方数量 | number(16,6) | Y |  |
| 102 | P16_CR_TRANS_AMT | 期间16-贷方金额-原币 | number(23,8) | Y |  |
| 103 | P16_CR_FUNCTION_AMT | 期间16-贷方金额-本币 | number(23,8) | Y |  |
| 104 | P17_DR_QTY | 期间17-借方数量 | number(16,6) | Y |  |
| 105 | P17_DR_TRANS_AMT | 期间17-借方金额-原币 | number(23,8) | Y |  |
| 106 | P17_DR_FUNCTION_AMT | 期间17-借方金额-本币 | number(23,8) | Y |  |
| 107 | P17_CR_QTY | 期间17-贷方数量 | number(16,6) | Y |  |
| 108 | P17_CR_TRANS_AMT | 期间17-贷方金额-原币 | number(23,8) | Y |  |
| 109 | P17_CR_FUNCTION_AMT | 期间17-贷方金额-本币 | number(23,8) | Y |  |
| 110 | P18_DR_QTY | 期间18-借方数量 | number(16,6) | Y |  |
| 111 | P18_DR_TRANS_AMT | 期间18-借方金额-原币 | number(23,8) | Y |  |
| 112 | P18_DR_FUNCTION_AMT | 期间18-借方金额-本币 | number(23,8) | Y |  |
| 113 | P18_CR_QTY | 期间18-贷方数量 | number(16,6) | Y |  |
| 114 | P18_CR_TRANS_AMT | 期间18-贷方金额-原币 | number(23,8) | Y |  |
| 115 | P18_CR_FUNCTION_AMT | 期间18-贷方金额-本币 | number(23,8) | Y |  |
| 116 | P19_DR_QTY | 期间19-借方数量 | number(16,6) | Y |  |
| 117 | P19_DR_TRANS_AMT | 期间19-借方金额-原币 | number(23,8) | Y |  |
| 118 | P19_DR_FUNCTION_AMT | 期间19-借方金额-本币 | number(23,8) | Y |  |
| 119 | P19_CR_QTY | 期间19-贷方数量 | number(16,6) | Y |  |
| 120 | P19_CR_TRANS_AMT | 期间19-贷方金额-原币 | number(23,8) | Y |  |
| 121 | P19_CR_FUNCTION_AMT | 期间19-贷方金额-本币 | number(23,8) | Y |  |
| 122 | P20_DR_QTY | 期间20-借方数量 | number(16,6) | Y |  |
| 123 | P20_DR_TRANS_AMT | 期间20-借方金额-原币 | number(23,8) | Y |  |
| 124 | P20_DR_FUNCTION_AMT | 期间20-借方金额-本币 | number(23,8) | Y |  |
| 125 | P20_CR_QTY | 期间20-贷方数量 | number(16,6) | Y |  |
| 126 | P20_CR_TRANS_AMT | 期间20-贷方金额-原币 | number(23,8) | Y |  |
| 127 | P20_CR_FUNCTION_AMT | 期间20-贷方金额-本币 | number(23,8) | Y |  |
| 128 | P21_DR_QTY | 期间21-借方数量 | number(16,6) | Y |  |
| 129 | P21_DR_TRANS_AMT | 期间21-借方金额-原币 | number(23,8) | Y |  |
| 130 | P21_DR_FUNCTION_AMT | 期间21-借方金额-本币 | number(23,8) | Y |  |
| 131 | P21_CR_QTY | 期间21-贷方数量 | number(16,6) | Y |  |
| 132 | P21_CR_TRANS_AMT | 期间21-贷方金额-原币 | number(23,8) | Y |  |
| 133 | P21_CR_FUNCTION_AMT | 期间21-贷方金额-本币 | number(23,8) | Y |  |
| 134 | P22_DR_QTY | 期间22-借方数量 | number(16,6) | Y |  |
| 135 | P22_DR_TRANS_AMT | 期间22-借方金额-原币 | number(23,8) | Y |  |
| 136 | P22_DR_FUNCTION_AMT | 期间22-借方金额-本币 | number(23,8) | Y |  |
| 137 | P22_CR_QTY | 期间22-贷方数量 | number(16,6) | Y |  |
| 138 | P22_CR_TRANS_AMT | 期间22-贷方金额-原币 | number(23,8) | Y |  |
| 139 | P22_CR_FUNCTION_AMT | 期间22-贷方金额-本币 | number(23,8) | Y |  |
| 140 | P23_DR_QTY | 期间23-借方数量 | number(16,6) | Y |  |
| 141 | P23_DR_TRANS_AMT | 期间23-借方金额-原币 | number(23,8) | Y |  |
| 142 | P23_DR_FUNCTION_AMT | 期间23-借方金额-本币 | number(23,8) | Y |  |
| 143 | P23_CR_QTY | 期间23-贷方数量 | number(16,6) | Y |  |
| 144 | P23_CR_TRANS_AMT | 期间23-贷方金额-原币 | number(23,8) | Y |  |
| 145 | P23_CR_FUNCTION_AMT | 期间23-贷方金额-本币 | number(23,8) | Y |  |
| 146 | P24_DR_QTY | 期间24-借方数量 | number(16,6) | Y |  |
| 147 | P24_DR_TRANS_AMT | 期间24-借方金额-原币 | number(23,8) | Y |  |
| 148 | P24_DR_FUNCTION_AMT | 期间24-借方金额-本币 | number(23,8) | Y |  |
| 149 | P24_CR_QTY | 期间24-贷方数量 | number(16,6) | Y |  |
| 150 | P24_CR_TRANS_AMT | 期间24-贷方金额-原币 | number(23,8) | Y |  |
| 151 | P24_CR_FUNCTION_AMT | 期间24-贷方金额-本币 | number(23,8) | Y |  |
| 152 | P25_DR_QTY | 期间25-借方数量 | number(16,6) | Y |  |
| 153 | P25_DR_TRANS_AMT | 期间25-借方金额-原币 | number(23,8) | Y |  |
| 154 | P25_DR_FUNCTION_AMT | 期间25-借方金额-本币 | number(23,8) | Y |  |
| 155 | P25_CR_QTY | 期间25-贷方数量 | number(16,6) | Y |  |
| 156 | P25_CR_TRANS_AMT | 期间25-贷方金额-原币 | number(23,8) | Y |  |
| 157 | P25_CR_FUNCTION_AMT | 期间25-贷方金额-本币 | number(23,8) | Y |  |
| 158 | P26_DR_QTY | 期间26-借方数量 | number(16,6) | Y |  |
| 159 | P26_DR_TRANS_AMT | 期间26-借方金额-原币 | number(23,8) | Y |  |
| 160 | P26_DR_FUNCTION_AMT | 期间26-借方金额-本币 | number(23,8) | Y |  |
| 161 | P26_CR_QTY | 期间26-贷方数量 | number(16,6) | Y |  |
| 162 | P26_CR_TRANS_AMT | 期间26-贷方金额-原币 | number(23,8) | Y |  |
| 163 | P26_CR_FUNCTION_AMT | 期间26-贷方金额-本币 | number(23,8) | Y |  |
| 164 | P27_DR_QTY | 期间27-借方数量 | number(16,6) | Y |  |
| 165 | P27_DR_TRANS_AMT | 期间27-借方金额-原币 | number(23,8) | Y |  |
| 166 | P27_DR_FUNCTION_AMT | 期间27-借方金额-本币 | number(23,8) | Y |  |
| 167 | P27_CR_QTY | 期间27-贷方数量 | number(16,6) | Y |  |
| 168 | P27_CR_TRANS_AMT | 期间27-贷方金额-原币 | number(23,8) | Y |  |
| 169 | P27_CR_FUNCTION_AMT | 期间27-贷方金额-本币 | number(23,8) | Y |  |
| 170 | P28_DR_QTY | 期间28-借方数量 | number(16,6) | Y |  |
| 171 | P28_DR_TRANS_AMT | 期间28-借方金额-原币 | number(23,8) | Y |  |
| 172 | P28_DR_FUNCTION_AMT | 期间28-借方金额-本币 | number(23,8) | Y |  |
| 173 | P28_CR_QTY | 期间28-贷方数量 | number(16,6) | Y |  |
| 174 | P28_CR_TRANS_AMT | 期间28-贷方金额-原币 | number(23,8) | Y |  |
| 175 | P28_CR_FUNCTION_AMT | 期间28-贷方金额-本币 | number(23,8) | Y |  |
| 176 | P29_DR_QTY | 期间29-借方数量 | number(16,6) | Y |  |
| 177 | P29_DR_TRANS_AMT | 期间29-借方金额-原币 | number(23,8) | Y |  |
| 178 | P29_DR_FUNCTION_AMT | 期间29-借方金额-本币 | number(23,8) | Y |  |
| 179 | P29_CR_QTY | 期间29-贷方数量 | number(16,6) | Y |  |
| 180 | P29_CR_TRANS_AMT | 期间29-贷方金额-原币 | number(23,8) | Y |  |
| 181 | P29_CR_FUNCTION_AMT | 期间29-贷方金额-本币 | number(23,8) | Y |  |
| 182 | P30_DR_QTY | 期间30-借方数量 | number(16,6) | Y |  |
| 183 | P30_DR_TRANS_AMT | 期间30-借方金额-原币 | number(23,8) | Y |  |
| 184 | P30_DR_FUNCTION_AMT | 期间30-借方金额-本币 | number(23,8) | Y |  |
| 185 | P30_CR_QTY | 期间30-贷方数量 | number(16,6) | Y |  |
| 186 | P30_CR_TRANS_AMT | 期间30-贷方金额-原币 | number(23,8) | Y |  |
| 187 | P30_CR_FUNCTION_AMT | 期间30-贷方金额-本币 | number(23,8) | Y |  |
| 188 | P31_DR_QTY | 期间31-借方数量 | number(16,6) | Y |  |
| 189 | P31_DR_TRANS_AMT | 期间31-借方金额-原币 | number(23,8) | Y |  |
| 190 | P31_DR_FUNCTION_AMT | 期间31-借方金额-本币 | number(23,8) | Y |  |
| 191 | P31_CR_QTY | 期间31-贷方数量 | number(16,6) | Y |  |
| 192 | P31_CR_TRANS_AMT | 期间31-贷方金额-原币 | number(23,8) | Y |  |
| 193 | P31_CR_FUNCTION_AMT | 期间31-贷方金额-本币 | number(23,8) | Y |  |
| 194 | P32_DR_QTY | 期间32-借方数量 | number(16,6) | Y |  |
| 195 | P32_DR_TRANS_AMT | 期间32-借方金额-原币 | number(23,8) | Y |  |
| 196 | P32_DR_FUNCTION_AMT | 期间32-借方金额-本币 | number(23,8) | Y |  |
| 197 | P32_CR_QTY | 期间32-贷方数量 | number(16,6) | Y |  |
| 198 | P32_CR_TRANS_AMT | 期间32-贷方金额-原币 | number(23,8) | Y |  |
| 199 | P32_CR_FUNCTION_AMT | 期间32-贷方金额-本币 | number(23,8) | Y |  |
| 200 | P33_DR_QTY | 期间33-借方数量 | number(16,6) | Y |  |
| 201 | P33_DR_TRANS_AMT | 期间33-借方金额-原币 | number(23,8) | Y |  |
| 202 | P33_DR_FUNCTION_AMT | 期间33-借方金额-本币 | number(23,8) | Y |  |
| 203 | P33_CR_QTY | 期间33-贷方数量 | number(16,6) | Y |  |
| 204 | P33_CR_TRANS_AMT | 期间33-贷方金额-原币 | number(23,8) | Y |  |
| 205 | P33_CR_FUNCTION_AMT | 期间33-贷方金额-本币 | number(23,8) | Y |  |
| 206 | P34_DR_QTY | 期间34-借方数量 | number(16,6) | Y |  |
| 207 | P34_DR_TRANS_AMT | 期间34-借方金额-原币 | number(23,8) | Y |  |
| 208 | P34_DR_FUNCTION_AMT | 期间34-借方金额-本币 | number(23,8) | Y |  |
| 209 | P34_CR_QTY | 期间34-贷方数量 | number(16,6) | Y |  |
| 210 | P34_CR_TRANS_AMT | 期间34-贷方金额-原币 | number(23,8) | Y |  |
| 211 | P34_CR_FUNCTION_AMT | 期间34-贷方金额-本币 | number(23,8) | Y |  |
| 212 | P35_DR_QTY | 期间35-借方数量 | number(16,6) | Y |  |
| 213 | P35_DR_TRANS_AMT | 期间35-借方金额-原币 | number(23,8) | Y |  |
| 214 | P35_DR_FUNCTION_AMT | 期间35-借方金额-本币 | number(23,8) | Y |  |
| 215 | P35_CR_QTY | 期间35-贷方数量 | number(16,6) | Y |  |
| 216 | P35_CR_TRANS_AMT | 期间35-贷方金额-原币 | number(23,8) | Y |  |
| 217 | P35_CR_FUNCTION_AMT | 期间35-贷方金额-本币 | number(23,8) | Y |  |
| 218 | P36_DR_QTY | 期间36-借方数量 | number(16,6) | Y |  |
| 219 | P36_DR_TRANS_AMT | 期间36-借方金额-原币 | number(23,8) | Y |  |
| 220 | P36_DR_FUNCTION_AMT | 期间36-借方金额-本币 | number(23,8) | Y |  |
| 221 | P36_CR_QTY | 期间36-贷方数量 | number(16,6) | Y |  |
| 222 | P36_CR_TRANS_AMT | 期间36-贷方金额-原币 | number(23,8) | Y |  |
| 223 | P36_CR_FUNCTION_AMT | 期间36-贷方金额-本币 | number(23,8) | Y |  |
| 224 | PERIOD_OPENING_QTY | 启用期间-期初余额-数量 | number(16,6) | Y |  |
| 225 | PERIOD_OPENING_TRANS_AMT | 启用期间-期初余额-原币 | number(23,8) | Y |  |
| 226 | PERIOD_OPENING_FUNCTION_AMT | 启用期间-期初余额-本币 | number(23,8) | Y |  |
| 227 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 228 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 229 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 230 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 231 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 232 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 233 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 234 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 235 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 236 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 237 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 238 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 239 | UDF041 | 自定义字段12 | date | Y |  |
| 240 | UDF042 | 自定义字段13 | date | Y |  |
| 241 | UDF051 | 自定义字段14 | GUID | Y |  |
| 242 | UDF052 | 自定义字段15 | GUID | Y |  |
| 243 | UDF053 | 自定义字段16 | GUID | Y |  |
| 244 | UDF054 | 自定义字段17 | GUID | Y |  |
| 245 | CreateDate | 创建日期 | date | Y |  |
| 246 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 247 | ModifiedDate | 修改日期 | date | Y |  |
| 248 | CreateBy | 创建者 | GUID | Y |  |
| 249 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 250 | ModifiedBy | 修改者 | GUID | Y |  |
| 251 | ACCOUNT_INITIAL_ID |  | GUID | Y |  |

### ACCOUNT_INITIAL_SD (科目初始数据子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ACCOUNT_INITIAL_SD_ID | 主键 | GUID | Y | Y |
| 3 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 4 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 5 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 6 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 7 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 8 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 9 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 10 | PROJECT_ID | 项目 | GUID | Y |  |
| 11 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 12 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 13 | BALANCE_DIRECTION | 平衡方向(借/贷) | number | Y |  |
| 14 | YEAR_OPENING_QTY | 年初余额-数量 | number(16,6) | Y |  |
| 15 | YEAR_OPENING_TRANS_AMT | 年初余额-原币 | number(23,8) | Y |  |
| 16 | YEAR_OPENING_FUNCTION_AMT | 年初余额-本币 | number(23,8) | Y |  |
| 17 | P01_DR_QTY | 期间1-借方数量 | number(16,6) | Y |  |
| 18 | P01_DR_TRANS_AMT | 期间1-借方金额-原币 | number(23,8) | Y |  |
| 19 | P01_DR_FUNCTION_AMT | 期间1-借方金额-本币 | number(23,8) | Y |  |
| 20 | P01_CR_QTY | 期间1-贷方数量 | number(16,6) | Y |  |
| 21 | P01_CR_TRANS_AMT | 期间1-贷方金额-原币 | number(23,8) | Y |  |
| 22 | P01_CR_FUNCTION_AMT | 期间1-贷方金额-本币 | number(23,8) | Y |  |
| 23 | P02_DR_QTY | 期间2-借方数量 | number(16,6) | Y |  |
| 24 | P02_DR_TRANS_AMT | 期间2-借方金额-原币 | number(23,8) | Y |  |
| 25 | P02_DR_FUNCTION_AMT | 期间2-借方金额-本币 | number(23,8) | Y |  |
| 26 | P02_CR_QTY | 期间2-贷方数量 | number(16,6) | Y |  |
| 27 | P02_CR_TRANS_AMT | 期间2-贷方金额-原币 | number(23,8) | Y |  |
| 28 | P02_CR_FUNCTION_AMT | 期间2-贷方金额-本币 | number(23,8) | Y |  |
| 29 | P03_DR_QTY | 期间3-借方数量 | number(16,6) | Y |  |
| 30 | P03_DR_TRANS_AMT | 期间3-借方金额-原币 | number(23,8) | Y |  |
| 31 | P03_DR_FUNCTION_AMT | 期间3-借方金额-本币 | number(23,8) | Y |  |
| 32 | P03_CR_QTY | 期间3-贷方数量 | number(16,6) | Y |  |
| 33 | P03_CR_TRANS_AMT | 期间3-贷方金额-原币 | number(23,8) | Y |  |
| 34 | P03_CR_FUNCTION_AMT | 期间3-贷方金额-本币 | number(23,8) | Y |  |
| 35 | P04_DR_QTY | 期间4-借方数量 | number(16,6) | Y |  |
| 36 | P04_DR_TRANS_AMT | 期间4-借方金额-原币 | number(23,8) | Y |  |
| 37 | P04_DR_FUNCTION_AMT | 期间4-借方金额-本币 | number(23,8) | Y |  |
| 38 | P04_CR_QTY | 期间4-贷方数量 | number(16,6) | Y |  |
| 39 | P04_CR_TRANS_AMT | 期间4-贷方金额-原币 | number(23,8) | Y |  |
| 40 | P04_CR_FUNCTION_AMT | 期间4-贷方金额-本币 | number(23,8) | Y |  |
| 41 | P05_DR_QTY | 期间5-借方数量 | number(16,6) | Y |  |
| 42 | P05_DR_TRANS_AMT | 期间5-借方金额-原币 | number(23,8) | Y |  |
| 43 | P05_DR_FUNCTION_AMT | 期间5-借方金额-本币 | number(23,8) | Y |  |
| 44 | P05_CR_QTY | 期间5-贷方数量 | number(16,6) | Y |  |
| 45 | P05_CR_TRANS_AMT | 期间5-贷方金额-原币 | number(23,8) | Y |  |
| 46 | P05_CR_FUNCTION_AMT | 期间5-贷方金额-本币 | number(23,8) | Y |  |
| 47 | P06_DR_QTY | 期间6-借方数量 | number(16,6) | Y |  |
| 48 | P06_DR_TRANS_AMT | 期间6-借方金额-原币 | number(23,8) | Y |  |
| 49 | P06_DR_FUNCTION_AMT | 期间6-借方金额-本币 | number(23,8) | Y |  |
| 50 | P06_CR_QTY | 期间6-贷方数量 | number(16,6) | Y |  |
| 51 | P06_CR_TRANS_AMT | 期间6-贷方金额-原币 | number(23,8) | Y |  |
| 52 | P06_CR_FUNCTION_AMT | 期间6-贷方金额-本币 | number(23,8) | Y |  |
| 53 | P07_DR_QTY | 期间7-借方数量 | number(16,6) | Y |  |
| 54 | P07_DR_TRANS_AMT | 期间7-借方金额-原币 | number(23,8) | Y |  |
| 55 | P07_DR_FUNCTION_AMT | 期间7-借方金额-本币 | number(23,8) | Y |  |
| 56 | P07_CR_QTY | 期间7-贷方数量 | number(16,6) | Y |  |
| 57 | P07_CR_TRANS_AMT | 期间7-贷方金额-原币 | number(23,8) | Y |  |
| 58 | P07_CR_FUNCTION_AMT | 期间7-贷方金额-本币 | number(23,8) | Y |  |
| 59 | P08_DR_QTY | 期间8-借方数量 | number(16,6) | Y |  |
| 60 | P08_DR_TRANS_AMT | 期间8-借方金额-原币 | number(23,8) | Y |  |
| 61 | P08_DR_FUNCTION_AMT | 期间8-借方金额-本币 | number(23,8) | Y |  |
| 62 | P08_CR_QTY | 期间8-贷方数量 | number(16,6) | Y |  |
| 63 | P08_CR_TRANS_AMT | 期间8-贷方金额-原币 | number(23,8) | Y |  |
| 64 | P08_CR_FUNCTION_AMT | 期间8-贷方金额-本币 | number(23,8) | Y |  |
| 65 | P09_DR_QTY | 期间9-借方数量 | number(16,6) | Y |  |
| 66 | P09_DR_TRANS_AMT | 期间9-借方金额-原币 | number(23,8) | Y |  |
| 67 | P09_DR_FUNCTION_AMT | 期间9-借方金额-本币 | number(23,8) | Y |  |
| 68 | P09_CR_QTY | 期间9-贷方数量 | number(16,6) | Y |  |
| 69 | P09_CR_TRANS_AMT | 期间9-贷方金额-原币 | number(23,8) | Y |  |
| 70 | P09_CR_FUNCTION_AMT | 期间9-贷方金额-本币 | number(23,8) | Y |  |
| 71 | P10_DR_QTY | 期间10-借方数量 | number(16,6) | Y |  |
| 72 | P10_DR_TRANS_AMT | 期间10-借方金额-原币 | number(23,8) | Y |  |
| 73 | P10_DR_FUNCTION_AMT | 期间10-借方金额-本币 | number(23,8) | Y |  |
| 74 | P10_CR_QTY | 期间10-贷方数量 | number(16,6) | Y |  |
| 75 | P10_CR_TRANS_AMT | 期间10-贷方金额-原币 | number(23,8) | Y |  |
| 76 | P10_CR_FUNCTION_AMT | 期间10-贷方金额-本币 | number(23,8) | Y |  |
| 77 | P11_DR_QTY | 期间11-借方数量 | number(16,6) | Y |  |
| 78 | P11_DR_TRANS_AMT | 期间11-借方金额-原币 | number(23,8) | Y |  |
| 79 | P11_DR_FUNCTION_AMT | 期间11-借方金额-本币 | number(23,8) | Y |  |
| 80 | P11_CR_QTY | 期间11-贷方数量 | number(16,6) | Y |  |
| 81 | P11_CR_TRANS_AMT | 期间11-贷方金额-原币 | number(23,8) | Y |  |
| 82 | P11_CR_FUNCTION_AMT | 期间11-贷方金额-本币 | number(23,8) | Y |  |
| 83 | P12_DR_QTY | 期间12-借方数量 | number(16,6) | Y |  |
| 84 | P12_DR_TRANS_AMT | 期间12-借方金额-原币 | number(23,8) | Y |  |
| 85 | P12_DR_FUNCTION_AMT | 期间12-借方金额-本币 | number(23,8) | Y |  |
| 86 | P12_CR_QTY | 期间12-贷方数量 | number(16,6) | Y |  |
| 87 | P12_CR_TRANS_AMT | 期间12-贷方金额-原币 | number(23,8) | Y |  |
| 88 | P12_CR_FUNCTION_AMT | 期间12-贷方金额-本币 | number(23,8) | Y |  |
| 89 | P13_DR_QTY | 期间13-借方数量 | number(16,6) | Y |  |
| 90 | P13_DR_TRANS_AMT | 期间13-借方金额-原币 | number(23,8) | Y |  |
| 91 | P13_DR_FUNCTION_AMT | 期间13-借方金额-本币 | number(23,8) | Y |  |
| 92 | P13_CR_QTY | 期间13-贷方数量 | number(16,6) | Y |  |
| 93 | P13_CR_TRANS_AMT | 期间13-贷方金额-原币 | number(23,8) | Y |  |
| 94 | P13_CR_FUNCTION_AMT | 期间13-贷方金额-本币 | number(23,8) | Y |  |
| 95 | P14_DR_QTY | 期间14-借方数量 | number(16,6) | Y |  |
| 96 | P14_DR_TRANS_AMT | 期间14-借方金额-原币 | number(23,8) | Y |  |
| 97 | P14_DR_FUNCTION_AMT | 期间14-借方金额-本币 | number(23,8) | Y |  |
| 98 | P14_CR_QTY | 期间14-贷方数量 | number(16,6) | Y |  |
| 99 | P14_CR_TRANS_AMT | 期间14-贷方金额-原币 | number(23,8) | Y |  |
| 100 | P14_CR_FUNCTION_AMT | 期间14-贷方金额-本币 | number(23,8) | Y |  |
| 101 | P15_DR_QTY | 期间15-借方数量 | number(16,6) | Y |  |
| 102 | P15_DR_TRANS_AMT | 期间15-借方金额-原币 | number(23,8) | Y |  |
| 103 | P15_DR_FUNCTION_AMT | 期间15-借方金额-本币 | number(23,8) | Y |  |
| 104 | P15_CR_QTY | 期间15-贷方数量 | number(16,6) | Y |  |
| 105 | P15_CR_TRANS_AMT | 期间15-贷方金额-原币 | number(23,8) | Y |  |
| 106 | P15_CR_FUNCTION_AMT | 期间15-贷方金额-本币 | number(23,8) | Y |  |
| 107 | P16_DR_QTY | 期间16-借方数量 | number(16,6) | Y |  |
| 108 | P16_DR_TRANS_AMT | 期间16-借方金额-原币 | number(23,8) | Y |  |
| 109 | P16_DR_FUNCTION_AMT | 期间16-借方金额-本币 | number(23,8) | Y |  |
| 110 | P16_CR_QTY | 期间16-贷方数量 | number(16,6) | Y |  |
| 111 | P16_CR_TRANS_AMT | 期间16-贷方金额-原币 | number(23,8) | Y |  |
| 112 | P16_CR_FUNCTION_AMT | 期间16-贷方金额-本币 | number(23,8) | Y |  |
| 113 | P17_DR_QTY | 期间17-借方数量 | number(16,6) | Y |  |
| 114 | P17_DR_TRANS_AMT | 期间17-借方金额-原币 | number(23,8) | Y |  |
| 115 | P17_DR_FUNCTION_AMT | 期间17-借方金额-本币 | number(23,8) | Y |  |
| 116 | P17_CR_QTY | 期间17-贷方数量 | number(16,6) | Y |  |
| 117 | P17_CR_TRANS_AMT | 期间17-贷方金额-原币 | number(23,8) | Y |  |
| 118 | P17_CR_FUNCTION_AMT | 期间17-贷方金额-本币 | number(23,8) | Y |  |
| 119 | P18_DR_QTY | 期间18-借方数量 | number(16,6) | Y |  |
| 120 | P18_DR_TRANS_AMT | 期间18-借方金额-原币 | number(23,8) | Y |  |
| 121 | P18_DR_FUNCTION_AMT | 期间18-借方金额-本币 | number(23,8) | Y |  |
| 122 | P18_CR_QTY | 期间18-贷方数量 | number(16,6) | Y |  |
| 123 | P18_CR_TRANS_AMT | 期间18-贷方金额-原币 | number(23,8) | Y |  |
| 124 | P18_CR_FUNCTION_AMT | 期间18-贷方金额-本币 | number(23,8) | Y |  |
| 125 | P19_DR_QTY | 期间19-借方数量 | number(16,6) | Y |  |
| 126 | P19_DR_TRANS_AMT | 期间19-借方金额-原币 | number(23,8) | Y |  |
| 127 | P19_DR_FUNCTION_AMT | 期间19-借方金额-本币 | number(23,8) | Y |  |
| 128 | P19_CR_QTY | 期间19-贷方数量 | number(16,6) | Y |  |
| 129 | P19_CR_TRANS_AMT | 期间19-贷方金额-原币 | number(23,8) | Y |  |
| 130 | P19_CR_FUNCTION_AMT | 期间19-贷方金额-本币 | number(23,8) | Y |  |
| 131 | P20_DR_QTY | 期间20-借方数量 | number(16,6) | Y |  |
| 132 | P20_DR_TRANS_AMT | 期间20-借方金额-原币 | number(23,8) | Y |  |
| 133 | P20_DR_FUNCTION_AMT | 期间20-借方金额-本币 | number(23,8) | Y |  |
| 134 | P20_CR_QTY | 期间20-贷方数量 | number(16,6) | Y |  |
| 135 | P20_CR_TRANS_AMT | 期间20-贷方金额-原币 | number(23,8) | Y |  |
| 136 | P20_CR_FUNCTION_AMT | 期间20-贷方金额-本币 | number(23,8) | Y |  |
| 137 | P21_DR_QTY | 期间21-借方数量 | number(16,6) | Y |  |
| 138 | P21_DR_TRANS_AMT | 期间21-借方金额-原币 | number(23,8) | Y |  |
| 139 | P21_DR_FUNCTION_AMT | 期间21-借方金额-本币 | number(23,8) | Y |  |
| 140 | P21_CR_QTY | 期间21-贷方数量 | number(16,6) | Y |  |
| 141 | P21_CR_TRANS_AMT | 期间21-贷方金额-原币 | number(23,8) | Y |  |
| 142 | P21_CR_FUNCTION_AMT | 期间21-贷方金额-本币 | number(23,8) | Y |  |
| 143 | P22_DR_QTY | 期间22-借方数量 | number(16,6) | Y |  |
| 144 | P22_DR_TRANS_AMT | 期间22-借方金额-原币 | number(23,8) | Y |  |
| 145 | P22_DR_FUNCTION_AMT | 期间22-借方金额-本币 | number(23,8) | Y |  |
| 146 | P22_CR_QTY | 期间22-贷方数量 | number(16,6) | Y |  |
| 147 | P22_CR_TRANS_AMT | 期间22-贷方金额-原币 | number(23,8) | Y |  |
| 148 | P22_CR_FUNCTION_AMT | 期间22-贷方金额-本币 | number(23,8) | Y |  |
| 149 | P23_DR_QTY | 期间23-借方数量 | number(16,6) | Y |  |
| 150 | P23_DR_TRANS_AMT | 期间23-借方金额-原币 | number(23,8) | Y |  |
| 151 | P23_DR_FUNCTION_AMT | 期间23-借方金额-本币 | number(23,8) | Y |  |
| 152 | P23_CR_QTY | 期间23-贷方数量 | number(16,6) | Y |  |
| 153 | P23_CR_TRANS_AMT | 期间23-贷方金额-原币 | number(23,8) | Y |  |
| 154 | P23_CR_FUNCTION_AMT | 期间23-贷方金额-本币 | number(23,8) | Y |  |
| 155 | P24_DR_QTY | 期间24-借方数量 | number(16,6) | Y |  |
| 156 | P24_DR_TRANS_AMT | 期间24-借方金额-原币 | number(23,8) | Y |  |
| 157 | P24_DR_FUNCTION_AMT | 期间24-借方金额-本币 | number(23,8) | Y |  |
| 158 | P24_CR_QTY | 期间24-贷方数量 | number(16,6) | Y |  |
| 159 | P24_CR_TRANS_AMT | 期间24-贷方金额-原币 | number(23,8) | Y |  |
| 160 | P24_CR_FUNCTION_AMT | 期间24-贷方金额-本币 | number(23,8) | Y |  |
| 161 | P25_DR_QTY | 期间25-借方数量 | number(16,6) | Y |  |
| 162 | P25_DR_TRANS_AMT | 期间25-借方金额-原币 | number(23,8) | Y |  |
| 163 | P25_DR_FUNCTION_AMT | 期间25-借方金额-本币 | number(23,8) | Y |  |
| 164 | P25_CR_QTY | 期间25-贷方数量 | number(16,6) | Y |  |
| 165 | P25_CR_TRANS_AMT | 期间25-贷方金额-原币 | number(23,8) | Y |  |
| 166 | P25_CR_FUNCTION_AMT | 期间25-贷方金额-本币 | number(23,8) | Y |  |
| 167 | P26_DR_QTY | 期间26-借方数量 | number(16,6) | Y |  |
| 168 | P26_DR_TRANS_AMT | 期间26-借方金额-原币 | number(23,8) | Y |  |
| 169 | P26_DR_FUNCTION_AMT | 期间26-借方金额-本币 | number(23,8) | Y |  |
| 170 | P26_CR_QTY | 期间26-贷方数量 | number(16,6) | Y |  |
| 171 | P26_CR_TRANS_AMT | 期间26-贷方金额-原币 | number(23,8) | Y |  |
| 172 | P26_CR_FUNCTION_AMT | 期间26-贷方金额-本币 | number(23,8) | Y |  |
| 173 | P27_DR_QTY | 期间27-借方数量 | number(16,6) | Y |  |
| 174 | P27_DR_TRANS_AMT | 期间27-借方金额-原币 | number(23,8) | Y |  |
| 175 | P27_DR_FUNCTION_AMT | 期间27-借方金额-本币 | number(23,8) | Y |  |
| 176 | P27_CR_QTY | 期间27-贷方数量 | number(16,6) | Y |  |
| 177 | P27_CR_TRANS_AMT | 期间27-贷方金额-原币 | number(23,8) | Y |  |
| 178 | P27_CR_FUNCTION_AMT | 期间27-贷方金额-本币 | number(23,8) | Y |  |
| 179 | P28_DR_QTY | 期间28-借方数量 | number(16,6) | Y |  |
| 180 | P28_DR_TRANS_AMT | 期间28-借方金额-原币 | number(23,8) | Y |  |
| 181 | P28_DR_FUNCTION_AMT | 期间28-借方金额-本币 | number(23,8) | Y |  |
| 182 | P28_CR_QTY | 期间28-贷方数量 | number(16,6) | Y |  |
| 183 | P28_CR_TRANS_AMT | 期间28-贷方金额-原币 | number(23,8) | Y |  |
| 184 | P28_CR_FUNCTION_AMT | 期间28-贷方金额-本币 | number(23,8) | Y |  |
| 185 | P29_DR_QTY | 期间29-借方数量 | number(16,6) | Y |  |
| 186 | P29_DR_TRANS_AMT | 期间29-借方金额-原币 | number(23,8) | Y |  |
| 187 | P29_DR_FUNCTION_AMT | 期间29-借方金额-本币 | number(23,8) | Y |  |
| 188 | P29_CR_QTY | 期间29-贷方数量 | number(16,6) | Y |  |
| 189 | P29_CR_TRANS_AMT | 期间29-贷方金额-原币 | number(23,8) | Y |  |
| 190 | P29_CR_FUNCTION_AMT | 期间29-贷方金额-本币 | number(23,8) | Y |  |
| 191 | P30_DR_QTY | 期间30-借方数量 | number(16,6) | Y |  |
| 192 | P30_DR_TRANS_AMT | 期间30-借方金额-原币 | number(23,8) | Y |  |
| 193 | P30_DR_FUNCTION_AMT | 期间30-借方金额-本币 | number(23,8) | Y |  |
| 194 | P30_CR_QTY | 期间30-贷方数量 | number(16,6) | Y |  |
| 195 | P30_CR_TRANS_AMT | 期间30-贷方金额-原币 | number(23,8) | Y |  |
| 196 | P30_CR_FUNCTION_AMT | 期间30-贷方金额-本币 | number(23,8) | Y |  |
| 197 | P31_DR_QTY | 期间31-借方数量 | number(16,6) | Y |  |
| 198 | P31_DR_TRANS_AMT | 期间31-借方金额-原币 | number(23,8) | Y |  |
| 199 | P31_DR_FUNCTION_AMT | 期间31-借方金额-本币 | number(23,8) | Y |  |
| 200 | P31_CR_QTY | 期间31-贷方数量 | number(16,6) | Y |  |
| 201 | P31_CR_TRANS_AMT | 期间31-贷方金额-原币 | number(23,8) | Y |  |
| 202 | P31_CR_FUNCTION_AMT | 期间31-贷方金额-本币 | number(23,8) | Y |  |
| 203 | P32_DR_QTY | 期间32-借方数量 | number(16,6) | Y |  |
| 204 | P32_DR_TRANS_AMT | 期间32-借方金额-原币 | number(23,8) | Y |  |
| 205 | P32_DR_FUNCTION_AMT | 期间32-借方金额-本币 | number(23,8) | Y |  |
| 206 | P32_CR_QTY | 期间32-贷方数量 | number(16,6) | Y |  |
| 207 | P32_CR_TRANS_AMT | 期间32-贷方金额-原币 | number(23,8) | Y |  |
| 208 | P32_CR_FUNCTION_AMT | 期间32-贷方金额-本币 | number(23,8) | Y |  |
| 209 | P33_DR_QTY | 期间33-借方数量 | number(16,6) | Y |  |
| 210 | P33_DR_TRANS_AMT | 期间33-借方金额-原币 | number(23,8) | Y |  |
| 211 | P33_DR_FUNCTION_AMT | 期间33-借方金额-本币 | number(23,8) | Y |  |
| 212 | P33_CR_QTY | 期间33-贷方数量 | number(16,6) | Y |  |
| 213 | P33_CR_TRANS_AMT | 期间33-贷方金额-原币 | number(23,8) | Y |  |
| 214 | P33_CR_FUNCTION_AMT | 期间33-贷方金额-本币 | number(23,8) | Y |  |
| 215 | P34_DR_QTY | 期间34-借方数量 | number(16,6) | Y |  |
| 216 | P34_DR_TRANS_AMT | 期间34-借方金额-原币 | number(23,8) | Y |  |
| 217 | P34_DR_FUNCTION_AMT | 期间34-借方金额-本币 | number(23,8) | Y |  |
| 218 | P34_CR_QTY | 期间34-贷方数量 | number(16,6) | Y |  |
| 219 | P34_CR_TRANS_AMT | 期间34-贷方金额-原币 | number(23,8) | Y |  |
| 220 | P34_CR_FUNCTION_AMT | 期间34-贷方金额-本币 | number(23,8) | Y |  |
| 221 | P35_DR_QTY | 期间35-借方数量 | number(16,6) | Y |  |
| 222 | P35_DR_TRANS_AMT | 期间35-借方金额-原币 | number(23,8) | Y |  |
| 223 | P35_DR_FUNCTION_AMT | 期间35-借方金额-本币 | number(23,8) | Y |  |
| 224 | P35_CR_QTY | 期间35-贷方数量 | number(16,6) | Y |  |
| 225 | P35_CR_TRANS_AMT | 期间35-贷方金额-原币 | number(23,8) | Y |  |
| 226 | P35_CR_FUNCTION_AMT | 期间35-贷方金额-本币 | number(23,8) | Y |  |
| 227 | P36_DR_QTY | 期间36-借方数量 | number(16,6) | Y |  |
| 228 | P36_DR_TRANS_AMT | 期间36-借方金额-原币 | number(23,8) | Y |  |
| 229 | P36_DR_FUNCTION_AMT | 期间36-借方金额-本币 | number(23,8) | Y |  |
| 230 | P36_CR_QTY | 期间36-贷方数量 | number(16,6) | Y |  |
| 231 | P36_CR_TRANS_AMT | 期间36-贷方金额-原币 | number(23,8) | Y |  |
| 232 | P36_CR_FUNCTION_AMT | 期间36-贷方金额-本币 | number(23,8) | Y |  |
| 233 | PERIOD_OPENING_QTY | 启用期间-期初余额-数量 | number(16,6) | Y |  |
| 234 | PERIOD_OPENING_TRANS_AMT | 启用期间-期初余额-原币 | number(23,8) | Y |  |
| 235 | PERIOD_OPENING_FUNCTION_AMT | 启用期间-期初余额-本币 | number(23,8) | Y |  |
| 236 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 237 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 238 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 239 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 240 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 241 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 242 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 243 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 244 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 245 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 246 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 247 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 248 | UDF041 | 自定义字段12 | date | Y |  |
| 249 | UDF042 | 自定义字段13 | date | Y |  |
| 250 | UDF051 | 自定义字段14 | GUID | Y |  |
| 251 | UDF052 | 自定义字段15 | GUID | Y |  |
| 252 | UDF053 | 自定义字段16 | GUID | Y |  |
| 253 | UDF054 | 自定义字段17 | GUID | Y |  |
| 254 | CreateDate | 创建日期 | date | Y |  |
| 255 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 256 | ModifiedDate | 修改日期 | date | Y |  |
| 257 | CreateBy | 创建者 | GUID | Y |  |
| 258 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 259 | ModifiedBy | 修改者 | GUID | Y |  |
| 260 | ACCOUNT_INITIAL_D_ID |  | GUID | Y |  |