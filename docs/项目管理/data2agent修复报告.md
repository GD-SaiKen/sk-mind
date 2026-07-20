# data2agent v0.1.8 部署修复完整报告

**环境**：data2agent portable v0.1.8  
**拓扑**：上游 SQL Server `192.168.33.199:1433/Zaitestlist` → 中间机 `192.168.33.185:8851` → 下游平台 `192.168.33.186:8850`  
**日期**：2026-07-17

---

## 一、初始状态

| 组件 | 原始状态 | 现象 |
|------|---------|------|
| 中间机 测试连接 | ❌ 500 | 点"测试连接"就报错 |
| 中间机 触发同步 | ❌ 500 | 点"触发同步"就报错 |
| 下游 ingest | ❌ 异常 | 三个核心服务全红 |
| 下游 mcp | ❌ 异常 | |
| 下游 apply | ❌ 异常 | |
| 下游 console | ✅ 正常 | |
| 对象物化 | 全部"未物化" | 一条业务数据都查不到 |

---

## 二、问题链路（按发现顺序）

问题不是孤立 bug，而是**层层叠加**的连锁反应：修完一层暴露下一层。共涉及 **两个节点、13 处修改**。

---

### 阶段 A：中间机（数据推送侧）

#### A1. quotation.yaml 的 `status: disabled` 不被 Pydantic 接受

**现象**：`POST /api/test-connection` → `500 Internal Server Error`，响应体为空。

**直接跑 Python 复现**：
```
TemplateLoadError: quotation.yaml: bindings.1.status
  Input should be 'draft' or 'verified' [type=literal_error, input_value='disabled']
```

**根因**：`quotation.yaml` 第 45 行 e10 源绑定标记了 `status: disabled`（因为 Zaitestlist 没 QUOTATION 表），但 `metamodel/schema.py` 第 84 行的 Pydantic Literal 只允许 `"draft" | "verified"`。`load_pack()` 的异常发生在 `/api/test-connection` 的 try/except 之外，未被捕获 → 500。

**修复**（2 处）：

| 文件 | 位置 | 改动 |
|------|------|------|
| `metamodel/schema.py` | L84 | `Literal["draft","verified"]` → `Literal["draft","verified","disabled"]` |
| `connect/sync.py` | L18 | `whitelist_from_pack` 增加 `b.status != "disabled"` 过滤条件 |

> **不改会怎样**：所有调用 `load_pack()` 的接口（测试连接、触发同步）全部 500。

---

#### A2. 无主键表走 keyset 增量分页崩溃

**现象**：A1 修完后，`POST /api/actions/trigger` 又 500。

**直接跑 run_sync_cycle 复现**：
```
NotImplementedError: CUSTOMER: keyset 增量只支持单列主键, got []
```

**根因**：Zaitestlist 的 4 张表（CUSTOMER、ITEM、SALES_ORDER_DOC、SALES_ORDER_DOC_D）没有形式化主键约束。`adapter.table_info()` 查询 `INFORMATION_SCHEMA.TABLE_CONSTRAINTS` 返回空 → `pk=[]`。水位增量路径 `_keyset_read` 要求 `len(table.pk) == 1`，拿到空列表抛异常。

**修复**（1 处）：

| 文件 | 位置 | 改动 |
|------|------|------|
| `connect/adapters/base.py` | L122, L130 | `read_increment` 和 `read_segment`：当 `len(table.pk) != 1` 时回落 `_read_full`（OFFSET/FETCH 分页） |

> **不改会怎样**：无主键表根本无法读取，同步永远启动不了。

---

#### A3. 下游拒绝空主键（HTTP 422）

**现象**：A2 修完后同步能读数据了，但下游 `192.168.33.186:8850` 返回：
```json
{"detail": "CUSTOMER: 缺少主键,无法幂等写入"}
```

**根因**：数据库无 PK 约束 → 中间机推给平台的 raw 批次里 `"pk": []`（空数组）。下游的 `/ingest/batch` 端点强制校验 `if not body.pk` → 422。

模板的 `key_map` 明明声明了业务键：
```yaml
Customer:  key_map: { customer_code: CUSTOMER.CUSTOMER_CODE }   → PK = CUSTOMER_CODE
Material:  key_map: { item_code: ITEM.ITEM_CODE }               → PK = ITEM_CODE
SalesOrder: key_map: { order_no: SALES_ORDER_DOC.DOC_NO }       → PK = DOC_NO
SalesOrderLine: key_map: { line_no: SALES_ORDER_DOC_D.SequenceNumber } → PK = SequenceNumber
```

**修复**（3 处）：

| 文件 | 位置 | 改动 |
|------|------|------|
| `connect/sync.py` | 新增 | `pk_hints_from_pack(pack, source)` 函数：从所有 binding 的 `key_map` 推导各表的逻辑主键列 |
| `connect/adapters/mssql.py` | L29, L46 | `__init__` 接受 `pk_hints` 参数；`table_info` 当 INFORMATION_SCHEMA 查不到 PK 时用 hints 兜底 |
| `connect/scheduler.py` | L31 | `build_adapter` 中调用 `pk_hints_from_pack` 并传入适配器 |

> **不改会怎样**：下游平台永远拒绝所有数据批次，数据推不进去。

---

#### A4. 同步异常响应不可读

**现象**：网络波动或下游异常时，trigger 返回 500 空响应。

**根因**：`trigger_action` 没有 try/except，`run_sync_cycle` 抛出的异常直接变成 FastAPI 500。

**修复**（1 处）：

| 文件 | 位置 | 改动 |
|------|------|------|
| `middle_admin/app.py` | L368 | `trigger_action` 包裹 try/except，异常时返回 `{ok: false, error: ..., detail: ...}` |

> **不改会怎样**：任何同步异常都显示为不可读的 500 空响应，无法定位问题。

---

### 阶段 B：下游平台（数据接收与物化侧）

用户在 `192.168.33.186` 上运行 portable-platform，进行后续排查和修复。

---

#### B1. 模板 `status: disabled` 未被识别 → 服务全挂

同 A1。平台侧同样因为 `quotation.yaml` 中 `status: disabled` 导致 `load_pack` 崩溃。平台启动时加载模板 → 抛异常 → ingest / mcp / apply 三个服务全部报"异常"。

**修复**：同 A1 的两处修改，同步到平台 data2agent 包目录。

---

#### B2. raw 表不存在时 apply 抛 500

**现象**：raw 表还没被 ingest 写入时，apply 直接 `OperationalError` → 500。

**根因**：缺少防御性检查。

**修复**：

| 文件 | 位置 | 改动 |
|------|------|------|
| `connect/mapping_apply.py` | L82-100 | `apply_object` 开头增加 raw 表存在性检查，不存在时返回 `skipped` 而非崩溃 |

---

#### B3. 源名不匹配：ingest 用 `e10`，模板写 `digiwin_e10`

**现象**：ingest 写的是 `raw_e10__CUSTOMER`，apply 去查 `raw_digiwin_e10__CUSTOMER` → 找不到表 → 全部跳过。

**根因**：`connect.yaml` 中 source name 是 `e10`，模板 binding 里写的是 `digiwin_e10`。

**修复**：

| 文件 | 位置 | 改动 |
|------|------|------|
| `connect/mapping_apply.py` | L78-98 | 源名自动适配：检测 digiwin_ 前缀 + raw 表前缀自检 |

---

#### B4. apply 探针误报

**现象**：面板上 apply 永远显示"异常"，但实际功能正常。

**根因**：下游平台 apply 没有独立进程，通过 API 按需触发，探针只检查进程 → 误报。

**修复**：

| 文件 | 位置 | 改动 |
|------|------|------|
| `middle_admin/app.py` | L494-497 | 探针逻辑：pack 已加载也算"正常 · api" |

---

#### B5. 模板列名与数据库列名不匹配

**现象**：Material 有 69,710 行 raw 数据但物化一直失败。

**根因**：模板 `material.yaml` 的 `field_map` 引用了 `CATEGORY_CODE`，raw 表里没有这一列。`build_select` 生成 SQL 包含不存在的列 → `OperationalError` → 整个对象物化失败。

**修复**：

| 文件 | 位置 | 改动 |
|------|------|------|
| `connect/mapping_apply.py` | L104-133 | `apply_object` 增加 while True 重试逻辑：遇到 `no such column` 错误时自动剔除该列并重新生成 SQL，只记录隔离日志而不中止整个对象 |

---

#### B6. JOIN 硬编码 `Id` 列名

**现象**：有 JOIN 的对象（SalesOrder、SalesOrderLine）物化全部失败。

**根因**：`mapping.py` 的 `build_select` 函数第 120 行：
```python
f' LEFT JOIN "{physical(t)}" {alias} ON {alias}."Id" = a."{fk}"'
```
硬编码了 `"Id"` 作为被关联表的主键列。但 Zaitestlist 的表没有 `Id` 列——它们用的是业务编码。

**对比**：
```sql
-- 改前（错误）：CUSTOMER 表没有 Id 列
LEFT JOIN "raw_e10__CUSTOMER" j1 ON j1."Id" = a."CUSTOMER_ID"

-- 改后（正确）：用 CUSTOMER_CODE
LEFT JOIN "raw_e10__CUSTOMER" j1 ON j1."CUSTOMER_CODE" = a."CUSTOMER_ID"
```

**修复**（2 处）：

| 文件 | 位置 | 改动 |
|------|------|------|
| `mapping.py` | L66, L120-122 | `build_select` 新增 `table_pk` 参数；JOIN ON 从硬编码 `"Id"` 改为 `_pk_map.get(t, "Id")` |
| `connect/mapping_apply.py` | L77-78, L244-263 | `apply_object` 和 `apply_objects` 构建 `table_pk` 字典（从所有对象 binding 的 key_map 推导），传入 `build_select` |

---

#### B7. derived 决策表引用不存在的列

**现象**：SalesOrder 物化失败——JOIN 修了还是报错。

**根因**：`sales_order.yaml` 的 `derived` 决策表引用了 `APPROVE_DATE`、`ApproveDate` 等列，raw 表里列名实际是 `ApproveStatus`、`LastModifiedDate` 等。B5 的重试逻辑只处理 field_map，没处理 derived 的 when 条件列。

**修复**：

| 文件 | 位置 | 改动 |
|------|------|------|
| `connect/mapping_apply.py` | L135-149 | 缺列重试逻辑扩展：同时处理 derived 规则中 when 条件引用的列 |

---

#### B8. 模板表名与数据库实际表名不匹配

**现象**：Customer 和 SalesOrder 物化仍然失败。

**根因**：
- `customer.yaml`：引用不存在的表（`CURRENCY`）
- `sales_order.yaml`：表名写 `SALES_ORDER`，实际是 `SALES_ORDER_DOC`
- `sales_order_line.yaml`：表名写 `SALES_ORDER_D`，实际是 `SALES_ORDER_DOC_D`

**修复**（3 个模板文件）：

| 文件 | 改动 |
|------|------|
| `app/templates/objects/customer.yaml` | tables 移除 `CURRENCY`，剔除 `currency` 字段，修正 notes |
| `app/templates/objects/sales_order.yaml` | `SALES_ORDER` → `SALES_ORDER_DOC`，移除不存在的列，删除 derived |
| `app/templates/objects/sales_order_line.yaml` | `SALES_ORDER_D` → `SALES_ORDER_DOC_D`，`SALES_ORDER` → `SALES_ORDER_DOC` |

---

#### B9. FK 存 UUID，PK 是业务编码 —— JOIN 语义不对

**现象**：SalesOrder 和 SalesOrderLine 物化后 0 行数据。

**根因**：这是最深的一层问题——不是代码 bug，而是**数据模型不匹配**。模板设计假设"FK = 业务编码"，但 Zaitestlist 实际数据是：

```
CUSTOMER.CUSTOMER_CODE = "ABRA098"          (业务编码)
SALES_ORDER_DOC.CUSTOMER_ID = UUID(...)      (GUID，不是业务编码！)
```

即使 JOIN 列名正确（`j1."CUSTOMER_CODE" = a."CUSTOMER_ID"`），UUID 也不可能等于业务编码 → JOIN 永远 0 行匹配。

**修复**（2 个模板文件）：

| 文件 | 改动 |
|------|------|
| `app/templates/objects/sales_order.yaml` | 改为单表映射：去掉所有 JOIN，只用 `SALES_ORDER_DOC` 自有列 |
| `app/templates/objects/sales_order_line.yaml` | 改为单表映射：只映射 `SALES_ORDER_DOC_D` 自有列，key 用 `SALES_ORDER_DOC_ID` + `SequenceNumber` |

> ⚠️ **这是一个权衡性的临时方案，不是最终态。** 见下方 [已知局限](#七已知局限待后续处理)。

---

### B9 补充：哪些可以恢复、哪些不能

单表映射后，实际损失分析（基于真实 DDL）：

**SalesOrder — 可恢复**：
- `state`（订单状态派生）：`ApproveStatus`、`CLOSE` 列**都在 SALES_ORDER_DOC 本表**，derived 决策表可以加回来

**SalesOrder — 无法恢复（JOIN 依赖）**：
- `customer`（客户名）：FK `CUSTOMER_ID` 存 UUID，CUSTOMER 表 PK 是 `CUSTOMER_CODE`（业务编码），跨表 JOIN 语义不成立

**SalesOrderLine — 无法恢复（JOIN 依赖）**：
- `order_no`：FK `SALES_ORDER_DOC_ID` 存 UUID，SALES_ORDER_DOC 表 PK 是 `DOC_NO`
- `material`：FK `ITEM_ID` 存 UUID，ITEM 表 PK 是 `ITEM_CODE`

---

## 三、修改文件全量清单

### 代码文件（Python）

| # | 文件（相对 data2agent 包目录） | 改动点 | 所在节点 |
|---|------------------------------|--------|---------|
| 1 | `metamodel/schema.py:84` | Literal 加 `"disabled"` | **双端** |
| 2 | `connect/sync.py:18` | whitelist 过滤 disabled | **双端** |
| 3 | `connect/sync.py` 新增 | `pk_hints_from_pack()` | 中间机 |
| 4 | `connect/adapters/base.py:122,130` | 无 PK 回落 `_read_full` | 中间机 |
| 5 | `connect/adapters/mssql.py:29,46` | 接受 pk_hints，table_info 兜底 | 中间机 |
| 6 | `connect/scheduler.py:31` | build_adapter 传入 pk_hints | 中间机 |
| 7 | `middle_admin/app.py:368` | trigger 加 try/except | 中间机 |
| 8 | `middle_admin/app.py:494-497` | apply 探针修正 | 下游 |
| 9 | `mapping.py:66,120-122` | build_select 加 table_pk 参数 | **双端** |
| 10 | `connect/mapping_apply.py:78-263` | apply_object/apply_objects 多处：raw 表检查、缺列重试、derived 列重试、table_pk 传递、源名适配 | **双端** |

### 模板文件（YAML）

| # | 文件 | 改动 |
|---|------|------|
| 11 | `app/templates/objects/customer.yaml` | 去掉 CURRENCY 表和 currency 字段 |
| 12 | `app/templates/objects/sales_order.yaml` | 改为单表映射，去掉 JOIN 和 derived |
| 13 | `app/templates/objects/sales_order_line.yaml` | 改为单表映射，去掉 JOIN |

---

## 四、修复前后对比

| 维度 | 修复前 | 修复后 |
|------|--------|--------|
| **下游服务状态** | ingest/mcp/apply 全异常 | 全部正常 |
| **中间机 测试连接** | 500 空响应 | 返回 4 张表连通详情 |
| **中间机 触发同步** | 500 空响应 | 正常推送 raw 数据到平台 |
| **Customer** | 未物化 | **1,060 行** |
| **Material** | 未物化 | **69,710 行** |
| **SalesOrder** | 未物化 | **8,317 行**（单表映射） |
| **SalesOrderLine** | 未物化 | **393 行**（待中间机补推全量） |
| **模板映射策略** | 多表 JOIN + derived 决策表 | 纯单表直接映射 ⚠️ 已知局限，见第七章 |
| **容错能力** | 一个缺列 → 全部 500 | 缺列自动跳过，单对象失败不阻塞其他 |
| **PK 来源** | 仅依赖数据库约束 | 数据库约束 → key_map 推导 双路径 |
| **JOIN 目标列** | 硬编码 `"Id"` | 从 key_map 推导实际业务键 |

---

## 五、核心矛盾

**展厅模板假设 vs 真实 ERP schema**：

| 假设 | 实际 |
|------|------|
| 表有主键约束 | Zaitestlist 4 张表全无 PK |
| PK 叫 `Id` | 业务编码（`CUSTOMER_CODE`、`DOC_NO` 等） |
| FK 存业务编码 | FK 存 UUID（GUID） |
| 列名与模板一致 | `CATEGORY_CODE`、`APPROVE_DATE` 等列不存在 |
| 表名与模板一致 | `SALES_ORDER` vs `SALES_ORDER_DOC` |
| 可以跨表 JOIN | FK=UUID vs PK=业务编码 → JOIN 永远 0 行 |

这些不是代码 bug，而是**模板需要针对真实数据库定制**。模板本质是"理想 schema"的蓝图，实际部署时必须按真实 DDL 调整。

---

## 六、还需要做的

1. **中间机重启** `data2agent.exe` 使 A 阶段所有修改生效
2. **补推 SalesOrderLine 全量**：当前下游只有 393 行，缺 60,236 行（可能是之前部分批次推送失败导致）
3. **Customer 的 region/currency/payment_days/contact**：当前用 UDF 占位列，需现场确认实际列映射后修正模板重新 apply

---

## 七、已知局限（待后续处理）

以下问题已通过"单表映射"绕过，但不是最终方案：

### 7.1 SalesOrder 缺失字段

| 字段 | 原因 | 可恢复？ |
|------|------|---------|
| `state`（订单状态） | derived 决策表被移除 | ✅ 可恢复 — `ApproveStatus`/`CLOSE` 是本表列，重写 derived 规则即可 |
| `customer`（客户名） | JOIN CUSTOMER 失败 | ❌ FK=UUID ≠ PK=业务编码，需数据层修复或应用层关联 |

### 7.2 SalesOrderLine 缺失字段

| 字段 | 原因 | 可恢复？ |
|------|------|---------|
| `order_no`（订单号） | JOIN SALES_ORDER_DOC 失败 | ❌ 同上 |
| `material`（品号） | JOIN ITEM 失败 | ❌ 同上 |

### 7.3 Customer 缺失字段

| 字段 | 原因 | 可恢复？ |
|------|------|---------|
| `currency`（币别） | JOIN CURRENCY 失败 | ❌ Zaitestlist 无 CURRENCY 表 |
| `region`/`payment_days`/`contact` | UDF 占位列 | ✅ 确认实际列映射后可直接改 field_map |

### 7.4 根本矛盾

FK 存 UUID、PK 是业务编码——这不是字段映射问题，是 **ERP 数据模型与模板假设的根本差异**。要恢复跨表 JOIN 需从以下方向之一解决：

- **数据层**：在 SQL Server 上建视图，把 UUID FK 转换为业务编码
- **模板层**：给 Zaitestlist 定制一套纯单表的模板，放弃跨表语义
- **应用层**：通过 MCP 分两次查询，应用代码自己关联
