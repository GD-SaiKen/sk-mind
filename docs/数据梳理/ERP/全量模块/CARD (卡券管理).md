---
module: "CARD"
name_zh: "卡券管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 29
columns: 1249
category: crm
tags: ["ERP", "E10", "crm"]
created: 2026-06-25 10:52
---

# CARD (卡券管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 29 | Columns: 1249

## Related Modules

- [[BP (业务伙伴)|BP (业务伙伴)]]
- [[CRM (客户关系)|CRM (客户关系)]]
- [[CUSTOMER (客户管理)|CUSTOMER (客户管理)]]
- [[MEMBER (会员管理)|MEMBER (会员管理)]]
- [[REPAIR (维修管理)|REPAIR (维修管理)]]
- [[REPLACE (替换管理)|REPLACE (替换管理)]]
- [[SERVICE (售后服务)|SERVICE (售后服务)]]
- [[TICKET (票券管理)|TICKET (票券管理)]]

---

## Tables


- **CARD_FREEZE_LIST**
- **CARD_GROUP (卡类型信息)**
- **CARD_GROUP_OC_D (卡类型所属营运域)**
- **CARD_GROUP_PAY_DISCOUNT (卡类型品类折扣)**
- **CARD_LOG (写卡日志)**
- **CARD_MAINTAIN_DOC (卡维护单)**
- **CARD_MODIFY_DETAIL (卡异动明细)**
- **CARD_MODIFY_DOC (卡异动单)**
- **CARD_MONEY_DETAIL (卡金额明细)**
- **CARD_NUM_BAL (卡数量余额档)**
- **CARD_PROPORTION_RATE (卡类型租户分摊比率)**
- **CARD_PROPORTION_RENTER**
- **CARD_RECHARGE_DOC**
- **CARD_RECHARGE_DOC_ITEM**
- **CARD_RECHARGE_DOC_PAYTYPE**
- **CARD_RECHARGE_DOC_TICKET**
- **CARD_RECHARGE_ITEM (卡充值赠品)**
- **CARD_RECHARGE_ITEM_SD (卡充值赠品列表)**
- **CARD_RECHARGE_LADDER (卡充值阶梯赠送)**
- **CARD_RECHARGE_RULE (卡充值策略)**
- **CARD_RECHARGE_SHOP (卡充值策略生效门店列表)**
- **CARD_RECHARGE_TICKET (卡充值赠券)**
- **CARD_REPLACE_REASON (换卡原因)**
- **CARD_TRANSACTION_DETAIL (维护卡交易明细)**
- **CARD_TRANSFER_DOC (卡移转单)**
- **CARD_TRANSFER_DOC_D (卡移转单单身)**
- **CARD_TRANSFER_DOC_DIFF (卡移转确认差异)**
- **CARD_WITHHOLD_DOC (维护卡扣款信息)**


---


---


> Tables: 29

### CARD (卡信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CARD_ID | 主键 | GUID | Y | Y |
| 4 | CARD_CODE | 卡号 | string(40) | Y |  |
| 5 | CARD_FACE_VALUE | 卡面额 | number(23,8) | Y |  |
| 6 | CARD_SALE_PRICE | 卡售价 | number(23,8) | Y |  |
| 7 | CARD_AMOUNT | 卡余额 | number(23,8) | Y |  |
| 8 | CARD_AMOUNT_HASHCODE | 卡余额校验码 | string(80) | Y |  |
| 9 | CARD_TYPE | 卡类别 | string(40) | Y |  |
| 10 | CARD_STATUS | 卡状态 | string(40) | Y |  |
| 11 | CARD_ENCRYPT_KEY | 卡加密号 | string(200) | Y |  |
| 12 | CARD_PASSWORD | 用户密码 | string(200) | Y |  |
| 13 | VALID_DATE | 有效日期 | date | Y |  |
| 14 | USE_VALID | 启用有效期控制 | number(0/1) | Y |  |
| 15 | CARD_CATEGORY | 卡种 | string(40) | Y |  |
| 16 | TOTAL_RECHARGE_MONEY | 累计充值金额 | number(23,8) | Y |  |
| 17 | TOTAL_FACE_VALUE | 累计面额 | number(23,8) | Y |  |
| 18 | ACCRUED_RATE | 增值比率 | number(5,4) | Y |  |
| 19 | MAKE_DATE | 制卡日期 | date | Y |  |
| 20 | MAKE_DOC_NO | 制卡单号 | string(40) | Y |  |
| 21 | SEND_DATE | 发卡日期 | date | Y |  |
| 22 | SEND_DOC_NO | 发卡单号 | string(40) | Y |  |
| 23 | REPLACE_DATE | 换卡日期 | date | Y |  |
| 24 | REPLACE_DOC_NO | 换卡单号 | string(40) | Y |  |
| 25 | RETURN_DATE | 退卡日期 | date | Y |  |
| 26 | RETURN_DOC_NO | 退卡单号 | string(40) | Y |  |
| 27 | REMARK | 备注 | string(510) | Y |  |
| 28 | CURRENT_SHOP | 主键 | GUID | Y |  |
| 29 | INIT_SHOP | 主键 | GUID | Y |  |
| 30 | CARD_GROUP_ID | 主键 | GUID | Y |  |
| 31 | CURRENT_OC_ID | 主键 | GUID | Y |  |
| 32 | MAKE_USER | 制卡人 | GUID | Y |  |
| 33 | SEND_USER | 发卡人 | GUID | Y |  |
| 34 | REPLACE_USER | 换卡人 | GUID | Y |  |
| 35 | RETURN_USER | 退卡人 | GUID | Y |  |
| 36 | ENCRYPT_KEY | 系统加密密钥 | string(80) | Y |  |
| 37 | IC_CARD_SN | IC卡序号(唯一) | string(80) | Y |  |
| 38 | CURRENT_SC_ID | 当前所在销售域 | GUID | Y |  |
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Attachments | 附件 | string | Y |  |
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
| 64 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 67 | ApproveDate | 修改日期 | date | Y |  |
| 68 | ApproveBy | 修改人 | GUID | Y |  |
| 69 | Owner_Org_RTK |  | string(400) | Y |  |
| 70 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_FREEZE_LIST

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CARD_FREEZE_LIST_ID | 主键 | GUID | Y | Y |
| 2 | CARD_ID | 卡ID | GUID | Y |  |
| 3 | CARD_CODE | 卡号 | string(80) | Y |  |
| 4 | CARD_STATUS | 卡状态 | string(40) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
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
| 31 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |

### CARD_GROUP (卡类型信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CARD_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | CARD_GROUP_CODE | 卡类型编号 | string(40) | Y |  |
| 5 | CARD_GROUP_NAME | 卡类型名称 | string(400) | Y |  |
| 6 | CARD_TYPE | 卡类别 | string(40) | Y |  |
| 7 | CARD_FACE_VALUE | 卡面额 | number(23,8) | Y |  |
| 8 | CARD_SALE_PRICE | 卡售价 | number(23,8) | Y |  |
| 9 | IS_RECHARGE | 可充值 | string(40) | Y |  |
| 10 | IS_REPORT_LOSS | 可挂失 | number(0/1) | Y |  |
| 11 | IS_POINT | 可积分 | number(0/1) | Y |  |
| 12 | IS_REPLACE | 可换卡 | number(0/1) | Y |  |
| 13 | RETURN_CALC_TYPE | 退卡计算方式 | string(40) | Y |  |
| 14 | CARD_BACK_RATE | 退卡金额比率 | number(5,4) | Y |  |
| 15 | RETURN_ABSORB_RATE | 退货吸收比率 | number(5,4) | Y |  |
| 16 | CARD_CODE_START | 卡号开头 | string(40) | Y |  |
| 17 | CARD_CODE_LENGTH | 卡号长度 | number | Y |  |
| 18 | VALID_DAYS | 有效期 | number | Y |  |
| 19 | USE_VALID_DAYS | 启用有效期控制 | number(0/1) | Y |  |
| 20 | CARD_CATEGORY | 卡种 | string(40) | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | IS_RETURN_BACK | 可退卡 | number(0/1) | Y |  |
| 23 | USE_PASSWORD | 密码管理 | number(0/1) | Y |  |
| 24 | CURRENCY_ID | 主键 | GUID | Y |  |
| 25 | TAX_ID | 税种 | GUID | Y |  |
| 26 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 27 | RECHARGE_DELAY | 充值延长有效期 | number(0/1) | Y |  |
| 28 | RECHARGE_DELAY_TYPE | 充值延长方式 | number | Y |  |
| 29 | RECHARGE_DELAY_DAYS | 充值延长天数 | number | Y |  |
| 30 | ITEM_GROUP_TYPE | 品类支付折扣方式 | string(40) | Y |  |
| 31 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Attachments | 附件 | string | Y |  |
| 39 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 40 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 41 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 42 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 43 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 44 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 45 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 46 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 47 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 48 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 49 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 50 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 51 | UDF041 | 自定义字段12 | date | Y |  |
| 52 | UDF042 | 自定义字段13 | date | Y |  |
| 53 | UDF051 | 自定义字段14 | GUID | Y |  |
| 54 | UDF052 | 自定义字段15 | GUID | Y |  |
| 55 | UDF053 | 自定义字段16 | GUID | Y |  |
| 56 | UDF054 | 自定义字段17 | GUID | Y |  |
| 57 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | Owner_Org_RTK |  | string(400) | Y |  |
| 63 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_GROUP_OC_D (卡类型所属营运域)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_GROUP_OC_D_ID | 主键 | GUID | Y | Y |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | OPERATION_CENTER_ID | 主键 | GUID | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | CARD_GROUP_ID |  | GUID | Y |  |

### CARD_GROUP_PAY_DISCOUNT (卡类型品类折扣)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_GROUP_PAY_DISCOUNT_ID | 主键 | GUID | Y | Y |
| 3 | DISCOUNT |  | number(5,4) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | ITEM_BRAND_FUTURE | 品牌属性 | GUID | Y |  |
| 6 | ITEM_CATEGORY_FUTURE | 分类属性 | GUID | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | CARD_GROUP_ID |  | GUID | Y |  |

### CARD_LOG (写卡日志)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | CARD_LOG_ID | 主键 | GUID | Y | Y |
| 5 | CARD_CODE | 卡号 | string(40) | Y |  |
| 6 | HAPPEN_CODE | 卡交易识别码 | string(40) | Y |  |
| 7 | HAPPEN_TYPE | 发生类型 | string(40) | Y |  |
| 8 | HAPPEN_DATE | 发生日期 | date | Y |  |
| 9 | OPERATE_TYPE | 操作类型 | string(40) | Y |  |
| 10 | BEFORE_EXPIRED_DATE | 修改前卡到期日 | date | Y |  |
| 11 | BEFORE_CARD_STATUS | 修改前卡状态 | string(4) | Y |  |
| 12 | BEFORE_CARD_AMOUNT | 修改前卡余额 | number(23,8) | Y |  |
| 13 | BEFORE_CARD_CORPUS | 修改前卡本金 | number(23,8) | Y |  |
| 14 | BEFORE_CARD_CHANGE_AMOUNT | 修改前卡异动金额 | number(23,8) | Y |  |
| 15 | BEFORE_CARD_CHANGE_BAL | 修改前卡异动后金额 | number(23,8) | Y |  |
| 16 | BEFORE_CARD_HAPPEN_CODE | 修改前卡交易识别码 | string(40) | Y |  |
| 17 | DOC_NO | 单号 | string(40) | Y |  |
| 18 | HAPPEN_MONEY | 发生金额 | number(23,8) | Y |  |
| 19 | HAPPEN_BAL | 发生后余额 | number(23,8) | Y |  |
| 20 | HAPPEN_CORPUS | 发生后本金 | number(23,8) | Y |  |
| 21 | HAPPEN_CARD_STATUS | 发生后卡状态 | string(4) | Y |  |
| 22 | EXPIRED_DATE | 修改后卡到期日 | date | Y |  |
| 23 | SHOP_CODE | 门店编号 | string(80) | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
| 25 | STATUS | 状态 | string(40) | Y |  |
| 26 | POS_ID | POS机台 | GUID | Y |  |
| 27 | CLASS_ID | 班次 | number | Y |  |
| 28 | SHOP_ID | 门店ID | GUID | Y |  |
| 29 | PrintCount | 打印次数 | number | Y |  |
| 30 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 31 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 32 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 33 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 52 | CreateDate | 创建日期 | date | Y |  |
| 53 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 54 | ModifiedDate | 修改日期 | date | Y |  |
| 55 | CreateBy | 创建者 | GUID | Y |  |
| 56 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 57 | ModifiedBy | 修改者 | GUID | Y |  |
| 58 | Attachments | 附件 | string | Y |  |
| 59 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_MAINTAIN_DOC (卡维护单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CARD_MAINTAIN_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | CARD_ID | 卡ID | GUID | Y |  |
| 10 | CARD_CODE | 卡号 | string(80) | Y |  |
| 11 | CARD_AMOUNT | 卡余额 | number(23,8) | Y |  |
| 12 | CARD_LOCAL_AMOUNT | 卡面余额 | number(23,8) | Y |  |
| 13 | CARD_LOCAL_HAPPEN_MONEY | 卡面异动金额 | number(23,8) | Y |  |
| 14 | CARD_LOCAL_HAPPEN_BAL | 卡面异动后余额 | number(23,8) | Y |  |
| 15 | HAPPEN_MONEY | 异动金额 | number(23,8) | Y |  |
| 16 | HAPPEN_BAL | 异动后余额 | number(23,8) | Y |  |
| 17 | CARD_TRANSACTION_DETAIL_ID | 卡交易明细ID | GUID | Y |  |
| 18 | HAPPEN_CODE | 交易识别码 | string(40) | Y |  |
| 19 | HAPPEN_TYPE | 发生类型 | string(40) | Y |  |
| 20 | HAPPEN_DATE | 发生日期 | date | Y |  |
| 21 | POS_ID | POS机台 | GUID | Y |  |
| 22 | PrintCount | 打印次数 | number | Y |  |
| 23 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 24 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 25 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 26 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 27 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 28 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 29 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 30 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 31 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 32 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 33 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 34 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 35 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 36 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 37 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 38 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 39 | UDF041 | 自定义字段12 | date | Y |  |
| 40 | UDF042 | 自定义字段13 | date | Y |  |
| 41 | UDF051 | 自定义字段14 | GUID | Y |  |
| 42 | UDF052 | 自定义字段15 | GUID | Y |  |
| 43 | UDF053 | 自定义字段16 | GUID | Y |  |
| 44 | UDF054 | 自定义字段17 | GUID | Y |  |
| 45 | CreateDate | 创建日期 | date | Y |  |
| 46 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 47 | ModifiedDate | 修改日期 | date | Y |  |
| 48 | CreateBy | 创建者 | GUID | Y |  |
| 49 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 50 | ModifiedBy | 修改者 | GUID | Y |  |
| 51 | Attachments | 附件 | string | Y |  |
| 52 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 53 | Version | 版本号，不要随意更改 | binary | Y |  |
| 54 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 55 | ApproveDate | 修改日期 | date | Y |  |
| 56 | ApproveBy | 修改人 | GUID | Y |  |
| 57 | Owner_Org_RTK |  | string(400) | Y |  |
| 58 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_MODIFY_DETAIL (卡异动明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_MODIFY_DETAIL_ID | 主键 | GUID | Y | Y |
| 3 | MODIFY_TYPE | 卡异动类型 | string(40) | Y |  |
| 4 | CARD_ID | 主键 | GUID | Y |  |
| 5 | MODIFY_DATE | 发生时间 | date | Y |  |
| 6 | MODIFY_DOC_NO |  | string(40) | Y |  |
| 7 | REMARK |  | string(510) | Y |  |
| 8 | RESON_REMARK | 异动原因 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |

### CARD_MODIFY_DOC (卡异动单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | CARD_MODIFY_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | CARD_MODIFY_TYPE | 卡异动类型 | string(40) | Y |  |
| 9 | CARD_ID | 卡号 | GUID | Y |  |
| 10 | RESON_REMARK | 异动原因 | string(510) | Y |  |
| 11 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 12 | SHOP_ID | 门店 | GUID | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | DATA_SOURCE_TYPE | 数据来源 | string(40) | Y |  |
| 15 | POS_ID | POS机号 | GUID | Y |  |
| 16 | CLASS_ID | 班次ID | number | Y |  |
| 17 | MEMBER_ID | 会员ID | GUID | Y |  |
| 18 | PrintCount | 打印次数 | number | Y |  |
| 19 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 20 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 21 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 22 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 41 | CreateDate | 创建日期 | date | Y |  |
| 42 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 43 | ModifiedDate | 修改日期 | date | Y |  |
| 44 | CreateBy | 创建者 | GUID | Y |  |
| 45 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 46 | ModifiedBy | 修改者 | GUID | Y |  |
| 47 | Attachments | 附件 | string | Y |  |
| 48 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 49 | Version | 版本号，不要随意更改 | binary | Y |  |
| 50 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 51 | ApproveDate | 修改日期 | date | Y |  |
| 52 | ApproveBy | 修改人 | GUID | Y |  |
| 53 | Owner_Org_RTK |  | string(400) | Y |  |
| 54 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_MONEY_DETAIL (卡金额明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_MONEY_DETAIL_ID | 主键 | GUID | Y | Y |
| 3 | HAPPEN_TYPE | 发生类型 | string(40) | Y |  |
| 4 | CARD_ID | 主键 | GUID | Y |  |
| 5 | HAPPEN_DATE | 发生日期 | date | Y |  |
| 6 | DOC_NO |  | string(40) | Y |  |
| 7 | HAPPEN_MONEY |  | number(23,8) | Y |  |
| 8 | REMARK |  | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
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
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |

### CARD_NUM_BAL (卡数量余额档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_NUM_BAL_ID | 主键 | GUID | Y | Y |
| 3 | CARD_GROUP_ID | 主键 | GUID | Y |  |
| 4 | CARD_STATUS | 卡状态 | string(4) | Y |  |
| 5 | CARD_NUM |  | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | ORG_TYPE | 机构类型 | string(40) | Y |  |
| 8 | ORG_ID | 机构 | GUID | Y |  |
| 9 | DOC_DATE | 日期 | date | Y |  |
| 10 | DATA_SOURCE_TYPE | 数据来源 | string(400) | Y |  |
| 11 | SOURCE_DOC_NO | 来源单号 | string(400) | Y |  |
| 12 | SOURCE_SERIALNO | 来源序号 | string(400) | Y |  |
| 13 | ACTION_TYPE | 发生类型 | number | Y |  |
| 14 | ACTION_DIRECTION | 发生方向 | number | Y |  |
| 15 | BEGIN_CARD_CODE | 开始卡号 | string(40) | Y |  |
| 16 | END_CARD_CODE | 结束卡号 | string(40) | Y |  |
| 17 | CARD_FACE_VALUE | 卡面值 | number(23,8) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |

### CARD_PROPORTION_RATE (卡类型租户分摊比率)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CARD_PROPORTION_RATE_ID | 主键 | GUID | Y | Y |
| 4 | IS_BASE | 基准 | number(0/1) | Y |  |
| 5 | CARD_GROUP_ID | 主键 | GUID | Y |  |
| 6 | RENTER_RANGE | 生效租户范围 | string(40) | Y |  |
| 7 | BEGIN_DATE | 生效日期 | date | Y |  |
| 8 | END_DATE | 失效日期 | date | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 11 | COUNTER_CHARGE_ID | 租户费用项目编号 | GUID | Y |  |
| 12 | DEF_PROPORTION_RATE | 默认分摊比率 | number(5,4) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Attachments | 附件 | string | Y |  |
| 20 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 21 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 22 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 23 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 24 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 25 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 26 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 27 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 28 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 29 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 30 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 31 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 32 | UDF041 | 自定义字段12 | date | Y |  |
| 33 | UDF042 | 自定义字段13 | date | Y |  |
| 34 | UDF051 | 自定义字段14 | GUID | Y |  |
| 35 | UDF052 | 自定义字段15 | GUID | Y |  |
| 36 | UDF053 | 自定义字段16 | GUID | Y |  |
| 37 | UDF054 | 自定义字段17 | GUID | Y |  |
| 38 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 39 | Version | 版本号，不要随意更改 | binary | Y |  |
| 40 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 41 | ApproveDate | 修改日期 | date | Y |  |
| 42 | ApproveBy | 修改人 | GUID | Y |  |
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_PROPORTION_RENTER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_PROPORTION_RENTER_ID | 主键 | GUID | Y | Y |
| 3 | RENTER_ID | 租户编号 | GUID | Y |  |
| 4 | PROPORTION_RATE | 分摊比率 | number(5,4) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | CARD_PROPORTION_RATE_ID |  | GUID | Y |  |

### CARD_RECHARGE_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CARD_RECHARGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | string(80) | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | CARD_ID | 卡ID | GUID | Y |  |
| 11 | CARD_CODE | 卡号 | string(400) | Y |  |
| 12 | MEMBER_ID | 会员ID | string(400) | Y |  |
| 13 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 14 | RECHARGE_AMOUNT | 充值金额 | number(23,8) | Y |  |
| 15 | RECHARGE_POINT | 充值赠送积分 | number(16,4) | Y |  |
| 16 | RECHARGE_FACE_VALUE | 充值面额 | number(23,8) | Y |  |
| 17 | RECHARGE_RULE_TYPE | 充值策略类型 | string(40) | Y |  |
| 18 | RECHARGE_RULE_CODE | 充值策略编号 | string(40) | Y |  |
| 19 | NEED_TICKET_GROUP_ID | 应赠券类型 | GUID | Y |  |
| 20 | NEED_TICKET_AMOUNT | 应赠券金额 | number(23,8) | Y |  |
| 21 | TICKET_NUM | 实赠券张数 | number(16,6) | Y |  |
| 22 | TICKET_AMOUNT | 实赠券金额 | number(23,8) | Y |  |
| 23 | REMARK | 备注 | string(510) | Y |  |
| 24 | POS_ID | POS机号 | GUID | Y |  |
| 25 | PrintCount | 打印次数 | number | Y |  |
| 26 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 27 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 28 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 29 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 62 | RECHARGE_RULE_ID_RTK |  | string(400) | Y |  |
| 63 | RECHARGE_RULE_ID_ROid |  | GUID | Y |  |

### CARD_RECHARGE_DOC_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CARD_RECHARGE_DOC_ITEM_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 品号ID | GUID | Y |  |
| 3 | ITEM_CODE | 品号 | string(40) | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | ITEM_QTY |  | number(16,6) | Y |  |
| 7 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 8 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
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
| 34 | CARD_RECHARGE_DOC_ID |  | GUID | Y |  |

### CARD_RECHARGE_DOC_PAYTYPE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_DOC_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 3 | PAYTYPE_ID | 付款方式 | GUID | Y |  |
| 4 | PAY_AMOUNT | 付款金额 | number(23,8) | Y |  |
| 5 | PAY_TYPE | 付款方式 | string(40) | Y |  |
| 6 | CT_TYPE | 卡券类型 | number | Y |  |
| 7 | CT_ID | 卡ID/券ID | GUID | Y |  |
| 8 | CT_CODE | 卡号/券号 | string(400) | Y |  |
| 9 | CT_ENCRYPT_KEY | 卡内号 | string(400) | Y |  |
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
| 37 | CARD_RECHARGE_DOC_ID |  | GUID | Y |  |

### CARD_RECHARGE_DOC_TICKET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_DOC_TICKET_ID | 主键 | GUID | Y | Y |
| 3 | TICKET_GROUP_ID | 券类型ID | GUID | Y |  |
| 4 | TICKET_GROUP_CODE | 券类型编号 | string(40) | Y |  |
| 5 | TICKET_ID | 券号ID | string(80) | Y |  |
| 6 | TICKET_CODE | 券号 | string(40) | Y |  |
| 7 | TICKET_FACE_VALUE_ID | 券面值 | GUID | Y |  |
| 8 | TICKET_AMOUNT | 券金额 | number(23,8) | Y |  |
| 9 | TICKET_PRESENT_AMOUNT | 实际赠送金额 | number(23,8) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | TICKET_NUM | 券数量 | number | Y |  |
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
| 37 | CARD_RECHARGE_DOC_ID |  | GUID | Y |  |

### CARD_RECHARGE_ITEM (卡充值赠品)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_ITEM_ID | 主键 | GUID | Y | Y |
| 3 | RECHARGE_MONEY | 充值金额 | number(23,8) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | CARD_RECHARGE_RULE_ID |  | GUID | Y |  |

### CARD_RECHARGE_ITEM_SD (卡充值赠品列表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_ITEM_SD_ID | 主键 | GUID | Y | Y |
| 3 | RECHARGE_MONEY | 充值金额 | number(23,8) | Y |  |
| 4 | ITEM_NUM |  | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | ITEM_ID | 主键 | GUID | Y |  |
| 7 | SALE_UNIT_ID | 零售单位 | GUID | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | CARD_RECHARGE_ITEM_ID |  | GUID | Y |  |

### CARD_RECHARGE_LADDER (卡充值阶梯赠送)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_LADDER_ID | 主键 | GUID | Y | Y |
| 3 | RECHARGE_MONEY | 充值金额 | number(23,8) | Y |  |
| 4 | RECHARGE_PRESENT_MONEY | 赠送金额 | number(23,8) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | CARD_RECHARGE_RULE_ID |  | GUID | Y |  |

### CARD_RECHARGE_RULE (卡充值策略)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | CARD_RECHARGE_RULE_ID | 主键 | GUID | Y | Y |
| 4 | CARD_RECHARGE_RULE_CODE | 充值策略编号 | string(40) | Y |  |
| 5 | CARD_RECHARGE_RULE_NAME | 充值策略编号 | string(200) | Y |  |
| 6 | RECHARGE_TYPE | 充值策略类型 | string(40) | Y |  |
| 7 | BEGIN_DATE | 生效开始时间 | date | Y |  |
| 8 | END_DATE | 生效结束时间 | date | Y |  |
| 9 | SHOP_RANGE | 生效门店范围 | string(40) | Y |  |
| 10 | RECHARGE_MIN_MONEY | 充值最低金额 | number(23,8) | Y |  |
| 11 | RECHARGE_MULTIPLE_MONEY | 充值倍额 | number(23,8) | Y |  |
| 12 | RECHARGE_FACE_MONEY | 充值面额 | number(23,8) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | IS_BASE | 基准 | number(0/1) | Y |  |
| 15 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 16 | CARD_GROUP_ID | 卡类型编号 | GUID | Y |  |
| 17 | RECHARGE_LIMIT_AMOUNT | 充值限额 | number(23,8) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 26 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 27 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 28 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 29 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 30 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 31 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 32 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 33 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 34 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 35 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 36 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 37 | UDF041 | 自定义字段12 | date | Y |  |
| 38 | UDF042 | 自定义字段13 | date | Y |  |
| 39 | UDF051 | 自定义字段14 | GUID | Y |  |
| 40 | UDF052 | 自定义字段15 | GUID | Y |  |
| 41 | UDF053 | 自定义字段16 | GUID | Y |  |
| 42 | UDF054 | 自定义字段17 | GUID | Y |  |
| 43 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 44 | Version | 版本号，不要随意更改 | binary | Y |  |
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_RECHARGE_SHOP (卡充值策略生效门店列表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_SHOP_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 主键 | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 30 | CARD_RECHARGE_RULE_ID |  | GUID | Y |  |

### CARD_RECHARGE_TICKET (卡充值赠券)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_RECHARGE_TICKET_ID | 主键 | GUID | Y | Y |
| 3 | RECHARGE_MONEY | 充值金额 | number(23,8) | Y |  |
| 4 | TICKET_GROUP | 券类型 | GUID | Y |  |
| 5 | TICKET_MONEY | 赠券金额 | number(23,8) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 32 | CARD_RECHARGE_RULE_ID |  | GUID | Y |  |

### CARD_REPLACE_REASON (换卡原因)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | CARD_REPLACE_REASON_ID | 主键 | GUID | Y | Y |
| 2 | CARD_REPLACE_REASON_CODE | 换卡原因编号 | string(40) | Y |  |
| 3 | CARD_REPLACE_REASON_DESC | 换卡原因名称 | string(160) | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Attachments | 附件 | string | Y |  |
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
| 30 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |

### CARD_TRANSACTION_DETAIL (维护卡交易明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | Owner_Dept | 关联部门 | GUID | Y |  |
| 3 | Owner_Emp | 关联员工 | GUID | Y |  |
| 4 | CARD_TRANSACTION_DETAIL_ID | 主键 | GUID | Y | Y |
| 5 | CARD_CODE | 卡号 | string(40) | Y |  |
| 6 | HAPPEN_TYPE | 发生类型 | string(40) | Y |  |
| 7 | HAPPEN_DATE | 发生日期 | date | Y |  |
| 8 | TRANSACTION_ID | 交易来源 | GUID | Y |  |
| 9 | DOC_NO |  | string(40) | Y |  |
| 10 | HAPPEN_MONEY | 发生金额 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | STATUS | 状态 | string(40) | Y |  |
| 13 | HAPPEN_BAL | 发生后余额 | number(23,8) | Y |  |
| 14 | POS_ID | POS机台 | GUID | Y |  |
| 15 | CLASS_ID | 班次 | number | Y |  |
| 16 | SHOP_ID | 门店ID | GUID | Y |  |
| 17 | HAPPEN_CODE | 交易识别码 | string(40) | Y |  |
| 18 | TRANSACTION_STATUS | 卡发生状态 | number | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
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
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |

### CARD_TRANSFER_DOC (卡移转单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CARD_TRANSFER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 9 | TRANSFER_DIRECTION | 卡移转类型 | string(40) | Y |  |
| 10 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 11 | CARD_NUM | 卡数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | CONFIRM_STATUS | 门店确认标志 | number(0/1) | Y |  |
| 14 | PrintCount | 打印次数 | number | Y |  |
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
| 33 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 34 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 35 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 36 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 37 | CreateDate | 创建日期 | date | Y |  |
| 38 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 39 | ModifiedDate | 修改日期 | date | Y |  |
| 40 | CreateBy | 创建者 | GUID | Y |  |
| 41 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 42 | ModifiedBy | 修改者 | GUID | Y |  |
| 43 | Attachments | 附件 | string | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |
| 51 | SEND_ORG_ID_RTK |  | string(400) | Y |  |
| 52 | SEND_ORG_ID_ROid |  | GUID | Y |  |
| 53 | RECEIVE_ORG_ID_RTK |  | string(400) | Y |  |
| 54 | RECEIVE_ORG_ID_ROid |  | GUID | Y |  |

### CARD_TRANSFER_DOC_D (卡移转单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_TRANSFER_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | CARD_ID | 卡ID | GUID | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 6 | BEGIN_CARD_CODE | 开始卡号 | string(40) | Y |  |
| 7 | END_CARD_CODE | 结束卡号 | string(40) | Y |  |
| 8 | CARD_NUM | 数量 | number | Y |  |
| 9 | CONFIRM_NUM | 确认数量 | number | Y |  |
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
| 28 | CreateDate | 创建日期 | date | Y |  |
| 29 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 30 | ModifiedDate | 修改日期 | date | Y |  |
| 31 | CreateBy | 创建者 | GUID | Y |  |
| 32 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 33 | ModifiedBy | 修改者 | GUID | Y |  |
| 34 | Version | 版本号，不要随意更改 | binary | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | CARD_TRANSFER_DOC_ID |  | GUID | Y |  |

### CARD_TRANSFER_DOC_DIFF (卡移转确认差异)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 3 | CARD_ID | 卡号 | GUID | Y |  |
| 4 | CARD_NUM | 数量 | number | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | CARD_TRANSFER_DOC_DIFF_ID | 主键 | string(400) | Y | Y |
| 7 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 8 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 9 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 10 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 11 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 12 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 13 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 14 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 15 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 16 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 17 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 18 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 19 | UDF041 | 自定义字段12 | date | Y |  |
| 20 | UDF042 | 自定义字段13 | date | Y |  |
| 21 | UDF051 | 自定义字段14 | GUID | Y |  |
| 22 | UDF052 | 自定义字段15 | GUID | Y |  |
| 23 | UDF053 | 自定义字段16 | GUID | Y |  |
| 24 | UDF054 | 自定义字段17 | GUID | Y |  |
| 25 | CreateDate | 创建日期 | date | Y |  |
| 26 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 27 | ModifiedDate | 修改日期 | date | Y |  |
| 28 | CreateBy | 创建者 | GUID | Y |  |
| 29 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 30 | ModifiedBy | 修改者 | GUID | Y |  |
| 31 | Version | 版本号，不要随意更改 | binary | Y |  |
| 32 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 33 | ApproveDate | 修改日期 | date | Y |  |
| 34 | ApproveBy | 修改人 | GUID | Y |  |
| 35 | CARD_TRANSFER_DOC_ID |  | GUID | Y |  |

### CARD_WITHHOLD_DOC (维护卡扣款信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | CARD_WITHHOLD_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | CARD_ID | 卡ID | GUID | Y |  |
| 11 | CARD_ENCRYPT_KEY | 卡内号 | string(80) | Y |  |
| 12 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 13 | CARD_CODE | 卡号 | string(40) | Y |  |
| 14 | CARD_AMOUNT | 卡余额 | number(23,8) | Y |  |
| 15 | CARD_STATUS | 卡状态 | string(40) | Y |  |
| 16 | CARD_CORPUS | 卡本金 | number(23,8) | Y |  |
| 17 | MEMBER_ID | 会员ID | GUID | Y |  |
| 18 | MEMBER_CODE | 会员号 | string(80) | Y |  |
| 19 | MEMBER_NAME | 会员姓名 | string(80) | Y |  |
| 20 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 21 | VALID_POINTS | 可用积分 | number(16,4) | Y |  |
| 22 | WITHHOLD_AMOUNT | 扣款金额 | number(23,8) | Y |  |
| 23 | AFTER_WITHHOLD_AMOUNT | 扣款后余额 | number(23,8) | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
| 25 | POS_ID | POS机号 | GUID | Y |  |
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Attachments | 附件 | string | Y |  |
| 33 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 34 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 35 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 36 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 37 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 38 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 39 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 40 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 41 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 42 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 43 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 44 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 45 | UDF041 | 自定义字段12 | date | Y |  |
| 46 | UDF042 | 自定义字段13 | date | Y |  |
| 47 | UDF051 | 自定义字段14 | GUID | Y |  |
| 48 | UDF052 | 自定义字段15 | GUID | Y |  |
| 49 | UDF053 | 自定义字段16 | GUID | Y |  |
| 50 | UDF054 | 自定义字段17 | GUID | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |