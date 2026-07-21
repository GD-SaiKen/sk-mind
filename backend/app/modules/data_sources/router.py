"""DataSource 模块路由层。"""

import uuid
from pathlib import Path

import yaml
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.data_sources import dao
from app.modules.data_sources.service import check_connection
from app.modules.data_sources.models import DataSource
from app.modules.data_sources.schemas import (
    DataSourceCreate,
    DataSourceListResponse,
    DataSourceResponse,
    DataSourceUpdate,
    InterfaceItem,
)

router = APIRouter(prefix="/data-sources", tags=["data-sources"])

_DUMP_OPTS = {"by_alias": True}

# Path to data source YAML configs
_CONFIG_DIR = Path(__file__).resolve().parents[3] / "config" / "data_sources"


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


@router.get("")
async def list_sources(
    keyword: str | None = Query(None),
    source_type: str | None = Query(None),
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.list_all(db, keyword, source_type, status, page, page_size)
    return _ok(DataSourceListResponse(
        items=[DataSourceResponse.model_validate(i) for i in items],
        total=total,
    ).model_dump(**_DUMP_OPTS))


@router.post("", status_code=201)
async def create_source(
    data: DataSourceCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = DataSource(**data.model_dump())
    ds = await dao.insert(db, ds)
    return _ok(DataSourceResponse.model_validate(ds).model_dump(**_DUMP_OPTS), msg="创建成功")


@router.get("/{ds_id}")
async def get_source(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据源不存在")
    return _ok(DataSourceResponse.model_validate(ds).model_dump(**_DUMP_OPTS))


@router.put("/{ds_id}")
async def update_source(
    ds_id: uuid.UUID,
    data: DataSourceUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据源不存在")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(ds, k, v)
    ds = await dao.update(db, ds)
    return _ok(DataSourceResponse.model_validate(ds).model_dump(**_DUMP_OPTS), msg="更新成功")




@router.post("/{ds_id}/check-connection")
async def check_source_connection(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Manually trigger DataSource connectivity health check."""
    result = await check_connection(ds_id, db)
    return _ok(result)


@router.delete("/{ds_id}")
async def delete_source(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ds = await dao.get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据源不存在")
    ds.status = "archived"
    await dao.update(db, ds)
    return _ok(msg="已归档")


@router.get("/{ds_id}/interfaces")
async def list_interfaces(
    ds_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return the list of API interfaces for a data source.

    Loads from config/data_sources/{code}.yaml based on the source's code.
    Returns interface name, endpoint, method, target table, and metadata.
    """
    ds = await dao.get_by_id(db, ds_id)
    if not ds:
        raise HTTPException(status_code=404, detail="数据源不存在")

    # Find matching YAML config by source code
    config_file = _CONFIG_DIR / f"{ds.code}.yaml"
    if not config_file.exists():
        # Try glob match — code might differ from filename
        matches = list(_CONFIG_DIR.glob(f"{ds.code}*.yaml"))
        if not matches:
            return _ok([])
        config_file = matches[0]

    try:
        with open(config_file, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except Exception:
        return _ok([])

    interfaces = []
    for idx, iface in enumerate(cfg.get("interfaces", []), 1):
        interfaces.append(InterfaceItem(
            name=iface.get("name", ""),
            endpoint=iface.get("endpoint", ""),
            method=iface.get("method", "POST"),
            target_table=iface.get("target_table", ""),
            order=idx,
            is_time_based=iface.get("time_config", {}).get("is_time_based", True),
            pk_fields=iface.get("pk_fields", []),
        ).model_dump(**_DUMP_OPTS))

    return _ok(interfaces)
