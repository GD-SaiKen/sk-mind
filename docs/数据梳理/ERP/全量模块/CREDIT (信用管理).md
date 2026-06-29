---
module: "CREDIT"
name_zh: "信用管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 122
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# CREDIT (信用管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 122

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


- **CREDIT_AREA (信控区域)**
- **CREDIT_AREA_D (信控区域单身)**
- **CREDIT_RULE (信控策略)**


---


---


> Tables: 3

### CREDIT_AREA (信控区域)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CREDIT_AREA_ID | 主键 | GUID | Y | Y |
| 4 | CREDIT_AREA_CODE | 信控区域编号 | string(8) | Y |  |
| 5 | CREDIT_AREA_NAME | 信控区域名称 | string(40) | Y |  |
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

### CREDIT_AREA_D (信控区域单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CREDIT_AREA_D_ID | 主键 | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 29 | ApproveDate | 修改日期 | date | Y |  |
| 30 | ApproveBy | 修改人 | GUID | Y |  |
| 31 | ORG_ID_RTK |  | string(400) | Y |  |
| 32 | ORG_ID_ROid |  | GUID | Y |  |
| 33 | CREDIT_AREA_ID |  | GUID | Y |  |

### CREDIT_RULE (信控策略)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CREDIT_RULE_ID | 主键 | GUID | Y | Y |
| 4 | CREDIT_RULE_CODE | 信控策略编号 | string(8) | Y |  |
| 5 | CREDIT_RULE_NAME | 信控策略名称 | string(40) | Y |  |
| 6 | CO_RATE | 未订货的合同金额比率 | number(5,4) | Y |  |
| 7 | SO_RATE | 未销货的订单金额比率 | number(5,4) | Y |  |
| 8 | SD_RATE | 未结算的销货金额比率 | number(5,4) | Y |  |
| 9 | AR_RATE | 应收账款比率 | number(5,4) | Y |  |
| 10 | BR_RATE | 应收票据比率 | number(5,4) | Y |  |
| 11 | ADV_RATE | 预收款比率 | number(5,4) | Y |  |
| 12 | CO_SAVE_CHECK | 合同保存时信用检查 | string(40) | Y |  |
| 13 | CO_APPROVE_CHECK | 合同审核时信用检查 | string(40) | Y |  |
| 14 | SO_SAVE_CHECK | 订单保存时信用检查 | string(40) | Y |  |
| 15 | SO_APPROVE_CHECK | 订单审核时信用检查 | string(40) | Y |  |
| 16 | SD_SAVE_CHECK | 销货保存时信用检查 | string(40) | Y |  |
| 17 | SD_APPROVE_CHECK | 销货审核时信用检查 | string(40) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | INCLUDE_BAD_DEBT | 包括坏账 | number(0/1) | Y |  |
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
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |