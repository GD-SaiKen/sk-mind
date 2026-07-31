"""YAML 语义模型 → SQL 查询翻译器。

ObjectQueryMapper: 将 object YAML definition → SELECT SQL
MetricQueryMapper: 将 metric YAML definition → 聚合 SQL
"""

from typing import Any, Optional


def _escape_ident(ident: str) -> str:
    """转义 PostgreSQL 标识符，防止注入。"""
    return '"' + ident.replace('"', '""') + '"'


class ObjectQueryMapper:
    """根据 object definition 构造 SELECT 查询。

    用法:
        mapper = ObjectQueryMapper(object_def)
        sql, params = mapper.build_query(
            filters={"machine_no": "MC-001"},
            order_by="event_time desc",
            limit=100,
        )
    """

    def __init__(self, object_def: dict):
        self._obj = object_def
        binding = (object_def.get("bindings") or [{}])[0]
        self._field_map: dict[str, str] = binding.get("field_map", {})
        self._tables = binding.get("tables", [{}])
        self._keys = object_def.get("keys", [])

    @property
    def from_clause(self) -> str:
        if not self._tables:
            return ""
        t = self._tables[0]
        schema = t.get("schema", "serving")
        table = t.get("table", "")
        return f"{_escape_ident(schema)}.{_escape_ident(table)}"

    def build_query(
        self,
        filters: dict[str, Any] | None = None,
        order_by: str | None = None,
        limit: int | None = None,
    ) -> tuple[str, dict[str, Any]]:
        """构造查询 SQL 和参数。

        Returns:
            (sql, params) — sql 使用 :param 占位符
        """
        select_cols = self._build_select()
        from_clause = self.from_clause
        where_clause, params = self._build_where(filters)
        order_clause = self._build_order(order_by)
        limit_clause = f"LIMIT {int(limit)}" if limit else ""

        sql = f"SELECT {select_cols} FROM {from_clause}"
        if where_clause:
            sql += f" WHERE {where_clause}"
        if order_clause:
            sql += f" ORDER BY {order_clause}"
        if limit_clause:
            sql += f" {limit_clause}"

        return sql, params

    def _build_select(self) -> str:
        cols = []
        for yaml_key, db_col in self._field_map.items():
            cols.append(f"{_escape_ident(db_col)} AS {_escape_ident(yaml_key)}")
        return ", ".join(cols) if cols else "*"

    def _build_where(
        self, filters: dict[str, Any] | None,
    ) -> tuple[str, dict[str, Any]]:
        if not filters:
            return "", {}

        clauses = []
        params: dict[str, Any] = {}
        for key, value in filters.items():
            db_col = self._field_map.get(key, key)
            param_name = f"p_{key}"
            clauses.append(f"{_escape_ident(db_col)} = :{param_name}")
            params[param_name] = value

        return " AND ".join(clauses), params

    def _build_order(self, order_by: str | None) -> str:
        if not order_by:
            return ""

        parts = order_by.strip().split()
        field = parts[0]
        direction = parts[1].upper() if len(parts) > 1 else "ASC"

        db_col = self._field_map.get(field, field)
        if direction not in ("ASC", "DESC"):
            direction = "ASC"

        return f"{_escape_ident(db_col)} {direction}"


