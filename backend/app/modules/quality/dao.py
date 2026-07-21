"""Quality 模块数据访问层。"""

import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.quality.models import QualityRule, QualityRun, QualityIssue


async def rule_list_all(
    db: AsyncSession,
    keyword: str | None = None,
    rule_type: str | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[QualityRule], int]:
    query = select(QualityRule)
    if keyword:
        query = query.filter(
            QualityRule.name.ilike(f"%{keyword}%")
            | QualityRule.code.ilike(f"%{keyword}%")
        )
    if rule_type:
        query = query.filter(QualityRule.rule_type == rule_type)
    if status == "enabled":
        query = query.filter(QualityRule.is_enabled.is_(True))
    elif status == "disabled":
        query = query.filter(QualityRule.is_enabled.is_(False))

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(QualityRule.updated_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def rule_get_by_id(db: AsyncSession, rule_id: uuid.UUID) -> QualityRule | None:
    return await db.get(QualityRule, rule_id)


async def rule_insert(db: AsyncSession, rule: QualityRule) -> QualityRule:
    db.add(rule)
    await db.flush()
    return rule


async def rule_update(db: AsyncSession, rule: QualityRule) -> QualityRule:
    await db.flush()
    return rule


async def run_list_all(
    db: AsyncSession,
    rule_id: uuid.UUID | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[QualityRun], int]:
    query = select(QualityRun)
    if rule_id:
        query = query.filter(QualityRun.rule_ids.ilike(f"%{rule_id}%"))

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(QualityRun.created_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def issue_list_all(
    db: AsyncSession,
    status: str | None = None,
    dataset_id: uuid.UUID | None = None,
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[QualityIssue], int]:
    query = select(QualityIssue)
    if status:
        query = query.filter(QualityIssue.status == status)
    if dataset_id:
        query = query.filter(QualityIssue.dataset_id == dataset_id)

    count_q = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_q)).scalar_one()

    query = query.order_by(QualityIssue.created_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    return list(result.scalars().all()), total


async def issue_get_by_id(
    db: AsyncSession, issue_id: uuid.UUID
) -> QualityIssue | None:
    return await db.get(QualityIssue, issue_id)


async def issue_update_status(
    db: AsyncSession, issue: QualityIssue, new_status: str
) -> QualityIssue:
    issue.status = new_status
    await db.flush()
    return issue
