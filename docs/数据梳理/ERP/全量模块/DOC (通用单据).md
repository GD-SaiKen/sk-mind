---
module: "DOC"
name_zh: "通用单据"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 35
columns: 1749
category: document
tags: ["ERP", "E10", "document"]
created: 2026-06-25 10:52
---

# DOC (通用单据)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 35 | Columns: 1749

---

## Tables


- **DOC_ADJUST_GOODS (库存调整单)**
- **DOC_ADJUST_GOODS_D (库存调整单单身)**
- **DOC_BUDGET_SETUP (单据类型预算设置)**
- **DOC_D**
- **DOC_OTHER_CHARGEIN (杂收单)**
- **DOC_OTHER_CHARGEIN_D (杂收单单身)**
- **DOC_OTHER_CHARGEOUT (杂支单)**
- **DOC_OTHER_CHARGEOUT_D (杂支单单身)**
- **DOC_POS_HAND (交班单)**
- **DOC_POS_HAND_D (交班单单身)**
- **DOC_POS_ORDER**
- **DOC_POS_ORDER_D**
- **DOC_POS_ORDER_PAY**
- **DOC_POS_ORDER_PAYDETAIL**
- **DOC_POS_ORDER_PROM**
- **DOC_POS_PAYMENT (POS解款单)**
- **DOC_POS_PAYMENT_D (解款单单身)**
- **DOC_POS_SALE**
- **DOC_POS_SALE_D**
- **DOC_POS_SALE_PAY**
- **DOC_POS_SALE_PAYDETAIL**
- **DOC_POS_SALE_PROM**
- **DOC_PRINT_LAYOUT**
- **DOC_RECEIPT_PAYMENT**
- **DOC_RECEIPT_PAYMENT_D**
- **DOC_SALE_PRICE (零售售价维护单)**
- **DOC_SALE_PRICE_D**
- **DOC_SALE_PRICE_SHOP (零售售价维护单门店单身)**
- **DOC_SHOP_PAYMENT**
- **DOC_SHOP_PAYMENT_D**
- **DOC_SHOP_SALE (门店销售单)**
- **DOC_SHOP_SALE_D (门店销售单单身)**
- **DOC_SHOP_SALE_PAY (门店销售单收款子单身)**
- **DOC_SHOP_SALE_PROM (门店销售单促销子单身)**


---


---


> Tables: 35

