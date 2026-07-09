# 03 — API 拉取同步策略

版本：v0.1
日期：2026-07-08

## 文档说明

本文档定义**策略二：API 拉取同步**的通用技术方案。

适用场景：源系统通过 HTTP REST API 提供数据，不可直连数据库。本方案不绑定任何特定系统（MES/SRM），各系统的具体接口配置见 [05-数据源同步配置](./05-数据源同步配置.md)。

---

## 1. 策略概述

### 1.1 核心流程

```text
┌──────────┐     ┌─────────────────┐     ┌──────────────────┐
│ REST API │ →   │ ApiConnector     │ →   │ PostgreSQL Raw 层 │
│          │     │ (httpx + 限流)   │     │ raw_record JSONB  │
│ POST/GET │     │ 分页/重试/鉴权   │     │ + 追踪字段         │
└──────────┘     └─────────────────┘     └──────────────────┘
```

### 1.2 适用条件

| 条件 | 要求 |
|---|---|
| 接口协议 | HTTP/HTTPS，支持 GET 或 POST |
| 鉴权方式 | Token / Basic Auth / API Key / Session Cookie |
| 分页支持 | 有分页参数（offset/limit 或游标） |
| 响应格式 | JSON（优先）或 XML |
| QPS 限制 | 明确或有据可查 |

### 1.3 与数据库视图同步的差异

| 维度 | 数据库视图同步 | API 拉取同步 |
|---|---|---|
| 数据获取 | SELECT 批量拉取 | HTTP 请求逐页拉取 |
| Raw 存储 | 物理表（结构稳定） | JSONB 通用表（结构可能变化） |
| 速度瓶颈 | 网络带宽 + 数据库 I/O | API QPS 限流 + 网络延迟 |
| Schema 管理 | DDL 主动管理 | JSONB 柔性存储 |
| 增量策略 | 时间戳 / hash | 依赖接口提供的查询参数 |

---

## 2. Connector 设计

### 2.1 抽象接口

```python
class ApiConnector(ABC):
    """API 连接器抽象基类"""

    @abstractmethod
    def authenticate(self) -> None: ...

    @abstractmethod
    def test_connection(self) -> bool: ...

    @abstractmethod
    def fetch_page(
        self, endpoint: str, method: str = "POST",
        params: dict = None, body: dict = None,
        page: int = 1, page_size: int = 100
    ) -> ApiPageResult: ...

    @abstractmethod
    def fetch_all_pages(
        self, endpoint: str, method: str = "POST",
        params: dict = None, body: dict = None,
        page_size: int = 100, max_pages: int = None
    ) -> Iterator[dict]: ...
```

### 2.2 通用实现 (HttpxApiConnector)

```python
class HttpxApiConnector(ApiConnector):
    """基于 httpx 的通用 API 连接器"""

    def __init__(self, config: ApiConfig):
        self.config = config
        self._client: httpx.Client = None
        self._rate_limiter: TokenBucket = None

    def connect(self):
        self._client = httpx.Client(
            base_url=self.config.base_url,
            timeout=self.config.timeout,
            headers=self.config.default_headers,
        )
        if self.config.auth_type == "bearer":
            self.authenticate()
        self._rate_limiter = TokenBucket(
            rate=self.config.qps_limit,  # 默认 10 QPS
        )

    def fetch_page(self, endpoint, method="POST", params=None,
                   body=None, page=1, page_size=100):
        self._rate_limiter.acquire()           # 限流等待
        payload = self._build_payload(body, page, page_size)
        resp = self._client.request(method, endpoint, params=params, json=payload)
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 5))
            time.sleep(retry_after)
            return self.fetch_page(...)        # 重试
        resp.raise_for_status()
        data = resp.json()
        return ApiPageResult(
            records=data.get(self.config.records_path),
            total=data.get(self.config.total_path),
            page=page, page_size=page_size,
        )

    def fetch_all_pages(self, endpoint, method="POST",
                        params=None, body=None,
                        page_size=100, max_pages=None):
        page = 1
        while True:
            result = self.fetch_page(endpoint, method, params, body, page, page_size)
            yield from result.records
            if max_pages and page >= max_pages:
                break
            if len(result.records) < page_size:
                break                            # 最后一页
            page += 1
```

