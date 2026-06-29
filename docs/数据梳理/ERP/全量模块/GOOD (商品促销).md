---
module: "GOOD"
name_zh: "商品促销"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 14
columns: 513
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# GOOD (商品促销)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 14 | Columns: 513

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


- **GOOD_PROMOTION_DOC (单品促销单)**
- **GOOD_PROMOTION_DOC_D (生效门店)**
- **GOOD_PROMOTION_DOC_D1 (品号范围)**
- **GOOD_PROMOTION_DOC_D10 (满抵)**
- **GOOD_PROMOTION_DOC_D11 (租柜费用分摊)**
- **GOOD_PROMOTION_DOC_D12 (顾客范围)**
- **GOOD_PROMOTION_DOC_D2 (加价购)**
- **GOOD_PROMOTION_DOC_D3 (折扣)**
- **GOOD_PROMOTION_DOC_D4 (满减)**
- **GOOD_PROMOTION_DOC_D5 (赠券)**
- **GOOD_PROMOTION_DOC_D6 (赠券)**
- **GOOD_PROMOTION_DOC_D7 (赠品)**
- **GOOD_PROMOTION_DOC_D8 (赠品)**
- **GOOD_PROMOTION_DOC_D9 (赠卡)**


---


---


> Tables: 14

### GOOD_PROMOTION_DOC (单品促销单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | GOOD_PROMOTION_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PROMOTION_SCHEDULE_ID | 促销活动 | GUID | Y |  |
| 9 | SHOP_RANGE | 门店范围 | string(40) | Y |  |
| 10 | CUSTOMER_RANGE | 顾客范围 | string(40) | Y |  |
| 11 | BEGDT | 开始日期 | date | Y |  |
| 12 | BEGTM | 开始时间 | date | Y |  |
| 13 | ENDDT | 结束日期 | date | Y |  |
| 14 | ENDTM | 结束时间 | date | Y |  |
| 15 | WEEK_CIRCULATION | 星期循环 | number(0/1) | Y |  |
| 16 | MONDAY | 周一 | number(0/1) | Y |  |
| 17 | TUESDAY | 周二 | number(0/1) | Y |  |
| 18 | WEDNESDAY | 周三 | number(0/1) | Y |  |
| 19 | THURSDAY | 周四 | number(0/1) | Y |  |
| 20 | FRIDAY | 周五 | number(0/1) | Y |  |
| 21 | SATURDAY | 周六 | number(0/1) | Y |  |
| 22 | SUNDAY | 周日 | number(0/1) | Y |  |
| 23 | TIME_CIRCULATION | 时间循环 | number(0/1) | Y |  |
| 24 | WEEK_BEGTM | 起始时间 | date | Y |  |
| 25 | WEEK_ENDTM | 截止时间 | date | Y |  |
| 26 | PROMOTION_DESCRIPTION | 促销简述 | string(200) | Y |  |
| 27 | COUNTER_CHARGE_ID | 费用分摊类型 | GUID | Y |  |
| 28 | REMARK | 备注 | string(510) | Y |  |
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

### GOOD_PROMOTION_DOC_D (生效门店)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D_ID |  | GUID | Y | Y |
| 3 | SHOP_ID | 门店 | GUID | Y |  |
| 4 | JOIN_COUNTER | 参与租柜 | string(40) | Y |  |
| 5 | SHARE_DEFINITION | 分摊定义 | string(40) | Y |  |
| 6 | SHARE_LIMIT | 分摊限制 | string(40) | Y |  |
| 7 | LIMIT_AMT | 限制金额 | number(23,8) | Y |  |
| 8 | LIMIT_QUANTITY | 限制数量 | number(16,6) | Y |  |
| 9 | COMPENSATIN_MODE | 补偿方式 | string(40) | Y |  |
| 10 | EACH_PIECE_AMT | 每件金额 | number(23,8) | Y |  |
| 11 | AMT_RATE | 金额比率 | number(5,4) | Y |  |
| 12 | DISCOUNT_AMT_RATE | 优惠额比率 | number(5,4) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | DISCOUNT_AMT_LIST | 优惠额比率取价 | string(40) | Y |  |
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
| 40 | GOOD_PROMOTION_DOC_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D1 (品号范围)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | SHOP_LIMITED_QUANTITY | 门店限量 | number(0/1) | Y |  |
| 6 | LIMIT_QUANTITY | 限制数量 | number(16,6) | Y |  |
| 7 | SALE_PRI | 参考零售价 | number(23,8) | Y |  |
| 8 | LOW_PRICE | 特价 | number(23,8) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | GOODS_SORT | 设置方式 | string(40) | Y |  |
| 11 | CATEGORY_ID | 品类 | GUID | Y |  |
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
| 37 | GOOD_PROMOTION_DOC_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D10 (满抵)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D10_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | TOTAL_MODE | 累计方式 | string(40) | Y |  |
| 7 | FULL_AMT | 满额金额 | number(23,8) | Y |  |
| 8 | USE_AMT | 抵用金额 | number(23,8) | Y |  |
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
| 35 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D11 (租柜费用分摊)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D11_ID |  | GUID | Y | Y |
| 3 | SHOP_ID | 门店 | GUID | Y |  |
| 4 | COUNTER_ID | 租柜 | GUID | Y |  |
| 5 | SHARE_LIMIT | 分摊限制 | string(40) | Y |  |
| 6 | LIMIT_AMT | 限制金额 | number(23,8) | Y |  |
| 7 | LIMIT_QUANTITY | 限制数量 | number(16,6) | Y |  |
| 8 | COMPENSATIN_MODE | 补偿方式 | string(40) | Y |  |
| 9 | EACH_PIECE_AMT | 每件金额 | number(23,8) | Y |  |
| 10 | AMT_RATE | 金额比率 | number(5,4) | Y |  |
| 11 | DISCOUNT_AMT_RATE | 优惠额比率 | number(5,4) | Y |  |
| 12 | DISCOUNT_AMT_LIST | 优惠额比率取价 | string(40) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
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
| 32 | CreateDate | 创建日期 | date | Y |  |
| 33 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 34 | ModifiedDate | 修改日期 | date | Y |  |
| 35 | CreateBy | 创建者 | GUID | Y |  |
| 36 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 37 | ModifiedBy | 修改者 | GUID | Y |  |
| 38 | Version | 版本号，不要随意更改 | binary | Y |  |
| 39 | GOOD_PROMOTION_DOC_D_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D12 (顾客范围)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D12_ID |  | GUID | Y | Y |
| 3 | MEMBER_GROUP_ID | 会员类型 | GUID | Y |  |
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
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
| 30 | GOOD_PROMOTION_DOC_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D2 (加价购)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D2_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | TOTAL_MODE | 累计方式 | string(40) | Y |  |
| 7 | ITEM_ID | 加价购商品 | GUID | Y |  |
| 8 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 9 | INCREASE_AMT | 加价金额 | number(23,8) | Y |  |
| 10 | INCREASE_QTY | 加价购数量 | number(16,6) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
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
| 37 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D3 (折扣)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D3_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | DISCOUNT | 适用折扣 | number(5,4) | Y |  |
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
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D4 (满减)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D4_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | TOTAL_MODE | 累计方式 | string(40) | Y |  |
| 7 | FULL_REDUCTION_AMT | 满减金额 | number(23,8) | Y |  |
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
| 34 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D5 (赠券)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D5_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | TOTAL_MODE | 累计方式 | string(40) | Y |  |
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
| 26 | CreateDate | 创建日期 | date | Y |  |
| 27 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 28 | ModifiedDate | 修改日期 | date | Y |  |
| 29 | CreateBy | 创建者 | GUID | Y |  |
| 30 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 31 | ModifiedBy | 修改者 | GUID | Y |  |
| 32 | Version | 版本号，不要随意更改 | binary | Y |  |
| 33 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D6 (赠券)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D6_ID |  | GUID | Y | Y |
| 3 | TICKET_GROUP_ID | 赠券类型 | GUID | Y |  |
| 4 | TICKET_AMT | 赠券金额 | number(23,8) | Y |  |
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
| 31 | GOOD_PROMOTION_DOC_D5_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D7 (赠品)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D7_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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
| 32 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D8 (赠品)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D8_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 赠品 | GUID | Y |  |
| 4 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 5 | GIFT_QTY | 赠送数量 | number(16,6) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
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
| 32 | GOOD_PROMOTION_DOC_D7_ID |  | GUID | Y |  |

### GOOD_PROMOTION_DOC_D9 (赠卡)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | GOOD_PROMOTION_DOC_D9_ID |  | GUID | Y | Y |
| 3 | START_CALCULATION_TYPE | 起算类型 | string(40) | Y |  |
| 4 | START_CALCULATION_AMT | 起算金额 | number(23,8) | Y |  |
| 5 | START_CALCULATION_QTY | 起算数量 | number(16,6) | Y |  |
| 6 | TOTAL_MODE | 累计方式 | string(40) | Y |  |
| 7 | CARD_GROUP_ID | 赠卡类型 | GUID | Y |  |
| 8 | CARD_AMT | 赠卡金额 | number(23,8) | Y |  |
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
| 35 | GOOD_PROMOTION_DOC_D1_ID |  | GUID | Y |  |