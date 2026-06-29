---
module: "LETTER"
name_zh: "信用证"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 4
columns: 207
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# LETTER (信用证)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 4 | Columns: 207

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


- **LETTER_CREDIT (信用证信息)**
- **LETTER_CREDIT_CHANGE (信用证变更信息)**
- **LETTER_CREDIT_CHANGE_D (信用证变更订单信息)**
- **LETTER_CREDIT_D (信用证订单信息)**


---


---


> Tables: 4

### LETTER_CREDIT (信用证信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | LETTER_CREDIT_ID | 主键 | GUID | Y | Y |
| 4 | LC_NO | 信用证号码 | string(40) | Y |  |
| 5 | CUSTOMER_ID | 主键 | GUID | Y |  |
| 6 | PARTIAL_SHIPMENT | 可分批 | number(0/1) | Y |  |
| 7 | TRANSHIPMENT | 可转运 | number(0/1) | Y |  |
| 8 | LICENSE_NO | 许可证号码 | string(40) | Y |  |
| 9 | ISSUE_BANK_ID | 开证银行 | GUID | Y |  |
| 10 | ADVISING_BANK_ID | 通知银行 | GUID | Y |  |
| 11 | NEGOTIATING_BANK_ID | 押汇银行 | GUID | Y |  |
| 12 | ISSUE_DATE | 开证日 | date | Y |  |
| 13 | RECEIVE_DATE | 收到日 | date | Y |  |
| 14 | LATEST_SHIPPING_DATE | 最晚装船日 | date | Y |  |
| 15 | LATEST_NEGOTIATING_DATE | 最晚押汇日 | date | Y |  |
| 16 | DUE_DATE | 到期日 | date | Y |  |
| 17 | CURRENCY_ID | 币种 | GUID | Y |  |
| 18 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 19 | AMT_LC | 总金额 | number(23,8) | Y |  |
| 20 | AMT_NEGOTIATING | 押汇金额 | number(23,8) | Y |  |
| 21 | AMT_SO | 订单金额 | number(23,8) | Y |  |
| 22 | LC_CLOSE | 结束 | number(0/1) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
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

