"""ColumnMapper: maps API JSON response rows to physical table columns.

Rule: scalar values -> matching column, list/dict values -> JSONB column.
No type conversion at Raw layer — that's the Clean layer's job.
"""

import re


class ColumnMapper:
    """Maps a flat JSON dict to {columns: {...}, jsonb_cols: {...}}.

    Args:
        table_columns: set of snake_case column names known to exist
                       in the target table.
    """

    def __init__(self, table_columns: set[str]):
        self._table_columns = table_columns

    def map_row(self, row: dict) -> dict:
        """Convert one API response row.

        Returns:
            {"columns": {snake_col: value, ...},
             "jsonb_cols": {snake_col: value, ...}}
        """
        columns: dict = {}
        jsonb_cols: dict = {}
        for key, value in row.items():
            col_name = self._to_snake(key)
            if col_name in self._table_columns:
                columns[col_name] = value
            elif isinstance(value, (list, dict)):
                jsonb_cols[col_name] = value
            # scalar not in table columns → silently drop
            # (source API added new fields before DDL caught up)
        return {"columns": columns, "jsonb_cols": jsonb_cols}

    @staticmethod
    def _to_snake(camel: str) -> str:
        """camelCase / PascalCase → snake_case.

        Rules:
        - single word (all lowercase): passthrough
        - two-word: "workorderNo" → "workorder_no"
        - all-caps suffix: "simpleProcedureVOS" → "simple_procedures"
        - repeated capitals: "productSpecificationQtyVOS" → "product_specification_qties"

        Implemented via regex: insert '_' between a lowercase or digit
        and an uppercase letter, handle the "VOS" plural suffix, then
        apply standard English pluralization rules.
        """
        s1 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", camel)
        # handle consecutive capitals like HTMLParser → HTML_Parser
        s2 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s1)
        # "VOS" at the end is an abbreviation plural ("VOs") → replace with "s"
        if s2.endswith("_VOS"):
            s2 = s2[:-4] + "s"
        # English plural rule: consonant + "y" → "ies" (e.g. Qty → qties)
        s3 = re.sub(
            r"([bcdfghjklmnpqrstvwxyz])ys$",
            r"\1ies",
            s2,
        )
        return s3.lower()
