"""语义模型路由层。"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import exc as sa_exc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.modules.auth.models import User
from app.modules.semantic import dao
from app.modules.semantic.models import (
    SemanticObject,
    SemanticProperty,
    SemanticRelation,
    DataMapping,
)
from app.modules.semantic.schemas import (
    DataMappingCreate,
    DataMappingListResponse,
    DataMappingResponse,
    DataMappingUpdate,
    SemanticRelationCreate,
    SemanticRelationListResponse,
    SemanticRelationResponse,
    SemanticRelationUpdate,
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
# SemanticRelation CRUD
# ═══════════════════════════════════════

@router.get("/relations")
async def list_relations(
    keyword: str | None = Query(None),
    relation_type: str | None = Query(None, alias="relationType"),
    subject_object_id: uuid.UUID | None = Query(None, alias="subjectObjectId"),
    object_object_id: uuid.UUID | None = Query(None, alias="objectObjectId"),
    agent_enabled: bool | None = Query(None, alias="agentEnabled"),
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items, total = await dao.semantic_relation_list(
        db,
        keyword=keyword,
        relation_type=relation_type,
        subject_object_id=subject_object_id,
        object_object_id=object_object_id,
        agent_enabled=agent_enabled,
        status=status,
        page=page,
        page_size=page_size,
    )
    resp_items = [SemanticRelationResponse(**item) for item in items]
    return _ok(
        SemanticRelationListResponse(
            items=resp_items,
            total=total,
            page=page,
            page_size=page_size,
        ).model_dump(**_DUMP_OPTS)
    )


@router.post("/relations", status_code=201)
async def create_relation(
    data: SemanticRelationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # 校验 code 唯一性（前置，避免 DB IntegrityError）
    existing = await dao.semantic_relation_get_by_code(db, data.code)
    if existing:
        raise HTTPException(status_code=409, detail="关系编码已存在")

    # 校验主体/客体对象存在 + 禁止自引用
    if data.subject_object_id == data.object_object_id:
        raise HTTPException(status_code=400, detail="主体对象与客体对象不能相同（禁止自引用）")
    subject = await dao.semantic_object_get_by_id(db, data.subject_object_id)
    if not subject:
        raise HTTPException(status_code=404, detail="主体业务对象不存在")
    obj = await dao.semantic_object_get_by_id(db, data.object_object_id)
    if not obj:
        raise HTTPException(status_code=404, detail="客体业务对象不存在")

    rel = SemanticRelation(**data.model_dump())
    try:
        rel = await dao.semantic_relation_insert(db, rel)
    except sa_exc.IntegrityError:
        raise HTTPException(status_code=409, detail="关系编码已存在")

    item = {
        "id": rel.id,
        "name": rel.name,
        "code": rel.code,
        "relation_type": rel.relation_type,
        "subject_object_id": rel.subject_object_id,
        "object_object_id": rel.object_object_id,
        "cardinality": rel.cardinality,
        "join_mechanism": rel.join_mechanism,
        "description": rel.description,
        "agent_enabled": rel.agent_enabled,
        "status": rel.status,
        "created_at": rel.created_at,
        "updated_at": rel.updated_at,
        "subject_object_name": subject.name,
        "object_object_name": obj.name,
        "edge_count": 0,
    }
    return _ok(
        SemanticRelationResponse(**item).model_dump(**_DUMP_OPTS),
        msg="创建成功",
    )


@router.get("/relations/{relation_id}")
async def get_relation(
    relation_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rel = await dao.semantic_relation_get_by_id(db, relation_id)
    if not rel:
        raise HTTPException(status_code=404, detail="语义关系不存在")

    subject = await dao.semantic_object_get_by_id(db, rel.subject_object_id)
    obj = await dao.semantic_object_get_by_id(db, rel.object_object_id)

    from app.modules.graph.models import BusinessGraphEdge

    edge_count = (
        await db.execute(
            select(func.count())
            .select_from(BusinessGraphEdge)
            .where(BusinessGraphEdge.relation_id == relation_id)
        )
    ).scalar_one()

    item = {
        "id": rel.id,
        "name": rel.name,
        "code": rel.code,
        "relation_type": rel.relation_type,
        "subject_object_id": rel.subject_object_id,
        "object_object_id": rel.object_object_id,
        "cardinality": rel.cardinality,
        "join_mechanism": rel.join_mechanism,
        "description": rel.description,
        "agent_enabled": rel.agent_enabled,
        "status": rel.status,
        "created_at": rel.created_at,
        "updated_at": rel.updated_at,
        "subject_object_name": subject.name if subject else None,
        "object_object_name": obj.name if obj else None,
        "edge_count": edge_count,
    }
    return _ok(SemanticRelationResponse(**item).model_dump(**_DUMP_OPTS))


@router.put("/relations/{relation_id}")
async def update_relation(
    relation_id: uuid.UUID,
    data: SemanticRelationUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rel = await dao.semantic_relation_get_by_id(db, relation_id)
    if not rel:
        raise HTTPException(status_code=404, detail="语义关系不存在")

    values = data.model_dump(exclude_unset=True)

    # 主体/客体校验
    if values.get("subject_object_id"):
        subject = await dao.semantic_object_get_by_id(
            db, values["subject_object_id"]
        )
        if not subject:
            raise HTTPException(status_code=404, detail="主体业务对象不存在")
    if values.get("object_object_id"):
        obj = await dao.semantic_object_get_by_id(db, values["object_object_id"])
        if not obj:
            raise HTTPException(status_code=404, detail="客体业务对象不存在")

    # 禁止自引用
    effective_subject = values.get("subject_object_id", rel.subject_object_id)
    effective_object = values.get("object_object_id", rel.object_object_id)
    if effective_subject == effective_object:
        raise HTTPException(
            status_code=400, detail="主体对象与客体对象不能相同（禁止自引用）"
        )

    for k, v in values.items():
        setattr(rel, k, v)
    await dao.semantic_relation_update(db, rel)

    # 构建响应
    subject = await dao.semantic_object_get_by_id(db, rel.subject_object_id)
    obj = await dao.semantic_object_get_by_id(db, rel.object_object_id)

    from app.modules.graph.models import BusinessGraphEdge

    edge_count = (
        await db.execute(
            select(func.count())
            .select_from(BusinessGraphEdge)
            .where(BusinessGraphEdge.relation_id == relation_id)
        )
    ).scalar_one()

    item = {
        "id": rel.id,
        "name": rel.name,
        "code": rel.code,
        "relation_type": rel.relation_type,
        "subject_object_id": rel.subject_object_id,
        "object_object_id": rel.object_object_id,
        "cardinality": rel.cardinality,
        "join_mechanism": rel.join_mechanism,
        "description": rel.description,
        "agent_enabled": rel.agent_enabled,
        "status": rel.status,
        "created_at": rel.created_at,
        "updated_at": rel.updated_at,
        "subject_object_name": subject.name if subject else None,
        "object_object_name": obj.name if obj else None,
        "edge_count": edge_count,
    }
    return _ok(
        SemanticRelationResponse(**item).model_dump(**_DUMP_OPTS),
        msg="更新成功",
    )


@router.delete("/relations/{relation_id}")
async def delete_relation(
    relation_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rel = await dao.semantic_relation_get_by_id(db, relation_id)
    if not rel:
        raise HTTPException(status_code=404, detail="语义关系不存在")
    rel.status = "archived"
    await dao.semantic_relation_update(db, rel)
    return _ok(msg="已归档")


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
