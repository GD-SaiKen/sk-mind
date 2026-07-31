"""YAML 语义模型加载器 — 从 YAML 配置加载语义对象/属性/指标，同步到 DB 缓存。"""

import logging
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger("sk-mind")

_SEMANTIC_CONFIG_DIR = os.environ.get(
    "SEMANTIC_CONFIG_DIR",
    str(Path(__file__).resolve().parents[3] / "config" / "semantic"),
)

_LOADER_CACHE: dict[str, "SourceSemanticLoader"] = {}


class SourceSemanticLoader:
    """单个数据源的 YAML 语义模型加载器。

    - 从 YAML 加载 objects/metadata，内存 dict 缓存
    - sync_to_db() 将数据 upsert 到 semantic_objects/properties/data_mappings
    """

    def __init__(self, source: str):
        self.source = source
        self._config_dir = Path(_SEMANTIC_CONFIG_DIR) / source
        self._objects: dict[str, dict] = {}
        self._metrics: dict[str, dict] = {}
        self._catalog: dict[str, Any] = {}
        self._file_mtimes: dict[str, float] = {}
        self._loaded = False

    # ── YAML loading ──────────────────────────────────────

    def load_all(self) -> None:
        """加载所有 YAML 文件到内存。"""
        self._loaded = False
        self._objects = {}
        self._metrics = {}
        self._catalog = {}
        self._file_mtimes = {}

        self._scan_files()
        self._load_objects()
        self._load_metrics()
        self._load_catalog()
        self._loaded = True
        logger.info(
            "Semantic loader [%s]: loaded %d objects, %d metrics",
            self.source, len(self._objects), len(self._metrics),
        )

    def _scan_files(self) -> None:
        """扫描目录下所有 .yaml 文件，记录 mtime。"""
        for yaml_file in self._config_dir.rglob("*.yaml"):
            if yaml_file.is_file():
                self._file_mtimes[str(yaml_file)] = yaml_file.stat().st_mtime

    def _any_file_changed(self) -> bool:
        """检查是否有文件被修改过。"""
        if not self._loaded:
            return True
        for path_str, old_mtime in self._file_mtimes.items():
            file_path = Path(path_str)
            if not file_path.exists():
                return True
            if file_path.stat().st_mtime != old_mtime:
                return True
        return False

    def _load_objects(self) -> None:
        objects_dir = self._config_dir / "objects"
        if not objects_dir.is_dir():
            logger.warning("Objects directory not found: %s", objects_dir)
            return
        for file_path in sorted(objects_dir.glob("*.yaml")):
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            obj_name = data.get("object")
            if not obj_name:
                continue
            self._objects[obj_name] = data

    def _load_metrics(self) -> None:
        metrics_dir = self._config_dir / "metrics"
        if not metrics_dir.is_dir():
            logger.warning("Metrics directory not found: %s", metrics_dir)
            return
        for file_path in sorted(metrics_dir.glob("*.yaml")):
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            for m in data.get("metrics", []):
                metric_name = m.get("metric")
                if metric_name:
                    self._metrics[metric_name] = m

    def _load_catalog(self) -> None:
        catalog_path = self._config_dir / "catalog.yaml"
        if catalog_path.is_file():
            with open(catalog_path, "r", encoding="utf-8") as f:
                self._catalog = yaml.safe_load(f) or {}

    # ── Access methods ────────────────────────────────────

    def get_object(self, name: str) -> dict | None:
        return self._objects.get(name)

    def get_metric(self, name: str) -> dict | None:
        return self._metrics.get(name)

    def list_objects(self) -> list[dict]:
        return list(self._objects.values())

    def list_metrics(self) -> list[dict]:
        return list(self._metrics.values())

    def get_catalog(self) -> dict:
        return self._catalog

    def is_loaded(self) -> bool:
        return self._loaded

    # ── DB sync (Plan A core) ─────────────────────────────

    async def sync_to_db(self, db: AsyncSession) -> None:
        """将 YAML 对象/属性/映射 upsert 到 DB 缓存表。

        策略:
        - Object: INSERT ON CONFLICT (code) DO UPDATE
        - Property: INSERT ON CONFLICT (semantic_object_id, code) DO UPDATE
        - 清理过期属性: DELETE properties WHERE code NOT IN (yaml_codes)
        - Mapping: 为每个 object 创建一条 'object' 类型的 DataMapping
        """
        objects_dir = self._config_dir / "objects"
        if not objects_dir.is_dir():
            return

        for file_path in sorted(objects_dir.glob("*.yaml")):
            with open(file_path, "r", encoding="utf-8") as f:
                obj_data = yaml.safe_load(f)

            obj_name = obj_data.get("object")
            if not obj_name:
                continue

            code = f"{self.source}.{obj_name}"
            display_name = obj_data.get("display_name", obj_name)
            description = obj_data.get("description", "")
            domain = obj_data.get("domain", "")
            source_of_truth = obj_data.get("source_of_truth", "")

            # Object upsert
            await db.execute(
                text("""
                    INSERT INTO semantic_objects (id, name, code, description, object_type, domain, status, created_at, updated_at)
                    VALUES (:id, :name, :code, :description, :object_type, :domain, 'active', NOW(), NOW())
                    ON CONFLICT (code) DO UPDATE SET
                        name = EXCLUDED.name,
                        description = EXCLUDED.description,
                        object_type = EXCLUDED.object_type,
                        domain = EXCLUDED.domain,
                        status = 'active',
                        updated_at = NOW()
                """),
                {
                    "id": uuid.uuid4(),
                    "name": display_name,
                    "code": code,
                    "description": description,
                    "object_type": self._infer_object_type(obj_data),
                    "domain": domain,
                },
            )

            # Get object ID
            obj_row = (await db.execute(
                text("SELECT id FROM semantic_objects WHERE code = :code"),
                {"code": code},
            )).fetchone()
            if obj_row is None:
                continue
            semantic_object_id = obj_row[0]

            # Properties: collect YAML codes for cleanup
            yaml_prop_codes: set[str] = set()

            # Property upsert
            for idx, prop in enumerate(obj_data.get("properties", [])):
                prop_code = prop.get("code")
                prop_name = prop.get("name", prop_code)
                prop_type = prop.get("property_type", "descriptive")
                data_type = prop.get("data_type", "STRING")
                prop_desc = prop.get("description", "")
                yaml_prop_codes.add(prop_code)

                await db.execute(
                    text("""
                        INSERT INTO semantic_properties
                            (id, semantic_object_id, name, code, description, property_type, data_type, is_required, is_sensitive, ordinal_position, status, created_at, updated_at)
                        VALUES (:id, :semantic_object_id, :name, :code, :description, :property_type, :data_type, FALSE, FALSE, :ordinal_position, 'active', NOW(), NOW())
                        ON CONFLICT (semantic_object_id, code) DO UPDATE SET
                            name = EXCLUDED.name,
                            description = EXCLUDED.description,
                            property_type = EXCLUDED.property_type,
                            data_type = EXCLUDED.data_type,
                            ordinal_position = EXCLUDED.ordinal_position,
                            status = 'active',
                            updated_at = NOW()
                    """),
                    {
                        "id": uuid.uuid4(),
                        "semantic_object_id": semantic_object_id,
                        "name": prop_name,
                        "code": prop_code,
                        "description": prop_desc,
                        "property_type": prop_type,
                        "data_type": data_type,
                        "ordinal_position": idx,
                    },
                )

            # Clean up stale properties
            if yaml_prop_codes:
                await db.execute(
                    text("""
                        DELETE FROM semantic_properties
                        WHERE semantic_object_id = :oid AND code NOT IN :codes
                    """),
                    {"oid": semantic_object_id, "codes": tuple(yaml_prop_codes)},
                )

            # Mapping: object-level binding
            for binding in obj_data.get("bindings", []):
                # Upsert DataMapping for the object
                now_val = datetime.utcnow()
                existing = (await db.execute(
                    text("""
                        SELECT id FROM data_mappings
                        WHERE mapping_type = 'object'
                          AND semantic_object_id = :oid
                          AND target_type = :target_type
                    """),
                    {"oid": semantic_object_id, "target_type": binding.get("source", source_of_truth)},
                )).fetchone()

                if existing:
                    # Only update if the target is a view/table reference
                    await db.execute(
                        text("""
                            UPDATE data_mappings SET
                                transform_rule = :rule,
                                confidence = 'high',
                                status = 'confirmed',
                                updated_at = NOW()
                            WHERE id = :id
                        """),
                        {
                            "id": existing[0],
                            "rule": f"source={source_of_truth}",
                        },
                    )
                else:
                    await db.execute(
                        text("""
                            INSERT INTO data_mappings
                                (id, mapping_type, semantic_object_id, target_type, target_id, transform_rule, confidence, status, created_by, created_at, updated_at)
                            VALUES
                                (:id, 'object', :oid, :target_type, :target_id, :rule, 'high', 'confirmed', 'yaml_sync', NOW(), NOW())
                        """),
                        {
                            "id": uuid.uuid4(),
                            "oid": semantic_object_id,
                            "target_type": "data_source",
                            "target_id": uuid.uuid4(),
                            "rule": f"source={source_of_truth}",
                        },
                    )

        await db.commit()
        logger.info("Semantic loader [%s]: sync_to_db complete", self.source)

    def _infer_object_type(self, obj_data: dict) -> str:
        """从 YAML 数据推断 object_type。"""
        mapping = {
            "machine_dim": "resource",
            "andon_event": "event_state",
            "error_report": "event_state",
            "oee_record": "event_state",
            "production_report": "transaction",
            "work_order": "transaction",
            "schedule_task": "process",
            "craft_hours": "master_data",
        }
        return mapping.get(obj_data.get("object", ""), "data")

    # ── Async lifecycle ───────────────────────────────────

    async def load_all_async(
        self, db: AsyncSession, force: bool = False,
    ) -> None:
        """异步加载 YAML + 同步到 DB。

        - force=True: 忽略 mtime 检查，强制重载
        """
        if force or self._any_file_changed():
            self.load_all()
        await self.sync_to_db(db)

    def reload(self) -> None:
        """强制重新加载 YAML（不触发 DB 同步）。"""
        self.load_all()


# ── Factory ────────────────────────────────────────────────

def get_loader(source: str) -> SourceSemanticLoader:
    """获取或创建指定 source 的 loader（单例）。"""
    if source in _LOADER_CACHE:
        return _LOADER_CACHE[source]

    config_dir = Path(_SEMANTIC_CONFIG_DIR) / source
    if not config_dir.is_dir():
        raise FileNotFoundError(
            f"Semantic config directory not found: {config_dir}. "
            f"Set SEMANTIC_CONFIG_DIR env var or create {config_dir}/"
        )

    loader = SourceSemanticLoader(source)
    _LOADER_CACHE[source] = loader
    return loader


def _available_sources() -> list[str]:
    """列出所有可用的语义配置源。"""
    root = Path(_SEMANTIC_CONFIG_DIR)
    if not root.is_dir():
        return []
    return [
        d.name for d in root.iterdir()
        if d.is_dir() and (d / "catalog.yaml").is_file()
    ]
