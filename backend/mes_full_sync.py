"""
MES 全量同步 — 薄封装，凭据在此，引擎在 backfill_engine.py。

用法: python mes_full_sync.py
新增系统只需加一行 engine.run_system("srm", creds_srm)。
"""
from app.modules.ingestion.backfill_engine import BackfillEngine

# MES 凭据（后续迁移到 connector_configs.credential_ref 加密存储）
MES_CREDS = {
    "auth_credentials": "AABD820E8F78B30735DBCBC119C29D92",
    "auth_credentials_2": "8DD80B9CD20900A528D21E21AF83F220",
}

if __name__ == "__main__":
    engine = BackfillEngine()
    engine.run_system("mes_light", MES_CREDS)
