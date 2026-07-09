"""Connector 抽象基类。

对应策略文档：
- 02-数据库视图同步策略 §2
- 03-API拉取同步策略 §2
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterator


# ── 通用数据结构 ──────────────────────────────

@dataclass
class ColumnInfo:
    """源表字段信息。"""
    name: str
    data_type: str
    is_nullable: bool = True
    is_primary_key: bool = False
    max_length: int | None = None
    numeric_precision: int | None = None
    numeric_scale: int | None = None


@dataclass
class ApiPageResult:
    """API 分页查询结果。"""
    records: list[dict[str, Any]]
    total: int | None = None       # 总数（部分接口不返回）
    page: int = 1
    page_size: int = 100
    next_cursor: str | None = None  # 游标分页


# ── Connector 抽象基类 ─────────────────────────

class DatabaseConnector(ABC):
    """数据库连接器抽象基类。

    所有数据库连接器（SqlServer、MySQL、PostgreSQL）必须实现此接口。
    """

    @abstractmethod
    def connect(self) -> None:
        """建立数据库连接。"""
        ...

    @abstractmethod
    def disconnect(self) -> None:
        """关闭数据库连接。"""
        ...

    @abstractmethod
    def test_connection(self) -> bool:
        """测试连接是否可用。

        Returns:
            True 表示连接成功，False 表示失败。
        """
        ...

    @abstractmethod
    def fetch_table_list(self, schema: str = "dbo") -> list[str]:
        """获取指定 schema 下的所有表名。

        Args:
            schema: 数据库 schema 名称。

        Returns:
            表名列表。
        """
        ...

    @abstractmethod
    def fetch_schema(self, table_name: str) -> list[ColumnInfo]:
        """获取表的列信息。

        Args:
            table_name: 表名。

        Returns:
            列信息列表。
        """
        ...

    @abstractmethod
    def fetch_data(
        self,
        table_name: str,
        columns: list[str] | None = None,
        where_clause: str | None = None,
        order_by: str | None = None,
        offset: int = 0,
        limit: int = 10000,
    ) -> Iterator[dict[str, Any]]:
        """分页获取表数据。

        Args:
            table_name: 表名。
            columns: 要获取的列，None 表示全部。
            where_clause: WHERE 子句（不含 WHERE 关键字）。
            order_by: ORDER BY 子句。
            offset: 偏移量。
            limit: 每批行数。

        Yields:
            每行数据字典。
        """
        ...

    @abstractmethod
    def count_rows(self, table_name: str, where_clause: str | None = None) -> int:
        """统计行数。

        Args:
            table_name: 表名。
            where_clause: WHERE 子句。

        Returns:
            行数。
        """
        ...


class ApiConnector(ABC):
    """API 连接器抽象基类。

    所有 API 连接器必须实现此接口。
    """

    @abstractmethod
    def authenticate(self) -> None:
        """执行鉴权，获取并缓存 token。"""
        ...

    @abstractmethod
    def test_connection(self) -> bool:
        """测试连接是否可用。"""
        ...

    @abstractmethod
    def fetch_page(
        self,
        endpoint: str,
        method: str = "POST",
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
        page: int = 1,
        page_size: int = 100,
    ) -> ApiPageResult:
        """获取单页数据。

        Args:
            endpoint: 接口路径。
            method: HTTP 方法。
            params: URL 查询参数。
            body: 请求体。
            page: 页码。
            page_size: 每页数量。

        Returns:
            分页结果。
        """
        ...

    @abstractmethod
    def fetch_all_pages(
        self,
        endpoint: str,
        method: str = "POST",
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
        page_size: int = 100,
        max_pages: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """遍历所有分页数据。

        Args:
            endpoint: 接口路径。
            method: HTTP 方法。
            params: URL 查询参数。
            body: 请求体。
            page_size: 每页数量。
            max_pages: 最大页数限制。

        Yields:
            每条记录字典。
        """
        ...
