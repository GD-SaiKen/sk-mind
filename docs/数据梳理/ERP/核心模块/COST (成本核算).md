---
module: "COST"
name_zh: "成本核算"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 17
columns: 748
category: financial
semantic_object: "CostAccounting/成本核算"
original_tables: 17
filtered_out: 0
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# COST (成本核算) - CostAccounting/成本核算

> [!info] Phase 1 Core Module
> Semantic Object: CostAccounting/成本核算
> Kept: 17 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 2

## Related Modules

- [[../modules/GL (总账).md|GL (总账)]]
- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]

---

## Tables

- **COST_ALLOC_BASIS (成本分配依据)**
- **COST_ALLOC_BASIS_COLL (成本分配依据收集)**
- **COST_ALLOC_BASIS_COLL_D (成本分配依据收集单身)**
- **COST_ALLOC_BASIS_D (成本分配依据单身)**
- **COST_ALLOC_FACTOR (成本分配因子)**
- **COST_ALLOC_FACTOR_D (成本分配因子多语言)**
- **COST_ALLOC_RATE (成本分配率)**
- **COST_ALLOC_RATE_D (成本分配率单身)**
- **COST_COMPLETION_RATE (完工率)**
- **COST_COMPLETION_RATE_D (完工率单身)**
- **COST_DOC (成本单据)**
- **COST_DOC_D (成本单身明细)**
- **COST_DOC_DISASSEMBLY (成本拆解单据)**
- **COST_DOC_IDCST_DETAIL (成本计算单间接成本明细)**
- **COST_DOMAIN (成本域)**
- **COST_ELEMENT (成本要素)**
- **COST_LLC (成本低层码)**

---

## Table Details

### COST_ALLOC_BASIS (成本分配依据)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_ALLOC_BASIS_ID | 主键 | GUID | Y | Y |
| 4 | COST_ALLOC_BASIS_CODE | 依据编号 | string(12) | Y |  |
| 5 | COST_ALLOC_BASIS_NAME | 依据名称 | string(40) | Y |  |
| 6 | AUTO_COLLECTION_MODE | 自动收集方式 | number | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | UNIT | 单位 | string(8) | Y |  |
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


### COST_ALLOC_BASIS_COLL (成本分配依据收集)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_ALLOC_BASIS_COLL_ID | 主键 | GUID | Y | Y |
| 4 | TRANS_DATE | 日期 | date | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 7 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 8 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 9 | PLANT_ID | 工厂 | GUID | Y |  |
| 10 | MO_ID | 工单 | GUID | Y |  |
| 11 | ITEM_ID | 品号 | GUID | Y |  |
| 12 | ITEM_NAME |  | string(120) | Y |  |
| 13 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 14 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |


### COST_ALLOC_BASIS_COLL_D (成本分配依据收集单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COST_ALLOC_BASIS_COLL_D_ID | 主键 | GUID | Y | Y |
| 3 | COST_ALLOC_BASIS_ID | 成本分配依据 | GUID | Y |  |
| 4 | COST_ALLOC_BASIS_VALUE | 成本分配依据数值 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | COST_ALLOC_BASIS_D_ID | 计算公式ID | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | COST_ALLOC_BASIS_COLL_ID |  | GUID | Y |  |


### COST_ALLOC_BASIS_D (成本分配依据单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COST_ALLOC_BASIS_D_ID | 主键 | GUID | Y | Y |
| 3 | FORMULA_CODE | 公式编号 | string(8) | Y |  |
| 4 | FORMULA | 公式内容 | string | Y |  |
| 5 | FORMULA_LIMIT | 作用范围 | string | Y |  |
| 6 | REMARK |  | string(510) | Y |  |
| 7 | FORMULA_OOQL | 公式内容OOQL | string | Y |  |
| 8 | FORMULA_LIMIT_OOQL | 作用范围OOQL | string | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | COST_ALLOC_BASIS_ID |  | GUID | Y |  |


