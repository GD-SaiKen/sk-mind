"""数据浏览 API — raw 表列表 + 抽样查询。"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User

router = APIRouter(prefix="/data-browse", tags=["data-browse"])


@router.get("/tables")
async def list_tables(
    schema: str = Query("raw"),
    system: str = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """列出 raw schema 下的表及行数。"""
    sql = text(
        "SELECT t.table_name,"
        "  (SELECT count(*) FROM information_schema.columns WHERE table_schema='raw' AND table_name=t.table_name) as col_count"
        " FROM information_schema.tables t"
        " WHERE t.table_schema = :schema"
    )
    if system:
        sql = text(
            "SELECT t.table_name,"
            "  (SELECT count(*) FROM information_schema.columns WHERE table_schema=:schema AND table_name=t.table_name) as col_count"
            " FROM information_schema.tables t"
            " WHERE t.table_schema = :schema AND t.table_name LIKE :pat"
        )
    result = await db.execute(
        sql, {"schema": schema, "pat": f"{system}_%"} if system else {"schema": schema}
    )
    tables = []
    for row in result:
        table_name = row.table_name
        # Get count
        count_result = await db.execute(text(f"SELECT count(*) FROM {schema}.{table_name}"))
        count = count_result.scalar_one()
        tables.append({"table_name": table_name, "row_count": count})
    return {"code": 0, "message": "success", "msg": "OK", "data": tables}


@router.get("/sample")
async def get_sample(
    table: str = Query(...),
    limit: int = Query(20, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """获取指定表的抽样数据（仅 payload 展开）。"""
    schema, tbl = table.split(".", 1) if "." in table else ("raw", table)
    try:
        result = await db.execute(
            text(f"SELECT payload FROM {schema}.{tbl} ORDER BY _ingested_at DESC LIMIT :lim")
        )
        rows = []
        for row in result:
            payload = row.payload
            if isinstance(payload, str):
                import json
                payload = json.loads(payload)
            rows.append(payload)
        return {"code": 0, "message": "success", "msg": "OK", "data": rows}
    except Exception as e:
        return {"code": 0, "message": "success", "msg": "OK", "data": [], "error": str(e)}
