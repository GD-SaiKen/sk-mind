"""通用 HTTP API 连接器。

对应策略文档：03-API拉取同步策略 §2。
"""

import threading
import time
from typing import Any, Iterator

import httpx

from app.modules.ingestion.connectors.base import ApiConnector, ApiPageResult
from app.modules.ingestion.connectors.rate_limiter import TokenBucket
from app.modules.ingestion.connectors.token_manager import TokenManager


class ApiBusinessError(RuntimeError):
    """API 返回 HTTP 200 但业务状态为失败（如 ``success=false``）。

    很多国产接口（含 MES lightmes）在参数非法、超出查询跨度限制等情况下
    仍返回 HTTP 200，仅在响应体里用 ``success=false`` + ``code``/``message``
    表达错误。若不显式检查，``data`` 字段为 null 会被当作“无数据”，导致
    同步批次被错误地标记为“成功 0 行”，真实错误被静默吞掉。
    """

    def __init__(self, message: str, code: Any = None, payload: Any = None):
        super().__init__(message)
        self.code = code
        self.payload = payload


class ApiHardTimeoutError(RuntimeError):
    """单次 HTTP 请求在硬性总时长上限内仍未完成（疑似服务端涓流挂死）。

    httpx 的 ``read`` 超时是「两次 recv 之间」的间隔，当服务端以极低速率
    持续吐字节（涓流）时该超时永不触发，导致请求无限挂起、Worker 线程冻结。
    本异常由硬性总超时守卫抛出，确保任何单请求都有可预期的上界，并进入
    重试/失败流程而不是永久卡死。
    """

    def __init__(self, message: str, budget: float | None = None):
        super().__init__(message)
        self.budget = budget


class HttpxApiConnector(ApiConnector):
    """基于 httpx 的通用 API 连接器。

    使用示例::

        connector = HttpxApiConnector(
            base_url="https://mes.example.com",
            auth_type="bearer",
            auth_credentials="your-token",
            qps_limit=10,
        )
        connector.connect()
        for record in connector.fetch_all_pages("/api/workorders", body={"teamId": "xxx"}):
            process(record)
        connector.disconnect()
    """

    def __init__(
        self,
        base_url: str,
        auth_type: str = "none",         # none / bearer / basic / api_key / dual_key / session
        auth_credentials: str | None = None,
        auth_header_name: str = "Authorization",
        auth_token_prefix: str = "Bearer",
        auth_url: str | None = None,
        auth_credentials_map: dict[str, str] | None = None,
        auth_credentials_2: str | None = None,
        auth_header_name_2: str = "",
        qps_limit: int = 10,
        timeout: int = 30,
        max_retries: int = 3,
        retry_backoff: float = 1.5,
        records_path: str = "data.list",
        total_path: str = "data.total",
        default_headers: dict[str, str] | None = None,
        ssl_verify: bool = True,
        proxy: str | None = None,
        total_timeout: int = 180,
    ):
        """初始化 API 连接器。

        Args:
            base_url: API 基础 URL。
            auth_type: 鉴权类型。
            auth_credentials: Bearer token 或 API Key（静态凭据）。
            auth_header_name: 鉴权 Header 名。
            auth_token_prefix: token 前缀（如 "Bearer"）。
            auth_url: 动态登录鉴权的 URL（session 模式）。
            auth_credentials_map: 动态登录的凭据。
            auth_credentials_2: 第二凭据（dual_key 模式的第二个 Header 值）。
            auth_header_name_2: 第二鉴权 Header 名（dual_key 模式）。
            qps_limit: QPS 上限。
            timeout: 请求超时秒数。
            max_retries: 最大重试次数。
            retry_backoff: 退避因子。
            records_path: 响应 JSON 中记录列表的路径（如 "data.list"）。
            total_path: 响应 JSON 中总数的路径。
            default_headers: 默认请求头。
            ssl_verify: 是否验证 SSL 证书（自签名证书场景设为 False）。
            proxy: 代理地址。默认为 None，即**不使用任何代理**（显式绕过系统
                HTTPS_PROXY/HTTP_PROXY 环境变量）。数据同步 Worker 连的是企业内网/
                云 MES/ERP，不应走开发者的个人代理；若某数据源确实需要代理，
                在 YAML connection 中设置 ``proxy: "http://host:port"`` 即可。
            total_timeout: 单次 HTTP 请求的**硬性总时长上限**（秒）。即使服务端
                以涓流方式持续吐字节导致 ``read`` 超时永不触发，超过此上限也会
                强制抛 ``ApiHardTimeoutError``，防止 Worker 线程无限冻结。
        """
        self._base_url = base_url.rstrip("/")
        self._ssl_verify = ssl_verify
        self._auth_type = auth_type
        self._auth_credentials = auth_credentials
        self._auth_header_name = auth_header_name
        self._auth_token_prefix = auth_token_prefix
        self._auth_url = auth_url
        self._auth_credentials_map = auth_credentials_map
        self._auth_credentials_2 = auth_credentials_2
        self._auth_header_name_2 = auth_header_name_2
        self._qps_limit = qps_limit
        self._timeout = timeout
        self._max_retries = max_retries
        self._retry_backoff = retry_backoff
        self._records_path = records_path
        self._total_path = total_path
        # 最近一次 fetch_page 的 total（来自 total_path），供对账 L1 读取
        self.last_total: int | None = None
        self._default_headers = default_headers or {}
        self._proxy = proxy
        # 单次请求硬性总时长上限（秒）。防止服务端涓流导致 read 超时永不触发、
        # 进而 Worker 永久冻结。默认 180s：远大于正常 30s 读超时，仅在真正异常时兜底。
        self._total_timeout = total_timeout

        self._client: httpx.Client | None = None
        self._rate_limiter: TokenBucket | None = None
        self._token_manager: TokenManager | None = None

        if auth_type == "session" and auth_url and auth_credentials_map:
            self._token_manager = TokenManager(
                auth_url=auth_url,
                credentials=auth_credentials_map,
            )

    # ── 连接管理 ──────────────────────────────

    def connect(self) -> None:
        """建立 HTTP 客户端并初始化限流器。"""
        headers = {**self._default_headers}

        if self._auth_type == "bearer" and self._auth_credentials:
            headers[self._auth_header_name] = (
                f"{self._auth_token_prefix} {self._auth_credentials}"
            )
        elif self._auth_type == "basic" and self._auth_credentials:
            headers[self._auth_header_name] = f"Basic {self._auth_credentials}"
        elif self._auth_type == "api_key" and self._auth_credentials:
            headers[self._auth_header_name] = self._auth_credentials
        elif self._auth_type == "dual_key" and self._auth_credentials and self._auth_credentials_2:
            headers[self._auth_header_name] = self._auth_credentials
            headers[self._auth_header_name_2] = self._auth_credentials_2
        elif self._auth_type == "session" and self._token_manager:
            token = self._token_manager.get_token()
            headers[self._auth_header_name] = (
                f"{self._auth_token_prefix} {token}"
            )

        # 显式分段超时：connect/read/write/pool 分别设定。
        # 注意 read 超时是「两次 recv 之间」的间隔，服务端涓流时不会触发，
        # 真正的无限挂死兜底由 _request_with_hard_timeout 的硬性总时长守卫负责。
        _timeout = httpx.Timeout(
            connect=10,
            read=max(30, int(self._timeout)),
            write=10,
            pool=10,
        )
        self._client = httpx.Client(
            base_url=self._base_url,
            timeout=_timeout,
            headers=headers,
            verify=self._ssl_verify,
            proxy=self._proxy,
        )
        self._rate_limiter = TokenBucket(rate=self._qps_limit)

    def disconnect(self) -> None:
        """关闭 HTTP 客户端。"""
        if self._client:
            self._client.close()
            self._client = None
        if self._token_manager:
            self._token_manager.close()
            self._token_manager = None

    def test_connection(self) -> bool:
        """测试连接 — 发送一个最小请求验证连通性。"""
        try:
            self.connect()
            return True
        except Exception:
            return False
        finally:
            self.disconnect()

    def authenticate(self) -> None:
        """执行鉴权（session 模式下由 TokenManager 自动处理）。"""
        if self._token_manager:
            self._token_manager.get_token()

    # ── 数据获取 ──────────────────────────────

    def fetch_page(
        self,
        endpoint: str,
        method: str = "POST",
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
        page: int = 1,
        page_size: int = 100,
    ) -> ApiPageResult:
        """获取单页数据。"""
        if self._client is None:
            raise RuntimeError("Connector 未连接，请先调用 connect()")
        if self._rate_limiter is None:
            raise RuntimeError("限流器未初始化")

        # session 模式每次请求前刷新 token
        if self._auth_type == "session" and self._token_manager:
            token = self._token_manager.get_token()
            self._client.headers[self._auth_header_name] = (
                f"{self._auth_token_prefix} {token}"
            )

        # Detect pagination key naming: MES uses pageNum, generic APIs use page
        page_key = "pageNum" if (body and "pageNum" in body) else "page"
        payload = {**(body or {}), page_key: page, "pageSize": page_size}

        response = self._request_with_retry(
            method=method,
            url=endpoint,
            params=params,
            json_data=payload,
        )

        data = response.json()

        # 业务状态校验：HTTP 200 不代表业务成功。若响应体显式带 success=false，
        # 必须抛错让批次标记为“失败”，而不是把 data=null 误判为“无数据成功”。
        # 仅在响应确实包含 success 字段时校验 —— 对无该字段的 API 零影响。
        if isinstance(data, dict) and "success" in data and not data["success"]:
            raise ApiBusinessError(
                f"API 业务错误: {data.get('message') or '未知错误'} "
                f"(code={data.get('code')}, endpoint={endpoint})",
                code=data.get("code"),
                payload=data,
            )

        records = self._extract_nested(data, self._records_path) or []
        total = self._extract_nested(data, self._total_path)
        # 记录本页 total，供对账 L1 读取（total_path 总量在各页一致）。
        # 兼容 total 以字符串返回的场景（如 "8368"），统一规整为 int。
        try:
            self.last_total = int(total) if total is not None else None
        except (ValueError, TypeError):
            self.last_total = None

        return ApiPageResult(
            records=records if isinstance(records, list) else [],
            total=total if isinstance(total, int) else None,
            page=page,
            page_size=page_size,
        )

    def fetch_all_pages(
        self,
        endpoint: str,
        method: str = "POST",
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
        page_size: int = 100,
        max_pages: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """遍历所有分页数据。"""
        page = 1
        while True:
            if max_pages and page > max_pages:
                break

            result = self.fetch_page(
                endpoint, method, params, body, page, page_size
            )
            yield from result.records

            if len(result.records) < page_size:
                break
            page += 1

    # ── 内部方法 ──────────────────────────────

    def _request_with_retry(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """带重试和限流的 HTTP 请求。

        捕获 httpx 的全部超时（TimeoutException）与传输层/网络异常
        （TransportError 涵盖 ConnectError / ReadError / RemoteProtocolError /
        ProtocolError / NetworkError 等），以及本连接器自有的硬性总超时
        （ApiHardTimeoutError）。这些异常都会触发退避重试；超过最大重试次数后
        向上抛出，由调用方标记批次失败。业务错误（ApiBusinessError）不在此捕获，
        会立即穿透，避免把 ``success=false`` 误判为无数据成功。
        """
        last_exception: Exception | None = None

        for attempt in range(self._max_retries):
            if self._rate_limiter:
                self._rate_limiter.acquire()

            try:
                response = self._request_with_hard_timeout(
                    method=method,
                    url=url,
                    params=params,
                    json_data=json_data,
                )

                # 限流重试
                if response.status_code == 429:
                    retry_after = int(
                        response.headers.get("Retry-After", 5)
                    )
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()
                return response

            except (
                httpx.TimeoutException,
                httpx.TransportError,
                ApiHardTimeoutError,
            ) as e:
                last_exception = e
                if attempt < self._max_retries - 1:
                    delay = self._retry_backoff ** attempt
                    time.sleep(delay)

        raise last_exception or RuntimeError("HTTP 请求失败")

    def _request_with_hard_timeout(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """在硬性总时长上限内执行单次阻塞请求，超时即抛 ``ApiHardTimeoutError``。

        实现：在守护线程中发起阻塞的 ``client.request``，主线程 ``join(total)``。
        超时则关闭并丢弃当前 client（杀掉挂死的底层 socket），强制下次重试时
        ``connect()`` 重建连接；被卡线程为守护线程，不会阻止进程退出。
        请求体在子线程内先 ``read()`` 完整缓冲，避免跨线程复用 client 的隐患。
        """
        if self._client is None:
            self.connect()

        result_holder: list[httpx.Response] = []
        error_holder: list[BaseException] = []

        def _blocking() -> None:
            try:
                resp = self._client.request(  # type: ignore[union-attr]
                    method=method,
                    url=url,
                    params=params,
                    json=json_data,
                )
                resp.read()  # 在子线程内完整缓冲响应体，主线程再 .json() 安全
                result_holder.append(resp)
            except BaseException as exc:  # noqa: BLE001 - 跨线程传递异常
                error_holder.append(exc)

        worker = threading.Thread(target=_blocking, daemon=True)
        worker.start()
        worker.join(timeout=self._total_timeout)

        if worker.is_alive():
            # 硬性超时：服务端涓流/挂死，强制丢弃当前 client 以释放底层 socket。
            try:
                self._client.close()
            except Exception:
                pass
            self._client = None
            raise ApiHardTimeoutError(
                f"请求在 {self._total_timeout}s 内未完成（疑似服务端无响应/涓流挂死），"
                f"endpoint={url}",
                budget=self._total_timeout,
            )

        if error_holder:
            raise error_holder[0]
        return result_holder[0]

    @staticmethod
    def _extract_nested(data: dict, path: str) -> Any:
        """从嵌套字典中按点分隔路径提取值。

        Example:
            _extract_nested({"data": {"list": [1,2]}}, "data.list") → [1,2]
        """
        keys = path.split(".")
        current: Any = data
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key)
            else:
                return None
        return current
