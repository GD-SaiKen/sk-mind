---
tags: [技术设计, 语义建模, MES]
---

# sk-mind MES 语义建模设计方案

## 一、原则

**d2a 做对的，我们照搬；实现方式，我们适配 sk-mind。**

d2a（data2agent）是技术顾问已验证跑通的项目。它的核心价值在于：
- YAML 格式的业务对象/指标定义（LLM 友好、可维护）
- `query_objects` / `query_metrics` 两个 MCP 工具的参数和返回格式
- object → SQL / metric → SQL 的翻译思路

这些我们直接保留。但是 d2a 是一个独立可执行文件（`data2agent.exe` + 内嵌 SQLite），而 sk-mind 是一个完整的 FastAPI + PostgreSQL + Redis/RQ 数据平台——实现手段要跟着 sk-mind 走。

---

## 二、对标 d2a：哪些照搬，哪些适配

### 2.1 YAML 格式 — 照搬

| d2a 字段 | 是否保留 | 说明 |
|----------|---------|------|
| Business Object YAML | ✅ 完整照搬 | `object` / `display_name` / `description` / `domain` / `source_of_truth` / `keys` / `properties` / `bindings` |
| Metrics YAML | ✅ 完整照搬 | `metric` / `display_name` / `formula` / `grain` / `dimensions` / `caveats` / `status` / `description` / `freshness_sla` |
| MCP 工具参数签名 | ✅ 照搬（适配） | `query_objects(object, filters, order_by, limit)` + `query_metrics(metric, group_by, dimensions, filters, limit)`；排序方向含在 `order_by` 字符串中（如 `"event_time desc"`），不再单独传 `desc` 参数 |
| catalog.yaml 总索引 | ✅ 照搬 | 我们叫 catalog.yaml 而不是 pack.yaml |

### 2.2 实现方式 — 适配 sk-mind

| d2a 怎么做的 | sk-mind 怎么做 | 原因 |
|---|---|---|
| 独立进程 `data2agent.exe` | sk-mind FastAPI 进程中新增 `app/modules/agent/` 模块，路由 `/api/agent/*` | sk-mind 已有完整的 FastAPI + auth/CORS/生命周期，不需要另起进程 |
| 内嵌 SQLite | 复用 sk-mind 现有的 PostgreSQL async engine | sk-mind 数据本来就在 PostgreSQL 里，直接用 |
| `app/templates/objects/*.yaml` | `backend/config/semantic/mes/objects/*.yaml` | sk-mind 按 source 分目录，MES 系统放 `mes/` 下；配置统一放 `config/` 下 |
| 硬编码 SQL 生成器 | `app/modules/semantic/` 模块：loader.py（读 YAML）+ mapper.py（翻译 SQL） | sk-mind 用模块化三层架构（router/service/dao），语义引擎放单独模块 |
| `propose_action` 建议卡 | v3 再做 | MES v1 不需要 |
| 独立的 materializer ETL | 不做——sk-mind 已有 Alembic migration + `serving.*` PostgreSQL VIEW | Serving 视图通过 Alembic 迁移管理，数据实时从 raw 计算 |

### 2.3 MES 特有补充（d2a 没有的）

| 场景 | 我们怎么做 |
|------|-----------|
| 波浪号全半角统一（`～`→`~`） | serving 视图层做 `REPLACE(machine_no, '～', '~')` |
| Java 毫秒时间戳 | serving 视图层做 `to_timestamp(col / 1000.0) AT TIME ZONE 'Asia/Shanghai'` |
| 多时间格式混用（毫秒 vs 字符串） | serving 视图按来源表逐个适配 |
| 车间代码→中文名 | serving 视图层做 `CASE WHEN` 映射 |
| 脏字段过滤 | serving 视图不 SELECT 已知不可用字段 |
| 班次推断 | serving 视图层做 `CASE WHEN EXTRACT(HOUR FROM ...) BETWEEN 8 AND 19 THEN '白班'` |

这些都在 serving 视图层解决，语义模型 YAML 只看到干净数据。

---

## 三、sk-mind 集成架构

### 3.1 在已有系统中新增的模块

```
sk-mind/backend/
├── config/
│   ├── data_sources/
│   │   └── MES.yaml                    # 已有，25个API接口配置
│   └── semantic/                       # ★ 新增（按数据源分层）
│       ├── mes/                        # MES 系统（v1 交付）
│       │   ├── objects/
│       │   │   ├── andon_event.yaml
│       │   │   ├── error_report.yaml
│       │   │   ├── oee_record.yaml
│       │   │   ├── production_report.yaml
│       │   │   ├── work_order.yaml
│       │   │   ├── schedule_task.yaml
│       │   │   ├── machine_dim.yaml
│       │   │   └── craft_hours.yaml
│       │   ├── metrics/
│       │   │   ├── andon_metrics.yaml
│       │   │   ├── oee_metrics.yaml
│       │   │   └── production_metrics.yaml
│       │   └── catalog.yaml           # MES 系统内总索引
│       ├── erp/                        # ERP 系统（未来扩展）
│       └── global_catalog.yaml        # 跨系统总索引（未来）
├── app/
│   ├── api/
│   │   └── __init__.py                # 修改：注册 agent_router
│   └── modules/
│       ├── semantic/                   # ★ 新增/填充（stub 已存在）
│       │   ├── __init__.py
│       │   ├── loader.py              # 从 config/semantic/ 加载 YAML
│       │   ├── mapper.py              # YAML → SQL 翻译引擎
│       │   └── schemas.py             # Pydantic 模型
│       └── agent/                      # ★ 新增/填充（stub 已存在）
│           ├── __init__.py
│           ├── router.py              # /api/agent/* 路由
│           ├── tools/
│           │   ├── __init__.py
│           │   ├── query_objects.py   # query_objects 工具实现
│           │   ├── query_metrics.py   # query_metrics 工具实现
│           │   └── get_catalog.py     # get_catalog 工具实现
│           └── schemas.py             # 请求/响应 Pydantic 模型
└── alembic/
    └── versions/
        └── 019_serving_views.py       # ★ 新增：Serving 视图迁移
```

### 3.2 数据流

```
┌──────────────────────────────────────────────────────────┐
│  sk-mind FastAPI 进程                                     │
│                                                           │
│  mes-agent ──HTTP POST──→ /api/agent/query_objects        │
│                              │  {source: "mes",             │
│                              │   object: "AndonEvent",      │
│                              │   filters: {...}}             │
│                              │                             │
│                              ├─ 读取 config/semantic/mes/   │
│                              │  objects/andon_event.yaml   │
│                              │                             │
│                              ├─ YAML → SQL 翻译             │
│                              │  mapper.translate()         │
│                              │                             │
│                              ├─ asyncpg 执行 SQL            │
│                              │  SELECT FROM serving.*      │
│                              │                             │
│                              └─ 返回 JSON                  │
│                              │                             │
│  已有系统组件（不做改动）：                                 │
│  - JWT Auth (get_current_user)                             │
│  - CORS                                                    │
│  - async_session_factory                                   │
│  - settings / config                                       │
│  - 生命周期管理 (app/main.py)                               │
└──────────────────────────────────────────────────────────┘
```

### 3.3 路由注册方式

`app/api/__init__.py` 中新增一行：

```python
from app.modules.agent.router import router as agent_router

router.include_router(agent_router)
```

与现有模块完全一致的注册模式。

---

## 四、Serving 视图（Alembic 迁移）

