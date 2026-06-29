---
module: "MEMBER"
name_zh: "会员管理"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 44
columns: 1694
category: crm
tags: ["ERP", "E10", "crm"]
created: 2026-06-25 10:52
---

# MEMBER (会员管理)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 44 | Columns: 1694

## Related Modules

- [[BP (业务伙伴)|BP (业务伙伴)]]
- [[CARD (卡券管理)|CARD (卡券管理)]]
- [[CRM (客户关系)|CRM (客户关系)]]
- [[CUSTOMER (客户管理)|CUSTOMER (客户管理)]]
- [[REPAIR (维修管理)|REPAIR (维修管理)]]
- [[REPLACE (替换管理)|REPLACE (替换管理)]]
- [[SERVICE (售后服务)|SERVICE (售后服务)]]
- [[TICKET (票券管理)|TICKET (票券管理)]]

---

## Tables


- **MEMBER_BUY_DOC_ITEM**
- **MEMBER_BUY_DOC_PAYTYPE**
- **MEMBER_BUY_DOC_TICKET**
- **MEMBER_BUY_ITEM**
- **MEMBER_BUY_PAYMENT**
- **MEMBER_BUY_SHOP**
- **MEMBER_BUY_TICKET**
- **MEMBER_DOC**
- **MEMBER_DOC_ITEM**
- **MEMBER_DOC_MEMORIAL_DAY**
- **MEMBER_DOC_PAYTYPE**
- **MEMBER_DOC_TICKET**
- **MEMBER_GROUP (会员类型)**
- **MEMBER_GROUP_CHANGE_DOC (会员类型调整单)**
- **MEMBER_GROUP_CHANGE_DOC_D (会员类型调整单单身)**
- **MEMBER_GROUP_OC (会员类型所属营运域)**
- **MEMBER_MEMORIAL_DAY (会员纪念日档)**
- **MEMBER_POINT_BUY_DOC**
- **MEMBER_POINT_BUY_RULE**
- **MEMBER_POINT_EX_ITEM**
- **MEMBER_POINT_HISTORY (会员积分变动档)**
- **MEMBER_POINT_ITEM**
- **MEMBER_POINT_LADDER**
- **MEMBER_POINT_MMR_DAY**
- **MEMBER_POINT_MODIFY_DOC (会员积分增减单)**
- **MEMBER_POINT_MODIFY_DOC_D**
- **MEMBER_POINT_PAYMENT**
- **MEMBER_POINT_RULE**
- **MEMBER_POINT_SHOP_LIST**
- **MEMBER_PRICE_DISCOUNT (会员品类价格设定)**
- **MEMBER_RECHARGE_ITEM (会员充值赠品明细表)**
- **MEMBER_RECHARGE_ITEM_SD (会员充值赠品列表)**
- **MEMBER_RECHARGE_LADDER (会员充值阶梯赠送)**
- **MEMBER_RECHARGE_POINT (会员充值赠积分明细)**
- **MEMBER_RECHARGE_RULE (会员充值策略)**
- **MEMBER_RECHARGE_SHOP (会员充值策略生效门店列表)**
- **MEMBER_RECHARGE_TICKET (会员充值赠券明细表)**
- **MEMBER_TO_MONEY_DOC**
- **MEMBER_TO_MONEY_RULE (会员积分转储策略)**
- **MEMBER_TO_MONEY_SHOP_D**
- **MEMBER_UPGRADE_CONDITION**
- **MEMBER_UPGRADE_RULE**
- **MEMBER_UPGRADE_SEQUENCE**


---


---


> Tables: 44

