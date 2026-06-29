---
module: "MCLOUD"
name_zh: "云消息"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 41
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# MCLOUD (云消息)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 41

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


- **MCLOUD_MESSAGE (MCLOUD消息)**
- **MCLOUD_MESSAGE_D (MCLOUD消息单身)**
- **MCLOUD_MESSAGE_SD (MCLOUD消息子单身)**


---


---


> Tables: 3

### MCLOUD_MESSAGE (MCLOUD消息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MCLOUD_MESSAGE_ID | 主键 | GUID | Y | Y |
| 2 | MCLOUD_USER_ID | MCLOUD用户ID | string(80) | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
| 9 | Attachments | 附件 | string | Y |  |
| 10 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |

### MCLOUD_MESSAGE_D (MCLOUD消息单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MCLOUD_MESSAGE_D_ID | 主键 | GUID | Y | Y |
| 2 | REPORT_TYPE | 报表类型 | number | Y |  |
| 3 | REPORT_TYPEKEY | 报表Typekey | string(400) | Y |  |
| 4 | REQUEST_TYPE | 请求类型 | string(40) | Y |  |
| 5 | SEQUENCE | 自定义排序序号 | number | Y |  |
| 6 | CUSTOM_NAME | 自定义名称 | string(400) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |
| 14 | MCLOUD_MESSAGE_ID |  | GUID | Y |  |

### MCLOUD_MESSAGE_SD (MCLOUD消息子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MCLOUD_MESSAGE_SD_ID | 主键 | GUID | Y | Y |
| 2 | DISPLAY_NAME | 显示名称 | string(400) | Y |  |
| 3 | STATE | 已读状态 | number | Y |  |
| 4 | RECEIVED_TIME | 收件时间 | date | Y |  |
| 5 | SNAPSHOT_ID | 报表快照ID | string(400) | Y |  |
| 6 | PROCESS_STATUS | 处理状态 | string(40) | Y |  |
| 7 | PROCESS_MESSAGE | 处理结果消息 | string(400) | Y |  |
| 8 | CONDITION_DESCRIPTION | 条件描述 | string(1000) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
| 16 | MCLOUD_MESSAGE_D_ID |  | GUID | Y |  |