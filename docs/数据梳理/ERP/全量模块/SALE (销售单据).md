---
module: "SALE"
name_zh: "销售单据"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 23
columns: 1019
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52

---

# SALE (销售单据)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599

> Tables: 23 | Columns: 1019

## Related Modules

- [[BEHALF (代销业务)|BEHALF (代销业务)]]
- [[BILL (账单促销)|BILL (账单促销)]]
- [[CALL (叫货管理)|CALL (叫货管理)]]
- [[CONTRACT (合同管理)|CONTRACT (合同管理)]]
- [[COUNTER (柜台交易)|COUNTER (柜台交易)]]
- [[CST (报关管理)|CST (报关管理)]]
- [[DELIVERY (交货条款)|DELIVERY (交货条款)]]
- [[DIRECT (直运业务)|DIRECT (直运业务)]]

---

## Tables


- **SALE_CARD_DOC**
- **SALE_CARD_DOC_D (售卡单单身)**
- **SALE_CARD_DOC_PAYTYPE**
- **SALE_DEFECTIVE_AI**
- **SALE_DEFECTIVE_VI**
- **SALE_INSPECTION (销退检验单)**
- **SALE_INSPECTION_D**
- **SALE_INSPECTION_D1**
- **SALE_INSPECTION_SD**
- **SALE_PAYTYPE (通用收款方式信息)**
- **SALE_PRICE_TABLE (价格表)**
- **SALE_PRICE_TABLE_D (价格表单身)**
- **SALE_PRICE_TABLE_SHOP**
- **SALE_QC_RESULT (销退质检业务)**
- **SALE_QC_RESULT_D (销退检验信息)**
- **SALE_QC_RESULT_SD (销退业务判定信息)**
- **SALE_RETURN_CARD_DOC**
- **SALE_RETURN_CARD_DOC_D**
- **SALE_RETURN_TICKET_DOC (售券退券单)**
- **SALE_RETURN_TICKET_DOC_D (售券退券单单身)**
- **SALE_TICKET_DOC (售券单)**
- **SALE_TICKET_DOC_D**
- **SALE_TICKET_DOC_PAYTYPE (会员积分换购收款)**


---


---


> Tables: 23

### SALE_CARD_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SALE_CARD_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | DATA_SOURCE_TYPE | 数据来源 | string(40) | Y |  |
| 10 | SHOP_ID | 门店 | GUID | Y |  |
| 11 | NUM_SUM | 售卡数量 | number(16,6) | Y |  |
| 12 | AMOUNT_SUM | 售卡金额 | number(23,8) | Y |  |
| 13 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 14 | CUSTOMER_BUSINESS_ID | 客户 | GUID | Y |  |
| 15 | CURRENCY_ID | 币种 | GUID | Y |  |
| 16 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | AMOUNT_NO_TAX | 无税金额 | number(23,8) | Y |  |
| 19 | AMOUNT_TAX | 税额 | number(23,8) | Y |  |
| 20 | POS_ID | POS机号 | GUID | Y |  |
| 21 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 22 | CNL_FLAG | 卡数量余额计算标志 | number(0/1) | Y |  |
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
| 41 | PrintCount | 打印次数 | number | Y |  |
| 42 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 43 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 44 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 45 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | Attachments | 附件 | string | Y |  |
| 53 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 54 | Version | 版本号，不要随意更改 | binary | Y |  |
| 55 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 56 | ApproveDate | 修改日期 | date | Y |  |
| 57 | ApproveBy | 修改人 | GUID | Y |  |
| 58 | Owner_Org_RTK |  | string(400) | Y |  |
| 59 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_CARD_DOC_D (售卡单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_CARD_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | CARD_ID | 卡ID | GUID | Y |  |
| 4 | CARD_FACE_VALUE | 卡面值 | number(23,8) | Y |  |
| 5 | CARD_SALE_PRICE | 卡售价 | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | TAX_ID | 税种 | GUID | Y |  |
| 8 | TAX_RATE |  | number(5,4) | Y |  |
| 9 | CARD_SALE_NOT_TAX | 无税金额 | number(23,8) | Y |  |
| 10 | CARD_SALE_TAX | 税额 | number(23,8) | Y |  |
| 11 | BEGIN_CARD_CODE | 开始卡号 | string(40) | Y |  |
| 12 | END_CARD_CODE | 结束卡号 | string(40) | Y |  |
| 13 | CARD_NUM | 数量 | number(16,6) | Y |  |
| 14 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | SALE_CARD_DOC_ID |  | GUID | Y |  |

### SALE_CARD_DOC_PAYTYPE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | E_SALE_CARD_DOC_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 3 | PAYTYPE_ID | 付款方式 | GUID | Y |  |
| 4 | PAY_AMOUNT | 付款金额 | number(23,8) | Y |  |
| 5 | PAY_TYPE | 付款方式 | number | Y |  |
| 6 | CT_TYPE | 卡券类型 | number | Y |  |
| 7 | CT_ID | 卡ID/券ID | GUID | Y |  |
| 8 | CT_CODE | 卡号/券号 | string(80) | Y |  |
| 9 | CT_ENCRYPT_KEY | 卡内号 | string(80) | Y |  |
| 10 | EXTRA | 溢收 | number(23,8) | Y |  |
| 11 | CHANGED | 找零金额 | number(23,8) | Y |  |
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
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | SALE_CARD_DOC_ID |  | GUID | Y |  |

### SALE_DEFECTIVE_AI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_DEFECTIVE_AI_ID |  | GUID | Y | Y |
| 3 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 4 | DEFECTS | 不合格数 | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
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
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | SALE_INSPECTION_D_ID |  | GUID | Y |  |

### SALE_DEFECTIVE_VI

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALE_DEFECTIVE_VI_ID | 主键 | GUID | Y | Y |
| 2 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 3 | DEFECTS | 不合格数 | number(16,6) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | SALE_INSPECTION_D1_ID |  | GUID | Y |  |

### SALE_INSPECTION (销退检验单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALE_INSPECTION_ID | 主键 | GUID | Y | Y |
| 7 | INSPECTION_TIMES | 最大抽样次数 | string(40) | Y |  |
| 8 | INSPECTION_DATE | 检验日期 | date | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | ITEM_ID | 品号 | GUID | Y |  |
| 11 | ITEM_DESCRIPTION | 品名 | string(120) | Y |  |
| 12 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 13 | ITEM_SPECIFICATION | 规格 | string(510) | Y |  |
| 14 | ITEM_LOT_ID | 批号 | GUID | Y |  |
| 15 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 16 | SOURCE_ID | 源单 | GUID | Y |  |
| 17 | INSPECTION_QTY | 送检数量 | number(16,6) | Y |  |
| 18 | INSPECTION_UNIT_ID | 品管单位 | GUID | Y |  |
| 19 | STRICTNESS_DEGREE | 宽严程度 | string(40) | Y |  |
| 20 | INSPECTION_DUE_DATE | 送检日期 | date | Y |  |
| 21 | ADMIN_UNIT_ID | 送检部门 | GUID | Y |  |
| 22 | EMPLOYEE_ID | 送检人员 | GUID | Y |  |
| 23 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 24 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 25 | ACCEPTABLE_QTY | 合格数量 | number(16,6) | Y |  |
| 26 | UNQUALIFIED_QTY | 不合格数量 | number(16,6) | Y |  |
| 27 | DESTROYED_QTY | 破坏数量 | number(16,6) | Y |  |
| 28 | DECISION_DESCRIPTION | 判定说明 | string(510) | Y |  |
| 29 | RESULT_STATUS | 业务判定状态 | string(40) | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | INSPECTION_PLAN_ID | 质检方案 | GUID | Y |  |
| 32 | COMPANY_ID | 公司 | GUID | Y |  |
| 33 | PROJECT_ID | 项目 | GUID | Y |  |
| 34 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 35 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 36 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 37 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 38 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 39 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 40 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 41 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 42 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 43 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 44 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 45 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 46 | UDF041 | 自定义字段12 | date | Y |  |
| 47 | UDF042 | 自定义字段13 | date | Y |  |
| 48 | UDF051 | 自定义字段14 | GUID | Y |  |
| 49 | UDF052 | 自定义字段15 | GUID | Y |  |
| 50 | UDF053 | 自定义字段16 | GUID | Y |  |
| 51 | UDF054 | 自定义字段17 | GUID | Y |  |
| 52 | PrintCount | 打印次数 | number | Y |  |
| 53 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 54 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 55 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 56 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 57 | Version | 版本号，不要随意更改 | binary | Y |  |
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | Attachments | 附件 | string | Y |  |
| 65 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |
| 69 | Owner_Org_RTK |  | string(400) | Y |  |
| 70 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_INSPECTION_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALE_INSPECTION_D_ID |  | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 4 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 5 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 6 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 7 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 8 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 9 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
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
| 36 | SALE_INSPECTION_ID |  | GUID | Y |  |

### SALE_INSPECTION_D1

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALE_INSPECTION_D1_ID |  | GUID | Y | Y |
| 2 | SEQUENCE | 检验顺序 | number | Y |  |
| 3 | INSPECTION_ITEM_ID | 检验项目 | GUID | Y |  |
| 4 | DEFECT_CLASS | 缺点等级 | string(40) | Y |  |
| 5 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 6 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 7 | ACCEPTANCE_CONSTANT | 接收常数k | number(16,6) | Y |  |
| 8 | SS | 样本标准差S | number(16,6) | Y |  |
| 9 | XX | 平均值X | number(16,6) | Y |  |
| 10 | UU | 标准上限 | number(16,6) | Y |  |
| 11 | LL | 标准下限 | number(16,6) | Y |  |
| 12 | QU | 质量QU | number(16,6) | Y |  |
| 13 | QL | 质量QL | number(16,6) | Y |  |
| 14 | DEFECTIVE_REASONS_ID | 不良原因 | GUID | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
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
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | SALE_INSPECTION_ID |  | GUID | Y |  |

### SALE_INSPECTION_SD

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALE_INSPECTION_SD_ID | 主键 | GUID | Y | Y |
| 2 | INSPECTION_QTY | 抽样数量 | number(16,6) | Y |  |
| 3 | INSPECTION_QQ | 不良数量 | number(16,6) | Y |  |
| 4 | INSPECTION_AC | 允收数量Ac | number(16,6) | Y |  |
| 5 | INSPECTION_RE | 拒收数量Re | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | INSPECTION_TIME | 检验次数 | number | Y |  |
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
| 33 | SALE_INSPECTION_D_ID |  | GUID | Y |  |

### SALE_PAYTYPE (通用收款方式信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALE_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 4 | SALE_PAYTYPE_CODE | 收款方式编号 | string(80) | Y |  |
| 5 | SALE_PAYTYPE_NAME | 收款方式名称 | string(80) | Y |  |
| 6 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 7 | BANK_FEE_RATE | 银行卡手续费率 | number(12,4) | Y |  |
| 8 | CASH_MANAGE | 钱箱管理 | number(0/1) | Y |  |
| 9 | ALLOW_CHANGE | 能否找零 | number(0/1) | Y |  |
| 10 | ALLOW_EXTEND | 能否超额支付 | number(0/1) | Y |  |
| 11 | HAND_CASH | 超额强制解款 | number(0/1) | Y |  |
| 12 | HAND_CASH_VALUE | 强制解款额 | number(12,2) | Y |  |
| 13 | WARNING | 超额钱箱报警 | number(0/1) | Y |  |
| 14 | WARNING_VALUE | 报警额 | number(12,2) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
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
| 41 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | Owner_Org_RTK |  | string(400) | Y |  |
| 47 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_PRICE_TABLE (价格表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALE_PRICE_TABLE_ID | 主键 | GUID | Y | Y |
| 4 | SALE_PRICE_TABLE_CODE | 价格表编号 | string(80) | Y |  |
| 5 | SALE_PRICE_TABLE_NAME | 价格表名称 | string(200) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Attachments | 附件 | string | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_PRICE_TABLE_D (价格表单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_PRICE1 | 会员价1 | number(23,8) | Y |  |
| 3 | MEMBER_PRICE2 | 会员价2 | number(23,8) | Y |  |
| 4 | MEMBER_PRICE3 | 会员价3 | number(23,8) | Y |  |
| 5 | MEMBER_PRICE4 | 会员价4 | number(23,8) | Y |  |
| 6 | MEMBER_PRICE5 | 会员价5 | number(23,8) | Y |  |
| 7 | MEMBER_PRICE6 | 会员价6 | number(23,8) | Y |  |
| 8 | SALE_PRICE_DOC_NO | 变价单号 | string(40) | Y |  |
| 9 | PRICE | 零售价 | number(23,8) | Y |  |
| 10 | MIN_PRICE | 零售最低价 | number(23,8) | Y |  |
| 11 | MAX_PRICE | 零售最高退货价 | number(23,8) | Y |  |
| 12 | BEGIN_DATE | 开始日期 | date | Y |  |
| 13 | UNIT_ID | 交易单位 | GUID | Y |  |
| 14 | ITEM_ID | 品号 | GUID | Y |  |
| 15 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 16 | SALE_PRICE_TABLE_D_ID | 主键 | GUID | Y | Y |
| 17 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | Version | 版本号，不要随意更改 | binary | Y |  |
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | SALE_PRICE_TABLE_ID |  | GUID | Y |  |

### SALE_PRICE_TABLE_SHOP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | SALE_PRICE_TABLE_SHOP_ID | 主键 | GUID | Y | Y |
| 5 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 6 | SHOP_ID | 门店 | GUID | Y |  |
| 7 | ITEM_ID | 品号 | GUID | Y |  |
| 8 | UNIT_ID | 交易单位 | GUID | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 11 | BEGIN_DATE | 开始日期 | date | Y |  |
| 12 | PRICE | 零售价 | number(23,8) | Y |  |
| 13 | MIN_PRICE | 零售最低价 | number(23,8) | Y |  |
| 14 | MAX_PRICE | 零售最高退货价 | number(23,8) | Y |  |
| 15 | MEMBER_PRICE1 | 会员价1 | number(23,8) | Y |  |
| 16 | MEMBER_PRICE2 | 会员价2 | number(23,8) | Y |  |
| 17 | MEMBER_PRICE3 | 会员价3 | number(23,8) | Y |  |
| 18 | MEMBER_PRICE4 | 会员价4 | number(23,8) | Y |  |
| 19 | MEMBER_PRICE5 | 会员价5 | number(23,8) | Y |  |
| 20 | MEMBER_PRICE6 | 会员价6 | number(23,8) | Y |  |
| 21 | SALE_PRICE_DOC_NO | 变价单号 | string(40) | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Attachments | 附件 | string | Y |  |
| 30 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 31 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 32 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 33 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 34 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 35 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 36 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 37 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 38 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 39 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 40 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 41 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 42 | UDF041 | 自定义字段12 | date | Y |  |
| 43 | UDF042 | 自定义字段13 | date | Y |  |
| 44 | UDF051 | 自定义字段14 | GUID | Y |  |
| 45 | UDF052 | 自定义字段15 | GUID | Y |  |
| 46 | UDF053 | 自定义字段16 | GUID | Y |  |
| 47 | UDF054 | 自定义字段17 | GUID | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Owner_Org_RTK |  | string(400) | Y |  |
| 54 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_QC_RESULT (销退质检业务)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SALE_QC_RESULT_ID | 主键 | GUID | Y | Y |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 6 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 7 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 8 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 9 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 10 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 11 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 12 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 13 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 14 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 15 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 16 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 17 | UDF041 | 自定义字段12 | date | Y |  |
| 18 | UDF042 | 自定义字段13 | date | Y |  |
| 19 | UDF051 | 自定义字段14 | GUID | Y |  |
| 20 | UDF052 | 自定义字段15 | GUID | Y |  |
| 21 | UDF053 | 自定义字段16 | GUID | Y |  |
| 22 | UDF054 | 自定义字段17 | GUID | Y |  |
| 23 | Attachments | 附件 | string | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
| 25 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 26 | ApproveDate | 修改日期 | date | Y |  |
| 27 | ApproveBy | 修改人 | GUID | Y |  |
| 28 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Owner_Org_RTK |  | string(400) | Y |  |
| 36 | Owner_Org_ROid |  | GUID | Y |  |
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |

### SALE_QC_RESULT_D (销退检验信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SALE_QC_RESULT_D_ID | 主键 | GUID | Y | Y |
| 2 | SALE_INSPECTION_ID | 检验单 | GUID | Y |  |
| 3 | SALE_INSPECTION_CODE | 检验单号 | string(40) | Y |  |
| 4 | QC_DATE | 检验日期 | date | Y |  |
| 5 | QUALIFIED_BUSINESS_QTY | 合格业务数量 | number(16,6) | Y |  |
| 6 | UNQUALIFIED_BUSINESS_QTY | 不合格业务数量 | number(16,6) | Y |  |
| 7 | IN_DESTROYED_BUSINESS_QTY | 检验破坏业务数量 | number(16,6) | Y |  |
| 8 | DETERMINE_QTY | 待判定业务数量 | number(16,6) | Y |  |
| 9 | RESULT_STATUS | 业务判定状态 | string(40) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
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
| 36 | SALE_QC_RESULT_ID |  | GUID | Y |  |

### SALE_QC_RESULT_SD (销退业务判定信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_QC_RESULT_SD_ID | 主键 | GUID | Y | Y |
| 3 | ACCEPTED_BUSINESS_QTY | 允收业务数量 | number(16,6) | Y |  |
| 4 | SP_RECEIPT_BUSINESS_QTY | 让步接收业务数量 | number(16,6) | Y |  |
| 5 | SCRAP_BUSINESS_QTY | 报废业务数量 | number(16,6) | Y |  |
| 6 | QC_DATE | 判定日期 | date | Y |  |
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
| 27 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 28 | ApproveDate | 修改日期 | date | Y |  |
| 29 | ApproveBy | 修改人 | GUID | Y |  |
| 30 | CreateDate | 创建日期 | date | Y |  |
| 31 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 32 | ModifiedDate | 修改日期 | date | Y |  |
| 33 | CreateBy | 创建者 | GUID | Y |  |
| 34 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 35 | ModifiedBy | 修改者 | GUID | Y |  |
| 36 | SALE_QC_RESULT_D_ID |  | GUID | Y |  |

### SALE_RETURN_CARD_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SALE_RETURN_CARD_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | DATA_SOURCE_TYPE | 数据来源 | string(40) | Y |  |
| 10 | SALE_CARD_DOC_ID | 售卡单单号 | GUID | Y |  |
| 11 | SHOP_ID | 门店 | GUID | Y |  |
| 12 | NUM_SUM | 退卡数量 | number(16,6) | Y |  |
| 13 | AMOUNT_SUM | 退卡金额 | number(23,8) | Y |  |
| 14 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 15 | CUSTOMER_BUSINESS_ID | 客户 | GUID | Y |  |
| 16 | CURRENCY_ID | 币种 | GUID | Y |  |
| 17 | TAX_ID | 税种 | GUID | Y |  |
| 18 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 19 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | AMOUNT_NO_TAX | 无税金额 | number(23,8) | Y |  |
| 22 | AMOUNT_TAX | 税额 | number(23,8) | Y |  |
| 23 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 24 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 25 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 26 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 27 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 28 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 29 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 30 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 31 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 32 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 33 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 34 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 35 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 36 | UDF041 | 自定义字段12 | date | Y |  |
| 37 | UDF042 | 自定义字段13 | date | Y |  |
| 38 | UDF051 | 自定义字段14 | GUID | Y |  |
| 39 | UDF052 | 自定义字段15 | GUID | Y |  |
| 40 | UDF053 | 自定义字段16 | GUID | Y |  |
| 41 | UDF054 | 自定义字段17 | GUID | Y |  |
| 42 | PrintCount | 打印次数 | number | Y |  |
| 43 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 44 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 45 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 46 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | Attachments | 附件 | string | Y |  |
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_RETURN_CARD_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_RETURN_CARD_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | CARD_ID | 卡ID | GUID | Y |  |
| 4 | CARD_FACE_VALUE | 卡面值 | number(23,8) | Y |  |
| 5 | CARD_SALE_PRICE | 卡售价 | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | TAX_ID | 税种 | GUID | Y |  |
| 8 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 9 | CARD_SALE_NOT_TAX | 无税金额 | number(23,8) | Y |  |
| 10 | CARD_SALE_TAX | 税额 | number(23,8) | Y |  |
| 11 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 12 | BEGIN_CARD_CODE | 开始卡号 | string(40) | Y |  |
| 13 | END_CARD_CODE | 结束卡号 | string(40) | Y |  |
| 14 | CARD_NUM | 数量 | number(16,6) | Y |  |
| 15 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 16 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 17 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 18 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 19 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 20 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 21 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 22 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 23 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 24 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 25 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 26 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 27 | UDF041 | 自定义字段12 | date | Y |  |
| 28 | UDF042 | 自定义字段13 | date | Y |  |
| 29 | UDF051 | 自定义字段14 | GUID | Y |  |
| 30 | UDF052 | 自定义字段15 | GUID | Y |  |
| 31 | UDF053 | 自定义字段16 | GUID | Y |  |
| 32 | UDF054 | 自定义字段17 | GUID | Y |  |
| 33 | CreateDate | 创建日期 | date | Y |  |
| 34 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 35 | ModifiedDate | 修改日期 | date | Y |  |
| 36 | CreateBy | 创建者 | GUID | Y |  |
| 37 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 38 | ModifiedBy | 修改者 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | SALE_RETURN_CARD_DOC_ID |  | GUID | Y |  |

### SALE_RETURN_TICKET_DOC (售券退券单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALE_RETURN_TICKET_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | DATA_SOURCE_TYPE | 数据来源 | string(40) | Y |  |
| 10 | SHOP_ID | 门店 | GUID | Y |  |
| 11 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 12 | CUSTOMER_BUSINESS_ID | 客户 | GUID | Y |  |
| 13 | PAYMENT_TERM_ID | 付款方式 | GUID | Y |  |
| 14 | CURRENCY_ID | 币种 | GUID | Y |  |
| 15 | TAX_ID | 税种 | GUID | Y |  |
| 16 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 17 | TICKET_NUM | 退券数量 | number(16,6) | Y |  |
| 18 | TICKET_AMOUNT | 退券金额 | number(23,8) | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | SALE_TICKET_DOC_ID | 售券单号 | GUID | Y |  |
| 21 | AMOUNT_NO_TAX | 无税金额 | number(23,8) | Y |  |
| 22 | AMOUNT_TAX | 税额 | number(23,8) | Y |  |
| 23 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 24 | HAND_NO | 手工单号 | string(200) | Y |  |
| 25 | PrintCount | 打印次数 | number | Y |  |
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
| 44 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 45 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 46 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 47 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | Attachments | 附件 | string | Y |  |
| 55 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 56 | Version | 版本号，不要随意更改 | binary | Y |  |
| 57 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 58 | ApproveDate | 修改日期 | date | Y |  |
| 59 | ApproveBy | 修改人 | GUID | Y |  |
| 60 | Owner_Org_RTK |  | string(400) | Y |  |
| 61 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_RETURN_TICKET_DOC_D (售券退券单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_RETURN_TICKET_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | TICKET_ID | 券号 | GUID | Y |  |
| 4 | TICKET_FACE_VALUE_ID | 券面值 | GUID | Y |  |
| 5 | TICKET_SALE_PRICE | 券售价 | number(23,8) | Y |  |
| 6 | TICKET_DISCOUNT | 券折扣 | number(5,4) | Y |  |
| 7 | TICKET_NUM |  | number(16,6) | Y |  |
| 8 | TICKET_AMOUNT | 券金额 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | TICKET_FACE_VALUE | 券面额 | number(23,8) | Y |  |
| 11 | TICKET_GROUP_ID | 券类型 | GUID | Y |  |
| 12 | TAX_ID | 税种 | GUID | Y |  |
| 13 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 14 | TICKET_AMOUNT_NO_TAX | 无税金额 | number(23,8) | Y |  |
| 15 | TICKET_AMOUNT_TAX | 税额 | number(23,8) | Y |  |
| 16 | BEGIN_TICKET_CODE | 开始券号 | string(80) | Y |  |
| 17 | END_TICKET_CODE | 结束券号 | string(80) | Y |  |
| 18 | DISCOUNT | 折扣 | number(5,4) | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | SALE_RETURN_TICKET_DOC_ID |  | GUID | Y |  |

### SALE_TICKET_DOC (售券单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SALE_TICKET_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | DATA_SOURCE_TYPE | 数据来源 | string(4) | Y |  |
| 10 | SHOP_ID | 门店 | GUID | Y |  |
| 11 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 12 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 13 | PAYMENT_TERM_ID | 付款方式 | GUID | Y |  |
| 14 | CURRENCY_ID | 币种 | GUID | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | TICKET_NUM | 券数量 | number(16,6) | Y |  |
| 17 | AMOUNT_SUM | 券金额 | number(23,8) | Y |  |
| 18 | AMOUNT_NO_TAX | 无税金额 | number(23,8) | Y |  |
| 19 | AMOUNT_TAX | 税额 | number(23,8) | Y |  |
| 20 | TNL_FLAG | 券数量余额计算标志 | number(0/1) | Y |  |
| 21 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 22 | HAND_NO | 手工单号 | string(40) | Y |  |
| 23 | PICKUP_DATE | 取货时间 | date | Y |  |
| 24 | PrintCount | 打印次数 | number | Y |  |
| 25 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 26 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 27 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 28 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 47 | CreateDate | 创建日期 | date | Y |  |
| 48 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 49 | ModifiedDate | 修改日期 | date | Y |  |
| 50 | CreateBy | 创建者 | GUID | Y |  |
| 51 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 52 | ModifiedBy | 修改者 | GUID | Y |  |
| 53 | Attachments | 附件 | string | Y |  |
| 54 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 55 | Version | 版本号，不要随意更改 | binary | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |

### SALE_TICKET_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_TICKET_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | TICKET_ID | 券号 | GUID | Y |  |
| 4 | TICKET_FACE_VALUE_ID | 券面值ID | GUID | Y |  |
| 5 | TICKET_SALE_PRICE | 券售价 | number(23,8) | Y |  |
| 6 | TICKET_DISCOUNT | 券折扣 | number(5,4) | Y |  |
| 7 | TICKET_NUM |  | number(16,6) | Y |  |
| 8 | TICKET_AMOUNT | 券金额 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | TICKET_GROUP_ID | 券类型 | GUID | Y |  |
| 11 | TAX_ID | 税种 | GUID | Y |  |
| 12 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 13 | TICKET_AMOUNT_NO_TAX | 无税金额 | number(23,8) | Y |  |
| 14 | TICKET_AMOUNT_TAX | 税额 | number(23,8) | Y |  |
| 15 | TICKET_FACE_VALUE | 券面额 | number(23,8) | Y |  |
| 16 | BEGIN_TICKET_CODE | 开始券号 | string(80) | Y |  |
| 17 | END_TICKET_CODE | 结束券号 | string(80) | Y |  |
| 18 | DISCOUNT | 销售折扣 | number(5,4) | Y |  |
| 19 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 20 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 21 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 22 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 23 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 24 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 25 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 26 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 27 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 28 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 29 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 30 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 31 | UDF041 | 自定义字段12 | date | Y |  |
| 32 | UDF042 | 自定义字段13 | date | Y |  |
| 33 | UDF051 | 自定义字段14 | GUID | Y |  |
| 34 | UDF052 | 自定义字段15 | GUID | Y |  |
| 35 | UDF053 | 自定义字段16 | GUID | Y |  |
| 36 | UDF054 | 自定义字段17 | GUID | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | SALE_TICKET_DOC_ID |  | GUID | Y |  |

### SALE_TICKET_DOC_PAYTYPE (会员积分换购收款)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALE_TICKET_DOC_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 3 | SALE_PAYTYPE_ID | 付款方式 | GUID | Y |  |
| 4 | PAY_AMOUNT | 付款金额 | number(23,8) | Y |  |
| 5 | PAY_TYPE | 付款方式 | string(40) | Y |  |
| 6 | CT_TYPE | 卡券类型 | number | Y |  |
| 7 | CT_ID | 卡ID/券ID | GUID | Y |  |
| 8 | CT_CODE | 卡号/券号 | string(80) | Y |  |
| 9 | CT_ENCRYPT_KEY | 卡内号 | string(80) | Y |  |
| 10 | EXTRA | 溢收 | number(23,8) | Y |  |
| 11 | CHANGED | 找零金额 | number(23,8) | Y |  |
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
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | SALE_TICKET_DOC_ID |  | GUID | Y |  |