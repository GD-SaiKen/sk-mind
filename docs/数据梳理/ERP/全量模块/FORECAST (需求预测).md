---
module: "FORECAST"
name_zh: "需求预测"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 278
category: manufacturing
tags: ["ERP", "E10", "manufacturing"]
created: 2026-06-25 10:52
---

# FORECAST (需求预测)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 278

## Related Modules

- [[APS (高级排程计划)|APS (高级排程计划)]]
- [[BOM (物料清单)|BOM (物料清单)]]
- [[CHANGE (变更执行)|CHANGE (变更执行)]]
- [[ECN (工程变更)|ECN (工程变更)]]
- [[MO (制造工单)|MO (制造工单)]]
- [[OUT (委外加工)|OUT (委外加工)]]
- [[PLAN (计划管理)|PLAN (计划管理)]]
- [[PRE (预置数据)|PRE (预置数据)]]

---

## Tables


- **FORECAST_D**
- **FORECAST_D_V**
- **FORECAST_SD**


---


---


> Tables: 4

### FORECAST (生产预测信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | FORECAST_ID | 主键 | GUID | Y | Y |
| 4 | FORECAST_DATE | 预测日期 | date | Y |  |
| 5 | FORECAST_METHOD | 预测方式 | string(40) | Y |  |
| 6 | START_DATE | 预测起始日期 | date | Y |  |
| 7 | END_DATE | 预测结束日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | BUCKET_SECTION_STRING | 时距区间字串 | string(8000) | Y |  |
| 10 | TIME_BUCKET_ID | 时距 | GUID | Y |  |
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
| 29 | PrintCount | 打印次数 | number | Y |  |
| 30 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 31 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 32 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 33 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### FORECAST_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | START_DATE | 起始日期 | date | Y |  |
| 2 | END_DATE | 结束日期 | date | Y |  |
| 3 | FORECAST_QTY | 预测数量 | number(16,6) | Y |  |
| 4 | FORECAST_D_ID | 主键 | GUID | Y | Y |
| 5 | FORECAST_D_V_ID | 横排OID | GUID | Y |  |
| 6 | COLUMN_NO | 列序号 | string(20) | Y |  |
| 7 | DEMAND_DATE | 需求日期 | date | Y |  |
| 8 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 9 | ITEM_ID | 品号 | GUID | Y |  |
| 10 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 11 | UNIT_ID | 主键 | GUID | Y |  |
| 12 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
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
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | FORECAST_ID |  | GUID | Y |  |