### DOC (单据性质)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_ID | 主键 | GUID | Y | Y |
| 4 | DOC_CODE | 单据类别 | string(8) | Y |  |
| 5 | DOC_NAME | 单据名称 | string(20) | Y |  |
| 6 | DOC_FULL_NAME | 单据全称 | string(144) | Y |  |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TRANSACTION_TYPE | 交易类别 | string(2) | Y |  |
| 9 | STOCK_ACTION | 库存影响 | number | Y |  |
| 10 | RESERVED_CONTROL | 保留控制 | string(40) | Y |  |
| 11 | CODING_BY | 编码方式 | string(40) | Y |  |
| 12 | YEAR_DIGIT | 年位数 | string(2) | Y |  |
| 13 | SEQUENCE_DIGIT | 流水号位数 | number | Y |  |
| 14 | USE_NOT_IN_FORCE_LAPSED | 使用未生效已失效品号 | number(0/1) | Y |  |
| 15 | UPDATE_RECEIPT_DATE | 更新入库日 | number(0/1) | Y |  |
| 16 | UPDATE_ISSUE_DATE | 更新出库日 | number(0/1) | Y |  |
| 17 | UPDATE_STOCKTAKING_DATE | 更新盘点日 | number(0/1) | Y |  |
| 18 | AUTO_APPROVE | 自动审核 | number(0/1) | Y |  |
| 19 | AUTO_POST | 自动过账 | number(0/1) | Y |  |
| 20 | AUTO_PRINT | 自动打印 | number(0/1) | Y |  |
| 21 | PRINT_FOOTER_PER_PAGE | 每页打印页脚 | number(0/1) | Y |  |
| 22 | MODIFY_FOOTER_WHEN_PRINTING | 打印时更改页脚 | number(0/1) | Y |  |
| 23 | PRINT_SIGN_PER_PAGE | 每页打印签核 | number(0/1) | Y |  |
| 24 | MODIFY_SIGN_WHEN_PRINTING | 打印时更改签核 | number(0/1) | Y |  |
| 25 | PRINT_SUMMARY_PER_PAGE | 每页打印合计 | number(0/1) | Y |  |
| 26 | DEFAULT_FORMAT | 单据格式 | string(40) | Y |  |
| 27 | SELECT_FORMAT_WHEN_PRINTING | 打印时选择单据格式 | number(0/1) | Y |  |
| 28 | DOC_SPECIFIED_PRINTER | 凭证指定打印机 | string(510) | Y |  |
| 29 | VOUCHER_NAME | 凭证名称 | string(40) | Y |  |
| 30 | INPUTOR_APPROVER_SAME | 制单与审核可为同一人 | number(0/1) | Y |  |
| 31 | ALLOW_EDIT_OTHER | 修改/作废他人凭证 | number(0/1) | Y |  |
| 32 | SUMMARY_PRINT | 汇总打印 | number(0/1) | Y |  |
| 33 | DEFAULT_FOOTER | 页脚编号（此字段废除//建议单号：T001-151209002） | string(12) | Y |  |
| 34 | DEFAULT_SIGN | 签核编号（此字段废除//建议单号：T001-151209002） | string(12) | Y |  |
| 35 | REMARK | 备注 | string(510) | Y |  |
| 36 | ACCOUNT_PERIOD_TYPE | 应用期间类型 | string(6) | Y |  |
| 37 | REVERSE_MODE | 凭证回转方式 | number | Y |  |
| 38 | OACCBOOK_USE_INDICATOR | 启用凭证类型标识 | number(0/1) | Y |  |
| 39 | OACCBOOK_DR_EXIST | 运营账簿-应用已定义的科目约束-借方必有 | number(0/1) | Y |  |
| 40 | OACCBOOK_CR_EXIST | 运营账簿-应用已定义的科目约束-贷方必有 | number(0/1) | Y |  |
| 41 | OACCBOOK_DOC_EXIST | 运营账簿-应用已定义的科目约束-凭证必有 | number(0/1) | Y |  |
| 42 | OACCBOOK_DR_NOEXIST | 运营账簿-应用已定义的科目约束-借方必无 | number(0/1) | Y |  |
| 43 | OACCBOOK_CR_NOEXIST | 运营账簿-应用已定义的科目约束-贷方必无 | number(0/1) | Y |  |
| 44 | OACCBOOK_DOC_NOEXIST | 运营账簿-应用已定义的科目约束-凭证必无 | number(0/1) | Y |  |
| 45 | MACCBOOK_USE_INDICATOR | 管理账簿-启用凭证类型标识 | number(0/1) | Y |  |
| 46 | MACCBOOK_DR_EXIST | 管理账簿-应用已定义的科目约束-借方必有 | number(0/1) | Y |  |
| 47 | MACCBOOK_CR_EXIST | 管理账簿-应用已定义的科目约束-贷方必有 | number(0/1) | Y |  |
| 48 | MACCBOOK_DOC_EXIST | 管理账簿-应用已定义的科目约束-凭证必有 | number(0/1) | Y |  |
| 49 | MACCBOOK_DR_NOEXIST | 管理账簿-应用已定义的科目约束-借方必无 | number(0/1) | Y |  |
| 50 | MACCBOOK_CR_NOEXIST | 管理账簿-应用已定义的科目约束-贷方必无 | number(0/1) | Y |  |
| 51 | MACCBOOK_DOC_NOEXIST | 管理账簿-应用已定义的科目约束-凭证必无 | number(0/1) | Y |  |
| 52 | MANUAL_NEW_INDICATORY | 禁止手动编制凭证 | number(0/1) | Y |  |
| 53 | ALLOW_REVERSE_OTHER | 允许凭证被他人回转 | number(0/1) | Y |  |
| 54 | ALLOW_OFFSET_OTHER | 允许凭证被他人冲销 | number(0/1) | Y |  |
| 55 | ENDING_TRANS | 期末处理事务 | number | Y |  |
| 56 | ALLOW_DELETE_OTHER | 允许凭证被他人删除 | number(0/1) | Y |  |
| 57 | ALLOW_VOID_OTHER | 允许凭证被他人作废 | number(0/1) | Y |  |
| 58 | CHECK_QUOTATION | 核对报价单 | number(0/1) | Y |  |
| 59 | CHECK_CONTRACT | 核对合同 | number(0/1) | Y |  |
| 60 | CHECK_SALES_ORDER | 核对订单 | number(0/1) | Y |  |
| 61 | UNDER_RED_PRICE | 可低于红线价格销售 | number(0/1) | Y |  |
| 62 | LOT_SEQUENCE_DIGIT | 流水号位数 | number | Y |  |
| 63 | ISSUE_OVERRUN | ISSUE_OVERRUN | string(40) | Y |  |
| 64 | RECEIPT_OVERRUN | 控制超入 | string(40) | Y |  |
| 65 | ISSUE_SHORTAGE | 控制缺领 | string(40) | Y |  |
| 66 | PROCESS_TYPE | 类别 | string(40) | Y |  |
| 67 | CHECK_RECEIPT_REQUISTION | 启用入库申请 | number(0/1) | Y |  |
| 68 | AUTO_ISSUE | 启用自动领料 | number(0/1) | Y |  |
| 69 | TRANSFER_OVERRUN | 控制超转 | string(40) | Y |  |
| 70 | INTERNAL | 内部交易 | number(0/1) | Y |  |
| 71 | CHECK_PURCHASE_ORDER | 核对采购订单 | number(0/1) | Y |  |
| 72 | ALLOW_APPROVED_PRICE | 更新核价 | number(0/1) | Y |  |
| 73 | VMI | VMI到/退货 | number(0/1) | Y |  |
| 74 | AUTO_MO_RECEIPT | 自动生成生产入库单 | number(0/1) | Y |  |
| 75 | ISSUE_BY_MO | 依工单领料 | number(0/1) | Y |  |
| 76 | VERIFICATION_MODE | 核销方式 | number | Y |  |
| 77 | TAX_CONTROL_INDICATOR | 税务发票控制 | number(0/1) | Y |  |
| 78 | CASH_SETTLEMENT_INDICATOR | CASH_SETTLEMENT_INDICATOR | number(0/1) | Y |  |
| 79 | INSTALLMEN_INDICATOR | 分期收付款标识(作废) | number(0/1) | Y |  |
| 80 | AUTHORIZED_USERS | 启用限定用户策略 | number(0/1) | Y |  |
| 81 | INNER_SYNERGY_INDICATOR | 内部协同(作废) | number(0/1) | Y |  |
| 82 | TAX_INVOICE_CATEGORY_ID | 税务发票种类 | GUID | Y |  |
| 83 | AUTO_ISSUE_DOC_ID | 自动领料单据类型 | GUID | Y |  |
| 84 | ISSUE_DOC_ID | 出库单据类型 | GUID | Y |  |
| 85 | SALES_CHANGE_DOC_ID | 换货销货单据类型 | GUID | Y |  |
| 86 | RETURN_DOC_ID | 退料入库单据类型 | GUID | Y |  |
| 87 | LOT_MO_DOC_ID | 批工单单据类型 | GUID | Y |  |
| 88 | AUTO_MO_RECEIPT_DOC_ID | 生产入库单据类型 | GUID | Y |  |
| 89 | CASH_SETTLEMENT_DOC_ID | 现结单据类型 | GUID | Y |  |
| 90 | PURCHASE_DOC_ID | 采购单据类型 | GUID | Y |  |
| 91 | E_MO | 试产工单 | number(0/1) | Y |  |
| 92 | LOT_INHERIT_SOURCE_DOC | 批工单共用源工单单据类型 | number(0/1) | Y |  |
| 93 | COST_CODE | 成本码 | string(40) | Y |  |
| 94 | RECEIPT_BY_MO | 非产出信息入库 | number(0/1) | Y |  |
| 95 | TRANSFER_DIRECTION | 转移方式 | string(40) | Y |  |
| 96 | LOSS1_DOC | 配送在途损失单据类型 | GUID | Y |  |
| 97 | LOSS2_DOC | 退配在途损失单据类型 | GUID | Y |  |
| 98 | SALE_PROMOTION_METHODS | 促销方法 | string(40) | Y |  |
| 99 | TICKET_EXCLUSIVE | 折扣券互斥 | number(0/1) | Y |  |
| 100 | TRANSFER_BY_SEQ | 按序转移 | number(0/1) | Y |  |
| 101 | RETAIL_PO | 零售转采 | number(0/1) | Y |  |
| 102 | PROMOTION_APPLY_DOC | 促销适用单据 | string(40) | Y |  |
| 103 | AUTO_GIO | 自动投产 | number(0/1) | Y |  |
| 104 | NMC_INDICATOR | 受控票据管理系统标识 | number(0/1) | Y |  |
| 105 | PRINT_ONLY_CONFIRMED | 审核后方可打印 | number(0/1) | Y |  |
| 106 | CONTROLBY | 控制依据 | string(40) | Y |  |
| 107 | AUTO_APPROVE_QC | 自动审核质检业务记录 | number(0/1) | Y |  |
| 108 | DOC_DF | 默认单别 | number(0/1) | Y |  |
| 109 | MEMBER_EXCLUSIVE | 会员折扣互斥 | number(0/1) | Y |  |
| 110 | NOT_MY_BE_OUT_OF_DATE | 不含过期品 | number(0/1) | Y |  |
| 111 | OFFSET_INSTAL_ADV_DOC_ID | 分期预收付冲减单据类型 | GUID | Y |  |
| 112 | AUTO_PO | 委外时产生采购订单 | number(0/1) | Y |  |
| 113 | BC_CHECK | 拣货核对 | string(40) | Y |  |
| 114 | AUTO_WIP_TRANSFER | 自动生成工艺转移/入库单 | number(0/1) | Y |  |
| 115 | WIP_TRANSFER_DOC_ID | 工艺转移单据类型 | GUID | Y |  |
| 116 | WIP_RECEIPT_DOC_ID | 工艺入库单据类型 | GUID | Y |  |
| 117 | QC_RESULT_INPUT_TYPE | 补入质检结果方式 | string(40) | Y |  |
| 118 | PLM_DOC_TAG | PLM集成默认单别 | number(0/1) | Y |  |
| 119 | EXPORT_CONTROL | 出口贸易 | number(0/1) | Y |  |
| 120 | IFRS_TRANS | IFRS事务 | number | Y |  |
| 121 | IFRS_ADC_FLAG | 转换日差异调整标识 | number(0/1) | Y |  |
| 122 | RACCBOOK1_USE_INDICATOR | 报告账簿1-启用凭证类型标识 | number(0/1) | Y |  |
| 123 | RACCBOOK1_DR_EXIST | 报告账簿1-启用科目约束-借方必有 | number(0/1) | Y |  |
| 124 | RACCBOOK1_CR_EXIST | 报告账簿1-启用科目约束-贷方必有 | number(0/1) | Y |  |
| 125 | RACCBOOK1_DOC_EXIST | 报告账簿1-启用科目约束-凭证必有 | number(0/1) | Y |  |
| 126 | RACCBOOK1_DR_NOEXIST | 报告账簿1-启用科目约束-借方必无 | number(0/1) | Y |  |
| 127 | RACCBOOK1_CR_NOEXIST | 报告账簿1-启用科目约束-贷方必无 | number(0/1) | Y |  |
| 128 | RACCBOOK1_DOC_NOEXIST | 报告账簿1-启用科目约束-凭证必无 | number(0/1) | Y |  |
| 129 | RACCBOOK2_USE_INDICATOR | 报告账簿2-启用凭证类型标识 | number(0/1) | Y |  |
| 130 | RACCBOOK2_DR_EXIST | 报告账簿2-启用科目约束-借方必有 | number(0/1) | Y |  |
| 131 | RACCBOOK2_CR_EXIST | 报告账簿2-启用科目约束-贷方必有 | number(0/1) | Y |  |
| 132 | RACCBOOK2_DOC_EXIST | 报告账簿2-启用科目约束-凭证必有 | number(0/1) | Y |  |
| 133 | RACCBOOK2_DR_NOEXIST | 报告账簿2-启用科目约束-借方必无 | number(0/1) | Y |  |
| 134 | RACCBOOK2_CR_NOEXIST | 报告账簿2-启用科目约束-贷方必无 | number(0/1) | Y |  |
| 135 | RACCBOOK2_DOC_NOEXIST | 报告账簿2-启用科目约束-凭证必无 | number(0/1) | Y |  |
| 136 | OVER_REQ_QTY | 超申请数量出库 | number(0/1) | Y |  |
| 137 | CHECK_INQUIRIES | 核对询价单 | number(0/1) | Y |  |
| 138 | ORDER_CLOSE_SETTLEMENT | 订单结束才可结算 | number(0/1) | Y |  |
| 139 | LARGESS_UNCHECK | 赠/备品不核对 | number(0/1) | Y |  |
| 140 | TRANS_WIP | 抛转WIP/MES | number(0/1) | Y |  |
| 141 | PL_CARRY_OVER_FLAG | 损益结转标识 | number(0/1) | Y |  |
| 142 | ENTRY_BALANCE_FLAG | 借贷平衡 | number(0/1) | Y |  |
| 143 | ADDED_ENTRY_STMT_DATA_FLAG | 补录报表数据 | number(0/1) | Y |  |
| 144 | ALLOW_NEGATIVE_NUMBER_FLAG | 分录行允许负数 | number(0/1) | Y |  |
| 145 | PLAN_QTY_OVERWIP | 工单变更预计产量可小于WIP已发放量 | number(0/1) | Y |  |
| 146 | ENTRY_NEG_FLAG | 允许分录行金额为负数 | number(0/1) | Y |  |
| 147 | AUTO_SETTLEMENT | 自动直接结账 | number(0/1) | Y |  |
| 148 | SERVICE_TYPE_ID | 服务类型 | GUID | Y |  |
| 149 | EXTRACT_TYPE | 展料方式 | string(40) | Y |  |
| 150 | ISISSUE | 库存量不足仍产生领料单 | number(0/1) | Y |  |
| 151 | NEGOTIATE_TYPE | 议价状态 | string(40) | Y |  |
| 152 | Version | 版本号，不要随意更改 | binary | Y |  |
| 153 | CreateDate | 创建日期 | date | Y |  |
| 154 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 155 | ModifiedDate | 修改日期 | date | Y |  |
| 156 | CreateBy | 创建者 | GUID | Y |  |
| 157 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 158 | ModifiedBy | 修改者 | GUID | Y |  |
| 159 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 160 | ApproveDate | 修改日期 | date | Y |  |
| 161 | ApproveBy | 修改人 | GUID | Y |  |
| 162 | Attachments | 附件 | string | Y |  |
| 163 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 164 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 165 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 166 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 167 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 168 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 169 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 170 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 171 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 172 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 173 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 174 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 175 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 176 | UDF041 | 自定义字段12 | date | Y |  |
| 177 | UDF042 | 自定义字段13 | date | Y |  |
| 178 | UDF051 | 自定义字段14 | GUID | Y |  |
| 179 | UDF052 | 自定义字段15 | GUID | Y |  |
| 180 | UDF053 | 自定义字段16 | GUID | Y |  |
| 181 | UDF054 | 自定义字段17 | GUID | Y |  |
| 182 | Owner_Org_RTK |  | string(400) | Y |  |
| 183 | Owner_Org_ROid |  | GUID | Y |  |
| 184 | PRINT_LAYOUT1_PROGRAM_INFO | 作业编号 | string(200) | Y |  |
| 185 | PRINT_LAYOUT1_REPORT_TYPEKEY | 报表编号 | string(200) | Y |  |
| 186 | PRINT_LAYOUT1_LAYOUT | 样式编号 | string(200) | Y |  |
| 187 | PRINT_LAYOUT1_ACCOUNTBOOK | 账簿 | number | Y |  |
| 188 | PRINT_LAYOUT1_VIEW_INFO | 视图名称 | string(200) | Y |  |
| 189 | PRINT_LAYOUT2_PROGRAM_INFO | 作业编号 | string(200) | Y |  |
| 190 | PRINT_LAYOUT2_REPORT_TYPEKEY | 报表编号 | string(200) | Y |  |
| 191 | PRINT_LAYOUT2_LAYOUT | 样式编号 | string(200) | Y |  |
| 192 | PRINT_LAYOUT2_ACCOUNTBOOK | 账簿 | number | Y |  |
| 193 | PRINT_LAYOUT2_VIEW_INFO | 视图名称 | string(200) | Y |  |
| 194 | PRINT_LAYOUT3_PROGRAM_INFO | 作业编号 | string(200) | Y |  |
| 195 | PRINT_LAYOUT3_REPORT_TYPEKEY | 报表编号 | string(200) | Y |  |
| 196 | PRINT_LAYOUT3_LAYOUT | 样式编号 | string(200) | Y |  |
| 197 | PRINT_LAYOUT3_ACCOUNTBOOK | 账簿 | number | Y |  |
| 198 | PRINT_LAYOUT3_VIEW_INFO | 视图名称 | string(200) | Y |  |
| 199 | PRINT_LAYOUT4_PROGRAM_INFO | 作业编号 | string(200) | Y |  |
| 200 | PRINT_LAYOUT4_REPORT_TYPEKEY | 报表编号 | string(200) | Y |  |
| 201 | PRINT_LAYOUT4_LAYOUT | 样式编号 | string(200) | Y |  |
| 202 | PRINT_LAYOUT4_ACCOUNTBOOK | 账簿 | number | Y |  |
| 203 | PRINT_LAYOUT4_VIEW_INFO | 视图名称 | string(200) | Y |  |
| 204 | CROSS_COP_PRODUCE | 跨公司委托生产 | number(0/1) | Y |  |
| 205 | DEFAULT_FOOTER_ID | 页脚 | GUID | Y |  |
| 206 | DEFAULT_SING_ID | 签核 | GUID | Y |  |
| 207 | ACCOUNTS_SYS_FLAG | 需往来系统结算标识 | number(0/1) | Y |  |
| 208 | IMPORT_CONTROL | 进口贸易 | number(0/1) | Y |  |
| 209 | DEF_INTEREST_EXPENSE_ID | 默认利息项目 | GUID | Y |  |
| 210 | IS_NEW_ISSUE | 不足可用量产生新领料记录 | number(0/1) | Y |  |
| 211 | INVOICE_NO_RULE_ID | INVOICE编号原则 | GUID | Y |  |
| 212 | ALL_SYNERGY | 整单协同 | number(0/1) | Y |  |
| 213 | UNBAL_SAVE_FLAG | 借贷不平允许保存标识 | number(0/1) | Y |  |
| 214 | CROSS_PLANT_PRODUCE | 跨工厂委托生产 | number(0/1) | Y |  |
| 215 | AUTO_GENGER_COP_DOC | 自动生成内部订单 | number(0/1) | Y |  |
| 216 | AUTO_GENGER_PLANT_DOC | 自动生成调拨申请单 | number(0/1) | Y |  |
| 217 | CROSS_COP_SYNERGY_ID | 跨公司协同关系 | GUID | Y |  |
| 218 | CROSS_PLANT_SYNERGY_ID | 跨工厂协同关系 | GUID | Y |  |
| 219 | BORROW_INV_METHOD | 借入业务存货认定方式 | string(40) | Y |  |
| 220 | INTERNAL_TRANSFER | 内部调拨 | number(0/1) | Y |  |
| 221 | SUBCONTRACTING_TRANSFER | 工艺委外加工中主件调拨 | number(0/1) | Y |  |
| 222 | MATERIAL_TRANSFER | 材料调拨 | number(0/1) | Y |  |
| 223 | CHECK_MO | 核对工单 | number(0/1) | Y |  |
| 224 | PURCHASE_RETURN_DOC_ID | 采购退货单据类型 | GUID | Y |  |
| 225 | INVENTORY_FREEZE_ADJUST | 存货冻结后允许结存调整 | number(0/1) | Y |  |
| 226 | CHECK_TRANSFER_REQUISITION | 核对调拨申请单 | number(0/1) | Y |  |

### DOC_ADJUST_GOODS (库存调整单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | DOC_ADJUST_GOODS_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | ADJUST_DATE | 调整日期 | date | Y |  |
| 9 | SHOP_ID | 入库门店 | GUID | Y |  |
| 10 | PLANT_ID | 储运机构 | GUID | Y |  |
| 11 | WAREHOUSE_ID | 调整仓库 | GUID | Y |  |
| 12 | ADJUST_REASON | 调整原因 | string(200) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | POS_ID | POS机号 | GUID | Y |  |
| 15 | CLASS_ID | 班次 | number | Y |  |
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
| 53 | COST_DOMAIN_ID_RTK |  | string(400) | Y |  |
| 54 | COST_DOMAIN_ID_ROid |  | GUID | Y |  |

### DOC_ADJUST_GOODS_D (库存调整单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_ADJUST_GOODS_D_ID |  | GUID | Y | Y |
| 3 | ITEM_ID | 品号 | GUID | Y |  |
| 4 | ITEM_NAME | 品名 | string(120) | Y |  |
| 5 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 6 | ITEM_SPECIFICATION |  | string(510) | Y |  |
| 7 | UNIT_ID | 单位 | GUID | Y |  |
| 8 | QTY |  | number(16,6) | Y |  |
| 9 | ADJUST_DIRECT | 调整方向 | number | Y |  |
| 10 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 11 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 12 | COST | 单位成本 | number(23,8) | Y |  |
| 13 | COST_AMT | 成本金额 | number(23,8) | Y |  |
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
| 40 | DOC_ADJUST_GOODS_ID |  | GUID | Y |  |

### DOC_BUDGET_SETUP (单据类型预算设置)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_BUDGET_SETUP_ID | 主键 | GUID | Y | Y |
| 4 | DOC_CATEGORY | 单据性质 | string(40) | Y |  |
| 5 | BUDGET_FLAG | 预算管理标识 | number(0/1) | Y |  |
| 6 | REMARK | 备注 | string(510) | Y |  |
| 7 | DOC_ID | 单据类型 | GUID | Y |  |
| 8 | BUDGET_GROUP_ID | 预算组 | GUID | Y |  |
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
| 36 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 37 | ApproveDate | 修改日期 | date | Y |  |
| 38 | ApproveBy | 修改人 | GUID | Y |  |
| 39 | Owner_Org_RTK |  | string(400) | Y |  |
| 40 | Owner_Org_ROid |  | GUID | Y |  |

### DOC_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_D_ID | 主键 | GUID | Y | Y |
| 2 | REMARK | 备注 | string(510) | Y |  |
| 3 | PUSHDOWN_DOC_ID | 单据类型 | GUID | Y |  |
| 4 | TO_BELONG | 在途归属 | string(40) | Y |  |
| 5 | WAREHOUSE_ID | 在途仓 | GUID | Y |  |
| 6 | DIRECT_INVOICING_INDICATOR | 直接开票 | number(0/1) | Y |  |
| 7 | CASH_SETTLEMENT_INDICATOR | 现结 | number(0/1) | Y |  |
| 8 | REORDER_DOC_ID | 再补货单据类型 | GUID | Y |  |
| 9 | TW_TAXREGISTRATION_ID | 申报营业人 | GUID | Y |  |
| 10 | INVOICE_USE_NUMBER | 使用顺序码 | number | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |
| 18 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 19 | ApproveDate | 修改日期 | date | Y |  |
| 20 | ApproveBy | 修改人 | GUID | Y |  |
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
| 39 | ORG_RTK |  | string(400) | Y |  |
| 40 | ORG_ROid |  | GUID | Y |  |
| 41 | DISTRIBUTION_OBJECT_RTK |  | string(400) | Y |  |
| 42 | DISTRIBUTION_OBJECT_ROid |  | GUID | Y |  |
| 43 | DOC_ID |  | GUID | Y |  |

### DOC_OTHER_CHARGEIN (杂收单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | DOC_OTHER_CHARGEIN_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SHOP_ID | 门店 | GUID | Y |  |
| 9 | CHARGE_DATE | 杂收日期 | date | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | POS_ID | POS机号 | GUID | Y |  |
| 12 | CLASS_ID | 班次 | number | Y |  |
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

### DOC_OTHER_CHARGEIN_D (杂收单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_OTHER_CHARGEIN_D_ID |  | GUID | Y | Y |
| 3 | OTHER_CHARGEIN_ID | 杂收项目 | GUID | Y |  |
| 4 | SALE_PAYTYPE_ID | 支付方式 | GUID | Y |  |
| 5 | AMT |  | number(23,8) | Y |  |
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
| 32 | DOC_OTHER_CHARGEIN_ID |  | GUID | Y |  |

### DOC_OTHER_CHARGEOUT (杂支单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_OTHER_CHARGEOUT_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | SHOP_ID | 门店 | GUID | Y |  |
| 9 | CHARGE_DATE | 杂支日期 | date | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | POS_ID | POS机号 | GUID | Y |  |
| 12 | CLASS_ID | 班次 | number | Y |  |
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

### DOC_OTHER_CHARGEOUT_D (杂支单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_OTHER_CHARGEOUT_D_ID |  | GUID | Y | Y |
| 3 | OTHER_CHARGEOUT_ID | 杂支项目 | GUID | Y |  |
| 4 | SALE_PAYTYPE_ID | 支付方式 | GUID | Y |  |
| 5 | AMT |  | number(23,8) | Y |  |
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
| 32 | DOC_OTHER_CHARGEOUT_ID |  | GUID | Y |  |

