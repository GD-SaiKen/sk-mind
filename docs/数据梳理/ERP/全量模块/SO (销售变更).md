---
module: "SO"
name_zh: "销售变更"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 6
columns: 591
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# SO (销售变更)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 6 | Columns: 591

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


- **SO_CHANGE_DOC (销售订单变更单)**
- **SO_CHANGE_DOC_D (销售订单变更单身)**
- **SO_CHANGE_DOC_EXPENSE (订单变更单费用组成)**
- **SO_CHANGE_DOC_INSTAL (订金/分期明细)**
- **SO_CHANGE_DOC_SD (销售订单变更子单身)**
- **SO_PRICE_DETAILS (销售订单价格明细)**


---


---


> Tables: 6

### SO_CHANGE_DOC (销售订单变更单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SO_CHANGE_DOC_ID | 主键 | GUID | Y | Y |
| 4 | SALES_ORDER_DOC_ID | 原订单ID | GUID | Y |  |
| 5 | CHANGE_VERSION | 变更版本 | string(4) | Y |  |
| 6 | DOC_DATE | 单据日期 | date | Y |  |
| 7 | CHANGE_DATE | 变更日期 | date | Y |  |
| 8 | CUSTOMER_ID | 客户 | GUID | Y |  |
| 9 | SETTLEMENT_COMPANY_ID | 结算公司 | GUID | Y |  |
| 10 | CURRENCY_ID | 币种 | GUID | Y |  |
| 11 | EXCHANGE_RATE |  | number(18,9) | Y |  |
| 12 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 13 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 14 | EARNEST_RATE |  | number(5,4) | Y |  |
| 15 | EARNEST | 订金 | number(23,8) | Y |  |
| 16 | CUSTOMER_ADDR_ID | 客户地址 | GUID | Y |  |
| 17 | CUSTOMER_ADDR_NAME | 客户地址名称 | string(510) | Y |  |
| 18 | CUSTOMER_CONTACT_ID | 客户联系人 | GUID | Y |  |
| 19 | CUSTOMER_CONTACT_NAME | 客户联系人名称 | string(72) | Y |  |
| 20 | PARTIAL_DELIVERY | 允许分批交货 | number(0/1) | Y |  |
| 21 | IS_INSTALLMENT | 分期付款 | number(0/1) | Y |  |
| 22 | INSTALLMENT_SOURCE | 分期源单 | string(40) | Y |  |
| 23 | CONTRACT_ID | 合同 | GUID | Y |  |
| 24 | MULTI_DELIVERY | 多收货地址 | number(0/1) | Y |  |
| 25 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 26 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 27 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 28 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 29 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 30 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 31 | INVOICE_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 32 | INVOICE_ADDR_ID | 发票邮寄地址 | GUID | Y |  |
| 33 | INVOICE_ADDR_NAME | 发票邮寄地址名称 | string(510) | Y |  |
| 34 | INVOICE_CONTACT_ID | 发票邮寄联系人 | GUID | Y |  |
| 35 | INVOICE_CONTACT_NAME | 发票邮寄联系人名称 | string(72) | Y |  |
| 36 | TAX_INVOICE_CATEGORY_ID | 发票种类 | GUID | Y |  |
| 37 | CUSTOMER_ORDER_NO | 客户单号 | string(510) | Y |  |
| 38 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 39 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 40 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 41 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 42 | REMARK1 | 备注-业务 | string(510) | Y |  |
| 43 | REMARK2 | 备注-物流 | string(510) | Y |  |
| 44 | REMARK3 | 备注-财务 | string(510) | Y |  |
| 45 | ORI_EXCHANGE_RATE | 原汇率 | number(18,9) | Y |  |
| 46 | ORI_PAYMENT_TERM_ID | 原付款条件 | GUID | Y |  |
| 47 | ORI_EARNEST_RATE | 原订金比率 | number(5,4) | Y |  |
| 48 | ORI_EARNEST | 原订金 | number(23,8) | Y |  |
| 49 | ORI_CUSTOMER_ADDR_ID | 原客户地址 | GUID | Y |  |
| 50 | ORI_CUSTOMER_ADDR_NAME | 原客户地址名称 | string(510) | Y |  |
| 51 | ORI_CUSTOMER_CONTACT_ID | 原客户联系人 | GUID | Y |  |
| 52 | ORI_CUSTOMER_CONTACT_NAME | 原客户联系人名称 | string(72) | Y |  |
| 53 | ORI_PARTIAL_DELIVERY | 原允许分批交货 | number(0/1) | Y |  |
| 54 | ORI_IS_INSTALLMENT | 原分期付款 | number(0/1) | Y |  |
| 55 | ORI_INSTALLMENT_SOURCE | 原分期源单 | string(40) | Y |  |
| 56 | ORI_CONTRACT_ID | 原合同 | GUID | Y |  |
| 57 | ORI_MULTI_DELIVERY | 原多收货地址 | number(0/1) | Y |  |
| 58 | ORI_SHIP_TO_CUSTOMER_ID | 原收货客户 | GUID | Y |  |
| 59 | ORI_SHIP_TO_ADDR_ID | 原收货地址 | GUID | Y |  |
| 60 | ORI_SHIP_TO_ADDR_NAME | 原收货地址名称 | string(510) | Y |  |
| 61 | ORI_SHIP_TO_CONTACT_ID | 原收货联系人 | GUID | Y |  |
| 62 | ORI_SHIP_TO_CONTACT_NAME | 原收货联系人名称 | string(72) | Y |  |
| 63 | ORI_DELIVERY_TERM_ID | 原运输方式 | GUID | Y |  |
| 64 | ORI_PIECES | 原件数 | number | Y |  |
| 65 | ORI_INVOICE_ADDR_ID | 原发票邮寄地址 | GUID | Y |  |
| 66 | ORI_INVOICE_ADDR_NAME | 原发票邮寄地址名称 | string(510) | Y |  |
| 67 | ORI_INVOICE_CONTACT_ID | 原发票邮寄联系人 | GUID | Y |  |
| 68 | ORI_INVOICE_CONTACT_NAME | 原发票邮寄联系人名称 | string(72) | Y |  |
| 69 | ORI_TAX_INVOICE_CATEGORY_ID | 原发票种类 | GUID | Y |  |
| 70 | ORI_CUSTOMER_ORDER_NO | 原客户单号 | string(510) | Y |  |
| 71 | ORI_AMT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 72 | ORI_TAX_OC | 原原币税额 | number(23,8) | Y |  |
| 73 | ORI_AMT_UNINCLUDE_TAX_BC | 原本币未税金额 | number(23,8) | Y |  |
| 74 | ORI_TAX_BC | 原本币税额 | number(23,8) | Y |  |
| 75 | ORI_REMARK1 | 原备注-业务 | string(510) | Y |  |
| 76 | ORI_REMARK2 | 原备注-物流 | string(510) | Y |  |
| 77 | ORI_REMARK3 | 原备注-财务 | string(510) | Y |  |
| 78 | ORI_Owner_Dept | 原销售部门 | GUID | Y |  |
| 79 | ORI_Owner_Emp | 原业务员 | GUID | Y |  |
| 80 | FULL_CLOSE | 整张结束 | number(0/1) | Y |  |
| 81 | CHANGE_CAUSE | 变更原因 | string(510) | Y |  |
| 82 | DOC_ID | 单据类型 | GUID | Y |  |
| 83 | UNLIMITED_RELEASE | 超限放行 | number(0/1) | Y |  |
| 84 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 85 | TAX_ID | 税种 | GUID | Y |  |
| 86 | ORI_CLOSE | 原结束码 | string(40) | Y |  |
| 87 | PROJECT_ID | 限用项目 | GUID | Y |  |
| 88 | ORI_PROJECT_ID | 原限用项目 | GUID | Y |  |
| 89 | PrintCount | 打印次数 | number | Y |  |
| 90 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 91 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 92 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 93 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 94 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 95 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 96 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 97 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 98 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 99 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 100 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 101 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 102 | UDF041 | 自定义字段12 | date | Y |  |
| 103 | UDF042 | 自定义字段13 | date | Y |  |
| 104 | UDF051 | 自定义字段14 | GUID | Y |  |
| 105 | UDF052 | 自定义字段15 | GUID | Y |  |
| 106 | UDF053 | 自定义字段16 | GUID | Y |  |
| 107 | UDF054 | 自定义字段17 | GUID | Y |  |
| 108 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 109 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 110 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 111 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 112 | CreateDate | 创建日期 | date | Y |  |
| 113 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 114 | ModifiedDate | 修改日期 | date | Y |  |
| 115 | CreateBy | 创建者 | GUID | Y |  |
| 116 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 117 | ModifiedBy | 修改者 | GUID | Y |  |
| 118 | Attachments | 附件 | string | Y |  |
| 119 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 120 | Version | 版本号，不要随意更改 | binary | Y |  |
| 121 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 122 | ApproveDate | 修改日期 | date | Y |  |
| 123 | ApproveBy | 修改人 | GUID | Y |  |
| 124 | Owner_Org_RTK |  | string(400) | Y |  |
| 125 | Owner_Org_ROid |  | GUID | Y |  |
| 126 | LOADING_PORT | 起始港口 | string(120) | Y |  |
| 127 | DESTINATION_PORT | 目的港口 | string(120) | Y |  |
| 128 | DESTINATION | 目的地 | string(120) | Y |  |
| 129 | COMMISSION_RATE | 佣金比率 | number(5,4) | Y |  |
| 130 | INVOICE_REMARK | INVOICE备注 | string(510) | Y |  |
| 131 | PACKING_LIST_REMARK | PACKINGLIST备注 | string(510) | Y |  |
| 132 | FRONT_MARK | 正唛 | string(510) | Y |  |
| 133 | FRONT_MARK_IS_PIC | 正唛用图片 | number(0/1) | Y |  |
| 134 | FRONT_MARK_PIC | 正唛图片 | string(120) | Y |  |
| 135 | SIDE_MARK | 侧唛 | string(510) | Y |  |
| 136 | SIDE_MARK_IS_PIC | 侧唛用图片 | number(0/1) | Y |  |
| 137 | SIDE_MARK_PIC | 侧唛图片 | string(120) | Y |  |
| 138 | LETTER_CREDIT_ID | 信用证号码 | GUID | Y |  |
| 139 | AGENT_CUSTOMER_ID | 代理商 | GUID | Y |  |
| 140 | BROKERS_SUPPLIER_ID | 报关行 | GUID | Y |  |
| 141 | INSPECTION_SUPPLIER_ID | 验货公司 | GUID | Y |  |
| 142 | TRANSPORT_SUPPLIER_ID | 运输公司 | GUID | Y |  |
| 143 | CONSIGNEE_CUSTOMER_ID | 进口方收货人信息 | GUID | Y |  |
| 144 | NOTIFY_CUSTOMER_ID | 进口方通知对象信息 | GUID | Y |  |
| 145 | CORRESPONDING_BANK_ID | 往来银行 | GUID | Y |  |
| 146 | NEGOTIATING_BANK_ID | 押汇银行 | GUID | Y |  |
| 147 | CUSTOMER_SHIPPING_MARK_ID | 客户唛头 | GUID | Y |  |
| 148 | BANK_ACCOUNT_ID | 银行账号 | GUID | Y |  |
| 149 | PRICE_TERMS_ID | 价格条款 | GUID | Y |  |
| 150 | ORI_LOADING_PORT | 原起始港口 | string(120) | Y |  |
| 151 | ORI_DESTINATION_PORT | 原目的港口 | string(120) | Y |  |
| 152 | ORI_DESTINATION | 原目的地 | string(120) | Y |  |
| 153 | ORI_COMMISSION_RATE | 原佣金比率 | number(5,4) | Y |  |
| 154 | ORI_INVOICE_REMARK | 原INVOICE备注 | string(510) | Y |  |
| 155 | ORI_PACKING_LIST_REMARK | 原PACKINGLIST备注 | string(510) | Y |  |
| 156 | ORI_FRONT_MARK | 原正唛 | string(510) | Y |  |
| 157 | ORI_FRONT_MARK_IS_PIC | 原正唛用图片 | number(0/1) | Y |  |
| 158 | ORI_FRONT_MARK_PIC | 原正唛图片 | string(120) | Y |  |
| 159 | ORI_SIDE_MARK | 原侧唛 | string(510) | Y |  |
| 160 | ORI_SIDE_MARK_IS_PIC | 原侧唛用图片 | number(0/1) | Y |  |
| 161 | ORI_SIDE_MARK_PIC | 原侧唛图片 | string(120) | Y |  |
| 162 | ORI_LETTER_CREDIT_ID | 原信用证号码 | GUID | Y |  |
| 163 | ORI_AGENT_CUSTOMER_ID | 原代理商 | GUID | Y |  |
| 164 | ORI_BROKERS_SUPPLIER_ID | 原报关行 | GUID | Y |  |
| 165 | ORI_INSPECTION_SUPPLIER_ID | 原验货公司 | GUID | Y |  |
| 166 | ORI_TRANSPORT_SUPPLIER_ID | 原运输公司 | GUID | Y |  |
| 167 | ORI_CONSIGNEE_CUSTOMER_ID | 原进口方收货人信息 | GUID | Y |  |
| 168 | ORI_NOTIFY_CUSTOMER_ID | 原进口方通知对象信息 | GUID | Y |  |
| 169 | ORI_CORRESPONDING_BANK_ID | 原往来银行 | GUID | Y |  |
| 170 | ORI_NEGOTIATING_BANK_ID | 原押汇银行 | GUID | Y |  |
| 171 | ORI_CUSTOMER_SHIPPING_MARK_ID | 原客户唛头 | GUID | Y |  |
| 172 | ORI_BANK_ACCOUNT_ID | 原银行账号 | GUID | Y |  |
| 173 | ORI_PRICE_TERMS_ID | 原价格条款 | GUID | Y |  |
| 174 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 175 | GROUP_SYNERGY_D_ID | 协同序号 | GUID | Y |  |
| 176 | GENERATE_NO | 抛转单号 | string(400) | Y |  |
| 177 | GENERATE_STATUS | 抛转状态 | number(0/1) | Y |  |
| 178 | DOC_Sequence | 单据顺序 | number | Y |  |
| 179 | SOURCE_CUSTOMER_ID | 最终客户 | GUID | Y |  |
| 180 | GROUP_SYNERGY_ID_RTK |  | string(400) | Y |  |
| 181 | GROUP_SYNERGY_ID_ROid |  | GUID | Y |  |
| 182 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 183 | SOURCE_ORDER_ROid |  | GUID | Y |  |