class MetricQueryMapper:
    """根据 metric definition + object definition 构造聚合查询。

    v1 策略: 公式翻译通过 pattern matching 硬编码 19 个指标。
    v2 可迭代为通用公式解析器。

    用法:
        mapper = MetricQueryMapper(metric_def, object_def)
        sql, params = mapper.build_query(
            group_by=["machine_no"],
            dimensions=["shift"],
            filters={"machine_no": "MC-001"},
            limit=10,
        )
    """

    # v1 硬编码公式翻译表
    _FORMULA_MAP: dict[str, str] = {
        "andon_call_count":     "COUNT({table}.ar_id)",
        "andon_response_avg":   "AVG({table}.response_minutes)",
        "andon_processing_avg": "AVG({table}.processing_minutes)",
        "andon_timeout_rate":   "CAST(SUM(CASE WHEN {table}.is_response_timeout OR {table}.is_processing_timeout THEN 1 ELSE 0 END) AS DECIMAL) / NULLIF(COUNT(*), 0)",
        "oee_avg":              "AVG({table}.oee_rate)",
        "green_rate_avg":       "AVG({table}.green_rate)",
        "performance_rate_avg": "AVG({table}.performance_rate)",
        "low_efficiency_rate":  "CAST(SUM(CASE WHEN {table}.is_low_efficiency THEN 1 ELSE 0 END) AS DECIMAL) / NULLIF(COUNT(*), 0)",
        "fault_count_total":    "SUM(COALESCE({table}.fault_count, 0))",
        "total_production_qty": "SUM(COALESCE({table}.total_qty, 0))",
        "good_qty_sum":         "SUM(COALESCE({table}.good_qty, 0))",
        "yield_rate_avg":       "AVG({table}.yield_rate)",
        "bad_qty_sum":          "SUM(COALESCE({table}.bad_qty_manufacturing, 0) + COALESCE({table}.bad_qty_incoming, 0))",
        "empty_shift_count":    "SUM(CASE WHEN {table}.is_empty THEN 1 ELSE 0 END)",
        "machine_utilization_rate": "AVG({table}.utilization_rate)",
        "green_time_avg":       "AVG({table}.green_minutes)",
        "standard_complete_rate_avg": "AVG({table}.standard_complete_rate)",
        "schedule_completion_rate": "AVG({table}.completion_rate)",
        "schedule_pending_qty": "SUM(COALESCE({table}.pending_qty, 0))",
    }

    def __init__(self, metric_def: dict, object_def: dict):
        self._metric = metric_def
        self._obj = object_def
        binding = (object_def.get("bindings") or [{}])[0]
        self._field_map: dict[str, str] = binding.get("field_map", {})
        self._tables = binding.get("tables", [{}])

    @property
    def from_clause(self) -> str:
        if not self._tables:
            return ""
        t = self._tables[0]
        schema = t.get("schema", "serving")
        table = t.get("table", "")
        return f"{_escape_ident(schema)}.{_escape_ident(table)}"

    def build_query(
        self,
        group_by: list[str] | None = None,
        dimensions: list[str] | None = None,
        filters: dict[str, Any] | None = None,
        limit: int | None = None,
    ) -> tuple[str, dict[str, Any]]:
        metric_name = self._metric.get("metric", "unknown")
        formula = self._translate_formula(metric_name)

        table_alias = self._tables[0].get("table", "t") if self._tables else "t"
        table_ident = self.from_clause

        # Replace {table} placeholder in formula
        formula_sql = formula.replace("{table}", table_ident)

        # Build SELECT: metric_expr AS value + dimension cols
        select_parts = [f"{formula_sql} AS value"]

        # Group by: combine group_by + dimensions
        actual_group_by = (group_by or []) + (dimensions or [])
        group_cols_sql: list[str] = []
        for col in set(actual_group_by):
            db_col = self._field_map.get(col, col)
            select_parts.append(f"{_escape_ident(db_col)} AS {_escape_ident(col)}")
            group_cols_sql.append(_escape_ident(db_col))

        from_clause = f"{table_ident}"

        # WHERE
        where_clause, params = self._build_where(filters)

        sql = f"SELECT {', '.join(select_parts)} FROM {from_clause}"
        if where_clause:
            sql += f" WHERE {where_clause}"
        if group_cols_sql:
            sql += f" GROUP BY {', '.join(group_cols_sql)}"
        # ORDER BY value DESC to show top metrics first
        sql += " ORDER BY value DESC"
        if limit:
            sql += f" LIMIT {int(limit)}"

        return sql, params

    def _translate_formula(self, metric_name: str) -> str:
        """v1: hardcoded pattern matching. v2: general formula parser."""
        return self._FORMULA_MAP.get(metric_name, f"COUNT(*)")

    def _build_where(
        self, filters: dict[str, Any] | None,
    ) -> tuple[str, dict[str, Any]]:
        if not filters:
            return "", {}

        clauses = []
        params: dict[str, Any] = {}
        for key, value in filters.items():
            db_col = self._field_map.get(key, key)
            param_name = f"p_{key}"
            clauses.append(f"{_escape_ident(db_col)} = :{param_name}")
            params[param_name] = value

        return " AND ".join(clauses), params
