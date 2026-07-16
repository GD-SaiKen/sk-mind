"""Validator: pre-write row-level validation with L1 (reject) and L2 (warn) tiers.

L1 structural checks (REJECT): field existence, primary key non-null, basic type parsability.
L2 content checks (WARN): empty values, format mismatches, enum range, duplicates.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional
import re


class ValidationLevel(str, Enum):
    PASS = "pass"
    WARN = "warn"
    REJECT = "reject"


@dataclass
class ValidationResult:
    level: ValidationLevel
    row: dict
    quality_flags: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    mapped_row: dict = field(default_factory=dict)


@dataclass
class ColumnRule:
    """Validation rule for a single column."""

    source_column: str
    target_column: str = ""

    # L1 rules
    required: bool = False
    expected_type: str = "auto"
    # "string" | "int" | "float" | "date" | "datetime" | "bool" | "auto"
    is_unique_key: bool = False

    # L2 rules
    format_pattern: Optional[str] = None
    allowed_values: Optional[list] = None

    def __post_init__(self):
        if not self.target_column:
            self.target_column = self.source_column


class Validator:
    """Per-row validator with L1 reject / L2 warn tier."""

    def __init__(self, rules: list[ColumnRule]):
        self._rules = rules
        self._rule_map = {r.source_column: r for r in rules}
        self._unique_keys_seen: set[str] = set()

    def validate(self, row: dict) -> ValidationResult:
        """Validate a single row.

        Returns:
            ValidationResult with level=PASS/WARN/REJECT.
            L1 failures produce REJECT (row blocked from raw).
            L2 failures produce WARN (row enters raw with quality_flags).
        """
        result = ValidationResult(level=ValidationLevel.PASS, row=row, mapped_row={})

        for rule in self._rules:
            value = row.get(rule.source_column)

            # --- L1: field existence ---
            if rule.source_column not in row:
                # Missing column: only a problem if required
                if rule.required:
                    result.errors.append(f"missing required column: {rule.source_column}")
                    result.level = ValidationLevel.REJECT
                continue

            # --- L1: primary key non-null ---
            if rule.is_unique_key and (value is None or str(value).strip() == ""):
                result.errors.append(f"primary key {rule.source_column} is null")
                result.level = ValidationLevel.REJECT
                result.mapped_row[rule.target_column] = value
                continue

            # --- L1: basic type parsability ---
            if value is not None and rule.expected_type != "auto":
                parsed, type_err = self._check_type(value, rule.expected_type)
                if type_err:
                    result.errors.append(
                        f"type mismatch on {rule.source_column}: {type_err}"
                    )
                    result.level = ValidationLevel.REJECT
                    result.mapped_row[rule.target_column] = value
                    continue

            # --- L2: empty required value ---
            if rule.required and (value is None or str(value).strip() == ""):
                flag = f"empty_required:{rule.source_column}"
                result.quality_flags.append(flag)
                if result.level == ValidationLevel.PASS:
                    result.level = ValidationLevel.WARN

            # --- L2: format pattern ---
            if rule.format_pattern and value is not None:
                try:
                    if not re.match(rule.format_pattern, str(value)):
                        flag = f"format_mismatch:{rule.source_column}"
                        result.quality_flags.append(flag)
                        if result.level == ValidationLevel.PASS:
                            result.level = ValidationLevel.WARN
                except re.error:
                    pass

            # --- L2: enum range ---
            if rule.allowed_values and value is not None:
                if value not in rule.allowed_values:
                    flag = f"out_of_range:{rule.source_column}"
                    result.quality_flags.append(flag)
                    if result.level == ValidationLevel.PASS:
                        result.level = ValidationLevel.WARN

            # --- L2: unique key duplicate detection ---
            if rule.is_unique_key and value is not None:
                key = f"{rule.source_column}:{value}"
                if key in self._unique_keys_seen:
                    flag = f"duplicate_key:{rule.source_column}"
                    result.quality_flags.append(flag)
                    if result.level == ValidationLevel.PASS:
                        result.level = ValidationLevel.WARN
                else:
                    self._unique_keys_seen.add(key)

            result.mapped_row[rule.target_column] = value

        return result

    def _check_type(self, value: Any, expected_type: str) -> tuple[Any, Optional[str]]:
        """Check if value can be parsed as expected_type. Returns (parsed, error)."""
        try:
            if expected_type == "int":
                return int(value), None
            elif expected_type == "float":
                return float(value), None
            elif expected_type == "bool":
                if isinstance(value, bool):
                    return value, None
                if str(value).lower() in ("true", "1", "yes"):
                    return True, None
                if str(value).lower() in ("false", "0", "no"):
                    return False, None
                return None, f"cannot parse '{value}' as bool"
            elif expected_type in ("date", "datetime"):
                from datetime import datetime as dt
                if isinstance(value, dt):
                    return value, None
                # Try common formats
                for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
                    try:
                        return dt.strptime(str(value)[:19], fmt), None
                    except ValueError:
                        continue
                return None, f"cannot parse '{value}' as date/datetime"
            else:
                return str(value), None
        except (ValueError, TypeError) as e:
            return None, str(e)
