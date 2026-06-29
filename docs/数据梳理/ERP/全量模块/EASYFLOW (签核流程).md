---
module: "EASYFLOW"
name_zh: "签核流程"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 239
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# EASYFLOW (签核流程)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 239

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]
- [[PARA (参数设置)|PARA (参数设置)]]

---

## Tables


- **EASYFLOW_OBJECT**
- **EASYFLOW_SIGN_INFO**
- **EASYFLOW_TEMPLATE**
- **EASYFLOW_TEMPLATE_D**
- **EASYFLOW_TEMPLATE_SD**
- **EASYFLOW_TEMPLATE_SDD**


---


---


> Tables: 6

### EASYFLOW_OBJECT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | EASYFLOW_OBJECT_ID | 主键 | GUID | Y | Y |
| 2 | PROGRAM_NO | 作业编号 | string(400) | Y |  |
| 3 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
| 4 | TYPEKEY | TYPEKEY编号 | string(400) | Y |  |
| 5 | PROGRAM_TYPE | 作业类型 | string(40) | Y |  |
| 6 | PROGRAM_OWNER_ORG_RTK | 作业组织类型 | string(40) | Y |  |
| 7 | DOC_ID | 单据类型字段编号 | string(400) | Y |  |
| 8 | DOC_NO | 单号字段编号 | string(400) | Y |  |
| 9 | INDIVIDUAL_CASE | 是否个案 | number(0/1) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
| 17 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 18 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 19 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 20 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 21 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 22 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 23 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 24 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 25 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 26 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 27 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 28 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 29 | UDF041 | 自定义字段12 | date | Y |  |
| 30 | UDF042 | 自定义字段13 | date | Y |  |
| 31 | UDF051 | 自定义字段14 | GUID | Y |  |
| 32 | UDF052 | 自定义字段15 | GUID | Y |  |
| 33 | UDF053 | 自定义字段16 | GUID | Y |  |
| 34 | UDF054 | 自定义字段17 | GUID | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |

### EASYFLOW_SIGN_INFO

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | EASYFLOW_SIGN_INFO_ID | 主键 | GUID | Y | Y |
| 2 | PROGRAM_NO | 作业编号 | string(80) | Y |  |
| 3 | DOC_CODE | 单据类型 | string(8) | Y |  |
| 4 | DOC_NO | 单号 | string(80) | Y |  |
| 5 | FLOW_ID | 工作流单别 | string(60) | Y |  |
| 6 | SHEET_NO | 工作流单号 | string(80) | Y |  |
| 7 | FLOW_NO | 关号 | string(8) | Y |  |
| 8 | BRANCH_NO | 支号 | string(8) | Y |  |
| 9 | ORDER_NO | 签核序号 | string(4) | Y |  |
| 10 | EMPOLYEE_ID | 签核人员编号 | string(20) | Y |  |
| 11 | EMPOLYEE_NAME | 签核人员姓名 | string(80) | Y |  |
| 12 | POSITION_GRADE_NAME | 签核人员职称 | string(40) | Y |  |
| 13 | APPROVAL_TYPE | 签核种类 | string(40) | Y |  |
| 14 | APPROVAL_RESULT | 签核结果 | string(40) | Y |  |
| 15 | APPROVAL_OPINION | 签核意见 | string(8000) | Y |  |
| 16 | DATE | 签核日期时间 | string(40) | Y |  |
| 17 | PIC_NAME | 签名图档名称 | string(60) | Y |  |
| 18 | PROGRAM_GUID | 作业GUID | GUID | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
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
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |

### EASYFLOW_TEMPLATE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | EASYFLOW_TEMPLATE_ID | 主键 | GUID | Y | Y |
| 2 | PROGRAM_NO | 作业编号 | string(400) | Y |  |
| 3 | PROGRAM_NAME | 作业名称 | string(400) | Y |  |
| 4 | VOUCHER_TYPE | 凭证类型 | string(400) | Y |  |
| 5 | VOUCHER_NO | 凭证编号 | string(400) | Y |  |
| 6 | SIGN_FLOW | 签核流程 | string(40) | Y |  |
| 7 | TRANS_MODE | 传送模式 | string(40) | Y |  |
| 8 | CANCEL_APPROVE | 是否撤销审核 | number(0/1) | Y |  |
| 9 | CANCEL | 是否作废 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | TABEL_TRANS_STATUS | 表传送状态 | string(40) | Y |  |
| 12 | TYPEKEY | 作业TYPEKEY | string(80) | Y |  |
| 13 | DOC_ID | 单据性质 | GUID | Y |  |
| 14 | PROGRAM_CHTNAME | 作业繁体名称 | string(400) | Y |  |
| 15 | PROGRAM_CHSNAME | 作业简体名称 | string(400) | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
| 17 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 46 | PROGRAM_OWNER_ORG_RTK |  | string(400) | Y |  |
| 47 | PROGRAM_OWNER_ORG_ROid |  | GUID | Y |  |
| 48 | PROGRAM_ENGNAME | 作业英文名称 | string(400) | Y |  |

### EASYFLOW_TEMPLATE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PATH | 路径 | string(2000) | Y |  |
| 2 | EASYFLOW_TEMPLATE_D_ID |  | GUID | Y | Y |
| 3 | TABLE_SNAME | 实体代号 | string(400) | Y |  |
| 4 | TABLE_DISNAME | 实体名称 | string(400) | Y |  |
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
| 31 | EASYFLOW_TEMPLATE_ID |  | GUID | Y |  |
| 32 | TABLE_DISNAME1 | 实体繁体名称 | string(400) | Y |  |
| 33 | TABLE_DISNAME2 | 实体英文名称 | string(400) | Y |  |

### EASYFLOW_TEMPLATE_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | COLUMN_NAME | 字段名称 | string(200) | Y |  |
| 3 | COLUMN_TYPE | 字段类型：1.实体字段；2.带值字段；3.计算字段 | string(2) | Y |  |
| 4 | EXPRESSION | 公式表达式 | string(2000) | Y |  |
| 5 | REFERENCE_COLUMN | 带值引用字段 | string(200) | Y |  |
| 6 | REFERENCE_SOURCE | 带值来源字段 | string(200) | Y |  |
| 7 | EASYFLOW_TEMPLATE_SD_ID |  | GUID | Y | Y |
| 8 | ISSUE | 发布 | number(0/1) | Y |  |
| 9 | MSOURCE_WHERE_FIELD | 是否为多来源字段 | number(0/1) | Y |  |
| 10 | CONDITION | 条件字段 | number(0/1) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | PICKLIST_TYPE | PICKLIST类型 | string(80) | Y |  |
| 13 | DISPLAY_NAME | 字段中文名称 | string(200) | Y |  |
| 14 | DISPLAY_CHTNAME | 字段繁体名称 | string(200) | Y |  |
| 15 | DISPLAY_ENGNAME | 字段英文名称 | string(200) | Y |  |
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
| 41 | EASYFLOW_TEMPLATE_D_ID |  | GUID | Y |  |

### EASYFLOW_TEMPLATE_SDD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | REFERENCE_SOURCE | 带值来源字段 | string(200) | Y |  |
| 2 | SequenceNumber |  | number | Y |  |
| 3 | EASYFLOW_TEMPLATE_SDD_ID |  | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | EASYFLOW_TEMPLATE_SD_ID |  | GUID | Y |  |