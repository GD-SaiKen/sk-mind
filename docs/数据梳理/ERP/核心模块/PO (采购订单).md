---
module: "PO"
name_zh: "采购订单"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 15
columns: 1009
category: purchase
semantic_object: "PurchaseOrder/采购订单"
original_tables: 15
filtered_out: 0
tags: ["ERP", "E10", "purchase", "core"]
phase: "P0-Core"
created: "2026-06-25 13:06"
---

# PO (采购订单) - PurchaseOrder/采购订单

> [!info] Phase 1 Core Module
> Semantic Object: PurchaseOrder/采购订单
> Kept: 15 tables | Filtered out: 0 (templates/logs/backups)
> Missing CN filled: 0

## Related Modules

- [[../modules/PURCHASE (采购管理).md|PURCHASE (采购管理)]]
- [[../modules/SUPPLIER (供应商).md|SUPPLIER (供应商)]]
- [[../modules/REQUISITION (请购管理).md|REQUISITION (请购管理)]]
- [[../modules/IMPORT (进口管理).md|IMPORT (进口管理)]]

---

## Tables

- **PO_ARRIVAL_INSPECTION (采购到货检验单)**
- **PO_ARRIVAL_INSPECTION_D (采购到货检验单计数单身)**
- **PO_ARRIVAL_INSPECTION_D1 (采购到货检验单计量单身)**
- **PO_ARRIVAL_INSPECTION_SD (多次检验信息)**
- **PO_CHANGE (采购订单变更单)**
- **PO_CHANGE_D (采购订单变更单单身)**
- **PO_CHANGE_INSTAL (采购订单变更单分期)**
- **PO_CHANGE_SD (收货信息变更)**
- **PO_CHANGE_SSD (采购需求信息变更)**
- **PO_CONTRACT_INSTAL (采购合同分期)**
- **PO_INSTAL (采购订单分期)**
- **PO_QC_RESULT (维护质检业务)**
- **PO_QC_RESULT_D (采购检验信息)**
- **PO_QC_RESULT_SD (采购业务判定信息)**
- **PO_REQ_SOURCE (采购订单需求来源)**

---

## Table Details

### PO_ARRIVAL_INSPECTION (采购到货检验单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | PO_ARRIVAL_INSPECTION_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | INSPECTION_DATE | 检验日期 | date | Y |  |
| 9 | INSPECTION_TIMES | 最大抽样次数 | string(40) | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 12 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 13 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 14 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 15 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 16 | INSPECTION_QTY | 送检数量 | number(16,6) | Y |  |
| 17 | INSPECTION_UNIT_ID | 品管单位 | GUID | Y |  |
| 18 | STRICTNESS_DEGREE | 宽严程度 | string(40) | Y |  |
| 19 | INSPECTION_DUE_DATE | 检验期限 | date | Y |  |
| 20 | SUBMIT_DEPT_ID | 送检部门 | GUID | Y |  |
| 21 | SUBMIT_EMP_ID | 送检人员 | GUID | Y |  |
| 22 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 23 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 24 | ACCEPTABLE_QTY | 合格数量 | number(16,6) | Y |  |
| 25 | UNQUALIFIED_QTY | 不合格数量 | number(16,6) | Y |  |
| 26 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 27 | DECISION | 判定结果 | string(40) | Y |  |
| 28 | DECISION_DESCRIPTION | 判定说明 | string(510) | Y |  |
| 29 | RESULT_STATUS | 业务判定状态 | string(40) | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | INSPECTION_PLAN_ID | 质检方案ID | GUID | Y |  |
| 32 | COMPANY_ID | 公司 | GUID | Y |  |
| 33 | SOURCE_ID | 源单 | GUID | Y |  |
| 34 | MO_ROUTING_D_ID | 工单工艺 | GUID | Y |  |
| 35 | OPERATION_ID | 工艺 | GUID | Y |  |
| 36 | TO_MO_ROUTING_D_ID | 后道工序 | GUID | Y |  |
| 37 | TO_OPERATION_ID | 后道工艺 | GUID | Y |  |
| 38 | PROJECT_ID | 项目 | GUID | Y |  |
| 39 | DEDUCT_ARRIVED_QTY | 扣已到货量 | number(0/1) | Y |  |
| 40 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 41 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 42 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 43 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 44 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 45 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 46 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 47 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 48 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 49 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 50 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 51 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 52 | UDF041 | 自定义字段12 | date | Y |  |
| 53 | UDF042 | 自定义字段13 | date | Y |  |
| 54 | UDF051 | 自定义字段14 | GUID | Y |  |
| 55 | UDF052 | 自定义字段15 | GUID | Y |  |
| 56 | UDF053 | 自定义字段16 | GUID | Y |  |
| 57 | UDF054 | 自定义字段17 | GUID | Y |  |
| 58 | PrintCount | 打印次数 | number | Y |  |
| 59 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 60 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 61 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 62 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 63 | Version | 版本号，不要随意更改 | binary | Y |  |
| 64 | CreateDate | 创建日期 | date | Y |  |
| 65 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 66 | ModifiedDate | 修改日期 | date | Y |  |
| 67 | CreateBy | 创建者 | GUID | Y |  |
| 68 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 69 | ModifiedBy | 修改者 | GUID | Y |  |
| 70 | Attachments | 附件 | string | Y |  |
| 71 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 72 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 73 | ApproveDate | 修改日期 | date | Y |  |
| 74 | ApproveBy | 修改人 | GUID | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |


### PO_ARRIVAL_INSPECTION_D (采购到货检验单计数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PO_ARRIVAL_INSPECTION_D_ID | 主键 | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 4 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 5 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 6 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 7 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 8 | DECISION | 合格否 | number(0/1) | Y |  |
| 9 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 12 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
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
| 41 | PO_ARRIVAL_INSPECTION_ID |  | GUID | Y |  |


### PO_ARRIVAL_INSPECTION_D1 (采购到货检验单计量单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PO_ARRIVAL_INSPECTION_D1_ID | 主键 | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 4 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 5 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 6 | DECISION | 合格否 | number(0/1) | Y |  |
| 7 | IMPACT_RESULT | 影响判定 | number(0/1) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 10 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 11 | ACCEPTANCE_CONSTANT | 接收常数K | number(16,6) | Y |  |
| 12 | SS | 样本标准差S | number(16,6) | Y |  |
| 13 | XX | 平均值X | number(16,6) | Y |  |
| 14 | UU | 标准上限 | number(16,6) | Y |  |
| 15 | LL | 标准下限 | number(16,6) | Y |  |
| 16 | QU | 质量QU | number(16,6) | Y |  |
| 17 | QL | 质量QL | number(16,6) | Y |  |
| 18 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 19 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 20 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 21 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 22 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 23 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 24 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 25 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 26 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 27 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 28 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 29 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 30 | UDF041 | 自定义字段12 | date | Y |  |
| 31 | UDF042 | 自定义字段13 | date | Y |  |
| 32 | UDF051 | 自定义字段14 | GUID | Y |  |
| 33 | UDF052 | 自定义字段15 | GUID | Y |  |
| 34 | UDF053 | 自定义字段16 | GUID | Y |  |
| 35 | UDF054 | 自定义字段17 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | PO_ARRIVAL_INSPECTION_ID |  | GUID | Y |  |


### PO_ARRIVAL_INSPECTION_SD (多次检验信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PO_ARRIVAL_INSPECTION_SD_ID | 主键 | GUID | Y | Y |
| 2 | INSPECTION_TIMES | 检验次数 | number | Y |  |
| 3 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 4 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 5 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 6 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 9 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 10 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 11 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 12 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 13 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 14 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 15 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 16 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 17 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 18 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 19 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 20 | UDF041 | 自定义字段12 | date | Y |  |
| 21 | UDF042 | 自定义字段13 | date | Y |  |
| 22 | UDF051 | 自定义字段14 | GUID | Y |  |
| 23 | UDF052 | 自定义字段15 | GUID | Y |  |
| 24 | UDF053 | 自定义字段16 | GUID | Y |  |
| 25 | UDF054 | 自定义字段17 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | PO_ARRIVAL_INSPECTION_D_ID |  | GUID | Y |  |


### PO_CHANGE (采购订单变更单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PO_CHANGE_ID | 主键 | GUID | Y | Y |
| 4 | CHANGE_DATE | 变更日期 | date | Y |  |
| 5 | SUPPLIER_FULL_NAME | 供应商全称 | string(144) | Y |  |
| 6 | SUPPLIER_CONTACT_NAME | 供应商联系人 | string(72) | Y |  |
| 7 | SUPPLIER_ADDR_NAME | 供应商地址 | string(510) | Y |  |
| 8 | EXCHANGE_RATE | 匯率 | number(18,9) | Y |  |
| 9 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 10 | MULTI_PLANT | 多收货工厂/储运 | number(0/1) | Y |  |
| 11 | DELIVERY_CONTACT_NAME | 发货联系人 | string(72) | Y |  |
| 12 | DELIVERY_ADDR_NAME | 发货地址 | string(510) | Y |  |
| 13 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 14 | INVOICE_CONTACT_NAME | 结算联系人 | string(72) | Y |  |
| 15 | INVOICE_ADDR_NAME | 结算地址 | string(510) | Y |  |
| 16 | SUPPLIER_ORDER_NO | 供应商单号 | string(510) | Y |  |
| 17 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 18 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 19 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 20 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | PIECES |  | number | Y |  |
| 23 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 24 | DIRECT_SHIPMENT | 供应商直运 | number(0/1) | Y |  |
| 25 | INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 26 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 27 | EARNEST | 订金 | number(23,8) | Y |  |
| 28 | EARNEST_RATE |  | number(5,4) | Y |  |
| 29 | EARNEST_SETTLEMENT_TYPE | 订金结算方式 | string(40) | Y |  |
| 30 | TAX_RATE |  | number(5,4) | Y |  |
| 31 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 32 | COMPANY_ID | 订单公司 | GUID | Y |  |
| 33 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 34 | SUPPLIER_CONTACT_ID | 联系人编码 | GUID | Y |  |
| 35 | SUPPLIER_ADDR_ID | 地址编码 | GUID | Y |  |
| 36 | CURRENCY_ID | 币种 | GUID | Y |  |
| 37 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 38 | PLANT_ID | 收货工厂/储运 | GUID | Y |  |
| 39 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 40 | DELIVERY_CONTACT_ID | 发货联系人编码 | GUID | Y |  |
| 41 | DELIVERY_ADDR_ID | 发货地址编码 | GUID | Y |  |
| 42 | INVOICE_COMPANY_ID | 结算公司 | GUID | Y |  |
| 43 | INVOICE_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 44 | INVOICE_CONTACT_ID | 结算联系人编码 | GUID | Y |  |
| 45 | INVOICE_ADDR_ID | 结算地址编码 | GUID | Y |  |
| 46 | PURCHASE_CONTRACT_ID | 采购合同 | GUID | Y |  |
| 47 | TAX_ID | 税种 | GUID | Y |  |
| 48 | CHANGE_VERSION | 变更版本 | string(4) | Y |  |
| 49 | REMARK_CHANGE | 变更原因 | string(510) | Y |  |
| 50 | PURCHASE_ORDER_ID | 原订单ID | GUID | Y |  |
| 51 | ORI_EXCHANGE_RATE | 原汇率 | number(18,9) | Y |  |
| 52 | ORI_TAX_INCLUDED | 原含税 | number(0/1) | Y |  |
| 53 | ORI_MULTI_PLANT | 原多收货工厂/储运 | number(0/1) | Y |  |
| 54 | ORI_DELIVERY_CONTACT_NAME | 原发货联系人 | string(72) | Y |  |
| 55 | ORI_DELIVERY_ADDR_NAME | 原发货地址 | string(510) | Y |  |
| 56 | ORI_PARTIAL_DELIVERY | 原允许分批交货 | number(0/1) | Y |  |
| 57 | ORI_INVOICE_CONTACT_NAME | 原结算联系人 | string(72) | Y |  |
| 58 | ORI_INVOICE_ADDR_NAME | 原结算地址 | string(510) | Y |  |
| 59 | ORI_SUPPLIER_ORDER_NO | 原供应商单号 | string(510) | Y |  |
| 60 | ORI_AMOUNT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 61 | ORI_TAX_OC | 原原币税额 | number(23,8) | Y |  |
| 62 | ORI_AMOUNT_UNINCLUDE_TAX_BC | 原本币未税金额 | number(23,8) | Y |  |
| 63 | ORI_TAX_BC | 原本币税额 | number(23,8) | Y |  |
| 64 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 65 | ORI_PIECES | 原件数 | number | Y |  |
| 66 | ORI_PURCHASE_TYPE | 原采购类型 | string(40) | Y |  |
| 67 | ORI_DIRECT_SHIPMENT | 原供应商直运 | number(0/1) | Y |  |
| 68 | ORI_INSTALLMENT | 原分期付款 | number(0/1) | Y |  |
| 69 | ORI_INSTALLMENT_TYPE | 原分期类型 | string(40) | Y |  |
| 70 | ORI_EARNEST | 原订金 | number(23,8) | Y |  |
| 71 | ORI_EARNEST_RATE |  | number(5,4) | Y |  |
| 72 | ORI_EARNEST_SETTLEMENT_TYPE | 原订金结算方式 | string(40) | Y |  |
| 73 | ORI_TAX_RATE | 原税率 | number(5,4) | Y |  |
| 74 | ORI_TAX_INVOICE_CATEGORY_ID | 原发票种类 | GUID | Y |  |
| 75 | ORI_COMPANY_ID | 原订单公司 | GUID | Y |  |
| 76 | ORI_CURRENCY_ID | 原币种 | GUID | Y |  |
| 77 | ORI_PAYMENT_TERM_ID | 原付款条件 | GUID | Y |  |
| 78 | ORI_PLANT_ID | 原收货工厂/储运 | GUID | Y |  |
| 79 | ORI_DELIVERY_TERM_ID | 原运输方式 | GUID | Y |  |
| 80 | ORI_DELIVERY_CONTACT_ID | 原发货联系人编码 | GUID | Y |  |
| 81 | ORI_DELIVERY_ADDR_ID | 原发货地址编码 | GUID | Y |  |
| 82 | ORI_INVOICE_COMPANY_ID | 原结算公司 | GUID | Y |  |
| 83 | ORI_INVOICE_SUPPLIER_ID | 原结算供应商 | GUID | Y |  |
| 84 | ORI_INVOICE_CONTACT_ID | 原结算联系人编码 | GUID | Y |  |
| 85 | ORI_INVOICE_ADDR_ID | 原结算地址编码 | GUID | Y |  |
| 86 | ORI_PURCHASE_CONTRACT_ID | 原采购合同 | GUID | Y |  |
| 87 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 88 | DOC_DATE | 单据日期 | date | Y |  |
| 89 | ORI_Owner_Dept | 原采购部门 | GUID | Y |  |
| 90 | ORI_Owner_Emp | 原采购员 | GUID | Y |  |
| 91 | ORI_SUPPLIER_ADDR_ID | 原地址编码 | GUID | Y |  |
| 92 | ORI_SUPPLIER_CONTACT_NAME | 原供应商联系人 | string(72) | Y |  |
| 93 | ORI_SUPPLIER_ADDR_NAME | 原供应商地址 | string(510) | Y |  |
| 94 | ORI_SUPPLIER_CONTACT_ID | 原联系人编码 | GUID | Y |  |
| 95 | PLANT_ADDRESS | 收货地址 | string(510) | Y |  |
| 96 | ORI_PLANT_ADDRESS | 原收货地址 | string(510) | Y |  |
| 97 | DOC_ID | 主键 | GUID | Y |  |
| 98 | FULL_CLOSE | 整张结束 | number(0/1) | Y |  |
| 99 | ORI_CLOSE | 原结束码 | string(40) | Y |  |
| 100 | PROJECT_ID | 限用项目 | GUID | Y |  |
| 101 | ORI_PROJECT_ID | 原限用项目 | GUID | Y |  |
| 102 | Version | 版本号，不要随意更改 | binary | Y |  |
| 103 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 104 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 105 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 106 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 107 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 108 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 109 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 110 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 111 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 112 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 113 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 114 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 115 | UDF041 | 自定义字段12 | date | Y |  |
| 116 | UDF042 | 自定义字段13 | date | Y |  |
| 117 | UDF051 | 自定义字段14 | GUID | Y |  |
| 118 | UDF052 | 自定义字段15 | GUID | Y |  |
| 119 | UDF053 | 自定义字段16 | GUID | Y |  |
| 120 | UDF054 | 自定义字段17 | GUID | Y |  |
| 121 | PrintCount | 打印次数 | number | Y |  |
| 122 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 123 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 124 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 125 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 126 | CreateDate | 创建日期 | date | Y |  |
| 127 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 128 | ModifiedDate | 修改日期 | date | Y |  |
| 129 | CreateBy | 创建者 | GUID | Y |  |
| 130 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 131 | ModifiedBy | 修改者 | GUID | Y |  |
| 132 | Attachments | 附件 | string | Y |  |
| 133 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 134 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 135 | ApproveDate | 修改日期 | date | Y |  |
| 136 | ApproveBy | 修改人 | GUID | Y |  |
| 137 | Owner_Org_RTK |  | string(400) | Y |  |
| 138 | Owner_Org_ROid |  | GUID | Y |  |
| 139 | REV_ORG_SOURCE_ID_RTK |  | string(400) | Y |  |
| 140 | REV_ORG_SOURCE_ID_ROid |  | GUID | Y |  |
| 141 | ORI_REV_ORG_SOURC_ID_RTK |  | string(400) | Y |  |
| 142 | ORI_REV_ORG_SOURC_ID_ROid |  | GUID | Y |  |
| 143 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 144 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 145 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 146 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 147 | DOC_Sequence | 单据顺序 | number | Y |  |
| 148 | SOURCE_SUPPLIER_ID | 最终供应商 | GUID | Y |  |
| 149 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 150 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |
| 151 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 152 | SOURCE_ORDER_ROid |  | GUID | Y |  |


