"""语义模型路由层。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import exc as sa_exc
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.semantic import dao
from app.modules.semantic.models import SemanticObject, SemanticProperty, DataMapping
from app.modules.semantic.schemas import (
    DataMappingCreate,
    DataMappingListResponse,
    DataMappingResponse,
    DataMappingUpdate,
    SemanticObjectCreate,
    SemanticObjectListResponse,
    SemanticObjectResponse,
    SemanticObjectUpdate,
    SemanticPropertyCreate,
    SemanticPropertyListResponse,
    SemanticPropertyResponse,
    SemanticPropertyUpdate,
    SemanticStatsResponse,
)

router = APIRouter(prefix="/semantic", tags=["semantic"])

_DUMP_OPTS = {"by_alias": True}


def _ok(data=None, msg="OK"):
    return {"code": 0, "message": "success", "msg": msg, "data": data}


# ═══════════════════════════════════════
# SemanticObject CRUD
# ═══════════════════════════════════════

@router.get("/objects")
async def list_objects(
    keyword: str | None = Query(None),
    object_type: str | None = Query(None, alias="objectType"),
    domain: str | None = Query(None),
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.semantic_object_list(
        db,
        keyword=keyword,
        object_type=object_type,
        domain=domain,
        status=status,
        page=page,
        page_size=page_size,
    )

    # Collect object IDs to get property/mapping counts
    obj_ids = [o.id for o in items]
    prop_counts: dict[uuid.UUID, int] = {}
    map_counts: dict[uuid.UUID, int] = {}
    if obj_ids:
        import sqlalchemy as sa
        from sqlalchemy import func, select as sa_select

        # Property counts
        prop_q = await db.execute(
            sa_select(
                SemanticProperty.semantic_object_id,
                func.count(SemanticProperty.id),
            )
            .where(SemanticProperty.semantic_object_id.in_(obj_ids))
            .group_by(SemanticProperty.semantic_object_id)
        )
        prop_counts = {row[0]: row[1] for row in prop_q}

        # Mapping counts
        map_q = await db.execute(
            sa_select(
                DataMapping.semantic_object_id,
                func.count(DataMapping.id),
            )
            .where(DataMapping.semantic_object_id.in_(obj_ids))
            .group_by(DataMapping.semantic_object_id)
        )
        map_counts = {row[0]: row[1] for row in map_q}

    response_items = []
    for obj in items:
        d = SemanticObjectResponse.model_validate(obj)
        d.property_count = prop_counts.get(obj.id, 0)
        d.mapping_count = map_counts.get(obj.id, 0)
        response_items.append(d)

    return _ok(
        SemanticObjectListResponse(
            items=response_items,
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("/objects", status_code=201)
async def create_object(
    data: SemanticObjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    obj = SemanticObject(**data.model_dump())
    try:
        obj = await dao.semantic_object_insert(db, obj)
    except sa_exc.IntegrityError:
        raise HTTPException(status_code=409, detail="业务对象名称或代码已存在")
    return _ok(
        SemanticObjectResponse.model_validate(obj).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.get("/objects/{object_id}")
async def get_object(
    object_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    obj = await dao.semantic_object_get_by_id(db, object_id)
    if not obj:
        raise HTTPException(status_code=404, detail="业务对象不存在")
    return _ok(SemanticObjectResponse.model_validate(obj).model_dump(**_DUMP_OPTS))


@router.put("/objects/{object_id}")
async def update_object(
    object_id: uuid.UUID,
    data: SemanticObjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    obj = await dao.semantic_object_get_by_id(db, object_id)
    if not obj:
        raise HTTPException(status_code=404, detail="业务对象不存在")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    obj = await dao.semantic_object_update(db, obj)
    return _ok(
        SemanticObjectResponse.model_validate(obj).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.delete("/objects/{object_id}")
async def delete_object(
    object_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    obj = await dao.semantic_object_get_by_id(db, object_id)
    if not obj:
        raise HTTPException(status_code=404, detail="业务对象不存在")
    obj.status = "archived"
    await dao.semantic_object_update(db, obj)
    return _ok(msg="已归档")


# ═══════════════════════════════════════
# SemanticProperty CRUD
# ═══════════════════════════════════════

@router.get("/properties")
async def list_properties(
    semantic_object_id: uuid.UUID | None = Query(None, alias="semanticObjectId"),
    property_type: str | None = Query(None, alias="propertyType"),
    page: int | None = Query(None, ge=1),
    page_size: int | None = Query(None, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.semantic_property_list(
        db,
        semantic_object_id=semantic_object_id,
        property_type=property_type,
        page=page,
        page_size=page_size,
    )
    resp_items = [SemanticPropertyResponse(**item) for item in items]
    return _ok(
        SemanticPropertyListResponse(
            items=resp_items,
            total=total,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("/properties", status_code=201)
async def create_property(
    data: SemanticPropertyCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Verify parent object exists
    parent = await dao.semantic_object_get_by_id(db, data.semantic_object_id)
    if not parent:
        raise HTTPException(status_code=404, detail="所属业务对象不存在")

    prop = SemanticProperty(**data.model_dump())
    try:
        prop = await dao.semantic_property_insert(db, prop)
    except sa_exc.IntegrityError:
        raise HTTPException(status_code=409, detail="属性代码已存在")
    return _ok(
        SemanticPropertyResponse.model_validate(prop).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.put("/properties/{property_id}")
async def update_property(
    property_id: uuid.UUID,
    data: SemanticPropertyUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    prop = await dao.semantic_property_get_by_id(db, property_id)
    if not prop:
        raise HTTPException(status_code=404, detail="属性不存在")
    prop = await dao.semantic_property_update_values(
        db, prop, data.model_dump(exclude_unset=True),
    )
    return _ok(
        SemanticPropertyResponse.model_validate(prop).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.delete("/properties/{property_id}")
async def delete_property(
    property_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    prop = await dao.semantic_property_get_by_id(db, property_id)
    if not prop:
        raise HTTPException(status_code=404, detail="属性不存在")
    await dao.semantic_property_delete(db, prop)
    return _ok(msg="已删除")


# ═══════════════════════════════════════
# DataMapping CRUD
# ═══════════════════════════════════════

@router.get("/mappings")
async def list_mappings(
    mapping_type: str | None = Query(None, alias="mappingType"),
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.data_mapping_list(
        db,
        mapping_type=mapping_type,
        status=status,
        page=page,
        page_size=page_size,
    )
    resp_items = [DataMappingResponse(**item) for item in items]
    return _ok(
        DataMappingListResponse(
            items=resp_items,
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("/mappings", status_code=201)
async def create_mapping(
    data: DataMappingCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dm = DataMapping(**data.model_dump())
    try:
        dm = await dao.data_mapping_insert(db, dm)
    except sa_exc.IntegrityError:
        raise HTTPException(status_code=409, detail="映射创建失败")
    return _ok(
        DataMappingResponse.model_validate(dm).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.put("/mappings/{mapping_id}")
async def update_mapping(
    mapping_id: uuid.UUID,
    data: DataMappingUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dm = await dao.data_mapping_get_by_id(db, mapping_id)
    if not dm:
        raise HTTPException(status_code=404, detail="映射不存在")
    dm = await dao.data_mapping_update_values(
        db, dm, data.model_dump(exclude_unset=True),
    )
    return _ok(
        DataMappingResponse.model_validate(dm).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.delete("/mappings/{mapping_id}")
async def delete_mapping(
    mapping_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dm = await dao.data_mapping_get_by_id(db, mapping_id)
    if not dm:
        raise HTTPException(status_code=404, detail="映射不存在")
    await dao.data_mapping_delete(db, dm)
    return _ok(msg="已删除")


# ═══════════════════════════════════════
# Stats
# ═══════════════════════════════════════

@router.get("/stats")
async def get_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stats = await dao.semantic_get_stats(db)
    return _ok(
        SemanticStatsResponse(**stats).model_dump(**_DUMP_OPTS)
    )
