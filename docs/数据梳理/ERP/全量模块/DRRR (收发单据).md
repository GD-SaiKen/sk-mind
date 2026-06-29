---
module: "DRRR"
name_zh: "收发单据"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 100
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# DRRR (收发单据)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 100

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


- **DRRR_DOC (递延确认收入单)**
- **DRRR_DOC_D (递延确认收入单单身)**


---


---


> Tables: 2

### DRRR_DOC (递延确认收入单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DRRR_DOC_ID | 主键 | GUID | Y | Y |
| 4 | DOC_ID | 单据类型 | GUID | Y |  |
| 5 | DOC_NO | 单号 | string(40) | Y |  |
| 6 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | REVENUE_AMT | 确认收入合计 | number(23,8) | Y |  |
| 11 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 12 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 13 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 14 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
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
| 34 | PrintCount | 打印次数 | number | Y |  |
| 35 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 36 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 37 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 38 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Attachments | 附件 | string | Y |  |
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### DRRR_DOC_D (递延确认收入单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DRRR_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | DEFERRED_REV_DOC_ID | 递延收益单 | GUID | Y |  |
| 4 | DEFERRED_REV_DOC_D_ID | 递延收益单行 | GUID | Y |  |
| 5 | CD_ACCOUNT_YEAR | 合约会计年度 | string(8) | Y |  |
| 6 | CD_ACCOUNT_PERIOD_SEQNO | 合约会计期间序号 | number | Y |  |
| 7 | CD_ACCOUNT_PERIOD_CODE | 合约会计期间期号 | string(20) | Y |  |
| 8 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 9 | REVENUE_AMT | 确认收入 | number(23,8) | Y |  |
| 10 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 11 | EMPLOYEE_ID | 业务人员 | GUID | Y |  |
| 12 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 13 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 14 | ITEM_NAME | 品名 | string(120) | Y |  |
| 15 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 16 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
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
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | DRRR_DOC_ID |  | GUID | Y |  |