### DOC_POS_HAND (交班单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_POS_HAND_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | HAND_DATE | 交班日期 | date | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | HAND_EMP | 交班人 | GUID | Y |  |
| 11 | RECEIPT_EMP | 接班人 | GUID | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | POS_ID | POS机号 | GUID | Y |  |
| 14 | CLASS_ID | 班次 | number | Y |  |
| 15 | PrintCount | 打印次数 | number | Y |  |
| 16 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 17 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 18 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 19 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 38 | CreateDate | 创建日期 | date | Y |  |
| 39 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 40 | ModifiedDate | 修改日期 | date | Y |  |
| 41 | CreateBy | 创建者 | GUID | Y |  |
| 42 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 43 | ModifiedBy | 修改者 | GUID | Y |  |
| 44 | Attachments | 附件 | string | Y |  |
| 45 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 46 | Version | 版本号，不要随意更改 | binary | Y |  |
| 47 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 48 | ApproveDate | 修改日期 | date | Y |  |
| 49 | ApproveBy | 修改人 | GUID | Y |  |
| 50 | Owner_Org_RTK |  | string(400) | Y |  |
| 51 | Owner_Org_ROid |  | GUID | Y |  |

### DOC_POS_HAND_D (交班单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_HAND_D_ID |  | GUID | Y | Y |
| 3 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 4 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 5 | CASH_DRAW_AMT | 钱箱金额 | number(23,8) | Y |  |
| 6 | PAY_AMT | 实际交接金额 | number(23,8) | Y |  |
| 7 | DIFFERENT_AMT | 长短款 | number(23,8) | Y |  |
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
| 34 | DOC_POS_HAND_ID |  | GUID | Y |  |

### DOC_POS_ORDER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_POS_ORDER_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TYPE | 交易类型 | string(40) | Y |  |
| 9 | SOURCE | 来源单类型 | string(40) | Y |  |
| 10 | SOURCE_ID | 来源单号 | string(40) | Y |  |
| 11 | SHOP_ID | 门店 | GUID | Y |  |
| 12 | QTY |  | number(16,6) | Y |  |
| 13 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 14 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 15 | SALT_TAX | 销项额 | number(23,8) | Y |  |
| 16 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 17 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 20 | CONT_MAN | 订货人 | string(20) | Y |  |
| 21 | CONT_TEL | 联系电话 | string(40) | Y |  |
| 22 | GET_MODE | 取货方式 | string(40) | Y |  |
| 23 | GET_SHOP_ID | 取货门店编号 | GUID | Y |  |
| 24 | GET_DATE | 取货日期 | date | Y |  |
| 25 | GET_TIME | 取货时间 | date | Y |  |
| 26 | SHIP_ADDR | 送货地址 | string(200) | Y |  |
| 27 | PAY_AMT | 已收金额 | number(23,8) | Y |  |
| 28 | ECSFLAG | 结案否 | number(0/1) | Y |  |
| 29 | ESC_DATE | 结案日期 | date | Y |  |
| 30 | SQUAD_NO | 班别编号 | number | Y |  |
| 31 | CARD_NO | 会员卡号 | string(60) | Y |  |
| 32 | MEMBER_ID | 会员ID | GUID | Y |  |
| 33 | POINT_QTY | 积分点数 | number(12,2) | Y |  |
| 34 | ISPRACTICE | 是否训练模式 | number(0/1) | Y |  |
| 35 | EXTRA_AMT | 溢收金额 | number(23,8) | Y |  |
| 36 | POS_ID | POS机号 | GUID | Y |  |
| 37 | SHIP_FLAG | 发货标志 | number(0/1) | Y |  |
| 38 | SHIP_DATE | 发货日期 | date | Y |  |
| 39 | ZPRODUCE_SHOP_ID | 加工地点 | GUID | Y |  |
| 40 | DELIVER_TYPE | 配送方式 | string(40) | Y |  |
| 41 | PrintCount | 打印次数 | number | Y |  |
| 42 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 43 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 44 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 45 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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
| 70 | Attachments | 附件 | string | Y |  |
| 71 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 72 | Version | 版本号，不要随意更改 | binary | Y |  |
| 73 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 74 | ApproveDate | 修改日期 | date | Y |  |
| 75 | ApproveBy | 修改人 | GUID | Y |  |
| 76 | Owner_Org_RTK |  | string(400) | Y |  |
| 77 | Owner_Org_ROid |  | GUID | Y |  |

### DOC_POS_ORDER_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_ORDER_D_ID |  | GUID | Y | Y |
| 3 | AUTHORIZER_ID | 授权人员 | GUID | Y |  |
| 4 | EMPLOYEE_ID | 营业员编号 | GUID | Y |  |
| 5 | ITEM_ID | 商品编码 | GUID | Y |  |
| 6 | BARCODE | 条码 | string(80) | Y |  |
| 7 | SCAN_NO | 扫描码 | string(80) | Y |  |
| 8 | SALE_QTY | 业务数量 | number(16,6) | Y |  |
| 9 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 10 | COUNTER_ID | 租柜 | GUID | Y |  |
| 11 | UNIT_ID | 业务单位 | GUID | Y |  |
| 12 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 13 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 14 | SALT_TAX | 销项税 | number(23,8) | Y |  |
| 15 | SALE_TAX_RATE | 销项税率 | number(5,4) | Y |  |
| 16 | POINT_QTY | 积分 | number(12,2) | Y |  |
| 17 | PROM_AMT | 优惠额 | number(23,8) | Y |  |
| 18 | MARKET_RATE | 商场折扣率 | number(5,4) | Y |  |
| 19 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 20 | SHOPPE_MARKET_GOODS_ID | 商场码 | GUID | Y |  |
| 21 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 22 | SHOPPE_CONTRACT_ID | 专柜合同 | GUID | Y |  |
| 23 | RENTER_ID | 租户 | GUID | Y |  |
| 24 | COUNTER_CONTRACT_ID | 租柜合同 | GUID | Y |  |
| 25 | COUNTRE_RATE | 租柜扣率 | number(5,4) | Y |  |
| 26 | COST_TAX_RATE | 进项税率 | number(5,4) | Y |  |
| 27 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 28 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 29 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 30 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 31 | REMARK | 备注 | string(510) | Y |  |
| 32 | PLAN_DISTRIBUTION_QTY | 已转配送任务量 | number(16,6) | Y |  |
| 33 | DISTRIBUTION_QTY | 已转配送量 | number(16,6) | Y |  |
| 34 | DRP_QTY | 已转DRP量 | number(16,6) | Y |  |
| 35 | LAST_INVENTORY_QTY | 余量库存单位数量 | number(16,6) | Y |  |
| 36 | OLD_PRICE | 原价 | number(23,8) | Y |  |
| 37 | PRICE | 成交价 | number(23,8) | Y |  |
| 38 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 39 | PLANT_ID | 发货储运机构 | GUID | Y |  |
| 40 | ZOPTIONDESCRIPTION | 选配描述 | string(1000) | Y |  |
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
| 66 | DOC_POS_ORDER_ID |  | GUID | Y |  |

### DOC_POS_ORDER_PAY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 3 | DOC_POS_ORDER_PAY_ID |  | GUID | Y | Y |
| 4 | CTTYPE | 券种/卡种编号 | string(80) | Y |  |
| 5 | PAYSERNUM | 卡券号 | string(80) | Y |  |
| 6 | SERIAL_NO | 银联卡流水号 | number | Y |  |
| 7 | DESCORE | 积分抵现扣减 | number(23,8) | Y |  |
| 8 | PAY | 收款金额 | number(23,8) | Y |  |
| 9 | EXTRA | 溢收金額 | number(23,8) | Y |  |
| 10 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 11 | CHANGED | 找零 | number(23,8) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | PAY_SOURCE | 收款来源 | string(40) | Y |  |
| 14 | PAY_DOC_ID | 尾款来源配送单号 | GUID | Y |  |
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
| 40 | DOC_POS_ORDER_ID |  | GUID | Y |  |