### 4.1 为什么不写 ad-hoc SQL

sk-mind 已有 18 个 Alembic 迁移版本，有标准化的 `alembic upgrade head` 流程。Serving 视图必须是迁移脚本，有以下好处：

- 版本化管理：`alembic history` 能看到视图创建历史
- 环境一致性：`alembic upgrade head` 一键建出所有视图
- 可回滚：`alembic downgrade -1` 删除视图
- Docker 启动自动执行：`docker-compose up` 时 entrypoint 会跑 migration

### 4.2 接入范围：14 个核心接口 → 8 个视图

从 MES.yaml 的 25 个接口中，选 14 个 v1 阶段需要的接口：

| 域 | 涉及接口 | raw 表 | 用途 |
|----|---------|--------|------|
| 安灯 | andonApiController | raw.mes_andon_api_controller | 安灯事件数据 |
| 异常 | selectErrorReport | raw.mes_select_error_report | 设备异常上报 |
| OEE | selectOeeReport | raw.mes_select_oee_report | OEE/三色灯效率 |
| OEE | getTrilightEfficiencyOneDay | raw.mes_get_trilight_efficiency_one_day | 单日三色灯 |
| OEE | getTrilightEfficiencyDurationTime | raw.mes_get_trilight_efficiency_duration_time | 三色灯时长 |
| OEE | getTrilightSummaryDurationTime | raw.mes_get_trilight_summary_duration_time | 三色灯汇总 |

> **OEE 4 表合并策略**：`selectOeeReport`（按天汇总）提供基础 OEE 指标，其他三张表（单日三色灯、时长、汇总）数据粒度不同（小时/天/月），不适合直接 JOIN。**v1 策略**：以 `selectOeeReport` 为主表（按天+机台粒度），LEFT JOIN `machine_dim` 补充车间信息，三色灯数据单独聚合后按 `(machine_id, report_date)` JOIN。如果三色灯数据缺失导致 JOIN 失败，对应行用 NULL 填充。
| 报工 | selectWorkorderTaskActionStatistics | raw.mes_select_workorder_task_action_statistics | 生产报工 |
| 报工 | selectProceduresReportDataByTime | raw.mes_select_procedures_report_data_by_time | 工序报工 |
| 工单 | filterWorkorder | raw.mes_filter_workorder | 工单查询 |
| 排产 | selectProductionBackParamsByTime | raw.mes_select_production_back_params_by_time | 工序排产 |
| 标准工时 | queryCraftHours | raw.mes_query_craft_hours | 产品标准工时 |
| 标准工时 | queryCraftHoursDetails | raw.mes_query_craft_hours_details | 标准工时明细 |
| 机台 | getMachineList | raw.mes_get_machine_list | 机台主数据 |
| 机台 | getMachineDetailById | raw.mes_get_machine_detail_by_id | 机台详情 |

对应 8 个 serving 视图：

| # | 视图 | 来源 raw 表 | 业务对象 |
|---|------|-----------|---|
| 1 | serving.andon_v1 | raw.mes_andon_api_controller | AndonEvent |
| 2 | serving.error_report_v1 | raw.mes_select_error_report | ErrorReport |
| 3 | serving.oee_v1 | raw.mes_select_oee_report + JOIN machine_dim | OEERecord |
| 4 | serving.reporting_v1 | raw.mes_select_workorder_task_action_statistics | ProductionReport |
| 5 | serving.workorder_v1 | raw.mes_filter_workorder | WorkOrder |
| 6 | serving.schedule_v1 | raw.mes_select_production_back_params_by_time | ScheduleTask |
| 7 | serving.machine_dim_v1 | raw.mes_get_machine_list | Machine |
| 8 | serving.craft_hours_v1 | raw.mes_query_craft_hours | CraftHours |

### 4.3 迁移脚本结构

`alembic/versions/019_serving_views.py`：

```python
"""Create serving.* views for MES semantic layer.

Revision ID: 019
Revises: 018_add_null_rate_and_agent_unavailable_reason
Create Date: 2026-07-28
"""
from alembic import op

revision = '019'
down_revision = '018'
branch_labels = None
depends_on = None

SERVING_VIEWS = {
    "andon_v1": """
        CREATE OR REPLACE VIEW serving.andon_v1 AS
        SELECT
            ar_id::text AS event_id,
            to_timestamp((trigger_time::bigint) / 1000.0)
                AT TIME ZONE 'Asia/Shanghai' AS event_time,
            -- ... (完整 SELECT 见附录)
        FROM raw.mes_andon_api_controller
        WHERE trigger_time IS NOT NULL
          AND trigger_time ~ E'^\\d+$';
    """,
    "error_report_v1": """...""",
    "oee_v1": """...""",
    # ... 其余视图
}

def upgrade():
    # Alembic 默认在事务中执行 upgrade()，若某个视图创建失败会自动回滚
    op.execute("CREATE SCHEMA IF NOT EXISTS serving")
    for view_name, sql in SERVING_VIEWS.items():
        op.execute(sql)
    # 添加 COMMENT（非关键操作，失败不影响视图可用性）
    for view_name, comment in VIEW_COMMENTS.items():
        op.execute(f"COMMENT ON VIEW serving.{view_name} IS '{comment}'")

def downgrade():
    for view_name in SERVING_VIEWS:
        op.execute(f"DROP VIEW IF EXISTS serving.{view_name}")
```

### 4.4 通用清洗规则（所有视图统一处理）

| 规则 | raw 特征 | serving 处理 |
|------|---------|-------------|
| 时间戳转换 | Java 毫秒 | `to_timestamp(col / 1000.0) AT TIME ZONE 'Asia/Shanghai'` |
| 字符串时间 | `"2026-07-22 00:00:00"` | `(col \|\| '+08')::timestamptz` |
| 波浪号统一 | `～` 混在 `~` 中 | `REPLACE(col, '～', '~')` |
| 车间代码 | `ws01` ~ `ws06` | `CASE WHEN ws01→BC装配 ... END` |
| 安灯类型 | 1/2/3 | `CASE WHEN 1→首件检验` |
| 脏字段过滤 | `processingTimeout` 永远 false | 不 SELECT |
| 理论值标注 | `produceHours` 理论值 | 保留，字段 COMMENT 标注 |
| 班次推断 | 无班次字段 | `CASE WHEN EXTRACT(HOUR FROM ...) BETWEEN 8 AND 19 THEN '白班'` |

### 4.5 每个视图的核心加工

#### serving.andon_v1
- Java 毫秒 → 北京时间（trigger_time / response_time / process_time）
- **时间差计算注意**：raw 表中 `trigger_time` 和 `response_time` 是 Java 毫秒 bigint，在 serving 视图先转为 `timestamptz`：
  ```sql
  to_timestamp(trigger_time::bigint / 1000.0)
      AT TIME ZONE 'Asia/Shanghai' AS event_time,
  to_timestamp(response_time::bigint / 1000.0)
      AT TIME ZONE 'Asia/Shanghai' AS response_time,
  ```
  转为 `timestamptz` 后不再是毫秒值，时间差需要用 `EXTRACT(EPOCH FROM ...)` 计算：
  ```sql
  EXTRACT(EPOCH FROM (
      to_timestamp(response_time::bigint / 1000.0)
      - to_timestamp(trigger_time::bigint / 1000.0)
  )) / 60 AS response_minutes
  ```
- `process_minutes` = 同理用 `EXTRACT(EPOCH FROM ...) / 60`
- `is_timeout` = response_minutes > 15 OR process_minutes > 30
- `shift` = 按 trigger_time 推断白班/夜班
- 机台号波浪号统一

#### serving.error_report_v1
- 字符串时间 → timestamptz
- 车间代码映射
- 灯色枚举映射（1→绿灯, 2→黄灯, 3→红灯）
- 机台号波浪号统一

#### serving.oee_v1

> **4 表合并策略**：参见 4.2 节说明。v1 以 `selectOeeReport` 为主表（按天+机台粒度），三色灯数据先按 `(machine_id, report_date)` 聚合，再 LEFT JOIN 到主表。缺失的三色灯数据用 NULL 填充，指标计算时用 NULLIF 防止除零错误。

- 四灯时长（秒→分钟）
- `green_rate` = green / (green+yellow+red+gray) * 100（灰灯放分母）
- `yellow_rate` / `red_rate`
- `is_low_efficiency` = green_rate < 60%（阈值待最终确认）
- `produce_hours` 保留，COMMENT 标注"理论值"
- LEFT JOIN serving.machine_dim 补充车间信息

#### serving.reporting_v1
- `total_qty` = good_qty + defect_qty
- `yield_rate` = good_qty / total_qty * 100
- `uph` = total_qty / report_hours
- `timeliness` = 班次结束后 30min 内报工为"及时"
- `is_empty` = good_qty=0 AND defect_qty=0
- `shift` = 按报工时间推断

#### serving.workorder_v1
- 状态映射（0→未开工, 1→生产中, 2→已完工...）
- 优先级映射
- `progress_pct` = completed / planned * 100
- `overdue_days` = NOW() - planned_end（仅未完工）
- `is_overdue` = planned_end < NOW() AND status NOT IN (已完工, 已结案)

#### serving.schedule_v1
- `completion_rate` = completed / planned * 100
- `progress_status` = 未开工/进行中/已完工

#### serving.machine_dim_v1
- 机台号波浪号统一
- 车间代码映射

#### serving.craft_hours_v1
- 车间代码映射

> **注意**：完整 SQL 将在实施阶段由 sk-mind 团队根据 raw 表实际 schema 编写，写入 Alembic 迁移的 `SERVING_VIEWS` dict。此处仅列核心加工要点作为规格说明。

---

## 五、语义模型 YAML 定义

### 5.1 文件位置与多数据源分层

所有 YAML 放在 `backend/config/semantic/` 下。按数据源（source）分目录，MES 系统放在 `mes/` 子目录：

```
config/semantic/
├── mes/                        # MES 系统（v1 交付）
│   ├── objects/
│   ├── metrics/
│   └── catalog.yaml
├── erp/                        # ERP 系统（未来扩展，目录已预留）
└── global_catalog.yaml         # 跨系统总索引（未来，列出所有可用 source）
```

这一位置与 sk-mind 已有的 YAML 配置加载模式一致（参考 `data_sources/router.py` 中 `_CONFIG_DIR` 的写法），多了一层 source 目录以适应 sk-mind 不局限于单一数据源的设计。

API 调用时通过 `source` 参数区分：

```
POST /api/agent/query_objects
{ "source": "mes", "object": "AndonEvent", "filters": {...} }

POST /api/agent/query_objects   # 未来
{ "source": "erp", "object": "PurchaseOrder", "filters": {...} }
```

`get_catalog` 同样支持 `?source=mes` 过滤，不传则返回所有系统的汇总。

### 5.2 objects/andon_event.yaml（完整示例）

```yaml
object: AndonEvent
display_name: "安灯事件"
description: "首件检验、调机请求、功能性异常等安灯触发记录。每条记录=一次安灯按钮触发事件"
domain: "生产制造"
source_of_truth: "LightMES andonApiController"
keys: [event_id]
properties:
  - { name: event_id, type: string, desc: "事件唯一标识" }
  - { name: event_time, type: datetime, desc: "事件触发时间 (北京时间)" }
  - { name: response_time, type: datetime, desc: "首次响应时间" }
  - { name: process_time, type: datetime, desc: "处理完成时间" }
  - { name: workshop, type: enum, enum_values: [BC装配, LP装配, SP装配, 注塑, 压铸, 表面处理], desc: "所在车间" }
  - { name: machine_no, type: string, desc: "机台号" }
  - { name: event_type, type: enum, enum_values: [首件检验, 调机请求, 功能性异常, 其他], desc: "安灯类型" }
  - { name: operator_name, type: string, desc: "操作员姓名" }
  - { name: response_minutes, type: decimal, desc: "响应耗时(分钟), 目标<=15min" }
  - { name: process_minutes, type: decimal, desc: "处理总耗时(分钟), 目标<=30min" }
  - { name: is_timeout, type: boolean, desc: "是否超时: 响应>15min 或 总耗时>30min" }
  - { name: shift, type: enum, enum_values: [白班, 夜班], desc: "班次 (按触发时间判定)" }
  - { name: product_code, type: string, desc: "产品编码" }
  - { name: product_name, type: string, desc: "产品名称" }
  - { name: mould_no, type: string, desc: "模具号" }
  - { name: event_status, type: enum, enum_values: [待响应, 处理中, 已完成], desc: "事件当前状态" }
bindings:
  - source: lightmes
    tables: [serving.andon_v1]
    status: draft
    key_map:
      event_id: serving.andon_v1.event_id
    field_map:
      event_id: serving.andon_v1.event_id
      event_time: serving.andon_v1.event_time
      response_time: serving.andon_v1.response_time
      process_time: serving.andon_v1.process_time
      workshop: serving.andon_v1.workshop
      machine_no: serving.andon_v1.machine_no
      event_type: serving.andon_v1.event_type
      operator_name: serving.andon_v1.operator_name
      response_minutes: serving.andon_v1.response_minutes
      process_minutes: serving.andon_v1.process_minutes
      is_timeout: serving.andon_v1.is_timeout
      shift: serving.andon_v1.shift
      product_code: serving.andon_v1.product_code
      product_name: serving.andon_v1.product_name
      mould_no: serving.andon_v1.mould_no
      event_status: serving.andon_v1.event_status
    notes: >
      - 机台号已在 serving 视图做全半角统一
      - 时间已转北京时间
      - is_timeout 按首件双达标规则（响应<=15min AND 总耗时<=30min）判定
```

### 5.3 其他业务对象一览

每个对象都需要完整的 `properties` + `bindings.field_map`，模式与 andon_event.yaml 一致：

| YAML 文件 | object | serving 视图 | keys |
|-----------|--------|-------------|------|
| error_report.yaml | ErrorReport | serving.error_report_v1 | [error_id] |
| oee_record.yaml | OEERecord | serving.oee_v1 | [machine_id, report_date, shift_name] |
| production_report.yaml | ProductionReport | serving.reporting_v1 | [report_id] |
| work_order.yaml | WorkOrder | serving.workorder_v1 | [wo_id] |
| schedule_task.yaml | ScheduleTask | serving.schedule_v1 | [schedule_id] |
| machine_dim.yaml | Machine | serving.machine_dim_v1 | [machine_id] |
| craft_hours.yaml | CraftHours | serving.craft_hours_v1 | [material_id] |

> **扩展点**：如果未来需要跨对象关联查询（如"查某工单关联的报工记录"），可以在 YAML 中新增 `relations` 字段。d2a 的 SalesOrder 有类似设计，但 v1 暂不需要。

