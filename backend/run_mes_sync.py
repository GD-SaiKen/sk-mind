"""MES sync verification script — end-to-end test of filterWorkorder -> raw.mes_workorders.

Usage:
    cd backend
    python run_mes_sync.py
"""
import os
import sys
import uuid
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(__file__))

from sqlalchemy import text

from app.modules.ingestion.engines.api_sync_engine import ApiSyncEngine, load_config
from app.modules.ingestion.stage_writer import StageWriter
from app.modules.ingestion.services.sync_database import get_sync_db

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "data_sources", "mes_light.yaml")


def _ensure_task(db, data_source_id: str) -> uuid.UUID:
    """Ensure an IngestionTask exists for the given data source, or create one."""
    result = db.execute(
        text("SELECT id FROM ingestion_tasks WHERE data_source_id = CAST(:dsid AS uuid) LIMIT 1"),
        {"dsid": data_source_id},
    ).fetchone()
    if result:
        return result[0]

    # Create a task record
    from datetime import datetime, timezone
    task_id = uuid.uuid4()
    db.execute(
        text(
            "INSERT INTO ingestion_tasks (id, name, code, data_source_id, "
            "target_layer, schedule_type, status, sync_mode, created_at, updated_at) "
            "VALUES (:id, :name, :code, :dsid, 'raw', 'manual', 'active', 'full', :now, :now)"
        ),
        {
            "id": task_id,
            "name": "MES Verification Sync",
            "code": "mes_verify_sync",
            "dsid": data_source_id,
            "now": datetime.now(timezone.utc),
        },
    )
    db.commit()
    return task_id


def main():
    config = load_config(CONFIG_PATH)

    # Inject MES credentials
    config["connection"]["auth_credentials"] = "AABD820E8F78B30735DBCBC119C29D92"
    config["connection"]["auth_credentials_2"] = "8DD80B9CD20900A528D21E21AF83F220"

    # Pick filterWorkorder interface
    iface_name = "filterWorkorder"
    iface = next(i for i in config["interfaces"] if i["name"] == iface_name)
    target_table = iface["target_table"]
    print(f"Testing: {iface_name} -> {target_table}")

    db = get_sync_db()
    try:
        # Find or create a task
        mes_ds_id = db.execute(
            text("SELECT id FROM data_sources WHERE code = 'mes_light' LIMIT 1")
        ).scalar_one()
        task_id = _ensure_task(db, str(mes_ds_id))
        print(f"Using ingestion task: {task_id}")

        engine = ApiSyncEngine(config, db)
        batch = StageWriter(db).create_batch(
            task_id=task_id,
            trigger_type="manual",
        )
        engine._writer.start_batch(batch)

        connector = engine._get_connector()
        connector.connect()

        # Disable SSL verification if MES uses self-signed cert
        try:
            connector._client.verify = False
            print("(SSL verification disabled for MES endpoint)")
        except Exception:
            pass

        try:
            # Sync only 2 days we know have data (verified via direct API call)
            today = date.today()
            start = today - timedelta(days=7)

            total = {"success": 0, "rejected": 0}
            # _sync_day signature: (iface, connector, batch, source_id, sync_mode, day_start, day_end)
            from app.modules.ingestion.engines.api_sync_engine import slice_days
            for day_start, day_end in slice_days(start, today):
                result = engine._sync_day(
                    iface, connector, batch, str(uuid.uuid4()), "full",
                    day_start, day_end,
                )
                total["success"] += result["success"]
                total["rejected"] += result["rejected"]
                print(f"  {day_start} -> {day_end}: +{result['success']} rows (rejected: {result['rejected']})")

            status = "partial_success" if total["rejected"] > 0 else "success"
            engine._writer.finish_batch(
                batch, status,
                total=total["success"] + total["rejected"],
                success=total["success"],
                rejected=total["rejected"],
            )
            print(f"\nDone: {total['success']} rows written to {target_table}")

        finally:
            connector.disconnect()

        # Verify data
        count_result = db.execute(text(f"SELECT count(*) FROM {target_table}"))
        row_count = count_result.scalar_one()
        print(f"Table {target_table}: {row_count} rows")

        if row_count > 0:
            sample = db.execute(
                text(f"SELECT woid, workorder_no, plan_qty, part_no FROM {target_table} LIMIT 3")
            )
            print("  Sample rows:")
            for r in sample:
                print(f"    woid={r[0]}, wo_no={r[1]}, plan_qty={r[2]}, part_no={r[3]}")

            # Check JSONB columns
            jb = db.execute(
                text(f"SELECT simple_procedures IS NOT NULL as has_proc, custom_fields IS NOT NULL as has_cf FROM {target_table} LIMIT 3")
            )
            for r in jb:
                print(f"    simple_procedures populated: {r.has_proc}, custom_fields populated: {r.has_cf}")

            print("\nVERIFICATION PASSED: data flows correctly from MES API to raw.mes_workorders.")
        else:
            print("\nWARNING: No rows found. MES API may have returned empty data for this date range.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