### DOC_POS_ORDER_PAYDETAIL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_ORDER_PAYDETAIL_ID |  | GUID | Y | Y |
| 3 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 4 | CTTYPE | 券种/卡种编号 | string(80) | Y |  |
| 5 | PAYSERNUM | 卡券号 | string(80) | Y |  |
| 6 | SERIAL_NO | 银联卡流水号 | number | Y |  |
| 7 | DESCORE | 积分抵现扣减 | number(23,8) | Y |  |
| 8 | PAY | 收款金额 | number(23,8) | Y |  |
| 9 | EXTRA | 溢收金額 | number(23,8) | Y |  |
| 10 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SEQUENCENUMBER_PARENT | 父序号 | number | Y |  |
| 13 | PAY_SOURCE | 收款来源 | string(40) | Y |  |
| 14 | PAY_DOC_ID | 尾款来源配送单号 | GUID | Y |  |
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
| 40 | DOC_POS_ORDER_PAY_ID |  | GUID | Y |  |

### DOC_POS_ORDER_PROM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_ORDER_PROM_ID |  | GUID | Y | Y |
| 3 | SEQUENCENUMBER_PARENT | 父序号 | number | Y |  |
| 4 | QTY | 参与数量 | number(16,6) | Y |  |
| 5 | AMT | 参与金额 | number(23,8) | Y |  |
| 6 | INPUT_DISC | 折扣录入 | number(23,8) | Y |  |
| 7 | DISC | 折扣金额 | number(23,8) | Y |  |
| 8 | DCTYPE | 折价方式 | string(40) | Y |  |
| 9 | CTTYPE | 券种/卡种编号 | string(80) | Y |  |
| 10 | PAYSERNUM | 卡券号 | string(80) | Y |  |
| 11 | PMT_NO | 促销单号 | string(80) | Y |  |
| 12 | PROM_ACTIVE_NO | 活动号 | string(80) | Y |  |
| 13 | SHOP_ID | 门店编号 | GUID | Y |  |
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
| 40 | DOC_POS_ORDER_D_ID |  | GUID | Y |  |

### DOC_POS_PAYMENT (POS解款单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_POS_PAYMENT_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PAYMENT_DATE | 要货日期 | date | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | RECEIPT_EMP | 接款人 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | POS_ID | POS机号 | GUID | Y |  |
| 13 | CLASS_ID | 班次 | number | Y |  |
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

### DOC_POS_PAYMENT_D (解款单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_PAYMENT_D_ID |  | GUID | Y | Y |
| 3 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 4 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 5 | CASH_DRAW_AMT | 钱箱金额 | number(23,8) | Y |  |
| 6 | PAY_AMT | 缴款金额 | number(23,8) | Y |  |
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
| 33 | DOC_POS_PAYMENT_ID |  | GUID | Y |  |

### DOC_POS_SALE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_POS_SALE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | TYPE | 交易类型 | string(40) | Y |  |
| 9 | SOURCE | 来源单类型 | string(40) | Y |  |
| 10 | SOURCE_ID | 来源单号 | string(40) | Y |  |
| 11 | QTY |  | number(16,6) | Y |  |
| 12 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 13 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 14 | SALE_TAX | 销项税 | number(23,8) | Y |  |
| 15 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 16 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 17 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 18 | REMARK | 备注 | string(510) | Y |  |
| 19 | SQUAD_NO | 班别编号 | number | Y |  |
| 20 | CARD_NO | 会员卡号 | string(60) | Y |  |
| 21 | SHOP_ID | 门店 | GUID | Y |  |
| 22 | POINT_QTY | 积分点数 | number(12,2) | Y |  |
| 23 | ISPRACTICE | 是否训练模式 | number(0/1) | Y |  |
| 24 | EXTRA_AMT | 溢收金额 | number(23,8) | Y |  |
| 25 | MEMBER_ID | 会员ID | GUID | Y |  |
| 26 | POS_ID | POS机号 | GUID | Y |  |
| 27 | PrintCount | 打印次数 | number | Y |  |
| 28 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 29 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 30 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 31 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
| 32 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 33 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 34 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 35 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 36 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 37 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 38 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 39 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 40 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 41 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 42 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 43 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 44 | UDF041 | 自定义字段12 | date | Y |  |
| 45 | UDF042 | 自定义字段13 | date | Y |  |
| 46 | UDF051 | 自定义字段14 | GUID | Y |  |
| 47 | UDF052 | 自定义字段15 | GUID | Y |  |
| 48 | UDF053 | 自定义字段16 | GUID | Y |  |
| 49 | UDF054 | 自定义字段17 | GUID | Y |  |
| 50 | CreateDate | 创建日期 | date | Y |  |
| 51 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 52 | ModifiedDate | 修改日期 | date | Y |  |
| 53 | CreateBy | 创建者 | GUID | Y |  |
| 54 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 55 | ModifiedBy | 修改者 | GUID | Y |  |
| 56 | Attachments | 附件 | string | Y |  |
| 57 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 58 | Version | 版本号，不要随意更改 | binary | Y |  |
| 59 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 60 | ApproveDate | 修改日期 | date | Y |  |
| 61 | ApproveBy | 修改人 | GUID | Y |  |
| 62 | Owner_Org_RTK |  | string(400) | Y |  |
| 63 | Owner_Org_ROid |  | GUID | Y |  |

### DOC_POS_SALE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_SALE_D_ID |  | GUID | Y | Y |
| 3 | AUTHORIZER_ID | 授权人员 | GUID | Y |  |
| 4 | BARCODE | 条码 | string(80) | Y |  |
| 5 | SCAN_NO | 扫描码 | string(80) | Y |  |
| 6 | SALE_QTY | 业务数量 | number(16,6) | Y |  |
| 7 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 8 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 9 | SALT_TAX | 销项税 | number(23,8) | Y |  |
| 10 | SALE_TAX_RATE | 销项税率 | number(5,4) | Y |  |
| 11 | POINT_QTY | 积分 | number(12,2) | Y |  |
| 12 | PROM_AMT | 优惠额 | number(23,8) | Y |  |
| 13 | MARKET_RATE | 商场扣率 | number(5,4) | Y |  |
| 14 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 15 | EMPLOYEE_ID | 营业员编号 | GUID | Y |  |
| 16 | ITEM_ID | 商品编码 | GUID | Y |  |
| 17 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 18 | COUNTER_ID | 租柜 | GUID | Y |  |
| 19 | UNIT_ID | 业务单位 | GUID | Y |  |
| 20 | SHOPPE_MARKET_GOODS_ID | 商场码 | GUID | Y |  |
| 21 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 22 | COUNTRE_RATE | 租柜扣率 | number(5,4) | Y |  |
| 23 | COST_TAX_RATE | 进项税率 | number(5,4) | Y |  |
| 24 | INVENTORY_QTY | 库存单位数量 | number(16,6) | Y |  |
| 25 | SHOPPE_CONTRACT_ID | 专柜合同 | GUID | Y |  |
| 26 | RENTER_ID | 租户 | GUID | Y |  |
| 27 | COUNTER_CONTRACT_ID | 租柜合同 | GUID | Y |  |
| 28 | SECOND_QTY | 第二数量 | number(16,6) | Y |  |
| 29 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 30 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 31 | REMARK |  | string(510) | Y |  |
| 32 | OLD_PRICE | 原价 | number(23,8) | Y |  |
| 33 | PRICE | 成交价 | number(23,8) | Y |  |
| 34 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 35 | NEWPROPERTY4 |  | string(400) | Y |  |
| 36 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 37 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 38 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 39 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 40 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 41 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 42 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 43 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 44 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 45 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 46 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 47 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 48 | UDF041 | 自定义字段12 | date | Y |  |
| 49 | UDF042 | 自定义字段13 | date | Y |  |
| 50 | UDF051 | 自定义字段14 | GUID | Y |  |
| 51 | UDF052 | 自定义字段15 | GUID | Y |  |
| 52 | UDF053 | 自定义字段16 | GUID | Y |  |
| 53 | UDF054 | 自定义字段17 | GUID | Y |  |
| 54 | CreateDate | 创建日期 | date | Y |  |
| 55 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 56 | ModifiedDate | 修改日期 | date | Y |  |
| 57 | CreateBy | 创建者 | GUID | Y |  |
| 58 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 59 | ModifiedBy | 修改者 | GUID | Y |  |
| 60 | Version | 版本号，不要随意更改 | binary | Y |  |
| 61 | DOC_POS_SALE_ID |  | GUID | Y |  |

