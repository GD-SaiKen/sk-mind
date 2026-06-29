---
module: "BUDGET"
name_zh: "预算管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 8
columns: 409
category: financial
semantic_object: "Budget/预算"
original_tables: 9
filtered_out: 0
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# BUDGET (预算管理) - Budget/预算

> [!info] Phase 1 Core Module
> Semantic Object: Budget/预算
> Kept: 8 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 1

## Related Modules

- [[../modules/GL (总账).md|GL (总账)]]
- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]

---

## Tables

- **BUDGET_ADJUST_DOC (预算单据)**
- **BUDGET_CTRL_CATEGORY (预算控制分类)**
- **BUDGET_D (预算单身)**
- **BUDGET_GROUP (预算组)**
- **BUDGET_ITEM (预算项)**
- **BUDGET_PERF_OBJECT (预算执行对象档)**
- **BUDGET_PERF_STATS (预算执行统计档)**
- **BUDGET_PERF_VERIFIED (预算执行核销档)**

---

## Table Details

### BUDGET_ADJUST_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | BUDGET_ADJUST_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ADJUST_DATE | 调整日期 | date | Y |  |
| 8 | ADJUST_TYPE | 调整类型 | number | Y |  |
| 9 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 10 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 11 | BUDGET_YEAR | 预算年度 | string(8) | Y |  |
| 12 | BUDGET_PERIOD_CODE | 预算期间期号 | string(20) | Y |  |
| 13 | BUDGET_PERIOD_SEQNO | 预算期间序号 | number | Y |  |
| 14 | O_BUDGET_AMT | 原预算金额 | number(23,8) | Y |  |
| 15 | BUDGET_ID | 预算 | GUID | Y |  |
| 16 | SYS_TSN | 系统业务序号 | number | Y |  |
| 17 | TFI_BUDGET_GROUP_ID | 拨入_预算组 | GUID | Y |  |
| 18 | TFI_BUDGET_ITEM_ID | 拨入_预算项 | GUID | Y |  |
| 19 | TFI_BUDGET_ADMIN_UNIT_ID | 拨入_预算部门 | GUID | Y |  |
| 20 | TFI_BUDGET_YEAR | 拨入_预算年度 | string(8) | Y |  |
| 21 | TFI_BUDGET_PERIOD_CODE | 拨入_预算期间期号 | string(20) | Y |  |
| 22 | TFI_BUDGET_PERIOD_SEQNO | 拨入_预算期间序号 | number | Y |  |
| 23 | TFI_O_BUDGET_AMT | 拨入_原预算金额 | number(23,8) | Y |  |
| 24 | TFI_BUDGET_ID | 拨入_预算 | GUID | Y |  |
| 25 | TFI_BUDGET_D_ID | 拨入_预算行 | GUID | Y |  |
| 26 | TFI_SYS_TSN | 拨入_系统业务序号 | number | Y |  |
| 27 | ADJUST_AMT | 调整额 | number(23,8) | Y |  |
| 28 | REMARK | 备注 | string(510) | Y |  |
| 29 | ADMIN_UNIT_ID | 主键 | GUID | Y |  |
| 30 | BUDGET_D_ID | 预算行 | GUID | Y |  |
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
| 49 | PrintCount | 打印次数 | number | Y |  |
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
| 62 | Version | 版本号，不要随意更改 | binary | Y |  |
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | Owner_Org_RTK |  | string(400) | Y |  |
| 67 | Owner_Org_ROid |  | GUID | Y |  |


### BUDGET_CTRL_CATEGORY (预算控制分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BUDGET_CTRL_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | BUDGET_CTRL_CATEGORY_CODE | 分类编号 | string(12) | Y |  |
| 5 | BUDGET_CTRL_CATEGORY_NAME | 分类名称 | string(40) | Y |  |
| 6 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 33 | Attachments | 附件 | string | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |


### BUDGET_D (预算单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BUDGET_D_ID | 主键 | GUID | Y | Y |
| 3 | BUDGET_PERIOD_CODE | 预算期间期号 | string(20) | Y |  |
| 4 | START_ACCPERIOD_CODE | 开始会计期间期号 | string(20) | Y |  |
| 5 | CUTOFF_ACCPERIOD_CODE | 结束会计期间期号 | string(20) | Y |  |
| 6 | START_ACCPERIOD_SEQNO | 开始会计期间序号 | number | Y |  |
| 7 | CUTOFF_ACCPERIOD_SEQNO | 结束会计期间序号 | number | Y |  |
| 8 | START_DATE | 会计期间开始日期 | date | Y |  |
| 9 | CUTOFF_DATE | 会计期间截止日期 | date | Y |  |
| 10 | BUDGET_AMT | 预算金额 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SYS_TSN | 系统业务序号 | number | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 38 | BUDGET_ID |  | GUID | Y |  |


### BUDGET_GROUP (预算组)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BUDGET_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | BUDGET_GROUP_CODE | 预算组编号 | string(12) | Y |  |
| 5 | BUDGET_GROUP_NAME | 预算组名称 | string(60) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | Attachments | 附件 | string | Y |  |
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |


### BUDGET_ITEM (预算项)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BUDGET_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | BUDGET_ITEM_CODE | 预算项编号 | string(60) | Y |  |
| 5 | BUDGET_ITEM_NAME | 预算项名称 | string(840) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 32 | Attachments | 附件 | string | Y |  |
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |


### BUDGET_PERF_OBJECT (预算执行对象档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BUDGET_PERF_OBJECT_ID | 主键 | GUID | Y | Y |
| 4 | DOC_CATEGORY | 单据性质 | string(40) | Y |  |
| 5 | TRNAS_DATE | 交易日期 | date | Y |  |
| 6 | BUDGET_YEAR | 预算年度 | string(8) | Y |  |
| 7 | BUDGET_PERIOD_SEQNO | 预算期间序号 | number | Y |  |
| 8 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 9 | TRANS_DOC_LINE_SEQNO | 交易单据行序号 | number | Y |  |
| 10 | PERFORMANCE_AMT | 执行金额 | number(23,8) | Y |  |
| 11 | VERIFICATION_AMT | 核销金额 | number(23,8) | Y |  |
| 12 | BUDGET_ID | 预算 | GUID | Y |  |
| 13 | BUDGET_D_ID | 预算行 | GUID | Y |  |
| 14 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 15 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 16 | ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |
| 51 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 52 | SOURCE2_ID_ROid |  | GUID | Y |  |


### BUDGET_PERF_STATS (预算执行统计档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BUDGET_PERF_STATS_ID | 主键 | GUID | Y | Y |
| 4 | BUDGET_ID | 预算 | GUID | Y |  |
| 5 | BUDGET_D_ID | 预算行 | GUID | Y |  |
| 6 | BUDGET_YEAR | 预算年度 | string(8) | Y |  |
| 7 | BUDGET_PERIOD_SEQNO | 预算期间序号 | number | Y |  |
| 8 | REQS_BAL_AMT | 未转采请购金额 | number(23,8) | Y |  |
| 9 | PO_BAL_AMT | 未到货采购金额 | number(23,8) | Y |  |
| 10 | PA_BAL_AMT | 未入库到货金额 | number(23,8) | Y |  |
| 11 | PR_BAL_AMT | 未出库退货金额 | number(23,8) | Y |  |
| 12 | PAR_UNSETTLED_AMT | 未结算入库金额 | number(23,8) | Y |  |
| 13 | PRI_UNSETTLED_AMT | 未结算出库金额 | number(23,8) | Y |  |
| 14 | SETTLED_AMT | 已结算金额 | number(23,8) | Y |  |
| 15 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 16 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 17 | ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 43 | Attachments | 附件 | string | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |


### BUDGET_PERF_VERIFIED (预算执行核销档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | BUDGET_PERF_VERIFIED_ID | 主键 | GUID | Y | Y |
| 4 | BUDGET_PERF_OBJECT_ID | 预算执行对象 | GUID | Y |  |
| 5 | DOC_CATEGORY | 单据性质 | string(40) | Y |  |
| 6 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 7 | TRANS_DOC_LINE_SEQNO | 交易单据行序号 | number | Y |  |
| 8 | VERIFICATION_AMT | 核销金额 | number(23,8) | Y |  |
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
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |
| 41 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE_ID_ROid |  | GUID | Y |  |
| 43 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 44 | SOURCE2_ID_ROid |  | GUID | Y |  |
