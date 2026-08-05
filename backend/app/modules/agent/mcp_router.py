"""MCP JSON-RPC 2.0 适配器 — 将 /mcp 端点桥接到 shared query logic。

协议版本: 2024-11-05
"""

import json
import logging
import re
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.modules.agent.handlers import (
    handle_catalog,
    handle_query_graph,
    handle_query_metrics,
    handle_query_objects,
    handle_query_relations,
    handle_reload,
)
from app.modules.agent.mcp_auth import verify_mcp_api_key

router = APIRouter(tags=["mcp"])
logger = logging.getLogger("sk-mind")

# ── JSON-RPC 错误码 ──────────────────────────────────────
JSONRPC_PARSE_ERROR = -32700
JSONRPC_INVALID_REQUEST = -32600
JSONRPC_METHOD_NOT_FOUND = -32601
JSONRPC_INVALID_PARAMS = -32602
JSONRPC_INTERNAL_ERROR = -32603
JSONRPC_SERVER_ERROR = -32000


def _make_jsonrpc_error(id_val: Any, code: int, message: str) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": id_val,
        "error": {"code": code, "message": message},
    }


def _make_jsonrpc_result(id_val: Any, result: Any) -> dict:
    return {"jsonrpc": "2.0", "id": id_val, "result": result}


# ── CamelCase → snake_case ───────────────────────────────
_RE_CAMEL = re.compile(r"(?<!^)(?=[A-Z])")


def _camel_to_snake(name: str) -> str:
    return _RE_CAMEL.sub("_", name).lower()


# 已知的 CamelCase → snake_case 映射（处理首字母连续大写等边缘情况）
_CAMEL_TO_SNAKE_MAP = {
    "objectName": "object_name",
    "metricName": "metric_name",
    "orderBy": "order_by",
    "groupBy": "group_by",
    "relationType": "relation_type",
    "subjectObject": "subject_object",
    "objectObject": "object_object",
    "agentEnabledOnly": "agent_enabled_only",
    "objectType": "object_type",
    "entityId": "entity_id",
    "relationCode": "relation_code",
    "minConfidence": "min_confidence",
    "confirmedOnly": "confirmed_only",
}


def _convert_args(args: dict[str, Any]) -> dict[str, Any]:
    """将 MCP tools/call 的 CamelCase 参数转为 handler 期望的 snake_case。"""
    result: dict[str, Any] = {}
    for key, value in args.items():
        snake_key = _CAMEL_TO_SNAKE_MAP.get(key, _camel_to_snake(key))
        result[snake_key] = value
    return result


# ── MCP 工具定义（JSON Schema input schemas）────────────

