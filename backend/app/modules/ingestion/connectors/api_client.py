"""通用 HTTP API 连接器。

对应策略文档：03-API拉取同步策略 §2。
"""

import time
from typing import Any, Iterator

import httpx

from app.modules.ingestion.connectors.base import ApiConnector, ApiPageResult
from app.modules.ingestion.connectors.rate_limiter import TokenBucket
from app.modules.ingestion.connectors.token_manager import TokenManager


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
        self._default_headers = default_headers or {}

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

        self._client = httpx.Client(
            base_url=self._base_url,
            timeout=self._timeout,
            headers=headers,
            verify=self._ssl_verify,
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
        records = self._extract_nested(data, self._records_path) or []
        total = self._extract_nested(data, self._total_path)

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
        """带重试和限流的 HTTP 请求。"""
        last_exception: Exception | None = None

        for attempt in range(self._max_retries):
            if self._rate_limiter:
                self._rate_limiter.acquire()

            try:
                response = self._client.request(  # type: ignore[union-attr]
                    method=method,
                    url=url,
                    params=params,
                    json=json_data,
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

            except (httpx.TimeoutException, httpx.HTTPStatusError) as e:
                last_exception = e
                if attempt < self._max_retries - 1:
                    delay = self._retry_backoff ** attempt
                    time.sleep(delay)

        raise last_exception or RuntimeError("HTTP 请求失败")

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