### 2.3 配置模型

```python
class ApiAuthType(str, Enum):
    NONE = "none"
    BEARER = "bearer"
    BASIC = "basic"
    API_KEY = "api_key"
    SESSION = "session"

class ApiConfig(BaseModel):
    base_url: str                     # 如 "https://mes.example.com"
    auth_type: ApiAuthType = ApiAuthType.BEARER
    auth_credentials: SecretStr       # token / user:pass / api-key
    auth_header_name: str = "Authorization"
    auth_token_prefix: str = "Bearer"
    qps_limit: int = 10               # QPS 上限
    timeout: int = 30                 # 请求超时(秒)
    max_retries: int = 3              # 最大重试次数
    retry_backoff: float = 1.5        # 退避因子

    # JSON 响应解析路径
    records_path: str = "data.list"   # 记录列表在响应 JSON 中的路径
    total_path: str = "data.total"    # 总数在响应 JSON 中的路径
    page_field: str = "page"          # 分页页码字段名
    page_size_field: str = "pageSize" # 分页大小字段名
```

---

## 3. 分页策略

### 3.1 分页模式

| 模式 | 请求参数 | 结束判断 | 适用 |
|---|---|---|---|
| **偏移分页** | `{page: N, pageSize: M}` | `len(records) < pageSize` | 大多数 REST API |
| **游标分页** | `{cursor: "xxx", limit: M}` | `next_cursor == null` | 数据量大、要求一致性 |
| **时间范围分页** | `{startTime: T1, endTime: T2}` | `endTime >= now` | 按时间段分批拉取 |

### 3.2 偏移分页实现

```python
def _paginate_offset(self, endpoint, body, page_size):
    page = 1
    while True:
        body[self.config.page_field] = page
        body[self.config.page_size_field] = page_size
        result = self.fetch_page(endpoint, body=body)
        yield from result.records
        if len(result.records) < page_size:
            break
        page += 1
```

### 3.3 游标分页实现

```python
def _paginate_cursor(self, endpoint, body, limit):
    cursor = None
    while True:
        if cursor:
            body['cursor'] = cursor
        result = self.fetch_page(endpoint, body={**body, 'limit': limit})
        yield from result.records
        cursor = result.next_cursor
        if not cursor:
            break
```

### 3.4 时间范围分页实现

适用于按时间窗口拉取的接口（如 MES 报工数据）：

```python
def _paginate_timerange(self, endpoint, body, start, end, window_hours=24):
    current = start
    while current < end:
        window_end = min(current + timedelta(hours=window_hours), end)
        body['startTime'] = current.isoformat()
        body['endTime'] = window_end.isoformat()
        result = self.fetch_page(endpoint, body=body)
        yield from result.records
        current = window_end
```

---

## 4. 限流策略

### 4.1 令牌桶算法

```python
class TokenBucket:
    """简单的令牌桶限流器"""

    def __init__(self, rate: int):
        self.rate = rate               # 每秒允许请求数
        self.tokens = rate
        self.last_refill = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self):
        with self._lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(self.rate, self.tokens + elapsed * self.rate)
            self.last_refill = now
            if self.tokens < 1:
                wait = (1 - self.tokens) / self.rate
                time.sleep(wait)
                self.tokens = 0
            else:
                self.tokens -= 1
```

### 4.2 限流策略

| 场景 | 策略 |
|---|---|
| 接口有明确 QPS 限制 | 按声明的 QPS 限流（如 MES 10 QPS） |
| 接口无明确限制 | 默认 5 QPS，逐步上调观察 |
| 接口返回 429 | 读取 `Retry-After` 头，暂停后恢复 |
| 多接口共用限流 | 按 base_url 分组，同域名共享令牌桶 |

---

## 5. 重试策略

### 5.1 重试决策

| HTTP 状态码 | 含义 | 重试？ | 策略 |
|---|---|---|---|
| 429 | 限流 | 是 | 等待 `Retry-After` 秒 |
| 502/503/504 | 服务端临时故障 | 是 | 指数退避 1s→2s→4s |
| 408 | 请求超时 | 是 | 指数退避 |
| 401/403 | 认证/权限失败 | 否 | 立即失败，告警 |
| 404 | 接口不存在 | 否 | 立即失败 |
| 422/400 | 请求参数错误 | 否 | 立即失败，记录请求参数 |

### 5.2 退避策略

```python
def _retry_with_backoff(self, func, max_retries=3, base_delay=1.0):
    for attempt in range(max_retries):
        try:
            return func()
        except (httpx.HTTPStatusError, httpx.TimeoutException) as e:
            if attempt == max_retries - 1:
                raise
            if e.response.status_code == 429:
                delay = int(e.response.headers.get("Retry-After", 5))
            else:
                delay = base_delay * (2 ** attempt)
            time.sleep(delay)
```

---

## 6. Raw 层存储策略

### 6.1 两种存储方式

| 方式 | 适用场景 | 表结构 |
|---|---|---|
| **JSONB 通用表**（默认） | API 响应结构可能变化、探索阶段 | `raw_record` 字段：`_raw_id, _batch_id, ..., payload JSONB` |
| **结构化物理表** | API 响应结构稳定、需要高性能查询 | 按响应字段生成物理表 DDL |

平台默认推荐 **JSONB 通用表** 作为初次接入的存储方式。待接口稳定、查询需求明确后，可迁移到结构化物理表。

### 6.2 JSONB 通用表 DDL

```sql
CREATE TABLE raw_record (
    _raw_id              BIGSERIAL PRIMARY KEY,
    _batch_id            VARCHAR(64)  NOT NULL,
    _source_system       VARCHAR(64)  NOT NULL,   -- 'MES_LIGHT' / 'SRM'
    _source_object       VARCHAR(256) NOT NULL,   -- 接口端点
    _source_row_hash     VARCHAR(64)  NOT NULL,   -- SHA-256 of payload
    _api_url             VARCHAR(512) NOT NULL,
    _api_request_params  JSONB,
    _api_response_at     TIMESTAMPTZ  NOT NULL,
    _ingested_at         TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    _is_deleted          BOOLEAN      NOT NULL DEFAULT FALSE,
    payload              JSONB        NOT NULL    -- 原始响应数据
);

CREATE INDEX idx_raw_record_batch   ON raw_record (_batch_id);
CREATE INDEX idx_raw_record_system  ON raw_record (_source_system);
CREATE INDEX idx_raw_record_object  ON raw_record (_source_object);
CREATE INDEX idx_raw_record_ingest  ON raw_record (_ingested_at);
-- GIN 索引支持 payload 内 JSON 查询
CREATE INDEX idx_raw_record_payload ON raw_record USING GIN (payload jsonb_path_ops);
```

### 6.3 JSONB 写入示例

```python
def write_page_to_raw(pg_session, batch_id, source_system, endpoint, body, records):
    """将一页 API 响应写入 raw_record 表"""
    rows = []
    for rec in records:
        rows.append({
            '_batch_id': batch_id,
            '_source_system': source_system,
            '_source_object': endpoint,
            '_source_row_hash': compute_hash(json.dumps(rec, sort_keys=True)),
            '_api_url': f"{base_url}{endpoint}",
            '_api_request_params': json.dumps(body),  # 脱敏后的请求参数
            '_api_response_at': datetime.utcnow().isoformat(),
            'payload': json.dumps(rec),
        })
    pg_session.execute(
        insert(RawRecord).values(rows).on_conflict_do_nothing()
    )
    pg_session.commit()
```

