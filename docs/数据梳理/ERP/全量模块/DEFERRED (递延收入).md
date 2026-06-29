---
module: "DEFERRED"
name_zh: "递延收入"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 139
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# DEFERRED (递延收入)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 139

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


- **DEFERRED_REV_DOC (递延收益单)**
- **DEFERRED_REV_DOC_D (递延收益单单身)**


---


---


> Tables: 2

### DEFERRED_REV_DOC (递延收益单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DEFERRED_REV_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | DREM_FLAG | 递延收益认列使用预估模式标识 | number(0/1) | Y |  |
| 12 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 13 | ESTI_DOC_TYPE | 预估单据类型 | number | Y |  |
| 14 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 15 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 16 | EMPLOYEE_ID | 业务人员 | GUID | Y |  |
| 17 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 18 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 19 | ITEM_NAME | 品名 | string(120) | Y |  |
| 20 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 21 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 22 | SALES_REV_AMT | 销售收入 | number(23,8) | Y |  |
| 23 | DEFERRED_REV_AMT | 递延收益 | number(23,8) | Y |  |
| 24 | TDR_BENCHMARK_RATE | 转递延基准比率 | number(5,4) | Y |  |
| 25 | TDR_ACTUAL_RATE | 转递延实际比率 | number(5,4) | Y |  |
| 26 | SD_S_ACCOUNT_YEAR | 来源单据确认收入_开始会计年度 | string(8) | Y |  |
| 27 | SD_S_ACCOUNT_PERIOD_SEQNO | 来源单据确认收入_开始会计期间序号 | number | Y |  |
| 28 | SD_S_ACCOUNT_PERIOD_CODE | 来源单据确认收入_开始会计期间期号 | string(20) | Y |  |
| 29 | ED_S_ACCOUNT_YEAR | 预估单据确认收入_开始会计年度 | string(8) | Y |  |
| 30 | ED_S_ACCOUNT_PERIOD_SEQNO | 预估单据确认收入_开始会计期间序号 | number | Y |  |
| 31 | ED_S_ACCOUNT_PERIOD_CODE | 预估单据确认收入_开始会计期间期号 | string(20) | Y |  |
| 32 | CD_S_ACCOUNT_YEAR | 合约_开始会计年度 | string(8) | Y |  |
| 33 | CD_S_ACCOUNT_PERIOD_SEQNO | 合约_开始会计期间序号 | number | Y |  |
| 34 | CD_S_ACCOUNT_PERIOD_CODE | 合约_开始会计期间期号 | string(20) | Y |  |
| 35 | DEFERRED_PERIODS | 递延期数 | number | Y |  |
| 36 | EDC_FLAG | 受控预估单据标识 | number(0/1) | Y |  |
| 37 | EDC2_FLAG | 受控预估单据标识2 | number(0/1) | Y |  |
| 38 | ED_SALES_REV_AMT | 预估单据销售收入 | number(23,8) | Y |  |
| 39 | ED_DEFERRED_REV_AMT | 预估单据递延收益 | number(23,8) | Y |  |
| 40 | ACCRUED_REV_AMT | 需确认收入合计 | number(23,8) | Y |  |
| 41 | REVENUE_AMT | 已确认收入合计 | number(23,8) | Y |  |
| 42 | BALANCE_AMT | 未确认收入合计 | number(23,8) | Y |  |
| 43 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 44 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 45 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 46 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 47 | REMARK | 备注 | string(510) | Y |  |
| 48 | REFERENCE_DOC_LINE_ID | 参考单据行 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | PrintCount | 打印次数 | number | Y |  |
| 51 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 52 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 53 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 54 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | Attachments | 附件 | string | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 67 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 68 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 69 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 70 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 71 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 72 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 73 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 74 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 75 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 76 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 77 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 78 | UDF041 | 自定义字段12 | date | Y |  |
| 79 | UDF042 | 自定义字段13 | date | Y |  |
| 80 | UDF051 | 自定义字段14 | GUID | Y |  |
| 81 | UDF052 | 自定义字段15 | GUID | Y |  |
| 82 | UDF053 | 自定义字段16 | GUID | Y |  |
| 83 | UDF054 | 自定义字段17 | GUID | Y |  |
| 84 | Owner_Org_RTK |  | string(400) | Y |  |
| 85 | Owner_Org_ROid |  | GUID | Y |  |
| 86 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 87 | SOURCE_ID_ROid |  | GUID | Y |  |
| 88 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 89 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 90 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 91 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 92 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 93 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 94 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 95 | SOURCE5_ID_ROid |  | GUID | Y |  |

### DEFERRED_REV_DOC_D (递延收益单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DEFERRED_REV_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | OWNER_ORG_ID | 公司 | GUID | Y |  |
| 4 | CD_ACCOUNT_YEAR | 合约会计年度 | string(8) | Y |  |
| 5 | CD_ACCOUNT_PERIOD_SEQNO | 合约会计期间序号 | number | Y |  |
| 6 | CD_ACCOUNT_PERIOD_CODE | 合约会计期间期号 | string(20) | Y |  |
| 7 | FI_ACCOUNT_YEAR | 财务确认收入会计年度 | string(8) | Y |  |
| 8 | FI_ACCOUNT_PERIOD_SEQNO | 财务确认收入会计期间序号 | number | Y |  |
| 9 | FI_ACCOUNT_PERIOD_CODE | 财务确认收入会计期间期号 | string(20) | Y |  |
| 10 | ACCRUED_REV_AMT | 需确认收入 | number(23,8) | Y |  |
| 11 | REVENUE_AMT | 已确认收入 | number(23,8) | Y |  |
| 12 | BALANCE_AMT | 未确认收入 | number(23,8) | Y |  |
| 13 | REFERENCE_RATE | 参考比率 | number(5,4) | Y |  |
| 14 | ACTUAL_RATE | 实际比率 | number(5,4) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | Version | 版本号，不要随意更改 | binary | Y |  |
| 17 | CreateDate | 创建日期 | date | Y |  |
| 18 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 19 | ModifiedDate | 修改日期 | date | Y |  |
| 20 | CreateBy | 创建者 | GUID | Y |  |
| 21 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 22 | ModifiedBy | 修改者 | GUID | Y |  |
| 23 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 24 | ApproveDate | 修改日期 | date | Y |  |
| 25 | ApproveBy | 修改人 | GUID | Y |  |
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
| 44 | DEFERRED_REV_DOC_ID |  | GUID | Y |  |