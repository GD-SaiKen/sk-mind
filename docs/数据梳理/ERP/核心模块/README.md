---
title: "E10 ERP Core - Phase 1"
type: "MOC"
phase: "P0-Core"
tables: 374
modules: 26
tags: [MOC, ERP, E10, Core, P0]
---

# E10 ERP - Phase 1 Core Modules

> [!important] Manufacturing Core Value Chain
> 374 tables from 26 core modules
> Focused on the manufacturing value chain: Item -> Purchase -> Production -> Sales -> Finance

## Core Value Chain

```
ITEM/BOM -> PO/PURCHASE/SUPPLIER -> MO/WORK -> SALES/SHIPPING/CUSTOMER -> AR/AP/GL/COST
                                         |
                                    INSPECTION (Quality)
```

## Modules

### Manufacturing/生产制造

| Module | Tables | Kept | Skipped | CN Filled | Missing CN |
|--------|--------|------|---------|-----------|------------|
| [[ITEM|ITEM (物料商品)]] | 52 | 51 | 1 | 0 | 0 |
| [[MO|MO (制造工单)]] | 41 | 41 | 0 | 2 | 3 |
| [[WORK|WORK (工作中心)]] | 12 | 12 | 0 | 0 | 3 |
| [[BOM|BOM (物料清单)]] | 10 | 10 | 0 | 0 | 1 |
| [[INSPECTION|INSPECTION (检验管理)]] | 7 | 7 | 0 | 0 | 0 |

### Procurement/采购供应

| Module | Tables | Kept | Skipped | CN Filled | Missing CN |
|--------|--------|------|---------|-----------|------------|
| [[PURCHASE|PURCHASE (采购管理)]] | 22 | 22 | 0 | 2 | 3 |
| [[PO|PO (采购订单)]] | 15 | 15 | 0 | 0 | 2 |
| [[SUPPLIER|SUPPLIER (供应商)]] | 7 | 7 | 0 | 0 | 7 |
| [[REQUISITION|REQUISITION (请购管理)]] | 2 | 2 | 0 | 1 | 0 |

### Sales/销售分销

| Module | Tables | Kept | Skipped | CN Filled | Missing CN |
|--------|--------|------|---------|-----------|------------|
| [[CUSTOMER|CUSTOMER (客户管理)]] | 23 | 23 | 0 | 0 | 1 |
| [[SALE|SALE (销售单据)]] | 23 | 23 | 0 | 6 | 5 |
| [[SALES|SALES (销售中心)]] | 23 | 23 | 0 | 1 | 1 |
| [[SHIPPING|SHIPPING (出货指令)]] | 3 | 3 | 0 | 0 | 1 |

### Finance/财务核算

| Module | Tables | Kept | Skipped | CN Filled | Missing CN |
|--------|--------|------|---------|-----------|------------|
| [[AR|AR (应收账款)]] | 22 | 21 | 1 | 0 | 2 |
| [[PAYMENT|PAYMENT (付款管理)]] | 19 | 19 | 0 | 3 | 5 |
| [[COST|COST (成本核算)]] | 17 | 17 | 0 | 2 | 4 |
| [[AP|AP (应付账款)]] | 15 | 14 | 1 | 2 | 1 |
| [[TAX|TAX (税务管理)]] | 12 | 12 | 0 | 0 | 0 |
| [[ACCOUNT|ACCOUNT (会计科目)]] | 10 | 10 | 0 | 1 | 0 |
| [[BUDGET|BUDGET (预算管理)]] | 8 | 8 | 0 | 1 | 0 |
| [[CASHFLOW|CASHFLOW (现金流量)]] | 8 | 7 | 1 | 1 | 0 |
| [[BANK|BANK (银行管理)]] | 8 | 7 | 1 | 2 | 0 |
| [[INV|INV (库存成本)]] | 8 | 7 | 1 | 0 | 0 |
| [[JOURNAL|JOURNAL (日记账)]] | 5 | 5 | 0 | 0 | 1 |
| [[VOUCHER|VOUCHER (凭证管理)]] | 4 | 4 | 0 | 0 | 1 |
| [[GL|GL (总账)]] | 4 | 4 | 0 | 0 | 0 |

## Next Steps

- [ ] Review filtered tables: verify no critical tables were removed
- [ ] Fill remaining missing Chinese names
- [ ] Map tables to BusinessObjects (semantic model)
- [ ] Identify BusinessGraphEdges between modules
- [ ] Phase 2: Add P1 Support modules as needed

## Reference

- [[../_MOC - E10 ERP Database Navigation|Full Module Index]]
- [[../modules/|All Module Files (modules/ directory)]]
- [Full Schema Document](../E10_Database_Schema.md)