### 6.4 JSONB 去重

由于 API 响应可能包含重复记录，使用 `_source_row_hash` + `_source_object` 做去重：

```sql
-- 同批次内相同接口相同内容不入库
INSERT INTO raw_record (...) VALUES (...)
ON CONFLICT (_source_row_hash, _source_object, _batch_id) DO NOTHING;
```

---

## 7. 鉴权管理

### 7.1 鉴权类型与配置

| 鉴权类型 | 配置方式 | Token 刷新 |
|---|---|---|
| **Bearer Token** | `Authorization: Bearer {token}` | 支持过期检测，自动用 refresh_token 续期 |
| **Basic Auth** | `Authorization: Basic {base64(user:pass)}` | 无需刷新 |
| **API Key** | 自定义 Header，如 `X-API-Key: {key}` | 无需刷新 |
| **Session Cookie** | 先 POST `/login` 获取 Cookie，后续请求携带 | 支持过期重登录 |

### 7.2 Token 管理

```python
class TokenManager:
    """Bearer Token 生命周期管理"""

    def __init__(self, auth_url, client_id, client_secret):
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = None
        self._refresh_token = None
        self._expires_at = None

    def get_token(self) -> str:
        if self._is_expired():
            if self._refresh_token:
                self._refresh()
            else:
                self._login()
        return self._access_token

    def _login(self):
        resp = httpx.post(self.auth_url, json={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        })
        self._update_tokens(resp.json())

    def _refresh(self):
        resp = httpx.post(self.auth_url, json={
            "grant_type": "refresh_token",
            "refresh_token": self._refresh_token,
        })
        self._update_tokens(resp.json())
```

---

## 8. 增量策略

API 拉取的增量同步依赖接口自身提供的查询参数：

| 增量方式 | 接口要求 | 参数示例 |
|---|---|---|
| 时间范围查询 | 接口支持 `startTime` / `endTime` 参数 | `{"startTime": "2026-07-07T00:00:00", "endTime": "2026-07-08T00:00:00"}` |
| 更新时间查询 | 接口支持 `modifyTime` 参数 | `{"modifyTime_gt": "2026-07-07T18:00:00"}` |
| ID 范围查询 | 接口支持 `id_gt` 参数 | `{"id_gt": 123456}` |

对于不支持增量查询的接口，只能执行**全量拉取 + hash 去重**。

---

## 9. 错误与异常处理

### 9.1 分页级错误

单个分页请求失败不阻塞整次同步：

```python
def fetch_all_pages_safe(self, endpoint, body, page_size):
    errors = []
    for page in range(1, max_pages or 999999):
        try:
            result = self.fetch_page(endpoint, body=body, page=page, page_size=page_size)
            yield from result.records
            if len(result.records) < page_size:
                break
        except Exception as e:
            errors.append({"page": page, "error": str(e)})
            continue  # 跳过此页，继续下一页
    if errors:
        raise PartialSyncError(errors)  # 最终汇总报告
```

### 9.2 响应结构变化

API 响应结构可能因版本升级而变化，处理策略：

1. 记录原始响应到 `raw_record.payload`（JSONB，不校验结构）
2. 如果配置了结构化映射 → 映射失败时记录错误，不崩溃
3. 管理台展示"字段映射异常"警告，提示人工检查

---

## 10. 作业编排

```text
1. 鉴权 → 获取/刷新 Token
2. 循环分页:
   2.1 令牌桶限流等待
   2.2 发送 HTTP 请求
   2.3 成功 → JSON 解析 → 逐行写入 raw_record
   2.4 限流 → 等待 Retry-After → 重试
   2.5 其他错误 → 指数退避重试 → 仍失败则跳过此页
3. 更新批次状态
4. 更新 last_sync_time（用于下次增量）
```

---

> **下一步**：[04-同步引擎技术实现](./04-同步引擎技术实现.md) — 研发落地细节。