### COST_ALLOC_FACTOR (成本分配因子)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_ALLOC_FACTOR_ID | 主键 | GUID | Y | Y |
| 4 | COST_ALLOC_FACTOR_CODE | 因子编号 | string(12) | Y |  |
| 5 | CATEGORY1 | 因子分类1 | number | Y |  |
| 6 | CATEGORY2 | 因子分类2 | number | Y |  |
| 7 | CATEGORY3 | 因子分类3 | number | Y |  |
| 8 | COST_ALLOC_BASIS_LIMIT | 适用成本分配依据范围 | string(8) | Y |  |
| 9 | FIELD_NAME | 因子对应字段 | string(60) | Y |  |
| 10 | SQL_SCRIPT | SQL脚本 | string | Y |  |
| 11 | GROUP_NO | 分组 | number | Y |  |
| 12 | GROUP_SEQNO | 组内序号 | number | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CATEGORY9 | 因子分类9 | number | Y |  |
| 15 | SF_DATA_LIST_ID | 生产项目ID | GUID | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 24 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 25 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 26 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 27 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 28 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 29 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 30 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 31 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 32 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 33 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 34 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 35 | UDF041 | 自定义字段12 | date | Y |  |
| 36 | UDF042 | 自定义字段13 | date | Y |  |
| 37 | UDF051 | 自定义字段14 | GUID | Y |  |
| 38 | UDF052 | 自定义字段15 | GUID | Y |  |
| 39 | UDF053 | 自定义字段16 | GUID | Y |  |
| 40 | UDF054 | 自定义字段17 | GUID | Y |  |
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |


### COST_ALLOC_FACTOR_D (成本分配因子多语言)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | COST_ALLOC_FACTOR_D_ID |  | GUID | Y | Y |
| 2 | LANGUAGE | 语言 | string(120) | Y |  |
| 3 | COST_ALLOC_FACTOR_NAME | 因子名称 | string(100) | Y |  |
| 4 | COST_ALLOC_FACTOR_DESC | 因子描述 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | COST_ALLOC_FACTOR_ID |  | GUID | Y |  |


### COST_ALLOC_RATE (成本分配率)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_ALLOC_RATE_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | PLANT_ID | 工厂 | GUID | Y |  |
| 8 | COST_AMT | 成本合计 | number(23,8) | Y |  |
| 9 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
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
| 43 | IDLE_CAPACITY_FLAG | 计算成本分配率考虑闲置产能 | number(0/1) | Y |  |


### COST_ALLOC_RATE_D (成本分配率单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COST_ALLOC_RATE_D_ID | 主键 | GUID | Y | Y |
| 3 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 4 | COST_ALLOC_BASIS_ID | 成本分配依据 | GUID | Y |  |
| 5 | COST_ALLOC_BASIS_VALUE | 成本分配依据数值 | number(16,6) | Y |  |
| 6 | COST_AMT | 可分配金额 | number(23,8) | Y |  |
| 7 | ALLOCATION_MODE | 分配方式 | number | Y |  |
| 8 | ACTUAL_ALLOC_RATE | 实际分配率 | number(23,8) | Y |  |
| 9 | STD_ALLOC_RATE | 标准分配率 | number(23,8) | Y |  |
| 10 | AMOUNT_FORMULA | 成本取数公式 | string | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | COST_ALLOC_RATE_ID |  | GUID | Y |  |
| 41 | STD_COST_ALLOC_BASIS_VALUE | 标准成本分配依据数值 | number(16,6) | Y |  |
| 42 | IDLE_RATE | 闲置率 | number(5,4) | Y |  |
| 43 | INCURRED_AMT | 发生额 | number(23,8) | Y |  |
| 44 | IDLE_AMT | 闲置金额 | number(23,8) | Y |  |


