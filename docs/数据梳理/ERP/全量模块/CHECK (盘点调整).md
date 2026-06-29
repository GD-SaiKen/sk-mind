---
module: "CHECK"
name_zh: "盘点调整"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 98
category: inventory
tags: ["ERP", "E10", "inventory"]
created: 2026-06-25 10:52
---

# CHECK (盘点调整)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 98

## Related Modules

- [[AJST (库存调整核算)|AJST (库存调整核算)]]
- [[BC (条码管理)|BC (条码管理)]]
- [[BORROW (借入借出)|BORROW (借入借出)]]
- [[CONSIGN (寄售管理)|CONSIGN (寄售管理)]]
- [[COUNTING (盘点计划)|COUNTING (盘点计划)]]
- [[DAMAGE (损坏管理)|DAMAGE (损坏管理)]]
- [[FIL (货位管理)|FIL (货位管理)]]
- [[ISSUE (发料出库)|ISSUE (发料出库)]]

---

## Tables


- **CHECK_GOODS_ADJUST (盘点盈亏单)**
- **CHECK_GOODS_ADJUST_D (盘点盈亏单单身)**


---


---


> Tables: 2

### CHECK_GOODS_ADJUST (盘点盈亏单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | CHECK_GOODS_ADJUST_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | ADJUST_DATE | 盈亏日期 | date | Y |  |
| 9 | CHECK_DATE | 盘点日期 | date | Y |  |
| 10 | CHECK_TIME | 库存快照时间 | date | Y |  |
| 11 | TASK_DOC_NO | 盘点任务单号 | string(40) | Y |  |
| 12 | WAREHOUSE_ID | 盘点仓库 | GUID | Y |  |
| 13 | TASK_NAME | 盘点任务名称 | string(200) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | CLOSE_CHECK_PLAN_ID | 盘点方案 | GUID | Y |  |
| 16 | POS_ID | POS机号 | GUID | Y |  |
| 17 | SHOP_ID | 门店 | GUID | Y |  |
| 18 | CLASS_ID | 班次 | number | Y |  |
| 19 | PrintCount | 打印次数 | number | Y |  |
| 20 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 21 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 22 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 23 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 56 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 57 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |

### CHECK_GOODS_ADJUST_D (盘点盈亏单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CHECK_GOODS_ADJUST_D_ID |  | GUID | Y | Y |
| 3 | SOURCE_ID_RTK | 盘点任务单号 | string(40) | Y |  |
| 4 | SOURCE_ID_ROID | 盘点任务单序号 | GUID | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_NAME | 品名 | string(120) | Y |  |
| 7 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 8 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 9 | UNIT_ID | 单位 | GUID | Y |  |
| 10 | SYSTEM_QTY | 账面数量 | number(16,6) | Y |  |
| 11 | INPUT_QTY | 实盘数量 | number(16,6) | Y |  |
| 12 | ADJUST_QTY | 盈亏数量 | number(16,6) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | COST | 单位成本 | number(23,8) | Y |  |
| 15 | COST_AMT | 成本金额 | number(23,8) | Y |  |
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
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | CHECK_GOODS_ADJUST_ID |  | GUID | Y |  |