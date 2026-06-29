---
module: "CASHFLOW"
name_zh: "现金流量"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 7
columns: 351
category: financial
semantic_object: "CashFlow/现金流量"
original_tables: 8
filtered_out: 1
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# CASHFLOW (现金流量) - CashFlow/现金流量

> [!info] Phase 1 Core Module
> Semantic Object: CashFlow/现金流量
> Kept: 7 tables | Filtered out: 1 (templates/logs/backups)
> Missing CN filled: 1

## Related Modules

- [[../modules/GL (总账).md|GL (总账)]]
- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]

---

## Tables

- **CASHFLOW_DATASET (现金流量表)**
- **CASHFLOW_INITIAL (现金流量初始数据)**
- **CASHFLOW_INITIAL_D (现金流量初始数据单身)**
- **CASHFLOW_ITEM (现金流量项目)**
- **CASHFLOW_ITEM_DIFF (现金流量项目差量)**
- **CASHFLOW_STATISTICS (现金流量统计表)**
- **CASHFLOW_TEMPLATE_D (现金流量单身明细)**

## Filtered Out

> These 1 tables were excluded (templates, logs, history, backups, system):

- ~~CASHFLOW_TEMPLATE~~ (template)

---

## Table Details

### CASHFLOW_DATASET (现金流量表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CASHFLOW_DATASET_ID | 主键 | GUID | Y | Y |
| 4 | CASHFLOW_DATASET_CODE | 现金流量表编号 | string(12) | Y |  |
| 5 | CASHFLOW_DATASET_NAME | 现金流量表名称 | string(40) | Y |  |
| 6 | DATASET_TYPE | 现金流量表类型 | number | Y |  |
| 7 | DATASET_AREA | 现金流量表范围 | number | Y |  |
| 8 | CASHFLOW_LEVEL | 现金流量表项目级次 | number | Y |  |
| 9 | CASHFLOW_CODEMODE | 现金流量表项目编码规则 | string(30) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |


### CASHFLOW_INITIAL (现金流量初始数据)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CASHFLOW_INITIAL_ID | 主键 | GUID | Y | Y |
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


### CASHFLOW_INITIAL_D (现金流量初始数据单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CASHFLOW_INITIAL_D_ID | 主键 | GUID | Y | Y |
| 2 | P01_CASHFLOW_AMT | 期间1-现金流量金额 | number(23,8) | Y |  |
| 3 | P02_CASHFLOW_AMT | 期间2-现金流量金额 | number(23,8) | Y |  |
| 4 | P03_CASHFLOW_AMT | 期间3-现金流量金额 | number(23,8) | Y |  |
| 5 | P04_CASHFLOW_AMT | 期间4-现金流量金额 | number(23,8) | Y |  |
| 6 | P05_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 7 | P06_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 8 | P07_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 9 | P08_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 10 | P09_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 11 | P10_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 12 | P11_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 13 | P12_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 14 | P13_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 15 | P14_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 16 | P15_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 17 | P16_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 18 | P17_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 19 | P18_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 20 | P19_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 21 | P20_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 22 | P21_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 23 | P22_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 24 | P23_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 25 | P24_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 26 | P25_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 27 | P26_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 28 | P27_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 29 | P28_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 30 | P29_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 31 | P30_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 32 | P31_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 33 | P32_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 34 | P33_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 35 | P34_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 36 | P35_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 37 | P36_CASHFLOW_AMT |  | number(23,8) | Y |  |
| 38 | CASHFLOW_ITEM_ID | 现金流量项目编号 | GUID | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | CreateDate | 创建日期 | date | Y |  |
| 58 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 59 | ModifiedDate | 修改日期 | date | Y |  |
| 60 | CreateBy | 创建者 | GUID | Y |  |
| 61 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 62 | ModifiedBy | 修改者 | GUID | Y |  |
| 63 | CASHFLOW_INITIAL_ID |  | GUID | Y |  |


### CASHFLOW_ITEM (现金流量项目)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CASHFLOW_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | CASHFLOW_ITEM_CODE |  | string(24) | Y |  |
| 5 | CASHFLOW_ITEM_NAME |  | string(80) | Y |  |
| 6 | CASHFLOW_ITEM_AREA | 现金流量项目范围 | number | Y |  |
| 7 | CASHFLOW_ITEM_PROPERTY | 现金流量项目流向性质 | number | Y |  |
| 8 | ALLOW_ADDCFITEM_INDICATOR | 允许增加下级项目 | number(0/1) | Y |  |
| 9 | CASHFLOW_ITEM_LEVEL | 现金流量项目层级 | number | Y |  |
| 10 | CASHFLOW_DATASET_ID | 现金流量表编号 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |
| 43 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE_ID_ROid |  | GUID | Y |  |


### CASHFLOW_ITEM_DIFF (现金流量项目差量)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CASHFLOW_ITEM_DIFF_ID | 主键 | GUID | Y | Y |
| 2 | CASHFLOW_ITEM_ID | 父主键 | GUID | Y |  |
| 3 | ALTER_CASHFLOW_ITEM_ID | 备选现金流量项目编号 | GUID | Y |  |
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


### CASHFLOW_STATISTICS (现金流量统计表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CASHFLOW_STATISTICS_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_BOOK | 账簿 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | AUXILIARY_ITEM1_ID | 自定义辅助核算项目1 | GUID | Y |  |
| 8 | AUXILIARY_ITEM2_ID | 自定义辅助核算项目2 | GUID | Y |  |
| 9 | CASHFLOW_AMT | 现金流量金额 | number(23,8) | Y |  |
| 10 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 11 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 12 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 13 | EMPLOYEE_ID | 人员 | GUID | Y |  |
| 14 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 15 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 16 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 17 | CASHFLOW_ITEM_ID | 现金流量项目编号 | GUID | Y |  |
| 18 | PROJECT_ID | 项目 | GUID | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
| 26 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 27 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 28 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 29 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 30 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 31 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 32 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 33 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 34 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 35 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 36 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 37 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 38 | UDF041 | 自定义字段12 | date | Y |  |
| 39 | UDF042 | 自定义字段13 | date | Y |  |
| 40 | UDF051 | 自定义字段14 | GUID | Y |  |
| 41 | UDF052 | 自定义字段15 | GUID | Y |  |
| 42 | UDF053 | 自定义字段16 | GUID | Y |  |
| 43 | UDF054 | 自定义字段17 | GUID | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |


### CASHFLOW_TEMPLATE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CASHFLOW_TEMPLATE_D_ID | 主键 | GUID | Y | Y |
| 3 | PRINT_CODE1 | 列印码1 | number | Y |  |
| 4 | PRINT_CODE2 | 列印码2 | number | Y |  |
| 5 | SPACE | 空格 | number | Y |  |
| 6 | DATA_SOURCE | 数据来源 | number | Y |  |
| 7 | FISTATEMENT_ITEM_NAME | 报表项目名称 | string(100) | Y |  |
| 8 | DATA_TYPE | 数据类型 | number | Y |  |
| 9 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 10 | ABS_FLAG | 绝对 | number(0/1) | Y |  |
| 11 | COMPUTE1 | 第1项合计值 | number | Y |  |
| 12 | COMPUTE2 | 第2项合计值 | number | Y |  |
| 13 | COMPUTE3 | 第3项合计值 | number | Y |  |
| 14 | COMPUTE4 | 第4项合计值 | number | Y |  |
| 15 | COMPUTE5 | 第5项合计值 | number | Y |  |
| 16 | COMPUTE6 | 第6项合计值 | number | Y |  |
| 17 | COMPUTE7 | 第7项合计值 | number | Y |  |
| 18 | COMPUTE8 | 第8项合计值 | number | Y |  |
| 19 | COMPUTE9 | 第9项合计值 | number | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
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
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | CASHFLOW_TEMPLATE_ID |  | GUID | Y |  |
