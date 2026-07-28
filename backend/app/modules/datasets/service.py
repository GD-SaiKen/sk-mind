"""Dataset 模块服务层 — 业务编排逻辑。"""

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.datasets import dao
from app.modules.datasets.models import Dataset


async def check_agent_availability(
    db: AsyncSession, dataset: Dataset,
) -> dict:
    """Run T6 Agent availability checks and return result.

    Does NOT modify the dataset — only returns the check result.
    Caller decides whether to apply is_agent_accessible.
    """
    reasons: list[str] = []

    # Rule 1: dataset must be active
    if dataset.status != "active":
        reasons.append("数据集状态不是 active，当前为 {}".format(dataset.status))

    # Rule 2: field description coverage >= 50%
    coverage = await dao.get_field_description_coverage(db, dataset.id)
    if coverage < 0.5:
        reasons.append(
            "字段说明覆盖率仅 {:.0%}，需补充至 50% 以上".format(coverage)
        )

    # Rule 3: no unmarked high-sensitivity fields
    # (fields that are sensitive/high_sensitive with no description = not reviewed)
    sensitive_count = await dao.count_unmarked_sensitive_fields(db, dataset.id)
    if sensitive_count > 0:
        reasons.append(
            "{} 个敏感字段未标注".format(sensitive_count)
        )

    return {
        "passed": len(reasons) == 0,
        "reasons": reasons,
        "field_description_coverage": coverage,
        "unmarked_sensitive_count": sensitive_count,
    }


async def compute_null_rates_for_dataset(
    db: AsyncSession, dataset: Dataset,
) -> int:
    """Compute null_rate for all fields of a dataset by querying the physical table.

    Reads the DataTable record to get schema_name/table_name,
    then calls dao.compute_null_rates.
    """
    tables, _ = await dao.data_table_list_by_dataset(db, dataset.id)
    if not tables:
        return 0

    dt = tables[0]  # Use the primary data table
    return await dao.compute_null_rates(db, dt.schema_name, dt.table_name, dataset.id)
