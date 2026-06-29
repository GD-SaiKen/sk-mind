---
module: "GL"
name_zh: "总账"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 44
category: financial
semantic_object: "GeneralLedger/总账"
original_tables: 4
filtered_out: 0
tags: ["ERP", "E10", "financial", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# GL (总账) - GeneralLedger/总账

> [!info] Phase 1 Core Module
> Semantic Object: GeneralLedger/总账
> Kept: 4 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 0

## Related Modules

- [[../modules/AR (应收账款).md|AR (应收账款)]]
- [[../modules/AP (应付账款).md|AP (应付账款)]]
- [[../modules/ACCOUNT (会计科目).md|ACCOUNT (会计科目)]]
- [[../modules/JOURNAL (日记账).md|JOURNAL (日记账)]]

---

## Tables

- **GL_B007 (GL_B007)**
- **GL_B008 (GL_B008)**
- **GL_B009 (GL_B009)**
- **GL_B010 (GL_B010)**

---

## Table Details

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