### MEMBER (会员信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_CODE | 会员编号 | string(40) | Y |  |
| 5 | MEMBER_NAME | 会员姓名 | string(120) | Y |  |
| 6 | SEX | 性别 | string(40) | Y |  |
| 7 | AGE | 年龄 | number | Y |  |
| 8 | PAPER_TYPE | 证件类型 | string(40) | Y |  |
| 9 | PAPER_NO | 证件号码 | string(100) | Y |  |
| 10 | INCOME | 月收入 | number(23,8) | Y |  |
| 11 | SCHOOL_RECORD | 学历 | string(40) | Y |  |
| 12 | MARRIED | 婚否 | string(40) | Y |  |
| 13 | HAS_CHILDREN | 有子女否 | number(0/1) | Y |  |
| 14 | AREA_ID | 地区 | GUID | Y |  |
| 15 | PROVINCE_ID | 省 | GUID | Y |  |
| 16 | CITY_ID | 市 | GUID | Y |  |
| 17 | RANGE_ID | 区 | GUID | Y |  |
| 18 | HOME_ADDRESS | 家庭住址 | string(510) | Y |  |
| 19 | WORK_UNIT | 工作单位 | string(510) | Y |  |
| 20 | HEIGHT | 身高 | number(16,4) | Y |  |
| 21 | WEIGHT | 体重 | number(16,4) | Y |  |
| 22 | CELLPHONE | 移动电话 | string(40) | Y |  |
| 23 | PHONE | 固定电话 | string(40) | Y |  |
| 24 | EMAIL | 电子邮件 | string(200) | Y |  |
| 25 | INIT_DATE | 办理日期 | date | Y |  |
| 26 | INIT_SHOP | 主键 | GUID | Y |  |
| 27 | TOTAL_POINTS | 总积分 | number(16,4) | Y |  |
| 28 | VALID_POINTS | 可用积分 | number(16,4) | Y |  |
| 29 | TOTAL_MONEY | 总消费额 | number(23,8) | Y |  |
| 30 | TOTAL_USE_TIMES | 总消费次数 | number | Y |  |
| 31 | MASTER_MEMBER_ID | 主会员 | GUID | Y |  |
| 32 | IS_WAIT_UPGRADE | 待升级 | number(0/1) | Y |  |
| 33 | UPGRADE_MEMBER_GROUP_ID | 升级后会员类型 | GUID | Y |  |
| 34 | UPGRADE_DESCREATE_POINTS | 升级后扣减积分 | number(16,4) | Y |  |
| 35 | REMARK | 备注 | string(510) | Y |  |
| 36 | MEMBER_UPGRADE_TYPE | 会员升级方式 | string(40) | Y |  |
| 37 | CARD_ID | 主键 | GUID | Y |  |
| 38 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 39 | MEMBER_PASSWORD | 会员密码 | string(40) | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 48 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 49 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 50 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 51 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 52 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 53 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 54 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 55 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 56 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 57 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 58 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 59 | UDF041 | 自定义字段12 | date | Y |  |
| 60 | UDF042 | 自定义字段13 | date | Y |  |
| 61 | UDF051 | 自定义字段14 | GUID | Y |  |
| 62 | UDF052 | 自定义字段15 | GUID | Y |  |
| 63 | UDF053 | 自定义字段16 | GUID | Y |  |
| 64 | UDF054 | 自定义字段17 | GUID | Y |  |
| 65 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 66 | Version | 版本号，不要随意更改 | binary | Y |  |
| 67 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 68 | ApproveDate | 修改日期 | date | Y |  |
| 69 | ApproveBy | 修改人 | GUID | Y |  |
| 70 | Owner_Org_RTK |  | string(400) | Y |  |
| 71 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_BUY_DOC_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_DOC_ITEM_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NUM | 数量 | number(16,6) | Y |  |
| 5 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 6 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 7 | EXCHANGE_POINTS | 扣减积分 | number(16,4) | Y |  |
| 8 | EXCHANGE_PAY_MONEY | 付款金额 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
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
| 35 | MEMBER_POINT_BUY_DOC_ID |  | GUID | Y |  |

### MEMBER_BUY_DOC_PAYTYPE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_DOC_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 3 | PAYTYPE_ID | 付款方式 | GUID | Y |  |
| 4 | PAY_AMOUNT | 付款金额 | number(23,8) | Y |  |
| 5 | PAY_TYPE | 付款方式 | number | Y |  |
| 6 | CT_TYPE | 卡券类型 | number | Y |  |
| 7 | CT_ID | 卡ID/券ID | GUID | Y |  |
| 8 | CT_CODE | 卡号/券号 | string(80) | Y |  |
| 9 | EXTRA | 溢收 | number(23,8) | Y |  |
| 10 | CHANGED | 找零金额 | number(23,8) | Y |  |
| 11 | CT_ENCRYPT_KEY | 卡内号 | string(80) | Y |  |
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
| 37 | MEMBER_POINT_BUY_DOC_ID |  | GUID | Y |  |

### MEMBER_BUY_DOC_TICKET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_DOC_TICKET_ID | 主键 | GUID | Y | Y |
| 3 | TICKET_GROUP_ID | 券类型 | GUID | Y |  |
| 4 | TICKET_ID | 券号 | GUID | Y |  |
| 5 | TICKET_FACE_VALUE_ID | 券面值 | GUID | Y |  |
| 6 | TICKET_NUM | 券数量 | number(16,6) | Y |  |
| 7 | POINT | 扣减积分 | number(16,4) | Y |  |
| 8 | AMOUNT | 付款金额 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
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
| 35 | MEMBER_POINT_BUY_DOC_ID |  | GUID | Y |  |

### MEMBER_BUY_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_ITEM_ID | 主键 | GUID | Y | Y |
| 3 | EXCHANGE_POINTS | 换购扣减积分 | number(16,4) | Y |  |
| 4 | EXCHANGE_PAY_MONEY | 付款（加钱） | number(23,8) | Y |  |
| 5 | ITEM_ID | 品号 | GUID | Y |  |
| 6 | ITEM_NUM | 数量 | number(16,6) | Y |  |
| 7 | SALE_UNIT_ID | 零售单位 | GUID | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | MEMBER_POINT_BUY_RULE_ID |  | GUID | Y |  |

