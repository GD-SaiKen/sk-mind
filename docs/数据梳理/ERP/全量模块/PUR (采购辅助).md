---
module: "PUR"
name_zh: "采购辅助"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 92
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# PUR (采购辅助)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 92

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


- **PUR_ARRIVAL_INSPECT_VER**
- **PUR_ARRIVAL_OFFSETDEP (到货单订金冲减明细)**


---


---


> Tables: 2

### PUR_ARRIVAL_INSPECT_VER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PUR_ARRIVAL_INSPECT_VER_ID | 主键 | GUID | Y | Y |
| 3 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 4 | VERIFICATION_INV_QTY | 本次核销库存单位数量 | number(16,6) | Y |  |
| 5 | QUALIFIED_INVENTORY_QTY | 合格库存单位数量 | number(16,6) | Y |  |
| 6 | UNQUALIFIED_INV_QTY | 不合格库存单位数量 | number(16,6) | Y |  |
| 7 | IN_DESTROYED_INV_QTY | 检验破坏库存单位数量 | number(16,6) | Y |  |
| 8 | ACCEPTED_INVENTORY_QTY | 允收库存单位数量 | number(16,6) | Y |  |
| 9 | RETURN_INVENTORY_QTY | 拒收库存单位数量 | number(16,6) | Y |  |
| 10 | SP_RECEIPT_INVENTORY_QTY | 特采库存单位数量 | number(16,6) | Y |  |
| 11 | SCRAP_INVENTORY_QTY | 报废库存单位数量 | number(16,6) | Y |  |
| 12 | RECEIPTED_INV_QTY | 已入库库存单位数量 | number(16,6) | Y |  |
| 13 | PURCHASE_ARRIVAL_D_ID | 到货单单身ID | GUID | Y |  |
| 14 | PURCHASE_ORDER_SSD_ID | 采购订单需求信息ID | GUID | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |

### PUR_ARRIVAL_OFFSETDEP (到货单订金冲减明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PUR_ARRIVAL_OFFSETDEP_ID | 主键 | GUID | Y | Y |
| 3 | PAYABLE_DOC_ID | 应付单号 | GUID | Y |  |
| 4 | PAYABLE_DOC_D_ID | 应付单序号 | GUID | Y |  |
| 5 | OFFSET_AMT_UN_TAX_OC | 冲减原币未税金额 | number(23,8) | Y |  |
| 6 | OFFSET_TAX_OC | 冲减原币税额 | number(23,8) | Y |  |
| 7 | OFFSET_TAX_BC | 冲减本币税额 | number(23,8) | Y |  |
| 8 | SETTLE_OFFSET_AMT_UN_TAX_OC | 已结算冲减原币未税金额 | number(23,8) | Y |  |
| 9 | SETTLE_OFFSET_TAX_OC | 已结算冲减原币税额 | number(23,8) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 13 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 14 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 15 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 16 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 17 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 18 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 19 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 20 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 21 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 22 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 23 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 24 | UDF041 | 自定义字段12 | date | Y |  |
| 25 | UDF042 | 自定义字段13 | date | Y |  |
| 26 | UDF051 | 自定义字段14 | GUID | Y |  |
| 27 | UDF052 | 自定义字段15 | GUID | Y |  |
| 28 | UDF053 | 自定义字段16 | GUID | Y |  |
| 29 | UDF054 | 自定义字段17 | GUID | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SOURCE1_ID_RTK |  | string(400) | Y |  |
| 40 | SOURCE1_ID_ROid |  | GUID | Y |  |
| 41 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 42 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 43 | PURCHASE_ARRIVAL_ID |  | GUID | Y |  |