![[2026-07-23-agent-config-design]]# sk-mind — AI 原生企业数据平台

面向中小型制造企业的可信数据底座与 Agent 数据服务平台。让企业的 ERP、MES、Excel、共享盘数据**接得进来、查得到、来源说得清、质量看得见**。

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + Vite + TypeScript + Element Plus |
| 后端 | Python + FastAPI + SQLAlchemy + Alembic |
| 数据库 | PostgreSQL 16 |
| 缓存/队列 | Redis + RQ |
| 部署 | Docker Compose + Nginx |

## 服务端口一览

项目由 6 个服务组成，分容器化部署和本地开发两种模式：

### 容器化部署（docker compose up -d）

| 服务 | 容器名 | 端口 | 作用 |
|------|--------|------|------|
| **PostgreSQL** | `skmind-postgres` | `5432` | 关系数据库，存储全部业务数据和元数据 |
| **Redis** | `skmind-redis` | `6379` | 缓存 + 消息队列（RQ），Worker 通过 Redis 消费任务 |
| **Backend API** | `skmind-backend` | `8000` | FastAPI 后端，含 REST API + Agent MCP 端点（`/api/agent/*`） + Swagger 文档（`/docs`） |
| **Worker** | `skmind-worker` | — | RQ Worker，消费 `ingestion` 队列，执行数据同步等异步长任务 |
| **Nginx** | `skmind-nginx` | `80` | 反向代理：前端静态资源 + `/api` 代理到 Backend |
| **Frontend** | — | — | Vue 3 SPA 静态文件，由 Nginx 托管，无独立端口 |

### 本地开发

| 服务 | 端口 | 启动命令 | 作用 |
|------|------|----------|------|
| **PostgreSQL** | `5432` | `docker compose up -d postgres` | 数据库 |
| **Redis** | `6379` | `docker compose up -d redis` | 缓存/队列 |
| **Backend API** | `8000` | `python run_api.py` | FastAPI + uvicorn，`--reload` 热重载 |
| **Frontend** | `5173` | `npm run dev` | Vite dev server，HMR 热更新，`/api` 代理到 `localhost:8000` |
| **Worker** | — | `python run_worker.py` | RQ Worker，消费 `ingestion` 队列 |
| **Scheduler** | — | `python run_scheduler.py` | APScheduler，按 cron 表达式将定时任务入队到 RQ |

> **说明**：Agent MCP 服务不是独立进程，它是 Backend API 的一部分——端点挂在 `/api/agent/*` 下（`query_objects` / `query_metrics` / `query_relations` / `query_graph` / `catalog` / `reload`），与 REST API 共享同一个 uvicorn 进程和 8000 端口。

## 项目结构

```
sk-mind/
├── backend/                # FastAPI 后端
│   ├── app/
│   │   ├── api/            # API 路由（auth）
│   │   ├── core/           # 配置、数据库、安全、日志、鉴权依赖
│   │   ├── modules/        # 业务模块
│   │   │   ├── auth/       #   用户、角色、权限、审计
│   │   │   ├── data_sources/  # 数据源管理 (模型)
│   │   │   ├── ingestion/  #   接入任务、批次、错误清单 (模型)
│   │   │   ├── datasets/   #   数据集、字段、数据表 (模型)
│   │   │   ├── quality/    #   质量规则、检查、问题 (模型)
│   │   │   ├── lineage/    #   数据血缘 (模型)
│   │   │   ├── catalog/    #   数据目录 (待开发)
│   │   │   ├── semantic/   #   语义模型 (待开发)
│   │   │   ├── graph/      #   业务关系图谱 (待开发)
│   │   │   ├── metrics/    #   指标规则 (待开发)
│   │   │   └── agent/      #   Agent 数据服务 (待开发)
│   │   ├── workers/        # 异步任务 Worker
│   │   ├── main.py         # 应用入口
│   │   └── seed.py         # 数据库初始化种子脚本
│   ├── alembic/            # 数据库迁移
│   ├── tests/              # 测试
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pyproject.toml
├── frontend/               # Vue 3 前端
│   └── src/
│       ├── api/            # Axios API 客户端
│       ├── layouts/        # 后台管理布局
│       ├── router/         # Vue Router
│       └── views/          # 页面（首页/数据源/接入任务/数据目录/数据质量）
├── deploy/                 # 部署配置
│   └── nginx/
│       └── default.conf
├── docs/                   # 产品/技术文档
├── docker-compose.yml
└── .env.example
```

## 快速开始

### 方式一：Docker Compose（推荐）

```bash
# 1. 复制环境配置
cp .env.example .env

# 2. 启动全部服务（PostgreSQL + Redis + Backend + Worker + Nginx）
docker-compose up -d

# 3. 初始化数据库和种子数据
docker-compose exec backend python -m app.seed

# 4. 访问
# 后端 API 文档: http://localhost:8000/docs
# 前端页面:     http://localhost
```

### 方式二：本地开发

