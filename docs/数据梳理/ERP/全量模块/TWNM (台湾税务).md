---
module: "TWNM"
name_zh: "台湾税务"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 0
columns: 0
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52
---

# TWNM (台湾税务)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 0 | Columns: 0

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

# TWNM (台湾税务)

> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
 | Server: .\\SQLEXPRESS | Tables: 36 | Generated: 2026-06-25 10:52

---


> Tables: 36

### TWNM_ARF

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_ARF_ID | 主键 | GUID | Y | Y |
| 4 | FORMAT_CODE | 格式编号 | string(12) | Y |  |
| 5 | FORMAT_NAME | 格式名称 | string(40) | Y |  |
| 6 | FORMAT_NATURE | 格式性质 | number | Y |  |
| 7 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 8 | SEPARATE_MODE | 分隔方式 | number | Y |  |
| 9 | EXPORT_FILE_NAME | 导出档案名称 | string(40) | Y |  |
| 10 | SEPARATE_SYMBOL_LENGTH | 分隔符长度 | number | Y |  |
| 11 | TRANS_AREA | 业务范围 | number | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | EXTENSION | 副档名 | number | Y |  |
| 14 | CODING_METHOD | 编码方式 | number | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_ARF_CODE_TRANSFER - 银行自动汇款代码转换设定

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_ARF_CODE_TRANSFER_ID | 主键 | GUID | Y | Y |
| 4 | TWNM_ARF_ID | 格式编号 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
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
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_ARF_CODE_TRANSFER_D - 银行自动汇款代码转换设定单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_ARF_CODE_TRANSFER_D_ID | 主键 | GUID | Y | Y |
| 3 | TWNM_ARF_D_ID | 自动汇款格式序号 | GUID | Y |  |
| 4 | OLD_REPLACE_CODE | 原值 | string(20) | Y |  |
| 5 | NEW_REPLACE_CODE | 新转换值 | string(20) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | TWNM_ARF_CODE_TRANSFER_ID |  | GUID | Y |  |

### TWNM_ARF_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_ARF_D_ID | 主键 | GUID | Y | Y |
| 3 | DATA_TYPE1 | 资料类型 | number | Y |  |
| 4 | DATA_NATURE | 资料性质 | number | Y |  |
| 5 | COLUMN | 字段 | string(60) | Y |  |
| 6 | COLUMN_NAME | 字段名称 | string(60) | Y |  |
| 7 | DATA_TYPE2 | 资料类型 | number | Y |  |
| 8 | FIXED_VALUE | 固定值 | string(40) | Y |  |
| 9 | CALC_MODE | 计算方式 | number | Y |  |
| 10 | COLUMN_LENGTH | 字段长度 | number | Y |  |
| 11 | DECIMAL_PLACE | 小数位数 | number | Y |  |
| 12 | DECIMAL_POINT_FLAG | 转出小数点标识 | number(0/1) | Y |  |
| 13 | DATE_FORMAT | 日期格式 | number | Y |  |
| 14 | FILL_MODE | 填补方式 | number | Y |  |
| 15 | FILL_DIRECTION | 填补方向 | number | Y |  |
| 16 | FILL_CHARACTER | 填补字符 | string(2) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | COMPUTE_LEVEL1 | 合计阶1 | number | Y |  |
| 19 | COMPUTE_LEVEL2 | 合计阶2 | number | Y |  |
| 20 | COMPUTE_LEVEL3 | 合计阶3 | number | Y |  |
| 21 | COMPUTE_LEVEL4 | 合计阶4 | number | Y |  |
| 22 | COMPUTE_LEVEL5 | 合计阶5 | number | Y |  |
| 23 | CHECK_FIELD_FLAG | 检查字段标识 | number(0/1) | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | TWNM_ARF_ID |  | GUID | Y |  |

### TWNM_ARF_DEFAULT_DATA - 自动汇款格式默认资料

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_ARF_DEFAULT_DATA_ID | 主键 | GUID | Y | Y |
| 4 | FIN_INSTITUTION_REGION | 金融机构所属区域 | number | Y |  |
| 5 | FIN_INSTITUTION_CODE | 金融机构编号 | string(40) | Y |  |
| 6 | FIN_INSTITUTION_NO | 金融机构代码 | string(40) | Y |  |
| 7 | FIN_INSTITUTION_FULL_NAME | 金融机构全称 | string(144) | Y |  |
| 8 | FIN_INSTITUTION_NAME | 金融机构简称 | string(40) | Y |  |
| 9 | SEPARATE_MODE | 分隔方式 | number | Y |  |
| 10 | EXPORT_FILE_NAME | 导出档案名称 | string(40) | Y |  |
| 11 | SEPARATE_SYMBOL_LENGTH | 分隔符长度 | number | Y |  |
| 12 | TRANS_AREA | 业务范围 | number | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | EXTENSION | 副档名 | number | Y |  |
| 15 | CODING_METHOD | 编码方式 | number | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
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
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_ARF_DEFAULT_DATA_D - 自动汇款格式默认资料单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | TWNM_ARF_DEFAULT_DATA_D_ID | 主键 | GUID | Y | Y |
| 2 | SEQNO | 顺序号 | number | Y |  |
| 3 | DATA_TYPE1 | 资料类型 | number | Y |  |
| 4 | DATA_NATURE | 资料性质 | number | Y |  |
| 5 | COLUMN | 字段 | string(60) | Y |  |
| 6 | COLUMN_NAME | 字段名称 | string(60) | Y |  |
| 7 | DATA_TYPE2 | 数据类型 | number | Y |  |
| 8 | FIXED_VALUE | 固定值 | string(40) | Y |  |
| 9 | CALC_MODE | 计算方式 | number | Y |  |
| 10 | COLUMN_LENGTH | 字段长度 | number | Y |  |
| 11 | DECIMAL_PLACE | 小数位数 | number | Y |  |
| 12 | DECIMAL_POINT_FLAG | 转出小数点标识 | number(0/1) | Y |  |
| 13 | DATE_FORMAT | 日期格式 | number | Y |  |
| 14 | FILL_MODE | 填补方式 | number | Y |  |
| 15 | FILL_DIRECTION | 填补方向 | number | Y |  |
| 16 | FILL_CHARACTER | 填补字符 | string(2) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | COMPUTE_LEVEL1 | 合计阶1 | number | Y |  |
| 19 | COMPUTE_LEVEL2 | 合计阶2 | number | Y |  |
| 20 | COMPUTE_LEVEL3 | 合计阶3 | number | Y |  |
| 21 | COMPUTE_LEVEL4 | 合计阶4 | number | Y |  |
| 22 | COMPUTE_LEVEL5 | 合计阶5 | number | Y |  |
| 23 | CHECK_FIELD_FLAG | 检查字段标识 | number(0/1) | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | TWNM_ARF_DEFAULT_DATA_ID |  | GUID | Y |  |

### TWNM_B008 - TWNM_B008

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | TWNM_B008_ID | 主键 | GUID | Y | Y |
| 2 | TWNM_B008_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### TWNM_B009 - TWNM_B009

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | TWNM_B009_ID | 主键 | GUID | Y | Y |
| 2 | TWNM_B009_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### TWNM_BANK_ACCOUNT_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_BANK_ACCOUNT_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 8 | OPENING_BANK_ACCOUNT_AMT_TC | 银行账号期初余额（原币） | number(23,8) | Y |  |
| 9 | OPENING_BANK_ACCOUNT_AMT_FC | 银行账号期初余额（本币） | number(23,8) | Y |  |
| 10 | INITIAL_AMT_TC | 银行账号本期发生额（原币） | number(23,8) | Y |  |
| 11 | INITIAL_AMT_FC | 银行账号本期发生额（本币） | number(23,8) | Y |  |
| 12 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
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
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_BANK_ACCOUNT_HISTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_BANK_ACCOUNT_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | BALANCE_DIRECTION | 方向 | number | Y |  |
| 7 | TRANS_NATURE | 交易性质 | number | Y |  |
| 8 | TRANS_DOC_ID | 交易单据类型 | GUID | Y |  |
| 9 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 10 | TRANS_DATE | 业务日期 | date | Y |  |
| 11 | AMT_TC | 原币金额 | number(23,8) | Y |  |
| 12 | AMT_FC | 本币金额 | number(23,8) | Y |  |
| 13 | AUTOMATIC_REMITTANCE_FLAG | 自动汇款 | number(0/1) | Y |  |
| 14 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 15 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 16 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 17 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 18 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
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
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |
| 52 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 53 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 57 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 58 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 59 | SOURCE3_ID_ROid |  | GUID | Y |  |

### TWNM_BANK_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_BANK_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 8 | OPENING_BANK_AMT_TC | 银行账号期初余额（原币） | number(23,8) | Y |  |
| 9 | OPENING_BANK_AMT_FC | 银行账号期初余额（本币） | number(23,8) | Y |  |
| 10 | INITIAL_AMT_TC | 银行账号本期发生额（原币） | number(23,8) | Y |  |
| 11 | INITIAL_AMT_FC | 银行账号本期发生额（本币） | number(23,8) | Y |  |
| 12 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 22 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 23 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 24 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 25 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 26 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 27 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 28 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 29 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 30 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 31 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 32 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 33 | UDF041 | 自定义字段12 | date | Y |  |
| 34 | UDF042 | 自定义字段13 | date | Y |  |
| 35 | UDF051 | 自定义字段14 | GUID | Y |  |
| 36 | UDF052 | 自定义字段15 | GUID | Y |  |
| 37 | UDF053 | 自定义字段16 | GUID | Y |  |
| 38 | UDF054 | 自定义字段17 | GUID | Y |  |
| 39 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_BANK_TRANS - 银行存提

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TWNM_BANK_TRANS_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 12 | CURRENCY_ID | 货币 | GUID | Y |  |
| 13 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 14 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 15 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 16 | TRANS_OBJECT_TYPE | 交易对象类型 | number | Y |  |
| 17 | AUTOMATIC_REMITTANCE_FLAG | 自动汇款 | number(0/1) | Y |  |
| 18 | DOC_SOURCE | 单据来源 | number | Y |  |
| 19 | VERIFICATION_FLAG | 需被应收/应付系统核销标识 | number(0/1) | Y |  |
| 20 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 21 | FIN_INSTITUTION_ACCOUNT_NO | 金融机构账号 | string(60) | Y |  |
| 22 | BANK_ACCOUNT2_ID | 银行账号2 | GUID | Y |  |
| 23 | CURRENCY2_ID | 货币2 | GUID | Y |  |
| 24 | AMT2_TC | 金额(原币)2 | number(23,8) | Y |  |
| 25 | EXCHANGE2_RATE | 汇率2 | number(18,9) | Y |  |
| 26 | AMT2_FC | 金额(本币)2 | number(23,8) | Y |  |
| 27 | CHARGE_BURDEN_MODE | 费用负担方式 | number | Y |  |
| 28 | JOURNAL_ENTRY_INDICTOR | 需生成分录标识 | number(0/1) | Y |  |
| 29 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 30 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 31 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 32 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 33 | DEP_WD_AMT_TC | 存提合计(原币) | number(23,8) | Y |  |
| 34 | DEP_WD_AMT_FC | 存提合计(本币) | number(23,8) | Y |  |
| 35 | CHARGE_AMT_TC | 费用合计(原币) | number(23,8) | Y |  |
| 36 | CHARGE_AMT_FC | 费用合计(本币) | number(23,8) | Y |  |
| 37 | REMARK | 备注 | string(510) | Y |  |
| 38 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 39 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 40 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 41 | SOURCE_ARAP_FLAG | 来源应收应付系统标识 | number(0/1) | Y |  |
| 42 | SCHEDULED_TRANSFER_FLAG | 预约付款标识 | number(0/1) | Y |  |
| 43 | ESTIMATE_EXCHANGE_RATE | 预约汇率 | number(18,9) | Y |  |
| 44 | ESTIMATE_AMT_TC | 预约金额(原币) | number(23,8) | Y |  |
| 45 | ESTIMATE_AMT_FC | 预约金额(本币) | number(23,8) | Y |  |
| 46 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 47 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 48 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 49 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 50 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 51 | CreateDate | 创建日期 | date | Y |  |
| 52 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 53 | ModifiedDate | 修改日期 | date | Y |  |
| 54 | CreateBy | 创建者 | GUID | Y |  |
| 55 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 56 | ModifiedBy | 修改者 | GUID | Y |  |
| 57 | Attachments | 附件 | string | Y |  |
| 58 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 63 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 64 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 65 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 66 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 67 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 68 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 69 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 70 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 71 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 72 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 73 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 74 | UDF041 | 自定义字段12 | date | Y |  |
| 75 | UDF042 | 自定义字段13 | date | Y |  |
| 76 | UDF051 | 自定义字段14 | GUID | Y |  |
| 77 | UDF052 | 自定义字段15 | GUID | Y |  |
| 78 | UDF053 | 自定义字段16 | GUID | Y |  |
| 79 | UDF054 | 自定义字段17 | GUID | Y |  |
| 80 | Version | 版本号，不要随意更改 | binary | Y |  |
| 81 | PrintCount | 打印次数 | number | Y |  |
| 82 | Owner_Org_RTK |  | string(400) | Y |  |
| 83 | Owner_Org_ROid |  | GUID | Y |  |
| 84 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 85 | SOURCE_ID_ROid |  | GUID | Y |  |
| 86 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 87 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 88 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 89 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 90 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 91 | SOURCE4_ID_ROid |  | GUID | Y |  |

