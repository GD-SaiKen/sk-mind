---
module: "SEND"
name_zh: "收发管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 115
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# SEND (收发管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 115

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


- **SEND_RECEIVE_DOC (收发件单)**
- **SEND_RECEIVE_DOC_D (收发件单单身档)**


---


---


> Tables: 2

### SEND_RECEIVE_DOC (收发件单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SEND_RECEIVE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | SEND_RECEIVE_DATE | 收发件日期 | date | Y |  |
| 8 | SEND_RECEIVE_TIME | 收发件时间 | time | Y |  |
| 9 | SR_TYPE | 收发件类型 | string(40) | Y |  |
| 10 | SR_MODE | 暂收\仓库 | string(40) | Y |  |
| 11 | SERVICE_SITE_ID | 站点 | GUID | Y |  |
| 12 | PLANT_ID | 工厂 | GUID | Y |  |
| 13 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 14 | RETURN_ITEM | 旧件返回 | number(0/1) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | COMPANY_ID | 公司 | GUID | Y |  |
| 17 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 18 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 19 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 20 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 21 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 22 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 23 | PrintCount | 打印次数 | number | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Attachments | 附件 | string | Y |  |
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | Owner_Org_RTK |  | string(400) | Y |  |
| 55 | Owner_Org_ROid |  | GUID | Y |  |

### SEND_RECEIVE_DOC_D (收发件单单身档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SEND_RECEIVE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 5 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 8 | SN | 序列号 | string(510) | Y |  |
| 9 | LEVEL_CODE | 层级码 | string(200) | Y |  |
| 10 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 11 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 12 | PRODUCT_ID | 成品识别码 | string(400) | Y |  |
| 13 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 14 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 15 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 16 | BIN_ID | 库位 | GUID | Y |  |
| 17 | RETURN | 需归还 | number(0/1) | Y |  |
| 18 | LOCATION | 暂收地点 | string(120) | Y |  |
| 19 | RECEIVE_DOC_ID | 冲销收件单号 | GUID | Y |  |
| 20 | UNIT_COST | 单位成本 | number(23,8) | Y |  |
| 21 | COST_AMT | 成本金额 | number(23,8) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | WRITE_OFF | 冲销否 | number(0/1) | Y |  |
| 24 | RECEIVE_QTY | 发件数量 | number(16,6) | Y |  |
| 25 | SERVICE_REQUEST_D_ID | 服务请求单 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 36 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 37 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 38 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 39 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 40 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 41 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 42 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 43 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 44 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 45 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 46 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 47 | UDF041 | 自定义字段12 | date | Y |  |
| 48 | UDF042 | 自定义字段13 | date | Y |  |
| 49 | UDF051 | 自定义字段14 | GUID | Y |  |
| 50 | UDF052 | 自定义字段15 | GUID | Y |  |
| 51 | UDF053 | 自定义字段16 | GUID | Y |  |
| 52 | UDF054 | 自定义字段17 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 55 | SOURCE_ID_ROid |  | GUID | Y |  |
| 56 | REFERENCE_ID_RTK |  | string(400) | Y |  |
| 57 | REFERENCE_ID_ROid |  | GUID | Y |  |
| 58 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 59 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |
| 60 | SEND_RECEIVE_DOC_ID |  | GUID | Y |  |