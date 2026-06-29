---
module: "SHOPPE"
name_zh: "门店费用"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 19
columns: 997
category: sales
tags: ["ERP", "E10", "sales"]
created: 2026-06-25 10:52
---

# SHOPPE (门店费用)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 19 | Columns: 997

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


- **SHOPPE_CHARGE (专柜费用类型信息)**
- **SHOPPE_CHARGE_DOC (专柜费用单)**
- **SHOPPE_CHARGE_DOC_D (专柜费用单明细)**
- **SHOPPE_CONTRACT (专柜合同通用信息)**
- **SHOPPE_CONTRACT_BD (专柜合同保底信息)**
- **SHOPPE_CONTRACT_CHARGE (专柜合同费用信息)**
- **SHOPPE_CONTRACT_DOC (维护专柜合同变更单通用信息)**
- **SHOPPE_CONTRACT_DOC_D (维护专柜合同变更单费用信息)**
- **SHOPPE_CONTRACT_DOC_D1 (维护专柜合同变更单保底信息)**
- **SHOPPE_CONTRACT_DOC_D2 (维护专柜合同变更单清算信息)**
- **SHOPPE_CONTRACT_QS (专柜合同清算信息)**
- **SHOPPE_MARKET_GOODS (专柜商场码信息)**
- **SHOPPE_MKT_GDS_KL_DOC (专柜商品商场码扣率调整单)**
- **SHOPPE_MKT_GDS_KL_DOC_D (专柜商品商场码扣率调整单明细)**
- **SHOPPE_SETTLE_DOC (专柜结算单)**
- **SHOPPE_SETTLE_DOC_CHARGE (专柜结算单费用明细)**
- **SHOPPE_SETTLE_DOC_SALE (专柜结算单销售成本明细)**
- **SHOPPE_SETTLE_QS_DOC (专柜清算单)**
- **SHOPPE_SETTLE_QS_DOC_D (专柜清算单结算保底明细)**


---


---


> Tables: 19

### SHOPPE_CHARGE (专柜费用类型信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOPPE_CHARGE_ID | 主键 | GUID | Y | Y |
| 4 | SHOPPE_CHARGE_CODE | 费用编号 | string(20) | Y |  |
| 5 | SHOPPE_CHARGE_NAME | 名称 | string(200) | Y |  |
| 6 | INVOICE_FLAG | 票扣 | number(0/1) | Y |  |
| 7 | RETURN_FLAG | 返还型费用 | number(0/1) | Y |  |
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

### SHOPPE_CHARGE_DOC (专柜费用单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SHOPPE_CHARGE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | HANDNO | 手工单号 | string(80) | Y |  |
| 9 | SHOPPE_SETTLE_STATUS | 结算状态 | string(40) | Y |  |
| 10 | SHOP_ID | 直营专柜 | GUID | Y |  |
| 11 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 12 | JS_DATE | 费用结算日 | date | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
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

### SHOPPE_CHARGE_DOC_D (专柜费用单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CHARGE_DOC_D_ID |  | GUID | Y | Y |
| 3 | SHOPPE_CHARGE_ID | 费用项目编号 | GUID | Y |  |
| 4 | CHARGE_DESCRIBE | 费用描述 | string(100) | Y |  |
| 5 | CHARGE_AMT | 费用金额 | number(23,8) | Y |  |
| 6 | TAX_ID | 税种 | GUID | Y |  |
| 7 | TAX_RATE |  | number(5,4) | Y |  |
| 8 | CHARGE_TAX_AMT | 税额 | number(23,8) | Y |  |
| 9 | FH_DATE | 返还日期 | date | Y |  |
| 10 | INVOICE_FLAG | 票扣 | number(0/1) | Y |  |
| 11 | RETURN_FLAG | 返还型费用 | number(0/1) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
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
| 31 | CreateDate | 创建日期 | date | Y |  |
| 32 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 33 | ModifiedDate | 修改日期 | date | Y |  |
| 34 | CreateBy | 创建者 | GUID | Y |  |
| 35 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 36 | ModifiedBy | 修改者 | GUID | Y |  |
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | SHOPPE_CHARGE_DOC_ID |  | GUID | Y |  |

