"""Quality 模块路由层。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.quality import dao
from app.modules.quality.models import QualityRule, QualityRun
from app.modules.quality.schemas import (
    QualityIssueListResponse,
    QualityIssueResponse,
    QualityIssueStatusUpdate,
    QualityRuleCreate,
    QualityRuleListResponse,
    QualityRuleResponse,
    QualityRuleUpdate,
    QualityRunListResponse,
    QualityRunResponse,
    QualityStatsResponse,
)

router = APIRouter(prefix="/quality", tags=["quality"])

_DUMP_OPTS = {"by_alias": True}


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


@router.get("/rules")
async def list_rules(
    keyword: str | None = Query(None),
    type: str | None = Query(None),
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.rule_list_all(db, keyword, type, status, page, page_size)
    return _ok(
        QualityRuleListResponse(
            items=[QualityRuleResponse.model_validate(i) for i in items],
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("/rules", status_code=201)
async def create_rule(
    data: QualityRuleCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rule = QualityRule(**data.model_dump())
    rule = await dao.rule_insert(db, rule)
    return _ok(
        QualityRuleResponse.model_validate(rule).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.get("/rules/{rule_id}")
async def get_rule(
    rule_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rule = await dao.rule_get_by_id(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="质量规则不存在")
    return _ok(QualityRuleResponse.model_validate(rule).model_dump(**_DUMP_OPTS))


@router.put("/rules/{rule_id}")
async def update_rule(
    rule_id: uuid.UUID,
    data: QualityRuleUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rule = await dao.rule_get_by_id(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="质量规则不存在")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(rule, k, v)
    rule = await dao.rule_update(db, rule)
    return _ok(
        QualityRuleResponse.model_validate(rule).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.post("/rules/{rule_id}/execute")
async def execute_rule(
    rule_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rule = await dao.rule_get_by_id(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="质量规则不存在")
    return _ok(
        {"rule_id": str(rule_id), "status": "triggered"},
        msg="规则已触发执行",
    )


@router.get("/runs")
async def list_runs(
    rule_id: uuid.UUID | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.run_list_all(db, rule_id, page, page_size)
    return _ok(
        QualityRunListResponse(
            items=[QualityRunResponse.model_validate(i) for i in items],
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.get("/issues")
async def list_issues(
    status: str | None = Query(None),
    dataset_id: uuid.UUID | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.issue_list_all(db, status, dataset_id, page, page_size)
    return _ok(
        QualityIssueListResponse(
            items=[QualityIssueResponse.model_validate(i) for i in items],
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.put("/issues/{issue_id}/status")
async def update_issue_status(
    issue_id: uuid.UUID,
    data: QualityIssueStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    issue = await dao.issue_get_by_id(db, issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="质量问题不存在")
    issue = await dao.issue_update_status(db, issue, data.status)
    return _ok(
        QualityIssueResponse.model_validate(issue).model_dump(**_DUMP_OPTS),
        msg="状态更新成功",
    )


@router.get("/stats")
async def get_quality_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rules, _ = await dao.rule_list_all(db, page=1, page_size=1000)
    issues, _ = await dao.issue_list_all(db, status="open", page=1, page_size=1000)

    total_rules = len(rules)
    enabled_rules = sum(1 for r in rules if r.is_enabled)
    passed_count = 0
    warning_count = sum(1 for r in rules if r.severity == "warning")
    error_count = sum(1 for r in rules if r.severity in ("error", "critical"))
    pass_rate = (passed_count / total_rules * 100) if total_rules > 0 else 0.0
    open_issues = len(issues)

    return _ok(
        QualityStatsResponse(
            total_rules=total_rules,
            enabled_rules=enabled_rules,
            passed_count=passed_count,
            warning_count=warning_count,
            error_count=error_count,
            pass_rate=round(pass_rate, 1),
            open_issues=open_issues,
        ).model_dump(**_DUMP_OPTS)
    )