### COST_COMPLETION_RATE (完工率)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_COMPLETION_RATE_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | PLANT_ID | 工厂 | GUID | Y |  |
| 8 | MO_ID | 工单 | GUID | Y |  |
| 9 | ITEM_ID | 品号 | GUID | Y |  |
| 10 | ITEM_NAME |  | string(120) | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 12 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 13 | WIP_QTY |  | number(16,6) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |


### COST_COMPLETION_RATE_D (完工率单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COST_COMPLETION_RATE_D_ID | 主键 | GUID | Y | Y |
| 3 | COMPLETION_RATE | 完工率 | number(5,4) | Y |  |
| 4 | WIPEU_QTY | 在制约量 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 7 | CLCOMPLETION_RATE | 本阶完工率 | number(5,4) | Y |  |
| 8 | LLCOMPLETION_RATE | 下阶完工率 | number(5,4) | Y |  |
| 9 | CLWIPEU_QTY | 本阶在制约量 | number(16,6) | Y |  |
| 10 | LLWIPEU_QTY | 下阶在制约量 | number(16,6) | Y |  |
| 11 | CLCOMPLETION_FLAG | 本阶完工率标识 | number(0/1) | Y |  |
| 12 | LLCOMPLETION_FLAG | 下阶完工率标识 | number(0/1) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 38 | COST_COMPLETION_RATE_ID |  | GUID | Y |  |


### COST_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_DOC_ID | 主键 | GUID | Y | Y |
| 4 | DOC_TYPE | 单据类型 | number | Y |  |
| 5 | PLANT_ID | 主鍵 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ITEM_ID | 主键 | GUID | Y |  |
| 10 | ITEM_NAME |  | string(120) | Y |  |
| 11 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 12 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 13 | ITEM_NATURE | 品号性质 | number | Y |  |
| 14 | MO_ID | 工单 | GUID | Y |  |
| 15 | PROD_COMPLETED_QTY | 生产入库 | number(16,6) | Y |  |
| 16 | SUB_COMPLETED_QTY | 委外入库 | number(16,6) | Y |  |
| 17 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 18 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 19 | MASTER_COST_DOC_ID | 主产品成本计算单 | GUID | Y |  |
| 20 | COST_DISASSEMBLY_RATE | 成本拆分比率 | number(5,4) | Y |  |
| 21 | COST_CONV_COEFFICIENT | 标准数量换算系数 | number(16,6) | Y |  |
| 22 | OPENING_COST_AMT | 期初在制成本合计 | number(23,8) | Y |  |
| 23 | INPUT_COST_AMT | 本期投入成本合计 | number(23,8) | Y |  |
| 24 | COMP_COST_AMT | 本期转出成本合计 | number(23,8) | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | DOC_NO |  | string(40) | Y |  |
| 27 | PER_QTY | 产出比例 | number(16,6) | Y |  |
| 28 | ADJ_COMP_COST_AMT | 本期转出调整合计 | number(23,8) | Y |  |
| 29 | MULTI_COMP_COST_AMT | 本期多产出转出合计 | number(23,8) | Y |  |
| 30 | ENDING_COST_AMT | 期末在制成本合计 | number(23,8) | Y |  |
| 31 | MASTER_FLAG | 主成本计算单标识 | number(0/1) | Y |  |
| 32 | DISASSEMBLY_LOCK_FLAG | 成本拆分比率锁定标识 | number(0/1) | Y |  |
| 33 | DASI_OPENING_EU_QTY | 拆件母件期初约当数量 | number(16,6) | Y |  |
| 34 | DASI_INPUT_QTY | 拆件母件本期投入数量 | number(16,6) | Y |  |
| 35 | DASI_ENDING_EU_QTY | 拆件母件期末约当数量 | number(16,6) | Y |  |
| 36 | INITIALIZED_FLAG | 初始化标识 | number(0/1) | Y |  |
| 37 | MO_PROCESS_TYPE | 工单性质 | string(40) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
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
| 63 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |
| 67 | Version | 版本号，不要随意更改 | binary | Y |  |
| 68 | Owner_Org_RTK |  | string(400) | Y |  |
| 69 | Owner_Org_ROid |  | GUID | Y |  |


