"""SQL Server 数据库连接器。

对应策略文档：02-数据库视图同步策略 §2。
"""

import hashlib
from typing import Any, Iterator

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from app.modules.ingestion.connectors.base import ColumnInfo, DatabaseConnector


class SqlServerConnector(DatabaseConnector):
    """SQL Server 连接器，基于 SQLAlchemy 同步引擎 + pyodbc。

    使用示例::

        connector = SqlServerConnector(
            host="192.168.1.100\\SQLEXPRESS",
            database="E10_3.0.0.2_CHS",
            username="readonly",
            password="xxx",
        )
        connector.connect()
        tables = connector.fetch_table_list()
        for table in tables:
            rows = connector.fetch_data(table, limit=5000)
            process(rows)
        connector.disconnect()
    """

    # SQL Server → PostgreSQL 类型映射
    TYPE_MAP: dict[str, str] = {
        "int": "INTEGER",
        "integer": "INTEGER",
        "bigint": "BIGINT",
        "smallint": "SMALLINT",
        "tinyint": "SMALLINT",
        "bit": "BOOLEAN",
        "decimal": "NUMERIC",
        "numeric": "NUMERIC",
        "float": "DOUBLE PRECISION",
        "real": "REAL",
        "money": "NUMERIC(19,4)",
        "smallmoney": "NUMERIC(19,4)",
        "datetime": "TIMESTAMP",
        "datetime2": "TIMESTAMP",
        "smalldatetime": "TIMESTAMP",
        "date": "DATE",
        "time": "TIME",
        "datetimeoffset": "TIMESTAMPTZ",
        "char": "CHAR",
        "varchar": "VARCHAR",
        "nvarchar": "VARCHAR",
        "nchar": "CHAR",
        "text": "TEXT",
        "ntext": "TEXT",
        "uniqueidentifier": "UUID",
        "varbinary": "BYTEA",
        "xml": "XML",
        "image": "BYTEA",
    }

    def __init__(
        self,
        host: str,
        database: str,
        username: str,
        password: str,
        port: int = 1433,
        driver: str = "ODBC Driver 17 for SQL Server",
        schema: str = "dbo",
        connect_timeout: int = 30,
        query_timeout: int = 300,
    ):
        """初始化 SQL Server 连接器。

        Args:
            host: 主机地址（如 "192.168.1.100\\SQLEXPRESS"）。
            database: 数据库名。
            username: 只读用户名。
            password: 密码。
            port: 端口，默认 1433。
            driver: ODBC 驱动名。
            schema: 默认 schema。
            connect_timeout: 连接超时秒数。
            query_timeout: 查询超时秒数。
        """
        self._host = host
        self._database = database
        self._username = username
        self._password = password
        self._port = port
        self._driver = driver
        self._schema = schema
        self._connect_timeout = connect_timeout
        self._query_timeout = query_timeout
        self._engine: Engine | None = None

    # ── 连接管理 ──────────────────────────────

    def connect(self) -> None:
        """建立 SQLAlchemy 同步引擎。"""
        conn_str = (
            f"mssql+pyodbc://{self._username}:{self._password}"
            f"@{self._host},{self._port}/{self._database}"
            f"?driver={self._driver.replace(' ', '+')}"
            f"&TrustServerCertificate=yes"
            f"&timeout={self._connect_timeout}"
        )
        self._engine = create_engine(
            conn_str,
            execution_options={"isolation_level": "READ UNCOMMITTED"},
            connect_args={"timeout": self._query_timeout},
            pool_pre_ping=True,
        )

    def disconnect(self) -> None:
        """关闭引擎连接池。"""
        if self._engine:
            self._engine.dispose()
            self._engine = None

    def test_connection(self) -> bool:
        """测试连接是否可用。"""
        try:
            self.connect()
            with self._engine.connect() as conn:  # type: ignore[union-attr]
                conn.execute(text("SELECT 1"))
            return True
        except Exception:
            return False
        finally:
            self.disconnect()

    # ── Schema 探测 ───────────────────────────

    def fetch_table_list(self, schema: str | None = None) -> list[str]:
        """获取指定 schema 下的所有用户表名。"""
        schema = schema or self._schema
        sql = text(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES "
            "WHERE TABLE_SCHEMA = :schema AND TABLE_TYPE = 'BASE TABLE' "
            "ORDER BY TABLE_NAME"
        )
        with self._engine.connect() as conn:  # type: ignore[union-attr]
            result = conn.execute(sql, {"schema": schema})
            return [row[0] for row in result]  # type: ignore[index]

    def fetch_schema(self, table_name: str) -> list[ColumnInfo]:
        """获取表的列信息。"""
        sql = text(
            "SELECT "
            "  COLUMN_NAME, DATA_TYPE, IS_NULLABLE, "
            "  CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE, "
            "  COLUMNPROPERTY(OBJECT_ID(TABLE_SCHEMA + '.' + TABLE_NAME), COLUMN_NAME, 'IsIdentity') AS IS_IDENTITY "
            "FROM INFORMATION_SCHEMA.COLUMNS "
            "WHERE TABLE_SCHEMA = :schema AND TABLE_NAME = :table "
            "ORDER BY ORDINAL_POSITION"
        )
        with self._engine.connect() as conn:  # type: ignore[union-attr]
            result = conn.execute(sql, {"schema": self._schema, "table": table_name})
            columns = []
            for row in result:
                col = ColumnInfo(
                    name=row.COLUMN_NAME,
                    data_type=row.DATA_TYPE,
                    is_nullable=row.IS_NULLABLE == "YES",
                    is_primary_key=bool(row.IS_IDENTITY),
                    max_length=row.CHARACTER_MAXIMUM_LENGTH,
                    numeric_precision=row.NUMERIC_PRECISION,
                    numeric_scale=row.NUMERIC_SCALE,
                )
                columns.append(col)
            return columns

    # ── 数据获取 ──────────────────────────────

    def fetch_data(
        self,
        table_name: str,
        columns: list[str] | None = None,
        where_clause: str | None = None,
        order_by: str | None = None,
        offset: int = 0,
        limit: int = 10000,
    ) -> Iterator[dict[str, Any]]:
        """分页获取表数据（使用 OFFSET...FETCH NEXT）。"""
        cols = ", ".join(f"[{c}]" for c in columns) if columns else "*"
        sql = f"SELECT {cols} FROM [{self._schema}].[{table_name}]"

        if where_clause:
            sql += f" WHERE {where_clause}"
        if order_by:
            sql += f" ORDER BY {order_by}"
        else:
            # 需要 ORDER BY 才能使用 OFFSET...FETCH
            sql += " ORDER BY (SELECT NULL)"

        sql += f" OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY"

        with self._engine.connect() as conn:  # type: ignore[union-attr]
            result = conn.execute(text(sql))
            # 将 Row 对象转为普通 dict
            keys = list(result.keys())
            for row in result:
                yield dict(zip(keys, row, strict=False))

    def count_rows(
        self, table_name: str, where_clause: str | None = None
    ) -> int:
        """统计行数。"""
        sql = f"SELECT COUNT(*) FROM [{self._schema}].[{table_name}]"
        if where_clause:
            sql += f" WHERE {where_clause}"

        with self._engine.connect() as conn:  # type: ignore[union-attr]
            result = conn.execute(text(sql))
            return result.scalar_one()

    # ── 工具方法 ──────────────────────────────

    def map_type_to_postgres(self, sqlserver_type: str) -> str:
        """将 SQL Server 类型映射为 PostgreSQL 类型。"""
        base_type = sqlserver_type.lower().split("(")[0].strip()
        return self.TYPE_MAP.get(base_type, "TEXT")

    @staticmethod
    def compute_row_hash(row: dict[str, Any]) -> str:
        """计算行数据的 SHA-256 hash（用于增量对比）。"""
        serialized = "|".join(
            f"{k}={v}" for k, v in sorted(row.items())
        )
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()[:16]