MCP_TOOLS = [
    {
        "name": "query_objects",
        "description": "查询业务对象数据。不传 objectName 时返回当前 MCP 可见的对象目录，确认可用对象及字段。"
                       "首次使用先调目录查询确认可用对象，再按 objectName + filters 查询具体数据。数据源 source 默认 mes。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "数据源标识，默认 mes。MES 系统使用 mes，未来扩展 erp 等",
                },
                "objectName": {
                    "type": "string",
                    "description": "对象名（CamelCase，小写蛇形）。不传则返回对象目录。",
                },
                "filters": {
                    "type": "object",
                    "description": "等值筛选条件，键为对象属性名（CamelCase）。常用：workshop, machine_no, event_type, shift, status, date 等",
                },
                "orderBy": {
                    "type": "string",
                    "description": "排序字段和方向，如 event_time desc。排序方向含在字符串中（ASC/DESC）。",
                },
                "limit": {
                    "type": "number",
                    "description": "返回行数，默认 100，上限 10000",
                    "default": 100,
                },
            },
        },
    },
    {
        "name": "query_metrics",
        "description": "查询指标聚合数据。不传 metricName 时返回指标目录。指标聚合数据用于汇总统计分析，支持 groupBy 分组和 dimensions 下钻。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "数据源标识，默认 mes",
                },
                "metricName": {
                    "type": "string",
                    "description": "指标名（CamelCase）。不传则返回指标目录。",
                },
                "groupBy": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "分组字段列表，如 [workshop, shift]",
                },
                "dimensions": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "完整分组维度列表，如 [workshop, shift]。与 groupBy 可同时使用。",
                },
                "filters": {
                    "type": "object",
                    "description": "过滤条件，如 {workshop: 注塑, date: 2026-07-30}",
                },
                "limit": {
                    "type": "number",
                    "description": "返回行数，默认 50，上限 10000",
                    "default": 50,
                },
            },
        },
    },
    {
        "name": "query_relations",
        "description": "查询语义关系定义（类型层）。不传 relationType 时返回全部关系目录，含 subject/object 对象与 join 字段，帮助 Agent 理解对象之间可沿哪些关系跳转。"
                       "查询关系目录或按类型/主体/客体过滤。配合 query_objects / query_graph 使用：先确认关系，再沿关系查询实例路径。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "数据源标识，默认 mes",
                },
                "relationType": {
                    "type": "string",
                    "description": "关系类型过滤：structural/transactional/resource/process/responsibility/financial/quality/event",
                },
                "subjectObject": {
                    "type": "string",
                    "description": "主体对象名（小写蛇形），如 machine_dim",
                },
                "objectObject": {
                    "type": "string",
                    "description": "客体对象名（小写蛇形），如 andon_event",
                },
                "agentEnabledOnly": {
                    "type": "boolean",
                    "description": "仅返回 Agent 可用的关系，默认 false",
                },
            },
        },
    },
    {
        "name": "query_graph",
        "description": "查询业务关系图谱实例路径（1-3 跳）。返回对象实例之间的关系边链，支持按对象类型/实体ID/关系编码过滤、可信度下限与仅已确认过滤。"
                       "给定起点对象类型（和可选实体ID），沿已确认关系边展开最多 hops 跳，返回路径列表。配合 query_relations 确认可用关系后再查。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "数据源标识，默认 mes",
                },
                "objectType": {
                    "type": "string",
                    "description": "起点对象类型（小写蛇形），如 work_order",
                },
                "entityId": {
                    "type": "string",
                    "description": "起点实体 ID，如 WO001；不填则查该类型全部",
                },
                "relationCode": {
                    "type": "string",
                    "description": "关系编码过滤，如 REL-M05",
                },
                "hops": {
                    "type": "number",
                    "description": "跳数范围 1-3，默认 2",
                    "default": 2,
                },
                "minConfidence": {
                    "type": "number",
                    "description": "可信度下限 0-1，默认 0",
                    "default": 0,
                },
                "confirmedOnly": {
                    "type": "boolean",
                    "description": "仅返回已确认关系，默认 false",
                },
            },
        },
    },
]


# ── MCP method handlers ─────────────────────────────────


def _serialize_for_json(obj: Any) -> Any:
    """递归将 Decimal / datetime / date / time 转为 JSON 可序列化类型。"""
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _serialize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize_for_json(v) for v in obj]
    return obj


async def _handle_initialize(params: dict, req_id: Any) -> dict:
    return _make_jsonrpc_result(req_id, {
        "protocolVersion": "2024-11-05",
        "capabilities": {"tools": {}},
        "serverInfo": {
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
        },
    })


async def _handle_tools_list(params: dict, req_id: Any) -> dict:
    return _make_jsonrpc_result(req_id, {"tools": MCP_TOOLS})