### COST_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COST_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | COST_ELEMENT_ID | 主键 | GUID | Y |  |
| 4 | OPENING_COST_AMT | 期初在制成本 | number(23,8) | Y |  |
| 5 | OPENING_CLCOST_AMT | 期初在制本阶成本 | number(23,8) | Y |  |
| 6 | OPENING_LLCOST_AMT | 期初在制下阶成本 | number(23,8) | Y |  |
| 7 | INPUT_COST_AMT | 本期投入成本 | number(23,8) | Y |  |
| 8 | INPUT_CLCOST_AMT | 本期本阶投入成本 | number(23,8) | Y |  |
| 9 | INPUT_LLCOST_AMT | 本期下阶投入成本 | number(23,8) | Y |  |
| 10 | ENDING_COST_AMT | 期末在制成本 | number(23,8) | Y |  |
| 11 | ENDING_CLCOST_AMT | 期末在制本阶成本 | number(23,8) | Y |  |
| 12 | ENDING_LLCOST_AMT | 期末在制下阶成本 | number(23,8) | Y |  |
| 13 | COMP_COST_AMT | 本期转出成本 | number(23,8) | Y |  |
| 14 | COMP_CLCOST_AMT | 本期本阶转出成本 | number(23,8) | Y |  |
| 15 | COMP_LLCOST_AMT | 本期下阶转出成本 | number(23,8) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | ADJ_COMP_COST_AMT | 本期转出成本调整金额 | number(23,8) | Y |  |
| 18 | ADJ_COMP_CLCOST_AMT | 本期本阶转出成本调整金额 | number(23,8) | Y |  |
| 19 | ADJ_COMP_LLCOST_AMT | 本期下阶转出成本调整金额 | number(23,8) | Y |  |
| 20 | MULTI_COMP_COST_AMT | 本期多产出转出成本 | number(23,8) | Y |  |
| 21 | MULTI_COMP_CLCOST_AMT | 本期多产出本阶转出成本 | number(23,8) | Y |  |
| 22 | MULTI_COMP_LLCOST_AMT | 本期多产出下阶转出成本 | number(23,8) | Y |  |
| 23 | ENDING_COST_TOTAMT | 期末在制成本合计 | number(23,8) | Y |  |
| 24 | ENDING_CLCOST_TOTAMT | 期末在制本阶成本合计 | number(23,8) | Y |  |
| 25 | ENDING_LLCOST_TOTAMT | 期末在制下阶成本合计 | number(23,8) | Y |  |
| 26 | MULTI_ENDING_COST_AMT | 期末多产出在制成本 | number(23,8) | Y |  |
| 27 | MULTI_ENDING_CLCOST_AMT | 期末多产出在制本阶成本 | number(23,8) | Y |  |
| 28 | MULTI_ENDING_LLCOST_AMT | 期末多产出在制下阶成本 | number(23,8) | Y |  |
| 29 | OPENING_CLWIPEU_QTY | 期初本阶在制约量 | number(16,6) | Y |  |
| 30 | OPENING_LLWIPEU_QTY | 期初下阶在制约量 | number(16,6) | Y |  |
| 31 | ENDING_CLWIPEU_QTY | 期末本阶在制约量 | number(16,6) | Y |  |
| 32 | ENDING_LLWIPEU_QTY | 期末下阶在制约量 | number(16,6) | Y |  |
| 33 | ENDING_CLWIPEU_LOCK_FLAG | 期末本阶在制约量锁定标识 | number(0/1) | Y |  |
| 34 | ENDING_LLWIPEU_LOCK_FLAG | 期末下阶在制约量锁定标识 | number(0/1) | Y |  |
| 35 | PCOST_ADJDOC_COST_AMT | 调整单成本金额 | number(23,8) | Y |  |
| 36 | PCOST_ADJDOC_CLCOST_AMT | 调整单本阶成本金额 | number(23,8) | Y |  |
| 37 | PCOST_ADJDOC_LLCOST_AMT | 调整单下阶成本金额 | number(23,8) | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 62 | Version | 版本号，不要随意更改 | binary | Y |  |
| 63 | COST_DOC_ID |  | GUID | Y |  |