### PO_CHANGE_D (采购订单变更单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PO_CHANGE_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 4 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 5 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 6 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 8 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 11 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 12 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 13 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 14 | PRICE | 單價 | number(23,8) | Y |  |
| 15 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 16 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 17 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 18 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 19 | AMOUNT |  | number(23,8) | Y |  |
| 20 | TAX_RATE | 稅率 | number(5,4) | Y |  |
| 21 | AMOUNT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 22 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 23 | AMOUNT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 24 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 25 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 26 | MULTI_ARRIVAL_DATE | 多交期 | number(0/1) | Y |  |
| 27 | PIECES |  | number | Y |  |
| 28 | MANUFACTURER | 品牌信息 | string(510) | Y |  |
| 29 | REMARK | 备注 | string(510) | Y |  |
| 30 | PURCHASE_TYPE | 采购类型 | string(40) | Y |  |
| 31 | ITEM_ID | 品号 | GUID | Y |  |
| 32 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 33 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 34 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 35 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 36 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 37 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 38 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 39 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 40 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 41 | TAX_ID | 税种 | GUID | Y |  |
| 42 | ITEM_CERTIFICATION_D_ID | 认可文号 | GUID | Y |  |
| 43 | OPERATION_ID | 工艺 | GUID | Y |  |
| 44 | REMARK_CHANGE | 变更原因 | string(510) | Y |  |
| 45 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 46 | PURCHASE_ORDER_D_ID | 原订单行ID | GUID | Y |  |
| 47 | ORI_ITEM_DESCRIPTION | 原品名 | string(120) | Y |  |
| 48 | ORI_ITEM_SPECIFICATION | 原规格 | string(510) | Y |  |
| 49 | ORI_ITEM_TYPE | 原商品类型 | string(40) | Y |  |
| 50 | ORI_PACKING_QTY1 | 原大包装数量 | number(16,6) | Y |  |
| 51 | ORI_PACKING_QTY2 | 原中包装数量 | number(16,6) | Y |  |
| 52 | ORI_PACKING_QTY3 | 原小包装数量 | number(16,6) | Y |  |
| 53 | ORI_PACKING_QTY4 | 原最小包装数量 | number(16,6) | Y |  |
| 54 | ORI_PACKING_QTY | 原包装数量描述 | string(240) | Y |  |
| 55 | ORI_BUSINESS_QTY | 原业务数量 | number(16,6) | Y |  |
| 56 | ORI_PRICE_QTY | 原计价数量 | number(16,6) | Y |  |
| 57 | ORI_INVENTORY_QTY | 原库存单位数量 | number(16,6) | Y |  |
| 58 | ORI_SECOND_QTY | 原第二数量 | number(16,6) | Y |  |
| 59 | ORI_PRICE | 原单价 | number(23,8) | Y |  |
| 60 | ORI_DISCOUNT_RATE | 原折扣率 | number(5,4) | Y |  |
| 61 | ORI_DISCOUNTED_PRICE | 原折扣后单价 | number(23,8) | Y |  |
| 62 | ORI_STANDARD_PRICE | 原标准单价 | number(23,8) | Y |  |
| 63 | ORI_DISCOUNT_AMT | 原折扣额 | number(23,8) | Y |  |
| 64 | ORI_AMOUNT | 原金额 | number(23,8) | Y |  |
| 65 | ORI_TAX_RATE | 原稅率 | number(5,4) | Y |  |
| 66 | ORI_AMOUNT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 67 | ORI_TAX_OC | 原原币税额 | number(23,8) | Y |  |
| 68 | ORI_AMOUNT_UNINCLUDE_TAX_BC | 原本币未税金额 | number(23,8) | Y |  |
| 69 | ORI_TAX_BC | 原本币税额 | number(23,8) | Y |  |
| 70 | ORI_PLAN_ARRIVAL_DATE | 原预到货日 | date | Y |  |
| 71 | ORI_MULTI_ARRIVAL_DATE | 原多交期 | number(0/1) | Y |  |
| 72 | ORI_PIECES | 原件数 | number | Y |  |
| 73 | ORI_MANUFACTURER | 原品牌信息 | string(510) | Y |  |
| 74 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 75 | ORI_PURCHASE_TYPE | 原采购类型 | string(40) | Y |  |
| 76 | ORI_ITEM_ID | 原品号 | GUID | Y |  |
| 77 | ORI_ITEM_FEATURE_ID | 原特征码 | GUID | Y |  |
| 78 | ORI_PACKING_MODE_ID | 原包装方式 | GUID | Y |  |
| 79 | ORI_PACKING1_UNIT_ID | 原大包装单位 | GUID | Y |  |
| 80 | ORI_PACKING2_UNIT_ID | 原中包装单位 | GUID | Y |  |
| 81 | ORI_PACKING3_UNIT_ID | 原小包装单位 | GUID | Y |  |
| 82 | ORI_PACKING4_UNIT_ID | 原最小包装单位 | GUID | Y |  |
| 83 | ORI_BUSINESS_UNIT_ID | 原业务单位 | GUID | Y |  |
| 84 | ORI_PRICE_UNIT_ID | 原计价单位 | GUID | Y |  |
| 85 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 86 | ORI_ITEM_CERTIFICATION_D_ID | 原认可文号 | GUID | Y |  |
| 87 | ORI_OPERATION_ID | 原工艺 | GUID | Y |  |
| 88 | DIRECT_SUPPLY | 直供 | number(0/1) | Y |  |
| 89 | ORI_DIRECT_SUPPLY | 原直供 | number(0/1) | Y |  |
| 90 | PROJECT_ID | 项目 | GUID | Y |  |
| 91 | ORI_PROJECT_ID | 原项目 | GUID | Y |  |
| 92 | Version | 版本号，不要随意更改 | binary | Y |  |
| 93 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 94 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 95 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 96 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 97 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 98 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 99 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 100 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 101 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 102 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 103 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 104 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 105 | UDF041 | 自定义字段12 | date | Y |  |
| 106 | UDF042 | 自定义字段13 | date | Y |  |
| 107 | UDF051 | 自定义字段14 | GUID | Y |  |
| 108 | UDF052 | 自定义字段15 | GUID | Y |  |
| 109 | UDF053 | 自定义字段16 | GUID | Y |  |
| 110 | UDF054 | 自定义字段17 | GUID | Y |  |
| 111 | CreateDate | 创建日期 | date | Y |  |
| 112 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 113 | ModifiedDate | 修改日期 | date | Y |  |
| 114 | CreateBy | 创建者 | GUID | Y |  |
| 115 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 116 | ModifiedBy | 修改者 | GUID | Y |  |
| 117 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 118 | ApproveDate | 修改日期 | date | Y |  |
| 119 | ApproveBy | 修改人 | GUID | Y |  |
| 120 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 121 | SOURCE_ID_ROid |  | GUID | Y |  |
| 122 | ORI_SOURCE_ID_RTK |  | string(400) | Y |  |
| 123 | ORI_SOURCE_ID_ROid |  | GUID | Y |  |
| 124 | PO_CHANGE_ID |  | GUID | Y |  |
| 125 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 126 | SOURCE_ORDER_ROid |  | GUID | Y |  |