### SO_CHANGE_DOC_D (销售订单变更单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SO_CHANGE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_TYPE | 商品类型 | string(40) | Y |  |
| 4 | ITEM_ID | 品号 | GUID | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_DESCRIPTION |  | string(120) | Y |  |
| 7 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 8 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 9 | BUSINESS_UNIT_ID | 业务单位 | GUID | Y |  |
| 10 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 11 | PRICE_UNIT_ID | 计价单位 | GUID | Y |  |
| 12 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 13 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 14 | PLAN_DELIVERY_DATE | 预交货日 | date | Y |  |
| 15 | PRICE | 单价 | number(23,8) | Y |  |
| 16 | DISCOUNT_RATE | 折扣率 | number(5,4) | Y |  |
| 17 | DISCOUNTED_PRICE | 折扣后单价 | number(23,8) | Y |  |
| 18 | AMOUNT |  | number(23,8) | Y |  |
| 19 | DISCOUNT_AMT | 折扣额 | number(23,8) | Y |  |
| 20 | STANDARD_PRICE | 标准单价 | number(23,8) | Y |  |
| 21 | STANDARD_DISCOUNT_RATE | 标准折扣率 | number(5,4) | Y |  |
| 22 | PRICE_TABLE_ID | 价格表 | GUID | Y |  |
| 23 | DISCOUNT_TABLE_ID | 折扣表 | GUID | Y |  |
| 24 | TAX_ID | 税种 | GUID | Y |  |
| 25 | TAX_RATE |  | number(5,4) | Y |  |
| 26 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 27 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 28 | AMT_UNINCLUDE_TAX_BC | 本币未税金额 | number(23,8) | Y |  |
| 29 | TAX_BC | 本币税额 | number(23,8) | Y |  |
| 30 | PACKING_MODE_ID | 包装方式 | GUID | Y |  |
| 31 | PACKING1_UNIT_ID | 大包装单位 | GUID | Y |  |
| 32 | PACKING2_UNIT_ID | 中包装单位 | GUID | Y |  |
| 33 | PACKING3_UNIT_ID | 小包装单位 | GUID | Y |  |
| 34 | PACKING4_UNIT_ID | 最小包装单位 | GUID | Y |  |
| 35 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 36 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 37 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 38 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 39 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 40 | PIECES |  | number | Y |  |
| 41 | CUSTOMER_ITEM_ID | 客户品号 | GUID | Y |  |
| 42 | REMARK | 备注 | string(510) | Y |  |
| 43 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 44 | SALES_ORDER_DOC_D_ID | 原订单行 | GUID | Y |  |
| 45 | ORI_ITEM_TYPE | 原商品类型 | string(40) | Y |  |
| 46 | ORI_ITEM_ID | 原品号 | GUID | Y |  |
| 47 | ORI_ITEM_FEATURE_ID | 原特征码 | GUID | Y |  |
| 48 | ORI_ITEM_DESCRIPTION | 原品名 | string(120) | Y |  |
| 49 | ORI_ITEM_SPECIFICATION | 原规格 | string(510) | Y |  |
| 50 | ORI_BUSINESS_QTY | 原业务数量 | number(16,6) | Y |  |
| 51 | ORI_BUSINESS_UNIT_ID | 原业务单位 | GUID | Y |  |
| 52 | ORI_PRICE_QTY | 原计价数量 | number(16,6) | Y |  |
| 53 | ORI_PRICE_UNIT_ID | 原计价单位 | GUID | Y |  |
| 54 | ORI_INVENTORY_QTY | 原库存单位数量 | number(16,6) | Y |  |
| 55 | ORI_SECOND_QTY | 原第二数量 | number(16,6) | Y |  |
| 56 | ORI_PLAN_DELIVERY_DATE | 原预交货日 | date | Y |  |
| 57 | ORI_PRICE | 原单价 | number(23,8) | Y |  |
| 58 | ORI_DISCOUNT_RATE | 原折扣率 | number(5,4) | Y |  |
| 59 | ORI_DISCOUNTED_PRICE | 原折扣后单价 | number(23,8) | Y |  |
| 60 | ORI_AMOUNT | 原金额 | number(23,8) | Y |  |
| 61 | ORI_DISCOUNT_AMT | 原折扣额 | number(23,8) | Y |  |
| 62 | ORI_STANDARD_PRICE | 原标准单价 | number(23,8) | Y |  |
| 63 | ORI_STANDARD_DISCOUNT_RATE | 原标准折扣率 | number(5,4) | Y |  |
| 64 | ORI_PRICE_TABLE_ID | 原价格表 | GUID | Y |  |
| 65 | ORI_DISCOUNT_TABLE_ID | 原折扣表 | GUID | Y |  |
| 66 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 67 | ORI_TAX_RATE | 原税率 | number(5,4) | Y |  |
| 68 | ORI_AMT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 69 | ORI_TAX_OC | 原原币税额 | number(23,8) | Y |  |
| 70 | ORI_AMT_UNINCLUDE_TAX_BC | 原本币未税金额 | number(23,8) | Y |  |
| 71 | ORI_TAX_BC | 原本币税额 | number(23,8) | Y |  |
| 72 | ORI_PACKING_MODE_ID | 原包装方式 | GUID | Y |  |
| 73 | ORI_PACKING1_UNIT_ID | 原大包装单位 | GUID | Y |  |
| 74 | ORI_PACKING2_UNIT_ID | 原中包装单位 | GUID | Y |  |
| 75 | ORI_PACKING3_UNIT_ID | 原小包装单位 | GUID | Y |  |
| 76 | ORI_PACKING4_UNIT_ID | 原最小包装单位 | GUID | Y |  |
| 77 | ORI_PACKING_QTY1 | 原大包装数量 | number(16,6) | Y |  |
| 78 | ORI_PACKING_QTY2 | 原中包装数量 | number(16,6) | Y |  |
| 79 | ORI_PACKING_QTY3 | 原小包装数量 | number(16,6) | Y |  |
| 80 | ORI_PACKING_QTY4 | 原最小包装数量 | number(16,6) | Y |  |
| 81 | ORI_PACKING_QTY | 原包装数量描述 | string(240) | Y |  |
| 82 | ORI_PIECES | 原件数 | number | Y |  |
| 83 | ORI_CUSTOMER_ITEM_ID | 原客户品号 | GUID | Y |  |
| 84 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 85 | SO_D_ID | 原订单序号 | GUID | Y |  |
| 86 | CHANGE_CAUSE | 变更原因 | string(510) | Y |  |
| 87 | KIT_DISTRIBUTION | 零组件配送 | number(0/1) | Y |  |
| 88 | ORI_KIT_DISTRIBUTION | 原零组件配送 | number(0/1) | Y |  |
| 89 | PROJECT_ID | 项目 | GUID | Y |  |
| 90 | ORI_PROJECT_ID | 原项目 | GUID | Y |  |
| 91 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 92 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 93 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 94 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 95 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 96 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 97 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 98 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 99 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 100 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 101 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 102 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 103 | UDF041 | 自定义字段12 | date | Y |  |
| 104 | UDF042 | 自定义字段13 | date | Y |  |
| 105 | UDF051 | 自定义字段14 | GUID | Y |  |
| 106 | UDF052 | 自定义字段15 | GUID | Y |  |
| 107 | UDF053 | 自定义字段16 | GUID | Y |  |
| 108 | UDF054 | 自定义字段17 | GUID | Y |  |
| 109 | CreateDate | 创建日期 | date | Y |  |
| 110 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 111 | ModifiedDate | 修改日期 | date | Y |  |
| 112 | CreateBy | 创建者 | GUID | Y |  |
| 113 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 114 | ModifiedBy | 修改者 | GUID | Y |  |
| 115 | Version | 版本号，不要随意更改 | binary | Y |  |
| 116 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 117 | ApproveDate | 修改日期 | date | Y |  |
| 118 | ApproveBy | 修改人 | GUID | Y |  |
| 119 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 120 | SOURCE_ID_ROid |  | GUID | Y |  |
| 121 | ORI_SOURCE_ID_RTK |  | string(400) | Y |  |
| 122 | ORI_SOURCE_ID_ROid |  | GUID | Y |  |
| 123 | SO_CHANGE_DOC_ID |  | GUID | Y |  |
| 124 | GROSS_WEIGHT | 毛重 | number(16,6) | Y |  |
| 125 | VOLUME | 材积 | number(16,6) | Y |  |
| 126 | ORI_GROSS_WEIGHT | 原毛重 | number(16,6) | Y |  |
| 127 | ORI_VOLUME | 原材积 | number(16,6) | Y |  |
| 128 | DEL_SO_D_ID | 原删除序号 | GUID | Y |  |
| 129 | MFG_DESCRIPTION | 生产信息 | string(400) | Y |  |
| 130 | SALES_DESCRIPTION | 销售信息 | string(400) | Y |  |
| 131 | ORI_MFG_DESCRIPTION | 原生产信息 | string(400) | Y |  |
| 132 | ORI_SALES_DESCRIPTION | 原销售信息 | string(400) | Y |  |
| 133 | ORI_DEL_SO_D_ID | 原原删除序号 | GUID | Y |  |
| 134 | PRODUCT_SUB_GROUP_ID | 替代群组主键 | GUID | Y |  |
| 135 | GROUP_ITEM_CODE | 群组品号 | string(80) | Y |  |
| 136 | ORI_PRODUCT_SUB_GROUP_ID | 原替代群组主键 | GUID | Y |  |
| 137 | ORI_GROUP_ITEM_CODE | 原群组品号 | string(80) | Y |  |
| 138 | SOURCE_ORDER_RTK |  | string(400) | Y |  |
| 139 | SOURCE_ORDER_ROid |  | GUID | Y |  |

### SO_CHANGE_DOC_EXPENSE (订单变更单费用组成)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SO_CHANGE_DOC_EXPENSE_ID | 主键 | GUID | Y | Y |
| 3 | AMOUNT | 金额 | number(23,8) | Y |  |
| 4 | CALC_RATE | 比率 | number(5,4) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SETTLEMENT_AMT_UN_TAX_OC | 已结算无税金额(原币) | number(23,8) | Y |  |
| 7 | SETTLEMENT_TAX_OC | 已结算税额(原币) | number(23,8) | Y |  |
| 8 | SETTLEMENT_CLOSE | 结算状态 | string(40) | Y |  |
| 9 | PRICE_TERMS_D_ID | 价格条款明细 | GUID | Y |  |
| 10 | CURRENCY_ID | 币种 | GUID | Y |  |
| 11 | ORI_AMOUNT | 金额 | number(23,8) | Y |  |
| 12 | ORI_CALC_RATE | 比率 | number(5,4) | Y |  |
| 13 | ORI_CURRENCY_ID | 币种 | GUID | Y |  |
| 14 | SALES_ORDER_DOC_EXPENSE_ID | 原序号 | GUID | Y |  |
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
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | SO_CHANGE_DOC_ID |  | GUID | Y |  |

### SO_CHANGE_DOC_INSTAL (订金/分期明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SO_CHANGE_DOC_INSTAL_ID | 主键 | GUID | Y | Y |
| 3 | SALES_ORDER_DOC_INSTAL_ID | 原序号 | GUID | Y |  |
| 4 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 5 | INSTALLMENT_NAME |  | string(60) | Y |  |
| 6 | INSTALLMENT_RATE | 分期比率 | number(5,4) | Y |  |
| 7 | INSTALLMENT_AMT_OC | 原币分期金额 | number(23,8) | Y |  |
| 8 | PAYMENT_BASE_DATE_S | 基准日来源 | number | Y |  |
| 9 | PAYMENT_BASE_DATE | 基准日 | date | Y |  |
| 10 | PAYMENT_TERM_ID | 付款条件 | GUID | Y |  |
| 11 | PAYMENT_DATE | 付款日 | date | Y |  |
| 12 | CASHING_DATE | 兑现日 | date | Y |  |
| 13 | CASH_DISCOUNT_MODE | 现金折扣方式 | number | Y |  |
| 14 | CASH_DISCOUNT_RATE1 | 现金折扣率1 | number(5,4) | Y |  |
| 15 | CASH_DISCOUNT_DUE_DATE1 | 现金折扣到期日1 | date | Y |  |
| 16 | CASH_DISCOUNT_RATE2 | 现金折扣率2 | number(5,4) | Y |  |
| 17 | CASH_DISCOUNT_DUE_DATE2 | 现金折扣到期日2 | date | Y |  |
| 18 | CASH_DISCOUNT_RATE3 | 现金折扣率3 | number(5,4) | Y |  |
| 19 | CASH_DISCOUNT_DUE_DATE3 | 现金折扣到期日3 | date | Y |  |
| 20 | CARRY_OUT_DATE | 执行日期 | date | Y |  |
| 21 | INSTALLMENT_TYPE | 分期类型 | string(40) | Y |  |
| 22 | TAX_ID | 税种 | GUID | Y |  |
| 23 | TAX_RATE |  | number(5,4) | Y |  |
| 24 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 25 | AMT_UNINCLUDE_TAX_OC | 原币未税金额 | number(23,8) | Y |  |
| 26 | TAX_OC | 原币税额 | number(23,8) | Y |  |
| 27 | ORI_INSTALLMENT_NAME | 原分期名称 | string(60) | Y |  |
| 28 | ORI_INSTALLMENT_RATE | 原分期比率 | number(5,4) | Y |  |
| 29 | ORI_INSTALLMENT_AMT_OC | 原原币分期金额 | number(23,8) | Y |  |
| 30 | ORI_PAYMENT_BASE_DATE_S | 原基准日来源 | number | Y |  |
| 31 | ORI_PAYMENT_BASE_DATE | 原基准日 | date | Y |  |
| 32 | ORI_PAYMENT_TERM_ID | 原付款条件 | GUID | Y |  |
| 33 | ORI_PAYMENT_DATE | 原付款日 | date | Y |  |
| 34 | ORI_CASHING_DATE | 原兑现日 | date | Y |  |
| 35 | ORI_CASH_DISCOUNT_MODE | 原现金折扣方式 | number | Y |  |
| 36 | ORI_CASH_DISCOUNT_RATE1 | 原现金折扣率1 | number(5,4) | Y |  |
| 37 | ORI_CASH_DISCOUNT_DUE_DATE1 | 原现金折扣到期日1 | date | Y |  |
| 38 | ORI_CASH_DISCOUNT_RATE2 | 原现金折扣率2 | number(5,4) | Y |  |
| 39 | ORI_CASH_DISCOUNT_DUE_DATE2 | 原现金折扣到期日2 | date | Y |  |
| 40 | ORI_CASH_DISCOUNT_RATE3 | 原现金折扣率3 | number(5,4) | Y |  |
| 41 | ORI_CASH_DISCOUNT_DUE_DATE3 | 原现金折扣到期日3 | date | Y |  |
| 42 | ORI_CARRY_OUT_DATE | 原执行日期 | date | Y |  |
| 43 | ORI_INSTALLMENT_TYPE | 原分期类型 | string(40) | Y |  |
| 44 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 45 | ORI_TAX_RATE | 原税率 | number(5,4) | Y |  |
| 46 | ORI_TAX_INCLUDED | 原含税 | number(0/1) | Y |  |
| 47 | ORI_AMT_UNINCLUDE_TAX_OC | 原原币未税金额 | number(23,8) | Y |  |
| 48 | ORI_TAX_OC | 原原币税额 | number(23,8) | Y |  |
| 49 | REMARK | 备注 | string(510) | Y |  |
| 50 | ORI_REMARK | 备注 | string(510) | Y |  |
| 51 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 52 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 53 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 54 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 55 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 56 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 57 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 58 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 59 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 60 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 61 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 62 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 63 | UDF041 | 自定义字段12 | date | Y |  |
| 64 | UDF042 | 自定义字段13 | date | Y |  |
| 65 | UDF051 | 自定义字段14 | GUID | Y |  |
| 66 | UDF052 | 自定义字段15 | GUID | Y |  |
| 67 | UDF053 | 自定义字段16 | GUID | Y |  |
| 68 | UDF054 | 自定义字段17 | GUID | Y |  |
| 69 | CreateDate | 创建日期 | date | Y |  |
| 70 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 71 | ModifiedDate | 修改日期 | date | Y |  |
| 72 | CreateBy | 创建者 | GUID | Y |  |
| 73 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 74 | ModifiedBy | 修改者 | GUID | Y |  |
| 75 | Version | 版本号，不要随意更改 | binary | Y |  |
| 76 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 77 | ApproveDate | 修改日期 | date | Y |  |
| 78 | ApproveBy | 修改人 | GUID | Y |  |
| 79 | SO_CHANGE_DOC_ID |  | GUID | Y |  |

### SO_CHANGE_DOC_SD (销售订单变更子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SO_CHANGE_DOC_SD_ID | 主键 | GUID | Y | Y |
| 3 | SHIP_TO_CUSTOMER_ID | 收货客户 | GUID | Y |  |
| 4 | SHIP_TO_ADDR_ID | 收货地址 | GUID | Y |  |
| 5 | SHIP_TO_ADDR_NAME | 收货地址名称 | string(510) | Y |  |
| 6 | SHIP_TO_CONTACT_ID | 收货联系人 | GUID | Y |  |
| 7 | SHIP_TO_CONTACT_NAME | 收货联系人名称 | string(72) | Y |  |
| 8 | DELIVERY_TERM_ID | 运输方式 | GUID | Y |  |
| 9 | BUSINESS_QTY | 业务数量 | number(16,6) | Y |  |
| 10 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 11 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 12 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 13 | PLAN_DELIVERY_DATE | 预交货日 | date | Y |  |
| 14 | PLAN_SHIP_DATE | 预发货日 | date | Y |  |
| 15 | DELIVERY_TYPE | 供货类型 | string(40) | Y |  |
| 16 | DELIVERY_PLANT_ID | 发货工厂 | GUID | Y |  |
| 17 | DELIVERY_WAREHOUSE_ID | 发货仓库 | GUID | Y |  |
| 18 | SYNERGY_ID | 协同关系 | GUID | Y |  |
| 19 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 20 | DIRECT_SHIP | 直运 | number(0/1) | Y |  |
| 21 | PACKING_QTY1 | 大包装数量 | number(16,6) | Y |  |
| 22 | PACKING_QTY2 | 中包装数量 | number(16,6) | Y |  |
| 23 | PACKING_QTY3 | 小包装数量 | number(16,6) | Y |  |
| 24 | PACKING_QTY4 | 最小包装数量 | number(16,6) | Y |  |
| 25 | PACKING_QTY | 包装数量描述 | string(240) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | PIECES |  | number | Y |  |
| 28 | CHANGE_TYPE | 变更类型 | string(40) | Y |  |
| 29 | SALES_ORDER_DOC_SD_ID | 原订单发货计划 | GUID | Y |  |
| 30 | ORI_SHIP_TO_CUSTOMER_ID | 原收货客户 | GUID | Y |  |
| 31 | ORI_SHIP_TO_ADDR_ID | 原收货地址 | GUID | Y |  |
| 32 | ORI_SHIP_TO_ADDR_NAME | 原收货地址名称 | string(510) | Y |  |
| 33 | ORI_SHIP_TO_CONTACT_ID | 原收货联系人 | GUID | Y |  |
| 34 | ORI_SHIP_TO_CONTACT_NAME | 原收货联系人名称 | string(72) | Y |  |
| 35 | ORI_DELIVERY_TERM_ID | 原运输方式 | GUID | Y |  |
| 36 | ORI_BUSINESS_QTY | 原业务数量 | number(16,6) | Y |  |
| 37 | ORI_PRICE_QTY | 原计价数量 | number(16,6) | Y |  |
| 38 | ORI_INVENTORY_QTY | 原库存单位数量 | number(16,6) | Y |  |
| 39 | ORI_SECOND_QTY | 原第二数量 | number(16,6) | Y |  |
| 40 | ORI_PLAN_DELIVERY_DATE | 原预交货日 | date | Y |  |
| 41 | ORI_PLAN_SHIP_DATE | 原预发货日 | date | Y |  |
| 42 | ORI_DELIVERY_TYPE | 原供货类型 | string(40) | Y |  |
| 43 | ORI_DELIVERY_PLANT_ID | 原发货工厂 | GUID | Y |  |
| 44 | ORI_DELIVERY_WAREHOUSE_ID | 原发货仓库 | GUID | Y |  |
| 45 | ORI_SYNERGY_ID | 原协同关系 | GUID | Y |  |
| 46 | ORI_SUPPLY_CENTER_ID | 原采购域 | GUID | Y |  |
| 47 | ORI_DIRECT_SHIP | 原直运 | number(0/1) | Y |  |
| 48 | ORI_PACKING_QTY1 | 原大包装数量 | number(16,6) | Y |  |
| 49 | ORI_PACKING_QTY2 | 原中包装数量 | number(16,6) | Y |  |
| 50 | ORI_PACKING_QTY3 | 原小包装数量 | number(16,6) | Y |  |
| 51 | ORI_PACKING_QTY4 | 原最小包装数量 | number(16,6) | Y |  |
| 52 | ORI_PACKING_QTY | 原包装数量描述 | string(240) | Y |  |
| 53 | ORI_DELIVERED_BUSINESS_QTY | 原已交业务数量 | number(16,6) | Y |  |
| 54 | ORI_DELIVERED_PRICE_QTY | 原已交计价数量 | number(16,6) | Y |  |
| 55 | ORI_CLOSE | 原结束码 | string(40) | Y |  |
| 56 | ORI_PLAN_STATUS | 原计划状态 | string(40) | Y |  |
| 57 | ORI_RESERVED_BUSINESS_QTY | 原已保留业务数量 | number(16,6) | Y |  |
| 58 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 59 | ORI_PIECES | 原件数 | number | Y |  |
| 60 | SO_SD_ID | 原订单次序号 | GUID | Y |  |
| 61 | ORI_BIN_ID | 原库位 | GUID | Y |  |
| 62 | KIT_WAREHOUSE_ID | 零组件接收仓库 | GUID | Y |  |
| 63 | ORI_KIT_WAREHOUSE_ID | 原零组件接收仓库 | GUID | Y |  |
| 64 | BIN_ID | 库位 | GUID | Y |  |
| 65 | SETT_COMPANY_ID | 采购结算公司 | GUID | Y |  |
| 66 | ORI_SETT_COMPANY_ID | 原采购结算公司 | GUID | Y |  |
| 67 | ESTI_PAYMENT_DATE | 预计付款日 | date | Y |  |
| 68 | ORI_ESTI_PAYMENT_DATE | 原预计付款日 | date | Y |  |
| 69 | IS_INDEPENDENT_DEMAND | 独立需求 | number(0/1) | Y |  |
| 70 | ORI_IS_INDPT_DEMAND | 原独立需求 | number(0/1) | Y |  |
| 71 | PROJECT_ID | 项目 | GUID | Y |  |
| 72 | ORI_PROJECT_ID | 原项目 | GUID | Y |  |
| 73 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 74 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 75 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 76 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 77 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 78 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 79 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 80 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 81 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 82 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 83 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 84 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 85 | UDF041 | 自定义字段12 | date | Y |  |
| 86 | UDF042 | 自定义字段13 | date | Y |  |
| 87 | UDF051 | 自定义字段14 | GUID | Y |  |
| 88 | UDF052 | 自定义字段15 | GUID | Y |  |
| 89 | UDF053 | 自定义字段16 | GUID | Y |  |
| 90 | UDF054 | 自定义字段17 | GUID | Y |  |
| 91 | CreateDate | 创建日期 | date | Y |  |
| 92 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 93 | ModifiedDate | 修改日期 | date | Y |  |
| 94 | CreateBy | 创建者 | GUID | Y |  |
| 95 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 96 | ModifiedBy | 修改者 | GUID | Y |  |
| 97 | Version | 版本号，不要随意更改 | binary | Y |  |
| 98 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 99 | ApproveDate | 修改日期 | date | Y |  |
| 100 | ApproveBy | 修改人 | GUID | Y |  |
| 101 | DELIVERY_PARTNER_ID_RTK |  | string(400) | Y |  |
| 102 | DELIVERY_PARTNER_ID_ROid |  | GUID | Y |  |
| 103 | ORI_DELIVERY_PARTNER_RTK |  | string(400) | Y |  |
| 104 | ORI_DELIVERY_PARTNER_ROid |  | GUID | Y |  |
| 105 | SYNERGY_SOURCE_ID_RTK |  | string(400) | Y |  |
| 106 | SYNERGY_SOURCE_ID_ROid |  | GUID | Y |  |
| 107 | ORI_SYN_SOURCE_ID_RTK |  | string(400) | Y |  |
| 108 | ORI_SYN_SOURCE_ID_ROid |  | GUID | Y |  |
| 109 | SO_CHANGE_DOC_D_ID |  | GUID | Y |  |
| 110 | PMC_STATUS | 任务执行状态 | string(40) | Y |  |
| 111 | INCLUDE_PLAN | 纳入计划 | number(0/1) | Y |  |
| 112 | TRANSACTION_PLANT_ID | 交易工厂 | GUID | Y |  |

### SO_PRICE_DETAILS (销售订单价格明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SO_PRICE_DETAILS_ID | 主键 | GUID | Y | Y |
| 3 | PRICE | 价格 | number(23,8) | Y |  |
| 4 | CALC_RATE | 比率 | number(5,4) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | PRICE_TERMS_D_ID | 价格条款明细 | GUID | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | SALES_ORDER_DOC_D_ID |  | GUID | Y |  |