**前置条件：** Python 3.11+ / Node.js 18+。项目已在根目录自带虚拟环境 `.venv`，无需另行创建。

```powershell
# 1. 启动 PostgreSQL 和 Redis（任选一种）
docker-compose up -d postgres redis

# 2. 安装后端依赖
cd backend
..\.venv\Scripts\python.exe -m pip install -r requirements.txt

# 3. 初始化数据库
cp ../.env.example ../.env
..\.venv\Scripts\python.exe -m app.seed

# 4. 启动后端 API（开发模式，热重载）
..\.venv\Scripts\python.exe run_api.py

# 5. 新终端，启动后台 Worker（消费同步任务队列，必须单独启动）
..\.venv\Scripts\python.exe run_worker.py

# 6.（可选）新终端，启动定时调度器
..\.venv\Scripts\python.exe run_scheduler.py

# 7. 新终端，启动前端
cd ../frontend
npm install
npm run dev
```

> **说明**：前端 `vite.config.ts` 已设 `server.host: true`，`npm run dev` 自动监听 `0.0.0.0`，局域网内其他设备（如 Mac mini、平板）可通过本机 IP:5173 访问。

> **说明**：`run_api.py` 内部即 `uvicorn.run("app.main:app", reload=True)`，等价于前端的 `npm run dev`。Git Bash 下路径写作 `../.venv/Scripts/python.exe`。API 与 Worker 是两个独立进程：API 负责即时应答与接收请求，Worker 在后台消费 Redis 队列执行数据同步等长任务，互不阻塞。

## API 文档

后端启动后访问：

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 当前可用 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| GET | `/api/status` | 模块状态 |
| POST | `/api/auth/login` | 用户登录 |
| POST | `/api/auth/register` | 用户注册 |
| POST | `/api/auth/refresh` | 刷新 Token |
| GET | `/api/auth/me` | 当前用户信息 |
| GET | `/api/auth/users` | 用户列表（管理员） |
| GET | `/api/auth/roles` | 角色列表（管理员） |
| POST | `/api/auth/roles` | 创建角色（管理员） |
| GET | `/api/auth/permissions` | 权限列表（管理员） |
| GET | `/api/auth/audit-logs` | 审计日志（管理员） |

### 默认管理员账号

| 用户名 | 密码 |
|--------|------|
| admin | admin123 |

## 开发

### 运行测试

```bash
cd backend
python -m pytest tests/ -v
```

### 数据库迁移

```bash
cd backend

# 生成迁移（修改模型后）
alembic revision --autogenerate -m "描述"

# 执行迁移
alembic upgrade head

# 回滚
alembic downgrade -1
```

### 本地启动（VSCode / 一键）

- **VSCode 调试**：按 F5 选择 `sk-mind Backend (API)` 断点调试（首次需安装 `debugpy`，F5 会提示）。
- **一键启动（Git Bash）**：`backend/` 下已提供 `Makefile`：
  - `make dev` 启动 API
  - `make worker` 启动 Worker
  - `make scheduler` 启动调度器
  - `make install` 安装依赖
- **为什么分 API 与 Worker**：API 负责即时应答与接收请求；Worker 在后台消费 Redis 队列执行数据同步等长任务，二者进程独立、互不阻塞。
- 完整启动命令见上文「方式二：本地开发」。

## 开发阶段

当前处于 **阶段 1：可信数据底座** 建设期。

| 任务 | 状态 |
|------|------|
| T01 工程骨架与本地开发环境 | ✅ 完成 |
| T02 数据库模型、迁移与测试基座 | ✅ 完成 |
| T03 用户、角色、权限与审计基础 | ✅ 完成 |
| T04 数据源管理后端 | 待开发 |
| T05 数据源管理前端 | 待开发 |
| T06-T14 阶段 1 其他任务 | 待开发 |

完整任务清单见 [`docs/ai-native-enterprise-data-platform-team-development-tasks.md`](docs/ai-native-enterprise-data-platform-team-development-tasks.md)

## 架构原则

- 模块化单体，不拆微服务
- PostgreSQL 优先，不引入独立图数据库/湖仓
- 异步任务用 RQ + Redis，不引入 Airflow/Spark
- 轻量语义模型用关系表 + JSONB，不引入 RDF/OWL
- Agent 通过受控工具使用数据，不直接执行任意 SQL

## 文档索引

| 文档 | 说明 |
|------|------|
| [产品方案](docs/ai-native-enterprise-data-platform-solution.md) | 产品定位、目标客户、业务价值 |
| [基础建设方案](docs/ai-native-enterprise-data-platform-foundation.md) | 平台数据库、语义图谱、Agent 服务 |
| [技术设计](docs/ai-native-enterprise-data-platform-technical-design.md) | 架构边界、模块职责、数据流 |
| [PRD](docs/ai-native-enterprise-data-platform-foundation-prd.md) | 功能需求、页面、状态、验收 |
| [团队开发任务](docs/ai-native-enterprise-data-platform-team-development-tasks.md) | 一人周任务拆解 |