### TWNM_BANK_TRANS_D - 银行存提单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_BANK_TRANS_D_ID | 主键 | GUID | Y | Y |
| 3 | LINE_TYPE | 行类型 | number | Y |  |
| 4 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 5 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | VERIFIED_AMT_TC | 已核销金额(原币) | number(23,8) | Y |  |
| 8 | VERIFIED_AMT_FC | 已核销金额(本币) | number(23,8) | Y |  |
| 9 | UNVERIFIED_AMT_TC | 未核销金额(原币) | number(23,8) | Y |  |
| 10 | UNVERIFIED_AMT_FC | 未核销金额(本币) | number(23,8) | Y |  |
| 11 | BUYER_ID | 业务人员 | GUID | Y |  |
| 12 | ADMIN_UNIT_ID | 业务部门 | GUID | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 39 | SOURCE_ID_ROid |  | GUID | Y |  |
| 40 | TWNM_BANK_TRANS_ID |  | GUID | Y |  |

### TWNM_BANK_TRANS_SD - 银行存提单子单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_BANK_TRANS_SD_ID | 主键 | GUID | Y | Y |
| 3 | TRANS_DOC_TYPE | 业务单据类型 | number | Y |  |
| 4 | VERIFIED_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 5 | VERIFIED_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 33 | SOURCE_ID_ROid |  | GUID | Y |  |
| 34 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 35 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 36 | TWNM_BANK_TRANS_D_ID |  | GUID | Y |  |

### TWNM_ESTI_CASH_FLOW - 维护预计收支

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TWNM_ESTI_CASH_FLOW_ID | 主键 | GUID | Y | Y |
| 7 | CASH_FLOW_TYPE | 收支别 | number | Y |  |
| 8 | TRANS_OBJECT_TYPE | 交易对象类型 | number | Y |  |
| 9 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 10 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 11 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 12 | FIN_INSTITUTION_ACCOUNT_NO | 金融机构账号 | string(60) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 15 | CURRENCY_ID | 货币 | GUID | Y |  |
| 16 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 17 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 18 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 19 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 20 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 21 | ESTIMATE_DATE | 预计日 | date | Y |  |
| 22 | REALIZED_FLAG | 已实现标识 | number(0/1) | Y |  |
| 23 | CHARGE_AMT_TC | 费用(原币) | number(23,8) | Y |  |
| 24 | VERIFICATION_FLAG | 需被应收/应付系统核销标识 | number(0/1) | Y |  |
| 25 | ARF_FLAG | 转出自动汇款资料标识 | number(0/1) | Y |  |
| 26 | SCHEDULED_TRANSFER_FLAG | 预约付款标识 | number(0/1) | Y |  |
| 27 | DOC_SOURCE | 单据来源 | number | Y |  |
| 28 | VERIFICATION_STATUS | 核销状态 | number | Y |  |
| 29 | TWNM_BANK_TRANS_ID | 银行存提单 | GUID | Y |  |
| 30 | CHARGE_BURDEN_MODE | 费用负担方式 | number | Y |  |
| 31 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 32 | SOURCE_ARAP_FLAG | 来源应收应付系统标识 | number(0/1) | Y |  |
| 33 | TWNM_ITEM_ID | 存提项目 | GUID | Y |  |
| 34 | CHARGE_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 35 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 36 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 37 | PrintCount | 打印次数 | number | Y |  |
| 38 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 39 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 40 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 41 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 42 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 43 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 44 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 45 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 46 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 47 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 48 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 49 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 50 | UDF041 | 自定义字段12 | date | Y |  |
| 51 | UDF042 | 自定义字段13 | date | Y |  |
| 52 | UDF051 | 自定义字段14 | GUID | Y |  |
| 53 | UDF052 | 自定义字段15 | GUID | Y |  |
| 54 | UDF053 | 自定义字段16 | GUID | Y |  |
| 55 | UDF054 | 自定义字段17 | GUID | Y |  |
| 56 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 57 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 58 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 59 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |
| 74 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 75 | SOURCE_ID_ROid |  | GUID | Y |  |
| 76 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 77 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 78 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 79 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 80 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 81 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 82 | SOURCE5_ID_RTK |  | string(400) | Y |  |
| 83 | SOURCE5_ID_ROid |  | GUID | Y |  |

### TWNM_EXCHANGE_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TWNM_EXCHANGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | EXCHANGE_LOSS_AMT | 汇兑损失合计 | number(23,8) | Y |  |
| 12 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 13 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 14 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 15 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | PrintCount | 打印次数 | number | Y |  |
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
| 36 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 37 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 38 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 39 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_EXCHANGE_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 3 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 4 | BALANCE_AMT_TC | 余额(原币) | number(23,8) | Y |  |
| 5 | BALANCE_AMT_FC | 余额(本币) | number(23,8) | Y |  |
| 6 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 7 | REVALUATION_BALANCE_AMT | 调整后余额 | number(23,8) | Y |  |
| 8 | CURRENCY_ID | 货币 | GUID | Y |  |
| 9 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 10 | TWNM_EXCHANGE_DOC_D_ID | 主键 | GUID | Y | Y |
| 11 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 12 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 13 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 14 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 15 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 16 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 17 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 18 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 19 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 20 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 21 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 22 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 23 | UDF041 | 自定义字段12 | date | Y |  |
| 24 | UDF042 | 自定义字段13 | date | Y |  |
| 25 | UDF051 | 自定义字段14 | GUID | Y |  |
| 26 | UDF052 | 自定义字段15 | GUID | Y |  |
| 27 | UDF053 | 自定义字段16 | GUID | Y |  |
| 28 | UDF054 | 自定义字段17 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | TWNM_EXCHANGE_DOC_ID |  | GUID | Y |  |

### TWNM_FINANCING_BN - 融资批号

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_FINANCING_BN_ID | 主键 | GUID | Y | Y |
| 4 | FINANCING_BN | 融资批号 | string(60) | Y |  |
| 5 | LIMIT_FLAG | 信用额度控制标识 | number(0/1) | Y |  |
| 6 | TWNM_FINANCING_LIMIT_ID | 信用群组 | GUID | Y |  |
| 7 | TWNM_FINANCING_LIMIT_D_ID | 信用群组行 | GUID | Y |  |
| 8 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 9 | BANK_ACCOUNT_ID | 借款账号 | GUID | Y |  |
| 10 | CLOSE_FLAG | 结案标识 | number(0/1) | Y |  |
| 11 | TRANS_DATE | 业务日期 | date | Y |  |
| 12 | FINANCING_METHOD_ID | 融资方式 | GUID | Y |  |
| 13 | FINANCING_NATURE | 融资性质 | number | Y |  |
| 14 | CYCLE_FINANCING_FLAG | 循环融资标识 | number(0/1) | Y |  |
| 15 | APR | 年利率 | number(6,5) | Y |  |
| 16 | VALUE_DATE | 起息日 | date | Y |  |
| 17 | DUE_DATE | 到期日 | date | Y |  |
| 18 | INTEREST_METHOD | 计息方式 | number | Y |  |
| 19 | REPAYMENT_METHOD | 还款方式 | number | Y |  |
| 20 | MONTH_REPAYMENT_DATE | 月还款日 | number | Y |  |
| 21 | AMT_TC | 金额合计(原币) | number(23,8) | Y |  |
| 22 | AMT_FC | 金额合计(本币) | number(23,8) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | CURRENCY_ID | 货币 | GUID | Y |  |
| 25 | PrintCount | 打印次数 | number | Y |  |
| 26 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 27 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 28 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 29 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | Owner_Org_RTK |  | string(400) | Y |  |
| 61 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_FINANCING_BN_D - 融资批号单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_FINANCING_BN_D_ID | 主键 | GUID | Y | Y |
| 3 | SOURCE_DOC_TYPE | 来源单据类型 | number | Y |  |
| 4 | CURRENCY_ID | 货币 | GUID | Y |  |
| 5 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 6 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 7 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 8 | FINANCING_INSTRUMENT_NO | 融资工具号 | string(80) | Y |  |
| 9 | FINANCING_SEQNO | 融资序号 | number | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE_ID_ROid |  | GUID | Y |  |
| 41 | TWNM_FINANCING_BN_ID |  | GUID | Y |  |

### TWNM_FINANCING_LIMIT - 融资额度

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_FINANCING_LIMIT_ID | 主键 | GUID | Y | Y |
| 4 | GROUP_CODE | 群组编号 | string(12) | Y |  |
| 5 | GROUP_NAME | 群组名称 | string(60) | Y |  |
| 6 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 7 | EFFECTIVE_DATE | 生效日期 | date | Y |  |
| 8 | EXPIRY_DATE | 失效日期 | date | Y |  |
| 9 | BANK_ACCOUNT_ID | 借款账号 | GUID | Y |  |
| 10 | CURRENCY_ID | 货币 | GUID | Y |  |
| 11 | LIMIT_AMT | 信用额度 | number(23,8) | Y |  |
| 12 | LIMIT_USED_AMT | 已用额度 | number(23,8) | Y |  |
| 13 | LIMIT_AVAILABLE_AMT | 可用额度 | number(23,8) | Y |  |
| 14 | FINANCING_BN_QTY | 融资批号数量 | number | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_FINANCING_LIMIT_D - 融资额度单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_FINANCING_LIMIT_D_ID | 主键 | GUID | Y | Y |
| 3 | FINANCING_METHOD_ID | 融资方式 | GUID | Y |  |
| 4 | LIMIT_AMT | 信用额度 | number(23,8) | Y |  |
| 5 | LIMIT_USED_AMT | 已用额度 | number(23,8) | Y |  |
| 6 | LIMIT_AVAILABLE_AMT | 可用额度 | number(23,8) | Y |  |
| 7 | FINANCING_BN_QTY | 融资批号数量 | number | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
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
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | TWNM_FINANCING_LIMIT_ID |  | GUID | Y |  |

### TWNM_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_ITEM_ID | 主键 | GUID | Y | Y |
| 4 | TWNM_ITEM_TYPE | 收付项目类别 | number | Y |  |
| 5 | TWNM_ITEM_CODE | 收付项目编号 | string(12) | Y |  |
| 6 | TWNM_ITEM_NAME | 收付项目名称 | string(60) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
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
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_LOAN_BALANCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_LOAN_BALANCE_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 6 | TRANS_NATURE | 交易性质 | number | Y |  |
| 7 | TWNM_LOAN_DOC_ID | 借款单 | GUID | Y |  |
| 8 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 9 | EXCHANGE_RATE | 借款汇率 | number(18,9) | Y |  |
| 10 | CURRENCY_ID | 借款货币 | GUID | Y |  |
| 11 | AMT_TC | 金额(原币) | number(23,8) | Y |  |
| 12 | AMT_FC | 金额(本币) | number(23,8) | Y |  |
| 13 | LOAN_PURPOSE_ID | 借款用途 | GUID | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_LOAN_DOC - 借款单

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | TWNM_LOAN_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | TWNM_FINANCING_BN_ID | 融资批号 | GUID | Y |  |
| 12 | LIMIT_FLAG | 信用额度控制标识 | number(0/1) | Y |  |
| 13 | BANK_ACCOUNT_ID | 借款账号 | GUID | Y |  |
| 14 | LOAN_PURPOSE_ID | 借款用途 | GUID | Y |  |
| 15 | CURRENCY_ID | 借款货币 | GUID | Y |  |
| 16 | EXCHANGE_RATE | 借款汇率 | number(18,9) | Y |  |
| 17 | LOAN_AMT_TC | 借款(原币) | number(23,8) | Y |  |
| 18 | LOAN_AMT_FC | 借款(本币) | number(23,8) | Y |  |
| 19 | VALUE_DATE | 起息日 | date | Y |  |
| 20 | DUE_DATE | 到期日 | date | Y |  |
| 21 | CREDIT_CURRENCY_ID | 信用货币 | GUID | Y |  |
| 22 | CREDIT_EXCHANGE_RATE | 信用汇率 | number(18,9) | Y |  |
| 23 | LIMIT_AVAILABLE_AMT | 可用额度 | number(23,8) | Y |  |
| 24 | LIMIT_USED_AMT | 占用额度 | number(23,8) | Y |  |
| 25 | EXPENSE_AMT_TC | 费用合计(原币) | number(23,8) | Y |  |
| 26 | EXPENSE_AMT_FC | 费用合计(本币) | number(23,8) | Y |  |
| 27 | LOAN_VERIFIED_AMT_TC | 核销借款(原币) | number(23,8) | Y |  |
| 28 | LOAN_VERIFIED_AMT_FC | 核销借款(本币) | number(23,8) | Y |  |
| 29 | LOAN_BALANCE_TC | 借款余额(原币) | number(23,8) | Y |  |
| 30 | LOAN_BALANCE_FC | 借款余额(本币) | number(23,8) | Y |  |
| 31 | LIMIT_RELEASED_AMT | 释放额度 | number(23,8) | Y |  |
| 32 | LIMIT_UNRELEASED_AMT | 占用余额 | number(23,8) | Y |  |
| 33 | LAST_PAYMENT_INTEREST_DATE | 最近付息日 | date | Y |  |
| 34 | LAST_REPAYMENT_DATE | 最近还款日 | date | Y |  |
| 35 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 36 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 37 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 38 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 39 | REMARK | 备注 | string(510) | Y |  |
| 40 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 41 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 42 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 43 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 44 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 45 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 46 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 47 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 48 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 49 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 50 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 51 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 52 | UDF041 | 自定义字段12 | date | Y |  |
| 53 | UDF042 | 自定义字段13 | date | Y |  |
| 54 | UDF051 | 自定义字段14 | GUID | Y |  |
| 55 | UDF052 | 自定义字段15 | GUID | Y |  |
| 56 | UDF053 | 自定义字段16 | GUID | Y |  |
| 57 | UDF054 | 自定义字段17 | GUID | Y |  |
| 58 | PrintCount | 打印次数 | number | Y |  |
| 59 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 60 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 61 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 62 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 63 | CreateDate | 创建日期 | date | Y |  |
| 64 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 65 | ModifiedDate | 修改日期 | date | Y |  |
| 66 | CreateBy | 创建者 | GUID | Y |  |
| 67 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 68 | ModifiedBy | 修改者 | GUID | Y |  |
| 69 | Attachments | 附件 | string | Y |  |
| 70 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 71 | Version | 版本号，不要随意更改 | binary | Y |  |
| 72 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 73 | ApproveDate | 修改日期 | date | Y |  |
| 74 | ApproveBy | 修改人 | GUID | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_LOAN_DOC_D - 借款单单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_LOAN_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 4 | SETTLEMENT_EXPENSE_ID | 费用项目 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
| 6 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 7 | AMT_TC | 费用(原币) | number(23,8) | Y |  |
| 8 | AMT_FC | 费用(本币) | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
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
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | TWNM_LOAN_DOC_ID |  | GUID | Y |  |

### TWNM_NOTE_BOOK

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_NOTE_BOOK_ID | 主键 | GUID | Y | Y |
| 4 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 5 | CURRENCY_ID | 货币 | GUID | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | Owner_Org_RTK |  | string(400) | Y |  |
| 38 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_NOTE_BOOK_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_NOTE_BOOK_D_ID | 主键 | GUID | Y | Y |
| 3 | NOTE_BOOK_NAME | 票据本名称 | string(20) | Y |  |
| 4 | PREFIX_CODE | 前置码 | string(10) | Y |  |
| 5 | START_NOTE_NO | 起始票据号码 | string(16) | Y |  |
| 6 | END_NOTE_NO | 截止票据号码 | string(16) | Y |  |
| 7 | USED_NO | 已使用号码 | string(16) | Y |  |
| 8 | EXPIRY_DATE | 失效日 | date | Y |  |
| 9 | PRIMARY_FLAG | 主要码 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | PRINT_LAYOUT_DEFAULT | 默认打印样式编号 | string(400) | Y |  |
| 12 | REPORT_TYPEKEY | 报表编号 | string(400) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | TWNM_NOTE_BOOK_ID |  | GUID | Y |  |

### TWNM_NOTE_HISTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_NOTE_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | NOTE_TYPE | 票据类型 | number | Y |  |
| 5 | SEQNO | 序号 | number | Y |  |
| 6 | TRANSACTION_DATE | 异动日 | date | Y |  |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | NOTE_ACTION | 动作 | number | Y |  |
| 9 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 10 | JOURNAL_INDICTOR | 产生分录码(已废除_命名错误) | number(0/1) | Y |  |
| 11 | JOURNAL_INDICATOR | 产生分录码 | number(0/1) | Y |  |
| 12 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 13 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 14 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 15 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 16 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 17 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | EXCHANGE_LOSS_AMT | 汇兑损失 | number(23,8) | Y |  |
| 20 | CHARGE_AMT_TC | 手续费(原币) | number(23,8) | Y |  |
| 21 | CHARGE_AMT_FC | 手续费(本币) | number(23,8) | Y |  |
| 22 | CHARGE_EXPENSE_ID | 手续费项目 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Owner_Org_RTK |  | string(400) | Y |  |
| 54 | Owner_Org_ROid |  | GUID | Y |  |
| 55 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 56 | SOURCE_ID_ROid |  | GUID | Y |  |

### TWNM_NP - 维护应付票据

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_NP_ID | 主键 | GUID | Y | Y |
| 4 | CURRENCY_ID | 货币 | GUID | Y |  |
| 5 | NOTE_TYPE_ID | 票据类型 | GUID | Y |  |
| 6 | NOTE_PREFIX_CODE | 前置码 | string(10) | Y |  |
| 7 | NOTE_NO | 票据流水号 | string(16) | Y |  |
| 8 | ISSUE_DATE | 开票日期 | date | Y |  |
| 9 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 10 | DUE_DATE | 票面到期日 | date | Y |  |
| 11 | EXPECT_CASHING_DATE | 预计兑现日 | date | Y |  |
| 12 | NOTE_STATUS | 票据状态 | number | Y |  |
| 13 | GUARANTEED_NOTE_FLAG | 保证票标志 | number(0/1) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | AMT_TC | 票面金额(原币) | number(23,8) | Y |  |
| 17 | AMT_FC | 票面金额(本币) | number(23,8) | Y |  |
| 18 | SETTLEMENT_OBJECT_TYPE | 收票人类型 | number | Y |  |
| 19 | PAYEE_FULL_NAME | 收票人全称 | string(144) | Y |  |
| 20 | NOTE_RECEIPT_MODE | 票据寄领方式 | number | Y |  |
| 21 | NOTE_MAIL_MODE | 票据邮寄方式 | number | Y |  |
| 22 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 23 | GLOB_ACCOUNT_CODE_ID | 应付票据科目-运营 | GUID | Y |  |
| 24 | GLMB_ACCOUNT_CODE_ID | 应付票据科目-管理 | GUID | Y |  |
| 25 | TWNM_NOTE_BOOK_D_ID | 银行票据本 | GUID | Y |  |
| 26 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 27 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 28 | VERIFICATION_FLAG | 需被应收/应付系统核销标识 | number(0/1) | Y |  |
| 29 | TWNM_ITEM_ID | 付款项目 | GUID | Y |  |
| 30 | VERIFIED_AMT_TC | 已核销金额(原币) | number(23,8) | Y |  |
| 31 | VERIFIED_AMT_FC | 已核销金额(本币) | number(23,8) | Y |  |
| 32 | UNVERIFIED_AMT_TC | 未核销金额(原币) | number(23,8) | Y |  |
| 33 | UNVERIFIED_AMT_FC | 未核销金额(本币) | number(23,8) | Y |  |
| 34 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 35 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 36 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 37 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 38 | DOC_SOURCE | 单据来源 | number | Y |  |
| 39 | SOURCE_ARAP_FLAG | 来源应收应付系统标识 | number(0/1) | Y |  |
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | PrintCount | 打印次数 | number | Y |  |
| 63 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 64 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 65 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 66 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 67 | CreateDate | 创建日期 | date | Y |  |
| 68 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 69 | ModifiedDate | 修改日期 | date | Y |  |
| 70 | CreateBy | 创建者 | GUID | Y |  |
| 71 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 72 | ModifiedBy | 修改者 | GUID | Y |  |
| 73 | Attachments | 附件 | string | Y |  |
| 74 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |
| 77 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 78 | SOURCE_ID_ROid |  | GUID | Y |  |
| 79 | SOURCE4_ID_RTK |  | string(400) | Y |  |
| 80 | SOURCE4_ID_ROid |  | GUID | Y |  |
| 81 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 82 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 83 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 84 | SOURCE3_ID_ROid |  | GUID | Y |  |
| 85 | FINANCING_SEQNO | 融资序号 | number | Y |  |
| 86 | FINANCING_FLAG | 融资标识 | number(0/1) | Y |  |

