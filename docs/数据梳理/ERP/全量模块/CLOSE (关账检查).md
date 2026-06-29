---
module: "CLOSE"
name_zh: "关账检查"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 182
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# CLOSE (关账检查)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 4 | Columns: 182

## Related Modules

- [[ACCOUNT (会计科目)|ACCOUNT (会计科目)]]
- [[ADJUST (调整凭证)|ADJUST (调整凭证)]]
- [[AP (应付账款)|AP (应付账款)]]
- [[AR (应收账款)|AR (应收账款)]]
- [[BANK (银行管理)|BANK (银行管理)]]
- [[BUDGET (预算管理)|BUDGET (预算管理)]]
- [[CASHFLOW (现金流量)|CASHFLOW (现金流量)]]
- [[CFS (财务结转)|CFS (财务结转)]]

---

## Tables

- **CLOSE_CHECK_PLAN**
- **CLOSE_CHECK_PLAN_ITEM**
- **CLOSE_CHECK_PLAN_ITEM2**
- **CLOSE_CHECK_PLAN_SHOP**

---


---


> Tables: 4

### CLOSE_CHECK_PLAN - 盘点方案

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CLOSE_CHECK_PLAN_ID | 主键 | GUID | Y | Y |
| 4 | CLOSE_CHECK_PLAN_CODE | 盘点方案编号 | string(40) | Y |  |
| 5 | CLOSE_CHECK_PLAN_NAME | 盘点方案名称 | string(200) | Y |  |
| 6 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 7 | SHOP_RANGE | 门店范围 | string(40) | Y |  |
| 8 | ITEM_RANGE | 商品范围 | string(40) | Y |  |
| 9 | LOGIC_TYPE | 星期与日期关系 | string(40) | Y |  |
| 10 | BEGIN_DATE | 启用日期 | date | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SUNDAY | 星期日 | number(0/1) | Y |  |
| 13 | MONDAY | 星期一 | number(0/1) | Y |  |
| 14 | TUESDAY | 星期二 | number(0/1) | Y |  |
| 15 | WEDNESDAY | 星期三 | number(0/1) | Y |  |
| 16 | THURSDAY | 星期四 | number(0/1) | Y |  |
| 17 | FRIDAY | 星期五 | number(0/1) | Y |  |
| 18 | SATURDAY | 星期六 | number(0/1) | Y |  |
| 19 | DAY1 | 1号 | number(0/1) | Y |  |
| 20 | DAY2 | 2号 | number(0/1) | Y |  |
| 21 | DAY3 | 3号 | number(0/1) | Y |  |
| 22 | DAY4 | 4号 | number(0/1) | Y |  |
| 23 | DAY5 | 5号 | number(0/1) | Y |  |
| 24 | DAY6 | 6号 | number(0/1) | Y |  |
| 25 | DAY7 | 7号 | number(0/1) | Y |  |
| 26 | DAY8 | 8号 | number(0/1) | Y |  |
| 27 | DAY9 | 9号 | number(0/1) | Y |  |
| 28 | DAY10 | 10号 | number(0/1) | Y |  |
| 29 | DAY11 | 11号 | number(0/1) | Y |  |
| 30 | DAY12 | 12号 | number(0/1) | Y |  |
| 31 | DAY13 | 13号 | number(0/1) | Y |  |
| 32 | DAY14 | 14号 | number(0/1) | Y |  |
| 33 | DAY15 | 15号 | number(0/1) | Y |  |
| 34 | DAY16 | 16号 | number(0/1) | Y |  |
| 35 | DAY17 | 17号 | number(0/1) | Y |  |
| 36 | DAY18 | 18号 | number(0/1) | Y |  |
| 37 | DAY19 | 19号 | number(0/1) | Y |  |
| 38 | DAY20 | 20号 | number(0/1) | Y |  |
| 39 | DAY21 | 21号 | number(0/1) | Y |  |
| 40 | DAY22 | 22号 | number(0/1) | Y |  |
| 41 | DAY23 | 23号 | number(0/1) | Y |  |
| 42 | DAY24 | 24号 | number(0/1) | Y |  |
| 43 | DAY25 | 25号 | number(0/1) | Y |  |
| 44 | DAY26 | 26号 | number(0/1) | Y |  |
| 45 | DAY27 | 27号 | number(0/1) | Y |  |
| 46 | DAY28 | 28号 | number(0/1) | Y |  |
| 47 | DAY29 | 29号 | number(0/1) | Y |  |
| 48 | DAY30 | 30号 | number(0/1) | Y |  |
| 49 | DAY31 | 31号 | number(0/1) | Y |  |
| 50 | DAY_MONTH_END | 月末 | number(0/1) | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 59 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 60 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 61 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 62 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 63 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 64 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 65 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 66 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 67 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 68 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 69 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 70 | UDF041 | 自定义字段12 | date | Y |  |
| 71 | UDF042 | 自定义字段13 | date | Y |  |
| 72 | UDF051 | 自定义字段14 | GUID | Y |  |
| 73 | UDF052 | 自定义字段15 | GUID | Y |  |
| 74 | UDF053 | 自定义字段16 | GUID | Y |  |
| 75 | UDF054 | 自定义字段17 | GUID | Y |  |
| 76 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 77 | Version | 版本号，不要随意更改 | binary | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |
| 81 | Owner_Org_RTK |  | string(400) | Y |  |
| 82 | Owner_Org_ROid |  | GUID | Y |  |

### CLOSE_CHECK_PLAN_ITEM - 盘点方案商品列表单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CLOSE_CHECK_PLAN_ITEM_ID | 主键 | GUID | Y | Y |
| 2 | CATEGORY_ID | 类别 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | CLOSE_CHECK_PLAN_ID |  | GUID | Y |  |

### CLOSE_CHECK_PLAN_ITEM2 - 盘点方案商品明细单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CLOSE_CHECK_PLAN_ITEM2_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | CLOSE_CHECK_PLAN_ID |  | GUID | Y |  |

### CLOSE_CHECK_PLAN_SHOP - 盘点方案门店范围单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CLOSE_CHECK_PLAN_SHOP_ID | 主键 | GUID | Y | Y |
| 2 | SHOP_ID | 门店 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | CLOSE_CHECK_PLAN_ID |  | GUID | Y |  |