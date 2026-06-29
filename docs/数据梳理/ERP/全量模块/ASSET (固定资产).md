---
module: "ASSET"
name_zh: "固定资产"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 39
columns: 2459
category: asset
tags: ["ERP", "E10", "asset"]
created: 2026-06-25 10:52
---

# ASSET (固定资产)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 39 | Columns: 2459

## Related Modules

- [[EQT (设备管理)|EQT (设备管理)]]
- [[EQUIPMENT (设备台账)|EQUIPMENT (设备台账)]]
- [[MAINTAIN (设备维护)|MAINTAIN (设备维护)]]

---

## Tables


- **ASSET_ADJUST**
- **ASSET_ASSY**
- **ASSET_BAK (资产信息期间档)**
- **ASSET_CATEGORY (维护资产类别)**
- **ASSET_CATEGORY_ACCOUNT**
- **ASSET_CATEGORY_ACCOUNT_D**
- **ASSET_CATEGORY_DATASET**
- **ASSET_CATEGORY_DIFFA**
- **ASSET_COUNT_LIST (资产盘点清单)**
- **ASSET_COUNT_LIST_DETAIL (资产盘点清单明细)**
- **ASSET_COUNT_PLAN (资产盘点计划)**
- **ASSET_D**
- **ASSET_DDS_BAK (资产交易单据摊提标准备份档)**
- **ASSET_DEPR**
- **ASSET_DEPR_ALLOC_STATS (资产摊提分配统计档)**
- **ASSET_DEPR_D**
- **ASSET_DEPR_EXP_ACCOUNT**
- **ASSET_DEPR_STD (资产摊提标准档)**
- **ASSET_HISTORY**
- **ASSET_HISTORY_A (资产交易历史档A)**
- **ASSET_IMPAIRMENT (资产减值准备单)**
- **ASSET_IMPROVE (资产改良单)**
- **ASSET_MTGE (资产抵押)**
- **ASSET_OUTSIDE (资产外送单)**
- **ASSET_OUTSIDE_D (资产外送单单身)**
- **ASSET_PTA_HISTORY (采购转资产历史档)**
- **ASSET_PTABC (采购转资产批次控制档)**
- **ASSET_RETURN**
- **ASSET_RETURN_D**
- **ASSET_REVALUE (资产重估单)**
- **ASSET_SCRAP**
- **ASSET_SELL**
- **ASSET_STATS_CATEGORY (资产统计分类)**
- **ASSET_TDI (维护税维初始单)**
- **ASSET_TRANSFER**
- **ASSET_TRANSFER_D**
- **ASSET_UNITS (资产工作量信息)**
- **ASSET_UNITS_D (资产工作量单身)**


---


---


> Tables: 39

### ASSET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_ID | 主键 | GUID | Y | Y |
| 4 | INITIALIZED_FLAG | 初始化标识 | number(0/1) | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_DATE | 单据日期 | date | Y |  |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | ASSET_NATURE | 资产性质 | number | Y |  |
| 12 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 13 | ASSET_CODE | 资产编号 | string(80) | Y |  |
| 14 | ASSET_NAME | 资产名称 | string(120) | Y |  |
| 15 | ASSET_SPECIFICATION | 资产规格 | string(510) | Y |  |
| 16 | UNIT_ID | 单位 | GUID | Y |  |
| 17 | QUANTITY | 数量 | number(16,6) | Y |  |
| 18 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 19 | MANUFACTURER | 制造商 | string(144) | Y |  |
| 20 | ASSET_PROFITABILITY_CATEGORY | 资产形态 | number | Y |  |
| 21 | MAIN_ASSET_ID | 主资产 | GUID | Y |  |
| 22 | RESPONSIBILITY_ORG_TYPE | 责任组织类型 | number | Y |  |
| 23 | EMPLOYEE_ID | 责任人 | GUID | Y |  |
| 24 | ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 25 | LOCATION | 存放地点 | string(510) | Y |  |
| 26 | CURRENCY_ID | 货币 | GUID | Y |  |
| 27 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 28 | ACQUISITION_AMT_TC | 取得成本(原币) | number(23,8) | Y |  |
| 29 | ACQUISITION_AMT | 取得成本 | number(23,8) | Y |  |
| 30 | IMPROVEMENT_AMT | 改良成本 | number(23,8) | Y |  |
| 31 | FVC_AMT | 公允价值变动 | number(23,8) | Y |  |
| 32 | CURRENT_AMT | 现行原值 | number(23,8) | Y |  |
| 33 | ACCUM_DEPR_AMT | 累计摊提 | number(23,8) | Y |  |
| 34 | NET_AMT | 资产净值 | number(23,8) | Y |  |
| 35 | IMPAIRMENT_AMT | 减值准备 | number(23,8) | Y |  |
| 36 | CARRYING_AMT | 账面价值 | number(23,8) | Y |  |
| 37 | REVALUATION_SURPLUS_AMT | 重估价盈余 | number(23,8) | Y |  |
| 38 | FVCP_TRANSFERRING_AMT | 公允价值变动收益(转换) | number(23,8) | Y |  |
| 39 | ACCUM_FVCP_AMT | 累计公允价值变动收益 | number(23,8) | Y |  |
| 40 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 41 | BENCHMARK_RESI_RATE | 基准净残值率 | number(11,10) | Y |  |
| 42 | ASSET_STATUS | 资产状态 | number | Y |  |
| 43 | DISPOSAL_DATE | 处置/转换日期 | date | Y |  |
| 44 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 45 | START_DEPR_DATE | 开始摊提日期 | date | Y |  |
| 46 | ESTI_DEPR_PERIODS | 预计摊提期数 | number | Y |  |
| 47 | DEPRED_PERIODS | 已摊提期数 | number | Y |  |
| 48 | UNDEPR_PERIODS | 待摊提期数 | number | Y |  |
| 49 | ESTI_UNITS | 预计总工作量 | number(16,6) | Y |  |
| 50 | USED_UNITS | 已使用的工作量 | number(16,6) | Y |  |
| 51 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 52 | EXTEND_ESTI_DEPR_PERIODS | 延续摊提_预计摊提期数 | number | Y |  |
| 53 | EXTEND_DEPRED_PERIODS | 延续摊提_已摊提期数 | number | Y |  |
| 54 | EXTEND_UNDEPR_PERIODS | 延续摊提_待摊提期数 | number | Y |  |
| 55 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 56 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 57 | PREVIOUS_DEPR_DATE | 上次摊提日期 | date | Y |  |
| 58 | LAST_DEPR_DATE | 最近摊提日期 | date | Y |  |
| 59 | DEPR_ALLOC_FLAG | 摊提分配标识 | number(0/1) | Y |  |
| 60 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 61 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 62 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 63 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 64 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 65 | ASSET_TRANS_SEQNO | 资产交易序号 | number | Y |  |
| 66 | ASSET_MACRODEPR_FLAG | 资产宏观摊提控制标识 | number(0/1) | Y |  |
| 67 | ASSET_MATURITY_FLAG | 资产到期标识 | number(0/1) | Y |  |
| 68 | ASSET_DEPR_EXP_ACCOUNT_ID | 费用归属分类 | GUID | Y |  |
| 69 | REMARK | 备注 | string(510) | Y |  |
| 70 | TD_ACQUISITION_AMT_TC | 税务_取得成本(原币) | number(23,8) | Y |  |
| 71 | TD_ACQUISITION_AMT | 税务_取得成本 | number(23,8) | Y |  |
| 72 | TD_IMPROVEMENT_AMT | 税务_改良成本 | number(23,8) | Y |  |
| 73 | TD_FVC_AMT | 税务_公允价值变动 | number(23,8) | Y |  |
| 74 | TD_CURRENT_AMT | 税务_现行原值 | number(23,8) | Y |  |
| 75 | TD_ACCUM_DEPR_AMT | 税务_累计摊提 | number(23,8) | Y |  |
| 76 | TD_NET_AMT | 税务_资产净值 | number(23,8) | Y |  |
| 77 | TD_IMPAIRMENT_AMT | 税务_减值准备 | number(23,8) | Y |  |
| 78 | TD_CARRYING_AMT | 税务_账面价值 | number(23,8) | Y |  |
| 79 | TD_REVALUATION_SURPLUS_AMT | 税务_重估价盈余 | number(23,8) | Y |  |
| 80 | TD_FVCP_TRANSFERRING_AMT | 税务_公允价值变动收益(转换) | number(23,8) | Y |  |
| 81 | TD_ACCUM_FVCP_AMT | 税务_累计公允价值变动收益 | number(23,8) | Y |  |
| 82 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 83 | TD_BENCHMARK_RESI_RATE | 税务_基准净残值率 | number(11,10) | Y |  |
| 84 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 85 | TD_START_DEPR_DATE | 税务_开始摊提日期 | date | Y |  |
| 86 | TD_ESTI_DEPR_PERIODS | 税务_预计摊提期数 | number | Y |  |
| 87 | TD_DEPRED_PERIODS | 税务_已摊提期数 | number | Y |  |
| 88 | TD_UNDEPR_PERIODS | 税务_待摊提期数 | number | Y |  |
| 89 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 90 | TD_EXTEND_ESTI_DEPR_PERIODS | 税务_延续摊提_预计摊提期数 | number | Y |  |
| 91 | TD_EXTEND_DEPRED_PERIODS | 税务_延续摊提_已摊提期数 | number | Y |  |
| 92 | TD_EXTEND_UNDEPR_PERIODS | 税务_延续摊提_待摊提期数 | number | Y |  |
| 93 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 94 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 95 | TD_LAST_DEPR_DATE | 税务_最近摊提日期 | date | Y |  |
| 96 | TD_ASSET_MACRODEPR_FLAG | 税务_资产宏观摊提控制标识 | number(0/1) | Y |  |
| 97 | TD_ASSET_MATURITY_FLAG | 税务_资产到期标识 | number(0/1) | Y |  |
| 98 | Attachments | 附件 | string | Y |  |
| 99 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 100 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 101 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 102 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 103 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 104 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 105 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 106 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 107 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 108 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 109 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 110 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 111 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 112 | UDF041 | 自定义字段12 | date | Y |  |
| 113 | UDF042 | 自定义字段13 | date | Y |  |
| 114 | UDF051 | 自定义字段14 | GUID | Y |  |
| 115 | UDF052 | 自定义字段15 | GUID | Y |  |
| 116 | UDF053 | 自定义字段16 | GUID | Y |  |
| 117 | UDF054 | 自定义字段17 | GUID | Y |  |
| 118 | Version | 版本号，不要随意更改 | binary | Y |  |
| 119 | PrintCount | 打印次数 | number | Y |  |
| 120 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 121 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 122 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 123 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 124 | CreateDate | 创建日期 | date | Y |  |
| 125 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 126 | ModifiedDate | 修改日期 | date | Y |  |
| 127 | CreateBy | 创建者 | GUID | Y |  |
| 128 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 129 | ModifiedBy | 修改者 | GUID | Y |  |
| 130 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 131 | ApproveDate | 修改日期 | date | Y |  |
| 132 | ApproveBy | 修改人 | GUID | Y |  |
| 133 | Owner_Org_RTK |  | string(400) | Y |  |
| 134 | Owner_Org_ROid |  | GUID | Y |  |
| 135 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 136 | SOURCE_ID_ROid |  | GUID | Y |  |
| 137 | DOC_NO | 单号 | string(40) | Y |  |
| 138 | REVALUEDIFF_AMT | 重估差价 | number(23,8) | Y |  |
| 139 | TD_REVALUEDIFF_AMT | 税务_重估差价 | number(23,8) | Y |  |
| 140 | OUTSIDE_FLAG | 已外送标识 | number(0/1) | Y |  |
| 141 | OUTSIDE_DATE | 外送日期 | date | Y |  |
| 142 | ESTI_RETURN_DATE | 预计收回日期 | date | Y |  |
| 143 | ACTUAL_RETURN_DATE | 实际收回日期 | date | Y |  |
| 144 | OUTSIDE_PLACE | 外送地点 | string(510) | Y |  |
| 145 | OUTSIDE_EMPLOYEE_ID | 外送责任人 | GUID | Y |  |
| 146 | OUTSIDE_ADMIN_UNIT_ID | 外送责任部门 | GUID | Y |  |
| 147 | ASSET_OUTSIDE_ID | 外送单据 | GUID | Y |  |
| 148 | ASSET_OUTSIDE_D_ID | 外送序号 | GUID | Y |  |
| 149 | ABANDON_FLAG | 不需收回标识 | number(0/1) | Y |  |
| 150 | ABANDON_REMARK | 不需收回备注 | string(510) | Y |  |
| 151 | LAST_TRANSFER_DATE | 最近转移日期 | date | Y |  |
| 152 | MTGE_FLAG | 已抵押标识 | number(0/1) | Y |  |
| 153 | ASSET_MTGE_SEQNO | 抵押序号 | number | Y |  |
| 154 | ASSET_STATS_CATEGORY_ID | 统计分类 | GUID | Y |  |
| 155 | ITEM_ID | 资产品号 | GUID | Y |  |
| 156 | ITC_STATUS | 投资抵减状态 | number | Y |  |
| 157 | ITC_RATE | 投资抵减率 | number(5,4) | Y |  |
| 158 | ITC_GOV_AN | 主管机关核准文号 | string(510) | Y |  |
| 159 | ITC_GOV_AD | 主管机关核准日期 | date | Y |  |
| 160 | ITC_GOV_AN2 | 国税局核准文号 | string(510) | Y |  |
| 161 | ITC_GOV_AD2 | 国税局核准日期 | date | Y |  |
| 162 | ITC_REMARK | 投资抵减备注 | string(510) | Y |  |
| 163 | SOURCE_TYPE | 来源类型 | number | Y |  |
| 164 | SOURCE_DOC_NO | 源单单号 | string(80) | Y |  |
| 165 | SOURCE_DOC_SEQNO | 源单序号 | number | Y |  |
| 166 | SOURCE_DOC_DATE | 源单日期 | date | Y |  |
| 167 | UI_STATUS | UI状态 | number | Y |  |
| 168 | ASSET_STATS_CATEGORY2 | 统计分类2 | number | Y |  |
| 169 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 170 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 171 | SOURCE3_ID_RTK |  | string(400) | Y |  |
| 172 | SOURCE3_ID_ROid |  | GUID | Y |  |