### FORECAST_D_V

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FORECAST_D_V_ID | 主键 | GUID | Y | Y |
| 3 | COLUMN01 | 列1 | number(16,6) | Y |  |
| 4 | COLUMN02 | 列2 | number(16,6) | Y |  |
| 5 | COLUMN03 | 列3 | number(16,6) | Y |  |
| 6 | COLUMN04 | 列4 | number(16,6) | Y |  |
| 7 | COLUMN05 | 列5 | number(16,6) | Y |  |
| 8 | COLUMN06 | 列6 | number(16,6) | Y |  |
| 9 | COLUMN07 | 列7 | number(16,6) | Y |  |
| 10 | COLUMN08 | 列8 | number(16,6) | Y |  |
| 11 | COLUMN09 | 列9 | number(16,6) | Y |  |
| 12 | COLUMN10 | 列10 | number(16,6) | Y |  |
| 13 | COLUMN11 | 列11 | number(16,6) | Y |  |
| 14 | COLUMN12 | 列12 | number(16,6) | Y |  |
| 15 | COLUMN13 | 列13 | number(16,6) | Y |  |
| 16 | COLUMN14 | 列14 | number(16,6) | Y |  |
| 17 | COLUMN15 | 列15 | number(16,6) | Y |  |
| 18 | COLUMN16 | 列16 | number(16,6) | Y |  |
| 19 | COLUMN17 | 列17 | number(16,6) | Y |  |
| 20 | COLUMN18 | 列18 | number(16,6) | Y |  |
| 21 | COLUMN19 | 列19 | number(16,6) | Y |  |
| 22 | COLUMN20 | 列20 | number(16,6) | Y |  |
| 23 | COLUMN21 | 列21 | number(16,6) | Y |  |
| 24 | COLUMN22 | 列22 | number(16,6) | Y |  |
| 25 | COLUMN23 | 列23 | number(16,6) | Y |  |
| 26 | COLUMN24 | 列24 | number(16,6) | Y |  |
| 27 | COLUMN25 | 列25 | number(16,6) | Y |  |
| 28 | COLUMN26 | 列26 | number(16,6) | Y |  |
| 29 | COLUMN27 | 列27 | number(16,6) | Y |  |
| 30 | COLUMN28 | 列28 | number(16,6) | Y |  |
| 31 | COLUMN29 | 列29 | number(16,6) | Y |  |
| 32 | COLUMN30 | 列30 | number(16,6) | Y |  |
| 33 | COLUMN31 | 列31 | number(16,6) | Y |  |
| 34 | COLUMN32 | 列32 | number(16,6) | Y |  |
| 35 | COLUMN33 | 列33 | number(16,6) | Y |  |
| 36 | COLUMN34 | 列34 | number(16,6) | Y |  |
| 37 | COLUMN35 | 列35 | number(16,6) | Y |  |
| 38 | COLUMN36 | 列36 | number(16,6) | Y |  |
| 39 | COLUMN37 | 列37 | number(16,6) | Y |  |
| 40 | COLUMN38 | 列38 | number(16,6) | Y |  |
| 41 | COLUMN39 | 列39 | number(16,6) | Y |  |
| 42 | COLUMN40 | 列40 | number(16,6) | Y |  |
| 43 | COLUMN41 | 列41 | number(16,6) | Y |  |
| 44 | COLUMN42 | 列42 | number(16,6) | Y |  |
| 45 | COLUMN43 | 列43 | number(16,6) | Y |  |
| 46 | COLUMN44 | 列44 | number(16,6) | Y |  |
| 47 | COLUMN45 | 列45 | number(16,6) | Y |  |
| 48 | COLUMN46 | 列46 | number(16,6) | Y |  |
| 49 | COLUMN47 | 列47 | number(16,6) | Y |  |
| 50 | COLUMN48 | 列48 | number(16,6) | Y |  |
| 51 | COLUMN49 | 列49 | number(16,6) | Y |  |
| 52 | COLUMN50 | 列50 | number(16,6) | Y |  |
| 53 | COLUMN51 | 列51 | number(16,6) | Y |  |
| 54 | COLUMN52 | 列52 | number(16,6) | Y |  |
| 55 | COLUMN53 | 列53 | number(16,6) | Y |  |
| 56 | COLUMN54 | 列54 | number(16,6) | Y |  |
| 57 | COLUMN55 | 列55 | number(16,6) | Y |  |
| 58 | COLUMN56 | 列56 | number(16,6) | Y |  |
| 59 | COLUMN57 | 列57 | number(16,6) | Y |  |
| 60 | COLUMN58 | 列58 | number(16,6) | Y |  |
| 61 | COLUMN59 | 列59 | number(16,6) | Y |  |
| 62 | COLUMN60 | 列60 | number(16,6) | Y |  |
| 63 | ITEM_ID | 品号 | GUID | Y |  |
| 64 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 65 | UNIT_ID | 主键 | GUID | Y |  |
| 66 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
| 67 | COLUMN61 | 列61 | number(16,6) | Y |  |
| 68 | COLUMN62 | 列62 | number(16,6) | Y |  |
| 69 | COLUMN63 | 列63 | number(16,6) | Y |  |
| 70 | COLUMN64 | 列64 | number(16,6) | Y |  |
| 71 | COLUMN65 | 列65 | number(16,6) | Y |  |
| 72 | COLUMN66 | 列66 | number(16,6) | Y |  |
| 73 | COLUMN67 | 列67 | number(16,6) | Y |  |
| 74 | COLUMN68 | 列68 | number(16,6) | Y |  |
| 75 | COLUMN69 | 列69 | number(16,6) | Y |  |
| 76 | COLUMN70 | 列70 | number(16,6) | Y |  |
| 77 | COLUMN71 | 列71 | number(16,6) | Y |  |
| 78 | COLUMN72 | 列72 | number(16,6) | Y |  |
| 79 | COLUMN73 | 列73 | number(16,6) | Y |  |
| 80 | COLUMN74 | 列74 | number(16,6) | Y |  |
| 81 | COLUMN75 | 列75 | number(16,6) | Y |  |
| 82 | COLUMN76 | 列76 | number(16,6) | Y |  |
| 83 | COLUMN77 | 列77 | number(16,6) | Y |  |
| 84 | COLUMN78 | 列78 | number(16,6) | Y |  |
| 85 | COLUMN79 | 列79 | number(16,6) | Y |  |
| 86 | COLUMN80 | 列80 | number(16,6) | Y |  |
| 87 | COLUMN81 | 列81 | number(16,6) | Y |  |
| 88 | COLUMN82 | 列82 | number(16,6) | Y |  |
| 89 | COLUMN83 | 列83 | number(16,6) | Y |  |
| 90 | COLUMN84 | 列84 | number(16,6) | Y |  |
| 91 | COLUMN85 | 列85 | number(16,6) | Y |  |
| 92 | COLUMN86 | 列86 | number(16,6) | Y |  |
| 93 | COLUMN87 | 列87 | number(16,6) | Y |  |
| 94 | COLUMN88 | 列88 | number(16,6) | Y |  |
| 95 | COLUMN89 | 列89 | number(16,6) | Y |  |
| 96 | COLUMN90 | 列90 | number(16,6) | Y |  |
| 97 | COLUMN91 | 列91 | number(16,6) | Y |  |
| 98 | COLUMN92 | 列92 | number(16,6) | Y |  |
| 99 | COLUMN93 | 列93 | number(16,6) | Y |  |
| 100 | COLUMN94 | 列94 | number(16,6) | Y |  |
| 101 | COLUMN95 | 列95 | number(16,6) | Y |  |
| 102 | COLUMN96 | 列96 | number(16,6) | Y |  |
| 103 | COLUMN97 | 列97 | number(16,6) | Y |  |
| 104 | COLUMN98 | 列98 | number(16,6) | Y |  |
| 105 | COLUMN99 | 列99 | number(16,6) | Y |  |
| 106 | COLUMN100 | 列100 | number(16,6) | Y |  |
| 107 | COLUMN101 | 列101 | number(16,6) | Y |  |
| 108 | COLUMN102 | 列102 | number(16,6) | Y |  |
| 109 | COLUMN103 | 列103 | number(16,6) | Y |  |
| 110 | COLUMN104 | 列104 | number(16,6) | Y |  |
| 111 | COLUMN105 | 列105 | number(16,6) | Y |  |
| 112 | COLUMN106 | 列106 | number(16,6) | Y |  |
| 113 | COLUMN107 | 列107 | number(16,6) | Y |  |
| 114 | COLUMN108 | 列108 | number(16,6) | Y |  |
| 115 | COLUMN109 | 列109 | number(16,6) | Y |  |
| 116 | COLUMN110 | 列110 | number(16,6) | Y |  |
| 117 | COLUMN111 | 列111 | number(16,6) | Y |  |
| 118 | COLUMN112 | 列112 | number(16,6) | Y |  |
| 119 | COLUMN113 | 列113 | number(16,6) | Y |  |
| 120 | COLUMN114 | 列114 | number(16,6) | Y |  |
| 121 | COLUMN115 | 列115 | number(16,6) | Y |  |
| 122 | COLUMN116 | 列116 | number(16,6) | Y |  |
| 123 | COLUMN117 | 列117 | number(16,6) | Y |  |
| 124 | COLUMN118 | 列118 | number(16,6) | Y |  |
| 125 | COLUMN119 | 列119 | number(16,6) | Y |  |
| 126 | COLUMN120 | 列120 | number(16,6) | Y |  |
| 127 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 128 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 129 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 130 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 131 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 132 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 133 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 134 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 135 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 136 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 137 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 138 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 139 | UDF041 | 自定义字段12 | date | Y |  |
| 140 | UDF042 | 自定义字段13 | date | Y |  |
| 141 | UDF051 | 自定义字段14 | GUID | Y |  |
| 142 | UDF052 | 自定义字段15 | GUID | Y |  |
| 143 | UDF053 | 自定义字段16 | GUID | Y |  |
| 144 | UDF054 | 自定义字段17 | GUID | Y |  |
| 145 | Version | 版本号，不要随意更改 | binary | Y |  |
| 146 | CreateDate | 创建日期 | date | Y |  |
| 147 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 148 | ModifiedDate | 修改日期 | date | Y |  |
| 149 | CreateBy | 创建者 | GUID | Y |  |
| 150 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 151 | ModifiedBy | 修改者 | GUID | Y |  |
| 152 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 153 | ApproveDate | 修改日期 | date | Y |  |
| 154 | ApproveBy | 修改人 | GUID | Y |  |
| 155 | FORECAST_ID |  | GUID | Y |  |

### FORECAST_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | FORECAST_SOURCE | 预测来源 | string(120) | Y |  |
| 3 | FORECAST_QTY | 预测数量 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | FORECAST_SD_ID | 主键 | GUID | Y | Y |
| 6 | COLUMN_NO | 列序号 | string(20) | Y |  |
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
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | FORECAST_D_V_ID |  | GUID | Y |  |