---
module: "CST"
name_zh: "报关管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 171
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# CST (报关管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 171

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]
- [[DISCOUNT (折扣表)|DISCOUNT (折扣表)]]

---

## Tables


- **CST_ASTGY**
- **CST_ASTGY_D**
- **CST_AWB**
- **CST_AWB_D**
- **CST_AWB_PROCESS**
- **CST_AWB_VALID (成本核算工作台检查信息)**


---


---


> Tables: 6

### CST_ASTGY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CST_ASTGY_ID | 主键 | GUID | Y | Y |
| 4 | PDS | 参数集 | string | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | Attachments | 附件 | string | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |

### CST_ASTGY_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CST_ASTGY_D_ID | 主键 | string(400) | Y | Y |
| 3 | OPERATION_CODE | 工作项编号 | string(40) | Y |  |
| 4 | VALID_CODE | 检查项 | string(40) | Y |  |
| 5 | ABNORMAL_TYPE | 异常类型 | number | Y |  |
| 6 | IGNORE_FLAG | 可忽略标识 | number(0/1) | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | CST_ASTGY_ID |  | GUID | Y |  |

### CST_AWB

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CST_AWB_ID | 主键 | GUID | Y | Y |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 8 | PDS | 参数集 | string | Y |  |
| 9 | SYS_VERSION | 全局控制版号 | number | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
| 17 | Owner_Org_RTK |  | string(400) | Y |  |
| 18 | Owner_Org_ROid |  | GUID | Y |  |

### CST_AWB_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Version | 版本号，不要随意更改 | binary | Y |  |
| 3 | CST_AWB_D_ID | 主键 | GUID | Y | Y |
| 4 | OPERATION_CODE | 工作项编号 | string(40) | Y |  |
| 5 | TASK_ID | 后台任务 | GUID | Y |  |
| 6 | EFFECTIVE_STATUS | 生失效状态 | number | Y |  |
| 7 | EXECUTE_STATUS | 执行状态 | number | Y |  |
| 8 | PASSED_COUNT | 通过数 | number | Y |  |
| 9 | ERROR_COUNT | 错误数 | number | Y |  |
| 10 | WARING_COUNT | 警告数 | number | Y |  |
| 11 | PASSED_FLAG | 通过标识 | number(0/1) | Y |  |
| 12 | SYS_VERSION | 控制版号 | number | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | CST_AWB_ID |  | GUID | Y |  |

### CST_AWB_PROCESS

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Version | 版本号，不要随意更改 | binary | Y |  |
| 3 | CST_AWB_PROCESS_ID |  | GUID | Y | Y |
| 4 | COMPANY_ID | 公司 | GUID | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | PROCESS_CODE | 流程编号 | string(40) | Y |  |
| 8 | SYS_VERSION | 流程控制版号 | number | Y |  |
| 9 | SYS_VERSION2 | 流程控制版号2 | number | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
| 17 | CST_AWB_ID |  | GUID | Y |  |

### CST_AWB_VALID (成本核算工作台检查信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | CST_AWB_VALID_ID | 主键 | GUID | Y | Y |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | OPERATION_CODE | 工作项编号 | string(40) | Y |  |
| 8 | VALID_CODE | 检查项编号 | string(40) | Y |  |
| 9 | ABNORMAL_TYPE | 异常类型 | number | Y |  |
| 10 | IGNORE_FLAG | 可忽略标识 | number(0/1) | Y |  |
| 11 | VALID_STATUS | 检查状态 | number | Y |  |
| 12 | PASSED_FLAG | 通过标识 | number(0/1) | Y |  |
| 13 | REPORT_LINK_PARA | 报表联查参数 | string | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |