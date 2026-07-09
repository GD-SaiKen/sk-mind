"""Token 生命周期管理。

对应策略文档：03-API拉取同步策略 §7。
"""

import time
from dataclasses import dataclass

import httpx


@dataclass
class TokenInfo:
    """鉴权 token 信息。"""
    access_token: str
    refresh_token: str | None = None
    expires_at: float = 0.0      # Unix 时间戳


class TokenManager:
    """Bearer Token 生命周期管理。

    使用示例::

        manager = TokenManager(
            auth_url="https://api.example.com/auth/login",
            credentials={"username": "admin", "password": "xxx"},
        )
        token = manager.get_token()  # 自动刷新过期 token
    """

    def __init__(
        self,
        auth_url: str,
        credentials: dict[str, str],
        token_path: str = "access_token",
        refresh_path: str = "refresh_token",
        expires_in_path: str = "expires_in",
        auth_method: str = "POST",
    ):
        """初始化 TokenManager。

        Args:
            auth_url: 鉴权接口 URL。
            credentials: 鉴权凭据（发送到 auth_url 的 JSON body）。
            token_path: 响应中 access_token 的 JSON 路径。
            refresh_path: 响应中 refresh_token 的 JSON 路径。
            expires_in_path: 响应中过期秒数的 JSON 路径。
            auth_method: 鉴权接口的 HTTP 方法。
        """
        self._auth_url = auth_url
        self._credentials = credentials
        self._token_path = token_path
        self._refresh_path = refresh_path
        self._expires_in_path = expires_in_path
        self._auth_method = auth_method
        self._token_info: TokenInfo | None = None
        self._client = httpx.Client(timeout=30.0)

    def get_token(self) -> str:
        """获取有效 token，自动刷新过期 token。"""
        if self._token_info is None:
            self._login()
        elif self._is_expired():
            if self._token_info.refresh_token:
                self._refresh()
            else:
                self._login()
        return self._token_info.access_token  # type: ignore[union-attr]

    def _is_expired(self) -> bool:
        """检查当前 token 是否过期（提前 60 秒刷新）。"""
        if self._token_info is None:
            return True
        return time.time() > (self._token_info.expires_at - 60)

    def _login(self) -> None:
        """登录获取新 token。"""
        resp = self._client.request(
            self._auth_method,
            self._auth_url,
            json=self._credentials,
        )
        resp.raise_for_status()
        data = resp.json()
        self._update_tokens(data)

    def _refresh(self) -> None:
        """使用 refresh_token 刷新 access_token。"""
        resp = self._client.request(
            self._auth_method,
            self._auth_url,
            json={"refresh_token": self._token_info.refresh_token},
        )
        resp.raise_for_status()
        data = resp.json()
        self._update_tokens(data)

    def _update_tokens(self, data: dict) -> None:
        """从响应中提取并缓存 token 信息。"""
        expires_in = data.get(self._expires_in_path, 3600)
        self._token_info = TokenInfo(
            access_token=data[self._token_path],
            refresh_token=data.get(self._refresh_path),
            expires_at=time.time() + expires_in,
        )

    def close(self) -> None:
        """关闭 HTTP 客户端。"""
        self._client.close()