### ASSET_ADJUST

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_ADJUST_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ASSET_NATURE | 资产性质 | number | Y |  |
| 12 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 13 | HIS_DEPR_STATUS | 原摊提状态 | number | Y |  |
| 14 | HIS_DEPR_METHOD | 原摊提方法 | number | Y |  |
| 15 | DEPR_METHOD | 新摊提方法 | number | Y |  |
| 16 | HIS_ACQUISITION_AMT | 原取得成本 | number(23,8) | Y |  |
| 17 | DIFF_ACQUISITION_AMT | 取得成本_调整额 | number(23,8) | Y |  |
| 18 | HIS_IMPROVEMENT_AMT | 原改良成本 | number(23,8) | Y |  |
| 19 | DIFF_IMPROVEMENT_AMT | 改良成本_调整额 | number(23,8) | Y |  |
| 20 | HIS_ACCUM_DEPR_AMT | 原累计摊提 | number(23,8) | Y |  |
| 21 | ASSET_ID | 资产编号 | GUID | Y |  |
| 22 | HIS_ASSET_CATEGORY_ID | 原资产类别 | GUID | Y |  |
| 23 | ASSET_CATEGORY_ID | 新资产类别 | GUID | Y |  |
| 24 | DIFF_ACCUM_DEPR_AMT | 累计摊提_调整额 | number(23,8) | Y |  |
| 25 | HIS_IMPAIRMENT_AMT | 原减值准备 | number(23,8) | Y |  |
| 26 | DIFF_IMPAIRMENT_AMT | 减值准备_调整额 | number(23,8) | Y |  |
| 27 | HIS_RESIDUAL_AMT | 原净残值 | number(23,8) | Y |  |
| 28 | DIFF_RESIDUAL_AMT | 净残值_调整额 | number(23,8) | Y |  |
| 29 | HIS_UNDEPR_PERIODS | 原待摊提期数 | number | Y |  |
| 30 | DIFF_UNDEPR_PERIODS | 待摊提期数_调整额 | number | Y |  |
| 31 | HIS_UNUSED_UNITS | 原剩余工作量 | number(16,6) | Y |  |
| 32 | DIFF_UNUSED_UNITS | 剩余工作量_调整额 | number(16,6) | Y |  |
| 33 | HIS_EXTEND_DEPR_FLAG | 原延续摊提标识 | number(0/1) | Y |  |
| 34 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 35 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 36 | REMARK | 备注 | string(510) | Y |  |
| 37 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 38 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 39 | HIS_ASSET_MATURITY_FLAG | 原资产到期标识 | number(0/1) | Y |  |
| 40 | ASSET_STATUS | 资产状态 | number | Y |  |
| 41 | ASSET_MATURITY_FLAG | 新资产到期标识 | number(0/1) | Y |  |
| 42 | HIS_START_DEPR_DATE | 原开始摊提日期 | date | Y |  |
| 43 | START_DEPR_DATE | 新开始摊提日期 | date | Y |  |
| 44 | HIS_CARRYING_AMT | 原账面价值 | number(23,8) | Y |  |
| 45 | DIFF_CARRYING_AMT | 账面价值_调整额 | number(23,8) | Y |  |
| 46 | TD_HIS_EXTEND_DEPR_FLAG | 税务_原延续摊提标识 | number(0/1) | Y |  |
| 47 | TD_HIS_DEPR_STATUS | 税务_原摊提状态 | number | Y |  |
| 48 | TD_HIS_ASSET_MATURITY_FLAG | 税务_原资产到期标识 | number(0/1) | Y |  |
| 49 | TD_ASSET_MATURITY_FLAG | 税务_新资产到期标识 | number(0/1) | Y |  |
| 50 | TD_HIS_DEPR_METHOD | 税务_原摊提方法 | number | Y |  |
| 51 | TD_DEPR_METHOD | 税务_新摊提方法 | number | Y |  |
| 52 | TD_HIS_START_DEPR_DATE | 税务_原开始摊提日期 | date | Y |  |
| 53 | TD_START_DEPR_DATE | 税务_新开始摊提日期 | date | Y |  |
| 54 | TD_HIS_ACQUISITION_AMT | 税务_原取得成本 | number(23,8) | Y |  |
| 55 | TD_DIFF_ACQUISITION_AMT | 税务_取得成本_调整额 | number(23,8) | Y |  |
| 56 | TD_HIS_IMPROVEMENT_AMT | 税务_原改良成本 | number(23,8) | Y |  |
| 57 | TD_DIFF_IMPROVEMENT_AMT | 税务_改良成本_调整额 | number(23,8) | Y |  |
| 58 | TD_HIS_ACCUM_DEPR_AMT | 税务_原累计摊提 | number(23,8) | Y |  |
| 59 | TD_DIFF_ACCUM_DEPR_AMT | 税务_累计摊提_调整额 | number(23,8) | Y |  |
| 60 | TD_HIS_IMPAIRMENT_AMT | 税务_原减值准备 | number(23,8) | Y |  |
| 61 | TD_DIFF_IMPAIRMENT_AMT | 税务_减值准备_调整额 | number(23,8) | Y |  |
| 62 | TD_HIS_RESIDUAL_AMT | 税务_原净残值 | number(23,8) | Y |  |
| 63 | TD_DIFF_RESIDUAL_AMT | 税务_净残值_调整额 | number(23,8) | Y |  |
| 64 | TD_HIS_CARRYING_AMT | 税务_原账面价值 | number(23,8) | Y |  |
| 65 | TD_DIFF_CARRYING_AMT | 税务_账面价值_调整额 | number(23,8) | Y |  |
| 66 | TD_HIS_UNDEPR_PERIODS | 税务_原待摊提期数 | number | Y |  |
| 67 | TD_DIFF_UNDEPR_PERIODS | 税务_待摊提期数_调整额 | number | Y |  |
| 68 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 69 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 70 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 71 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 72 | Version | 版本号，不要随意更改 | binary | Y |  |
| 73 | CreateDate | 创建日期 | date | Y |  |
| 74 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 75 | ModifiedDate | 修改日期 | date | Y |  |
| 76 | CreateBy | 创建者 | GUID | Y |  |
| 77 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 78 | ModifiedBy | 修改者 | GUID | Y |  |
| 79 | Attachments | 附件 | string | Y |  |
| 80 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 81 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 82 | ApproveDate | 修改日期 | date | Y |  |
| 83 | ApproveBy | 修改人 | GUID | Y |  |
| 84 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 85 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 86 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 87 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 88 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 89 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 90 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 91 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 92 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 93 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 94 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 95 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 96 | UDF041 | 自定义字段12 | date | Y |  |
| 97 | UDF042 | 自定义字段13 | date | Y |  |
| 98 | UDF051 | 自定义字段14 | GUID | Y |  |
| 99 | UDF052 | 自定义字段15 | GUID | Y |  |
| 100 | UDF053 | 自定义字段16 | GUID | Y |  |
| 101 | UDF054 | 自定义字段17 | GUID | Y |  |
| 102 | PrintCount | 打印次数 | number | Y |  |
| 103 | Owner_Org_RTK |  | string(400) | Y |  |
| 104 | Owner_Org_ROid |  | GUID | Y |  |
| 105 | HIS_REVALUEDIFF_AMT | 原重估差价 | number(23,8) | Y |  |
| 106 | DIFF_REVALUEDIFF_AMT | 重估差价_调整额 | number(23,8) | Y |  |
| 107 | TD_HIS_REVALUEDIFF_AMT | 税务_原重估差价 | number(23,8) | Y |  |
| 108 | TD_DIFF_REVALUEDIFF_AMT | 税务_重估差价_调整额 | number(23,8) | Y |  |

### ASSET_ASSY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_ASSY_ID | 主键 | GUID | Y | Y |
| 3 | ASSY_DESCRIPTION | 附件名称 | string(120) | Y |  |
| 4 | ASSY_SPECIFICATION | 规格型号 | string(510) | Y |  |
| 5 | UNIT | 单位 | string(20) | Y |  |
| 6 | QUANTITY | 数量 | number(16,6) | Y |  |
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
| 36 | ASSET_ID |  | GUID | Y |  |

