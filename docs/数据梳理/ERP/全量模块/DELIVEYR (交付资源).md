---
module: "DELIVEYR"
name_zh: "交付资源"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 103
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# DELIVEYR (交付资源)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 103

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


- **DELIVEYR_RESOURCE (配送资源信息)**
- **DELIVEYR_RESOURCE_D (配送资源储存信息)**


---


---


> Tables: 2

### DELIVEYR_RESOURCE (配送资源信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DELIVEYR_RESOURCE_ID | 主键 | GUID | Y | Y |
| 4 | DELIVEYR_RESOURCE_CODE | 车号 | string(20) | Y |  |
| 5 | DELIVEYR_RESOURCE_NAME | 车辆名称 | string(40) | Y |  |
| 6 | INFO_DELIVEYR_RESOURCE | 车辆描述 | string(510) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | ROUTE_ID | 主键 | GUID | Y |  |
| 9 | CAR_NO | 出车状态 | string(40) | Y |  |
| 10 | APPROVE_WEIGHT | 核定载重 | number(16,6) | Y |  |
| 11 | CARRY_WEIGHT | 承载重量 | number(16,6) | Y |  |
| 12 | CARRY_BULK | 承载体积 | number(16,6) | Y |  |
| 13 | CAR_LONG | 车厢长 | number(16,6) | Y |  |
| 14 | CAR_HIGH | 车厢高 | number(16,6) | Y |  |
| 15 | CAR_WIDE | 车厢宽 | number(16,6) | Y |  |
| 16 | CAR_IN_LONG | 车厢内长 | number(16,6) | Y |  |
| 17 | CAR_IN_HIGH | 车厢内高 | number(16,6) | Y |  |
| 18 | CAR_IN_WIDE | 车厢内宽 | number(16,6) | Y |  |
| 19 | MILEAGE | 初始里程数 | number(16,6) | Y |  |
| 20 | FACTURE | 制造商 | string(80) | Y |  |
| 21 | OPERATING_NO | 营运证号 | string(80) | Y |  |
| 22 | TIRE_NO | 轮胎数 | number | Y |  |
| 23 | CHASSIS_NO | 底盘号 | string(80) | Y |  |
| 24 | FRAME_NO | 车架号 | string(80) | Y |  |
| 25 | ENGINE_NO | 发动机号 | string(80) | Y |  |
| 26 | SAFE_NO | 保险号 | string(80) | Y |  |
| 27 | MODEL_NO | 品牌/型号 | string(80) | Y |  |
| 28 | RURCHASE_NO | 购置证号 | string(80) | Y |  |
| 29 | FUEL_LODE | 载重耗油(升/公里) | number(16,6) | Y |  |
| 30 | FUEL_EMPTY | 空车耗油(升/公里) | number(16,6) | Y |  |
| 31 | DRIVING_LICENSE_NO | 行驶证号 | string(80) | Y |  |
| 32 | INPUT_DATE | 建档日期 | date | Y |  |
| 33 | BUY_DATE | 购买日期 | date | Y |  |
| 34 | CARD_NO | 上牌日期 | date | Y |  |
| 35 | POWER | 马力 | number(16,6) | Y |  |
| 36 | BEAR_NO | 轴数 | number | Y |  |
| 37 | PILOT | 驾驶员 | GUID | Y |  |
| 38 | PILOT_TELPHONE | 驾驶员手机号码 | string(80) | Y |  |
| 39 | LICENSE | 驾驶证号 | string(80) | Y |  |
| 40 | COPILOT | 副驾驶员 | GUID | Y |  |
| 41 | LICENSE_F | 副驾驶证号 | string(80) | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | Attachments | 附件 | string | Y |  |
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
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 69 | ApproveDate | 修改日期 | date | Y |  |
| 70 | ApproveBy | 修改人 | GUID | Y |  |
| 71 | Version | 版本号，不要随意更改 | binary | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |

### DELIVEYR_RESOURCE_D (配送资源储存信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DELIVEYR_RESOURCE_D_ID | 主键 | GUID | Y | Y |
| 3 | STORAGE_LIMIT_ID | 储存限制编号 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | DELIVEYR_RESOURCE_ID |  | GUID | Y |  |