async def _handle_tools_call(params: dict, req_id: Any, db: AsyncSession) -> dict:
    tool_name = params.get("name", "")
    arguments = params.get("arguments", {})
    args = _convert_args(arguments)

    try:
        if tool_name == "query_objects":
            result = await handle_query_objects(
                db=db,
                source=args.get("source", "mes"),
                object_name=args.get("object_name"),
                filters=args.get("filters"),
                order_by=args.get("order_by"),
                limit=args.get("limit", 100),
            )
        elif tool_name == "query_metrics":
            result = await handle_query_metrics(
                db=db,
                source=args.get("source", "mes"),
                metric_name=args.get("metric_name"),
                group_by=args.get("group_by"),
                dimensions=args.get("dimensions"),
                filters=args.get("filters"),
                limit=args.get("limit", 50),
            )
        elif tool_name == "query_relations":
            result = handle_query_relations(
                source=args.get("source", "mes"),
                relation_type=args.get("relation_type"),
                subject_object=args.get("subject_object"),
                object_object=args.get("object_object"),
                agent_enabled_only=args.get("agent_enabled_only", False),
            )
        elif tool_name == "query_graph":
            result = await handle_query_graph(
                db=db,
                source=args.get("source", "mes"),
                object_type=args.get("object_type"),
                entity_id=args.get("entity_id"),
                relation_code=args.get("relation_code"),
                hops=args.get("hops", 2),
                min_confidence=args.get("min_confidence", 0.0),
                confirmed_only=args.get("confirmed_only", False),
            )
        else:
            return _make_jsonrpc_error(req_id, JSONRPC_METHOD_NOT_FOUND,
                                       f"Tool '{tool_name}' not found")

        return _make_jsonrpc_result(req_id, {
            "content": [{"type": "text", "text": json.dumps(_serialize_for_json(result), ensure_ascii=False)}],
        })
    except ValueError as e:
        return _make_jsonrpc_error(req_id, JSONRPC_INVALID_PARAMS, str(e))
    except RuntimeError as e:
        return _make_jsonrpc_error(req_id, JSONRPC_SERVER_ERROR, str(e))
    except Exception as e:
        logger.exception("tools/call failed: %s", tool_name)
        return _make_jsonrpc_error(req_id, JSONRPC_INTERNAL_ERROR, str(e))


# ── POST / ──────────────────────────────────────────────


@router.post("")
async def mcp_endpoint(
    request: Request,
    db: AsyncSession = Depends(get_db),
    _auth: None = Depends(verify_mcp_api_key),
):
    """MCP JSON-RPC 2.0 入口。"""
    try:
        body = await request.json()
    except Exception:
        return JSONResponse(
            content=_make_jsonrpc_error(None, JSONRPC_PARSE_ERROR, "Parse error"),
            status_code=400,
        )

    req_id = body.get("id")
    method = body.get("method", "")
    params = body.get("params", {})

    # 通知（无 id）不需要响应
    if req_id is None and method.startswith("notifications/"):
        return JSONResponse(content={}, status_code=200)

    if not method:
        return JSONResponse(
            content=_make_jsonrpc_error(req_id, JSONRPC_INVALID_REQUEST, "Invalid Request"),
            status_code=400,
        )

    try:
        if method == "initialize":
            response = await _handle_initialize(params, req_id)
        elif method == "tools/list":
            response = await _handle_tools_list(params, req_id)
        elif method == "tools/call":
            response = await _handle_tools_call(params, req_id, db)
        else:
            response = _make_jsonrpc_error(req_id, JSONRPC_METHOD_NOT_FOUND,
                                           f"Method '{method}' not found")

        status_code = 200
        if "error" in response:
            # Map JSON-RPC error codes to HTTP status
            error_code = response["error"]["code"]
            if isinstance(req_id, str) and len(req_id) > 200:
                status_code = 400  # path through
            else:
                status_code = 200  # JSON-RPC errors are 200 per spec
        return JSONResponse(content=response, status_code=status_code)

    except Exception as e:
        logger.exception("MCP endpoint error")
        return JSONResponse(
            content=_make_jsonrpc_error(req_id, JSONRPC_INTERNAL_ERROR, f"Internal error: {str(e)}"),
            status_code=200,
        )