### 5.4 指标 YAML 示例（metrics/oee_metrics.yaml）

```yaml
metrics:
  - metric: oee_green_rate
    display_name: "线效(绿灯率)"
    description: "各机台/车间的绿灯时长占比，灰灯放分母计算"
    status: draft
    formula: "SUM(green_minutes) / SUM(green+yellow+red+gray) * 100"
    grain: [日期, 车间, 机台]
    dimensions: [车间, 机台, 班次]
    source_object: OEERecord
    caveats: "灰灯放入分母计算；低效阈值由配置定义"
    freshness_sla: "T+1"

  - metric: oee_yellow_rate
    display_name: "黄灯率"
    description: "黄灯时长占总时长的百分比，灰灯放分母"
    status: draft
    formula: "SUM(yellow_minutes) / SUM(green+yellow+red+gray) * 100"
    grain: [日期, 车间, 机台]
    dimensions: [车间, 机台]
    source_object: OEERecord
    freshness_sla: "T+1"

  - metric: oee_red_rate
    display_name: "红灯率"
    description: "红灯时长占总时长的百分比，灰灯放分母"
    status: draft
    formula: "SUM(red_minutes) / SUM(green+yellow+red+gray) * 100"
    grain: [日期, 车间, 机台]
    dimensions: [车间, 机台]
    source_object: OEERecord
    freshness_sla: "T+1"

  - metric: low_efficiency_count
    display_name: "低效机台数"
    description: "green_rate 低于阈值的机台数量"
    status: draft
    formula: "COUNT(OEERecord WHERE is_low_efficiency=TRUE)"
    grain: [日期, 车间]
    dimensions: [车间]
    source_object: OEERecord
    freshness_sla: "T+1"
```

### 5.5 指标清单一览

| 类别 | metric | 名称 | source_object |
|------|--------|------|---------------|
| 安灯 | andon_response_rate | 安灯响应及时率 | AndonEvent |
| 安灯 | andon_process_rate | 安灯处理及时率 | AndonEvent |
| 安灯 | andon_event_count | 安灯事件数 | AndonEvent |
| 安灯 | andon_timeout_rate | 安灯超时率 | AndonEvent |
| OEE | oee_green_rate | 线效(绿灯率) | OEERecord |
| OEE | oee_yellow_rate | 黄灯率 | OEERecord |
| OEE | oee_red_rate | 红灯率 | OEERecord |
| OEE | low_efficiency_count | 低效机台数 | OEERecord |
| OEE | oee_green_rate_trend | 线效多日趋势 | OEERecord |
| 报工 | total_output_qty | 总产量 | ProductionReport |
| 报工 | yield_rate | 良率 | ProductionReport |
| 报工 | uph | 单位小时产出 | ProductionReport |
| 报工 | reporting_timeliness_rate | 报工及时率 | ProductionReport |
| 报工 | empty_report_count | 空报工数 | ProductionReport |
| 工单 | overdue_order_count | 逾期工单数 | WorkOrder |
| 工单 | urgent_order_count | 紧急工单数 | WorkOrder |
| 工单 | completion_rate | 完工率 | WorkOrder |
| 排产 | scheduled_task_count | 排产任务数 | ScheduleTask |
| 排产 | schedule_completion_rate | 排产完工率 | ScheduleTask |

共 19 个指标，分 3 个 YAML 文件：`andon_metrics.yaml` / `oee_metrics.yaml` / `production_metrics.yaml`。

### 5.6 catalog.yaml（总索引）

```yaml
# config/semantic/mes/catalog.yaml
catalog:
  source: "mes"
  name: "MES 语义模型"
  version: "1.0.0"
  description: "LightMES 制造执行系统的业务对象和指标语义定义"
  objects:
    - name: AndonEvent
      file: objects/andon_event.yaml
      domain: 生产制造
    - name: ErrorReport
      file: objects/error_report.yaml
      domain: 生产制造
    - name: OEERecord
      file: objects/oee_record.yaml
      domain: 生产制造
    - name: ProductionReport
      file: objects/production_report.yaml
      domain: 生产制造
    - name: WorkOrder
      file: objects/work_order.yaml
      domain: 生产制造
    - name: ScheduleTask
      file: objects/schedule_task.yaml
      domain: 生产制造
    - name: Machine
      file: objects/machine_dim.yaml
      domain: 主数据
    - name: CraftHours
      file: objects/craft_hours.yaml
      domain: 主数据
  metrics:
    # 共 19 个指标，分 3 个 YAML 文件
    - name: andon_response_rate
      file: metrics/andon_metrics.yaml
    - name: andon_process_rate
      file: metrics/andon_metrics.yaml
    - name: andon_event_count
      file: metrics/andon_metrics.yaml
    - name: andon_timeout_rate
      file: metrics/andon_metrics.yaml
    - name: oee_green_rate
      file: metrics/oee_metrics.yaml
    - name: oee_yellow_rate
      file: metrics/oee_metrics.yaml
    - name: oee_red_rate
      file: metrics/oee_metrics.yaml
    - name: low_efficiency_count
      file: metrics/oee_metrics.yaml
    - name: oee_green_rate_trend
      file: metrics/oee_metrics.yaml
    - name: total_output_qty
      file: metrics/production_metrics.yaml
    - name: yield_rate
      file: metrics/production_metrics.yaml
    - name: uph
      file: metrics/production_metrics.yaml
    - name: reporting_timeliness_rate
      file: metrics/production_metrics.yaml
    - name: empty_report_count
      file: metrics/production_metrics.yaml
    - name: overdue_order_count
      file: metrics/production_metrics.yaml
    - name: urgent_order_count
      file: metrics/production_metrics.yaml
    - name: completion_rate
      file: metrics/production_metrics.yaml
    - name: schedule_completion_rate
      file: metrics/production_metrics.yaml
    - name: scheduled_task_count
      file: metrics/production_metrics.yaml
```

---

## 六、代码模块设计

### 6.1 app/modules/semantic/（YAML 加载 + SQL 翻译）

这个模块负责：从 `config/semantic/<source>/` 读取 YAML → 解析为 Python 对象 → 翻译成 SQL。

**不需要 ORM 模型**——语义模块不存数据，只在内存中加载 YAML 并翻译查询。

**按 source 分目录**：`config/semantic/mes/`、`config/semantic/erp/` 各有一套独立的 objects/metrics/catalog.yaml，loaded 实例可以按 source 隔离加载。

#### loader.py