### PO_CHANGE_INSTAL (采购订单变更单分期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PO_INSTAL_ID | 原序号 | GUID | Y |  |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | INSTALLMENT_NAME |  | string(60) | Y |  |
| 5 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 6 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 7 | INSTALLMENT_DATE | 执行日 | date | Y |  |
| 8 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 9 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 10 | PAYMENT_TERM_ID | 主键 | GUID | Y |  |
| 11 | PAYMENT_TERM_REMARK |  | string(510) | Y |  |
| 12 | PAYMENT_DATE | 付款日 | date | Y |  |
| 13 | CASHING_DATE | 兑现日 | date | Y |  |
| 14 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 15 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 16 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 17 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 18 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 19 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 20 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 21 | REMARK |  | string(510) | Y |  |
| 22 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 23 | TAX_ID | 税种 | GUID | Y |  |
| 24 | TAX_RATE |  | number(5,4) | Y |  |
| 25 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 26 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 27 | ORI_INSTALLMENT_NAME | 原分期名称 | string(60) | Y |  |
| 28 | ORI_INSTALLMENT_RATE | 原分期比率 | number(5,4) | Y |  |
| 29 | ORI_INSTALLMENT_AMT_OC | 原原币分期金额 | number(23,8) | Y |  |
| 30 | ORI_INSTALLMENT_DATE | 原执行日 | date | Y |  |
| 31 | ORI_PAYMENT_BASE_DATE_S | 原基准日来源 | number | Y |  |
| 32 | ORI_PAYMENT_BASE_DATE | 原基准日 | date | Y |  |
| 33 | ORI_PAYMENT_TERM_ID | 原付款条件 | GUID | Y |  |
| 34 | ORI_PAYMENT_TERM_REMARK | 原付款条件说明 | string(510) | Y |  |
| 35 | ORI_PAYMENT_DATE | 原付款日 | date | Y |  |
| 36 | ORI_CASHING_DATE | 原兑现日 | date | Y |  |
| 37 | ORI_CASH_DISCOUNT_MODE | 原现金折扣方式 | number | Y |  |
| 38 | ORI_CASH_DISCOUNT_RATE1 | 原现金折扣率1 | number(5,4) | Y |  |
| 39 | ORI_CASH_DISCOUNT_DUE_DATE1 | 原现金折扣到期日1 | date | Y |  |
| 40 | ORI_CASH_DISCOUNT_RATE2 | 原现金折扣率2 | number(5,4) | Y |  |
| 41 | ORI_CASH_DISCOUNT_DUE_DATE2 | 原现金折扣到期日2 | date | Y |  |
| 42 | ORI_CASH_DISCOUNT_RATE3 | 原现金折扣率3 | number(5,4) | Y |  |
| 43 | ORI_CASH_DISCOUNT_DUE_DATE3 | 原现金折扣到期日3 | date | Y |  |
| 44 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 45 | ORI_INSTALLMENT_TYPE | 原分期类型 | string(40) | Y |  |
| 46 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 47 | ORI_TAX_RATE | 原税率 | number(5,4) | Y |  |
| 48 | ORI_AMT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 49 | ORI_TAX_OC | 原原币税额 | number(23,8) | Y |  |
| 50 | CONTRACT_INSTAL_ID | 主键 | GUID | Y | Y |
| 51 | ORI_TAX_INCLUDED | 原含税 | number(0/1) | Y |  |
| 52 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 55 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 56 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 57 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 58 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 59 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 60 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 61 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 62 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 63 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 64 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 65 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 66 | UDF041 | 自定义字段12 | date | Y |  |
| 67 | UDF042 | 自定义字段13 | date | Y |  |
| 68 | UDF051 | 自定义字段14 | GUID | Y |  |
| 69 | UDF052 | 自定义字段15 | GUID | Y |  |
| 70 | UDF053 | 自定义字段16 | GUID | Y |  |
| 71 | UDF054 | 自定义字段17 | GUID | Y |  |
| 72 | CreateDate | 创建日期 | date | Y |  |
| 73 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 74 | ModifiedDate | 修改日期 | date | Y |  |
| 75 | CreateBy | 创建者 | GUID | Y |  |
| 76 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 77 | ModifiedBy | 修改者 | GUID | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |
| 81 | PO_CHANGE_ID |  | GUID | Y |  |


