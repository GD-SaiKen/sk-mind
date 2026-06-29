---
module: "GL"
name_zh: "总账"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 44
category: financial
tags: ["ERP", "E10", "financial"]
created: 2026-06-25 10:52

---

# GL (总账)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 4 | Columns: 44

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

## Tables


- **GL_B007 (GL_B007)**
- **GL_B008 (GL_B008)**
- **GL_B009 (GL_B009)**
- **GL_B010 (GL_B010)**


---


---


> Tables: 4

### GL_B007 (GL_B007)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | GL_B007_ID | 主键 | GUID | Y | Y |
| 2 | GL_B007_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### GL_B008 (GL_B008)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | GL_B008_ID | 主键 | GUID | Y | Y |
| 2 | GL_B008_NAME | SDFDFS | string(400) | Y |  |
| 3 | Version | 版本号，不要随意更改 | binary | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### GL_B009 (GL_B009)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | GL_B009_ID | 主键 | GUID | Y | Y |
| 2 | GL_B009_NAME | SDFDFS | string(400) | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
| 9 | Attachments | 附件 | string | Y |  |
| 10 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |

### GL_B010 (GL_B010)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | GL_B010_ID | 主键 | GUID | Y | Y |
| 2 | GL_B010_NAME | SDFDFS | string(400) | Y |  |
| 3 | CreateDate | 创建日期 | date | Y |  |
| 4 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 5 | ModifiedDate | 修改日期 | date | Y |  |
| 6 | CreateBy | 创建者 | GUID | Y |  |
| 7 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 8 | ModifiedBy | 修改者 | GUID | Y |  |
| 9 | Attachments | 附件 | string | Y |  |
| 10 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |