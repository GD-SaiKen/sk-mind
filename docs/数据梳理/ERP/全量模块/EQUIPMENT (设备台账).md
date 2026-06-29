---
module: "EQUIPMENT"
name_zh: "设备台账"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 159
category: asset
tags: ["ERP", "E10", "asset"]
created: 2026-06-25 10:52
---

# EQUIPMENT (设备台账)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 159

## Related Modules

- [[ASSET (固定资产)|ASSET (固定资产)]]
- [[EQT (设备管理)|EQT (设备管理)]]
- [[MAINTAIN (设备维护)|MAINTAIN (设备维护)]]

---

## Tables


- **EQUIPMENT_D**
- **EQUIPMENT_PLAN**


---


---


> Tables: 3

### EQUIPMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | EQUIPMENT_ID | 主键 | GUID | Y | Y |
| 4 | EQUIPMENT_CODE | 设备编号 | string(80) | Y |  |
| 5 | EQUIPMENT_NAME | 设备名称 | string(160) | Y |  |
| 6 | EQT_CATEGORY_ID | 设备类别 | GUID | Y |  |
| 7 | EQT_SPEC | 规格 | string(120) | Y |  |
| 8 | EQT_STATUS_ID | 设备状态 | GUID | Y |  |
| 9 | ASSET_ID | 固定资产编号 | GUID | Y |  |
| 10 | MADE_CODE | 出厂编号 | string(80) | Y |  |
| 11 | EQT_MODEL_ID | 设备型号 | GUID | Y |  |
| 12 | WARRAATY | 保修期 | date | Y |  |
| 13 | MANUFACTURER | 制造商 | string(160) | Y |  |
| 14 | USEFUL_LIFE | 使用年限 | number(11,1) | Y |  |
| 15 | MANUFACTURE_DATE | 出厂日期 | date | Y |  |
| 16 | USE_DATE | 投产日期 | date | Y |  |
| 17 | ABC_CATEGORY | ABC类别 | string(2) | Y |  |
| 18 | LOCATION | 使用地点 | string(120) | Y |  |
| 19 | FAILURE_DAY | 最近故障日期 | date | Y |  |
| 20 | TOT_FAILURE_TIMES | 累计故障停机时数 | number(16,6) | Y |  |
| 21 | STANDARD_OPERATING_QTY | 每日标准运行量 | number(16,6) | Y |  |
| 22 | OPERATING_QTY_UNIT_ID | 运行量单位 | GUID | Y |  |
| 23 | TOT_OPERATING_QTY | 累计运行量 | number(16,6) | Y |  |
| 24 | LATEST_DUE_DATE | 最近记录截止日期 | date | Y |  |
| 25 | IS_INSTALL | 启用放置地点 | number(0/1) | Y |  |
| 26 | SETUP_LOCATION | 放置地点描述 | string(120) | Y |  |
| 27 | SETUP_TIME | 安装完工时间 | date | Y |  |
| 28 | HANDOVER_DATE | 交接日期 | date | Y |  |
| 29 | SETUP_EMPLOYEE_ID | 安装负责人 | GUID | Y |  |
| 30 | SETUP_DES | 安装情况说明 | string(510) | Y |  |
| 31 | DEBUG_DES | 调试情况说明 | string(510) | Y |  |
| 32 | ATTACH_COUNTING_DESCRIP | 附件工具清点情况 | string(510) | Y |  |
| 33 | ACCEPT_EMPLOYEE_ID | 验收人员 | GUID | Y |  |
| 34 | ACCEPT_UNIT_EMPLOYEE_ID | 安装单位负责人 | GUID | Y |  |
| 35 | REMARK | 备注 | string(510) | Y |  |
| 36 | INSP_EMPLOYEE_ID | 维修负责人 | GUID | Y |  |
| 37 | INSP_ADMIN_UNIT_ID | 维修负责部门 | GUID | Y |  |
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 63 | Attachments | 附件 | string | Y |  |
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 66 | ApproveDate | 修改日期 | date | Y |  |
| 67 | ApproveBy | 修改人 | GUID | Y |  |
| 68 | Owner_Org_RTK |  | string(400) | Y |  |
| 69 | Owner_Org_ROid |  | GUID | Y |  |
| 70 | MACHINE_ID_RTK |  | string(400) | Y |  |
| 71 | MACHINE_ID_ROid |  | GUID | Y |  |
| 72 | SOURCE_LOC_ID_RTK |  | string(400) | Y |  |
| 73 | SOURCE_LOC_ID_ROid |  | GUID | Y |  |

### EQUIPMENT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQUIPMENT_D_ID | 主键 | GUID | Y | Y |
| 3 | FEATURE_NAME | 属性名称 | string(160) | Y |  |
| 4 | FEATURE_VALUE | 属性值 | string(40) | Y |  |
| 5 | PRINT_EQT_CARD | 列印到设备卡 | number(0/1) | Y |  |
| 6 | MUST_INPUT | 必须输入 | number(0/1) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | UNIT_ID | 单位 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | EQUIPMENT_ID |  | GUID | Y |  |

### EQUIPMENT_PLAN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | EQUIPMENT_PLAN_ID | 主键 | GUID | Y | Y |
| 3 | PLAN_ID | 维护方案 | GUID | Y |  |
| 4 | SHUTDOWN | 停机 | number(0/1) | Y |  |
| 5 | REFER_WORK_HOURS | 参考作业时数 | number(16,6) | Y |  |
| 6 | REFER_SHUTDOWN_HOURS | 参考停机时数 | number(16,6) | Y |  |
| 7 | EQT_PERIOD_ID | 周期 | GUID | Y |  |
| 8 | CYCLE_QTY | 周期次数 | string(8) | Y |  |
| 9 | TOT_OPERATING_QTY | 本次累计运行量 | number(16,6) | Y |  |
| 10 | EXECUTION_DATETIME | 执行时间 | date | Y |  |
| 11 | NEXT_MAINTAIN_DATETIME | 下次维护时间 | date | Y |  |
| 12 | NEXT_OPERATING_QTY | 下次维护运行量 | number(16,6) | Y |  |
| 13 | SUPER_ZERO | 允许被更高级别方案归零 | number(0/1) | Y |  |
| 14 | MAINTAIN_DOC_D_ID | 归零单据 | GUID | Y |  |
| 15 | EMPLOYEE_ID | 负责人 | GUID | Y |  |
| 16 | ORIGINAL_EXE_DATETIME | 原执行时间 | date | Y |  |
| 17 | ORG_TOT_QTY | 原本次累计运行量 | number(16,6) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE_ID_ROid |  | GUID | Y |  |
| 49 | EQUIPMENT_ID |  | GUID | Y |  |