### TWNM_NP_BROKEN - 票据断号

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_NP_BROKEN_ID | 主键 | GUID | Y | Y |
| 4 | TWNM_NOTE_BOOK_D_ID | 票据本 | GUID | Y |  |
| 5 | NOTE_PREFIX_CODE | 前置码 | string(10) | Y |  |
| 6 | BROKEN_NO | 断号 | string(16) | Y |  |
| 7 | BROKEN_TYPE | 断号类别 | number | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
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
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_NP_D - 维护应付票据单身

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_NP_D_ID | 主键 | GUID | Y | Y |
| 3 | TRANS_DOC_TYPE | 业务单据类型 | number | Y |  |
| 4 | VERIFIED_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 5 | VERIFIED_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 27 | ApproveDate | 修改日期 | date | Y |  |
| 28 | ApproveBy | 修改人 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 36 | SOURCE_ID_ROid |  | GUID | Y |  |
| 37 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 39 | TWNM_NP_ID |  | GUID | Y |  |

### TWNM_NR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | TWNM_NR_ID | 主键 | GUID | Y | Y |
| 4 | NOTE_TYPE_ID | 票据类型 | GUID | Y |  |
| 5 | NOTE_NO | 票号 | string(40) | Y |  |
| 6 | ISSUE_DATE | 收票日期 | date | Y |  |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | DUE_DATE | 票面到期日 | date | Y |  |
| 9 | EXPECT_CASHING_DATE | 预计兑现日 | date | Y |  |
| 10 | NOTE_STATUS | 票据状态 | number | Y |  |
| 11 | GUARANTEED_NOTE_FLAG | 保证票标志 | number(0/1) | Y |  |
| 12 | CUSTOMER_NOTE_FLAG | 客票标志 | number(0/1) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CURRENCY_ID | 货币 | GUID | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | AMT_TC | 票面金额（原币） | number(23,8) | Y |  |
| 17 | AMT_FC | 票面金额（本币） | number(23,8) | Y |  |
| 18 | SETTLEMENT_OBJECT_TYPE | 开票人类型 | number | Y |  |
| 19 | VERIFICATION_FLAG | 需被应收/应付系统核销标识 | number(0/1) | Y |  |
| 20 | RESPONSIBILITY_ORG_TYPE | 责任域类型 | number | Y |  |
| 21 | COLLECTION_BANK_ACCOUNT_ID | 托收银行账号 | GUID | Y |  |
| 22 | CHARGE_AMT_TC | 手续费(原币) | number(23,8) | Y |  |
| 23 | CHARGE_EXPENSE_ID | 手续费项目 | GUID | Y |  |
| 24 | GLOB_ACCOUNT_CODE_ID | 应收票据科目-运营 | GUID | Y |  |
| 25 | GLMB_ACCOUNT_CODE_ID | 应收票据科目-管理 | GUID | Y |  |
| 26 | ACCOUNT_CODE | 银行账号 | string(60) | Y |  |
| 27 | FIN_INSTITUTION_ID | 金融机构 | GUID | Y |  |
| 28 | VERIFIED_AMT_TC | 已核销金额（原币） | number(23,8) | Y |  |
| 29 | VERIFIED_AMT_FC | 已核销金额（本币） | number(23,8) | Y |  |
| 30 | UNVERIFIED_AMT_TC | 未核销金额（原币） | number(23,8) | Y |  |
| 31 | UNVERIFIED_AMT_FC | 未核销金额（本币） | number(23,8) | Y |  |
| 32 | RESPONSIBILITY_ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 33 | RESPONSIBILITY_EMPLOYEE_ID | 责任人员 | GUID | Y |  |
| 34 | SETTLEMENT_FULL_NAME | 开票人全称 | string(144) | Y |  |
| 35 | TWNM_ITEM_ID | 收款项目 | GUID | Y |  |
| 36 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 37 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 38 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 39 | SOURCE_ARAP_FLAG | 来源应收应付系统标识 | number(0/1) | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 50 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 51 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 52 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 53 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 54 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 55 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 56 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 57 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 58 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 59 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 60 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 61 | UDF041 | 自定义字段12 | date | Y |  |
| 62 | UDF042 | 自定义字段13 | date | Y |  |
| 63 | UDF051 | 自定义字段14 | GUID | Y |  |
| 64 | UDF052 | 自定义字段15 | GUID | Y |  |
| 65 | UDF053 | 自定义字段16 | GUID | Y |  |
| 66 | UDF054 | 自定义字段17 | GUID | Y |  |
| 67 | PrintCount | 打印次数 | number | Y |  |
| 68 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 69 | ApproveDate | 修改日期 | date | Y |  |
| 70 | ApproveBy | 修改人 | GUID | Y |  |
| 71 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 72 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 73 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 74 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |
| 77 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 78 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 79 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 80 | SOURCE_ID_ROid |  | GUID | Y |  |

### TWNM_NR_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | VERIFIED_AMT_TC | 核销金额（原币） | number(23,8) | Y |  |
| 3 | VERIFIED_AMT_FC | 核销金额（本币） | number(23,8) | Y |  |
| 4 | TWNM_NR_D_ID | 主键 | GUID | Y | Y |
| 5 | TRANS_DOC_TYPE | 业务单据类型 | number | Y |  |
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
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 36 | SOURCE_ID_ROid |  | GUID | Y |  |
| 37 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 39 | TWNM_NR_ID |  | GUID | Y |  |

### TWNM_REPAYMENT_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | TWNM_REPAYMENT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | CURRENCY_ID | 还款货币 | GUID | Y |  |
| 12 | EXCHANGE_RATE | 还款汇率 | number(18,9) | Y |  |
| 13 | INTEREST_EXPENSE_ID | 利息项目 | GUID | Y |  |
| 14 | MULTI_CURRENCY_FLAG | 异货币核销标识 | number(0/1) | Y |  |
| 15 | PRINCIPAL_AMT_TC | 本金合计(原币) | number(23,8) | Y |  |
| 16 | PRINCIPAL_AMT_FC | 本金合计(本币) | number(23,8) | Y |  |
| 17 | INTEREST_AMT_TC | 利息合计(原币) | number(23,8) | Y |  |
| 18 | INTEREST_AMT_FC | 利息合计(本币) | number(23,8) | Y |  |
| 19 | LOAN_AMT_TC | 借款合计(原币) | number(23,8) | Y |  |
| 20 | LOAN_AMT_FC | 借款合计(本币) | number(23,8) | Y |  |
| 21 | V_LOAN_AMT_TC | 核销借款合计(原币) | number(23,8) | Y |  |
| 22 | V_LOAN_AMT_FC | 核销借款合计(本币) | number(23,8) | Y |  |
| 23 | V_INTEREST_AMT_TC | 核销利息合计(原币) | number(23,8) | Y |  |
| 24 | V_INTEREST_AMT_FC | 核销利息合计(本币) | number(23,8) | Y |  |
| 25 | EXCHANGE_LOSS_AMT | 汇兑损失合计 | number(23,8) | Y |  |
| 26 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 27 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 28 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 29 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | PrintCount | 打印次数 | number | Y |  |
| 32 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 33 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 34 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 35 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | Owner_Org_RTK |  | string(400) | Y |  |
| 67 | Owner_Org_ROid |  | GUID | Y |  |

### TWNM_REPAYMENT_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_REPAYMENT_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 4 | CURRENCY_ID | 货币 | GUID | Y |  |
| 5 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 6 | PRINCIPAL_AMT_TC | 本金(原币) | number(23,8) | Y |  |
| 7 | PRINCIPAL_AMT_FC | 本金(本币) | number(23,8) | Y |  |
| 8 | INTEREST_AMT_TC | 利息(原币) | number(23,8) | Y |  |
| 9 | INTEREST_AMT_FC | 利息(本币) | number(23,8) | Y |  |
| 10 | AMT_TC | 合计(原币) | number(23,8) | Y |  |
| 11 | AMT_FC | 合计(本币) | number(23,8) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
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
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | TWNM_REPAYMENT_DOC_ID |  | GUID | Y |  |

### TWNM_REPAYMENT_DOC_LVD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | TWNM_REPAYMENT_DOC_LVD_ID | 主键 | GUID | Y | Y |
| 3 | CURRENCY_ID | 货币 | GUID | Y |  |
| 4 | HIS_EXCHANGE_RATE | 历史汇率 | number(18,9) | Y |  |
| 5 | BALANCE_AMT_TC | 借款余额(原币) | number(23,8) | Y |  |
| 6 | BALANCE_AMT_FC | 借款余额(本币) | number(23,8) | Y |  |
| 7 | CURR_EXCHANGE_RATE | 现行汇率 | number(18,9) | Y |  |
| 8 | VERIFICATION_AMT_TC | 核销金额(原币) | number(23,8) | Y |  |
| 9 | VERIFICATION_AMT_FC | 核销金额(本币) | number(23,8) | Y |  |
| 10 | VERIFICATION_HEXG_AMT_FC | 历史本币核销金额 | number(23,8) | Y |  |
| 11 | EXCHANGE_LOSS_AMT |  | number(23,8) | Y |  |
| 12 | INTEREST_AMT_TC | 利息(原币) | number(23,8) | Y |  |
| 13 | INTEREST_AMT_FC | 利息(本币) | number(23,8) | Y |  |
| 14 | LIMIT_FLAG | 信用额度控制标识 | number(0/1) | Y |  |
| 15 | CREDIT_CURRENCY_ID | 信用货币 | GUID | Y |  |
| 16 | LIMIT_USED_AMT | 占用额度 | number(23,8) | Y |  |
| 17 | RELEASE_LIMIT_AMT | 释放额度 | number(23,8) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | TWNM_LOAN_DOC_ID | 借款单 | GUID | Y |  |
| 20 | TWNM_FINANCING_BN_ID | 融资批号 | GUID | Y |  |
| 21 | CreateDate | 创建日期 | date | Y |  |
| 22 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 23 | ModifiedDate | 修改日期 | date | Y |  |
| 24 | CreateBy | 创建者 | GUID | Y |  |
| 25 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 26 | ModifiedBy | 修改者 | GUID | Y |  |
| 27 | Version | 版本号，不要随意更改 | binary | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | TWNM_REPAYMENT_DOC_ID |  | GUID | Y |  |