### DOC_POS_SALE_PAY

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_SALE_PAY_ID |  | GUID | Y | Y |
| 3 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 4 | CTTYPE | 券种/卡种编号 | string(80) | Y |  |
| 5 | PAYSERNUM | 卡券号 | string(80) | Y |  |
| 6 | SERIAL_NO | 银联卡流水号 | number | Y |  |
| 7 | DESCORE | 积分抵现扣减 | number(23,8) | Y |  |
| 8 | PAY | 收款金额 | number(23,8) | Y |  |
| 9 | EXTRA | 溢收金額 | number(23,8) | Y |  |
| 10 | CHANGED | 找零 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 13 | PAY_SOURCE | 收款来源 | string(40) | Y |  |
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
| 39 | DOC_POS_SALE_ID |  | GUID | Y |  |

### DOC_POS_SALE_PAYDETAIL

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_SALE_PAYDETAIL_ID |  | GUID | Y | Y |
| 3 | SEQUENCENUMBER_PARENT | 父序号 | number | Y |  |
| 4 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 5 | CTTYPE | 券种/卡种编号 | string(80) | Y |  |
| 6 | PAYSERNUM | 卡券号 | string(80) | Y |  |
| 7 | SERIAL_NO | 银联卡流水号 | number | Y |  |
| 8 | DESCORE | 积分抵现扣减 | number(23,8) | Y |  |
| 9 | PAY | 收款金额 | number(23,8) | Y |  |
| 10 | EXTRA | 溢收金額 | number(23,8) | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 13 | PAY_SOURCE | 收款来源 | string(40) | Y |  |
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
| 39 | DOC_POS_SALE_PAY_ID |  | GUID | Y |  |

### DOC_POS_SALE_PROM

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_POS_SALE_PROM_ID |  | GUID | Y | Y |
| 3 | SEQUENCENUMBER_PARENT | 父序号 | number | Y |  |
| 4 | QTY | 参与数量 | number(16,6) | Y |  |
| 5 | AMT | 参与金额 | number(23,8) | Y |  |
| 6 | INPUT_DISC | 折扣录入 | number(23,8) | Y |  |
| 7 | DISC | 折扣金额 | number(23,8) | Y |  |
| 8 | DCTYPE | 折价方式 | string(40) | Y |  |
| 9 | CTTYPE | 券种/卡种编号 | string(80) | Y |  |
| 10 | PAYSERNUM | 卡券号 | string(80) | Y |  |
| 11 | PMT_NO | 促销单号 | string(80) | Y |  |
| 12 | PROM_ACTIVE_NO | 活动号 | string(80) | Y |  |
| 13 | REMARK | 备注 | string(510) | Y |  |
| 14 | SHOP_ID | 门店编号 | GUID | Y |  |
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
| 40 | DOC_POS_SALE_D_ID |  | GUID | Y |  |

### DOC_PRINT_LAYOUT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_PRINT_LAYOUT_ID | 主键 | GUID | Y | Y |
| 3 | PROGRAM_INFO | 作业 | string(400) | Y |  |
| 4 | REPORT_TYPEKEY | 报表 | string(400) | Y |  |
| 5 | LAYOUT | 样式 | string(400) | Y |  |
| 6 | ACCOUNTBOOK | 账簿 | number | Y |  |
| 7 | VIEW_INFO | 视图名称 | string(200) | Y |  |
| 8 | Version | 版本号，不要随意更改 | binary | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 16 | ApproveDate | 修改日期 | date | Y |  |
| 17 | ApproveBy | 修改人 | GUID | Y |  |
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
| 36 | DOC_ID |  | GUID | Y |  |

### DOC_RECEIPT_PAYMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | DOC_RECEIPT_PAYMENT_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PAY_DATE | 纳款日期 | date | Y |  |
| 9 | RECEIPT_EMP | 纳款人 | GUID | Y |  |
| 10 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | RECEIPT_COMPANY_ID | 纳款公司 | GUID | Y |  |
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

### DOC_RECEIPT_PAYMENT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 3 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 4 | PAY_AMT | 缴款单金额 | number(23,8) | Y |  |
| 5 | RECEIPT_AMT | 实际纳款金额 | number(23,8) | Y |  |
| 6 | DIFFERENT_AMT | 长短款 | number(23,8) | Y |  |
| 7 | SHOP_ID | 缴款门店 | GUID | Y |  |
| 8 | HAND_EMP | 缴款人 | GUID | Y |  |
| 9 | CURRENCY_ID | 币种 | GUID | Y |  |
| 10 | HAND_COMPANY_ID | 主键 | GUID | Y |  |
| 11 | REMARK | 备注 | string(510) | Y |  |
| 12 | DOC_RECEIPT_PAYMENT_D_ID | 主键 | GUID | Y | Y |
| 13 | SOURCE_ID | 缴款单号 | GUID | Y |  |
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
| 42 | DOC_RECEIPT_PAYMENT_ID |  | GUID | Y |  |

### DOC_SALE_PRICE (零售售价维护单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_SALE_PRICE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | OPERATION_CENTER_ID | 营运域 | GUID | Y |  |
| 9 | BEGIN_DATE | 开始日期 | date | Y |  |
| 10 | ADJUST_PRICE_TYPE | 调价类型 | string(40) | Y |  |
| 11 | SHOP_RANGE | 门店范围 | string(40) | Y |  |
| 12 | REMARK | 备注 | string(510) | Y |  |
| 13 | SALE_PRICE_TABLE_ID | 价格表 | GUID | Y |  |
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

### DOC_SALE_PRICE_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | ITEM_ID | 品号 | GUID | Y |  |
| 3 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 4 | ITEM_SPECIFICATION | 规格 | string(80) | Y |  |
| 5 | UNIT_ID | 单位 | GUID | Y |  |
| 6 | PRICE | 售价 | number(23,8) | Y |  |
| 7 | MIN_PRICE | 零售最低价 | number(23,8) | Y |  |
| 8 | MAX_PRICE | 零售最高退货价 | number(23,8) | Y |  |
| 9 | MEMBER_PRICE1 | 会员价1 | number(23,8) | Y |  |
| 10 | MEMBER_PRICE2 | 会员价2 | number(23,8) | Y |  |
| 11 | MEMBER_PRICE3 | 会员价3 | number(23,8) | Y |  |
| 12 | MEMBER_PRICE4 | 会员价4 | number(23,8) | Y |  |
| 13 | MEMBER_PRICE5 | 会员价5 | number(23,8) | Y |  |
| 14 | MEMBER_PRICE6 | 会员价6 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | DOC_SALE_PRICE_D_ID | 主键 | GUID | Y | Y |
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
| 41 | Version | 版本号，不要随意更改 | binary | Y |  |
| 42 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 43 | ApproveDate | 修改日期 | date | Y |  |
| 44 | ApproveBy | 修改人 | GUID | Y |  |
| 45 | DOC_SALE_PRICE_ID |  | GUID | Y |  |

