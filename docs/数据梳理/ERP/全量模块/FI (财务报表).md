---
module: "FI"
name_zh: "财务报表"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 3
columns: 64
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# FI (财务报表)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 3 | Columns: 64

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


- **FI_TPTRPT (财务第三方工具报表)**
- **FI_TPTRPT_BAK (财务第三方工具报表备份档)**
- **FI_TPTRPT_CATEGORY (财务第三方工具报表分类)**


---


---


> Tables: 3

### FI_TPTRPT (财务第三方工具报表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | FI_TPTRPT_ID | 主键 | GUID | Y | Y |
| 4 | RPT_NAME | 报表名称 | string(510) | Y |  |
| 5 | FI_TPTRPT_CATEGORY_ID | 报表分类 | GUID | Y |  |
| 6 | SYS_FLAG | 系统标识 | number(0/1) | Y |  |
| 7 | RPT_DATA_ID | 报表数据 | GUID | Y |  |
| 8 | FILE_EXTENSION | 文件扩展名 | string(40) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
| 18 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 19 | ApproveDate | 修改日期 | date | Y |  |
| 20 | ApproveBy | 修改人 | GUID | Y |  |
| 21 | Owner_Org_RTK |  | string(400) | Y |  |
| 22 | Owner_Org_ROid |  | GUID | Y |  |

### FI_TPTRPT_BAK (财务第三方工具报表备份档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | FI_TPTRPT_BAK_ID | 主键 | GUID | Y | Y |
| 4 | FI_TPTRPT_ID | 报表ID | GUID | Y |  |
| 5 | RPT_NAME | 报表名称 | string(510) | Y |  |
| 6 | SYS_FLAG | 系统标识 | number(0/1) | Y |  |
| 7 | RPT_DATA_ID | 报表数据 | GUID | Y |  |
| 8 | FILE_EXTENSION | 文件扩展名 | string(40) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
| 18 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 19 | ApproveDate | 修改日期 | date | Y |  |
| 20 | ApproveBy | 修改人 | GUID | Y |  |
| 21 | Owner_Org_RTK |  | string(400) | Y |  |
| 22 | Owner_Org_ROid |  | GUID | Y |  |

### FI_TPTRPT_CATEGORY (财务第三方工具报表分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | FI_TPTRPT_CATEGORY_ID | 主键 | GUID | Y | Y |
| 5 | CATEGORY_NAME | 分类名称 | string(510) | Y |  |
| 6 | FATHER_CATEGORY_ID | 父分类 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
| 14 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
| 16 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 17 | ApproveDate | 修改日期 | date | Y |  |
| 18 | ApproveBy | 修改人 | GUID | Y |  |
| 19 | Owner_Org_RTK |  | string(400) | Y |  |
| 20 | Owner_Org_ROid |  | GUID | Y |  |