### SHOPPE_CONTRACT (专柜合同通用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOPPE_CONTRACT_ID | 主键 | GUID | Y | Y |
| 4 | SHOPPE_CONTRACT_CODE | 合同编号 | string(40) | Y |  |
| 5 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 6 | CONTRACT_STATUS | 合同状态 | string(40) | Y |  |
| 7 | BEGDT | 起始日期 | date | Y |  |
| 8 | ENDDT | 截止日期 | date | Y |  |
| 9 | BRAND | 经营品牌 | string(200) | Y |  |
| 10 | CLASS | 经营品类 | string(200) | Y |  |
| 11 | KL1 | 默认扣率 | number(5,4) | Y |  |
| 12 | KL2 |  | number(5,4) | Y |  |
| 13 | KL3 | 扣率3 | number(5,4) | Y |  |
| 14 | KL4 | 扣率4 | number(5,4) | Y |  |
| 15 | KL5 | 扣率5 | number(5,4) | Y |  |
| 16 | KL6 | 扣率6 | number(5,4) | Y |  |
| 17 | BDFX_MODE | 保底方向 | string(40) | Y |  |
| 18 | BD_MODE | 保底方式 | string(40) | Y |  |
| 19 | BDCE_MODE | 保底超额方式 | string(40) | Y |  |
| 20 | BD_TIME | 保底期间段 | string(40) | Y |  |
| 21 | PAY_MODE | 结算支付方式 | number | Y |  |
| 22 | JSDAY_MODE | 结算日类型 | string(40) | Y |  |
| 23 | JS_DAY | 结算日 | number | Y |  |
| 24 | PAY_MONTHS | 付款条件-结算后月数 | number | Y |  |
| 25 | PAY_DAY | 付款条件-结算后日 | number | Y |  |
| 26 | LAST_JS_DATE | 上次结算日期 | date | Y |  |
| 27 | LAST_QS_DATE | 上次清算日期 | date | Y |  |
| 28 | SHOP_SIGNER | 专柜方签约人 | string(40) | Y |  |
| 29 | MARKET_SIGNER | 商场方签约人 | string(40) | Y |  |
| 30 | REMARK | 备注 | string(510) | Y |  |
| 31 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 32 | CURRENCY_ID | 结算币种 | GUID | Y |  |
| 33 | TAX_ID | 税种 | GUID | Y |  |
| 34 | TAX_RATE |  | number(5,4) | Y |  |
| 35 | SHOP_ID | 直营专柜 | GUID | Y |  |
| 36 | CreateDate | 创建日期 | date | Y |  |
| 37 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 38 | ModifiedDate | 修改日期 | date | Y |  |
| 39 | CreateBy | 创建者 | GUID | Y |  |
| 40 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 41 | ModifiedBy | 修改者 | GUID | Y |  |
| 42 | Attachments | 附件 | string | Y |  |
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
| 61 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 62 | Version | 版本号，不要随意更改 | binary | Y |  |
| 63 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 64 | ApproveDate | 修改日期 | date | Y |  |
| 65 | ApproveBy | 修改人 | GUID | Y |  |
| 66 | Owner_Org_RTK |  | string(400) | Y |  |
| 67 | Owner_Org_ROid |  | GUID | Y |  |

### SHOPPE_CONTRACT_BD (专柜合同保底信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CONTRACT_BD_ID | 主键 | GUID | Y | Y |
| 3 | EFF_DATE | 生效日期 | date | Y |  |
| 4 | INVA_DATE | 失效日期 | date | Y |  |
| 5 | BD_SALE_AMT | 保底销售额 | number(23,8) | Y |  |
| 6 | BDKL |  | number(5,4) | Y |  |
| 7 | BDML | 保底毛利 | number(23,8) | Y |  |
| 8 | BDZB1 | 超额指标1 | number(23,8) | Y |  |
| 9 | BDKL1 | 超额扣率1 | number(5,4) | Y |  |
| 10 | BDZB2 |  | number(23,8) | Y |  |
| 11 | BDKL2 |  | number(5,4) | Y |  |
| 12 | BDZB3 | 超额指标3 | number(23,8) | Y |  |
| 13 | BDKL3 | 超额扣率3 | number(5,4) | Y |  |
| 14 | BDZB4 | 超额指标4 | number(23,8) | Y |  |
| 15 | BDKL4 | 超额扣率4 | number(5,4) | Y |  |
| 16 | BDZB5 | 超额指标5 | number(23,8) | Y |  |
| 17 | BDKL5 | 超额扣率5 | number(5,4) | Y |  |
| 18 | BDZB6 | 超额指标6 | number(23,8) | Y |  |
| 19 | BDKL6 | 超额扣率6 | number(5,4) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | CLOSE | 结束码 | string(40) | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | SHOPPE_CONTRACT_ID |  | GUID | Y |  |

### SHOPPE_CONTRACT_CHARGE (专柜合同费用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CONTRACT_CHARGE_ID | 主键 | GUID | Y | Y |
| 3 | JS_FREQUENCE | 结算频率 | string(40) | Y |  |
| 4 | EFF_DATE | 生效日期 | date | Y |  |
| 5 | INVA_DATE | 失效日期 | date | Y |  |
| 6 | RET_DATE | 返还日期 | date | Y |  |
| 7 | MONEY |  | number(23,8) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | SHOPPE_CHARGE_ID | 主键 | GUID | Y |  |
| 10 | INVOICE_FLAG | 票扣 | number(0/1) | Y |  |
| 11 | RETURN_FLAG | 返还型费用 | number(0/1) | Y |  |
| 12 | CLOSE | 结束码 | string(40) | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 37 | Version | 版本号，不要随意更改 | binary | Y |  |
| 38 | SHOPPE_CONTRACT_ID |  | GUID | Y |  |

### SHOPPE_CONTRACT_DOC (维护专柜合同变更单通用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SHOPPE_CONTRACT_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | CHANGE_DATE | 变更日期 | date | Y |  |
| 9 | CHANGE_EMP | 变更人 | string(80) | Y |  |
| 10 | CHANGE_CAUSE | 变更原因 | string(510) | Y |  |
| 11 | CHANGE_VERSION | 变更版本 | string(4) | Y |  |
| 12 | SHOPPE_CONTRACT_ID | 合同编号 | GUID | Y |  |
| 13 | SHOP_ID | 直营专柜编号 | GUID | Y |  |
| 14 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 15 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 16 | CURRENCY_ID | 结算币种 | GUID | Y |  |
| 17 | CONTRACT_STATUS | 合同状态 | string(40) | Y |  |
| 18 | BEGDT | 起始日期 | date | Y |  |
| 19 | ENDDT | 截止日期 | date | Y |  |
| 20 | BRAND | 经营品牌 | string(200) | Y |  |
| 21 | CLASS | 经营品类 | string(200) | Y |  |
| 22 | KL1 | 默认扣率 | number(5,4) | Y |  |
| 23 | KL2 | 扣率2 | number(5,4) | Y |  |
| 24 | KL3 | 扣率3 | number(5,4) | Y |  |
| 25 | KL4 | 扣率4 | number(5,4) | Y |  |
| 26 | KL5 | 扣率5 | number(5,4) | Y |  |
| 27 | KL6 | 扣率6 | number(5,4) | Y |  |
| 28 | BDFX_MODE | 保底方向 | string(40) | Y |  |
| 29 | BD_MODE | 保底方式 | string(40) | Y |  |
| 30 | BDCE_MODE | 保底超额方式 | string(40) | Y |  |
| 31 | BD_TIME | 保底期间段 | string(40) | Y |  |
| 32 | PAY_MODE | 结算支付方式 | number | Y |  |
| 33 | TAX_ID | 税种 | GUID | Y |  |
| 34 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 35 | JSDAY_MODE | 结算日类型 | string(40) | Y |  |
| 36 | JS_DAY | 结算日 | number | Y |  |
| 37 | PAY_MONTHS | 付款条件-结算后月数 | number | Y |  |
| 38 | PAY_DAY | 付款条件-结算后日 | number | Y |  |
| 39 | LAST_JS_DATE | 上次结算日期 | date | Y |  |
| 40 | LAST_QS_DATE | 上次清算日期 | date | Y |  |
| 41 | SHOP_SIGNER | 专柜方签约人 | string(40) | Y |  |
| 42 | MARKET_SIGNER | 商场方签约人 | string(40) | Y |  |
| 43 | REMARK | 备注 | string(510) | Y |  |
| 44 | ORI_CONTRACT_STATUS | 原合同状态 | string(40) | Y |  |
| 45 | ORI_COMPANY_ID | 原结算公司 | GUID | Y |  |
| 46 | ORI_CURRENCY_ID | 原结算币种 | GUID | Y |  |
| 47 | ORI_BEGDT | 原起始日期 | date | Y |  |
| 48 | ORI_ENDDT | 原截止日期 | date | Y |  |
| 49 | ORI_KL1 | 原默认扣率 | number(5,4) | Y |  |
| 50 | ORI_BDFX_MODE | 原保底方向 | string(40) | Y |  |
| 51 | ORI_BD_MODE | 原保底方式 | string(40) | Y |  |
| 52 | ORI_BDCE_MODE | 原保底超额方式 | string(40) | Y |  |
| 53 | ORI_BD_TIME | 原保底期间段 | string(40) | Y |  |
| 54 | ORI_PAY_MODE | 原结算支付方式 | string(40) | Y |  |
| 55 | ORI_TAX_ID | 原税种 | GUID | Y |  |
| 56 | ORI_TAX_RATE | 原税率 | number(5,4) | Y |  |
| 57 | ORI_JSDAY_MODE | 原结算日类型 | string(40) | Y |  |
| 58 | ORI_JS_DAY | 原结算日 | number | Y |  |
| 59 | ORI_PAY_MONTHS | 原付款条件-结算后月数 | number | Y |  |
| 60 | ORI_PAY_DAY | 原付款条件-结算后日 | number | Y |  |
| 61 | ORI_SHOP_SIGNER | 原专柜方签约人 | string(40) | Y |  |
| 62 | ORI_MARKET_SIGNER | 原商场方签约人 | string(40) | Y |  |
| 63 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 64 | PrintCount | 打印次数 | number | Y |  |
| 65 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 66 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 67 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 68 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 69 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 70 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 71 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 72 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 73 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 74 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 75 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 76 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 77 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 78 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 79 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 80 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 81 | UDF041 | 自定义字段12 | date | Y |  |
| 82 | UDF042 | 自定义字段13 | date | Y |  |
| 83 | UDF051 | 自定义字段14 | GUID | Y |  |
| 84 | UDF052 | 自定义字段15 | GUID | Y |  |
| 85 | UDF053 | 自定义字段16 | GUID | Y |  |
| 86 | UDF054 | 自定义字段17 | GUID | Y |  |
| 87 | CreateDate | 创建日期 | date | Y |  |
| 88 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 89 | ModifiedDate | 修改日期 | date | Y |  |
| 90 | CreateBy | 创建者 | GUID | Y |  |
| 91 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 92 | ModifiedBy | 修改者 | GUID | Y |  |
| 93 | Attachments | 附件 | string | Y |  |
| 94 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 95 | Version | 版本号，不要随意更改 | binary | Y |  |
| 96 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 97 | ApproveDate | 修改日期 | date | Y |  |
| 98 | ApproveBy | 修改人 | GUID | Y |  |
| 99 | Owner_Org_RTK |  | string(400) | Y |  |
| 100 | Owner_Org_ROid |  | GUID | Y |  |

### SHOPPE_CONTRACT_DOC_D (维护专柜合同变更单费用信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CTRT_CHARGE_DOC_ID | 主键 | GUID | Y | Y |
| 3 | MODIFY_TYPE | 变更类型 | string(40) | Y |  |
| 4 | SHOPPE_CHARGE_ID | 费用项目编号 | GUID | Y |  |
| 5 | INVOICE_FLAG | 票扣 | number(0/1) | Y |  |
| 6 | RETURN_FLAG | 返还型费用 | number(0/1) | Y |  |
| 7 | JS_FREQUENCE | 结算频率 | string(40) | Y |  |
| 8 | EFF_DATE | 生效日期 | date | Y |  |
| 9 | INVA_DATE | 失效日期 | date | Y |  |
| 10 | RET_DATE | 返还日期 | date | Y |  |
| 11 | MONEY |  | number(23,8) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | ORI_SHOPPE_CHARGE_ID | 原费用项目编号 | GUID | Y |  |
| 14 | ORI_INVOICE_FLAG | 原票扣 | number(0/1) | Y |  |
| 15 | ORI_RETURN_FLAG | 原返还型费用 | number(0/1) | Y |  |
| 16 | ORI_JS_FREQUENCE | 原结算频率 | string(40) | Y |  |
| 17 | ORI_EFF_DATE | 原生效日期 | date | Y |  |
| 18 | ORI_INVA_DATE | 原失效日期 | date | Y |  |
| 19 | ORI_RET_DATE | 原返还日期 | date | Y |  |
| 20 | ORI_MONEY | 原金额 | number(23,8) | Y |  |
| 21 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 22 | ORI_SEQUENCENUMBER | 原序号 | GUID | Y |  |
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
| 47 | Version | 版本号，不要随意更改 | binary | Y |  |
| 48 | SHOPPE_CONTRACT_DOC_ID |  | GUID | Y |  |

### SHOPPE_CONTRACT_DOC_D1 (维护专柜合同变更单保底信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CONTRACT_BD_DOC_ID | 主键 | GUID | Y | Y |
| 3 | MODIFY_TYPE | 变更类型 | string(40) | Y |  |
| 4 | EFF_DATE | 生效日期 | date | Y |  |
| 5 | INVA_DATE | 失效日期 | date | Y |  |
| 6 | BD_SALE_AMT | 保底销售额 | number(23,8) | Y |  |
| 7 | BDKL | 保底扣率 | number(5,4) | Y |  |
| 8 | BDML | 保底毛利 | number(23,8) | Y |  |
| 9 | BDZB1 | 超额指标1 | number(23,8) | Y |  |
| 10 | BDKL1 | 超额扣率1 | number(5,4) | Y |  |
| 11 | BDZB2 | 超额指标2 | number(23,8) | Y |  |
| 12 | BDKL2 | 超额扣率2 | number(5,4) | Y |  |
| 13 | BDZB3 | 超额指标3 | number(23,8) | Y |  |
| 14 | BDKL3 | 超额扣率3 | number(5,4) | Y |  |
| 15 | BDZB4 | 超额指标4 | number(23,8) | Y |  |
| 16 | BDKL4 | 超额扣率4 | number(5,4) | Y |  |
| 17 | BDZB5 | 超额指标5 | number(23,8) | Y |  |
| 18 | BDKL5 | 超额扣率5 | number(5,4) | Y |  |
| 19 | BDZB6 | 超额指标6 | number(23,8) | Y |  |
| 20 | BDKL6 | 超额扣率6 | number(5,4) | Y |  |
| 21 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 22 | ORI_SEQUENCENUMBER | 原序号 | GUID | Y |  |
| 23 | ORI_EFF_DATE | 原生效日期 | date | Y |  |
| 24 | ORI_INVA_DATE | 原失效日期 | date | Y |  |
| 25 | ORI_BD_SALE_AMT | 原保底销售额 | number(23,8) | Y |  |
| 26 | ORI_BDKL | 原保底扣率 | number(5,4) | Y |  |
| 27 | ORI_BDML | 原保底毛利 | number(23,8) | Y |  |
| 28 | ORI_BDZB1 | 原超额指标1 | number(23,8) | Y |  |
| 29 | ORI_BDKL1 | 原超额扣率1 | number(5,4) | Y |  |
| 30 | ORI_BDZB2 | 原超额指标2 | number(23,8) | Y |  |
| 31 | ORI_BDKL2 | 原超额扣率2 | number(5,4) | Y |  |
| 32 | ORI_BDZB3 | 原超额指标3 | number(23,8) | Y |  |
| 33 | ORI_BDKL3 | 原超额扣率3 | number(5,4) | Y |  |
| 34 | ORI_BDZB4 | 原超额指标4 | number(23,8) | Y |  |
| 35 | ORI_BDKL4 | 原超额扣率4 | number(5,4) | Y |  |
| 36 | ORI_BDZB5 | 原超额指标5 | number(23,8) | Y |  |
| 37 | ORI_BDKL5 | 原超额扣率5 | number(5,4) | Y |  |
| 38 | ORI_BDZB6 | 原超额指标6 | number(23,8) | Y |  |
| 39 | ORI_BDKL6 | 原超额扣率6 | number(5,4) | Y |  |
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
| 58 | CreateDate | 创建日期 | date | Y |  |
| 59 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 60 | ModifiedDate | 修改日期 | date | Y |  |
| 61 | CreateBy | 创建者 | GUID | Y |  |
| 62 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 63 | ModifiedBy | 修改者 | GUID | Y |  |
| 64 | Version | 版本号，不要随意更改 | binary | Y |  |
| 65 | SHOPPE_CONTRACT_DOC_ID |  | GUID | Y |  |

### SHOPPE_CONTRACT_DOC_D2 (维护专柜合同变更单清算信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CONTRACT_QS_DOC_ID | 主键 | GUID | Y | Y |
| 3 | MODIFY_TYPE | 变更类型 | string(40) | Y |  |
| 4 | EFF_DATE | 生效日期 | date | Y |  |
| 5 | INVA_DATE | 失效日期 | date | Y |  |
| 6 | BD_SALE_AMT | 保底销售额 | number(23,8) | Y |  |
| 7 | BDKL | 保底扣率 | number(5,4) | Y |  |
| 8 | BDML | 保底毛利 | number(23,8) | Y |  |
| 9 | BDZB1 | 超额指标1 | number(23,8) | Y |  |
| 10 | BDKL1 | 超额扣率1 | number(5,4) | Y |  |
| 11 | BDZB2 | 超额指标2 | number(23,8) | Y |  |
| 12 | BDKL2 | 超额扣率2 | number(5,4) | Y |  |
| 13 | BDZB3 | 超额指标3 | number(23,8) | Y |  |
| 14 | BDKL3 | 超额扣率3 | number(5,4) | Y |  |
| 15 | BDZB4 | 超额指标4 | number(23,8) | Y |  |
| 16 | BDKL4 | 超额扣率4 | number(5,4) | Y |  |
| 17 | BDZB5 | 超额指标5 | number(23,8) | Y |  |
| 18 | BDKL5 | 超额扣率5 | number(5,4) | Y |  |
| 19 | BDZB6 | 超额指标6 | number(23,8) | Y |  |
| 20 | BDKL6 | 超额扣率6 | number(5,4) | Y |  |
| 21 | REMARK | 备注 | string(510) | Y |  |
| 22 | ORI_EFF_DATE | 原生效日期 | date | Y |  |
| 23 | ORI_INVA_DATE | 原失效日期 | date | Y |  |
| 24 | ORI_BD_SALE_AMT | 原保底销售额 | number(23,8) | Y |  |
| 25 | ORI_BDKL | 原保底扣率 | number(5,4) | Y |  |
| 26 | ORI_BDML | 原保底毛利 | number(23,8) | Y |  |
| 27 | ORI_BDZB1 | 原超额指标1 | number(23,8) | Y |  |
| 28 | ORI_BDKL1 | 原超额扣率1 | number(5,4) | Y |  |
| 29 | ORI_BDZB2 | 原超额指标2 | number(23,8) | Y |  |
| 30 | ORI_BDKL2 | 原超额扣率2 | number(5,4) | Y |  |
| 31 | ORI_BDZB3 | 原超额指标3 | number(23,8) | Y |  |
| 32 | ORI_BDKL3 | 原超额扣率3 | number(5,4) | Y |  |
| 33 | ORI_BDZB4 | 原超额指标4 | number(23,8) | Y |  |
| 34 | ORI_BDKL4 | 原超额扣率4 | number(5,4) | Y |  |
| 35 | ORI_BDZB5 | 原超额指标5 | number(23,8) | Y |  |
| 36 | ORI_BDKL5 | 原超额扣率5 | number(5,4) | Y |  |
| 37 | ORI_BDZB6 | 原超额指标6 | number(23,8) | Y |  |
| 38 | ORI_BDKL6 | 原超额扣率6 | number(5,4) | Y |  |
| 39 | ORI_REMARK | 原备注 | string(510) | Y |  |
| 40 | ORI_SEQUENCENUMBER | 原序号 | GUID | Y |  |
| 41 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 42 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 43 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 44 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 45 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 46 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 47 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 48 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 49 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 50 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 51 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 52 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 53 | UDF041 | 自定义字段12 | date | Y |  |
| 54 | UDF042 | 自定义字段13 | date | Y |  |
| 55 | UDF051 | 自定义字段14 | GUID | Y |  |
| 56 | UDF052 | 自定义字段15 | GUID | Y |  |
| 57 | UDF053 | 自定义字段16 | GUID | Y |  |
| 58 | UDF054 | 自定义字段17 | GUID | Y |  |
| 59 | CreateDate | 创建日期 | date | Y |  |
| 60 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 61 | ModifiedDate | 修改日期 | date | Y |  |
| 62 | CreateBy | 创建者 | GUID | Y |  |
| 63 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 64 | ModifiedBy | 修改者 | GUID | Y |  |
| 65 | Version | 版本号，不要随意更改 | binary | Y |  |
| 66 | SHOPPE_CONTRACT_DOC_ID |  | GUID | Y |  |

### SHOPPE_CONTRACT_QS (专柜合同清算信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_CONTRACT_QS_ID | 主键 | GUID | Y | Y |
| 3 | EFF_DATE | 生效日期 | date | Y |  |
| 4 | INVA_DATE | 失效日期 | date | Y |  |
| 5 | BD_SALE_AMT | 保底销售额 | number(23,8) | Y |  |
| 6 | BDKL | 保底扣率 | number(5,4) | Y |  |
| 7 | BDML | 保底毛利 | number(23,8) | Y |  |
| 8 | BDZB1 | 超额指标1 | number(23,8) | Y |  |
| 9 | BDKL1 | 超额扣率1 | number(5,4) | Y |  |
| 10 | BDZB2 | 超额指标2 | number(23,8) | Y |  |
| 11 | BDKL2 | 超额扣率2 | number(5,4) | Y |  |
| 12 | BDZB3 | 超额指标3 | number(23,8) | Y |  |
| 13 | BDKL3 | 超额扣率3 | number(5,4) | Y |  |
| 14 | BDZB4 | 超额指标4 | number(23,8) | Y |  |
| 15 | BDKL4 | 超额扣率4 | number(5,4) | Y |  |
| 16 | BDZB5 | 超额指标5 | number(23,8) | Y |  |
| 17 | BDKL5 | 超额扣率5 | number(5,4) | Y |  |
| 18 | BDZB6 | 超额指标6 | number(23,8) | Y |  |
| 19 | BDKL6 | 超额扣率6 | number(5,4) | Y |  |
| 20 | REMARK | 备注 | string(510) | Y |  |
| 21 | CLOSE | 结束码 | string(40) | Y |  |
| 22 | CreateDate | 创建日期 | date | Y |  |
| 23 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 24 | ModifiedDate | 修改日期 | date | Y |  |
| 25 | CreateBy | 创建者 | GUID | Y |  |
| 26 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 27 | ModifiedBy | 修改者 | GUID | Y |  |
| 28 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 29 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 30 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 31 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 32 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 33 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 34 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 35 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 36 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 37 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 38 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 39 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 40 | UDF041 | 自定义字段12 | date | Y |  |
| 41 | UDF042 | 自定义字段13 | date | Y |  |
| 42 | UDF051 | 自定义字段14 | GUID | Y |  |
| 43 | UDF052 | 自定义字段15 | GUID | Y |  |
| 44 | UDF053 | 自定义字段16 | GUID | Y |  |
| 45 | UDF054 | 自定义字段17 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | SHOPPE_CONTRACT_ID |  | GUID | Y |  |

### SHOPPE_MARKET_GOODS (专柜商场码信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SHOPPE_MARKET_GOODS_ID | 主键 | GUID | Y | Y |
| 4 | SHOPPE_MARKET_GOODS_CODE | 商场码编码 | string(80) | Y |  |
| 5 | GOODS_NAME | 品名 | string(200) | Y |  |
| 6 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 7 | KL | 扣率 | number(5,4) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | SHOP_ID | 直营专柜 | GUID | Y |  |
| 10 | TAX_ID | 税种 | GUID | Y |  |
| 11 | TAX_RATE | 税率 | number(5,4) | Y |  |
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

### SHOPPE_MKT_GDS_KL_DOC (专柜商品商场码扣率调整单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SHOPPE_MKT_GDS_KL_DOC_ID | 主键 | GUID | Y | Y |
| 7 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 8 | BEG_DATE | 开始日期 | date | Y |  |
| 9 | END_DATE | 结束日期 | date | Y |  |
| 10 | KL_MODIFY_RATE | 扣率默认调整幅度 | number(23,4) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SHOP_ID | 直营专柜 | GUID | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 15 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 16 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 17 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### SHOPPE_MKT_GDS_KL_DOC_D (专柜商品商场码扣率调整单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_MKT_GDS_KL_DOC_D_ID | 主键 | GUID | Y | Y |
| 3 | SHOPPE_MARKET_GOODS_ID | 专柜商场码编码 | GUID | Y |  |
| 4 | ORI_KL | 原扣率 | number(5,4) | Y |  |
| 5 | KL | 新扣率 | number(5,4) | Y |  |
| 6 | IS_PROMOTION_SALE | 特卖 | number(0/1) | Y |  |
| 7 | IS_JOIN_BD | 参与保底 | number(0/1) | Y |  |
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
| 34 | SHOPPE_MKT_GDS_KL_DOC_ID |  | GUID | Y |  |

### SHOPPE_SETTLE_DOC (专柜结算单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | SHOPPE_SETTLE_DOC_ID | 主键 | GUID | Y | Y |
| 7 | ENDDT | 结算截止日期 | date | Y |  |
| 8 | BEGDT | 结算起始日期 | date | Y |  |
| 9 | CATEGORY | 单据性质 | string(400) | Y |  |
| 10 | SHOP_ID | 直营专柜编号 | GUID | Y |  |
| 11 | MARKET_ID | 商场编号 | GUID | Y |  |
| 12 | CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 13 | SHOPPE_CONTRACT_ID | 合同编号 | GUID | Y |  |
| 14 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 15 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 16 | CURRENCY_ID | 结算币种 | GUID | Y |  |
| 17 | BDFX_MODE | 保底方向 | string(40) | Y |  |
| 18 | BD_MODE | 保底方式 | string(40) | Y |  |
| 19 | BDCE_MODE | 保底超额方式 | string(40) | Y |  |
| 20 | BD_TIME | 保底期间段 | string(40) | Y |  |
| 21 | PAY_COST_AMT | 本期应结货款 | number(23,8) | Y |  |
| 22 | PAY_COST_TAX_AMT | 本期应结货款税额 | number(23,8) | Y |  |
| 23 | PAY_INVOICE_CHARGE_AMT | 本期票扣费用 | number(23,8) | Y |  |
| 24 | PAY_INVOICE_CHARGE_TAX_AMT | 本期票扣费用税额 | number(23,8) | Y |  |
| 25 | PAY_CHARGE_AMT | 本期非票扣费用 | number(23,8) | Y |  |
| 26 | PAY_TOTAL_AMT | 应结算金额 | number(23,8) | Y |  |
| 27 | PAY_TOTAL_COST_AMT | 开票总额 | number(23,8) | Y |  |
| 28 | PAY_TOTAL_COST_TAX_AMT | 开票税额 | number(23,8) | Y |  |
| 29 | PAY_TOTAL_COST_NOTAX_AMT | 开票无税金额 | number(23,8) | Y |  |
| 30 | PAY_PLAN_DAY | 计划付款日 | date | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | PrintCount | 打印次数 | number | Y |  |
| 33 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 34 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 35 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 36 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 37 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 38 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 39 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 40 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 41 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 42 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 43 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 44 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 45 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 46 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 47 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 48 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 49 | UDF041 | 自定义字段12 | date | Y |  |
| 50 | UDF042 | 自定义字段13 | date | Y |  |
| 51 | UDF051 | 自定义字段14 | GUID | Y |  |
| 52 | UDF052 | 自定义字段15 | GUID | Y |  |
| 53 | UDF053 | 自定义字段16 | GUID | Y |  |
| 54 | UDF054 | 自定义字段17 | GUID | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | Attachments | 附件 | string | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | Version | 版本号，不要随意更改 | binary | Y |  |
| 64 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 65 | ApproveDate | 修改日期 | date | Y |  |
| 66 | ApproveBy | 修改人 | GUID | Y |  |
| 67 | Owner_Org_RTK |  | string(400) | Y |  |
| 68 | Owner_Org_ROid |  | GUID | Y |  |

### SHOPPE_SETTLE_DOC_CHARGE (专柜结算单费用明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_SETTLE_DOC_CHARGE_ID | 主键 | GUID | Y | Y |
| 3 | SETTLE_TYPE | 数据来源 | string(40) | Y |  |
| 4 | CHARGE_NO | 费用单号 | string(40) | Y |  |
| 5 | ROWNO | 费用单行号 | number | Y |  |
| 6 | SHOPPE_CHARGE_ID | 费用编号 | GUID | Y |  |
| 7 | INVOICE_FLAG | 票扣 | number(0/1) | Y |  |
| 8 | SETTLE_DAY | 费用结算日 | date | Y |  |
| 9 | CHARGE_AMT |  | number(23,8) | Y |  |
| 10 | TAX_ID | 税种 | GUID | Y |  |
| 11 | TAX_RATE |  | number(5,4) | Y |  |
| 12 | SALE_COST_TAX_AMT | 票扣税额 | number(23,8) | Y |  |
| 13 | DESCRIPTION | 说明 | string(200) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
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
| 43 | SHOPPE_SETTLE_DOC_ID |  | GUID | Y |  |

### SHOPPE_SETTLE_DOC_SALE (专柜结算单销售成本明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_SETTLE_DOC_SALE_ID | 主键 | GUID | Y | Y |
| 3 | SETTLE_TYPE | 数据来源 | string(40) | Y |  |
| 4 | SHOPPE_MARKET_GOODS_ID | 商场码 | GUID | Y |  |
| 5 | SALE_AMT | 销售收入 | number(23,8) | Y |  |
| 6 | KL | 扣率 | number(5,4) | Y |  |
| 7 | SALE_TC_AMT | 提成额 | number(23,8) | Y |  |
| 8 | SALE_COST_AMT | 销售成本 | number(23,8) | Y |  |
| 9 | TAX_ID | 税种 | GUID | Y |  |
| 10 | TAX_RATE |  | number(5,4) | Y |  |
| 11 | SALE_COST_TAX_AMT | 税额 | number(23,8) | Y |  |
| 12 | DESCRIPTION | 说明 | string(200) | Y |  |
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
| 39 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 40 | ApproveDate | 修改日期 | date | Y |  |
| 41 | ApproveBy | 修改人 | GUID | Y |  |
| 42 | SHOPPE_SETTLE_DOC_ID |  | GUID | Y |  |

### SHOPPE_SETTLE_QS_DOC (专柜清算单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | SHOPPE_SETTLE_QS_DOC_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | BEGDT | 清算起始日期 | date | Y |  |
| 9 | ENDDT | 清算截止日期 | date | Y |  |
| 10 | SHOP_ID | 直营专柜编号 | GUID | Y |  |
| 11 | MARKET_ID | 商场编号 | GUID | Y |  |
| 12 | CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 13 | SHOPPE_CONTRACT_ID | 合同编号 | GUID | Y |  |
| 14 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 15 | BDFX_MODE | 保底方向 | string(40) | Y |  |
| 16 | BD_MODE | 保底方式 | string(40) | Y |  |
| 17 | BDCE_MODE | 保底超额方式 | string(40) | Y |  |
| 18 | BD_TIME | 保底期间段 | string(40) | Y |  |
| 19 | COMPANY_ID | 结算公司 | GUID | Y |  |
| 20 | CURRENCY_ID | 结算币种 | GUID | Y |  |
| 21 | TAX_ID | 税种 | GUID | Y |  |
| 22 | TAX_RATE |  | number(5,4) | Y |  |
| 23 | BD_TC_AMT | 本期保底提成额 | number(23,8) | Y |  |
| 24 | QS_TC_AMT | 本期清算提成额 | number(23,8) | Y |  |
| 25 | PAY_ADJUST_AMT | 本期调整额 | number(23,8) | Y |  |
| 26 | PAY_TOTAL_AMT | 应结算金额 | number(23,8) | Y |  |
| 27 | PAY_TOTAL_COST_AMT | 开票总额 | number(23,8) | Y |  |
| 28 | PAY_TOTAL_COST_TAX_AMT | 开票税额 | number(23,8) | Y |  |
| 29 | PAY_TOTAL_COST_NOTAX_AMT | 开票无税金额 | number(23,8) | Y |  |
| 30 | PAY_PLAN_DAY | 计划付款日 | date | Y |  |
| 31 | SALE_AMT | 销售收入 | number(23,8) | Y |  |
| 32 | SALE_COST_AMT | 销售成本 | number(23,8) | Y |  |
| 33 | SALE_TC_AMT | 提成额 | number(23,8) | Y |  |
| 34 | DESCRIPTION | 说明 | string(200) | Y |  |
| 35 | REMARK | 备注 | string(510) | Y |  |
| 36 | QS_TC_AMOUNT | 清算提成额 | number(23,8) | Y |  |
| 37 | PrintCount | 打印次数 | number | Y |  |
| 38 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 39 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 40 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 41 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 42 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 43 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 44 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 45 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 46 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 47 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 48 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 49 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 50 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 51 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 52 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 53 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 54 | UDF041 | 自定义字段12 | date | Y |  |
| 55 | UDF042 | 自定义字段13 | date | Y |  |
| 56 | UDF051 | 自定义字段14 | GUID | Y |  |
| 57 | UDF052 | 自定义字段15 | GUID | Y |  |
| 58 | UDF053 | 自定义字段16 | GUID | Y |  |
| 59 | UDF054 | 自定义字段17 | GUID | Y |  |
| 60 | CreateDate | 创建日期 | date | Y |  |
| 61 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 62 | ModifiedDate | 修改日期 | date | Y |  |
| 63 | CreateBy | 创建者 | GUID | Y |  |
| 64 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 65 | ModifiedBy | 修改者 | GUID | Y |  |
| 66 | Attachments | 附件 | string | Y |  |
| 67 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |

### SHOPPE_SETTLE_QS_DOC_D (专柜清算单结算保底明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOPPE_SETTLE_QS_DOC_D_ID |  | GUID | Y | Y |
| 3 | BEG_END_DATE | 结算起止期 | string(50) | Y |  |
| 4 | SALE_AMT | 销售收入 | number(23,8) | Y |  |
| 5 | SALE_COST_AMT | 销售成本 | number(23,8) | Y |  |
| 6 | SALE_TC_AMT | 销售提成额 | number(23,8) | Y |  |
| 7 | BD_TC_AMT | 保底提成额 | number(23,8) | Y |  |
| 8 | DESCRIPTION | 说明 | string(200) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | SHOPPE_SETTLE_DOC_ID | 结算单号 | GUID | Y |  |
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
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | SHOPPE_SETTLE_QS_DOC_ID |  | GUID | Y |  |