### DOC_SALE_PRICE_SHOP (零售售价维护单门店单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | SHOP_ID | 门店编号 | GUID | Y |  |
| 3 | REMARK | 备注 | string(510) | Y |  |
| 4 | DOC_SALE_PRICE_SHOP_ID | 主键 | GUID | Y | Y |
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
| 30 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 31 | ApproveDate | 修改日期 | date | Y |  |
| 32 | ApproveBy | 修改人 | GUID | Y |  |
| 33 | DOC_SALE_PRICE_ID |  | GUID | Y |  |

### DOC_SHOP_PAYMENT

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | DOC_NO | 单号 | string(40) | Y |  |
| 4 | DOC_DATE | 单据日期 | date | Y |  |
| 5 | DOC_ID | 单据类型 | GUID | Y |  |
| 6 | DOC_SHOP_PAYMENT_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | PAY_DATE | 缴款日期 | date | Y |  |
| 9 | SHOP_ID | 门店 | GUID | Y |  |
| 10 | REMARK | 备注 | string(510) | Y |  |
| 11 | POS_ID | POS机号 | GUID | Y |  |
| 12 | CLASS_ID | 班次 | number | Y |  |
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

### DOC_SHOP_PAYMENT_D

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_SHOP_PAYMENT_D_ID | 主键 | GUID | Y | Y |
| 3 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 4 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 5 | CASH_DRAW_AMT | 钱箱金额 | number(23,8) | Y |  |
| 6 | PAY_AMT | 缴款金额 | number(23,8) | Y |  |
| 7 | REMARK | 备注 | string(510) | Y |  |
| 8 | RECEIPT_EMP | 纳款人 | GUID | Y |  |
| 9 | RECEIPT_STATUS | 纳款状态 | number(0/1) | Y |  |
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
| 35 | DOC_SHOP_PAYMENT_ID |  | GUID | Y |  |

### DOC_SHOP_SALE (门店销售单)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DOC_NO | 单号 | string(40) | Y |  |
| 2 | DOC_DATE | 单据日期 | date | Y |  |
| 3 | DOC_ID | 单据类型 | GUID | Y |  |
| 4 | Owner_Dept | 关联部门 | GUID | Y |  |
| 5 | Owner_Emp | 关联员工 | GUID | Y |  |
| 6 | DOC_SHOP_SALE_ID | 主键 | GUID | Y | Y |
| 7 | CATEGORY | 单据性质 | string(40) | Y |  |
| 8 | QTY |  | number(16,6) | Y |  |
| 9 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 10 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 11 | SALT_TAX | 销项税 | number(23,8) | Y |  |
| 12 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 13 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 14 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 15 | REMARK | 备注 | string(510) | Y |  |
| 16 | SHOP_ID | 门店 | GUID | Y |  |
| 17 | PrintCount | 打印次数 | number | Y |  |
| 18 | EFNETStatus | EF签核码 | string(400) | Y |  |
| 19 | EFNETAction | 签核业务动作 | string(400) | Y |  |
| 20 | EFNETDOCCategory | EFNET单别 | string(400) | Y |  |
| 21 | EFNETDOCNumber | EFNET单号 | string(400) | Y |  |
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

### DOC_SHOP_SALE_D (门店销售单单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_SHOP_SALE_D_ID |  | GUID | Y | Y |
| 3 | MANA_MODE | 经营方式 | string(40) | Y |  |
| 4 | MARKET_RATE | 商场扣率 | number(5,4) | Y |  |
| 5 | ITEM_ID | 商品编码 | GUID | Y |  |
| 6 | ITEM_FEATURE_ID | 特征码 | GUID | Y |  |
| 7 | SUPPLIER_ID | 供应商 | GUID | Y |  |
| 8 | SHOPPE_CONTRACT_ID | 专柜合同 | GUID | Y |  |
| 9 | SHOPPE_MARKET_GOODS_ID | 商场码 | GUID | Y |  |
| 10 | COUNTER_ID | 租柜 | GUID | Y |  |
| 11 | RENTER_ID | 租户 | GUID | Y |  |
| 12 | COUNTRE_RATE | 租柜扣率 | number(5,4) | Y |  |
| 13 | IS_PROMOTION_SALE | 特卖 | number(0/1) | Y |  |
| 14 | COST_TAX_RATE | 进项税率 | number(5,4) | Y |  |
| 15 | SALE_TAX_RATE | 销项税率 | number(5,4) | Y |  |
| 16 | QTY |  | number(16,6) | Y |  |
| 17 | SALE_AMT | 销售额(含税) | number(23,8) | Y |  |
| 18 | SALE_AMT_NOTAX | 销售额(未税) | number(23,8) | Y |  |
| 19 | COUNTER_CONTRACT_ID | 租柜合同 | GUID | Y |  |
| 20 | SALT_TAX | 销项税 | number(23,8) | Y |  |
| 21 | COST_AMT | 销售成本(含税) | number(23,8) | Y |  |
| 22 | COST_AMT_NOTAX | 销售成本(未税) | number(23,8) | Y |  |
| 23 | COST_TAX | 进项税 | number(23,8) | Y |  |
| 24 | PROM_AMT | 优惠额 | number(23,8) | Y |  |
| 25 | PAY_AMT | 收款额 | number(23,8) | Y |  |
| 26 | REMARK | 备注 | string(510) | Y |  |
| 27 | IS_JION_BD | 参与保底 | number(0/1) | Y |  |
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
| 46 | CreateDate | 创建日期 | date | Y |  |
| 47 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 48 | ModifiedDate | 修改日期 | date | Y |  |
| 49 | CreateBy | 创建者 | GUID | Y |  |
| 50 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 51 | ModifiedBy | 修改者 | GUID | Y |  |
| 52 | Version | 版本号，不要随意更改 | binary | Y |  |
| 53 | DOC_SHOP_SALE_ID |  | GUID | Y |  |

### DOC_SHOP_SALE_PAY (门店销售单收款子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_SHOP_SALE_PAY_ID |  | GUID | Y | Y |
| 3 | PAYTYPE | 收款方式分类 | string(40) | Y |  |
| 4 | PAY_AMT | 收款金额 | number(23,8) | Y |  |
| 5 | SALE_PAYTYPE_ID | 收款方式 | GUID | Y |  |
| 6 | CARD_GROUP_ID | 卡类型 | GUID | Y |  |
| 7 | TICKET_GROUP_ID | 券类型 | GUID | Y |  |
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
| 34 | DOC_SHOP_SALE_D_ID |  | GUID | Y |  |

### DOC_SHOP_SALE_PROM (门店销售单促销子单身)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SequenceNumber |  | number | Y |  |
| 2 | DOC_SHOP_SALE_PROM_ID |  | GUID | Y | Y |
| 3 | PROM_AMT | 优惠额 | number(23,8) | Y |  |
| 4 | PROM_TYPE | 优惠方式 | string(40) | Y |  |
| 5 | PROM_ACTIVE_NO | 活动号 | string(80) | Y |  |
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
| 32 | DOC_SHOP_SALE_D_ID |  | GUID | Y |  |