### MEMBER_BUY_PAYMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_PAYMENT_ID | 主键 | GUID | Y | Y |
| 3 | SALE_PAYTYPE_ID | 付款方式 | GUID | Y |  |
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
| 30 | MEMBER_POINT_BUY_RULE_ID |  | GUID | Y |  |

### MEMBER_BUY_SHOP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_SHOP_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 门店编号 | GUID | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 29 | MEMBER_POINT_BUY_RULE_ID |  | GUID | Y |  |

### MEMBER_BUY_TICKET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_BUY_TICKET_ID | 主键 | GUID | Y | Y |
| 3 | EXCHANGE_POINTS | 换购扣减积分 | number(16,4) | Y |  |
| 4 | EXCHANGE_PAY_MONEY | 付款（加钱） | number(23,8) | Y |  |
| 5 | TICKET_GROUP_ID | 券类型 | GUID | Y |  |
| 6 | TICKET_MONEY | 券金额 | number(23,8) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
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
| 33 | MEMBER_POINT_BUY_RULE_ID |  | GUID | Y |  |

### MEMBER_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | MEMBER_DOC_ID | 主键 | GUID | Y | Y |
| 7 | MEMBER_NAME | 会员姓名 | string(120) | Y |  |
| 8 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 9 | AGE | 年龄 | number | Y |  |
| 10 | PAPER_TYPE | 证件类型 | string(40) | Y |  |
| 11 | PAPER_NO | 证件号码 | string(400) | Y |  |
| 12 | INCOME | 月收入 | number(23,8) | Y |  |
| 13 | SCHOOL_RECORD | 学历 | string(40) | Y |  |
| 14 | MARRIED | 婚否 | string(40) | Y |  |
| 15 | HAS_CHILDREN | 有子女否 | number(0/1) | Y |  |
| 16 | AREA_ID | 地区 | GUID | Y |  |
| 17 | PROVINCE_ID | 省 | GUID | Y |  |
| 18 | CITY_ID | 市 | GUID | Y |  |
| 19 | RANGE_ID | 区 | GUID | Y |  |
| 20 | HOME_ADDRESS | 家庭住址 | string(510) | Y |  |
| 21 | WORK_UNIT | 工作单位 | string(510) | Y |  |
| 22 | HEIGHT | 身高 | number(16,4) | Y |  |
| 23 | WEIGHT | 体重 | number(16,4) | Y |  |
| 24 | CELLPHONE | 移动电话 | string(40) | Y |  |
| 25 | PHONE | 固定电话 | string(40) | Y |  |
| 26 | EMAIL | 电子邮件 | string(200) | Y |  |
| 27 | INIT_DATE | 办理日期 | date | Y |  |
| 28 | INIT_SHOP | 办理门店 | GUID | Y |  |
| 29 | MASTER_MEMBER_ID | 主会员 | GUID | Y |  |
| 30 | CARD_ID | 卡号 | GUID | Y |  |
| 31 | MEMBER_UPGRADE_TYPE | 会员升级方式 | string(40) | Y |  |
| 32 | RECHARGE_AMOUNT | 充值金额 | number(23,8) | Y |  |
| 33 | RECHARGE_FACE_VALUE | 充值面额 | number(23,8) | Y |  |
| 34 | REMARK | 备注 | string(510) | Y |  |
| 35 | POS_ID | POS机号 | GUID | Y |  |
| 36 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 37 | SHOP_ID | 门店 | GUID | Y |  |
| 38 | SEX | 性别 | string(40) | Y |  |
| 39 | CATEGORY | 单据性质 | string(40) | Y |  |
| 40 | PrintCount | 打印次数 | number | Y |  |
| 41 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 42 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 43 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 44 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 45 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 46 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 47 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 48 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 49 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 50 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 51 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 52 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 53 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 54 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 55 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 56 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 57 | UDF041 | 自定义字段12 | date | Y |  |
| 58 | UDF042 | 自定义字段13 | date | Y |  |
| 59 | UDF051 | 自定义字段14 | GUID | Y |  |
| 60 | UDF052 | 自定义字段15 | GUID | Y |  |
| 61 | UDF053 | 自定义字段16 | GUID | Y |  |
| 62 | UDF054 | 自定义字段17 | GUID | Y |  |
| 63 | CreateDate | 创建日期 | date | Y |  |
| 64 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 65 | ModifiedDate | 修改日期 | date | Y |  |
| 66 | CreateBy | 创建者 | GUID | Y |  |
| 67 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 68 | ModifiedBy | 修改者 | GUID | Y |  |
| 69 | Attachments | 附件 | string | Y |  |
| 70 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 71 | Version | 版本号，不要随意更改 | binary | Y |  |
| 72 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 73 | ApproveDate | 修改日期 | date | Y |  |
| 74 | ApproveBy | 修改人 | GUID | Y |  |
| 75 | Owner_Org_RTK |  | string(400) | Y |  |
| 76 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_DOC_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MEMBER_DOC_ITEM_ID | 主键 | GUID | Y | Y |
| 2 | ITEM_ID | 品号ID | GUID | Y |  |
| 3 | ITEM_CODE | 品号 | string(400) | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | ITEM_QTY |  | number(16,6) | Y |  |
| 6 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 7 | SECOND_QTY | 第二单位数量 | number(16,6) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
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
| 34 | MEMBER_DOC_ID |  | GUID | Y |  |

### MEMBER_DOC_MEMORIAL_DAY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_DOC_MEMORIAL_DAY_ID | 主键 | GUID | Y | Y |
| 3 | MEMORIAL_DAY_ID | 纪念日类型 | GUID | Y |  |
| 4 | MEMORIAL_DAY_DATE | 纪念日日期 | date | Y |  |
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
| 24 | CreateDate | 创建日期 | date | Y |  |
| 25 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 26 | ModifiedDate | 修改日期 | date | Y |  |
| 27 | CreateBy | 创建者 | GUID | Y |  |
| 28 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 29 | ModifiedBy | 修改者 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | MEMBER_DOC_ID |  | GUID | Y |  |

### MEMBER_DOC_PAYTYPE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_DOC_PAYTYPE_ID | 主键 | GUID | Y | Y |
| 3 | PAYTYPE_ID | 付款方式 | GUID | Y |  |
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
| 37 | MEMBER_DOC_ID |  | GUID | Y |  |

### MEMBER_DOC_TICKET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MEMBER_DOC_TICKET_ID | 主键 | GUID | Y | Y |
| 2 | TICKET_GROUP_ID | 券类型ID | GUID | Y |  |
| 3 | TICKET_GROUP_CODE | 券类型编号 | string(400) | Y |  |
| 4 | TICKET_ID | 券号ID | GUID | Y |  |
| 5 | TICKET_CODE | 券号 | string(400) | Y |  |
| 6 | TICKET_NUM | 券数量 | number | Y |  |
| 7 | TICKET_FACE_VALUE_ID | 券面值 | GUID | Y |  |
| 8 | TICKET_AMOUNT | 券金额 | number(23,8) | Y |  |
| 9 | TICKET_PRESENT_AMOUNT | 实际赠送金额 | number(23,8) | Y |  |
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
| 29 | CreateDate | 创建日期 | date | Y |  |
| 30 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 31 | ModifiedDate | 修改日期 | date | Y |  |
| 32 | CreateBy | 创建者 | GUID | Y |  |
| 33 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 34 | ModifiedBy | 修改者 | GUID | Y |  |
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | MEMBER_DOC_ID |  | GUID | Y |  |

### MEMBER_GROUP (会员类型)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_GROUP_CODE | 会员类型编号 | string(40) | Y |  |
| 5 | MEMBER_GROUP_NAME | 会员类型名称 | string(120) | Y |  |
| 6 | DISCOUNT_PRICE_TYPE | 默认取价方法 | string(40) | Y |  |
| 7 | DEFAULT_DISCOUNT | 默认折扣 | number(5,4) | Y |  |
| 8 | DEFAULT_MEMBER_PRICE | 默认会员价 | string(40) | Y |  |
| 9 | MEMBER_CODE_START | 会员号开头 | string(20) | Y |  |
| 10 | MEMBER_CODE_LENGTH | 会员号长度 | number | Y |  |
| 11 | RETURN_POINT_BACK_TYPE | 积分退货吸收方式 | string(4) | Y |  |
| 12 | RETURN_POINT_BACK_RATE | 积分退货吸收比率 | number(5,4) | Y |  |
| 13 | IS_RECHARGED | 可充值 | number(0/1) | Y |  |
| 14 | MIN_CHARGE_MONEY | 默认最低充值金额 | number(23,8) | Y |  |
| 15 | IS_POINT | 可积分 | number(0/1) | Y |  |
| 16 | IS_POINT_TO_MONEY | 积分可转储 | number(0/1) | Y |  |
| 17 | POINT_TRUNC_METHOD | 积分取整方式 | string(4) | Y |  |
| 18 | POINT_TRUNC_DIGIT | 积分取整位数 | number | Y |  |
| 19 | IS_INIT_PRESENT_POINT | 开卡送积分 | number(0/1) | Y |  |
| 20 | INIT_PRESENT_POINT | 开卡送积分额 | number(16,4) | Y |  |
| 21 | CURRENCY_ID | 币种 | GUID | Y |  |
| 22 | REMARK | 备注 | string(510) | Y |  |
| 23 | ITEM_GROUP_TYPE | 品类价格方式 | string(40) | Y |  |
| 24 | IS_INIT_RECHARGE | 开卡充值 | number(0/1) | Y |  |
| 25 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
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

### MEMBER_GROUP_CHANGE_DOC (会员类型调整单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | MEMBER_GROUP_CHANGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | AFTER_MEMBER_GROUP_ID | 调整后会员类型 | GUID | Y |  |
| 9 | DECREASE_POINTS | 调整扣减积分 | number(16,4) | Y |  |
| 10 | POINT_TRANSFER_RATE | 调整后积分换算比率 | number(5,4) | Y |  |
| 11 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | REASON_REMARK | 原因说明 | string(510) | Y |  |
| 14 | PrintCount | 打印次数 | number | Y |  |
| 15 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 16 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 17 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 18 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 43 | Attachments | 附件 | string | Y |  |
| 44 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 45 | Version | 版本号，不要随意更改 | binary | Y |  |
| 46 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 47 | ApproveDate | 修改日期 | date | Y |  |
| 48 | ApproveBy | 修改人 | GUID | Y |  |
| 49 | Owner_Org_RTK |  | string(400) | Y |  |
| 50 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_GROUP_CHANGE_DOC_D (会员类型调整单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_GROUP_CHANGE_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | MEMBER_ID | 会员号 | GUID | Y |  |
| 4 | BEFORE_MEMBER_GROUP_ID | 升级前会员类型 | GUID | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | REASON_REMARK | 原因说明 | string(510) | Y |  |
| 7 | BEFORE_VALID_POINTS | 会员可用积分 | number(16,4) | Y |  |
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
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | MEMBER_GROUP_CHANGE_DOC_ID |  | GUID | Y |  |

### MEMBER_GROUP_OC (会员类型所属营运域)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_GROUP_OC_ID | 主键 | GUID | Y | Y |
| 3 | OPERATION_CENTER_ID | 所属营运域 | GUID | Y |  |
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
| 30 | MEMBER_GROUP_ID |  | GUID | Y |  |

### MEMBER_MEMORIAL_DAY (会员纪念日档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_IMPORTANT_DAY_ID | 主键 | GUID | Y | Y |
| 3 | MEMORIAL_DAY_DATE | 纪念日日期 | date | Y |  |
| 4 | REMARK | 备注 | string(510) | Y |  |
| 5 | MEMORIAL_DAY_ID | 纪念日类型 | GUID | Y |  |
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
| 31 | MEMBER_ID |  | GUID | Y |  |

### MEMBER_POINT_BUY_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | MEMBER_POINT_BUY_DOC_ID | 主键 | GUID | Y | Y |
| 7 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 8 | SHOP_ID | 门店 | GUID | Y |  |
| 9 | CATEGORY | 单据性质 | string(40) | Y |  |
| 10 | MEMBER_ID | 会员编号 | string(80) | Y |  |
| 11 | CARD_ID | 卡ID | string(80) | Y |  |
| 12 | TNL_FLAG | 券数量余额计算标志 | number(0/1) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | POS_ID | POS机ID | GUID | Y |  |
| 15 | MEMBER_POINT_BUY_RULE_ID | 换购策略编号 | GUID | Y |  |
| 16 | PrintCount | 打印次数 | number | Y |  |
| 17 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 18 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 19 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 20 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 21 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 22 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 23 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 24 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 25 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 26 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 27 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 28 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 29 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 30 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 31 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 32 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 33 | UDF041 | 自定义字段12 | date | Y |  |
| 34 | UDF042 | 自定义字段13 | date | Y |  |
| 35 | UDF051 | 自定义字段14 | GUID | Y |  |
| 36 | UDF052 | 自定义字段15 | GUID | Y |  |
| 37 | UDF053 | 自定义字段16 | GUID | Y |  |
| 38 | UDF054 | 自定义字段17 | GUID | Y |  |
| 39 | CreateDate | 创建日期 | date | Y |  |
| 40 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 41 | ModifiedDate | 修改日期 | date | Y |  |
| 42 | CreateBy | 创建者 | GUID | Y |  |
| 43 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 44 | ModifiedBy | 修改者 | GUID | Y |  |
| 45 | Attachments | 附件 | string | Y |  |
| 46 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | Owner_Org_RTK |  | string(400) | Y |  |
| 52 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_POINT_BUY_RULE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_POINT_BUY_RULE_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_POINT_BUY_RULE_CODE | 积分换购策略编号 | string(40) | Y |  |
| 5 | MEMBER_POINT_BUY_RULE_NAME | 积分换购策略名称 | string(120) | Y |  |
| 6 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 7 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 8 | BEGIN_DATE | 生效日期 | date | Y |  |
| 9 | END_DATE | 失效日期 | date | Y |  |
| 10 | SHOP_RANGE | 生效门店范围 | string(40) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
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
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | Owner_Org_RTK |  | string(400) | Y |  |
| 43 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_POINT_EX_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_EX_ITEM_D_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 主键 | GUID | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 29 | MEMBER_POINT_RULE_ID |  | GUID | Y |  |

### MEMBER_POINT_HISTORY (会员积分变动档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | MEMBER_POINT_HISTORY_ID | 主键 | GUID | Y | Y |
| 5 | MEMBER_POINT_HISTORY_TYPE | 来源类型 | string(4) | Y |  |
| 6 | POINT | 积分值 | number(16,4) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | DOC_NO | 来源单据号 | string(40) | Y |  |
| 9 | MEMBER_ID | 会员 | GUID | Y |  |
| 10 | POINT_DATE | 积分日期 | date | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
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
| 36 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_POINT_ITEM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_ITEM_D_ID | 主键 | GUID | Y | Y |
| 3 | POINT_BASE_VALUE | 积分基数 | number(16,4) | Y |  |
| 4 | UNIT_POINT | 单位积分 | number(16,4) | Y |  |
| 5 | PRESENT_POINT | 额外赠送积分 | number(16,4) | Y |  |
| 6 | ITEM_BRAND_FUTURE | 品牌属性 | GUID | Y |  |
| 7 | ITEM_CATEGORY_FUTURE | 类别属性 | GUID | Y |  |
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
| 33 | MEMBER_POINT_RULE_ID |  | GUID | Y |  |

### MEMBER_POINT_LADDER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_LADDER_D_ID | 主键 | GUID | Y | Y |
| 3 | POINT_BASE_VALUE | 积分基数 | number(16,4) | Y |  |
| 4 | UNIT_POINT | 单位积分 | number(16,4) | Y |  |
| 5 | PRESENT_POINT | 额外赠送积分 | number(16,4) | Y |  |
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
| 31 | MEMBER_POINT_RULE_ID |  | GUID | Y |  |

### MEMBER_POINT_MMR_DAY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_MMR_DAY_D_ID | 主键 | GUID | Y | Y |
| 3 | BEFORE_DAYS | 纪念日前天数 | number(7,3) | Y |  |
| 4 | AFTER_DAYS | 纪念日后天数 | number(7,3) | Y |  |
| 5 | POINT_MULTIPLE | 积分倍数 | number(16,4) | Y |  |
| 6 | PRESENT_POINT | 额外赠送积分 | number(16,4) | Y |  |
| 7 | MEMORIAL_DAY_ID | 会员纪念日 | GUID | Y |  |
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
| 33 | MEMBER_POINT_RULE_ID |  | GUID | Y |  |

### MEMBER_POINT_MODIFY_DOC (会员积分增减单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | MEMBER_POINT_MODIFY_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | DATA_SOURCE_TYPE | 数据来源 | string(40) | Y |  |
| 10 | SHOP_ID | 门店 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | PrintCount | 打印次数 | number | Y |  |
| 13 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 14 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 15 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 16 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 17 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 18 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 19 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 20 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 21 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 22 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 23 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 24 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 25 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 26 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 27 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 28 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 29 | UDF041 | 自定义字段12 | date | Y |  |
| 30 | UDF042 | 自定义字段13 | date | Y |  |
| 31 | UDF051 | 自定义字段14 | GUID | Y |  |
| 32 | UDF052 | 自定义字段15 | GUID | Y |  |
| 33 | UDF053 | 自定义字段16 | GUID | Y |  |
| 34 | UDF054 | 自定义字段17 | GUID | Y |  |
| 35 | CreateDate | 创建日期 | date | Y |  |
| 36 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 37 | ModifiedDate | 修改日期 | date | Y |  |
| 38 | CreateBy | 创建者 | GUID | Y |  |
| 39 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 40 | ModifiedBy | 修改者 | GUID | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 43 | Version | 版本号，不要随意更改 | binary | Y |  |
| 44 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 45 | ApproveDate | 修改日期 | date | Y |  |
| 46 | ApproveBy | 修改人 | GUID | Y |  |
| 47 | Owner_Org_RTK |  | string(400) | Y |  |
| 48 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_POINT_MODIFY_DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_MODIFY_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | MEMBER_ID | 会员号 | GUID | Y |  |
| 4 | POINT_CHANGE_TYPE | 增减积分类型 | string(40) | Y |  |
| 5 | SALE_DOC_ID | 零售单据号 | string(40) | Y |  |
| 6 | POINT | 积分 | number(16,4) | Y |  |
| 7 | RESON_REMARK | 原因说明 | string(510) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
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
| 34 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 35 | ApproveDate | 修改日期 | date | Y |  |
| 36 | ApproveBy | 修改人 | GUID | Y |  |
| 37 | MEMBER_POINT_MODIFY_DOC_ID |  | GUID | Y |  |

### MEMBER_POINT_PAYMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_PAYMENT_D_ID | 主键 | GUID | Y | Y |
| 3 | SALE_PAYTYPE_ID | 主键 | GUID | Y |  |
| 4 | POINT_BASE_VALUE | 积分基数 | number(16,4) | Y |  |
| 5 | UNIT_POINT | 单位积分 | number(16,4) | Y |  |
| 6 | PRESENT_POINT | 额外赠送积分 | number(16,4) | Y |  |
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
| 32 | MEMBER_POINT_RULE_ID |  | GUID | Y |  |

### MEMBER_POINT_RULE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_POINT_RULE_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_POINT_RULE_CODE | 积分策略编号 | string(40) | Y |  |
| 5 | MEMBER_POINT_RULE_NAME | 积分策略名称 | string(120) | Y |  |
| 6 | MEMBER_GROUP_ID | 主键 | GUID | Y |  |
| 7 | POINT_RULE_TYPE | 积分策略类型 | string(40) | Y |  |
| 8 | POINT_CALC_TYPE | 积分计算取整方式 | string(40) | Y |  |
| 9 | IS_BASE | 基准 | number(0/1) | Y |  |
| 10 | BEGIN_DATE | 生效日期 | date | Y |  |
| 11 | END_DATE | 失效日期 | date | Y |  |
| 12 | SHOP_RANGE | 生效门店范围 | string(40) | Y |  |
| 13 | POINT_BASE_VALUE | 积分基数 | number(16,4) | Y |  |
| 14 | UNIT_POINT | 单位积分 | number(16,4) | Y |  |
| 15 | PRESENT_POINT | 额外赠送积分 | number(16,4) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | ITEM_GROUP_TYPE | 品类积分方式 | string(40) | Y |  |
| 18 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
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

### MEMBER_POINT_SHOP_LIST

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_POINT_SHOP_LIST_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 主键 | GUID | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 29 | MEMBER_POINT_RULE_ID |  | GUID | Y |  |

### MEMBER_PRICE_DISCOUNT (会员品类价格设定)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_PRICE_DISCOUNT_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_BRAND_FUTURE | 品牌属性 | GUID | Y |  |
| 4 | ITEM_CATEGORY_FUTURE | 分类属性 | GUID | Y |  |
| 5 | MEMBER_PRICE_DISCOUNT_TYPE | 取价方法 | string(40) | Y |  |
| 6 | MEMBER_DISCOUNT |  | number(5,4) | Y |  |
| 7 | MEMBER_PRICE_ITEM | 会员价 | string(4) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 33 | Version | 版本号，不要随意更改 | binary | Y |  |
| 34 | MEMBER_GROUP_ID |  | GUID | Y |  |

### MEMBER_RECHARGE_ITEM (会员充值赠品明细表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_RECHARGE_ITEM_ID | 主键 | GUID | Y | Y |
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
| 30 | MEMBER_RECHARGE_RULE_ID |  | GUID | Y |  |

### MEMBER_RECHARGE_ITEM_SD (会员充值赠品列表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_RECHARGE_ITEM_SD_ID | 主键 | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NUM |  | number(16,6) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SALE_UNIT_ID | 零售单位 | GUID | Y |  |
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
| 32 | MEMBER_RECHARGE_ITEM_ID |  | GUID | Y |  |

### MEMBER_RECHARGE_LADDER (会员充值阶梯赠送)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_RECHARGE_LADDER_ID | 主键 | GUID | Y | Y |
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
| 31 | MEMBER_RECHARGE_RULE_ID |  | GUID | Y |  |

### MEMBER_RECHARGE_POINT (会员充值赠积分明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_RECHARGE_POINT_ID | 主键 | GUID | Y | Y |
| 3 | RECHARGE_MONEY | 充值金额 | number(23,8) | Y |  |
| 4 | PRESENT_POINTS | 赠送积分 | number(16,4) | Y |  |
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
| 31 | MEMBER_RECHARGE_RULE_ID |  | GUID | Y |  |

### MEMBER_RECHARGE_RULE (会员充值策略)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_RECHARGE_RULE_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_RECHARGE_RULE_CODE | 充值策略编号 | string(40) | Y |  |
| 5 | MEMBER_RECHARGE_RULE_NAME | 充值策略名称 | string(200) | Y |  |
| 6 | RECHARGE_TYPE | 充值策略类型 | string(40) | Y |  |
| 7 | IS_BASE | 基准 | number(0/1) | Y |  |
| 8 | SHOP_RANGE | 生效门店范围 | string(40) | Y |  |
| 9 | BEGIN_DATE | 生效日期 | date | Y |  |
| 10 | END_DATE | 失效日期 | date | Y |  |
| 11 | RECHARGE_MIN_MONEY | 最低充值金额 | number(23,8) | Y |  |
| 12 | RECHARGE_MULTIPLE_MONEY | 充值倍额 | number(23,8) | Y |  |
| 13 | RECHARGE_FACE_MONEY | 充值面额 | number(23,8) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 16 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
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

### MEMBER_RECHARGE_SHOP (会员充值策略生效门店列表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOP_ID | 门店编号 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | MEMBER_RECHARGE_SHOP_ID | 主键 | GUID | Y | Y |
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
| 30 | MEMBER_RECHARGE_RULE_ID |  | GUID | Y |  |

### MEMBER_RECHARGE_TICKET (会员充值赠券明细表)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_RECHARGE_TICKET_ID | 主键 | GUID | Y | Y |
| 3 | RECHARGE_MONEY | 充值金额 | number(23,8) | Y |  |
| 4 | TICKET_GROUP_ID | 券类型 | GUID | Y |  |
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
| 32 | MEMBER_RECHARGE_RULE_ID |  | GUID | Y |  |

### MEMBER_TO_MONEY_DOC

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | MEMBER_TO_MONEY_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | MEMBER_ID | 会员编号 | GUID | Y |  |
| 11 | CARD_ID | 卡ID | GUID | Y |  |
| 12 | MEMBER_TO_MONEY_RULE_ID | 积分换购策略编号 | GUID | Y |  |
| 13 | POINT_BASE_VALUE | 积分基数 | number(16,4) | Y |  |
| 14 | TO_MONEY | 单位金额 | number(23,8) | Y |  |
| 15 | POINT | 积分 | number(16,4) | Y |  |
| 16 | MONEY |  | number(23,8) | Y |  |
| 17 | REMARK | 备注 | string(510) | Y |  |
| 18 | POS_ID | POS机号 | GUID | Y |  |
| 19 | MEMBER_CODE | 会员编号 | string(400) | Y |  |
| 20 | MEMBER_NAME | 会员姓名 | string(80) | Y |  |
| 21 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 22 | VALID_POINTS | 会员可用积分 | number(16,4) | Y |  |
| 23 | CARD_CODE | 卡号 | string(80) | Y |  |
| 24 | CARD_ENCRYPT_KEY | 卡内号 | string(80) | Y |  |
| 25 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 26 | CARD_STATUS | 卡状态 | string(40) | Y |  |
| 27 | CARD_AMOUNT | 卡余额 | number(23,8) | Y |  |
| 28 | CLASS_ID | 班次号 | number | Y |  |
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

### MEMBER_TO_MONEY_RULE (会员积分转储策略)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_TO_MONEY_RULE_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_TO_MONEY_RULE_CODE | 积分转储策略编号 | string(40) | Y |  |
| 5 | MEMBER_TO_MONEY_RULE_NAME | 积分转储策略名称 | string(200) | Y |  |
| 6 | IS_BASE | 是否基准 | number(0/1) | Y |  |
| 7 | SHOP_RANGE | 生效门店范围 | string(40) | Y |  |
| 8 | BEGIN_DATE | 生效日期 | date | Y |  |
| 9 | END_DATE | 失效日期 | date | Y |  |
| 10 | POINT_BASE_VALUE | 积分基数 | number(16,4) | Y |  |
| 11 | TO_MONEY | 转储金额 | number(16,4) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
| 14 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 23 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 24 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 25 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 26 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 27 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 28 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 29 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 30 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 31 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 32 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 33 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 34 | UDF041 | 自定义字段12 | date | Y |  |
| 35 | UDF042 | 自定义字段13 | date | Y |  |
| 36 | UDF051 | 自定义字段14 | GUID | Y |  |
| 37 | UDF052 | 自定义字段15 | GUID | Y |  |
| 38 | UDF053 | 自定义字段16 | GUID | Y |  |
| 39 | UDF054 | 自定义字段17 | GUID | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | Owner_Org_RTK |  | string(400) | Y |  |
| 46 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_TO_MONEY_SHOP_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_TO_MONEY_SHOP_D_ID | 主键 | GUID | Y | Y |
| 3 | SHOP_ID | 门店编号 | GUID | Y |  |
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
| 30 | MEMBER_TO_MONEY_RULE_ID |  | GUID | Y |  |

### MEMBER_UPGRADE_CONDITION

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_UPGRADE_CONDITION_ID | 主键 | GUID | Y | Y |
| 3 | MEMBER_UPGRADE_CONDITION_ITEM | 升级条件 | string(40) | Y |  |
| 4 | CONDITION_VALUE | 条件值 | number(23,8) | Y |  |
| 5 | CONDITION_LOGIC | 逻辑关系 | string(40) | Y |  |
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
| 31 | MEMBER_UPGRADE_SEQUENCE_ID |  | GUID | Y |  |

### MEMBER_UPGRADE_RULE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | MEMBER_UPGRADE_RULE_ID | 主键 | GUID | Y | Y |
| 4 | MEMBER_UPGRADE_RULE_CODE | 升级策略编号 | string(20) | Y |  |
| 5 | MEMBER_UPGRADE_RULE_NAME | 升级策略名称 | string(120) | Y |  |
| 6 | BEGIN_DATE | 生效日期 | date | Y |  |
| 7 | END_DATE | 失效日期 | date | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
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
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### MEMBER_UPGRADE_SEQUENCE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | MEMBER_UPGRADE_SEQUENCE_ID | 主键 | GUID | Y | Y |
| 3 | BEFORE_MEMBER_GROUP_ID | 主键 | GUID | Y |  |
| 4 | AFTER_MEMBER_GROUP_ID | 主键 | GUID | Y |  |
| 5 | UPGRADE_DECREASE_POINTS | 升级扣减积分 | number(9,4) | Y |  |
| 6 | UPGRADE_POINT_TRANSFER_RATE | 升级后积分换算比率 | number(5,4) | Y |  |
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
| 32 | MEMBER_UPGRADE_RULE_ID |  | GUID | Y |  |