### PO_CHANGE_SD (收货信息变更)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PO_CHANGE_SD_ID | 主键 | GUID | Y | Y |
| 3 | PLAN_ARRIVAL_DATE | 预到货日 | date | Y |  |
| 4 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 5 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 6 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 8 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 9 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 10 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 11 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 12 | PIECES |  | number | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 15 | SUPPLY_SYNERGY_ID | 供应协同关系 | GUID | Y |  |
| 16 | PLANT_ID | 收货工厂/储运 | GUID | Y |  |
| 17 | WAREHOUSE_ID | 仓库 | GUID | Y |  |
| 18 | REMARK_CHANGE | 变更原因 | string(510) | Y |  |
| 19 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 20 | PURCHASE_ORDER_SD_ID |  | GUID | Y |  |
| 21 | ORI_PLAN_ARRIVAL_DATE | 原预到货日 | date | Y |  |
| 22 | ORI_BUSINESS_QTY | 原业务数量 | number(16,6) | Y |  |
| 23 | ORI_PRICE_QTY | 原计价数量 | number(16,6) | Y |  |
| 24 | ORI_SECOND_QTY | 原第二数量 | number(16,6) | Y |  |
| 25 | ORI_INVENTORY_QTY | 原库存单位数量 | number(16,6) | Y |  |
| 26 | ORI_PACKING_QTY | 原包装数量描述 | string(240) | Y |  |
| 27 | ORI_PACKING_QTY1 | 原大包装数量 | number(16,6) | Y |  |
| 28 | ORI_PACKING_QTY2 | 原中包装数量 | number(16,6) | Y |  |
| 29 | ORI_PACKING_QTY3 | 原小包装数量 | number(16,6) | Y |  |
| 30 | ORI_PACKING_QTY4 | 原最小包装数量 | number(16,6) | Y |  |
| 31 | ORI_PIECES | 原件数 | number | Y |  |
| 32 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 33 | ORI_SUPPLY_SYNERGY_ID | 原供应协同关系 | GUID | Y |  |
| 34 | ORI_PLANT_ID | 原收货工厂/储运 | GUID | Y |  |
| 35 | ORI_WAREHOUSE_ID | 原仓库 | GUID | Y |  |
| 36 | PLANT_ADDRESS | 收货地址 | string(510) | Y |  |
| 37 | ORI_PLANT_ADDRESS | 原收货地址 | string(510) | Y |  |
| 38 | ORI_RECEIPT_CLOSE | 原入库结束码 | string(40) | Y |  |
| 39 | ORI_RECEIPTED_PRICE_QTY | 原已入库计价数量 | number(16,6) | Y |  |
| 40 | ORI_RECEIPTED_BUSINESS_QTY | 原已入库业务数量 | number(16,6) | Y |  |
| 41 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 42 | ORI_ESTI_PAYMENT_DATE | 原预计付款日 | date | Y |  |
| 43 | PROJECT_ID | 项目 | GUID | Y |  |
| 44 | ORI_PROJECT_ID | 原项目 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 47 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 48 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 49 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 50 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 51 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 52 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 53 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 54 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 55 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 56 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 57 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 58 | UDF041 | 自定义字段12 | date | Y |  |
| 59 | UDF042 | 自定义字段13 | date | Y |  |
| 60 | UDF051 | 自定义字段14 | GUID | Y |  |
| 61 | UDF052 | 自定义字段15 | GUID | Y |  |
| 62 | UDF053 | 自定义字段16 | GUID | Y |  |
| 63 | UDF054 | 自定义字段17 | GUID | Y |  |
| 64 | CreateDate | 创建日期 | date | Y |  |
| 65 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 66 | ModifiedDate | 修改日期 | date | Y |  |
| 67 | CreateBy | 创建者 | GUID | Y |  |
| 68 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 69 | ModifiedBy | 修改者 | GUID | Y |  |
| 70 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 71 | ApproveDate | 修改日期 | date | Y |  |
| 72 | ApproveBy | 修改人 | GUID | Y |  |
| 73 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 74 | SOURCE_ID_ROid |  | GUID | Y |  |
| 75 | ORI_SOURCE_ID_RTK |  | string(400) | Y |  |
| 76 | ORI_SOURCE_ID_ROid |  | GUID | Y |  |
| 77 | REV_Owner_Org_RTK |  | string(400) | Y |  |
| 78 | REV_Owner_Org_ROid |  | GUID | Y |  |
| 79 | ORI_REV_Owner_Org_RTK |  | string(400) | Y |  |
| 80 | ORI_REV_Owner_Org_ROid |  | GUID | Y |  |
| 81 | SO_SOURCE_ID_RTK |  | string(400) | Y |  |
| 82 | SO_SOURCE_ID_ROid |  | GUID | Y |  |
| 83 | ORI_SO_SOURCE_ID_RTK |  | string(400) | Y |  |
| 84 | ORI_SO_SOURCE_ID_ROid |  | GUID | Y |  |
| 85 | PO_CHANGE_D_ID |  | GUID | Y |  |
| 86 | AMOUNT | 金额 | number(23,8) | Y |  |
| 87 | ORI_AMOUNT | 原金额 | number(23,8) | Y |  |
| 88 | BUDGET_ADMIN_UNIT_ID | 预算部门 | GUID | Y |  |
| 89 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
| 90 | BUDGET_ITEM_ID | 预算项 | GUID | Y |  |
| 91 | BUDGET_ID | 执行预算 | GUID | Y |  |
| 92 | BUDGET_D_ID | 执行预算行 | GUID | Y |  |
| 93 | PRE_BUDGET_D_ID | 前置预算行 | GUID | Y |  |
| 94 | PRE_BUDGET_ID | 前置预算 | GUID | Y |  |
| 95 | INCLUDE_PLAN | 纳入计划 | number(0/1) | Y |  |
| 96 | TRANSACTION_PLANT_ID | 交易工厂 | GUID | Y |  |


### PO_CHANGE_SSD (采购需求信息变更)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PO_CHANGE_SSD_ID | 主键 | GUID | Y | Y |
| 3 | DEMAND_NO | 参考单号 | string(8000) | Y |  |
| 4 | DEMAND_QTY | 业务数量 | number(16,6) | Y |  |
| 5 | DEMAND_DATE | 需求日期 | date | Y |  |
| 6 | PURCHASED_QTY | 已采业务数量 | number(16,6) | Y |  |
| 7 | ARRIVED_QTY | 已到货业务数量 | number(16,6) | Y |  |
| 8 | RECEIPTED_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 9 | PURCHASE_SEQUENCE | 采购核销顺序 | string(20) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | PLAN_ARRIVAL_DATE | 收货信息预到货日 | date | Y |  |
| 12 | REQUISITION_D_DATE | 请购单单身需求日期 | date | Y |  |
| 13 | PLAN_SHIP_DATE1 | 销售订单预发货日 | date | Y |  |
| 14 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 15 | LOCKED_FLAG | 供需关连锁定 | number(0/1) | Y |  |
| 16 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 17 | ORI_DEMAND_NO | 原参考单号 | string(8000) | Y |  |
| 18 | ORI_DEMAND_QTY | 原业务数量 | number(16,6) | Y |  |
| 19 | DEMAND_UNIT_ID | 业务单位 | GUID | Y |  |
| 20 | ORI_DEMAND_DATE | 原需求日期 | date | Y |  |
| 21 | ORI_ARRIVED_QTY | 原已到货业务数量 | number(16,6) | Y |  |
| 22 | ORI_RECEIPTED_QTY | 原已入库业务数量 | number(16,6) | Y |  |
| 23 | ORI_PURCHASE_SEQ | 采购核销顺序 | string(20) | Y |  |
| 24 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 25 | ORI_DEMAND_UNIT_ID | 原业务单位 | GUID | Y |  |
| 26 | ORI_PLANARRIVAL_DATE | 原收货信息预到货日 | date | Y |  |
| 27 | ORI_REQ_D_DATE | 原请购单单身需求日期 | date | Y |  |
| 28 | ORI_PLAN_SHIP_DATE1 | 原销售订单预发货日 | date | Y |  |
| 29 | ORI_PRICE_QTY | 原计价数量 | number(16,6) | Y |  |
| 30 | ORI_LOCKED_FLAG | 原供需关连锁定 | number(0/1) | Y |  |
| 31 | ORI_INVENTORY_QTY | 原库存单位数量 | number(16,6) | Y |  |
| 32 | ARRIVED_INV_QTY | 已到货库存单位数量 | number(16,6) | Y |  |
| 33 | RECEIPTED_INV_QTY | 已入库库存单位数量 | number(16,6) | Y |  |
| 34 | ORI_ARRIVED_INV_QTY | 原已到货库存单位数量 | number(16,6) | Y |  |
| 35 | ORI_RECEIPT_INV_QTY | 原已入库库存单位数量 | number(16,6) | Y |  |
| 36 | PUR_ORDER_SSD_ID | 原需求信息主键 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 44 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 45 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 46 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 47 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 48 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 49 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 50 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 51 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 52 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 53 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 54 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 55 | UDF041 | 自定义字段12 | date | Y |  |
| 56 | UDF042 | 自定义字段13 | date | Y |  |
| 57 | UDF051 | 自定义字段14 | GUID | Y |  |
| 58 | UDF052 | 自定义字段15 | GUID | Y |  |
| 59 | UDF053 | 自定义字段16 | GUID | Y |  |
| 60 | UDF054 | 自定义字段17 | GUID | Y |  |
| 61 | Version | 版本号，不要随意更改 | binary | Y |  |
| 62 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 63 | ApproveDate | 修改日期 | date | Y |  |
| 64 | ApproveBy | 修改人 | GUID | Y |  |
| 65 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE_ID_ROid |  | GUID | Y |  |
| 67 | REFERENCE_SOURCE_ID_RTK |  | string(400) | Y |  |
| 68 | REFERENCE_SOURCE_ID_ROid |  | GUID | Y |  |
| 69 | ORI_SOURCE_ID_RTK |  | string(400) | Y |  |
| 70 | ORI_SOURCE_ID_ROid |  | GUID | Y |  |
| 71 | ORI_REF_SOURCE_ID_RTK |  | string(400) | Y |  |
| 72 | ORI_REF_SOURCE_ID_ROid |  | GUID | Y |  |
| 73 | PO_CHANGE_SD_ID |  | GUID | Y |  |


### PO_CONTRACT_INSTAL (采购合同分期)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | INSTALLMENT_NAME |  | string(60) | Y |  |
| 3 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 4 | SETTLEMENT_AMT_OC | 原币已结算金额 | number(23,8) | Y |  |
| 5 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 6 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 7 | PAYMENT_DATE | 付款日 | date | Y |  |
| 8 | CASHING_DATE | 兑现日 | date | Y |  |
| 9 | DISCOUNT_INDICATOR | 取得折扣标识 | number(0/1) | Y |  |
| 10 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 11 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 12 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 13 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 14 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 15 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 16 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 17 | PO_CONTRACT_INSTAL_ID | 主键 | GUID | Y | Y |
| 18 | CONTRACT_INSTAL_AMT_TC | 合同分期-原币 | number(23,8) | Y |  |
| 19 | PAYMENT_TERM_REMARK | 付款条件说明 | string(510) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | VERIFICATION_AMT_OC | 原币已核销金额 | number(23,8) | Y |  |
| 22 | INSTALLMENT_DATE | 执行日 | date | Y |  |
| 23 | BALANCE_AMT_OC | 原币未付余额 | number(23,8) | Y |  |
| 24 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 25 | PREPAYMENT_AMT_OC | 原币预付金额 | number(23,8) | Y |  |
| 26 | SETTLEMENT_AMT_TC | 已结算原币金额 | number(23,8) | Y |  |
| 27 | UNSETTLEMENT_AMT_TC | 未结算原币金额 | number(23,8) | Y |  |
| 28 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 29 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 30 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 31 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 32 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 33 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 34 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 35 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 36 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 37 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 38 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 39 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 40 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 41 | UDF041 | 自定义字段12 | date | Y |  |
| 42 | UDF042 | 自定义字段13 | date | Y |  |
| 43 | UDF051 | 自定义字段14 | GUID | Y |  |
| 44 | UDF052 | 自定义字段15 | GUID | Y |  |
| 45 | UDF053 | 自定义字段16 | GUID | Y |  |
| 46 | UDF054 | 自定义字段17 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | PURCHASE_CONTRACT_ID |  | GUID | Y |  |


### PO_INSTAL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PO_INSTAL_ID | 主键 | GUID | Y | Y |
| 3 | INSTALLMENT_NAME | 分期名称 | string(60) | Y |  |
| 4 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 5 | INSTALLMENT_DATE | 执行日 | date | Y |  |
| 6 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 7 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 8 | PAYMENT_TERM_REMARK | 付款条件说明 | string(510) | Y |  |
| 9 | PAYMENT_DATE | 付款日 | date | Y |  |
| 10 | CASHING_DATE | 兑现日 | date | Y |  |
| 11 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 12 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 13 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 14 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 15 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 16 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 17 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | VERIFICATION_AMT_OC | 原币已核销金额 | number(23,8) | Y |  |
| 20 | BALANCE_AMT_OC | 原币未付余额 | number(23,8) | Y |  |
| 21 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 22 | PREPAYMENT_AMT_OC | 原币预付金额 | number(23,8) | Y |  |
| 23 | SETTLEMENT_AMT_OC | 原币已结算金额 | number(23,8) | Y |  |
| 24 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 25 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 26 | TAX_ID | 税种 | GUID | Y |  |
| 27 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 28 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 29 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 30 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 31 | PRE_SETTLEMENT_AMT_UN_TAX_OC | 预结算原币未税金额 | number(23,8) | Y |  |
| 32 | PRE_SETTLEMENT_TAX_OC | 预结算原币税额 | number(23,8) | Y |  |
| 33 | OFFSETED_AMT_UN_TAX_OC | 已冲减原币未税金额 | number(23,8) | Y |  |
| 34 | OFFSETED_TAX_OC | 已冲减原币税额 | number(23,8) | Y |  |
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
| 53 | CreateDate | 创建日期 | date | Y |  |
| 54 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 55 | ModifiedDate | 修改日期 | date | Y |  |
| 56 | CreateBy | 创建者 | GUID | Y |  |
| 57 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 58 | ModifiedBy | 修改者 | GUID | Y |  |
| 59 | Version | 版本号，不要随意更改 | binary | Y |  |
| 60 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 61 | ApproveDate | 修改日期 | date | Y |  |
| 62 | ApproveBy | 修改人 | GUID | Y |  |
| 63 | PURCHASE_ORDER_ID |  | GUID | Y |  |


### PO_QC_RESULT (维护质检业务)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PO_QC_RESULT_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | DEDUCT_ARRIVED_QTY | 扣已到货量 | number(0/1) | Y |  |
| 6 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 7 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 8 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 9 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 10 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 11 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 12 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 13 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 14 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 15 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 16 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 17 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 18 | UDF041 | 自定义字段12 | date | Y |  |
| 19 | UDF042 | 自定义字段13 | date | Y |  |
| 20 | UDF051 | 自定义字段14 | GUID | Y |  |
| 21 | UDF052 | 自定义字段15 | GUID | Y |  |
| 22 | UDF053 | 自定义字段16 | GUID | Y |  |
| 23 | UDF054 | 自定义字段17 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 26 | ApproveDate | 修改日期 | date | Y |  |
| 27 | ApproveBy | 修改人 | GUID | Y |  |
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |
| 38 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 39 | SOURCE_ID_ROid |  | GUID | Y |  |


### PO_QC_RESULT_D (采购检验信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PO_QC_RESULT_D_ID | 主键 | GUID | Y | Y |
| 2 | QC_DATE | 检验日期 | date | Y |  |
| 3 | QUALIFIED_BUSINESS_QTY | 合格业务数量 | number(16,6) | Y |  |
| 4 | UNQUALIFIED_BUSINESS_QTY | 不合格业务数量 | number(16,6) | Y |  |
| 5 | IN_DESTROYED_BUSINESS_QTY | 检验破坏业务数量 | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | PO_INSPECTION_CODE | 检验单号 | string(400) | Y |  |
| 8 | DETERMINE_QTY | 待判定业务数量 | number(16,6) | Y |  |
| 9 | RESULT_STATUS | 业务判定状态 | string(400) | Y |  |
| 10 | PO_INSPECTION_ID | 检验单 | GUID | Y |  |
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
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | PO_QC_RESULT_ID |  | GUID | Y |  |


### PO_QC_RESULT_SD (采购业务判定信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ACCEPTED_BUSINESS_QTY | 允收业务数量 | number(16,6) | Y |  |
| 3 | SP_RECEIPT_BUSINESS_QTY | 特采业务数量 | number(16,6) | Y |  |
| 4 | SCRAP_BUSINESS_QTY | 报废业务数量 | number(16,6) | Y |  |
| 5 | RETURN_BUSINESS_QTY | 拒收业务数量 | number(16,6) | Y |  |
| 6 | QC_DATE | 判定日期 | date | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | PO_QC_RESULT_SD_ID | 主键 | GUID | Y | Y |
| 9 | DEDUCT_ARRIVED_QTY | 扣已到货量 | number(0/1) | Y |  |
| 10 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 11 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 12 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 13 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 14 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 15 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 16 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 17 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 18 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 19 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 20 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 21 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 22 | UDF041 | 自定义字段12 | date | Y |  |
| 23 | UDF042 | 自定义字段13 | date | Y |  |
| 24 | UDF051 | 自定义字段14 | GUID | Y |  |
| 25 | UDF052 | 自定义字段15 | GUID | Y |  |
| 26 | UDF053 | 自定义字段16 | GUID | Y |  |
| 27 | UDF054 | 自定义字段17 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
| 29 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 30 | ApproveDate | 修改日期 | date | Y |  |
| 31 | ApproveBy | 修改人 | GUID | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | PO_QC_RESULT_D_ID |  | GUID | Y |  |


### PO_REQ_SOURCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PO_REQ_SOURCE_ID | 主键 | GUID | Y | Y |
| 3 | PURCHASE_ORDER_SD1_ID | 父主键 | GUID | Y |  |
| 4 | DEMAND_QTY | 需求业务数量 | number(16,6) | Y |  |
| 5 | DEMAND_UNIT_ID | 需求业务单位 | GUID | Y |  |
| 6 | DEMAND_DATE | 需求日期 | date | Y |  |
| 7 | PURCHASED_QTY | 已采业务数量 | number(16,6) | Y |  |
| 8 | ARRIVED_QTY | 已到货业务数量 | number(16,6) | Y |  |
| 9 | RECEIPTED_QTY | 已入库业务数量 | number(16,6) | Y |  |
| 10 | PURCHASE_SEQUENCE | 采购核销优先序 | string(400) | Y |  |
| 11 | DEMAND_NO | 需求单号 | string(510) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 15 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 16 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 17 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 18 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 19 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 20 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 21 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 22 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 23 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 24 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 25 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 26 | UDF041 | 自定义字段12 | date | Y |  |
| 27 | UDF042 | 自定义字段13 | date | Y |  |
| 28 | UDF051 | 自定义字段14 | GUID | Y |  |
| 29 | UDF052 | 自定义字段15 | GUID | Y |  |
| 30 | UDF053 | 自定义字段16 | GUID | Y |  |
| 31 | UDF054 | 自定义字段17 | GUID | Y |  |
| 32 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 33 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 34 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 35 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
