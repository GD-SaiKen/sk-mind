"""公共 Pydantic 基类 — 蛇形↔驼峰自动转换。

项目规范：前后端 API 交互一律使用 camelCase（请求 + 响应）。

用法：
    from app.core.schemas import CamelModel

    class MyRequest(CamelModel):
        user_name: str       # Python: snake_case
        # → API JSON: {"userName": "..."}

    class MyResponse(CamelModel):
        created_at: datetime  # → JSON: {"createdAt": "..."}
"""

from pydantic import BaseModel, ConfigDict


def _to_camel(snake: str) -> str:
    parts = snake.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class CamelModel(BaseModel):
    """自动 snake_case ↔ camelCase 转换。

    - 请求：前端发 camelCase → Python 属性 snake_case（populate_by_name）
    - 响应：Python 属性 snake_case → JSON camelCase（alias_generator）
    """

    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        from_attributes=True,  # 所有 CamelModel 子类均支持 ORM 对象直接构造
    )