```python
"""从 config/semantic/<source>/ 加载 YAML 模板，返回解析后的 Python dict/list。

预加载 + 缓存：首次加载后缓存到内存，避免每次 MCP 请求都读文件。
支持按 source（mes/erp/...）分层加载。
"""

import yaml
import os
from pathlib import Path
from typing import Any
import logging

logger = logging.getLogger(__name__)

# 通过环境变量配置根路径，与 sk-mind 已有 _CONFIG_DIR 模式一致
# 默认值保留工整的后备逻辑：{project_root}/backend/config/semantic/
_ENV_SEMANTIC_DIR = os.getenv("SEMANTIC_CONFIG_DIR")
_SEMANTIC_BASE = (
    Path(_ENV_SEMANTIC_DIR) if _ENV_SEMANTIC_DIR
    else Path(__file__).resolve().parents[3] / "config" / "semantic"
)


class SourceSemanticLoader:
    """按数据源加载并缓存语义模型 YAML 模板。

    缓存策略：首次 load_all() 后记录所有 YAML 文件的 mtime，后续调用时自动检测
    文件变更并触发 revalidate。同时暴露 reload() 方法供内部管理端点调用。
    """

    def __init__(self, source: str = "mes"):
        """
        Args:
            source: 数据源标识，对应 config/semantic/<source>/ 目录
        """
        self._source = source
        self._source_dir = _SEMANTIC_BASE / source
        self._objects: dict[str, dict[str, Any]] = {}
        self._metrics: dict[str, dict[str, Any]] = {}
        self._catalog: dict[str, Any] | None = None
        self._loaded = False
        self._file_mtimes: dict[str, float] = {}  # 文件路径 → 最后修改时间

    def _scan_files(self) -> list[Path]:
        """扫描该 source 下所有 YAML 文件。"""
        files: list[Path] = []
        for subdir in ("objects", "metrics"):
            d = self._source_dir / subdir
            if d.is_dir():
                files.extend(d.glob("*.yaml"))
        cf = self._source_dir / "catalog.yaml"
        if cf.exists():
            files.append(cf)
        return files

    def _any_file_changed(self) -> bool:
        """检查是否有 YAML 文件在上次加载后发生修改。"""
        for fp in self._scan_files():
            current_mtime = fp.stat().st_mtime
            if self._file_mtimes.get(str(fp), 0) != current_mtime:
                return True
        return False

    def load_all(self, force: bool = False):
        """首次调用时加载该 source 下所有 YAML 到内存。幂等。

        若 force=True 或检测到文件变更，则重新加载。
        """
        if self._loaded and not force and not self._any_file_changed():
            return
        if not self._source_dir.is_dir():
            logger.warning("Semantic source dir not found: %s", self._source_dir)
            return
        # 清理旧数据
        self._objects.clear()
        self._metrics.clear()
        self._file_mtimes.clear()
        self._load_objects()
        self._load_metrics()
        self._load_catalog()
        self._loaded = True
        logger.info("[%s] Semantic templates loaded: %d objects, %d metrics",
                     self._source, len(self._objects), len(self._metrics))

    def reload(self):
        """强制重新加载所有 YAML（供 POST /api/agent/reload 调用）。"""
        logger.info("[%s] Manual reload triggered", self._source)
        self._loaded = False
        self.load_all(force=True)

    def _load_objects(self):
        obj_dir = self._source_dir / "objects"
        if obj_dir.is_dir():
            for f in obj_dir.glob("*.yaml"):
                self._file_mtimes[str(f)] = f.stat().st_mtime
                data = yaml.safe_load(f.read_text(encoding="utf-8"))
                self._objects[data["object"]] = data

    def _load_metrics(self):
        m_dir = self._source_dir / "metrics"
        if m_dir.is_dir():
            for f in m_dir.glob("*.yaml"):
                self._file_mtimes[str(f)] = f.stat().st_mtime
                data = yaml.safe_load(f.read_text(encoding="utf-8"))
                for metric in data.get("metrics", []):
                    self._metrics[metric["metric"]] = metric

    def _load_catalog(self):
        cf = self._source_dir / "catalog.yaml"
        if cf.exists():
            self._file_mtimes[str(cf)] = cf.stat().st_mtime
            self._catalog = yaml.safe_load(cf.read_text(encoding="utf-8"))

    def get_object(self, name: str) -> dict | None:
        self.load_all()
        return self._objects.get(name)

    def get_metric(self, name: str) -> dict | None:
        self.load_all()
        return self._metrics.get(name)

    def list_objects(self) -> list[dict]:
        self.load_all()
        return list(self._objects.values())

    def list_metrics(self) -> list[dict]:
        self.load_all()
        return list(self._metrics.values())

    def get_catalog(self) -> dict | None:
        self.load_all()
        return self._catalog


# loader 注册表：按需按 source 创建/获取 loader
_loaders: dict[str, SourceSemanticLoader] = {}


def get_loader(source: str = "mes") -> SourceSemanticLoader:
    """获取指定 source 的语义模型加载器（懒加载 + 缓存）。"""
    if source not in _loaders:
        _loaders[source] = SourceSemanticLoader(source)
    return _loaders[source]
```

#### mapper.py

```python
"""YAML → SQL 翻译引擎。

核心职责：将 LLM 的 MCP 调用参数翻译成可执行的 SQL。
"""

from typing import Any


class ObjectQueryMapper:
    """将 query_objects 参数翻译成 SQL。

    输入：object="AndonEvent", filters={"workshop":"注塑"}, order_by="event_time desc", limit=50
    输出：SELECT ... FROM serving.andon_v1 WHERE workshop='注塑' ORDER BY event_time DESC LIMIT 50
    """

    def __init__(self, object_def: dict):
        self._def = object_def

    def build_query(
        self,
        filters: dict[str, Any] | None = None,
        order_by: str | None = None,
        limit: int = 100
    ) -> tuple[str, dict]:
        """构建 SQL 和参数。"""

        # 定位 serving 表
        binding = self._def["bindings"][0]
        table = binding["tables"][0]  # e.g. "serving.andon_v1"
        field_map = binding["field_map"]  # 业务字段 → SQL 列名

        # SELECT 列（跳过 field_map 中值为 null 的条目）
        active_fields = {k: v for k, v in field_map.items() if v is not None}
        columns_sql = ", ".join(f"{col} AS {name}"
                                for name, col in active_fields.items())

        # WHERE 子句
        where_clauses = []
        params = {}
        if filters:
            for field, value in filters.items():
                col = field_map.get(field, field)
                param_name = f"p_{field}"
                where_clauses.append(f"{col} = :{param_name}")
                params[param_name] = value

        # 组装
        sql = f"SELECT {columns_sql} FROM {table}"
        if where_clauses:
            sql += " WHERE " + " AND ".join(where_clauses)
        if order_by:
            # order_by 可能是 "event_time desc" 格式
            # 需要把业务字段名翻译成 SQL 列名
            order_parts = order_by.split()
            order_field = order_parts[0]
            raw_dir = order_parts[1] if len(order_parts) > 1 else "asc"
            order_dir = raw_dir.upper()
            if order_dir not in ("ASC", "DESC"):
                raise ValueError(f"order_by 排序方向无效: {raw_dir}，仅支持 ASC/DESC")
            if order_field in field_map:
                order_field = field_map[order_field]
            sql += f" ORDER BY {order_field} {order_dir}"
        sql += f" LIMIT {limit}"

        return sql, params

    def get_properties(self) -> list[dict]:
        """返回字段元信息，供 get_catalog 使用。"""
        return self._def.get("properties", [])


class MetricQueryMapper:
    """将 query_metrics 参数翻译成聚合 SQL。

    输入：metric="andon_response_rate", group_by="workshop"
    输出：SELECT workshop, COUNT(CASE WHEN response_minutes<=15 THEN 1 END)::float / COUNT(*) * 100
           FROM serving.andon_v1 GROUP BY workshop
    """

    def __init__(self, metric_def: dict, object_def: dict):
        self._metric = metric_def
        self._object = object_def

    def build_query(
        self,
        group_by: str | None = None,
        dimensions: list[str] | None = None,
        filters: dict[str, Any] | None = None,
        limit: int = 100
    ) -> tuple[str, dict]:
        """构建聚合 SQL。

        group_by 与 dimensions 的关系：`group_by` 是简化写法（传入单个分组字段字符串），
        `dimensions` 是完整写法（传入分组字段列表）。两者可同时传入，最终分组字段为
        dimensions + group_by 的并集（group_by 追加到 dimensions 末尾）。
        建议 LLM 调用时仅使用 `dimensions` 参数以保证语义清晰。
        """

        # 定位 serving 表
        binding = self._object["bindings"][0]
        table = binding["tables"][0]
        field_map = binding["field_map"]

        # 指标公式→SQL 聚合（简化版，实际需要公式解析器）
        formula = self._metric.get("formula", "")
        metric_name = self._metric["metric"]

        # 按公式类型生成聚合表达式
        agg_expr = self._translate_formula(formula, field_map)

        # GROUP BY：dimensions + group_by 并集
        group_cols = list(dimensions or [])
        if group_by and group_by not in group_cols:
            group_cols.append(group_by)

        sql_cols = [field_map.get(c, c) for c in group_cols]
        select_parts = [f"{c} AS {n}" for n, c in zip(group_cols, sql_cols)]
        select_parts.append(f"{agg_expr} AS {metric_name}")
        group_parts = [field_map.get(c, c) for c in group_cols]

        # WHERE 子句（支持过滤条件）
        where_clauses = []
        params = {}
        if filters:
            for field, value in filters.items():
                col = field_map.get(field, field)
                param_name = f"p_{field}"
                where_clauses.append(f"{col} = :{param_name}")
                params[param_name] = value

        sql = f"SELECT {', '.join(select_parts)} FROM {table}"
        if where_clauses:
            sql += " WHERE " + " AND ".join(where_clauses)
        if group_parts:
            sql += " GROUP BY " + ", ".join(group_parts)
        sql += f" LIMIT {limit}"

        return sql, params

    def _translate_formula(self, formula: str, field_map: dict) -> str:
        """将自然语言公式翻译成 SQL 聚合表达式。

        示例：
        "COUNT(AndonEvent WHERE response_minutes <= 15) / COUNT(AndonEvent) * 100"
        → "ROUND(COUNT(CASE WHEN response_minutes <= 15 THEN 1 END)::float / COUNT(*) * 100, 2)"
        """
        # 简化实现：按已知公式模式匹配
        if "response_rate" in self._metric.get("metric", ""):
            col = field_map.get("response_minutes", "response_minutes")
            return f"ROUND(COUNT(CASE WHEN {col} <= 15 THEN 1 END)::float / NULLIF(COUNT(*), 0) * 100, 2)"
        # 其他公式以此类推...
        return formula  # fallback: 原样返回（需要后续完善解析器）
```

> **说明**：`_translate_formula` 的完整实现需要公式解析器（自然语言→SQL）。d2a 内部也是类似的策略——按已知公式模式匹配。v1 阶段可以硬编码 19 个指标的翻译规则，后续可迭代为更通用的解析器。

### 6.2 app/modules/agent/（MCP 端点）

这个模块负责：暴露 HTTP 端点供 mes-agent 调用。不是标准 MCP 协议的 JSON-RPC，而是 sk-mind 自己的 REST API——因为 mes-agent 通过 Hermes/Claude Code 的 MCP 连接机制访问，Hermes 负责协议转换。

> **注**：如果未来需要标准 MCP 协议的 JSON-RPC 端点（兼容其他 MCP 客户端），可在 `/api/agent/mcp` 下加一层 JSON-RPC adapter。v1 先做 REST API，已验证 mes-agent 可以通过 MCP transport 配置连接。

#### router.py

```python
"""Agent MCP 路由 — 供 mes-agent 调用。

端点：
  POST /api/agent/query_objects   — 查询业务对象
  POST /api/agent/query_metrics   — 查询指标
  GET  /api/agent/catalog         — 获取所有可用对象和指标目录
  POST /api/agent/reload          — 热重载语义模型 YAML（无需重启进程）
"""

import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.semantic.loader import get_loader, _SEMANTIC_BASE, _loaders
from app.modules.semantic.mapper import ObjectQueryMapper, MetricQueryMapper
from app.modules.agent.schemas import (
    QueryObjectsRequest, QueryObjectsResponse,
    QueryMetricsRequest, QueryMetricsResponse,
    CatalogResponse,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/agent", tags=["agent"])


def _handle_semantic_error(obj_name: str, e: Exception) -> dict:
    """统一错误处理：捕获 mapper 层的翻译/校验错误。"""
    logger.warning("Semantic query error for [%s]: %s", obj_name, str(e))
    return {"code": 400, "message": f"查询参数无效: {str(e)}"}


@router.post("/query_objects")
async def query_objects(
    req: QueryObjectsRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """查询业务对象数据。"""
    source = req.source or "mes"
    loader = get_loader(source)
    obj_def = loader.get_object(req.object)
    if not obj_def:
        return {"code": 404, "message": f"未知业务对象: {req.object}"}

    mapper = ObjectQueryMapper(obj_def)
    try:
        sql, params = mapper.build_query(
            filters=req.filters,
            order_by=req.order_by,
            limit=req.limit or 100,
        )
    except ValueError as e:
        return _handle_semantic_error(req.object, e)

    logger.debug("query_objects SQL: %s | params: %s", sql, params)
    try:
        result = await db.execute(text(sql), params)
        rows = result.fetchall()
        columns = list(result.keys())
    except SQLAlchemyError as e:
        logger.error("SQL execution failed for object [%s]: %s", req.object, str(e))
        return {"code": 500, "message": "数据查询失败，请稍后重试"}

    return QueryObjectsResponse(
        object=req.object,
        columns=columns,
        rows=[dict(zip(columns, row)) for row in rows],
        total=len(rows),
    ).model_dump()


@router.post("/query_metrics")
async def query_metrics(
    req: QueryMetricsRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """查询指标聚合数据。"""
    source = req.source or "mes"
    loader = get_loader(source)
    metric_def = loader.get_metric(req.metric)
    if not metric_def:
        return {"code": 404, "message": f"未知指标: {req.metric}"}

    obj_name = metric_def.get("source_object")
    obj_def = loader.get_object(obj_name)
    if not obj_def:
        return {"code": 404, "message": f"指标关联的业务对象不存在: {obj_name}"}

    mapper = MetricQueryMapper(metric_def, obj_def)
    try:
        sql, params = mapper.build_query(
            group_by=req.group_by,
            dimensions=req.dimensions,
            filters=req.filters,
            limit=req.limit or 100,
        )
    except ValueError as e:
        return _handle_semantic_error(req.metric, e)

    logger.debug("query_metrics SQL: %s | params: %s", sql, params)
    try:
        result = await db.execute(text(sql), params)
        rows = result.fetchall()
        columns = list(result.keys())
    except SQLAlchemyError as e:
        logger.error("SQL execution failed for metric [%s]: %s", req.metric, str(e))
        return {"code": 500, "message": "数据查询失败，请稍后重试"}

    return QueryMetricsResponse(
        metric=req.metric,
        columns=columns,
        rows=[dict(zip(columns, row)) for row in rows],
        total=len(rows),
    ).model_dump()


@router.get("/catalog")
async def get_catalog(
    source: str | None = Query(None, description="数据源, e.g. mes。不传则汇总所有系统"),
    current_user: User = Depends(get_current_user),
):
    """返回可用业务对象和指标目录。"""
    sources = [source] if source else _available_sources()
    all_objects = []
    all_metrics = []
    for src in sources:
        loader = get_loader(src)
        all_objects.extend(loader.list_objects())
        all_metrics.extend(loader.list_metrics())

    return CatalogResponse(
        objects=[
            {
                "name": o["object"],
                "display_name": o["display_name"],
                "description": o["description"],
                "keys": o.get("keys", []),
            }
            for o in all_objects
        ],
        metrics=[
            {
                "name": m["metric"],
                "display_name": m["display_name"],
                "description": m.get("description", ""),
                "formula": m.get("formula", ""),
            }
            for m in all_metrics
        ],
    ).model_dump()


def _available_sources() -> list[str]:
    """扫描 config/semantic/ 下所有可用数据源目录。"""
    sources = []
    for d in _SEMANTIC_BASE.iterdir():
        if d.is_dir() and (d / "catalog.yaml").exists():
            sources.append(d.name)
    return sources if sources else ["mes"]


@router.post("/reload")
async def reload_semantic(
    source: str | None = Query(None, description="指定重载的数据源, e.g. mes。不传则全部重载"),
    current_user: User = Depends(get_current_user),
):
    """热重载语义模型 YAML 配置，无需重启进程。

    供运维人员在修改 YAML 文件后调用。
    """
    if source:
        loader = get_loader(source)
        loader.reload()
        return {"code": 200, "message": f"已重新加载 [{source}] 语义模型"}
    else:
        for src, ld in _loaders.items():
            ld.reload()
        return {"code": 200, "message": f"已重新加载所有语义模型 ({len(_loaders)} 个数据源)"}
```

#### schemas.py

```python
"""Agent MCP 请求/响应 Pydantic 模型。"""

from pydantic import BaseModel, Field
from typing import Any


class QueryObjectsRequest(BaseModel):
    source: str | None = Field(None, description="数据源, e.g. mes。默认 mes")
    object: str = Field(..., description="业务对象名, e.g. AndonEvent")
    filters: dict[str, Any] | None = Field(None, description="过滤条件, e.g. {workshop: 注塑}")
    order_by: str | None = Field(None, description="排序, e.g. event_time desc。排序方向含在字符串中")
    limit: int = Field(100, ge=1, le=1000)


class QueryObjectsResponse(BaseModel):
    object: str
    columns: list[str]
    rows: list[dict[str, Any]]
    total: int


class QueryMetricsRequest(BaseModel):
    source: str | None = Field(None, description="数据源, e.g. mes。默认 mes")
    metric: str = Field(..., description="指标名, e.g. andon_response_rate")
    group_by: str | None = Field(None, description="分组字段, e.g. workshop")
    dimensions: list[str] | None = Field(None, description="下钻维度")
    filters: dict[str, Any] | None = Field(None, description="过滤条件, e.g. {workshop: 注塑, date: 2026-07-01}")
    limit: int = Field(100, ge=1, le=1000)


class QueryMetricsResponse(BaseModel):
    metric: str
    columns: list[str]
    rows: list[dict[str, Any]]
    total: int


class CatalogObjectItem(BaseModel):
    name: str
    display_name: str
    description: str
    keys: list[str]


class CatalogMetricItem(BaseModel):
    name: str
    display_name: str
    description: str
    formula: str


class CatalogResponse(BaseModel):
    objects: list[CatalogObjectItem]
    metrics: list[CatalogMetricItem]
```

### 6.3 路由注册

`app/api/__init__.py` 中新增两行：

```python
from app.modules.agent.router import router as agent_router

# 在现有 router.include_router(...) 块末尾加：
router.include_router(agent_router)
```

---

## 七、与已有模块的关系

### 7.1 与 datasets 模块

sk-mind 的 `Dataset` / `DatasetField` / `DataTable` 是**物理表级别的元数据管理**——记录 raw 表有哪些、字段是什么类型。

语义模型 YAML 是**业务级别的抽象**——定义"安灯事件"这个业务概念对应哪个 serving 视图、有哪些业务字段。

两者是**并行关系**，不互相依赖：
- `datasets` 管理的是 raw 表（`raw.mes_andon_api_controller`）
- `semantic` 定义的是业务对象（`AndonEvent` → `serving.andon_v1`）

将来可以做**自动关联**：语义模型的每个 business object 自动创建一个 `Dataset` 记录（`data_layer='serving'`），让数据目录面板也能看到 serving 层数据。但这是 v2 的事。

### 7.2 与 catalog 模块

sk-mind 的 `catalog/` 模块是**跨数据集的搜索和浏览**（前端数据目录 UI）。

语义模型的 `catalog.yaml` + `GET /api/agent/catalog` 是**给 LLM 看的 API 目录**——告诉 mes-agent 有哪些 business object 和 metric 可以查。

两个 catalog 的受众不同（人类 vs LLM），不冲突。

### 7.3 与 data_sources 模块

不直接关联。语义模型 YAML 中的 `bindings[].source: lightmes` 仅用于文档标注，MCP 查询不需要查 `data_sources` 表。

### 7.4 如何集成 Auth

所有 agent 端点都使用 `Depends(get_current_user)`，与 sk-mind 现有路由完全一致的权限控制。

mes-agent 通过环境变量 `SKMIND_MCP_TOKEN` 传入 JWT token，与现有认证流程一致。

### 7.5 数据库连接

复用 `app.core.database.async_session_factory`，通过 `get_db` 依赖注入获取 `AsyncSession`。不另建连接池。

---

## 八、实施阶段

### 阶段 1：Alembic 迁移 — Serving 视图（sk-mind 团队）

1. 创建 `alembic/versions/019_serving_views.py`
2. UPGRADE：建 `serving` schema + 8 个 CREATE VIEW + COMMENT
3. DOWNGRADE：DROP VIEW
4. 跑 `alembic upgrade head` 验证
5. 抽样验证每个视图的数据正确性

### 阶段 2：语义模型 YAML 文件（mes-agent 团队交付）

1. 8 个 `config/semantic/mes/objects/*.yaml`
2. 3 个 `config/semantic/mes/metrics/*.yaml`
3. 1 个 `config/semantic/mes/catalog.yaml`

这些 YAML 直接提交到 sk-mind 仓库的 `backend/config/semantic/mes/` 目录。

### 阶段 3：代码模块（sk-mind 团队）

1. 实现 `app/modules/semantic/loader.py`（YAML 加载 + 缓存）
2. 实现 `app/modules/semantic/mapper.py`（ObjectQueryMapper + MetricQueryMapper 的 SQL 翻译）
3. 实现 `app/modules/agent/schemas.py`（Pydantic 模型）
4. 实现 `app/modules/agent/router.py`（3 个端点）
5. 在 `app/api/__init__.py` 注册 `agent_router`
6. 本地启动验证：`POST /api/agent/catalog` 返回目录

### 阶段 4：联调（mes-agent ↔ sk-mind）

1. mes-agent 的 `agent.yaml` 配置 MCP URL 指向 sk-mind 的 `/api/agent/*`
2. 按 Skill 逐一验证查询结果
3. 调整语义模型 YAML 和 mes-agent rules 直到质量达标

---

## 九、注意事项（MES 特有陷阱）

### 9.1 车间代码映射

不同接口的车间字段名不同：`workshop_code`、`department_code`、`workshop`。**Serving 视图的 CASE WHEN 映射需要在实施时按实际 API 返回值逐一验证**，不可假设所有接口都返回 `ws01`~`ws06`。

### 9.2 时间格式差异