### ASSET_BAK (资产信息期间档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_BAK_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 6 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 7 | QUANTITY | 数量 | number(16,6) | Y |  |
| 8 | ASSET_PROFITABILITY_CATEGORY | 资产形态 | number | Y |  |
| 9 | MAIN_ASSET_ID | 主资产 | GUID | Y |  |
| 10 | RESPONSIBILITY_ORG_TYPE | 责任组织类型 | number | Y |  |
| 11 | ASSET_ID | 资产 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 13 | EMPLOYEE_ID | 责任人 | GUID | Y |  |
| 14 | ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 15 | LOCATION | 存放地点 | string(510) | Y |  |
| 16 | ACQUISITION_AMT | 取得成本 | number(23,8) | Y |  |
| 17 | IMPROVEMENT_AMT | 改良成本 | number(23,8) | Y |  |
| 18 | FVC_AMT | 公允价值变动 | number(23,8) | Y |  |
| 19 | CURRENT_AMT | 现行原值 | number(23,8) | Y |  |
| 20 | ACCUM_DEPR_AMT | 累计摊提 | number(23,8) | Y |  |
| 21 | NET_AMT | 资产净值 | number(23,8) | Y |  |
| 22 | IMPAIRMENT_AMT | 减值准备 | number(23,8) | Y |  |
| 23 | CARRYING_AMT | 账面价值 | number(23,8) | Y |  |
| 24 | REVALUATION_SURPLUS_AMT | 重估价盈余 | number(23,8) | Y |  |
| 25 | FVCP_TRANSFERRING_AMT | 公允价值变动收益(转换) | number(23,8) | Y |  |
| 26 | ACCUM_FVCP_AMT | 累计公允价值变动收益 | number(23,8) | Y |  |
| 27 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 28 | ASSET_STATUS | 资产状态 | number | Y |  |
| 29 | DISPOSAL_DATE | 处置/转换日期 | date | Y |  |
| 30 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 31 | START_DEPR_DATE | 开始摊提日期 | date | Y |  |
| 32 | ESTI_DEPR_PERIODS | 预计摊提期数 | number | Y |  |
| 33 | DEPRED_PERIODS | 已摊提期数 | number | Y |  |
| 34 | UNDEPR_PERIODS | 待摊提期数 | number | Y |  |
| 35 | ESTI_UNITS | 预计总工作量 | number(16,6) | Y |  |
| 36 | USED_UNITS | 已使用的工作量 | number(16,6) | Y |  |
| 37 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 38 | EXTEND_ESTI_DEPR_PERIODS | 延续摊提_预计摊提期数 | number | Y |  |
| 39 | EXTEND_DEPRED_PERIODS | 延续摊提_已摊提期数 | number | Y |  |
| 40 | EXTEND_UNDEPR_PERIODS | 延续摊提_待摊提期数 | number | Y |  |
| 41 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 42 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 43 | PREVIOUS_DEPR_DATE | 上次摊提日期(作废) | date | Y |  |
| 44 | LAST_DEPR_DATE | 最近摊提日期 | date | Y |  |
| 45 | DEPR_ALLOC_FLAG | 摊提分配标识 | number(0/1) | Y |  |
| 46 | ASSET_MATURITY_FLAG | 资产到期标识 | number(0/1) | Y |  |
| 47 | TD_ACQUISITION_AMT_TC | 税务_取得成本(原币) | number(23,8) | Y |  |
| 48 | TD_ACQUISITION_AMT | 税务_取得成本 | number(23,8) | Y |  |
| 49 | TD_IMPROVEMENT_AMT | 税务_改良成本 | number(23,8) | Y |  |
| 50 | TD_FVC_AMT | 税务_公允价值变动 | number(23,8) | Y |  |
| 51 | TD_CURRENT_AMT | 税务_现行原值 | number(23,8) | Y |  |
| 52 | TD_ACCUM_DEPR_AMT | 税务_累计摊提 | number(23,8) | Y |  |
| 53 | TD_NET_AMT | 税务_资产净值 | number(23,8) | Y |  |
| 54 | TD_IMPAIRMENT_AMT | 税务_减值准备 | number(23,8) | Y |  |
| 55 | TD_CARRYING_AMT | 税务_账面价值 | number(23,8) | Y |  |
| 56 | TD_REVALUATION_SURPLUS_AMT | 税务_重估价盈余 | number(23,8) | Y |  |
| 57 | TD_FVCP_TRANSFERRING_AMT | 税务_公允价值变动收益(转换) | number(23,8) | Y |  |
| 58 | TD_ACCUM_FVCP_AMT | 税务_累计公允价值变动收益 | number(23,8) | Y |  |
| 59 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 60 | TD_BENCHMARK_RESI_RATE | 税务_基准净残值率 | number(11,10) | Y |  |
| 61 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 62 | TD_START_DEPR_DATE | 税务_开始摊提日期 | date | Y |  |
| 63 | TD_ESTI_DEPR_PERIODS | 税务_预计摊提期数 | number | Y |  |
| 64 | TD_DEPRED_PERIODS | 税务_已摊提期数 | number | Y |  |
| 65 | TD_UNDEPR_PERIODS | 税务_待摊提期数 | number | Y |  |
| 66 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 67 | TD_EXTEND_ESTI_DEPR_PERIODS | 税务_延续摊提_预计摊提期数 | number | Y |  |
| 68 | TD_EXTEND_DEPRED_PERIODS | 税务_延续摊提_已摊提期数 | number | Y |  |
| 69 | TD_EXTEND_UNDEPR_PERIODS | 税务_延续摊提_待摊提期数 | number | Y |  |
| 70 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 71 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 72 | TD_LAST_DEPR_DATE | 税务_最近摊提日期 | date | Y |  |
| 73 | TD_ASSET_MACRODEPR_FLAG | 税务_资产宏观摊提控制标识 | number(0/1) | Y |  |
| 74 | TD_ASSET_MATURITY_FLAG | 税务_资产到期标识 | number(0/1) | Y |  |
| 75 | PrintCount | 打印次数 | number | Y |  |
| 76 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 77 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 78 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 79 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 80 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 81 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 82 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 83 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 84 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 85 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 86 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 87 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 88 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 89 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 90 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 91 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 92 | UDF041 | 自定义字段12 | date | Y |  |
| 93 | UDF042 | 自定义字段13 | date | Y |  |
| 94 | UDF051 | 自定义字段14 | GUID | Y |  |
| 95 | UDF052 | 自定义字段15 | GUID | Y |  |
| 96 | UDF053 | 自定义字段16 | GUID | Y |  |
| 97 | UDF054 | 自定义字段17 | GUID | Y |  |
| 98 | CreateDate | 创建日期 | date | Y |  |
| 99 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 100 | ModifiedDate | 修改日期 | date | Y |  |
| 101 | CreateBy | 创建者 | GUID | Y |  |
| 102 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 103 | ModifiedBy | 修改者 | GUID | Y |  |
| 104 | Attachments | 附件 | string | Y |  |
| 105 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 106 | Version | 版本号，不要随意更改 | binary | Y |  |
| 107 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 108 | ApproveDate | 修改日期 | date | Y |  |
| 109 | ApproveBy | 修改人 | GUID | Y |  |
| 110 | Owner_Org_RTK |  | string(400) | Y |  |
| 111 | Owner_Org_ROid |  | GUID | Y |  |
| 112 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 113 | SOURCE_ID_ROid |  | GUID | Y |  |
| 114 | REVALUEDIFF_AMT | 重估差价 | number(23,8) | Y |  |
| 115 | TD_REVALUEDIFF_AMT | 税务_重估差价 | number(23,8) | Y |  |

### ASSET_CATEGORY (维护资产类别)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_CATEGORY_CODE | 资产类别编号 | string(60) | Y |  |
| 5 | ASSET_CATEGORY_NAME | 资产类别名称 | string(60) | Y |  |
| 6 | ASSET_CATEGORY_FULL_NAME | 资产类别全称 | string(620) | Y |  |
| 7 | ASSET_CATEGORY_DATASET_ID | 资产类别表 | GUID | Y |  |
| 8 | ASSET_CATEGORY_AREA | 资产类别范围 | number | Y |  |
| 9 | ASSET_NATURE | 资产性质 | number | Y |  |
| 10 | ASSET_CATEGORY_LEVEL | 资产类别层级 | number | Y |  |
| 11 | ALLOW_ADDPRIVATE_FLAG | 允许增加私有资产类别 | number(0/1) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
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
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |

### ASSET_CATEGORY_ACCOUNT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_CATEGORY_ACCOUNT_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_CATEGORY_ACCOUNT_CODE | 编号 | string(12) | Y |  |
| 5 | ASSET_NATURE | 资产性质 | number | Y |  |
| 6 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 7 | ACCOUNT_CODE_ID | 资产运营科目 | GUID | Y |  |
| 8 | ACCOUNT_CODE2_ID | 摊提运营科目 | GUID | Y |  |
| 9 | ACCOUNT_CODE3_ID | 重估差价运营科目 | GUID | Y |  |
| 10 | ACCOUNT_CODE4_ID | 公允价值变动运营科目 | GUID | Y |  |
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
| 44 | ACCOUNT_CODE5_ID | 减值准备运营科目 | GUID | Y |  |
| 45 | ACCOUNT_CODE6_ID | 减值损失运营科目 | GUID | Y |  |
| 46 | ACCOUNT_CODE7_ID | 减值转回运营科目 | GUID | Y |  |
| 47 | ACCOUNT_CODE8_ID | 资产清理运营科目 | GUID | Y |  |
| 48 | ACCOUNT_CODE21_ID | 资产管理科目 | GUID | Y |  |
| 49 | ACCOUNT_CODE22_ID | 摊提管理科目 | GUID | Y |  |
| 50 | ACCOUNT_CODE23_ID | 重估差价管理科目 | GUID | Y |  |
| 51 | ACCOUNT_CODE24_ID | 公允价值变动管理科目 | GUID | Y |  |
| 52 | ACCOUNT_CODE25_ID | 减值准备管理科目 | GUID | Y |  |
| 53 | ACCOUNT_CODE26_ID | 减值损失管理科目 | GUID | Y |  |
| 54 | ACCOUNT_CODE27_ID | 减值转回管理科目 | GUID | Y |  |
| 55 | ACCOUNT_CODE28_ID | 资产清理管理科目 | GUID | Y |  |

### ASSET_CATEGORY_ACCOUNT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 3 | ASSET_CATEGORY_ACCOUNT_D_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_NATURE | 资产性质 | number | Y |  |
| 5 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
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
| 31 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 32 | SOURCE_ID_ROid |  | GUID | Y |  |
| 33 | ASSET_CATEGORY_ACCOUNT_ID |  | GUID | Y |  |

### ASSET_CATEGORY_DATASET

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_CATEGORY_DATASET_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_CATEGORY_DATASET_CODE | 资产类别表编号 | string(12) | Y |  |
| 5 | ASSET_CATEGORY_DATASET_NAME | 资产类别表名称 | string(40) | Y |  |
| 6 | DATASET_AREA | 资产类别表范围 | number | Y |  |
| 7 | ASSET_CATEGORY_LEVEL | 资产类别级次 | number | Y |  |
| 8 | ASSET_CATEGORY_CODEMODE | 资产类别编码规则 | string(60) | Y |  |
| 9 | LEVEL1_LENGTH | 第一级长度 | number | Y |  |
| 10 | LEVEL2_LENGTH | 第二级长度 | number | Y |  |
| 11 | LEVEL3_LENGTH | 第三级长度 | number | Y |  |
| 12 | LEVEL4_LENGTH | 第四级长度 | number | Y |  |
| 13 | LEVEL5_LENGTH | 第五级长度 | number | Y |  |
| 14 | LEVEL6_LENGTH | 第六级长度 | number | Y |  |
| 15 | LEVEL7_LENGTH | 第七级长度 | number | Y |  |
| 16 | LEVEL8_LENGTH | 第八级长度 | number | Y |  |
| 17 | LEVEL9_LENGTH | 第九级长度 | number | Y |  |
| 18 | LEVEL10_LENGTH | 第十级长度 | number | Y |  |
| 19 | REMARK | 备注 | string(510) | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
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
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_CATEGORY_DIFFA

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ASSET_CATEGORY_DIFFA_ID | 主键 | GUID | Y | Y |
| 2 | ASSET_CATEGORY_ID | 父主键 | GUID | Y |  |
| 3 | COMPANY_ID | 所属公司 | GUID | Y |  |
| 4 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 5 | UNIT_ID | 单位 | GUID | Y |  |
| 6 | ESTI_DEPR_PERIODS | 预计摊提期数 | number | Y |  |
| 7 | BENCHMARK_RESI_RATE | 基准净残值率 | number(11,10) | Y |  |
| 8 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 9 | EXTEND_ESTI_DEPR_PERIODS | 预计延续摊提期数 | number | Y |  |
| 10 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 11 | TD_ESTI_DEPR_PERIODS | 税务_预计摊提期数 | number | Y |  |
| 12 | TD_BENCHMARK_RESI_RATE | 税务_基准净残值率 | number(11,10) | Y |  |
| 13 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 14 | TD_EXTEND_ESTI_PERIODS | 税务_预计延续摊提期数 | number | Y |  |
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
| 45 | ASSET_STATS_CATEGORY_ID | 统计分类 | GUID | Y |  |
| 46 | ITEM_ID | 资产品号 | GUID | Y |  |

### ASSET_COUNT_LIST (资产盘点清单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_COUNT_LIST_ID | 主键 | GUID | Y | Y |
| 4 | BATCH_SEQNO | 批序号 | number | Y |  |
| 5 | ASSET_COUNT_PLAN_ID | 盘点计划 | GUID | Y |  |
| 6 | O_LOCATION | 原存放地点 | string(510) | Y |  |
| 7 | O_RESPONSIBILITY_ORG_TYPE | 原责任组织类型 | number | Y |  |
| 8 | O_EMPLOYEE_ID | 原责任人 | GUID | Y |  |
| 9 | O_ADMIN_UNIT_ID | 原责任部门 | GUID | Y |  |
| 10 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 11 | ASSET_CODE | 资产编号 | string(80) | Y |  |
| 12 | ASSET_PROFITABILITY_CATEGORY | 资产形态 | number | Y |  |
| 13 | MAIN_ASSET_ID | 主资产 | GUID | Y |  |
| 14 | COUNT_TYPE | 盘点类型 | number | Y |  |
| 15 | CARRYING_QTY | 账面数量 | number(16,6) | Y |  |
| 16 | OUTSIDE_QTY | 外送数量 | number(16,6) | Y |  |
| 17 | COUNT_QTY | 盘点数量 | number(16,6) | Y |  |
| 18 | F_COUNT_QTY | 初盘数量 | number(16,6) | Y |  |
| 19 | R_COUNT_QTY | 复盘数量 | number(16,6) | Y |  |
| 20 | R_COUNT_FLAG | 需复盘标识 | number(0/1) | Y |  |
| 21 | RESPONSIBILITY_ORG_TYPE | 新责任组织类型 | number | Y |  |
| 22 | LOCATION | 新存放地点 | string(510) | Y |  |
| 23 | COUNT_DIFF_FLAG | 盘点差异标识 | number(0/1) | Y |  |
| 24 | REMARK | 备注 | string(510) | Y |  |
| 25 | COUNT_CONFIRM_FLAG | 盘点确认标识 | number(0/1) | Y |  |
| 26 | EMPLOYEE_ID | 新责任人 | GUID | Y |  |
| 27 | ADMIN_UNIT_ID | 新责任部门 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 47 | PrintCount | 打印次数 | number | Y |  |
| 48 | CreateDate | 创建日期 | date | Y |  |
| 49 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 50 | ModifiedDate | 修改日期 | date | Y |  |
| 51 | CreateBy | 创建者 | GUID | Y |  |
| 52 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 53 | ModifiedBy | 修改者 | GUID | Y |  |
| 54 | Attachments | 附件 | string | Y |  |
| 55 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 56 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 57 | ApproveDate | 修改日期 | date | Y |  |
| 58 | ApproveBy | 修改人 | GUID | Y |  |
| 59 | Owner_Org_RTK |  | string(400) | Y |  |
| 60 | Owner_Org_ROid |  | GUID | Y |  |
| 61 | O_SOURCE_ID_RTK |  | string(400) | Y |  |
| 62 | O_SOURCE_ID_ROid |  | GUID | Y |  |
| 63 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 64 | SOURCE_ID_ROid |  | GUID | Y |  |
| 65 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 66 | SOURCE2_ID_ROid |  | GUID | Y |  |

