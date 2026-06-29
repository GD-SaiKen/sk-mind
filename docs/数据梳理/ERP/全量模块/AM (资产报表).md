---
module: "AM"
name_zh: "资产报表"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 22
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# AM (资产报表)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 22

## Related Modules

- [[ABTABAC (表格映射)|ABTABAC (表格映射)]]
- [[ABTABVC (表格方案)|ABTABVC (表格方案)]]
- [[ACCCODE (科目数据集)|ACCCODE (科目数据集)]]
- [[ACCESS (权限控制)|ACCESS (权限控制)]]
- [[ACCPERIOD (会计期间)|ACCPERIOD (会计期间)]]
- [[ALTER (变更)|ALTER (变更)]]
- [[AU (辅助特性)|AU (辅助特性)]]
- [[AVOUCHER (自动凭证)|AVOUCHER (自动凭证)]]

---

## Tables


- **AM_B004 (AM_B004)**
- **AM_B005 (AM_B005)**


---


---


> Tables: 2

### AM_B004 (AM_B004)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AM_B004_ID | 主键 | GUID | Y | Y |
| 2 | AM_B004_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### AM_B005 (AM_B005)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AM_B005_ID | 主键 | GUID | Y | Y |
| 2 | AM_B005_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |