"""初始迁移 — 创建阶段 1 全部表结构。

Revision ID: 001
Revises: None
Create Date: 2026-06-13
"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, String, Text, Integer, Float, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB

# revision identifiers
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """创建所有表。"""

    # ── Auth 模块 ──────────────────────────
    op.create_table(
        "departments",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(100), nullable=False),
        Column("code", String(50), unique=True, nullable=False),
        Column("parent_id", UUID(as_uuid=True), nullable=True),
        Column("sort_order", Integer, default=0, nullable=False),
        Column("is_active", Boolean, default=True, nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "users",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("username", String(100), unique=True, nullable=False),
        Column("email", String(255), unique=True, nullable=False),
        Column("hashed_password", String(255), nullable=False),
        Column("display_name", String(100), nullable=False),
        Column("department_id", UUID(as_uuid=True), nullable=True),
        Column("is_active", Boolean, default=True, nullable=False),
        Column("is_superuser", Boolean, default=False, nullable=False),
        Column("last_login_at", DateTime(timezone=True), nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "roles",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(100), unique=True, nullable=False),
        Column("code", String(50), unique=True, nullable=False),
        Column("description", Text, nullable=True),
        Column("is_active", Boolean, default=True, nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "permissions",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(100), nullable=False),
        Column("code", String(100), unique=True, nullable=False),
        Column("resource", String(100), nullable=False),
        Column("action", String(50), nullable=False),
        Column("description", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "user_roles",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("user_id", UUID(as_uuid=True), nullable=False),
        Column("role_id", UUID(as_uuid=True), nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "role_permissions",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("role_id", UUID(as_uuid=True), nullable=False),
        Column("permission_id", UUID(as_uuid=True), nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "audit_logs",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("user_id", UUID(as_uuid=True), nullable=True),
        Column("username", String(100), nullable=True),
        Column("action", String(100), nullable=False),
        Column("resource", String(100), nullable=False),
        Column("resource_id", String(100), nullable=True),
        Column("detail", Text, nullable=True),
        Column("ip_address", String(50), nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    # ── 数据源模块 ─────────────────────────
    op.create_table(
        "data_sources",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(200), nullable=False),
        Column("code", String(100), unique=True, nullable=False),
        Column("description", Text, nullable=True),
        Column("source_type", String(50), nullable=False),
        Column("access_method", String(50), nullable=False),
        Column("owner_name", String(100), nullable=True),
        Column("owner_dept", String(100), nullable=True),
        Column("contact_info", String(200), nullable=True),
        Column("sensitivity_level", String(20), default="internal", nullable=False),
        Column("status", String(20), default="draft", nullable=False),
        Column("is_agent_accessible", Boolean, default=False, nullable=False),
        Column("tags", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "source_objects",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("data_source_id", UUID(as_uuid=True), nullable=False),
        Column("name", String(200), nullable=False),
        Column("object_type", String(50), nullable=False),
        Column("object_path", String(500), nullable=True),
        Column("schema_name", String(100), nullable=True),
        Column("description", Text, nullable=True),
        Column("row_count_estimate", Integer, nullable=True),
        Column("is_active", Boolean, default=True, nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "connector_configs",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("data_source_id", UUID(as_uuid=True), nullable=False),
        Column("config_type", String(50), nullable=False),
        Column("host", String(255), nullable=True),
        Column("port", Integer, nullable=True),
        Column("database_name", String(100), nullable=True),
        Column("username", String(100), nullable=True),
        Column("credential_ref", String(255), nullable=True),
        Column("extra_config", Text, nullable=True),
        Column("is_validated", Boolean, default=False, nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    # ── 接入任务模块 ───────────────────────
    op.create_table(
        "ingestion_tasks",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(200), nullable=False),
        Column("code", String(100), unique=True, nullable=False),
        Column("data_source_id", UUID(as_uuid=True), nullable=False),
        Column("source_object_id", UUID(as_uuid=True), nullable=True),
        Column("target_layer", String(20), nullable=False),
        Column("schedule_type", String(20), default="manual", nullable=False),
        Column("cron_expression", String(50), nullable=True),
        Column("status", String(20), default="draft", nullable=False),
        Column("config", JSONB, nullable=True),
        Column("description", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "ingestion_batches",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("task_id", UUID(as_uuid=True), nullable=False),
        Column("triggered_by", String(100), nullable=True),
        Column("trigger_type", String(20), default="manual", nullable=False),
        Column("started_at", DateTime(timezone=True), nullable=True),
        Column("finished_at", DateTime(timezone=True), nullable=True),
        Column("file_count", Integer, default=0, nullable=False),
        Column("record_count", Integer, default=0, nullable=False),
        Column("success_count", Integer, default=0, nullable=False),
        Column("fail_count", Integer, default=0, nullable=False),
        Column("skip_count", Integer, default=0, nullable=False),
        Column("status", String(30), default="pending", nullable=False),
        Column("affected_datasets", Text, nullable=True),
        Column("error_summary", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "file_assets",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("data_source_id", UUID(as_uuid=True), nullable=True),
        Column("ingestion_task_id", UUID(as_uuid=True), nullable=True),
        Column("batch_id", UUID(as_uuid=True), nullable=True),
        Column("file_name", String(500), nullable=False),
        Column("file_path", String(1000), nullable=False),
        Column("file_size", Integer, nullable=True),
        Column("file_hash", String(128), nullable=True),
        Column("file_mtime", DateTime(timezone=True), nullable=True),
        Column("template_type", String(50), nullable=True),
        Column("sheet_names", Text, nullable=True),
        Column("status", String(20), default="pending", nullable=False),
        Column("row_count", Integer, nullable=True),
        Column("error_message", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "import_errors",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("batch_id", UUID(as_uuid=True), nullable=False),
        Column("file_asset_id", UUID(as_uuid=True), nullable=True),
        Column("error_level", String(20), nullable=False),
        Column("sheet_name", String(200), nullable=True),
        Column("row_number", Integer, nullable=True),
        Column("field_name", String(200), nullable=True),
        Column("error_type", String(100), nullable=False),
        Column("error_message", Text, nullable=False),
        Column("raw_value", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    # ── 数据集模块 ─────────────────────────
    op.create_table(
        "datasets",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(200), nullable=False),
        Column("code", String(100), unique=True, nullable=False),
        Column("description", Text, nullable=True),
        Column("data_layer", String(20), nullable=False),
        Column("data_source_id", UUID(as_uuid=True), nullable=True),
        Column("source_object_id", UUID(as_uuid=True), nullable=True),
        Column("generated_by_task_id", UUID(as_uuid=True), nullable=True),
        Column("last_batch_id", UUID(as_uuid=True), nullable=True),
        Column("record_count", Integer, nullable=True),
        Column("field_count", Integer, nullable=True),
        Column("business_domain", String(100), nullable=True),
        Column("owner_name", String(100), nullable=True),
        Column("tags", Text, nullable=True),
        Column("sensitivity_level", String(20), default="internal", nullable=False),
        Column("is_agent_accessible", Boolean, default=False, nullable=False),
        Column("status", String(20), default="draft", nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "dataset_fields",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("dataset_id", UUID(as_uuid=True), nullable=False),
        Column("field_name", String(200), nullable=False),
        Column("field_alias", String(200), nullable=True),
        Column("description", Text, nullable=True),
        Column("data_type", String(50), nullable=False),
        Column("field_length", Integer, nullable=True),
        Column("is_nullable", Boolean, default=True, nullable=False),
        Column("ordinal_position", Integer, default=0, nullable=False),
        Column("sensitivity_level", String(20), default="internal", nullable=False),
        Column("quality_status", String(20), nullable=True),
        Column("sample_values", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "data_tables",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("dataset_id", UUID(as_uuid=True), nullable=True),
        Column("schema_name", String(100), nullable=False),
        Column("table_name", String(200), nullable=False),
        Column("table_type", String(20), default="table", nullable=False),
        Column("description", Text, nullable=True),
        Column("row_count", Integer, nullable=True),
        Column("data_size_bytes", Integer, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    # ── 数据质量模块 ───────────────────────
    op.create_table(
        "quality_rules",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("name", String(200), nullable=False),
        Column("code", String(100), unique=True, nullable=False),
        Column("description", Text, nullable=True),
        Column("rule_type", String(50), nullable=False),
        Column("dataset_id", UUID(as_uuid=True), nullable=True),
        Column("field_id", UUID(as_uuid=True), nullable=True),
        Column("rule_params", JSONB, nullable=True),
        Column("is_enabled", Boolean, default=True, nullable=False),
        Column("severity", String(20), default="warning", nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "quality_runs",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("triggered_by", String(100), nullable=True),
        Column("trigger_type", String(20), default="manual", nullable=False),
        Column("rule_ids", Text, nullable=True),
        Column("dataset_ids", Text, nullable=True),
        Column("started_at", DateTime(timezone=True), nullable=True),
        Column("finished_at", DateTime(timezone=True), nullable=True),
        Column("total_rules", Integer, default=0, nullable=False),
        Column("passed_rules", Integer, default=0, nullable=False),
        Column("failed_rules", Integer, default=0, nullable=False),
        Column("total_issues", Integer, default=0, nullable=False),
        Column("status", String(20), default="running", nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    op.create_table(
        "quality_issues",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("quality_run_id", UUID(as_uuid=True), nullable=False),
        Column("rule_id", UUID(as_uuid=True), nullable=False),
        Column("dataset_id", UUID(as_uuid=True), nullable=True),
        Column("field_id", UUID(as_uuid=True), nullable=True),
        Column("batch_id", UUID(as_uuid=True), nullable=True),
        Column("issue_type", String(50), nullable=False),
        Column("severity", String(20), nullable=False),
        Column("issue_message", Text, nullable=False),
        Column("sample_value", Text, nullable=True),
        Column("sample_row", Integer, nullable=True),
        Column("affected_record_count", Integer, nullable=True),
        Column("status", String(20), default="open", nullable=False),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    # ── 数据血缘模块 ───────────────────────
    op.create_table(
        "data_lineage",
        Column("id", UUID(as_uuid=True), primary_key=True),
        Column("source_type", String(50), nullable=False),
        Column("source_id", UUID(as_uuid=True), nullable=False),
        Column("source_name", String(300), nullable=False),
        Column("target_type", String(50), nullable=False),
        Column("target_id", UUID(as_uuid=True), nullable=False),
        Column("target_name", String(300), nullable=False),
        Column("transform_type", String(50), nullable=False),
        Column("transform_rule", Text, nullable=True),
        Column("ingestion_task_id", UUID(as_uuid=True), nullable=True),
        Column("batch_id", UUID(as_uuid=True), nullable=True),
        Column("description", Text, nullable=True),
        Column("created_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
        Column("updated_at", DateTime(timezone=True), server_default=op.f("now()"), nullable=False),
    )

    # ── 索引 ───────────────────────────────
    op.create_index("ix_users_username", "users", ["username"])
    op.create_index("ix_roles_code", "roles", ["code"])
    op.create_index("ix_data_sources_code", "data_sources", ["code"])
    op.create_index("ix_data_sources_source_type", "data_sources", ["source_type"])
    op.create_index("ix_data_sources_status", "data_sources", ["status"])
    op.create_index("ix_ingestion_tasks_code", "ingestion_tasks", ["code"])
    op.create_index("ix_ingestion_tasks_status", "ingestion_tasks", ["status"])
    op.create_index("ix_ingestion_batches_task_id", "ingestion_batches", ["task_id"])
    op.create_index("ix_ingestion_batches_status", "ingestion_batches", ["status"])
    op.create_index("ix_datasets_code", "datasets", ["code"])
    op.create_index("ix_datasets_data_layer", "datasets", ["data_layer"])
    op.create_index("ix_dataset_fields_dataset_id", "dataset_fields", ["dataset_id"])
    op.create_index("ix_quality_rules_code", "quality_rules", ["code"])
    op.create_index("ix_quality_rules_rule_type", "quality_rules", ["rule_type"])
    op.create_index("ix_quality_issues_quality_run_id", "quality_issues", ["quality_run_id"])
    op.create_index("ix_quality_issues_rule_id", "quality_issues", ["rule_id"])
    op.create_index("ix_audit_logs_action", "audit_logs", ["action"])
    op.create_index("ix_audit_logs_created_at", "audit_logs", ["created_at"])
    op.create_index("ix_file_assets_file_hash", "file_assets", ["file_hash"])
    op.create_index("ix_file_assets_batch_id", "file_assets", ["batch_id"])


def downgrade() -> None:
    """删除所有表。"""
    op.drop_table("data_lineage")
    op.drop_table("quality_issues")
    op.drop_table("quality_runs")
    op.drop_table("quality_rules")
    op.drop_table("data_tables")
    op.drop_table("dataset_fields")
    op.drop_table("datasets")
    op.drop_table("import_errors")
    op.drop_table("file_assets")
    op.drop_table("ingestion_batches")
    op.drop_table("ingestion_tasks")
    op.drop_table("connector_configs")
    op.drop_table("source_objects")
    op.drop_table("data_sources")
    op.drop_table("audit_logs")
    op.drop_table("role_permissions")
    op.drop_table("user_roles")
    op.drop_table("permissions")
    op.drop_table("roles")
    op.drop_table("users")
    op.drop_table("departments")