### ASSET_COUNT_LIST_DETAIL (资产盘点清单明细)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_COUNT_LIST_DETAIL_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_ID | 资产 | GUID | Y |  |
| 5 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 6 | ASSET_COUNT_LIST_ID | 父主键 | GUID | Y |  |
| 7 | ASSET_COUNT_PLAN_ID | 盘点计划 | GUID | Y |  |
| 8 | ASSET_STATS_CATEGORY_ID | 资产统计分类 | GUID | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 34 | Attachments | 附件 | string | Y |  |
| 35 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 36 | Owner_Org_RTK |  | string(400) | Y |  |
| 37 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_COUNT_PLAN (资产盘点计划)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_COUNT_PLAN_ID | 主键 | GUID | Y | Y |
| 4 | BATCH_NO | 盘点批号 | string(60) | Y |  |
| 5 | COUNT_DATE | 盘点日期 | date | Y |  |
| 6 | EMPLOYEE_ID | 盘点负责人 | GUID | Y |  |
| 7 | ADMIN_UNIT_ID | 盘点负责部门 | GUID | Y |  |
| 8 | STATS_CATEGORY_FLAG | 统计分类汇总标识 | number(0/1) | Y |  |
| 9 | CLOSE_FLAG | 结案标识 | number(0/1) | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | CreateDate | 创建日期 | date | Y |  |
| 12 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 13 | ModifiedDate | 修改日期 | date | Y |  |
| 14 | CreateBy | 创建者 | GUID | Y |  |
| 15 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 16 | ModifiedBy | 修改者 | GUID | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 36 | Attachments | 附件 | string | Y |  |
| 37 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 38 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 39 | ApproveDate | 修改日期 | date | Y |  |
| 40 | ApproveBy | 修改人 | GUID | Y |  |
| 41 | Owner_Org_RTK |  | string(400) | Y |  |
| 42 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_D_ID | 主键 | GUID | Y | Y |
| 3 | DEPR_ALLOC_ORG_TYPE | 摊提分配组织类型 | number | Y |  |
| 4 | ADMIN_UNIT_ID | 摊提分配部门 | GUID | Y |  |
| 5 | DEPR_ALLOC_RATE | 摊提分配比率 | number(5,4) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | ASSET_DEPR_EXP_ACCOUNT_ID | 费用归属分类 | GUID | Y |  |
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
| 36 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 37 | SOURCE_ID_ROid |  | GUID | Y |  |
| 38 | ASSET_ID |  | GUID | Y |  |

### ASSET_DDS_BAK (资产交易单据摊提标准备份档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_DDS_BAK_ID | 主键 | GUID | Y | Y |
| 4 | LINE_TYPE | 行类型 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | ASSET_ID | 资产 | GUID | Y |  |
| 8 | BD_DEPRED_PERIODS | 摊提基准_已摊提期数 | number | Y |  |
| 9 | BD_LIFE | 摊提基准_期数/工作量 | number(16,6) | Y |  |
| 10 | BD_AMT | 摊提基准_金额 | number(23,8) | Y |  |
| 11 | DEPR_RATE | 摊提率 | number(11,10) | Y |  |
| 12 | DEPR_AMT | 摊提金额 | number(23,8) | Y |  |
| 13 | DEPR_STATUS | 摊提状态 | number | Y |  |
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
| 51 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 52 | SOURCE_ID_ROid |  | GUID | Y |  |

### ASSET_DEPR

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_DEPR_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ASSET_ID | 资产 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 13 | ASSET_NATURE | 资产性质 | number | Y |  |
| 14 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 15 | ASSET_STATUS | 资产状态 | number | Y |  |
| 16 | AD_FLAG | 会计维度标识 | number(0/1) | Y |  |
| 17 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 18 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 19 | DEPR_RATE | 摊提率 | number(11,10) | Y |  |
| 20 | CURRENT_DEPR_AMT | 本期应摊提金额 | number(23,8) | Y |  |
| 21 | VERIFICATION_DEPR_AMT | 本期已摊提金额 | number(23,8) | Y |  |
| 22 | DEPR_AMT | 本次摊提金额 | number(23,8) | Y |  |
| 23 | PREVIOUS_DEPR_DATE | 上次摊提日期 | date | Y |  |
| 24 | TD_FLAG | 税务维度标识 | number(0/1) | Y |  |
| 25 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 26 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 27 | TD_DEPR_RATE | 税务_摊提率 | number(11,10) | Y |  |
| 28 | TD_CURRENT_DEPR_AMT | 税务_本期应摊提金额 | number(23,8) | Y |  |
| 29 | TD_VERIFICATION_DEPR_AMT | 税务_本期已摊提金额 | number(23,8) | Y |  |
| 30 | TD_DEPR_AMT | 税务_本次摊提金额 | number(23,8) | Y |  |
| 31 | TD_PREVIOUS_DEPR_DATE | 税务_上次摊提日期 | date | Y |  |
| 32 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 33 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 34 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 35 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 36 | REMARK | 备注 | string(510) | Y |  |
| 37 | PrintCount | 打印次数 | number | Y |  |
| 38 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 39 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 40 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 41 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 42 | CreateDate | 创建日期 | date | Y |  |
| 43 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 44 | ModifiedDate | 修改日期 | date | Y |  |
| 45 | CreateBy | 创建者 | GUID | Y |  |
| 46 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 47 | ModifiedBy | 修改者 | GUID | Y |  |
| 48 | Attachments | 附件 | string | Y |  |
| 49 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 50 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 69 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 70 | ApproveDate | 修改日期 | date | Y |  |
| 71 | ApproveBy | 修改人 | GUID | Y |  |
| 72 | Owner_Org_RTK |  | string(400) | Y |  |
| 73 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_DEPR_ALLOC_STATS (资产摊提分配统计档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_DEPR_ALLOC_STATS_ID | 主键 | GUID | Y | Y |
| 4 | LINE_TYPE | 行类型 | number | Y |  |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | ASSET_ID | 资产 | GUID | Y |  |
| 8 | ADMIN_UNIT_ID | 摊提分配部门 | GUID | Y |  |
| 9 | OPENING_DEPR_AMT | 期初累计摊提(作废) | number(23,8) | Y |  |
| 10 | DEPR_AMT | 本期摊提 | number(23,8) | Y |  |
| 11 | ASSET_DEPR_EXP_ACCOUNT_ID | 费用归属分类 | GUID | Y |  |
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
| 49 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 50 | SOURCE_ID_ROid |  | GUID | Y |  |

### ASSET_DEPR_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_DEPR_D_ID | 主键 | GUID | Y | Y |
| 3 | DEPR_ALLOC_ORG_TYPE | 摊提分配组织类型 | number | Y |  |
| 4 | ADMIN_UNIT_ID | 摊提分配部门 | GUID | Y |  |
| 5 | CURRENT_UNITS | 工作量_本期应摊提(作废) | number(16,6) | Y |  |
| 6 | VERIFICATION_DEPR_AMT | 摊提额_本期已摊提(作废) | number(23,8) | Y |  |
| 7 | DEPR_AMT | 本次摊提金额 | number(23,8) | Y |  |
| 8 | TD_DEPR_AMT | 税务_本次摊提金额 | number(23,8) | Y |  |
| 9 | ASSET_DEPR_EXP_ACCOUNT_ID | 费用归属分类 | GUID | Y |  |
| 10 | TD_ASSET_DEPR_EXP_ACCOUNT_ID | 税务_费用归属分类 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 41 | SOURCE_ID_ROid |  | GUID | Y |  |
| 42 | ASSET_DEPR_ID |  | GUID | Y |  |

### ASSET_DEPR_EXP_ACCOUNT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_DEPR_EXP_ACCOUNT_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_DEPR_EXP_ACCOUNT_CODE | 编号 | string(12) | Y |  |
| 5 | ASSET_DEPR_EXP_ACCOUNT_NAME | 名称 | string(60) | Y |  |
| 6 | ACCOUNT_CODE2_ID | 停用状态运营科目 | GUID | Y |  |
| 7 | ACCOUNT_CODE3_ID | 常规状态管理科目 | GUID | Y |  |
| 8 | ACCOUNT_CODE4_ID | 停用状态管理科目 | GUID | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | ACCOUNT_CODE_ID | 常规状态运营科目 | GUID | Y |  |
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

### ASSET_DEPR_STD (资产摊提标准档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_DEPR_STD_ID | 主键 | GUID | Y | Y |
| 4 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 5 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 6 | DATA_SOURCE | 数据来源 | number | Y |  |
| 7 | BD_DEPRED_PERIODS | 摊提基准_已摊提期数 | number | Y |  |
| 8 | BD_LIFE | 摊提基准_期数/工作量 | number(16,6) | Y |  |
| 9 | BD_AMT | 摊提基准_金额 | number(23,8) | Y |  |
| 10 | ASSET_ID | 资产 | GUID | Y |  |
| 11 | USED_UNITS | 工作量 | number(16,6) | Y |  |
| 12 | DEPR_AMT | 摊提金额 | number(23,8) | Y |  |
| 13 | DEPR_RATE | 摊提率 | number(11,10) | Y |  |
| 14 | ASSET_CHANGE_COUNT1 | 资产变动次数(作废) | number | Y |  |
| 15 | ASSET_CHANGE_COUNT2 | 资产增加变动次数(作废) | number | Y |  |
| 16 | ASSET_CHANGE_COUNT3 | 资产减少变动次数(作废) | number | Y |  |
| 17 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 18 | DEPR_COUNT | 摊提次数 | number | Y |  |
| 19 | VERIFICATION_DEPR_AMT | 实际已摊提金额 | number(23,8) | Y |  |
| 20 | LINE_TYPE | 行类型 | number | Y |  |
| 21 | PrintCount | 打印次数 | number | Y |  |
| 22 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 23 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 24 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 25 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 44 | CreateDate | 创建日期 | date | Y |  |
| 45 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 46 | ModifiedDate | 修改日期 | date | Y |  |
| 47 | CreateBy | 创建者 | GUID | Y |  |
| 48 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 49 | ModifiedBy | 修改者 | GUID | Y |  |
| 50 | Attachments | 附件 | string | Y |  |
| 51 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 54 | ApproveDate | 修改日期 | date | Y |  |
| 55 | ApproveBy | 修改人 | GUID | Y |  |
| 56 | Owner_Org_RTK |  | string(400) | Y |  |
| 57 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_HISTORY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | ASSET_HISTORY_ID | 主键 | GUID | Y | Y |
| 5 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 6 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 7 | DOC_DATE | 业务日期 | date | Y |  |
| 8 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 9 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 10 | ASSET_ID | 资产编号 | GUID | Y |  |
| 11 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 12 | START_DEPR_DATE | 开始摊提日期 | date | Y |  |
| 13 | UNDEPR_PERIODS | 待摊提期数(作废) | number | Y |  |
| 14 | UNUSED_UNITS | 剩余工作量(作废) | number(16,6) | Y |  |
| 15 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 16 | DIFF_ACQUISITION_AMT | 取得成本_差额 | number(23,8) | Y |  |
| 17 | DIFF_IMPROVEMENT_AMT | 改良成本_差额 | number(23,8) | Y |  |
| 18 | DIFF_FVC_AMT | 公允价值变动_差额 | number(23,8) | Y |  |
| 19 | DIFF_ACCUM_DEPR_AMT | 累计摊提_差额 | number(23,8) | Y |  |
| 20 | DIFF_IMPAIRMENT_AMT | 减值准备_差额 | number(23,8) | Y |  |
| 21 | DIFF_RESIDUAL_AMT | 净残值_差额 | number(23,8) | Y |  |
| 22 | DEPR_AMT | 摊提金额(作废) | number(23,8) | Y |  |
| 23 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 24 | TRANS_DOC_ID | 交易单据类型 | GUID | Y |  |
| 25 | REMARK | 备注 | string(510) | Y |  |
| 26 | LINE_TYPE | 行类型 | number | Y |  |
| 27 | DIFF_ESTI_DEPR_PERIODS | 预计摊提期数_差量 | number | Y |  |
| 28 | DIFF_DEPRED_PERIODS | 已摊提期数_差量 | number | Y |  |
| 29 | DIFF_EXTEND_ESTI_DEPR_PERIODS | 延续摊提_预计摊提期数_差量 | number | Y |  |
| 30 | DIFF_EXTEND_DEPRED_PERIODS | 延续摊提_已摊提期数_差量 | number | Y |  |
| 31 | DIFF_ESTI_UNITS | 预计总工作量_差量 | number(16,6) | Y |  |
| 32 | DIFF_USED_UNITS | 已使用的工作量_差量 | number(16,6) | Y |  |
| 33 | DIFF_EXTEND_RESIDUAL_AMT | 延续摊提_净残值_差额 | number(23,8) | Y |  |
| 34 | CreateDate | 创建日期 | date | Y |  |
| 35 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 36 | ModifiedDate | 修改日期 | date | Y |  |
| 37 | CreateBy | 创建者 | GUID | Y |  |
| 38 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 39 | ModifiedBy | 修改者 | GUID | Y |  |
| 40 | Attachments | 附件 | string | Y |  |
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
| 59 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 62 | ApproveDate | 修改日期 | date | Y |  |
| 63 | ApproveBy | 修改人 | GUID | Y |  |
| 64 | Owner_Org_RTK |  | string(400) | Y |  |
| 65 | Owner_Org_ROid |  | GUID | Y |  |
| 66 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 67 | SOURCE_ID_ROid |  | GUID | Y |  |
| 68 | DIFF_REVALUEDIFF_AMT | 重估差价_差额 | number(23,8) | Y |  |

### ASSET_HISTORY_A (资产交易历史档A)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | SequenceNumber |  | number | Y |  |
| 4 | ASSET_HISTORY_A_ID | 主键 | GUID | Y | Y |
| 5 | LINE_TYPE | 行类型 | number | Y |  |
| 6 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 7 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 8 | TRANS_DOC_ID | 交易单据类型 | GUID | Y |  |
| 9 | TRANS_DOC_NO | 交易单据单号 | string(80) | Y |  |
| 10 | DOC_DATE | 业务日期 | date | Y |  |
| 11 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 12 | ASSET_ID | 资产 | GUID | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | CreateDate | 创建日期 | date | Y |  |
| 15 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 16 | ModifiedDate | 修改日期 | date | Y |  |
| 17 | CreateBy | 创建者 | GUID | Y |  |
| 18 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 19 | ModifiedBy | 修改者 | GUID | Y |  |
| 20 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 39 | Attachments | 附件 | string | Y |  |
| 40 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 41 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 42 | ApproveDate | 修改日期 | date | Y |  |
| 43 | ApproveBy | 修改人 | GUID | Y |  |
| 44 | Owner_Org_RTK |  | string(400) | Y |  |
| 45 | Owner_Org_ROid |  | GUID | Y |  |
| 46 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | SOURCE_ID_ROid |  | GUID | Y |  |

### ASSET_IMPAIRMENT (资产减值准备单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ASSET_IMPAIRMENT_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ASSET_ID | 资产 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 13 | ASSET_NATURE | 资产性质 | number | Y |  |
| 14 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 15 | ASSET_STATUS | 资产状态 | number | Y |  |
| 16 | ZERO_FLAG | 可收回金额为零标识 | number(0/1) | Y |  |
| 17 | RECOVERABLE_AMT | 可收回金额 | number(23,8) | Y |  |
| 18 | AD_FLAG | 会计维度标识 | number(0/1) | Y |  |
| 19 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 20 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 21 | UNDEPR_PERIODS | 待摊提期数 | number | Y |  |
| 22 | EXTEND_UNDEPR_PERIODS | 延续摊提_待摊提期数 | number | Y |  |
| 23 | O_CARRYING_AMT | 原账面价值 | number(23,8) | Y |  |
| 24 | O_IMPAIRMENT_AMT | 已计提减值准备 | number(23,8) | Y |  |
| 25 | IMPAIRMENT_AMT | 本次减值准备 | number(23,8) | Y |  |
| 26 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 27 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 28 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 29 | TD_FLAG | 税务维度标识 | number(0/1) | Y |  |
| 30 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 31 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 32 | TD_UNDEPR_PERIODS | 税务_待摊提期数 | number | Y |  |
| 33 | TD_EXTEND_UNDEPR_PERIODS | 税务_延续摊提_待摊提期数 | number | Y |  |
| 34 | TD_O_CARRYING_AMT | 税务_原账面价值 | number(23,8) | Y |  |
| 35 | TD_O_IMPAIRMENT_AMT | 税务_已计提减值准备 | number(23,8) | Y |  |
| 36 | TD_IMPAIRMENT_AMT | 税务_本次减值准备 | number(23,8) | Y |  |
| 37 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 38 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 39 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 40 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 41 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 42 | REMARK | 备注 | string(510) | Y |  |
| 43 | O_RESIDUAL_AMT | 原净残值 | number(23,8) | Y |  |
| 44 | O_EXTEND_RESIDUAL_AMT | 原延续摊提_净残值 | number(23,8) | Y |  |
| 45 | TD_O_RESIDUAL_AMT | 税务_原净残值 | number(23,8) | Y |  |
| 46 | TD_O_EXTEND_RESIDUAL_AMT | 税务_原延续摊提_净残值 | number(23,8) | Y |  |
| 47 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 48 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 49 | REVERSE_FLAG | 转回标识 | number(0/1) | Y |  |
| 50 | TD_REVERSE_FLAG | 税务_转回标识 | number(0/1) | Y |  |
| 51 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 52 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 53 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 54 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | Attachments | 附件 | string | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 64 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 65 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 66 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 67 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 68 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 69 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 70 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 71 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 72 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 73 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 74 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 75 | UDF041 | 自定义字段12 | date | Y |  |
| 76 | UDF042 | 自定义字段13 | date | Y |  |
| 77 | UDF051 | 自定义字段14 | GUID | Y |  |
| 78 | UDF052 | 自定义字段15 | GUID | Y |  |
| 79 | UDF053 | 自定义字段16 | GUID | Y |  |
| 80 | UDF054 | 自定义字段17 | GUID | Y |  |
| 81 | Version | 版本号，不要随意更改 | binary | Y |  |
| 82 | PrintCount | 打印次数 | number | Y |  |
| 83 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 84 | ApproveDate | 修改日期 | date | Y |  |
| 85 | ApproveBy | 修改人 | GUID | Y |  |
| 86 | Owner_Org_RTK |  | string(400) | Y |  |
| 87 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_IMPROVE (资产改良单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ASSET_IMPROVE_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ASSET_ID | 资产 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 13 | ASSET_NATURE | 资产性质 | number | Y |  |
| 14 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 15 | ASSET_STATUS | 资产状态 | number | Y |  |
| 16 | SUPPLY_CENTER_ID | 采购域 | GUID | Y |  |
| 17 | SETTLEMENT_SUPPLIER_ID | 结算供应商 | GUID | Y |  |
| 18 | ORDER_SUPPLIER_ID | 采购供应商 | GUID | Y |  |
| 19 | EMPLOYEE_ID | 责任人 | GUID | Y |  |
| 20 | ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 21 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 22 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 23 | TAX_ID | 税种 | GUID | Y |  |
| 24 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 25 | VAT_FLAG | VAT标识 | number(0/1) | Y |  |
| 26 | TAX_INCLUDED_FLAG | 含税标识 | number(0/1) | Y |  |
| 27 | TAX_DEDUCTIBLE_FLAG | 税额抵扣标识 | number(0/1) | Y |  |
| 28 | ACCOUNTS_SYS_FLAG | 需往来系统结算标识 | number(0/1) | Y |  |
| 29 | SETTLE_STATUS | 结算状态 | string(40) | Y |  |
| 30 | UNIT_ID | 单位 | GUID | Y |  |
| 31 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 32 | SETTLED_QTY | 已结算数量 | number(16,6) | Y |  |
| 33 | AMT_UNTAX_TC | 无税金额(原币) | number(23,8) | Y |  |
| 34 | TAX_TC | 税额(原币) | number(23,8) | Y |  |
| 35 | AMT_TC | 价税合计(原币) | number(23,8) | Y |  |
| 36 | AMT_UNTAX_FC | 无税金额(本币) | number(23,8) | Y |  |
| 37 | TAX_FC | 税额(本币) | number(23,8) | Y |  |
| 38 | AMT_FC | 价税合计(本币) | number(23,8) | Y |  |
| 39 | IMPROVEMENT_AMT_FC | 改良成本(本币) | number(23,8) | Y |  |
| 40 | AD_FLAG | 会计维度标识 | number(0/1) | Y |  |
| 41 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 42 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 43 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 44 | O_CARRYING_AMT | 原账面价值 | number(23,8) | Y |  |
| 45 | UNDEPR_PERIODS | 待摊提期数 | number | Y |  |
| 46 | EXTEND_UNDEPR_PERIODS | 延续摊提_待摊提期数 | number | Y |  |
| 47 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 48 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 49 | UNUSED_UNITS | 剩余工作量 | number(16,6) | Y |  |
| 50 | UPDATE_UNITS_FLAG | 更新工作量标识 | number(0/1) | Y |  |
| 51 | TD_FLAG | 税务维度标识 | number(0/1) | Y |  |
| 52 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 53 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 54 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 55 | TD_O_CARRYING_AMT | 税务_原账面价值 | number(23,8) | Y |  |
| 56 | TD_UNDEPR_PERIODS | 税务_待摊提期数 | number | Y |  |
| 57 | TD_EXTEND_UNDEPR_PERIODS | 税务_延续摊提_待摊提期数 | number | Y |  |
| 58 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 59 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 60 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 61 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 62 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 63 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 64 | REMARK | 备注 | string(510) | Y |  |
| 65 | O_ESTI_UNITS | 原预计总工作量 | number(16,6) | Y |  |
| 66 | O_ASSET_MATURITY_FLAG | 原资产到期标识 | number(0/1) | Y |  |
| 67 | O_EXTEND_ESTI_DEPR_PERIODS | 原延续摊提_预计摊提期数 | number | Y |  |
| 68 | O_ESTI_DEPR_PERIODS | 原预计摊提期数 | number | Y |  |
| 69 | O_RESIDUAL_AMT | 原净残值 | number(23,8) | Y |  |
| 70 | O_EXTEND_RESIDUAL_AMT | 原延续摊提_净残值 | number(23,8) | Y |  |
| 71 | TD_O_ASSET_MATURITY_FLAG | 税务_原资产到期标识 | number(0/1) | Y |  |
| 72 | TD_O_ESTI_DEPR_PERIODS | 税务_原预计摊提期数 | number | Y |  |
| 73 | TD_O_EXTEND_ESTI_DEPR_PERIODS | 税务_原延续摊提_预计摊提期数 | number | Y |  |
| 74 | TD_O_RESIDUAL_AMT | 税务_原净残值 | number(23,8) | Y |  |
| 75 | TD_O_EXTEND_RESIDUAL_AMT | 税务_原延续摊提_净残值 | number(23,8) | Y |  |
| 76 | ITEM_ID | 资产品号 | GUID | Y |  |
| 77 | CURRENCY_ID | 货币 | GUID | Y |  |
| 78 | IMPROVEMENT_AMT_TC | 改良成本(原币) | number(23,8) | Y |  |
| 79 | O_USED_UNITS | 原已使用的工作量 | number(16,6) | Y |  |
| 80 | CreateDate | 创建日期 | date | Y |  |
| 81 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 82 | ModifiedDate | 修改日期 | date | Y |  |
| 83 | CreateBy | 创建者 | GUID | Y |  |
| 84 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 85 | ModifiedBy | 修改者 | GUID | Y |  |
| 86 | Attachments | 附件 | string | Y |  |
| 87 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 88 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 89 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 90 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 91 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 92 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 93 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 94 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 95 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 96 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 97 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 98 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 99 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 100 | UDF041 | 自定义字段12 | date | Y |  |
| 101 | UDF042 | 自定义字段13 | date | Y |  |
| 102 | UDF051 | 自定义字段14 | GUID | Y |  |
| 103 | UDF052 | 自定义字段15 | GUID | Y |  |
| 104 | UDF053 | 自定义字段16 | GUID | Y |  |
| 105 | UDF054 | 自定义字段17 | GUID | Y |  |
| 106 | Version | 版本号，不要随意更改 | binary | Y |  |
| 107 | PrintCount | 打印次数 | number | Y |  |
| 108 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 109 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 110 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 111 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 112 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 113 | ApproveDate | 修改日期 | date | Y |  |
| 114 | ApproveBy | 修改人 | GUID | Y |  |
| 115 | Owner_Org_RTK |  | string(400) | Y |  |
| 116 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_MTGE (资产抵押)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_MTGE_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_ID | 资产 | GUID | Y |  |
| 5 | ASSET_TRANS_SEQNO | 资产交易序号 | number | Y |  |
| 6 | ASSET_MTGE_SEQNO | 资产抵押序号 | number | Y |  |
| 7 | MTGE_DATE | 抵押日期 | date | Y |  |
| 8 | MTGE_CUTOFF_DATA | 结束日期 | date | Y |  |
| 9 | MTGE_RESCISSION_DATE | 解除日期 | date | Y |  |
| 10 | MORTGAGEE | 抵押权人 | string(144) | Y |  |
| 11 | MTGE_CONTRACT | 抵押合同 | string(80) | Y |  |
| 12 | MTGE_DOC_TYPE | 抵押单据类型 | number | Y |  |
| 13 | MTGE_DOC_NO | 抵押单据单号 | string(80) | Y |  |
| 14 | MTGE_DOC_LINE_SEQNO | 抵押单据行序号 | number | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | CreateDate | 创建日期 | date | Y |  |
| 17 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 18 | ModifiedDate | 修改日期 | date | Y |  |
| 19 | CreateBy | 创建者 | GUID | Y |  |
| 20 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 21 | ModifiedBy | 修改者 | GUID | Y |  |
| 22 | Attachments | 附件 | string | Y |  |
| 23 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
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
| 43 | Owner_Org_RTK |  | string(400) | Y |  |
| 44 | Owner_Org_ROid |  | GUID | Y |  |
| 45 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 46 | SOURCE_ID_ROid |  | GUID | Y |  |
| 47 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 48 | SOURCE2_ID_ROid |  | GUID | Y |  |

### ASSET_OUTSIDE (资产外送单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_OUTSIDE_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | ACCOUNT_PERIOD_CODE | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 外送日期 | date | Y |  |
| 11 | OUTSIDE_QTY | 外送数量 | number(16,6) | Y |  |
| 12 | ABANDON_QTY | 不需收回数量 | number(16,6) | Y |  |
| 13 | RETURN_QTY | 已收回数量 | number(16,6) | Y |  |
| 14 | REMARK | 备注 | string(510) | Y |  |
| 15 | PrintCount | 打印次数 | number | Y |  |
| 16 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 17 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 18 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 19 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 20 | CreateDate | 创建日期 | date | Y |  |
| 21 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 22 | ModifiedDate | 修改日期 | date | Y |  |
| 23 | CreateBy | 创建者 | GUID | Y |  |
| 24 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 25 | ModifiedBy | 修改者 | GUID | Y |  |
| 26 | Attachments | 附件 | string | Y |  |
| 27 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 28 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_OUTSIDE_D (资产外送单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_OUTSIDE_D_ID | 主键 | GUID | Y | Y |
| 3 | ASSET_ID | 资产 | GUID | Y |  |
| 4 | ASSET_NAME | 资产名称 | string(120) | Y |  |
| 5 | ASSET_SPECIFICATION | 资产规格 | string(510) | Y |  |
| 6 | ASSET_STATUS | 资产状态 | number | Y |  |
| 7 | EMPLOYEE_ID | 责任人 | GUID | Y |  |
| 8 | ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 9 | OUTSIDE_PLACE | 外送地点 | string(510) | Y |  |
| 10 | ESTI_RETURN_DATE | 预计收回日期 | date | Y |  |
| 11 | RETURN_STATUS | 收回状态 | string(40) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | ABANDON_REMARK | 备注2 | string(510) | Y |  |
| 14 | PREVIOUS_RETURN_DATE | 上次外送收回日期 | date | Y |  |
| 15 | PREVIOUS_ASSET_OUTSIDE_ID | 上次外送单据 | GUID | Y |  |
| 16 | PREVIOUS_ASSET_OUTSIDE_D_ID | 上次外送序号 | GUID | Y |  |
| 17 | PREVIOUS_OUTSIDE_DATE | 上次外送日期 | date | Y |  |
| 18 | PREVIOUS_OUTSIDE_PLACE | 上次外送地点 | string(510) | Y |  |
| 19 | PREVIOUS_ESTI_RETURN_DATE | 上次外送预计收回日期 | date | Y |  |
| 20 | PREVIOUS_EMPLOYEE_ID | 上次外送责任人 | GUID | Y |  |
| 21 | PREVIOUS_ADMIN_UNIT_ID | 上次外送责任部门 | GUID | Y |  |
| 22 | ASSET_RETURN_ID | 资产收回单 | GUID | Y |  |
| 23 | CreateDate | 创建日期 | date | Y |  |
| 24 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 25 | ModifiedDate | 修改日期 | date | Y |  |
| 26 | CreateBy | 创建者 | GUID | Y |  |
| 27 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 28 | ModifiedBy | 修改者 | GUID | Y |  |
| 29 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 48 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 49 | ApproveDate | 修改日期 | date | Y |  |
| 50 | ApproveBy | 修改人 | GUID | Y |  |
| 51 | ASSET_OUTSIDE_ID |  | GUID | Y |  |

### ASSET_PTA_HISTORY (采购转资产历史档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_PTA_HISTORY_ID | 主键 | GUID | Y | Y |
| 4 | QUANTITY | 转资数量 | number | Y |  |
| 5 | SYS_CTRL_COUNT | 系统控制计数器 | number | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | Attachments | 附件 | string | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | Owner_Org_RTK |  | string(400) | Y |  |
| 34 | Owner_Org_ROid |  | GUID | Y |  |
| 35 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 36 | SOURCE_ID_ROid |  | GUID | Y |  |
| 37 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE2_ID_ROid |  | GUID | Y |  |

### ASSET_PTABC (采购转资产批次控制档)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_PTABC_ID | 主键 | GUID | Y | Y |
| 4 | SYS_TASK_ID | 作业ID | GUID | Y |  |
| 5 | SYS_TASK_LINE_ID | 作业行ID | GUID | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 31 | Attachments | 附件 | string | Y |  |
| 32 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 33 | Owner_Org_RTK |  | string(400) | Y |  |
| 34 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_RETURN

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_RETURN_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 收回日期 | date | Y |  |
| 11 | RETURN_QTY | 收回数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 15 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 16 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 17 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_RETURN_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_RETURN_D_ID | 主键 | GUID | Y | Y |
| 3 | ASSET_NAME | 资产名称 | string(120) | Y |  |
| 4 | ASSET_SPECIFICATION | 资产规格 | string(510) | Y |  |
| 5 | OUTSIDE_DATE | 外送日期 | date | Y |  |
| 6 | ASSET_ID | 资产 | GUID | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | ASSET_OUTSIDE_ID | 外送单据 | GUID | Y |  |
| 9 | ASSET_OUTSIDE_D_ID | 外送序号 | GUID | Y |  |
| 10 | EMPLOYEE_ID | 责任人 | GUID | Y |  |
| 11 | ADMIN_UNIT_ID | 责任部门 | GUID | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 37 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 38 | ApproveDate | 修改日期 | date | Y |  |
| 39 | ApproveBy | 修改人 | GUID | Y |  |
| 40 | ASSET_RETURN_ID |  | GUID | Y |  |

### ASSET_REVALUE (资产重估单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ASSET_REVALUE_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ASSET_ID | 资产 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 13 | ASSET_NATURE | 资产性质 | number | Y |  |
| 14 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 15 | ASSET_STATUS | 资产状态 | number | Y |  |
| 16 | ZERO_FLAG | 重估价值为零标识 | number(0/1) | Y |  |
| 17 | REVALUE_AMT | 重估价值 | number(23,8) | Y |  |
| 18 | AD_FLAG | 会计维度标识 | number(0/1) | Y |  |
| 19 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 20 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 21 | UNDEPR_PERIODS | 待摊提期数 | number | Y |  |
| 22 | EXTEND_UNDEPR_PERIODS | 延续摊提_待摊提期数 | number | Y |  |
| 23 | O_CARRYING_AMT | 原账面价值 | number(23,8) | Y |  |
| 24 | O_REVALUEDIFF_AMT | 原重估差价 | number(23,8) | Y |  |
| 25 | REVALUEDIFF_AMT | 本次重估差价 | number(23,8) | Y |  |
| 26 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 27 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 28 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 29 | TD_FLAG | 税务维度标识 | number(0/1) | Y |  |
| 30 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 31 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 32 | TD_UNDEPR_PERIODS | 税务_待摊提期数 | number | Y |  |
| 33 | TD_EXTEND_UNDEPR_PERIODS | 税务_延续摊提_待摊提期数 | number | Y |  |
| 34 | TD_O_CARRYING_AMT | 税务_原账面价值 | number(23,8) | Y |  |
| 35 | TD_O_REVALUEDIFF_AMT | 税务_原重估差价 | number(23,8) | Y |  |
| 36 | TD_REVALUEDIFF_AMT | 税务_本次重估差价 | number(23,8) | Y |  |
| 37 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 38 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 39 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 40 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 41 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 42 | REMARK | 备注 | string(510) | Y |  |
| 43 | O_RESIDUAL_AMT | 原净残值 | number(23,8) | Y |  |
| 44 | O_EXTEND_RESIDUAL_AMT | 原延续摊提_净残值 | number(23,8) | Y |  |
| 45 | TD_O_RESIDUAL_AMT | 税务_原净残值 | number(23,8) | Y |  |
| 46 | TD_O_EXTEND_RESIDUAL_AMT | 税务_原延续摊提_净残值 | number(23,8) | Y |  |
| 47 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 48 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 49 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 50 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 51 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 52 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 53 | CreateDate | 创建日期 | date | Y |  |
| 54 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 55 | ModifiedDate | 修改日期 | date | Y |  |
| 56 | CreateBy | 创建者 | GUID | Y |  |
| 57 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 58 | ModifiedBy | 修改者 | GUID | Y |  |
| 59 | Attachments | 附件 | string | Y |  |
| 60 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 61 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 62 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 63 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 64 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 65 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 66 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 67 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 68 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 69 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 70 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 71 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 72 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 73 | UDF041 | 自定义字段12 | date | Y |  |
| 74 | UDF042 | 自定义字段13 | date | Y |  |
| 75 | UDF051 | 自定义字段14 | GUID | Y |  |
| 76 | UDF052 | 自定义字段15 | GUID | Y |  |
| 77 | UDF053 | 自定义字段16 | GUID | Y |  |
| 78 | UDF054 | 自定义字段17 | GUID | Y |  |
| 79 | Version | 版本号，不要随意更改 | binary | Y |  |
| 80 | PrintCount | 打印次数 | number | Y |  |
| 81 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 82 | ApproveDate | 修改日期 | date | Y |  |
| 83 | ApproveBy | 修改人 | GUID | Y |  |
| 84 | Owner_Org_RTK |  | string(400) | Y |  |
| 85 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_SCRAP

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_SCRAP_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 11 | ASSET_NATURE | 资产性质 | number | Y |  |
| 12 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 13 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 14 | DEPR_ACTION_DATE | 影响摊提日期 | date | Y |  |
| 15 | ACQUISITION_AMT | 取得成本 | number(23,8) | Y |  |
| 16 | IMPROVEMENT_AMT | 改良成本 | number(23,8) | Y |  |
| 17 | FVC_AMT | 公允价值变动 | number(23,8) | Y |  |
| 18 | CURRENT_AMT | 现行原值 | number(23,8) | Y |  |
| 19 | ACCUM_DEPR_AMT | 累计摊提 | number(23,8) | Y |  |
| 20 | IMPAIRMENT_AMT | 减值准备 | number(23,8) | Y |  |
| 21 | CARRYING_AMT | 账面价值 | number(23,8) | Y |  |
| 22 | REVALUATION_SURPLUS_AMT | 重估价盈余 | number(23,8) | Y |  |
| 23 | ASSET_ID | 资产 | GUID | Y |  |
| 24 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 25 | EMPLOYEE_ID | 处置人员 | GUID | Y |  |
| 26 | ADMIN_UNIT_ID | 处置部门 | GUID | Y |  |
| 27 | FVCP_TRANSFERRING_AMT | 公允价值变动收益(转换) | number(23,8) | Y |  |
| 28 | ACCUM_FVCP_AMT | 累计公允价值变动收益 | number(23,8) | Y |  |
| 29 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 30 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 31 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 32 | REMARK | 备注 | string(510) | Y |  |
| 33 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 34 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 35 | ASSET_STATUS | 资产状态 | number | Y |  |
| 36 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 37 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 38 | TD_ACQUISITION_AMT | 税务_取得成本 | number(23,8) | Y |  |
| 39 | TD_IMPROVEMENT_AMT | 税务_改良成本 | number(23,8) | Y |  |
| 40 | TD_FVC_AMT | 税务_公允价值变动 | number(23,8) | Y |  |
| 41 | TD_CURRENT_AMT | 税务_现行原值 | number(23,8) | Y |  |
| 42 | TD_ACCUM_DEPR_AMT | 税务_累计摊提 | number(23,8) | Y |  |
| 43 | TD_IMPAIRMENT_AMT | 税务_减值准备 | number(23,8) | Y |  |
| 44 | TD_CARRYING_AMT | 税务_账面价值 | number(23,8) | Y |  |
| 45 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 46 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 47 | TD_REVALUATION_SURPLUS_AMT | 税务_重估价盈余 | number(23,8) | Y |  |
| 48 | TD_FVCP_TRANSFERRING_AMT | 税务_公允价值变动收益(转换) | number(23,8) | Y |  |
| 49 | TD_ACCUM_FVCP_AMT | 税务_累计公允价值变动收益 | number(23,8) | Y |  |
| 50 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 51 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 52 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 53 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 54 | PrintCount | 打印次数 | number | Y |  |
| 55 | CreateDate | 创建日期 | date | Y |  |
| 56 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 57 | ModifiedDate | 修改日期 | date | Y |  |
| 58 | CreateBy | 创建者 | GUID | Y |  |
| 59 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 60 | ModifiedBy | 修改者 | GUID | Y |  |
| 61 | Attachments | 附件 | string | Y |  |
| 62 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 63 | Version | 版本号，不要随意更改 | binary | Y |  |
| 64 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 65 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 66 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 67 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 68 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 69 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 70 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 71 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 72 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 73 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 74 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 75 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 76 | UDF041 | 自定义字段12 | date | Y |  |
| 77 | UDF042 | 自定义字段13 | date | Y |  |
| 78 | UDF051 | 自定义字段14 | GUID | Y |  |
| 79 | UDF052 | 自定义字段15 | GUID | Y |  |
| 80 | UDF053 | 自定义字段16 | GUID | Y |  |
| 81 | UDF054 | 自定义字段17 | GUID | Y |  |
| 82 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 83 | ApproveDate | 修改日期 | date | Y |  |
| 84 | ApproveBy | 修改人 | GUID | Y |  |
| 85 | Owner_Org_RTK |  | string(400) | Y |  |
| 86 | Owner_Org_ROid |  | GUID | Y |  |
| 87 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 88 | IGNORE_FLAG | 忽略当期摊提标识 | number(0/1) | Y |  |
| 89 | REVALUEDIFF_AMT | 重估差价 | number(23,8) | Y |  |
| 90 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 91 | TD_IGNORE_FLAG | 税务_忽略当期摊提标识 | number(0/1) | Y |  |
| 92 | TD_REVALUEDIFF_AMT | 税务_重估差价 | number(23,8) | Y |  |

### ASSET_SELL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_SELL_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 11 | ASSET_ID | 资产编号 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产 | GUID | Y |  |
| 13 | ASSET_NATURE | 资产性质 | number | Y |  |
| 14 | ACQUISITION_AMT | 取得成本 | number(23,8) | Y |  |
| 15 | IMPROVEMENT_AMT | 改良成本 | number(23,8) | Y |  |
| 16 | FVC_AMT | 公允价值变动 | number(23,8) | Y |  |
| 17 | CURRENT_AMT | 现行原值 | number(23,8) | Y |  |
| 18 | ACCUM_DEPR_AMT | 累计摊提 | number(23,8) | Y |  |
| 19 | IMPAIRMENT_AMT | 减值准备 | number(23,8) | Y |  |
| 20 | CARRYING_AMT | 账面价值 | number(23,8) | Y |  |
| 21 | REVALUATION_SURPLUS_AMT | 重估价盈余 | number(23,8) | Y |  |
| 22 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 23 | ASSET_STATUS | 资产状态 | number | Y |  |
| 24 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 25 | DEPR_ACTION_DATE | 影响摊提日期 | date | Y |  |
| 26 | EMPLOYEE_ID | 处置人员 | GUID | Y |  |
| 27 | ADMIN_UNIT_ID | 处置部门 | GUID | Y |  |
| 28 | TAX_TC | 税额(原币) | number(23,8) | Y |  |
| 29 | TAX_RATE | 税率 | number(5,4) | Y |  |
| 30 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 31 | ACCUM_FVCP_AMT | 累计公允价值变动收益 | number(23,8) | Y |  |
| 32 | FVCP_TRANSFERRING_AMT | 公允价值变动收益(转换) | number(23,8) | Y |  |
| 33 | AMT_UNTAX_TC | 无税金额(原币) | number(23,8) | Y |  |
| 34 | TAX_ID | 税种税率 | GUID | Y |  |
| 35 | TAX_INCLUDED_INDICATOR | 含税标识 | number(0/1) | Y |  |
| 36 | PROFIT_AMT | 出售收益 | number(23,8) | Y |  |
| 37 | AMT_FC | 价税合计(本币) | number(23,8) | Y |  |
| 38 | TAX_FC | 税额(本币) | number(23,8) | Y |  |
| 39 | AMT_UNTAX_FC | 无税金额(本币) | number(23,8) | Y |  |
| 40 | AMT_TC | 价税合计(原币) | number(23,8) | Y |  |
| 41 | GLMB_JE_INDICATOR | 已生成管理账簿分录 | number(0/1) | Y |  |
| 42 | GLOB_JE_INDICATOR | 已生成运营账簿分录 | number(0/1) | Y |  |
| 43 | GLOB_JE_ID | 运营账簿分录 | GUID | Y |  |
| 44 | GLMB_JE_ID | 管理账簿分录 | GUID | Y |  |
| 45 | REMARK | 备注 | string(510) | Y |  |
| 46 | CURRENCY_ID | 货币 | GUID | Y |  |
| 47 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 48 | SALES_CENTER_ID | 销售域 | GUID | Y |  |
| 49 | SETTLEMENT_CUSTOMER_ID | 结算客户 | GUID | Y |  |
| 50 | ORDER_CUSTOMER_ID | 订货客户 | GUID | Y |  |
| 51 | VAT_FLAG | VAT标识 | number(0/1) | Y |  |
| 52 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 53 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 54 | TD_ACQUISITION_AMT | 税务_取得成本 | number(23,8) | Y |  |
| 55 | TD_IMPROVEMENT_AMT | 税务_改良成本 | number(23,8) | Y |  |
| 56 | TD_FVC_AMT | 税务_公允价值变动 | number(23,8) | Y |  |
| 57 | TD_CURRENT_AMT | 税务_现行原值 | number(23,8) | Y |  |
| 58 | TD_ACCUM_DEPR_AMT | 税务_累计摊提 | number(23,8) | Y |  |
| 59 | TD_IMPAIRMENT_AMT | 税务_减值准备 | number(23,8) | Y |  |
| 60 | TD_CARRYING_AMT | 税务_账面价值 | number(23,8) | Y |  |
| 61 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 62 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 63 | TD_REVALUATION_SURPLUS_AMT | 税务_重估价盈余 | number(23,8) | Y |  |
| 64 | TD_FVCP_TRANSFERRING_AMT | 税务_公允价值变动收益(转换) | number(23,8) | Y |  |
| 65 | TD_ACCUM_FVCP_AMT | 税务_累计公允价值变动收益 | number(23,8) | Y |  |
| 66 | TD_PROFIT_AMT | 税务_出售收益 | number(23,8) | Y |  |
| 67 | CreateDate | 创建日期 | date | Y |  |
| 68 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 69 | ModifiedDate | 修改日期 | date | Y |  |
| 70 | CreateBy | 创建者 | GUID | Y |  |
| 71 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 72 | ModifiedBy | 修改者 | GUID | Y |  |
| 73 | Attachments | 附件 | string | Y |  |
| 74 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 75 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 76 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 77 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 78 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 79 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 80 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 81 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 82 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 83 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 84 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 85 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 86 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 87 | UDF041 | 自定义字段12 | date | Y |  |
| 88 | UDF042 | 自定义字段13 | date | Y |  |
| 89 | UDF051 | 自定义字段14 | GUID | Y |  |
| 90 | UDF052 | 自定义字段15 | GUID | Y |  |
| 91 | UDF053 | 自定义字段16 | GUID | Y |  |
| 92 | UDF054 | 自定义字段17 | GUID | Y |  |
| 93 | Version | 版本号，不要随意更改 | binary | Y |  |
| 94 | PrintCount | 打印次数 | number | Y |  |
| 95 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 96 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 97 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 98 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 99 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 100 | ApproveDate | 修改日期 | date | Y |  |
| 101 | ApproveBy | 修改人 | GUID | Y |  |
| 102 | Owner_Org_RTK |  | string(400) | Y |  |
| 103 | Owner_Org_ROid |  | GUID | Y |  |
| 104 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 105 | SOURCE_ID_ROid |  | GUID | Y |  |
| 106 | SOURCE1_ID_RTK |  | string(400) | Y |  |
| 107 | SOURCE1_ID_ROid |  | GUID | Y |  |
| 108 | SOURCE2_ID_RTK |  | string(400) | Y |  |
| 109 | SOURCE2_ID_ROid |  | GUID | Y |  |
| 110 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 111 | IGNORE_FLAG | 忽略当期摊提标识 | number(0/1) | Y |  |
| 112 | REVALUEDIFF_AMT | 重估差价 | number(23,8) | Y |  |
| 113 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 114 | TD_IGNORE_FLAG | 税务_忽略当期摊提标识 | number(0/1) | Y |  |
| 115 | TD_REVALUEDIFF_AMT | 税务_重估差价 | number(23,8) | Y |  |
| 116 | ACCOUNTS_SYS_FLAG | 需往来系统结算标识 | number(0/1) | Y |  |
| 117 | SETTLE_STATUS | 结算状态 | string(40) | Y |  |
| 118 | ITEM_ID | 资产品号 | GUID | Y |  |
| 119 | UNIT_ID | 主键 | GUID | Y |  |
| 120 | PRICE_QTY | 计价数量 | number(16,6) | Y |  |
| 121 | SETTLED_QTY | 已结算数量 | number(16,6) | Y |  |
| 122 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |

### ASSET_STATS_CATEGORY (资产统计分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | ASSET_STATS_CATEGORY_ID | 主键 | GUID | Y | Y |
| 4 | ASSET_STATS_CATEGORY_CODE | 分类编号 | string(80) | Y |  |
| 5 | ASSET_STATS_CATEGORY_NAME | 分类名称 | string(120) | Y |  |
| 6 | ASSET_STATS_CATEGORY_SPEC | 分类规格 | string(510) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 33 | Attachments | 附件 | string | Y |  |
| 34 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 35 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 36 | ApproveDate | 修改日期 | date | Y |  |
| 37 | ApproveBy | 修改人 | GUID | Y |  |
| 38 | Owner_Org_RTK |  | string(400) | Y |  |
| 39 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_TDI (维护税维初始单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_TDI_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 11 | ASSET_ID | 资产 | GUID | Y |  |
| 12 | ASSET_CATEGORY_ID | 资产类别 | GUID | Y |  |
| 13 | ASSET_NATURE | 资产性质 | number | Y |  |
| 14 | MEASUREMENT_MODE | 计量模式 | number | Y |  |
| 15 | ASSET_STATUS | 资产状态 | number | Y |  |
| 16 | ACQUISITION_DATE | 取得日期 | date | Y |  |
| 17 | CURRENCY_ID | 货币 | GUID | Y |  |
| 18 | EXCHANGE_RATE | 汇率 | number(18,9) | Y |  |
| 19 | ACQUISITION_AMT_TC | 取得成本(原币) | number(23,8) | Y |  |
| 20 | ACQUISITION_AMT | 取得成本 | number(23,8) | Y |  |
| 21 | IMPROVEMENT_AMT | 改良成本 | number(23,8) | Y |  |
| 22 | FVC_AMT | 公允价值变动 | number(23,8) | Y |  |
| 23 | CURRENT_AMT | 现行原值 | number(23,8) | Y |  |
| 24 | ACCUM_DEPR_AMT | 累计摊提 | number(23,8) | Y |  |
| 25 | NET_AMT | 资产净值 | number(23,8) | Y |  |
| 26 | IMPAIRMENT_AMT | 减值准备 | number(23,8) | Y |  |
| 27 | CARRYING_AMT | 账面价值 | number(23,8) | Y |  |
| 28 | RESIDUAL_AMT | 净残值 | number(23,8) | Y |  |
| 29 | BENCHMARK_RESI_RATE | 基准净残值率 | number(11,10) | Y |  |
| 30 | REVALUATION_SURPLUS_AMT | 重估价盈余 | number(23,8) | Y |  |
| 31 | FVCP_TRANSFERRING_AMT | 公允价值变动收益(转换) | number(23,8) | Y |  |
| 32 | ACCUM_FVCP_AMT | 累计公允价值变动收益 | number(23,8) | Y |  |
| 33 | DEPR_METHOD | 摊提方法 | number | Y |  |
| 34 | START_DEPR_DATE | 开始摊提日期 | date | Y |  |
| 35 | ESTI_DEPR_PERIODS | 预计摊提期数 | number | Y |  |
| 36 | DEPRED_PERIODS | 已摊提期数 | number | Y |  |
| 37 | UNDEPR_PERIODS | 待摊提期数 | number | Y |  |
| 38 | ESTI_UNITS | 预计总工作量 | number(16,6) | Y |  |
| 39 | USED_UNITS | 已使用工作量 | number(16,6) | Y |  |
| 40 | EXTEND_DEPR_FLAG | 延续摊提标识 | number(0/1) | Y |  |
| 41 | EXTEND_ESTI_DEPR_PERIODS | 延续摊提_预计摊提期数 | number | Y |  |
| 42 | EXTEND_DEPRED_PERIODS | 延续摊提_已摊提期数 | number | Y |  |
| 43 | EXTEND_UNDEPR_PERIODS | 延续摊提_待摊提期数 | number | Y |  |
| 44 | EXTEND_RESIDUAL_AMT | 延续摊提_净残值 | number(23,8) | Y |  |
| 45 | DEPR_STATUS | 摊提状态 | number | Y |  |
| 46 | ASSET_MACRODEPR_FLAG | 资产宏观摊提控制标识 | number(0/1) | Y |  |
| 47 | TD_ACQUISITION_AMT_TC | 税务_取得成本(原币) | number(23,8) | Y |  |
| 48 | TD_ACQUISITION_AMT | 税务_取得成本 | number(23,8) | Y |  |
| 49 | TD_IMPROVEMENT_AMT | 税务_改良成本 | number(23,8) | Y |  |
| 50 | TD_FVC_AMT | 税务_公允价值变动 | number(23,8) | Y |  |
| 51 | TD_CURRENT_AMT | 税务_现行原值 | number(23,8) | Y |  |
| 52 | TD_ACCUM_DEPR_AMT | 税务_累计摊提 | number(23,8) | Y |  |
| 53 | TD_NET_AMT | 税务_资产净值 | number(23,8) | Y |  |
| 54 | TD_IMPAIRMENT_AMT | 税务_减值准备 | number(23,8) | Y |  |
| 55 | TD_CARRYING_AMT | 税务_账面价值 | number(23,8) | Y |  |
| 56 | TD_RESIDUAL_AMT | 税务_净残值 | number(23,8) | Y |  |
| 57 | TD_BENCHMARK_RESI_RATE | 税务_基准净残值率 | number(11,10) | Y |  |
| 58 | TD_REVALUATION_SURPLUS_AMT | 税务_重估价盈余 | number(23,8) | Y |  |
| 59 | TD_FVCP_TRANSFERRING_AMT | 税务_公允价值变动收益(转换) | number(23,8) | Y |  |
| 60 | TD_ACCUM_FVCP_AMT | 税务_累计公允价值变动收益 | number(23,8) | Y |  |
| 61 | TD_DEPR_METHOD | 税务_摊提方法 | number | Y |  |
| 62 | TD_START_DEPR_DATE | 税务_开始摊提日期 | date | Y |  |
| 63 | TD_ESTI_DEPR_PERIODS | 税务_预计摊提期数 | number | Y |  |
| 64 | TD_DEPRED_PERIODS | 税务_已摊提期数 | number | Y |  |
| 65 | TD_UNDEPR_PERIODS | 税务_待摊提期数 | number | Y |  |
| 66 | TD_ESTI_UNITS | 税务_预计总工作量 | number(16,6) | Y |  |
| 67 | TD_USED_UNITS | 税务_已使用工作量 | number(16,6) | Y |  |
| 68 | TD_EXTEND_DEPR_FLAG | 税务_延续摊提标识 | number(0/1) | Y |  |
| 69 | TD_EXTEND_ESTI_DEPR_PERIODS | 税务_延续摊提_预计摊提期数 | number | Y |  |
| 70 | TD_EXTEND_DEPRED_PERIODS | 税务_延续摊提_已摊提期数 | number | Y |  |
| 71 | TD_EXTEND_UNDEPR_PERIODS | 税务_延续摊提_待摊提期数 | number | Y |  |
| 72 | TD_EXTEND_RESIDUAL_AMT | 税务_延续摊提_净残值 | number(23,8) | Y |  |
| 73 | TD_DEPR_STATUS | 税务_摊提状态 | number | Y |  |
| 74 | TD_ASSET_MACRODEPR_FLAG | 税务_资产宏观摊提控制标识 | number(0/1) | Y |  |
| 75 | TD_ASSET_MATURITY_FLAG | 税务_资产到期标识 | number(0/1) | Y |  |
| 76 | REMARK | 备注 | string(510) | Y |  |
| 77 | TD_O_ACQUISITION_AMT_TC | 税务_原取得成本(原币) | number(23,8) | Y |  |
| 78 | TD_O_ACQUISITION_AMT | 税务_原取得成本 | number(23,8) | Y |  |
| 79 | TD_O_IMPROVEMENT_AMT | 税务_原改良成本 | number(23,8) | Y |  |
| 80 | TD_O_FVC_AMT | 税务_原公允价值变动 | number(23,8) | Y |  |
| 81 | TD_O_CURRENT_AMT | 税务_原现行原值 | number(23,8) | Y |  |
| 82 | TD_O_ACCUM_DEPR_AMT | 税务_原累计摊提 | number(23,8) | Y |  |
| 83 | TD_O_NET_AMT | 税务_原资产净值 | number(23,8) | Y |  |
| 84 | TD_O_IMPAIRMENT_AMT | 税务_原减值准备 | number(23,8) | Y |  |
| 85 | TD_O_CARRYING_AMT | 税务_原账面价值 | number(23,8) | Y |  |
| 86 | TD_O_RESIDUAL_AMT | 税务_原净残值 | number(23,8) | Y |  |
| 87 | TD_O_BENCHMARK_RESI_RATE | 税务_原基准净残值率 | number(11,10) | Y |  |
| 88 | TD_O_REVALUATION_SURPLUS_AMT | 税务_原重估价盈余 | number(23,8) | Y |  |
| 89 | TD_O_FVCP_TRANSFERRING_AMT | 税务_原公允价值变动收益(转换) | number(23,8) | Y |  |
| 90 | TD_O_ACCUM_FVCP_AMT | 税务_原累计公允价值变动收益 | number(23,8) | Y |  |
| 91 | TD_O_DEPR_METHOD | 税务_原摊提方法 | number | Y |  |
| 92 | TD_O_START_DEPR_DATE | 税务_原开始摊提日期 | date | Y |  |
| 93 | TD_O_ESTI_DEPR_PERIODS | 税务_原预计摊提期数 | number | Y |  |
| 94 | TD_O_DEPRED_PERIODS | 税务_原已摊提期数 | number | Y |  |
| 95 | TD_O_UNDEPR_PERIODS | 税务_原待摊提期数 | number | Y |  |
| 96 | TD_O_ESTI_UNITS | 税务_原预计总工作量 | number(16,6) | Y |  |
| 97 | TD_O_USED_UNITS | 税务_原已使用工作量 | number(16,6) | Y |  |
| 98 | TD_O_EXTEND_DEPR_FLAG | 税务_原延续摊提标识 | number(0/1) | Y |  |
| 99 | TD_O_EXTEND_ESTI_DEPR_PERIODS | 税务_原延续摊提_预计摊提期数 | number | Y |  |
| 100 | TD_O_EXTEND_DEPRED_PERIODS | 税务_原延续摊提_已摊提期数 | number | Y |  |
| 101 | TD_O_EXTEND_UNDEPR_PERIODS | 税务_原延续摊提_待摊提期数 | number | Y |  |
| 102 | TD_O_EXTEND_RESIDUAL_AMT | 税务_原延续摊提_净残值 | number(23,8) | Y |  |
| 103 | TD_O_DEPR_STATUS | 税务_原摊提状态 | number | Y |  |
| 104 | TD_O_ASSET_MACRODEPR_FLAG | 税务_原资产宏观摊提控制标识 | number(0/1) | Y |  |
| 105 | TD_O_ASSET_MATURITY_FLAG | 税务_原资产到期标识 | number(0/1) | Y |  |
| 106 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 107 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 108 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 109 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 110 | Version | 版本号，不要随意更改 | binary | Y |  |
| 111 | CreateDate | 创建日期 | date | Y |  |
| 112 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 113 | ModifiedDate | 修改日期 | date | Y |  |
| 114 | CreateBy | 创建者 | GUID | Y |  |
| 115 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 116 | ModifiedBy | 修改者 | GUID | Y |  |
| 117 | Attachments | 附件 | string | Y |  |
| 118 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 119 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 120 | ApproveDate | 修改日期 | date | Y |  |
| 121 | ApproveBy | 修改人 | GUID | Y |  |
| 122 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 123 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 124 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 125 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 126 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 127 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 128 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 129 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 130 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 131 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 132 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 133 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 134 | UDF041 | 自定义字段12 | date | Y |  |
| 135 | UDF042 | 自定义字段13 | date | Y |  |
| 136 | UDF051 | 自定义字段14 | GUID | Y |  |
| 137 | UDF052 | 自定义字段15 | GUID | Y |  |
| 138 | UDF053 | 自定义字段16 | GUID | Y |  |
| 139 | UDF054 | 自定义字段17 | GUID | Y |  |
| 140 | PrintCount | 打印次数 | number | Y |  |
| 141 | Owner_Org_RTK |  | string(400) | Y |  |
| 142 | Owner_Org_ROid |  | GUID | Y |  |
| 143 | REVALUEDIFF_AMT | 重估差价 | number(23,8) | Y |  |
| 144 | TD_REVALUEDIFF_AMT | 税务_重估差价 | number(23,8) | Y |  |
| 145 | TD_O_REVALUEDIFF_AMT | 税务_原重估差价 | number(23,8) | Y |  |

### ASSET_TRANSFER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | ASSET_TRANSFER_ID | 主键 | GUID | Y | Y |
| 7 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 8 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 9 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
| 10 | BOOKKEEPING_DATE | 转移日期 | date | Y |  |
| 11 | TRANSFER_QTY | 转移数量 | number(16,6) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PrintCount | 打印次数 | number | Y |  |
| 14 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 15 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 16 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 17 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Attachments | 附件 | string | Y |  |
| 25 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 45 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 46 | ApproveDate | 修改日期 | date | Y |  |
| 47 | ApproveBy | 修改人 | GUID | Y |  |
| 48 | Owner_Org_RTK |  | string(400) | Y |  |
| 49 | Owner_Org_ROid |  | GUID | Y |  |

### ASSET_TRANSFER_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_ID | 资产 | GUID | Y |  |
| 3 | ASSET_NAME | 资产名称 | string(120) | Y |  |
| 4 | ASSET_SPECIFICATION | 资产规格 | string(510) | Y |  |
| 5 | PREVIOUS_TRANSFER_DATE | 上次转移日期 | date | Y |  |
| 6 | O_RESPONSIBILITY_ORG_TYPE | 原责任组织类型 | number | Y |  |
| 7 | O_EMPLOYEE_ID | 原责任人 | GUID | Y |  |
| 8 | O_ADMIN_UNIT_ID | 原责任部门 | GUID | Y |  |
| 9 | O_ASSET_DEPR_EXP_ACCOUNT_ID | 原费用归属分类 | GUID | Y |  |
| 10 | O_LOCATION | 原存放地点 | string(510) | Y |  |
| 11 | RESPONSIBILITY_ORG_TYPE | 新责任组织类型 | number | Y |  |
| 12 | EMPLOYEE_ID | 新责任人 | GUID | Y |  |
| 13 | ADMIN_UNIT_ID | 新责任部门 | GUID | Y |  |
| 14 | ASSET_DEPR_EXP_ACCOUNT_ID | 新费用归属分类 | GUID | Y |  |
| 15 | LOCATION | 新存放地点 | string(510) | Y |  |
| 16 | REMARK | 备注 | string(510) | Y |  |
| 17 | ASSET_TRANSFER_D_ID | 主键 | GUID | Y | Y |
| 18 | CreateDate | 创建日期 | date | Y |  |
| 19 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 20 | ModifiedDate | 修改日期 | date | Y |  |
| 21 | CreateBy | 创建者 | GUID | Y |  |
| 22 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 23 | ModifiedBy | 修改者 | GUID | Y |  |
| 24 | Version | 版本号，不要随意更改 | binary | Y |  |
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
| 43 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 44 | ApproveDate | 修改日期 | date | Y |  |
| 45 | ApproveBy | 修改人 | GUID | Y |  |
| 46 | O_SOURCE_ID_RTK |  | string(400) | Y |  |
| 47 | O_SOURCE_ID_ROid |  | GUID | Y |  |
| 48 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 49 | SOURCE_ID_ROid |  | GUID | Y |  |
| 50 | ASSET_TRANSFER_ID |  | GUID | Y |  |

### ASSET_UNITS (资产工作量信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | ASSET_UNITS_ID | 主键 | GUID | Y | Y |
| 7 | BOOKKEEPING_DATE | 记账日期 | date | Y |  |
| 8 | ACCOUNT_YEAR | 会计年度 | string(8) | Y |  |
| 9 | ACCOUNT_PERIOD_SEQNO | 会计期间序号 | number | Y |  |
| 10 | ACCOUNT_PERIOD_CODE | 会计期间期号 | string(20) | Y |  |
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

### ASSET_UNITS_D (资产工作量单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ASSET_UNITS_D_ID | 主键 | GUID | Y | Y |
| 3 | ASSET_ID | 资产 | GUID | Y |  |
| 4 | DEPR_ALLOC_ORG_TYPE | 摊提分配组织类型 | number | Y |  |
| 5 | ADMIN_UNIT_ID | 部门 | GUID | Y |  |
| 6 | CURRENT_UNITS | 本期工作量 | number(16,6) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | ASSET_DEPR_EXP_ACCOUNT_ID | 费用归属分类 | GUID | Y |  |
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
| 37 | SOURCE_ID_RTK |  | string(400) | Y |  |
| 38 | SOURCE_ID_ROid |  | GUID | Y |  |
| 39 | ASSET_UNITS_ID |  | GUID | Y |  |