| 接口 | 时间字段格式 |
|------|------------|
| andonApiController | Java 毫秒 (bigint) |
| filterWorkorder | `"%Y-%m-%d"` 字符串 |
| selectOeeReport | `"%Y-%m-%d %H:%M:%S"` 字符串 |
| selectErrorReport | `"%Y-%m-%d %H:%M:%S"` 字符串 |

Serving 视图的 SQL 需按实际格式适配，不可套用一种转换逻辑。

### 9.3 已知的脏字段

按 [[mes-hermes-skill]] 记录：
- `processingTimeout`：永远 false，不写入 serving 视图
- `produceHours`：理论值非实测，保留但 COMMENT 标注
- `greenRate`：灰灯放分母，可能压低线效数值

### 9.4 机台号全半角

LightMES API 返回的机台号中，半角 `~` 和全角 `～` 同时存在。Serving 视图 JOIN 时必须：
```sql
ON REPLACE(a.machine_no, '～', '~') = REPLACE(b.machine_no, '～', '~')
```

---

## 十、验收标准

- [x] `alembic upgrade head` 可执行，8 个 serving 视图创建成功（020_create_serving_views.py）
- [x] 所有 serving 视图有 COMMENT 注释
- [x] 8 个 `config/semantic/mes/objects/*.yaml` 完整（properties + bindings.field_map）
- [x] 3 个 `config/semantic/mes/metrics/*.yaml` 完整（19 个指标，含 description + freshness_sla）
- [x] 1 个 `config/semantic/mes/catalog.yaml` 总索引
- [x] `GET /api/agent/catalog` 返回完整目录（需登录）— 2026-07-31 已验证
- [ ] `POST /api/agent/query_objects` 传入 `{"source":"mes", "objectName":"andon_event"}` 可返回数据 — 需 serving 视图 + 数据
- [ ] `POST /api/agent/query_metrics` 传入 `{"source":"mes", "metricName":"green_rate_avg", "dimensions":["machine_no"]}` 可返回聚合数据 — 需 serving 视图 + 数据
- [x] `GET /api/agent/catalog?source=mes` 返回 MES 系统目录；不传 source 返回所有系统汇总
- [ ] mes-agent 可通过 HTTP 调用三个端点，各端点返回正确数据 — 待 mes-agent 联调
- [x] `app/api/__init__.py` 注册了 agent_router

### 集成测试（阶段 4 联调中补充）

自动化测试用例建议覆盖以下路径：

| 测试类型 | 测试内容 | 验证点 |
|----------|---------|--------|
| query_objects 正常路径 | 查询安灯事件（无过滤、带过滤、带排序） | 返回正确 column 和 row |
| query_objects 异常路径 | 不存在的 object、无效 order_by 方向 | 返回 404 / 400 错误 |
| query_metrics 正常路径 | 查询 OEE 绿灯率（按车间分组、加时间过滤） | 聚合结果正确 |
| query_metrics 异常路径 | 不存在的 metric、断链的 source_object | 返回 404 / 400 错误 |
| catalog 正常路径 | 获取 MES 全量目录、获取特定 source | 返回完整对象+指标列表 |
| reload 正常路径 | 修改 YAML 后调用 reload，再次查询 | 返回更新后的数据 |
| 已知 YAML → SQL 验证 | 对 8 个 object YAML 分别生成 SQL | SQL 语法正确，列映射一致 |
| 已知 YAML → 指标 SQL 验证 | 对 19 个 metric 分别生成 SQL | 聚合表达式正确 |

---

## 附录 A：与前一版设计的核心差异

| 维度 | 前一版设计 | 本版设计 | 原因 |
|------|-----------|---------|------|
| MCP Server 部署 | 独立进程，端口 8848 | `app/modules/agent/` FastAPI 模块 | 复用已有 auth/CORS/生命周期 |
| YAML 位置 | `templates/objects/` | `config/semantic/mes/objects/` | 与 `config/data_sources/MES.yaml` 同级，按 source 分目录 |
| Serving 视图 | ad-hoc SQL | Alembic migration `019_serving_views.py` | 遵循已有 18 个迁移的工作流 |
| YAML 加载器 | 从零造 | `SourceSemanticLoader` + `get_loader(source)` 按 source 懒加载 | 与 data_sources 的 YAML 加载模式一致，支持多数据源 |
| 数据库连接 | 独立 mcp_reader 用户 | 复用 `async_session_factory` + `get_db` | 不重复建连接池 |
| 认证 | 独立 MCP token | 复用 JWT `get_current_user` | 统一认证 |
| 语义模型模块 | 无拆分 | `semantic/` (加载+翻译) + `agent/` (端点) | 职责分离 |

## 附录 B：serving 视图 SQL（实施时完善）

8 个视图的完整 CREATE VIEW SQL 将在阶段 1（Alembic 迁移）实施时，由 sk-mind 团队根据 raw 表实际 schema 编写。设计依据：
- 4.4 节的通用清洗规则（时间戳转换、波浪号统一、车间映射、班次推断等）
- 4.5 节每个视图的核心加工要点
- `config/data_sources/MES.yaml` 中各接口的 `target_table`、`pk_fields`、`time_config`

---

## 附录 C：实施状态更新（2026-07-31）

> **说明**：本设计方案于 2026-07-28 编写，至 2026-07-31 已完成大部分实施。以下为实际代码状态与设计文档的差异汇总。

### 已完成项

| 设计章节 | 设计阶段 | 实际状态 |
|---------|---------|---------|
| 四、Serving 视图 | 待实施 | ✅ Alembic 020 `020_create_serving_views.py` 已创建 8 个视图 |
| 五、YAML 定义 | 仅 1 示例 | ✅ 8 object + 3 metric + 1 catalog 全部存在 |
| 六、代码模块 | 伪代码 | ✅ loader/mapper/models/dao/router/schemas 完整实现 |
| 七、模块关系 | 设计说明 | ✅ agent_router 和 semantic_router 已注册 |
| 十、验收标准 | checklist | ✅ 见下方 D2 |

### 实际代码与设计文档的差异

| 差异点 | 设计文档 | 实际代码 | 影响 |
|--------|---------|---------|------|
| agent schema 字段名 | `object` / `metric` | `objectName` / `metricName` (CamelCase) | mes-agent 调用时需使用 CamelCase |
| YAML properties 格式 | `{ name, type, desc }` | `{ code, name, property_type, data_type }` | 无影响，已按实际调整 |
| loader 职责 | 仅 YAML 加载 | 额外含 `sync_to_db()` DB 同步 | Plan A 核心，已实现 |
| semantic 模块 | stub | 含完整 ORM 模型 + CRUD API | 超出设计范围但已实现 |
| metric 名称 | 如 `andon_response_rate` | 如 `andon_call_count` | 与 mapper 公式表一致 |
| limit 上限 | 1000 | 10000 | 无影响 |
| Alembic 版本号 | 019 | 019(表) + 020(视图) | 设计文档写 019，实际 020 |

### 单元测试

- [[../../backend/tests/test_semantic_loader.py|test_semantic_loader.py]] — 18 个测试，覆盖 loader 加载/缓存/reload/完整性校验
- [[../../backend/tests/test_semantic_mapper.py|test_semantic_mapper.py]] — 24 个测试，覆盖 mapper SQL 翻译/19 指标公式

### 待完成（依赖外部）

- B4：serving 视图数据正确性验证（需要 raw 表有真实 MES 数据）
- C1-C3：mes-agent 联调集成（mes-agent 为独立仓库）
- 附录 B：完整 serving 视图 SQL（已在 `020_create_serving_views.py` 中实现）
