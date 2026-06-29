---
module: "POINT"
name_zh: "积分促销"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 157
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# POINT (积分促销)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 157

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]

---

## Tables


- **POINT_PROMOTION_DOC**
- **POINT_PROMOTION_DOC_D**
- **POINT_PROMOTION_DOC_D1**
- **POINT_PROMOTION_DOC_D2**


---


---


> Tables: 4

### POINT_PROMOTION_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | POINT_PROMOTION_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PROMOTION_SCHEDULE_ID | 促销活动 | GUID | Y |  |
| 9 | SHOP_RANGE | 门店范围 | string(40) | Y |  |
| 10 | BEGDT | 开始日期 | date | Y |  |
| 11 | BEGTM | 开始时间 | date | Y |  |
| 12 | ENDDT | 结束日期 | date | Y |  |
| 13 | ENDTM | 结束时间 | date | Y |  |
| 14 | WEEK_CIRCULATION | 星期循环 | number(0/1) | Y |  |
| 15 | MONDAY | 周一 | number(0/1) | Y |  |
| 16 | TUESDAY | 周二 | number(0/1) | Y |  |
| 17 | WEDNESDAY | 周三 | number(0/1) | Y |  |
| 18 | THURSDAY | 周四 | number(0/1) | Y |  |
| 19 | FRIDAY | 周五 | number(0/1) | Y |  |
| 20 | SATURDAY | 周六 | number(0/1) | Y |  |
| 21 | SUNDAY | 周日 | number(0/1) | Y |  |
| 22 | TIME_CIRCULATION | 时间循环 | number(0/1) | Y |  |
| 23 | WEEK_BEGTM | 起始时间 | date | Y |  |
| 24 | WEEK_ENDTM | 截止时间 | date | Y |  |
| 25 | PROMOTION_DESCRIPTION | 促销简述 | string(200) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | PrintCount | 打印次数 | number | Y |  |
| 28 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 29 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 30 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 31 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 32 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 33 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 34 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 35 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 36 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 37 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 38 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 39 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 40 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 41 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 42 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 43 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 44 | UDF041 | 自定义字段12 | date | Y |  |
| 45 | UDF042 | 自定义字段13 | date | Y |  |
| 46 | UDF051 | 自定义字段14 | GUID | Y |  |
| 47 | UDF052 | 自定义字段15 | GUID | Y |  |
| 48 | UDF053 | 自定义字段16 | GUID | Y |  |
| 49 | UDF054 | 自定义字段17 | GUID | Y |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | Attachments | 附件 | string | Y |  |
| 57 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | Owner_Org_RTK |  | string(400) | Y |  |
| 63 | Owner_Org_ROid |  | GUID | Y |  |

### POINT_PROMOTION_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | POINT_PROMOTION_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 门店 | GUID | Y |  |
| 4 | JOIN_COUNTER | 参与租柜 | string(40) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | POINT_PROMOTION_DOC_ID |  | GUID | Y |  |

### POINT_PROMOTION_DOC_D1

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | POINT_PROMOTION_DOC_D1_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 门店 | GUID | Y |  |
| 4 | COUNTER_ID | 租柜 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | POINT_PROMOTION_DOC_D_ID |  | GUID | Y |  |

### POINT_PROMOTION_DOC_D2

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | POINT_PROMOTION_DOC_D2_ID | 主键 | GUID | Y | Y |
| 3 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 4 | POINT_MULTIPLE | 积分倍数 | number | Y |  |
| 5 | POINT_AMT | 积分赠送额 | number(16,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | POINT_PROMOTION_DOC_ID |  | GUID | Y |  |