### LETTER_CREDIT_CHANGE (信用证变更信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | LETTER_CREDIT_CHANGE_ID | 主键 | GUID | Y | Y |
| 4 | LC_NO | 信用证号码 | string(40) | Y |  |
| 5 | CHANGE_VERSION | 变更版本 | string(4) | Y |  |
| 6 | PARTIAL_SHIPMENT | 可分批 | number(0/1) | Y |  |
| 7 | TRANSHIPMENT | 可转运 | number(0/1) | Y |  |
| 8 | LICENSE_NO | 许可证号码 | string(40) | Y |  |
| 9 | ISSUE_DATE | 开证日 | date | Y |  |
| 10 | CHANGE_DATE | 变更日期 | date | Y |  |
| 11 | RECEIVE_DATE | 收到日 | date | Y |  |
| 12 | LATEST_SHIPPING_DATE | 最晚装船日 | date | Y |  |
| 13 | LATEST_NEGOTIATING_DATE | 最晚押汇日 | date | Y |  |
| 14 | DUE_DATE | 到期日 | date | Y |  |
| 15 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 16 | AMT_LC | 总金额 | number(23,8) | Y |  |
| 17 | AMT_NEGOTIATING | 押汇金额 | number(23,8) | Y |  |
| 18 | AMT_SO | 订单金额 | number(23,8) | Y |  |
| 19 | LC_CLOSE | 结束 | number(0/1) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | NEGOTIATING_BANK_ID | 押汇银行 | GUID | Y |  |
| 22 | ORI_PARTIAL_SHIPMENT | 原可分批 | number(0/1) | Y |  |
| 23 | ORI_TRANSHIPMENT | 原可转运 | number(0/1) | Y |  |
| 24 | ORI_LICENSE_NO | 原许可证号码 | string(40) | Y |  |
| 25 | ORI_ISSUE_DATE | 原开证日 | date | Y |  |
| 26 | ORI_RECEIVE_DATE | 原收到日 | date | Y |  |
| 27 | ORI_LATEST_SHIPPING_DATE | 原最晚装船日 | date | Y |  |
| 28 | ORI_LATEST_NEGOTIATING_DATE | 原最晚押汇日 | date | Y |  |
| 29 | ORI_DUE_DATE | 原到期日 | date | Y |  |
| 30 | ORI_EXCHANGE_RATE | 原汇率 | number(18,9) | Y |  |
| 31 | ORI_AMT_LC | 原总金额 | number(23,8) | Y |  |
| 32 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 33 | ORI_CUSTOMER_ID | 原客户 | GUID | Y |  |
| 34 | ORI_CURRENCY_ID | 原币种 | GUID | Y |  |
| 35 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 36 | ISSUE_BANK_ID | 开证银行 | GUID | Y |  |
| 37 | ADVISING_BANK_ID | 通知银行 | GUID | Y |  |
| 38 | CURRENCY_ID | 币种 | GUID | Y |  |
| 39 | ORI_ISSUE_BANK_ID | 原开证银行 | GUID | Y |  |
| 40 | ORI_ADVISING_BANK_ID | 原通知银行 | GUID | Y |  |
| 41 | ORI_NEGOTIATING_BANK_ID | 原押汇银行 | GUID | Y |  |
| 42 | ORI_Owner_Emp | 原业务人员 | GUID | Y |  |
| 43 | ORI_Owner_Dept | 原业务部门 | GUID | Y |  |
| 44 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 45 | LETTER_CREDIT_ID | 原信用证主键 | GUID | Y |  |
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
| 64 | PrintCount | 打印次数 | number | Y |  |
| 65 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 66 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 67 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 68 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 69 | CreateDate | 创建日期 | date | Y |  |
| 70 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 71 | ModifiedDate | 修改日期 | date | Y |  |
| 72 | CreateBy | 创建者 | GUID | Y |  |
| 73 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 74 | ModifiedBy | 修改者 | GUID | Y |  |
| 75 | Attachments | 附件 | string | Y |  |
| 76 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 77 | Version | 版本号，不要随意更改 | binary | Y |  |
| 78 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 79 | ApproveDate | 修改日期 | date | Y |  |
| 80 | ApproveBy | 修改人 | GUID | Y |  |
| 81 | Owner_Org_RTK |  | string(400) | Y |  |
| 82 | Owner_Org_ROid |  | GUID | Y |  |

### LETTER_CREDIT_CHANGE_D (信用证变更订单信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | LETTER_CREDIT_CHANGE_D_ID | 主键 | GUID | Y | Y |
| 3 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 4 | LETTER_CREDIT_D_ID | 原信用证序号 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 7 | ORI_SALES_ORDER_DOC_ID | 原订单单号 | GUID | Y |  |
| 8 | SALES_ORDER_DOC_ID | 订单单号 | GUID | Y |  |
| 9 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 10 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 11 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 12 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 13 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 14 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 15 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 16 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 17 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 18 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 19 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 20 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 21 | UDF041 | 自定义字段12 | date | Y |  |
| 22 | UDF042 | 自定义字段13 | date | Y |  |
| 23 | UDF051 | 自定义字段14 | GUID | Y |  |
| 24 | UDF052 | 自定义字段15 | GUID | Y |  |
| 25 | UDF053 | 自定义字段16 | GUID | Y |  |
| 26 | UDF054 | 自定义字段17 | GUID | Y |  |
| 27 | CreateDate | 创建日期 | date | Y |  |
| 28 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 29 | ModifiedDate | 修改日期 | date | Y |  |
| 30 | CreateBy | 创建者 | GUID | Y |  |
| 31 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 32 | ModifiedBy | 修改者 | GUID | Y |  |
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | LETTER_CREDIT_CHANGE_ID |  | GUID | Y |  |

### LETTER_CREDIT_D (信用证订单信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SALES_ORDER_DOC_ID | 订单单号 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | LETTER_CREDIT_D_ID | 主键 | GUID | Y | Y |
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
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | LETTER_CREDIT_ID |  | GUID | Y |  |