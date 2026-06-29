---
module: "PARAM"
name_zh: "参数设置"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 2
columns: 101
category: module
tags: ["ERP", "E10"]
created: 2026-06-25 10:52
---

# PARAM (参数设置)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 2 | Columns: 101

## Related Modules

- [[ABTABAC (表格映射)|ABTABAC (表格映射)]]
- [[ABTABVC (表格方案)|ABTABVC (表格方案)]]
- [[ACCCODE (科目数据集)|ACCCODE (科目数据集)]]
- [[ACCESS (权限控制)|ACCESS (权限控制)]]
- [[ACCPERIOD (会计期间)|ACCPERIOD (会计期间)]]
- [[ALTER (变更)|ALTER (变更)]]
- [[AM (资产报表)|AM (资产报表)]]
- [[AU (辅助特性)|AU (辅助特性)]]

---

## Tables


- **PARAM_CARD_READER**
- **PARAM_MEMBER_MASTER_SLAVE**


---


---


> Tables: 2

### PARAM_CARD_READER

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARAM_CARD_READER_ID | 主键 | GUID | Y | Y |
| 4 | CARD_READER_TYPE | 读卡器硬件型号 | string(40) | Y |  |
| 5 | CARD_READER_PORT_TYPE | 读卡器端口 | string(40) | Y |  |
| 6 | BAUD_RATE | 波特率 | string(40) | Y |  |
| 7 | ENCRYPT_STRING | 卡加密串 | string(100) | Y |  |
| 8 | ENCRYPT_KEY | 系统加密密钥 | string(100) | Y |  |
| 9 | REMARK | 备注 | string(510) | Y |  |
| 10 | CARD_READER_PORT | 读卡器端口号 | number | Y |  |
| 11 | IC_CARD_READER_TYPE | IC卡读卡器类型 | string(40) | Y |  |
| 12 | IC_CARD_TYPE | IC卡类型 | string(400) | Y |  |
| 13 | IC_CARD_READER_PORT_TYPE | IC读卡器端口 | string(400) | Y |  |
| 14 | IC_BAUD_RATE | IC波特率 | string(40) | Y |  |
| 15 | IC_ENCRYPT_STRING | IC卡加密串 | string(400) | Y |  |
| 16 | IC_ENCRYPT_KEY1 | IC卡私钥1 | string(400) | Y |  |
| 17 | IC_ENCRYPT_KEY2 | IC卡私钥2 | string(400) | Y |  |
| 18 | IC_ENCRYPT_KEY3 | IC卡私钥3 | string(400) | Y |  |
| 19 | IC_BASE_SECTOR | 基础信息扇区 | number | Y |  |
| 20 | IC_CARDNO_SECTOR | 卡号扇区 | number | Y |  |
| 21 | IC_CHANGE_SECTOR | 异动扇区 | number | Y |  |
| 22 | IC_CARD_LOG | 记录日志 | number(0/1) | Y |  |
| 23 | IC_KEY1 | 密钥1 | string(24) | Y |  |
| 24 | IC_KEY2 | 密钥2 | string(24) | Y |  |
| 25 | IC_KEY3 | 密钥3 | string(24) | Y |  |
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

### PARAM_MEMBER_MASTER_SLAVE

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Owner_Dept | 关联部门 | GUID | Y |  |
| 2 | Owner_Emp | 关联员工 | GUID | Y |  |
| 3 | PARAM_MEMBER_MASTER_SLAVE_ID | 主键 | GUID | Y | Y |
| 4 | POINT_FUNCTION | 积分方法 | string(40) | Y |  |
| 5 | SLAVE_MEMBER_POINT_FOUNDATION | 子会员积分策略依据 | string(40) | Y |  |
| 6 | UPGRADE_OPTION | 升级设置 | string(40) | Y |  |
| 7 | SLAVE_MEMBER_CHARGE_FOUNDATION | 子会员充值策略依据 | string(40) | Y |  |
| 8 | PRICE_FOUNDATION | 取价原则 | string(40) | Y |  |
| 9 | SLAVE_PRESENT_MASTER | 子会员积分时额外赠送主会员积分 | number(0/1) | Y |  |
| 10 | SLAVE_POINTS | 子会员积分额 | number(16,4) | Y |  |
| 11 | MASTER_POINTS | 主会员积分赠送额 | number(16,4) | Y |  |
| 12 | MASTER_PRESENT_POINTS | 主会员固定加赠积分额 | number(16,4) | Y |  |
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