### COST_DOC_DISASSEMBLY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COST_DOC_DISASSEMBLY_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 产出品号 | GUID | Y |  |
| 4 | ITEM_NAME |  | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | PROD_COMPLETED_QTY | 生产入库 | number(16,6) | Y |  |
| 8 | SUB_COMPLETED_QTY | 委外入库 | number(16,6) | Y |  |
| 9 | SCRAP_QTY | 报废数量 | number(16,6) | Y |  |
| 10 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 11 | MULTI_COST_DOC_ID | 产出品号成本计算单 | GUID | Y |  |
| 12 | DEFAULT_UNIT_COST_DISA_RATE | 默认单位成本拆分比率 | number(5,4) | Y |  |
| 13 | UNIT_COST_DISASSEMBLY_RATE | 单位成本拆分比率 | number(23,8) | Y |  |
| 14 | COST_DISASSEMBLY_RATE | 成本拆分比率 | number(5,4) | Y |  |
| 15 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 16 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | COST_DOC_ID |  | GUID | Y |  |


### COST_DOC_IDCST_DETAIL (成本计算单间接成本明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | COST_DOC_IDCST_DETAIL_ID | 主键 | GUID | Y | Y |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | COST_DOC_ID | 成本计算单 | GUID | Y |  |
| 8 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 9 | PLANT_ID | 工厂 | GUID | Y |  |
| 10 | COST_ELEMENT_ID | 成本要素 | GUID | Y |  |
| 11 | COST_ALLOC_BASIS_ID | 成本分配依据 | GUID | Y |  |
| 12 | COST_ALLOC_BASIS_VALUE | 数量成本分配依据数值 | number(16,6) | Y |  |
| 13 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 22 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 23 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 24 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 25 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 26 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 27 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 28 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 29 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 30 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 31 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 32 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 33 | UDF041 | 自定义字段12 | date | Y |  |
| 34 | UDF042 | 自定义字段13 | date | Y |  |
| 35 | UDF051 | 自定义字段14 | GUID | Y |  |
| 36 | UDF052 | 自定义字段15 | GUID | Y |  |
| 37 | UDF053 | 自定义字段16 | GUID | Y |  |
| 38 | UDF054 | 自定义字段17 | GUID | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | MO_ID |  | GUID | Y |  |
| 47 | ALLOCATION_MODE |  | number | Y |  |
| 48 | COST_ALLOC_RATE |  | number(23,8) | Y |  |


### COST_DOMAIN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_DOMAIN_ID | 主键 | GUID | Y | Y |
| 4 | COST_DOMAIN_CODE | 域编号 | string(400) | Y |  |
| 5 | COST_DOMAIN_NAME | 域名称 | string(400) | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |


### COST_ELEMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 2 | ApproveDate | 修改日期 | date | Y |  |
| 3 | ApproveBy | 修改人 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | COST_ELEMENT_ID | 主键 | GUID | Y | Y |
| 7 | COST_ELEMENT_CODE | 成本要素编号 | string(12) | Y |  |
| 8 | COST_ELEMENT_NAME | 成本要素名称 | string(60) | Y |  |
| 9 | COST_ELEMENT_CATEGORY | 成本要素类别 | number | Y |  |
| 10 | COST_BEHAVIOR | 成本性态 | number | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
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
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |


### COST_LLC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | COST_LLC_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_CODE |  | string(20) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | LLC | 低阶码 | number | Y |  |
| 10 | STATUS | 状态 | number | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | ITEM_FEATURE_COST_FLAG | 按特征码区分成本 | number(0/1) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |
