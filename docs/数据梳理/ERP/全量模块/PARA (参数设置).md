---
module: "PARA"
name_zh: "参数设置"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 24
columns: 1098
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# PARA (参数设置)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 24 | Columns: 1098

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]

---

## Tables


- **PARA_BASESETTEMP (门店参数设置模板)**
- **PARA_BASESETTEMP_D (门店参数设置模板单身)**
- **PARA_BC_OP_EMP (维护工艺条码员工参数)**
- **PARA_COMPANY (公司参数)**
- **PARA_COMPANY_D (公司参数单身)**
- **PARA_DISTRIBUTION**
- **PARA_DOC_ALS (PARA_DOC_ALS)**
- **PARA_DOC_FIL (PARA_DOC_FIL)**
- **PARA_FIL (PARA_FIL)**
- **PARA_FIL_D (FIL参数单身)**
- **PARA_GROUP (公共参数)**
- **PARA_GROUP_BC_OP (工艺条码参数)**
- **PARA_GROUP_CRM (CRM参数设置)**
- **PARA_GROUP_CRM_1 (CRM参数设置_1)**
- **PARA_GROUP_DOC_TYPE (文件类型档)**
- **PARA_GROUP_ERPII (ERPII集成参数设置)**
- **PARA_OP_TRACK (维护生产追踪参数设定)**
- **PARA_PLANT (工厂参数)**
- **PARA_POS (POS参数)**
- **PARA_SALES_CENTER (PARA_SUPPLYE_CENTER)**
- **PARA_SERVICE_CENTER (服务域参数)**
- **PARA_SHOP (维护门店参数)**
- **PARA_SUPPLY_CENTER (采购域参数)**
- **PARA_SUPPLY_CENTER_D (采购域参数单身)**


---


---


> Tables: 24

### PARA_BASESETTEMP (门店参数设置模板)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_BASESETTEMP_ID | 主键 | GUID | Y | Y |
| 4 | ITEM | 参数名 | string(40) | Y |  |
| 5 | DEF | 默认值 | string(40) | Y |  |
| 6 | TYPE | 类型 | string(40) | Y |  |
| 7 | LENGTH | 长度 | number | Y |  |
| 8 | CHSMSG | 简体中文信息 | string(200) | Y |  |
| 9 | CHTMSG | 繁体中文信息 | string(200) | Y |  |
| 10 | ENGMSG | 英文信息 | string(200) | Y |  |
| 11 | STYPE | 设置类型 | string(40) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Attachments | 附件 | string | Y |  |
| 19 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
| 21 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 22 | ApproveDate | 修改日期 | date | Y |  |
| 23 | ApproveBy | 修改人 | GUID | Y |  |
| 24 | Owner_Org_RTK |  | string(400) | Y |  |
| 25 | Owner_Org_ROid |  | GUID | Y |  |

### PARA_BASESETTEMP_D (门店参数设置模板单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PARA_BASESETTEMP_D_ID |  | GUID | Y | Y |
| 3 | ITEM | 参数名 | string(40) | Y |  |
| 4 | ITEMVALUE | 参数值 | string(120) | Y |  |
| 5 | CHSMSG | 简体中文信息 | string(200) | Y |  |
| 6 | CHTMSG | 繁体中文信息 | string(200) | Y |  |
| 7 | ENGMSG | 英文信息 | string(200) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 16 | ApproveDate | 修改日期 | date | Y |  |
| 17 | ApproveBy | 修改人 | GUID | Y |  |
| 18 | PARA_BASESETTEMP_ID |  | GUID | Y |  |

### PARA_BC_OP_EMP (维护工艺条码员工参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_BC_OP_EMP_ID | 主键 | GUID | Y | Y |
| 4 | EMPLOYEE_ID | 员工 | GUID | Y |  |
| 5 | PLANT_ID | 工厂 | GUID | Y |  |
| 6 | BC_TYPE_BATCH_TRANSFER | (工艺整批转移)扫描条码类型 | string(40) | Y |  |
| 7 | OPERATION_ID | 默认工艺 | GUID | Y |  |
| 8 | BC_TYPE_BATCH_DISPATCH | (工艺派工)扫描条码类型 | string(40) | Y |  |
| 9 | TRANSFER_DOC_ID | (工艺整批转移)转移单类型 | GUID | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | BC_TYPE_CHECKINOUT | (上下线)扫描条码类型 | string(40) | Y |  |
| 12 | WIP_RECEIPT_DOC_ID | （工艺整批转移）工艺入库单类型 | GUID | Y |  |
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
| 45 | WORKCENTER_SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | WORKCENTER_SOURCE_ID_ROid |  | GUID | Y |  |

### PARA_COMPANY (公司参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_COMPANY_ID | 主键 | GUID | Y | Y |
| 4 | GLOB_PL_CARRY_OVER_MODE | 运营账簿-期间损益结转模式 | number | Y |  |
| 5 | GLOB_DEFAULT_EXG_TYPE | 运营账簿-默认记账汇率 | number | Y |  |
| 6 | GLOB_CASH_DEFICIT_CONTROL | 运营账簿-现金类科目赤字控制政策 | number | Y |  |
| 7 | GLOB_CASHIER_SIGN_INDICATOR | 运营账簿-出纳签字-现金及银行存款业务 | number(0/1) | Y |  |
| 8 | GLOB_FULLCASHFLOW_INDICATOR | 运营账簿-记账时必须登记完整的现金流量信息 | number(0/1) | Y |  |
| 9 | GLOB_QTY_DECIMAL_PLACE | 运营账簿-显示打印-数量小数位数 | number | Y |  |
| 10 | GLOB_PRICE_DECIMAL_PLACE | 运营账簿-显示打印-单价小数位数 | number | Y |  |
| 11 | GLOB_VOID_VOUCHER_INDICATOR | 运营账簿-允许作废凭证 | number(0/1) | Y |  |
| 12 | GLOB_VNO_AUTOFILL_INDICATOR | 运营账簿-自动填补断开的凭证号 | number(0/1) | Y |  |
| 13 | GLOB_VAMT_CHINESE_INDICATOR | 运营账簿-凭证显示中文金额 | number(0/1) | Y |  |
| 14 | GLOB_AC_FULLNAME_INDICATOR | 运营账簿-显示打印-科目全称 | number(0/1) | Y |  |
| 15 | GLOB_CS_FULLNAME_INDICATOR | 运营账簿-显示打印-客户/供应商全称 | number(0/1) | Y |  |
| 16 | GLOB_DEFAULT_DISPLAY_VSNTYPE | 运营账簿-默认显示总号类型(编码模式) | number | Y |  |
| 17 | GLMB_PL_CARRY_OVER_MODE | 管理账簿-期间损益结转模式 | number | Y |  |
| 18 | GLMB_DEFAULT_EXG_TYPE | 管理账簿-默认记账汇率 | number | Y |  |
| 19 | GLMB_CASH_DEFICIT_CONTROL | 管理账簿-现金类科目赤字控制政策 | number | Y |  |
| 20 | GLMB_CASHIER_SIGN_INDICATOR | 管理账簿-出纳签字-现金及银行存款业务 | number(0/1) | Y |  |
| 21 | GLMB_FULLCASHFLOW_INDICATOR | 管理账簿-记账时必须登记完整的现金流量信息 | number(0/1) | Y |  |
| 22 | GLMB_QTY_DECIMAL_PLACE | 管理账簿-显示打印-数量小数位数 | number | Y |  |
| 23 | GLMB_PRICE_DECIMAL_PLACE | 管理账簿-显示打印-单价小数位数 | number | Y |  |
| 24 | GLMB_VOID_VOUCHER_INDICATOR | 管理账簿-允许作废凭证 | number(0/1) | Y |  |
| 25 | GLMB_VNO_AUTOFILL_INDICATOR | 管理账簿-自动填补断开的凭证号 | number(0/1) | Y |  |
| 26 | GLMB_VAMT_CHINESE_INDICATOR | 管理账簿-凭证显示中文金额 | number(0/1) | Y |  |
| 27 | GLMB_AC_FULLNAME_INDICATOR | 管理账簿-显示打印-科目全称 | number(0/1) | Y |  |
| 28 | GLMB_CS_FULLNAME_INDICATOR | 管理账簿-显示打印-客户/供应商全称 | number(0/1) | Y |  |
| 29 | GLMB_DEFAULT_DISPLAY_VSNTYPE | 管理账簿-默认显示总号类型(编码模式) | number | Y |  |
| 30 | GLOB_VSEQ_AUTOFILL_INDICATOR | 运营账簿-自动填补断开的总号 | number(0/1) | Y |  |
| 31 | GLMB_VSEQ_AUTOFILL_INDICATOR | 管理账簿-自动填补断开的总号 | number(0/1) | Y |  |
| 32 | GLOB_INITIALIZED_INDICATOR | 运营账簿-初始化结束标识 | number(0/1) | Y |  |
| 33 | GLMB_INITIALIZED_INDICATOR | 管理账簿-初始化结束标识 | number(0/1) | Y |  |
| 34 | GLOB_CF_FROZEN_YEAR | 冻结现金流量期间_年—总账运营账簿 | string(8) | Y |  |
| 35 | GLOB_CF_FROZEN_PERIOD_CODE | 冻结现金流量期间_期号—总账运营账簿 | string(20) | Y |  |
| 36 | GLOB_CF_FROZEN_PERIOD_SEQNO | 冻结现金流量期间_序号—总账运营账簿 | number | Y |  |
| 37 | GLMB_CF_FROZEN_YEAR | 冻结现金流量期间_年—总账管理账簿 | string(8) | Y |  |
| 38 | GLMB_CF_FROZEN_PERIOD_CODE | 冻结现金流量期间_期号—总账管理账簿 | string(20) | Y |  |
| 39 | GLMB_CF_FROZEN_PERIOD_SEQNO | 冻结现金流量期间_序号—总账管理账簿 | number | Y |  |
| 40 | KEEP_OPEN_PERIOD_NUMBER | 同时连续开放会计期间数目(包括现行期间) | number | Y |  |
| 41 | OACCBOOK_START_YEAR | 启用期间_年—总账运营账簿 | string(8) | Y |  |
| 42 | MACCBOOK_START_YEAR | 启用期间_年—总账管理账簿 | string(8) | Y |  |
| 43 | AR_START_YEAR | 启用期间_年—应收 | string(8) | Y |  |
| 44 | AP_START_YEAR | 启用期间_年—应付 | string(8) | Y |  |
| 45 | CASH_START_YEAR | 启用期间_年—现金管理 | string(8) | Y |  |
| 46 | INV_START_YEAR | 启用期间_年—存货 | string(8) | Y |  |
| 47 | OACCBOOK_START_PERIOD_CODE | 启用期间_期号—总账运营账簿 | string(20) | Y |  |
| 48 | MACCBOOK_START_PERIOD_CODE | 启用期间_期号—总账管理账簿 | string(20) | Y |  |
| 49 | AR_START_PERIOD_CODE | 启用期间_期号—应收 | string(20) | Y |  |
| 50 | AP_START_PERIOD_CODE | 启用期间_期号—应付 | string(20) | Y |  |
| 51 | CASH_START_PERIOD_CODE | 启用期间_期号—现金管理 | string(20) | Y |  |
| 52 | INV_START_PERIOD_CODE | 启用期间_期号—存货 | string(20) | Y |  |
| 53 | OACCBOOK_START_PERIOD_SEQNO | 启用期间_序号—总账运营账簿 | number | Y |  |
| 54 | MACCBOOK_START_PERIOD_SEQNO | 启用期间_序号—总账管理账簿 | number | Y |  |
| 55 | AR_START_PERIOD_SEQNO | 启用期间_序号—应收 | number | Y |  |
| 56 | AP_START_PERIOD_SEQNO | 启用期间_序号—应付 | number | Y |  |
| 57 | CASH_START_PERIOD_SEQNO | 启用期间_序号—现金管理 | number | Y |  |
| 58 | INV_START_PERIOD_SEQNO | 启用期间_序号—存货 | number | Y |  |
| 59 | OACCBOOK_CURRENT_YEAR | 现行期间_年—总账运营账簿 | string(8) | Y |  |
| 60 | MACCBOOK_CURRENT_YEAR | 现行期间_年—总账管理账簿 | string(8) | Y |  |
| 61 | AR_CURRENT_YEAR | 现行期间_年—应收 | string(8) | Y |  |
| 62 | AP_CURRENT_YEAR | 现行期间_年—应付 | string(8) | Y |  |
| 63 | CASH_CURRENT_YEAR | 现行期间_年—现金管理 | string(8) | Y |  |
| 64 | INV_CURRENT_YEAR | 现行期间_年—存货 | string(8) | Y |  |
| 65 | OACCBOOK_CURRENT_PERIOD_CODE | 现行期间_期号—总账运营账簿 | string(20) | Y |  |
| 66 | MACCBOOK_CURRENT_PERIOD_CODE | 现行期间_期号—总账管理账簿 | string(20) | Y |  |
| 67 | AR_CURRENT_PERIOD_CODE | 现行期间_期号—应收 | string(20) | Y |  |
| 68 | AP_CURRENT_PERIOD_CODE | 现行期间_期号—应付 | string(20) | Y |  |
| 69 | CASH_CURRENT_PERIOD_CODE | 现行期间_期号—现金管理 | string(20) | Y |  |
| 70 | INV_CURRENT_PERIOD_CODE | 现行期间_期号—存货 | string(20) | Y |  |
| 71 | OACCBOOK_CURRENT_PERIOD_SEQNO | 现行期间_序号—总账运营账簿 | number | Y |  |
| 72 | MACCBOOK_CURRENT_PERIOD_SEQNO | 现行期间_序号—总账管理账簿 | number | Y |  |
| 73 | AR_CURRENT_PERIOD_SEQNO | 现行期间_序号—应收 | number | Y |  |
| 74 | AP_CURRENT_PERIOD_SEQNO | 现行期间_序号—应付 | number | Y |  |
| 75 | CASH_CURRENT_PERIOD_SEQNO | 现行期间_序号—现金管理 | number | Y |  |
| 76 | INV_CURRENT_PERIOD_SEQNO | 现行期间_序号—存货 | number | Y |  |
| 77 | OACCBOOK_OPEN_START_DATE | 开放日期范围起—总账运营账簿 | date | Y |  |
| 78 | MACCBOOK_OPEN_START_DATE | 开放日期范围起—总账管理账簿 | date | Y |  |
| 79 | AR_OPEN_START_DATE | 开放日期范围起—应收 | date | Y |  |
| 80 | AP_OPEN_START_DATE | 开放日期范围起—应付 | date | Y |  |
| 81 | CASH_OPEN_START_DATE | 开放日期范围起—现金管理 | date | Y |  |
| 82 | INV_OPEN_START_DATE | 开放日期范围起—存货 | date | Y |  |
| 83 | OACCBOOK_OPEN_CUTOFF_DATE | 开放日期范围止—总账运营账簿 | date | Y |  |
| 84 | MACCBOOK_OPEN_CUTOFF_DATE | 开放日期范围止—总账管理账簿 | date | Y |  |
| 85 | AR_OPEN_CUTOFF_DATE | 开放日期范围止—应收 | date | Y |  |
| 86 | AP_OPEN_CUTOFF_DATE | 开放日期范围止—应付 | date | Y |  |
| 87 | CASH_OPEN_CUTOFF_DATE | 开放日期范围止—现金管理 | date | Y |  |
| 88 | INV_OPEN_CUTOFF_DATE | 开放日期范围止—存货 | date | Y |  |
| 89 | INVENTORY_FROZEN_DATE | 存货冻结至-日期 | date | Y |  |
| 90 | SALES_DEFAULT_EXG_TYPE | 销售业务默认汇率类型 | number | Y |  |
| 91 | PUR_DEFAULT_EXG_TYPE | 采购业务默认汇率类型 | number | Y |  |
| 92 | PROVISION_ACCRUED_MODE | 坏账准备计提方式 | number | Y |  |
| 93 | PROVISION_ACCRUED_RATE | 坏账准备计提比率 | number(5,4) | Y |  |
| 94 | AR_FULLNAME_INDICATOR | 应收-结算对象显示全称 | number(0/1) | Y |  |
| 95 | AP_ESTI_REVERSE_MODE | 暂估冲回方式 | number | Y |  |
| 96 | AP_FULLNAME_INDICATOR | 应付-结算对象显示全称 | number(0/1) | Y |  |
| 97 | ACCPERIOD_DATASET_INHERIT | 新会计年度自动继承上一年度使用的会计期间表 | number(0/1) | Y |  |
| 98 | ALTER_CASHFLOW_INDICATOR | 启用备选现金流量 | number(0/1) | Y |  |
| 99 | ALTER_OACCCODE_INDICATOR | 运营账簿—启用备选科目 | number(0/1) | Y |  |
| 100 | MACCOUNT_BOOK_INDICATOR | 启用管理账簿 | number(0/1) | Y |  |
| 101 | ALTER_MACCCODE_INDICATOR | 管理账簿—启用备选科目 | number(0/1) | Y |  |
| 102 | INVENTORY_VALUATION_LEVEL | 存货评估等级 | number | Y |  |
| 103 | AR_OTOVM_INDICATOR | 应收-按单据生成凭证底稿 | number(0/1) | Y |  |
| 104 | AP_OTOVM_INDICATOR | 应付-按单据生成凭证底稿 | number(0/1) | Y |  |
| 105 | INV_OTOVM_INDICATOR | 存货-按业务单据逐张生成分录 | number(0/1) | Y |  |
| 106 | FUNCTION_CURRENCY_ID | 记账本位币 | GUID | Y |  |
| 107 | TAX_REGION_ID | 所属税区 | GUID | Y |  |
| 108 | EXCHANGE_DATASET_ID | 货币汇率表编号 | GUID | Y |  |
| 109 | CASHFLOW_DATASET_ID | 现金流量表编号 | GUID | Y |  |
| 110 | ALTER_CASHFLOW_DATASET_ID | 备选现金流量表编号 | GUID | Y |  |
| 111 | OACCCODE_DATASET_ID | 运营账簿—科目表编号 | GUID | Y |  |
| 112 | ALTER_MACCCODE_DATASET_ID | 管理账簿—备选科目表编号 | GUID | Y |  |
| 113 | ALTER_OACCCODE_DATASET_ID | 主键 | GUID | Y |  |
| 114 | MACCCODE_DATASET_ID | 主键 | GUID | Y |  |
| 115 | TRANSFER_CST_PRICING_METHOD | 跨域调拨成本取价方法 | string(40) | Y |  |
| 116 | AP_INVADJDOC_TYPE_ID | 采购价款存货调整单类型 | GUID | Y |  |
| 117 | AP_INVADJDOC_INDICATOR | 应付单审核时自动生成存货PPV调整单 | number(0/1) | Y |  |
| 118 | AP_EXP_INVADJDOC_TYPE_ID | 采购费用存货调整单类型 | GUID | Y |  |
| 119 | AP_EXP_INVADJDOC_INDICATOR | 费用分摊单审核时自动生成存货PPV调整单 | number(0/1) | Y |  |
| 120 | ESTIMATE_DOC_INDICATOR | 暂估单流程 | number(0/1) | Y |  |
| 121 | TWNM_START_YEAR | 启用期间_年—票据 | string(8) | Y |  |
| 122 | TWNM_START_PERIOD_CODE | 启用期间_期号—票据 | string(20) | Y |  |
| 123 | TWNM_START_PERIOD_SEQNO | 启用期间_序号—票据 | number | Y |  |
| 124 | TWNM_CURRENT_YEAR | 现行期间_年—票据 | string(8) | Y |  |
| 125 | TWNM_CURRENT_PERIOD_CODE | 现行期间_期号—票据 | string(20) | Y |  |
| 126 | TWNM_CURRENT_PERIOD_SEQNO | 现行期间_序号—票据 | number | Y |  |
| 127 | TWNM_OPEN_START_DATE | 开放日期范围起—票据 | date | Y |  |
| 128 | TWNM_OPEN_CUTOFF_DATE | 开放日期范围止—票据 | date | Y |  |
| 129 | BANK_WORK_CALENDAR_ID | 银行行事历 | GUID | Y |  |
| 130 | NOTE_DELIVERY_FLAG | 应付票据交付管理标志 | number(0/1) | Y |  |
| 131 | NOTE_MAIL_NAME | 票据邮寄名称 | string(144) | Y |  |
| 132 | NOTE_MAIL_ADDRESS | 票据邮寄地址 | string(510) | Y |  |
| 133 | NOTE_MAIL_PHONE | 票据邮寄电话 | string(40) | Y |  |
| 134 | NOTE_RECEIPT_MODE | 票据寄领方式 | number | Y |  |
| 135 | NOTE_MAIL_MODE | 票据邮寄方式 | number | Y |  |
| 136 | EXCHANGE_DAY_LOCAL | 交换天数-本埠 | number | Y |  |
| 137 | EXCHANGE_DAY_OTHER | 交换天数-外埠 | number | Y |  |
| 138 | AR_PSL_FLAG | 资金收付逐笔分单记账 | number(0/1) | Y |  |
| 139 | AP_PSL_FLAG | 资金收付逐笔分单记账 | number(0/1) | Y |  |
| 140 | TWNM_FULLNAME_FLAG | 台湾票据-结算对象显示全称 | number(0/1) | Y |  |
| 141 | TWNM_OTOVM_INDICATOR | 票据-按业务单据逐张生成分录 | number(0/1) | Y |  |
| 142 | TWNM_OTOVM2_INDICATOR | 票据-按单据记账日期逐张生成分录 | number(0/1) | Y |  |
| 143 | AM_FA_MEASUREMENT_MODE | 固定资产计量模式 | number | Y |  |
| 144 | AM_IA_MEASUREMENT_MODE | 无形资产计量模式 | number | Y |  |
| 145 | AM_IP_MEASUREMENT_MODE | 投资性房地产计量模式 | number | Y |  |
| 146 | AM_IMPAIRMENT_REVERSE_FLAG | 减值准备可转回标识 | number(0/1) | Y |  |
| 147 | AM_OTOVM_INDICATOR | 资产-按业务单据逐张生成分录 | number(0/1) | Y |  |
| 148 | AM_INITIALIZED_FLAG | 资产-初始化结束标识 | number(0/1) | Y |  |
| 149 | AM_START_YEAR | 启用期间_年—资产 | string(8) | Y |  |
| 150 | AM_START_PERIOD_CODE | 启用期间_期号—资产 | string(20) | Y |  |
| 151 | AM_START_PERIOD_SEQNO | 启用期间_序号—资产 | number | Y |  |
| 152 | AM_CURRENT_YEAR | 现行期间_年—资产 | string(8) | Y |  |
| 153 | AM_CURRENT_PERIOD_CODE | 现行期间_期号—资产 | string(20) | Y |  |
| 154 | AM_CURRENT_PERIOD_SEQNO | 现行期间_序号—资产 | number | Y |  |
| 155 | AM_OPEN_START_DATE | 开放日期范围起—资产 | date | Y |  |
| 156 | AM_OPEN_CUTOFF_DATE | 开放日期范围止—资产 | date | Y |  |
| 157 | AM_DEPR1_FLAG | 资产摊提标识1 | number(0/1) | Y |  |
| 158 | AM_DEPR2_FLAG | 资产摊提标识2 | number(0/1) | Y |  |
| 159 | AM_DEPR3_FLAG | 资产摊提标识3 | number(0/1) | Y |  |
| 160 | AM_DEPR4_FLAG | 资产摊提标识4 | number(0/1) | Y |  |
| 161 | AM_IDLE_DEPR_FLAG | 停用资产继续摊提标识 | number(0/1) | Y |  |
| 162 | AM_CODING_BY | 资产编号方式 | number | Y |  |
| 163 | AM_CODE_PREFIX | 资产编号前缀 | number | Y |  |
| 164 | AM_SEQUENCE_DIGIT | 资产编号流水号位数 | number | Y |  |
| 165 | AM_DEPR_RATE_DECIMAL_PLACE | 资产摊提率小数位数 | number | Y |  |
| 166 | AM_RESI_RATE_DECIMAL_PLACE | 资产残值率小数位数 | number | Y |  |
| 167 | ASSET_CATEGORY_DATASET_ID | 资产类别表 | GUID | Y |  |
| 168 | AM_UNITS_DECIMAL_PLACE | 工作量小数位数 | number | Y |  |
| 169 | NP_AUTO_APPROVE_FLAG | 应付票据自动审核标识 | number(0/1) | Y |  |
| 170 | NR_AUTO_APPROVE_FLAG | 应收票据自动审核标识 | number(0/1) | Y |  |
| 171 | TWNM_PAYMENT_DOC_TYPE_ID | 台湾票据-付款单据类型 | GUID | Y |  |
| 172 | CNNM_DEF_OUT_EXG_TYPE | 默认记账汇率类型_一般流出 | number | Y |  |
| 173 | CNNM_DEF_IN_EXG_TYPE | 默认记账汇率类型_一般流入 | number | Y |  |
| 174 | CNNM_DEF_TF_EXG_TYPE | 默认记账汇率类型_内部同货币转移 | number | Y |  |
| 175 | CNNM_START_YEAR | 启用期间_年—出纳 | string(8) | Y |  |
| 176 | CNNM_START_PERIOD_CODE | 启用期间_期号—出纳 | string(20) | Y |  |
| 177 | CNNM_START_PERIOD_SEQNO | 启用期间_序号—出纳 | number | Y |  |
| 178 | CNNM_CURRENT_YEAR | 现行期间_年—出纳 | string(8) | Y |  |
| 179 | CNNM_CURRENT_PERIOD_CODE | 现行期间_期号—出纳 | string(20) | Y |  |
| 180 | CNNM_CURRENT_PERIOD_SEQNO | 现行期间_序号—出纳 | number | Y |  |
| 181 | CNNM_OPEN_START_DATE | 开放日期范围起—出纳 | date | Y |  |
| 182 | CNNM_OPEN_CUTOFF_DATE | 开放日期范围止—出纳 | date | Y |  |
| 183 | CNNM_NOTE_BOOK_FLAG | 票据簿管理标识 | number(0/1) | Y |  |
| 184 | CNNM_INITIALIZED_FLAG | 出纳-初始化结束标识 | number(0/1) | Y |  |
| 185 | DISPLAY_INVALID_AC_FLAG | 树形开窗显示失效科目 | number(0/1) | Y |  |
| 186 | CNNM_OTOVM_INDICATOR | 出纳-按业务单据逐张生成分录 | number(0/1) | Y |  |
| 187 | CNNM_OTOVM2_INDICATOR | 出纳-按票据逐张生成分录 | number(0/1) | Y |  |
| 188 | CNNM_OTOVM3_INDICATOR | 出纳-按票据行为逐张生成分录 | number(0/1) | Y |  |
| 189 | GLRB1_PL_CARRY_OVER_MODE | 报告账簿1—期间损益结转模式 | number | Y |  |
| 190 | GLRB1_DEFAULT_EXG_TYPE | 报告账簿1—默认记账汇率类型 | number | Y |  |
| 191 | GLRB1_CASH_DEFICIT_CONTROL | 报告账簿1—现金类科目赤字控制政策 | number | Y |  |
| 192 | GLRB1_CASHIER_SIGN_INDICATOR | 报告账簿1—出纳签字—现金及银行存款业务 | number(0/1) | Y |  |
| 193 | GLRB1_FULLCASHFLOW_INDICATOR | 报告账簿1—记账时必须登记完整的现金流量信息 | number(0/1) | Y |  |
| 194 | GLRB1_QTY_DECIMAL_PLACE | 报告账簿1—显示打印—数量小数位数 | number | Y |  |
| 195 | GLRB1_PRICE_DECIMAL_PLACE | 报告账簿1—显示打印—单价小数位数 | number | Y |  |
| 196 | GLRB1_VOID_VOUCHER_INDICATOR | 报告账簿1—允许作废凭证 | number(0/1) | Y |  |
| 197 | GLRB1_VNO_AUTOFILL_INDICATOR | 报告账簿1—自动填补断开的凭证号 | number(0/1) | Y |  |
| 198 | GLRB1_VSEQ_AUTOFILL_INDICATOR | 报告账簿1—自动填补断开的总号 | number(0/1) | Y |  |
| 199 | GLRB1_VAMT_CHINESE_INDICATOR | 报告账簿1—凭证显示中文金额 | number(0/1) | Y |  |
| 200 | GLRB1_DEFAULT_DISPLAY_VSNTYPE | 报告账簿1—默认显示总号类型(编码模式) | number | Y |  |
| 201 | GLRB1_AC_FULLNAME_INDICATOR | 报告账簿1—显示打印—科目全称 | number(0/1) | Y |  |
| 202 | GLRB1_CS_FULLNAME_INDICATOR | 报告账簿1—显示打印—客户/供应商全称 | number(0/1) | Y |  |
| 203 | GLRB1_INITIALIZED_INDICATOR | 报告账簿1—初始化结束标识 | number(0/1) | Y |  |
| 204 | GLRB1_CF_FROZEN_YEAR | 报告账簿1—现金流量冻结至—期间_年 | string(8) | Y |  |
| 205 | GLRB1_CF_FROZEN_PERIOD_CODE | 报告账簿1—现金流量冻结至—期间_期号 | string(20) | Y |  |
| 206 | GLRB1_CF_FROZEN_PERIOD_SEQNO | 报告账簿1—现金流量冻结至—期间_序号 | number | Y |  |
| 207 | GLRB2_PL_CARRY_OVER_MODE | 报告账簿2—期间损益结转模式 | number | Y |  |
| 208 | GLRB2_DEFAULT_EXG_TYPE | 报告账簿2—默认记账汇率类型 | number | Y |  |
| 209 | GLRB2_CASH_DEFICIT_CONTROL | 报告账簿2—现金类科目赤字控制政策 | number | Y |  |
| 210 | GLRB2_CASHIER_SIGN_INDICATOR | 报告账簿2—出纳签字—现金及银行存款业务 | number(0/1) | Y |  |
| 211 | GLRB2_FULLCASHFLOW_INDICATOR | 报告账簿2—记账时必须登记完整的现金流量信息 | number(0/1) | Y |  |
| 212 | GLRB2_QTY_DECIMAL_PLACE | 报告账簿2—显示打印—数量小数位数 | number | Y |  |
| 213 | GLRB2_PRICE_DECIMAL_PLACE | 报告账簿2—显示打印—单价小数位数 | number | Y |  |
| 214 | GLRB2_VOID_VOUCHER_INDICATOR | 报告账簿2—允许作废凭证 | number(0/1) | Y |  |
| 215 | GLRB2_VNO_AUTOFILL_INDICATOR | 报告账簿2—自动填补断开的凭证号 | number(0/1) | Y |  |
| 216 | GLRB2_VSEQ_AUTOFILL_INDICATOR | 报告账簿2—自动填补断开的总号 | number(0/1) | Y |  |
| 217 | GLRB2_VAMT_CHINESE_INDICATOR | 报告账簿2—凭证显示中文金额 | number(0/1) | Y |  |
| 218 | GLRB2_DEFAULT_DISPLAY_VSNTYPE | 报告账簿2—默认显示总号类型(编码模式) | number | Y |  |
| 219 | GLRB2_AC_FULLNAME_INDICATOR | 报告账簿2—显示打印—科目全称 | number(0/1) | Y |  |
| 220 | GLRB2_CS_FULLNAME_INDICATOR | 报告账簿2—显示打印—客户/供应商全称 | number(0/1) | Y |  |
| 221 | GLRB2_INITIALIZED_INDICATOR | 报告账簿2—初始化结束标识 | number(0/1) | Y |  |
| 222 | GLRB2_CF_FROZEN_YEAR | 报告账簿2—现金流量冻结至—期间_年 | string(8) | Y |  |
| 223 | GLRB2_CF_FROZEN_PERIOD_CODE | 报告账簿2—现金流量冻结至—期间_期号 | string(20) | Y |  |
| 224 | GLRB2_CF_FROZEN_PERIOD_SEQNO | 报告账簿2—现金流量冻结至—期间_序号 | number | Y |  |
| 225 | RACCBOOK1_START_YEAR | 启用期间_年—总账报告账簿1 | string(8) | Y |  |
| 226 | RACCBOOK2_START_YEAR | 启用期间_年—总账报告账簿2 | string(8) | Y |  |
| 227 | RACCBOOK1_START_PERIOD_CODE | 启用期间_期号—总账报告账簿1 | string(20) | Y |  |
| 228 | RACCBOOK2_START_PERIOD_CODE | 启用期间_期号—总账报告账簿2 | string(20) | Y |  |
| 229 | RACCBOOK1_START_PERIOD_SEQNO | 启用期间_序号—总账报告账簿1 | number | Y |  |
| 230 | RACCBOOK2_START_PERIOD_SEQNO | 启用期间_序号—总账报告账簿2 | number | Y |  |
| 231 | RACCBOOK1_CURRENT_YEAR | 现行期间_年—总账报告账簿1 | string(8) | Y |  |
| 232 | RACCBOOK2_CURRENT_YEAR | 现行期间_年—总账报告账簿2 | string(8) | Y |  |
| 233 | RACCBOOK1_CURRENT_PERIOD_CODE | 现行期间_期号—总账报告账簿1 | string(20) | Y |  |
| 234 | RACCBOOK2_CURRENT_PERIOD_CODE | 现行期间_期号—总账报告账簿2 | string(20) | Y |  |
| 235 | RACCBOOK1_CURRENT_PERIOD_SEQNO | 现行期间_序号—总账报告账簿1 | number | Y |  |
| 236 | RACCBOOK2_CURRENT_PERIOD_SEQNO | 现行期间_序号—总账报告账簿2 | number | Y |  |
| 237 | RACCBOOK1_OPEN_START_DATE | 开放日期范围起—总账报告账簿1 | date | Y |  |
| 238 | RACCBOOK2_OPEN_START_DATE | 开放日期范围起—总账报告账簿2 | date | Y |  |
| 239 | RACCBOOK1_OPEN_CUTOFF_DATE | 开放日期范围止—总账报告账簿1 | date | Y |  |
| 240 | RACCBOOK2_OPEN_CUTOFF_DATE | 开放日期范围止—总账报告账簿2 | date | Y |  |
| 241 | RACCOUNT_BOOK1_INDICATOR | 启用报告账簿1 | number(0/1) | Y |  |
| 242 | RB1_FUNCTION_CURRENCY_ID | 报告账簿1—记账本位币 | GUID | Y |  |
| 243 | RB1_EXCHANGE_DATASET_ID | 报告账簿1—货币汇率表编号 | GUID | Y |  |
| 244 | RB1_CASHFLOW_DATASET_ID | 报告账簿1—现金流量表编号 | GUID | Y |  |
| 245 | RB1_ACCCODE_DATASET_ID | 报告账簿1—科目表编号 | GUID | Y |  |
| 246 | RACCOUNT_BOOK2_INDICATOR | 启用报告账簿2 | number(0/1) | Y |  |
| 247 | RB2_FUNCTION_CURRENCY_ID | 报告账簿2—记账本位币 | GUID | Y |  |
| 248 | RB2_EXCHANGE_DATASET_ID | 报告账簿2—货币汇率表编号 | GUID | Y |  |
| 249 | RB2_CASHFLOW_DATASET_ID | 报告账簿2—现金流量表编号 | GUID | Y |  |
| 250 | RB2_ACCCODE_DATASET_ID | 报告账簿2—科目表编号 | GUID | Y |  |
| 251 | ALTER_R1ACCCODE_INDICATOR | 报告账簿1—启用备选科目 | number(0/1) | Y |  |
| 252 | ALTER_R2ACCCODE_INDICATOR | 报告账簿2—启用备选科目 | number(0/1) | Y |  |
| 253 | ALTER_R1CASHFLOW_INDICATOR | 报告账簿1—启用备选现金流量 | number(0/1) | Y |  |
| 254 | ALTER_R2CASHFLOW_INDICATOR | 报告账簿2—启用备选现金流量 | number(0/1) | Y |  |
| 255 | ALTER_R1ACCCODE_DATASET_ID | 报告账簿1—备选科目表编号 | GUID | Y |  |
| 256 | ALTER_R2ACCCODE_DATASET_ID | 报告账簿2—备选科目表编号 | GUID | Y |  |
| 257 | ALTER_R1CASHFLOW_DATASET_ID | 报告账簿1—备选现金流量表编号 | GUID | Y |  |
| 258 | ALTER_R2CASHFLOW_DATASET_ID | 报告账簿2—备选现金流量表编号 | GUID | Y |  |
| 259 | DREM_FLAG | 递延收益认列使用预估模式标识 | number(0/1) | Y |  |
| 260 | DRRRNAP_FLAG | 递延收益从下期开始确认收入标识 | number(0/1) | Y |  |
| 261 | AM_TAX_DIMENSION_FLAG | 启用资产税务维度标识 | number(0/1) | Y |  |
| 262 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 263 | CreateDate | 创建日期 | date | Y |  |
| 264 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 265 | ModifiedDate | 修改日期 | date | Y |  |
| 266 | CreateBy | 创建者 | GUID | Y |  |
| 267 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 268 | ModifiedBy | 修改者 | GUID | Y |  |
| 269 | Version | 版本号，不要随意更改 | binary | Y |  |
| 270 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 271 | ApproveDate | 修改日期 | date | Y |  |
| 272 | ApproveBy | 修改人 | GUID | Y |  |
| 273 | Attachments | 附件 | string | Y |  |
| 274 | Owner_Org_RTK |  | string(400) | Y |  |
| 275 | Owner_Org_ROid |  | GUID | Y |  |
| 276 | AP_RESET_CURR_EXG_FLAG | 应付-账款核销重置现行汇率标识 | number(0/1) | Y |  |
| 277 | AR_RESET_CURR_EXG_FLAG | 应收-账款核销重置现行汇率标识 | number(0/1) | Y |  |
| 278 | PROMOTION_TRADE_RATE | 推广贸易费率 | number(5,4) | Y |  |
| 279 | PROMOTION_TRADE_EXP_ID | 推广贸易费用代号 | GUID | Y |  |
| 280 | COMMODITY_TAX_EXP_ID | 货物税额费用代号 | GUID | Y |  |
| 281 | IMPORT_TARIFF_EXP_ID | 进口关税费用代号 | GUID | Y |  |
| 282 | IMPORT_TAX_EXP_ID | 进口税额费用代号 | GUID | Y |  |
| 283 | UPDATE_PLAN_ARRIVAL_DATE | 确认预交日更新采购订单预交日 | string(40) | Y |  |
| 284 | CNNM_FULLNAME_FLAG | 出纳-结算对象显示全称 | number(0/1) | Y |  |
| 285 | TAX_INVOICE_CATEGORY_ID | 海关代徵营业税种 | GUID | Y |  |
| 286 | AM_TD_IMPAIRMENT_FLAG | 税务维度计提减值准备标识 | number(0/1) | Y |  |
| 287 | BUDGET_FLAG | 预算管理标识 | number(0/1) | Y |  |

### PARA_COMPANY_D (公司参数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_COMPANY_D_ID |  | GUID | Y | Y |
| 2 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 3 | ACCPERIOD_DATASET_ID | 会计期间表编号 | GUID | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Version | 版本号，不要随意更改 | binary | Y |  |
| 11 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 12 | ApproveDate | 修改日期 | date | Y |  |
| 13 | ApproveBy | 修改人 | GUID | Y |  |
| 14 | PARA_COMPANY_ID |  | GUID | Y |  |

### PARA_DISTRIBUTION

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_DISTRIBUTION_ID | 主键 | GUID | Y | Y |
| 4 | DISTRIBUTION_APPROVE_DATE_BY | 审核日依据 | string(40) | Y |  |
| 5 | REMARK | 备注 | string(510) | Y |  |
| 6 | SORTING | 启用分货管理 | number(0/1) | Y |  |
| 7 | DISPATCH | 启用调度管理 | number(0/1) | Y |  |
| 8 | SORTING_MODE | 分货方式 | string(40) | Y |  |
| 9 | BULK | 车辆商品体积单位 | GUID | Y |  |
| 10 | WEIGHT | 车辆商品重量单位 | GUID | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Attachments | 附件 | string | Y |  |
| 18 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 19 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 20 | ApproveDate | 修改日期 | date | Y |  |
| 21 | ApproveBy | 修改人 | GUID | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | Owner_Org_RTK |  | string(400) | Y |  |
| 24 | Owner_Org_ROid |  | GUID | Y |  |

### PARA_DOC_ALS (PARA_DOC_ALS)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_DOC_ALS_ID | 主键 | GUID | Y | Y |
| 4 | CATEGORY |  | string(400) | Y |  |
| 5 | DOC_ID | 单据性质 | GUID | Y |  |
| 6 | STOCK_ACTION |  | string(400) | Y |  |
| 7 | REMARK |  | string(510) | Y |  |
| 8 | SOURCE_DOC_ID | 单据性质 | GUID | Y |  |
| 9 | PROGRAM_NO |  | GUID | Y |  |
| 10 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 35 | Attachments | 附件 | string | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | SOURCE_OWNER_ORG_RTK |  | string(400) | Y |  |
| 43 | SOURCE_OWNER_ORG_ROid |  | GUID | Y |  |

### PARA_DOC_FIL (PARA_DOC_FIL)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_DOC_FIL_ID | 主键 | GUID | Y | Y |
| 4 | CATEGORY |  | string(400) | Y |  |
| 5 | DOC_ID | 单据性质 | GUID | Y |  |
| 6 | STOCK_ACTION |  | string(400) | Y |  |
| 7 | REMARK |  | string(510) | Y |  |
| 8 | SOURCE_DOC_ID | 单据性质 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 35 | Version | 版本号，不要随意更改 | binary | Y |  |
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |
| 41 | SOURCE_OWNER_ORG_RTK |  | string(400) | Y |  |
| 42 | SOURCE_OWNER_ORG_ROid |  | GUID | Y |  |

### PARA_FIL (PARA_FIL)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_FIL_ID | 主键 | GUID | Y | Y |
| 2 | FIL_CONTROL |  | number(0/1) | Y |  |
| 3 | BC_LINE_MANAGEMENT |  | number(0/1) | Y |  |
| 4 | BC_INVENTORY_MANAGEMENT |  | number(0/1) | Y |  |
| 5 | FIFO_CONTROL |  | string(400) | Y |  |
| 6 | CHECK_TOTAL_QTY |  | number(0/1) | Y |  |
| 7 | GENERATE_BARCODE_BY_DOC |  | number(0/1) | Y |  |
| 8 | SETTING_BY_ORGAN |  | number(0/1) | Y |  |
| 9 | PARAMETER1 |  | number(0/1) | Y |  |
| 10 | PARAMETER2 |  | string(400) | Y |  |
| 11 | OUT_QTY_DEF_INV |  | number(18,8) | Y |  |
| 12 | BARCODE_SYMBOL_FOR_WH_BIN |  | string(16) | Y |  |
| 13 | ITEM_FEATURE_CONTROL |  | number(0/1) | Y |  |
| 14 | SUPPLIER_PLATFORM_CONTROL |  | number(0/1) | Y |  |
| 15 | RANGE_OF_DOWNLOAD_BARCODE |  | string(400) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
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
| 40 | Version | 版本号，不要随意更改 | binary | Y |  |
| 41 | Attachments | 附件 | string | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |

### PARA_FIL_D (FIL参数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_FIL_D_ID |  | GUID | Y | Y |
| 4 | BC_LINE_MANAGEMENT |  | number(0/1) | Y |  |
| 5 | BC_INVENTORY_MANAGEMENT |  | number(0/1) | Y |  |
| 6 | FIFO_CONTROL |  | string(400) | Y |  |
| 7 | CHECK_TOTAL_QTY |  | number(0/1) | Y |  |
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
| 33 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 34 | ApproveDate | 修改日期 | date | Y |  |
| 35 | ApproveBy | 修改人 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |
| 38 | PARA_FIL_ID |  | GUID | Y |  |

### PARA_GROUP (公共参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_GROUP_ID | 主键 | GUID | Y | Y |
| 4 | GROUP_NAME | 集团名称 | string(144) | Y |  |
| 5 | BOM_SECRET_CONTROL | BOM保密控制 | string(40) | Y |  |
| 6 | E_ITEM_KEEP | 保留工程品号 | number(0/1) | Y |  |
| 7 | DAY_FOR_WEEK_BUCKET | 周时距归属日 | number | Y |  |
| 8 | DAY_FOR_TEN_DAYS_BUCKET | 旬时距归属日 | number | Y |  |
| 9 | DAY_FOR_MONTH_BUCKET | 月时距归属日 | number | Y |  |
| 10 | DATE_FORMAT | 日期格式 | string(40) | Y |  |
| 11 | DATE_SPACE_CODE | 日期间隔符 | string(40) | Y |  |
| 12 | ENABLE_INTEGRATE | 启用PLM集成 | number(0/1) | Y |  |
| 13 | DOC_ID | 工程变更单别 | GUID | Y |  |
| 14 | BOM_ApproveStatus | 新增BOM默认状态 | string(40) | Y |  |
| 15 | REPLACE_ApproveStatus | 新增取替代料默认状态 | string(40) | Y |  |
| 16 | Owner_Org_PUR | 默认采购域 | GUID | Y |  |
| 17 | Owner_Org_SAL | 默认销售域 | GUID | Y |  |
| 18 | Owner_Org_COM | 默认公司 | GUID | Y |  |
| 19 | CHANGE_QTY | 单张工程变更单变更BOM笔数 | number | Y |  |
| 20 | DG_SECRECY_WORD | 个资保密宣告字词 | string(510) | Y |  |
| 21 | PIC_SIZE | 图片大小 | number | Y |  |
| 22 | DG_SECRECY_WORD_CHT | 个资保密宣告字词 | string(510) | Y |  |
| 23 | ENABLE_HRM | 启用HRM集成 | number(0/1) | Y |  |
| 24 | BPM_NET_FLAG | BPM.NET集成参数 | number(0/1) | Y |  |
| 25 | ENABLE_CRM | 启用CRM集成 | number(0/1) | Y |  |
| 26 | BP_CLUSTER_ID | 生成正式客户的编码原则 | GUID | Y |  |
| 27 | REPORT_SUBSCRIPTION | 启用报表订阅 | number(0/1) | Y |  |
| 28 | ENABLE_38dee | 启用 | number(0/1) | Y |  |
| 29 | URL_ADDRESS_38dee | 外部URL | string(510) | Y |  |
| 30 | APPKEY_38dee | 连结用KEY | string(200) | Y |  |
| 31 | APPSECRET_38dee | 连结用密钥 | string(64) | Y |  |
| 32 | BROWSE_MODE | 图文查看方式 | string(40) | Y |  |
| 33 | USER_VERIFICATION | 是否验证登录 | number(0/1) | Y |  |
| 34 | COMMON_USER | 通用用户 | string(40) | Y |  |
| 35 | COMMON_PWD | 通用密码 | string(40) | Y |  |
| 36 | ENABLE_WIP | 启用WIP集成 | number(0/1) | Y |  |
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
| 51 | ENABLE_IWC | 启用IWC集成 | number(0/1) | Y |  |
| 52 | IWC_AUTHSVR | 认证地址 | string(512) | Y |  |
| 53 | IWC_APISVR | 上传服务地址 | string(512) | Y |  |
| 54 | PMC_IS_CHANGE_NOTICE | 变更主动通知 | number(0/1) | Y |  |
| 55 | PMC_SO_CHANGE_NOTICE_SET | 销售订单变更单通知人员 | string(40) | Y |  |
| 56 | PMC_ECN_NOTICE_SET | 工程变更单通知人员 | string(40) | Y |  |
| 57 | PMC_MO_CHANGE_NOTICE_SET | 工单变更单通知人员 | string(40) | Y |  |
| 58 | DG_SECRECY_WORD_ENU | 个资保密宣告字词_英文 | string(510) | Y |  |
| 59 | ENABLE_MES_INTEGRATE | 启用MES集成 | number(0/1) | Y |  |

### PARA_GROUP_BC_OP (工艺条码参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_GROUP_BC_OP_ID | 主键 | GUID | Y | Y |
| 2 | PLANT_ID | 工厂 | GUID | Y |  |
| 3 | BC_MO_INPUT | 工单投产是否启用条码 | number(0/1) | Y |  |
| 4 | BC_BATCH_TRANSFER | 工艺整批转移是否启用条码 | number(0/1) | Y |  |
| 5 | BC_TYPE_BATCH_TRANSFER | (工艺整批转移)扫描条码类型 | string(40) | Y |  |
| 6 | BC_BATCH_DISPATCH | 工艺派工是否启用条码 | number(0/1) | Y |  |
| 7 | BC_TYPE_BATCH_DISPATCH | (工艺派工)扫描条码类型 | string(40) | Y |  |
| 8 | REMARK | 备注 | string(510) | Y |  |
| 9 | TRANSFER_DOC_ID | (工艺整批转移)转移单类型 | GUID | Y |  |
| 10 | BC_CHECKINOUT | 上下线是否启用条码 | number(0/1) | Y |  |
| 11 | BC_TYPE_CHECKINOUT | (上下线)扫描条码类型 | string(40) | Y |  |
| 12 | WIP_RECEIPT_DOC_ID | （工艺整批转移）工艺入库单类型 | GUID | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
| 20 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 21 | ApproveDate | 修改日期 | date | Y |  |
| 22 | ApproveBy | 修改人 | GUID | Y |  |
| 23 | PARA_GROUP_ID |  | GUID | Y |  |

### PARA_GROUP_CRM (CRM参数设置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_GROUP_CRM_ID | 主键 | GUID | Y | Y |
| 2 | CRM_INVOICE_SOURCE | 分类 | string(40) | Y |  |
| 3 | INVOICE_FORM_CODE | CRM发票联式 | string(40) | Y |  |
| 4 | DECLARE_VAT_CODE | CRM课税别 | string(40) | Y |  |
| 5 | BUSINESS_TAX_RATE | CRM营业税率 | number(5,4) | Y |  |
| 6 | TAX_INCLUDED_INDICATOR | 含税 | number(0/1) | Y |  |
| 7 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 8 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 9 | TAX_ID | 税种 | GUID | Y |  |
| 10 | COMPANY_ID | 公司 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CUSTOMER_FICATEGORY_ID | 会计分类 | GUID | Y |  |
| 13 | CreateDate | 创建日期 | date | Y |  |
| 14 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 15 | ModifiedDate | 修改日期 | date | Y |  |
| 16 | CreateBy | 创建者 | GUID | Y |  |
| 17 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 18 | ModifiedBy | 修改者 | GUID | Y |  |
| 19 | Version | 版本号，不要随意更改 | binary | Y |  |
| 20 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 21 | ApproveDate | 修改日期 | date | Y |  |
| 22 | ApproveBy | 修改人 | GUID | Y |  |
| 23 | PARA_GROUP_ID |  | GUID | Y |  |

### PARA_GROUP_CRM_1 (CRM参数设置_1)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_GROUP_CRM_1_ID | 主键 | GUID | Y | Y |
| 2 | COMPANY_ID | 公司 | GUID | Y |  |
| 3 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 4 | ARRIVAL_PLANT_ID | 进货工厂 | GUID | Y |  |
| 5 | ARRIVAL_WAREHOUSE_ID | 进货仓库 | GUID | Y |  |
| 6 | ARRIVAL_BIN_ID | 进货库位 | GUID | Y |  |
| 7 | EXPENSE_ITEM_ID | 进货费用品号 | GUID | Y |  |
| 8 | EXPENSE_ITEM_FEATURE_ID | 进货费用特征碼 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
| 16 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 17 | ApproveDate | 修改日期 | date | Y |  |
| 18 | ApproveBy | 修改人 | GUID | Y |  |
| 19 | PARA_GROUP_ID |  | GUID | Y |  |

### PARA_GROUP_DOC_TYPE (文件类型档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_GROUP_DOC_TYPE_ID |  | GUID | Y | Y |
| 2 | CLASS | 类 | string(40) | Y |  |
| 3 | CLASSIFICATION | 分类 | string(40) | Y |  |
| 4 | DOC_TYPE | 文件类型 | string(100) | Y |  |
| 5 | OPEN_WITH | 打开方式 | string(400) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
| 13 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 14 | ApproveDate | 修改日期 | date | Y |  |
| 15 | ApproveBy | 修改人 | GUID | Y |  |
| 16 | PARA_GROUP_ID |  | GUID | Y |  |

### PARA_GROUP_ERPII (ERPII集成参数设置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PRODUCT | 产品别 | number | Y |  |
| 2 | INTERNET_PROTOCOL | IP地址 | string(510) | Y |  |
| 3 | IDENTITY | ID识别 | string(120) | Y |  |
| 4 | PARA_GROUP_ERPII_ID | 主键 | GUID | Y | Y |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 13 | ApproveDate | 修改日期 | date | Y |  |
| 14 | ApproveBy | 修改人 | GUID | Y |  |
| 15 | PARA_GROUP_ID |  | GUID | Y |  |
| 16 | ORGANIZATION_RTK |  | string(400) | Y |  |
| 17 | ORGANIZATION_ROid |  | GUID | Y |  |

### PARA_OP_TRACK (维护生产追踪参数设定)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_OP_TRACK_ID | 主键 | GUID | Y | Y |
| 4 | DISPATCH_CONTROL | 启用工艺派工 | number(0/1) | Y |  |
| 5 | WORK_CENTER_ID | 工作中心 | GUID | Y |  |
| 6 | OPERATION_ID | 工艺 | GUID | Y |  |
| 7 | CHECKIN_CONTROL | 启用上线 | number(0/1) | Y |  |
| 8 | CHECKOUT_CONTROL | 启用下线 | number(0/1) | Y |  |
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

### PARA_PLANT (工厂参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_PLANT_ID | 主键 | GUID | Y | Y |
| 4 | PLANT_APPROVE_DATE_BY | 审核日依据 | string(40) | Y |  |
| 5 | PLANT_POST_DATE_BY | 过账日依据 | string(40) | Y |  |
| 6 | COMPLETED_INCLUDE_SCRAP | 报废数量计入已完工数量 | number(0/1) | Y |  |
| 7 | COMPLETED_INCLUDE_DESTROY | 破坏数量计入已完工数量 | number(0/1) | Y |  |
| 8 | MO_AUTO_REPLACE | 工单展料自动取代 | number(0/1) | Y |  |
| 9 | SCRAP_QTY_FEEDBACK_MO | 报废数量回馈工单报废数量 | number(0/1) | Y |  |
| 10 | DESTROY_QTY_FEEDBACK_MO | 破坏数量回馈工单破坏数量 | number(0/1) | Y |  |
| 11 | LINEAR_ROUTING | 仅支持线性工艺 | number(0/1) | Y |  |
| 12 | UPDATE_LOW_LEVEL_CODE | 更新低阶码 | number(0/1) | Y |  |
| 13 | MO_URGENT_CONDITIONS | 生产急料条件 | number | Y |  |
| 14 | PR_URGENT_CONDITIONS | 采购急料条件 | number | Y |  |
| 15 | JOINT_PRODUCT_APP_MODE | 联产品成本分摊方式 | number | Y |  |
| 16 | BY_PRODUCT_APP_MODE | 副产品成本分摊方式 | number | Y |  |
| 17 | RECYCLED_MATERIAL_APP_MODE | 回收料成本分摊方式 | number | Y |  |
| 18 | WIPEU_ZERO_FLAG | 在制约量置零控制 | number(0/1) | Y |  |
| 19 | WIPEU_ZERO_START | 在制约量置零区间起始值 | number(16,6) | Y |  |
| 20 | WIPEU_ZERO_END | 在制约量置零区间终止值 | number(16,6) | Y |  |
| 21 | YEAR_DIGIT | 年位数 | string(2) | Y |  |
| 22 | ISSUE_SETS_CALC_MODE | 领料套数取值逻辑 | string(40) | Y |  |
| 23 | ISSUE_SETS_BY_CRITICAL | 依关键料计算套数 | number(0/1) | Y |  |
| 24 | COLLECT_LEVEL | 收集维度 | string(40) | Y |  |
| 25 | BY_TEAM | 班组成员报工 | string(40) | Y |  |
| 26 | ALLOWANCE_QMSYSTEM | 启用质量管理系统 | number(0/1) | Y |  |
| 27 | ALLOWANCE_SALESRETURN | 启用销退检验 | number(0/1) | Y |  |
| 28 | ALLOWANCE_RULES_ACTI | 启用转换规则 | number(0/1) | Y |  |
| 29 | CONTINUE_NORMAL_TO_DECR | 连续(正常->放宽) | number | Y |  |
| 30 | REJECT_NORMAL_TO_DECR | 拒收(正常->放宽) | number | Y |  |
| 31 | CONTINUE_NORMAL_TO_STRI | 连续(正常->加严) | number | Y |  |
| 32 | REJECT_NORMAL_TO_STRI | 拒收(正常->加严) | number | Y |  |
| 33 | CONTINUE_DECR_TO_NORMAL | 连续(放宽->正常) | number | Y |  |
| 34 | REJECT_DECR_TO_NORMAL | 拒收(放宽->正常) | number | Y |  |
| 35 | CONTINUE_STRI_TO_NORMAL | 连续(加严->正常) | number | Y |  |
| 36 | REJECT_STRI_TO_NORMAL | 拒收(加严->正常) | number | Y |  |
| 37 | CONTINUE_STRI_TO_STOP | 连续(加严->暂停检验) | number | Y |  |
| 38 | REJECT_STRI_TO_STOP | 拒收(加严->暂停检验) | number | Y |  |
| 39 | SORTING_2 | 启用分货管理 | number(0/1) | Y |  |
| 40 | SORTING_MODE_2 | 分货方式 | string(40) | Y |  |
| 41 | DISPATCH_2 | 启用调度管理 | number(0/1) | Y |  |
| 42 | BULK_ID | 车辆商品体积单位 | GUID | Y |  |
| 43 | WEIGHT_ID | 车辆商品重量单位 | GUID | Y |  |
| 44 | COLLECT_RANGE | 收集区间 | number | Y |  |
| 45 | SYNERGY_DOC_PLAN_TYPE | 协同单据计划类型 | string(40) | Y |  |
| 46 | PLANT_COLLECT_RANGE | 统计信息收集天数 | number | Y |  |
| 47 | ECN_RELEASE_TYPE | 客户BOM变更方法 | string(40) | Y |  |
| 48 | ECN_DOC_ID | 自动发布ECN单据类型 | GUID | Y |  |
| 49 | COLLECT_TIME | 收集时机 | string(40) | Y |  |
| 50 | ITEM_LOT_CONTROL | 出库单据保存时批号必填 | number(0/1) | Y |  |
| 51 | SAFE_STOCK | 安全库存 | number(0/1) | Y |  |
| 52 | RESERVE | 行政保留 | number(0/1) | Y |  |
| 53 | PRE_SALES | 预计销货 | number(0/1) | Y |  |
| 54 | PLAN_SALES | 计划销货 | number(0/1) | Y |  |
| 55 | PRE_ISSUE | 预计领料 | number(0/1) | Y |  |
| 56 | PLAN_ISSUE | 计划领料 | number(0/1) | Y |  |
| 57 | PRE_RECEIPT | 预计进货 | number(0/1) | Y |  |
| 58 | PRE_PURCHASE | 预计采购 | number(0/1) | Y |  |
| 59 | PLAN_PURCHASE | 计划采购 | number(0/1) | Y |  |
| 60 | PRE_TRANSFER_IN | 预计调入 | number(0/1) | Y |  |
| 61 | PRE_PRODUCE | 预计生产 | number(0/1) | Y |  |
| 62 | PLAN_PRODUCE | 计划生产 | number(0/1) | Y |  |
| 63 | WIP_TRANS_AUTO_PA | 工艺整批转移是否生成委外到货 | number(0/1) | Y |  |
| 64 | PA1_DOC_ID | 非质检的工艺委外到货单单据类型 | GUID | Y |  |
| 65 | PA2_DOC_ID | 质检的工艺委外到货单单据类型 | GUID | Y |  |
| 66 | COMBINE_STRATEGY | 主件结合策略 | string(40) | Y |  |
| 67 | Attachments | 附件 | string | Y |  |
| 68 | Version | 版本号，不要随意更改 | binary | Y |  |
| 69 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 70 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 71 | ApproveDate | 修改日期 | date | Y |  |
| 72 | ApproveBy | 修改人 | GUID | Y |  |
| 73 | CreateDate | 创建日期 | date | Y |  |
| 74 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 75 | ModifiedDate | 修改日期 | date | Y |  |
| 76 | CreateBy | 创建者 | GUID | Y |  |
| 77 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 78 | ModifiedBy | 修改者 | GUID | Y |  |
| 79 | Owner_Org_RTK |  | string(400) | Y |  |
| 80 | Owner_Org_ROid |  | GUID | Y |  |
| 81 | IDLE_CAPACITY_FLAG | 计算成本分配率考虑闲置产能 | number(0/1) | Y |  |
| 82 | MAINTAIN_DOC_ID | 设备维护单单别 | GUID | Y |  |
| 83 | IS_EQT_DISPATCH | 启用设备派工 | number(0/1) | Y |  |
| 84 | DEFAULT_INSP_RESULT | 自动默认巡检结果 | number(0/1) | Y |  |
| 85 | OPERATING_STATUS_ID | 非停机维护状态 | GUID | Y |  |
| 86 | SHUTDOWN_STATUS_ID | 停机维护状态 | GUID | Y |  |
| 87 | RECEIVE_STATUS_ID | 默认设备接收状态 | GUID | Y |  |
| 88 | EQT_TRANSFER_DOC_ID | 默认设备收发单单别 | GUID | Y |  |
| 89 | TRANSACTION_DOC_ID | 默认入库单单别 | GUID | Y |  |
| 90 | SEND_STATUS_ID | 默认设备发出状态 | GUID | Y |  |
| 91 | PRE_DISPATCH_CONTROL | 是否启用预派工 | number(0/1) | Y |  |
| 92 | CONTROL_COLLECT_OVERRUN | 控制报工超转移数量 | string(40) | Y |  |
| 93 | CONTROL_DISPATCH_OVERRUN | 控制超派工 | string(40) | Y |  |

### PARA_POS (POS参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_POS_ID | 主键 | GUID | Y | Y |
| 4 | KEYBOARD | 机台键盘 | string(120) | Y |  |
| 5 | POS_ID | POS机号 | GUID | Y |  |
| 6 | SHOP_ID | 门店 | GUID | Y |  |
| 7 | CNFCLERK | 是否录入营业员 | number(0/1) | Y |  |
| 8 | CNFCOUNTER | 是否录入租柜 | number(0/1) | Y |  |
| 9 | BPRINT | 是否先列印 | number(0/1) | Y |  |
| 10 | ISPRACTICE | 训练模式 | number(0/1) | Y |  |
| 11 | ESCCL | 退出时是否关机 | number(0/1) | Y |  |
| 12 | REMAINQTY | 发票目前剩余张数 | number | Y |  |
| 13 | ROWQTYPERPAGE | 发票每页列数 | number | Y |  |
| 14 | WORDQTYPERROW | 发票每列列印字数 | number | Y |  |
| 15 | PRINTGOODSTYPE | 列印商品方式 | string(120) | Y |  |
| 16 | ISPREVIEW | 发票列印预览 | number(0/1) | Y |  |
| 17 | ISPRINTBDATE | 加印营业日期 | number(0/1) | Y |  |
| 18 | ISPRINTFIRST | 先列印发票 | number(0/1) | Y |  |
| 19 | ISPRINTINVNO | 加印发票号码 | number(0/1) | Y |  |
| 20 | ISPRINTSHOPSEAL | 加印店名章 | number(0/1) | Y |  |
| 21 | ISPRINTTAXINFO | 二联式列印应/免税金额 | number(0/1) | Y |  |
| 22 | ISRECORDINVINFO | 记录发票明细 | number(0/1) | Y |  |
| 23 | ISSETPOSITION | 发票定位 | number(0/1) | Y |  |
| 24 | ISZEROPRINT | 零金额列印发票 | number(0/1) | Y |  |
| 25 | HEADSPACEROW | 发票开头间隔列数 | number | Y |  |
| 26 | INVFIXEDCONTENT1 | 发票固定内容一 | string(120) | Y |  |
| 27 | INVFIXEDCONTENT2 | 发票固定内容二 | string(120) | Y |  |
| 28 | INVFIXEDCONTENT3 | 发票固定内容三 | string(120) | Y |  |
| 29 | INVFIXEDCONTENT4 | 发票固定内容四 | string(120) | Y |  |
| 30 | INVOPENEDNO | 已开发票号码 | number | Y |  |
| 31 | INVPAPERROLL | 发票纸卷张数 | number | Y |  |
| 32 | INVREMAINWARNINGQTY | 发票剩余警告张数 | number | Y |  |
| 33 | INVTITLEITEM1 | 发票抬头内容一 | string(120) | Y |  |
| 34 | INVTITLEITEM2 | 发票抬头内容二 | string(120) | Y |  |
| 35 | INVTITLEITEM3 | 发票抬头内容三 | string(120) | Y |  |
| 36 | INVTITLEITEM4 | 发票抬头内容四 | string(120) | Y |  |
| 37 | INVTYPE | 联数 | number | Y |  |
| 38 | ISENABLEIM | 启用发票管理 | number(0/1) | Y |  |
| 39 | KEYBOARD_ID | 机台键盘ID | GUID | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### PARA_SALES_CENTER (PARA_SUPPLYE_CENTER)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_SALES_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | SALES_APPROVE_DATE_BY | 审核日依据 | string(40) | Y |  |
| 5 | SELLING_CONTROL | 销售限制策略 | string(40) | Y |  |
| 6 | SELLING_LIMIT_WAY | 允限销方式 | string(40) | Y |  |
| 7 | TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 8 | DEFAULT_PRICE_STRATEGY_ID | 默认取价策略 | GUID | Y |  |
| 9 | SALES_CENTER_TAX_REGION_ID | 税区 | GUID | Y |  |
| 10 | SALES_COMPANY_ID | 统计币种所属公司 | GUID | Y |  |
| 11 | COLLECT_RANGE | 收集区间 | number | Y |  |
| 12 | CRM_SALES_CUSTOM_TAB | 客户页签配置信息 | string(4000) | Y |  |
| 13 | EXPORT_CONTROL | 出口贸易 | number(0/1) | Y |  |
| 14 | TAX_MODE | 税额计算方式 | string(40) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |
| 24 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 25 | ApproveDate | 修改日期 | date | Y |  |
| 26 | ApproveBy | 修改人 | GUID | Y |  |
| 27 | Owner_Org_RTK |  | string(400) | Y |  |
| 28 | Owner_Org_ROid |  | GUID | Y |  |
| 29 | FINISHED_REP_SHIPMENTS | 成品替代出货 | number(0/1) | Y |  |
| 30 | IFS_GENERATE_SD_DOC_ID | 集团委外材料销货单据类型 | GUID | Y |  |
| 31 | IFS_GENERATE_RETURN_DOC_ID | 集团委外材料销退单据类型 | GUID | Y |  |

### PARA_SERVICE_CENTER (服务域参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_SERVICE_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | URGENCY_ID | 服务请求单默认紧急程度 | GUID | Y |  |
| 5 | CHECK_SERVICE | 旧件返回需核对服务处理单 | number(0/1) | Y |  |
| 6 | SERVICE_TIME | 预计服务起讫时间依据 | string(40) | Y |  |
| 7 | WARRANTY_MODE | 保修模式 | string(40) | Y |  |
| 8 | SEND_MODE | 派工方式 | string(40) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CreateDate | 创建日期 | date | Y |  |
| 11 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 12 | ModifiedDate | 修改日期 | date | Y |  |
| 13 | CreateBy | 创建者 | GUID | Y |  |
| 14 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 15 | ModifiedBy | 修改者 | GUID | Y |  |
| 16 | Attachments | 附件 | string | Y |  |
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
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Version | 版本号，不要随意更改 | binary | Y |  |
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | Owner_Org_RTK |  | string(400) | Y |  |
| 41 | Owner_Org_ROid |  | GUID | Y |  |
| 42 | INVENTORY_MODE | 服务处理单库存管理 | string(40) | Y |  |

### PARA_SHOP (维护门店参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_SHOP_ID | 主键 | GUID | Y | Y |
| 4 | ERPID | 产品服务识别码 | number | Y |  |
| 5 | ERPIP | ERP地址 | string(120) | Y |  |
| 6 | OPENDATE | 开幕日期 | date | Y |  |
| 7 | CHGDTIME | 换日时间 | string(120) | Y |  |
| 8 | MCASHDRAW | 钱箱管理 | number(0/1) | Y |  |
| 9 | MSQUAD | 班次管理 | number(0/1) | Y |  |
| 10 | MEDATE | 日结管理 | number(0/1) | Y |  |
| 11 | SOAPURL | SOAP网址 | string(120) | Y |  |
| 12 | DEFFIND | 默认查询 | string(400) | Y |  |
| 13 | DECAMT | 金额小数位数 | number | Y |  |
| 14 | DECCOUNT | 数量小数位数 | number | Y |  |
| 15 | EFBARCODE | 生鲜条码标识讫 | number | Y |  |
| 16 | BCFBARCODE | 生鲜数量开始位 | number | Y |  |
| 17 | BFBARCODE | 生鲜条码标识起 | number | Y |  |
| 18 | BMFBARCODE | 生鲜金额开始位 | number | Y |  |
| 19 | BPFBARCODE | 生鲜单价开始位 | number | Y |  |
| 20 | BPLUFBARCODE | 生鲜PLU起始位 | number | Y |  |
| 21 | CDECFBARCODE | 生鲜数量小数位 | number | Y |  |
| 22 | CINTFBARCODE | 生鲜数量整数位 | number | Y |  |
| 23 | MDECFBARCODE | 生鲜金额小数位 | number | Y |  |
| 24 | MINTFBARCODE | 生鲜金额整数位 | number | Y |  |
| 25 | PDECFBARCODE | 生鲜单价小数位 | number | Y |  |
| 26 | PINTFBARCODE | 生鲜单价整数位 | number | Y |  |
| 27 | LPLUFBARCODE | 生鲜PLU长度 | number | Y |  |
| 28 | CTYPE | 钱箱接口类型 | string(120) | Y |  |
| 29 | LTYPE | 客显接口类型 | string(120) | Y |  |
| 30 | PTYPE | 打印机接口类型 | string(120) | Y |  |
| 31 | SHOP_ID | 门店 | GUID | Y |  |
| 32 | PARA_BASESETTEMP_D_ID |  | GUID | Y |  |
| 33 | CTYPE_ID | 钱箱接口类型ID | GUID | Y |  |
| 34 | LTYPE_ID | 客显接口类型ID | GUID | Y |  |
| 35 | PTYPE_ID | 打印机接口类型ID | GUID | Y |  |
| 36 | IC_READER_PORT | IC读卡器端口 | number | Y |  |
| 37 | BLIND | 盲交 | number(0/1) | Y |  |
| 38 | PAYER | 缴款人员 | string(40) | Y |  |
| 39 | DEF_CRADTYPE | 收银默认卡类型 | string(40) | Y |  |
| 40 | CreateDate | 创建日期 | date | Y |  |
| 41 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 42 | ModifiedDate | 修改日期 | date | Y |  |
| 43 | CreateBy | 创建者 | GUID | Y |  |
| 44 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 45 | ModifiedBy | 修改者 | GUID | Y |  |
| 46 | Attachments | 附件 | string | Y |  |
| 47 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 48 | Version | 版本号，不要随意更改 | binary | Y |  |
| 49 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 50 | ApproveDate | 修改日期 | date | Y |  |
| 51 | ApproveBy | 修改人 | GUID | Y |  |
| 52 | Owner_Org_RTK |  | string(400) | Y |  |
| 53 | Owner_Org_ROid |  | GUID | Y |  |

### PARA_SUPPLY_CENTER (采购域参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARA_SUPPLY_CENTER_ID | 主键 | GUID | Y | Y |
| 4 | SUPPLY_APPROVE_DATE_BY | 审核日依据 | string(40) | Y |  |
| 5 | PURCHASE_TAX_INCLUDED | 含税 | number(0/1) | Y |  |
| 6 | IFS_GENERATE_PA_DOC_ID | 厂供料到货单据类型 | GUID | Y |  |
| 7 | SUPPLY_CENTER_TAX_REGION_ID | 税区 | GUID | Y |  |
| 8 | SUPPLY_COMPANY_ID | 统计币种所属公司 | GUID | Y |  |
| 9 | IFS_GENERATE_RETURN_DOC_ID | 厂供料退货单据类型 | GUID | Y |  |
| 10 | PO_REQ_CLOSE | 采购订单指定结束同步结束请购单 | number(0/1) | Y |  |
| 11 | TAX_MODE | 税额计算方式 | string(40) | Y |  |
| 12 | COMBINE_PURCHASE | 合并采购(作废) | number(0/1) | Y |  |
| 13 | PURCHASE_SEQUENCE | 合并采购需求核销顺序(作废) | string(40) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Attachments | 附件 | string | Y |  |
| 21 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 24 | ApproveDate | 修改日期 | date | Y |  |
| 25 | ApproveBy | 修改人 | GUID | Y |  |
| 26 | Owner_Org_RTK |  | string(400) | Y |  |
| 27 | Owner_Org_ROid |  | GUID | Y |  |
| 28 | PUR_SEQ_PRODUCE_BY | 采购到货核销顺序生成依据 | string(40) | Y |  |
| 29 | PUR_COMBINE_RULE | 生成采购订单收货信息合并规则 | string(40) | Y |  |
| 30 | AUTO_SHOW_ADJUST_QTY | 自动弹出调整需求数量画面 | number(0/1) | Y |  |
| 31 | IFS_INTERNAL_PA_DOC_ID | 集团委外材料到货单据类型 | GUID | Y |  |
| 32 | IFS_INTERNAL_RETURN_DOC_ID | 集团委外材料退货单据类型 | GUID | Y |  |

### PARA_SUPPLY_CENTER_D (采购域参数单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PARA_SUPPLY_CENTER_D_ID | 主键 | GUID | Y | Y |
| 2 | PLANT_ID | 工厂/储运 | GUID | Y |  |
| 3 | IFS_GENERATE_IR_DOC_ID | 厂供料领料单据类型 | GUID | Y |  |
| 4 | CATEGORY | 单据性质 | string(40) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 13 | ApproveDate | 修改日期 | date | Y |  |
| 14 | ApproveBy | 修改人 | GUID | Y |  |
| 15 | PARA_SUPPLY_CENTER_ID |  | GUID | Y |  |