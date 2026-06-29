---
module: "BgSchedule"
name_zh: "后台任务"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 70
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# BgSchedule (后台任务)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 70

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


- **BgSchedule_SubTasks**
- **BgSchedule_SubTasks_EventNotifies**


---


---


> Tables: 3

### BgSchedule (背景排程实体)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | Id | 主键 | GUID | Y | Y |
| 4 | Code | 排程编号 | string(100) | Y |  |
| 5 | DisplayName | 排程名称 | string(200) | Y |  |
| 6 | Memo | 备注 | string(510) | Y |  |
| 7 | IsOnErrorResumeNext | 错误是否继续执行 | number(0/1) | Y |  |
| 8 | PeriodicHour | 周期任务执行小时 | number | Y |  |
| 9 | PeriodicMinute | 周期任务执行分 | number | Y |  |
| 10 | PeriodicMode | 周期方式 | string(40) | Y |  |
| 11 | IntervalDay | 间隔几天 | number | Y |  |
| 12 | IntervalWeek | 间隔几周 | number | Y |  |
| 13 | IntervalWeekDayofWeek | 间隔每N个周的周几 | number | Y |  |
| 14 | IntervalMonth | 间隔几个月 | number | Y |  |
| 15 | IntervalMonthDayofMonth | 间隔每N个月的几号 | number | Y |  |
| 16 | IntervalMonthWeek | 间隔几个月第N个周N | number | Y |  |
| 17 | IntervalMonthWeekNo | 间隔N个月第几个周N | number | Y |  |
| 18 | IntervalMonthDayofWeek | 间隔N个月第N个周几 | number | Y |  |
| 19 | PeriodicRangeMode | 周期任务起讫方式 | string(40) | Y |  |
| 20 | PeriodicStartDate | 周期任务开始日期 | date | Y |  |
| 21 | PeriodicEndDate | 周期任务结束日期 | date | Y |  |
| 22 | PeriodicExecuteTimes | 周期任务执行次数 | number | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | Owner_Org_RTK |  | string(400) | Y |  |
| 34 | Owner_Org_ROid |  | GUID | Y |  |

### BgSchedule_SubTasks

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Id |  | GUID | Y | Y |
| 3 | ProgramId |  | string(100) | Y |  |
| 4 | ExecuteName |  | string(100) | Y |  |
| 5 | ConditionProject |  | string | Y |  |
| 6 | TaskInfo |  | string | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 15 | ApproveDate | 修改日期 | date | Y |  |
| 16 | ApproveBy | 修改人 | GUID | Y |  |
| 17 | F_Id |  | GUID | Y |  |

### BgSchedule_SubTasks_EventNotifies

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Id |  | GUID | Y | Y |
| 2 | TaskEvent |  | string(40) | Y |  |
| 3 | NotifyMode |  | string(40) | Y |  |
| 4 | Recipients |  | string | Y |  |
| 5 | RecipientsName |  | string | Y |  |
| 6 | Subject |  | string(510) | Y |  |
| 7 | IsAutoSubject |  | number(0/1) | Y |  |
| 8 | Content |  | string | Y |  |
| 9 | Version | 版本号，不要随意更改 | binary | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 17 | ApproveDate | 修改日期 | date | Y |  |
| 18 | ApproveBy | 修改人 | GUID | Y |  |
| 19 | F_Id |  | GUID | Y |  |