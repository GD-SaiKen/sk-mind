"""MES 全量历史回填 — 从探底日期逐天切片拉到今天。"""
import hashlib, json, time, uuid
from datetime import datetime, timedelta, timezone

import httpx
from sqlalchemy import create_engine, text
from app.core.config import settings

BASE = "https://a.lightmes.cn"
HEADERS = {
    "Content-Type": "application/json",
    "AccessKeyId": "AABD820E8F78B30735DBCBC119C29D92",
    "AccessKeySecret": "8DD80B9CD20900A528D21E21AF83F220",
}
NOW = datetime.now()
T_FMT = "%Y-%m-%d %H:%M:%S"
D_FMT = "%Y-%m-%d"
START_DATE = datetime(2026, 5, 5)  # 探底结果
TOTAL_DAYS = (NOW - START_DATE).days + 1
BATCH_ID = str(uuid.uuid4())
SYS = "mes_light"

# 需要按天切片的时间接口（每24小时一段）
TIME_IFACES = [
    ("03","工序报工数据查询","procedure_report",
     "/lightmesapi/open/workorderController/selectProceduresReportDataByTime","T"),
    ("04","工单排产参数查询","production_params",
     "/lightmesapi/open/workorderController/selectProductionBackParamsByTime","T"),
    ("05","查询投料明细","task_material",
     "/lightmesapi/open/workorderController/selectTaskUseMaterial","T"),
    ("06","工单工序查询","workorder_procedure",
     "/lightmesapi/open/workorderController/selectWorkorderProcedure","T"),
    ("07","工单报工数据查询","workorder_report",
     "/lightmesapi/open/workorderController/selectWorkorderReportDataByTime","T"),
    ("09","安灯报表","andon_report",
     "/lightmesapi/open/trilightSummary/andonApiController","D"),
    ("10","三色灯时间段消息数量","trilight_time_msgs",
     "/lightmesapi/open/trilightSummary/getTimecountMessagesByTimeSim","T"),
    ("11","三色灯时间段消息之和","trilight_count_sum",
     "/lightmesapi/open/trilightSummary/getTrilightCountByTimeSim","T"),
    ("14","三色灯指定时间效率","trilight_efficiency_duration",
     "/lightmesapi/open/trilightSummary/getTrilightEfficiencyDurationTime","T"),
    ("16","三色灯颜色变化信息","trilight_summary_duration",
     "/lightmesapi/open/trilightSummary/getTrilightSummaryDurationTime","T"),
    ("17","设备OEE报表","oee_report",
     "/lightmesapi/open/trilightSummary/selectOeeReport","D"),
    ("25","异常上报记录列表","error_report",
     "/lightmesapi/open/errorReportAPIController/selectErrorReport","D"),
]

DDL = (
    "CREATE TABLE IF NOT EXISTS {tbl} ("
    "  _raw_id BIGSERIAL PRIMARY KEY, _batch_id VARCHAR(64) NOT NULL,"
    "  _source_system VARCHAR(64) NOT NULL, _source_object VARCHAR(256) NOT NULL,"
    "  _source_row_hash VARCHAR(64) NOT NULL, _api_url VARCHAR(512) NOT NULL,"
    "  _api_request_params JSONB, _api_response_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),"
    "  _ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),"
    "  _is_deleted BOOLEAN NOT NULL DEFAULT FALSE, payload JSONB NOT NULL)"
)
INSERT_SQL = (
    "INSERT INTO {tbl} "
    "(_batch_id,_source_system,_source_object,_source_row_hash,"
    " _api_url,_api_request_params,_api_response_at,_ingested_at,payload) "
    "VALUES (:bid,:sys,:obj,:hash,:url,:params,:rat,:iat,:p) "
    "ON CONFLICT (_batch_id,_source_row_hash) DO NOTHING"
)

engine = create_engine(settings.DATABASE_URL_SYNC)
total_records = 0
day_count = 0

def pull_day(endpoint, body):
    """拉取单日单接口数据。"""
    r = httpx.post(BASE + endpoint, headers=HEADERS, json=body, timeout=30, verify=False)
    data = r.json()
    if not data.get("success"):
        return []
    records = data.get("data", [])
    if isinstance(records, dict):
        records = records.get("list", records.get("records", []))
    return records if isinstance(records, list) else []

shard = 1  # 用于 batch_id 分组
for offset in range(TOTAL_DAYS):
    day = START_DATE + timedelta(days=offset)
    day_end = day + timedelta(days=1)
    ts = day.strftime(T_FMT)
    te = day_end.strftime(T_FMT)
    ds = day.strftime(D_FMT)
    de = day_end.strftime(D_FMT)

    for num, name_cn, short, endpoint, fmt_type in TIME_IFACES:
        table_name = f"raw.{SYS}_{num}_{short}"
        tbl = table_name.split(".")[1]

        if fmt_type == "T":
            body = {"pageNum": 1, "pageSize": 500, "startTime": ts, "endTime": te}
        else:
            body = {"pageNum": 1, "pageSize": 500, "startDate": ds, "endDate": de}
            if "date" in str(endpoint):  # 25 uses single date
                body = {"pageNum": 1, "pageSize": 500, "date": ts}

        try:
            records = pull_day(endpoint, body)
            if not records:
                continue

            # Ensure table
            with engine.connect() as conn:
                conn.execute(text(DDL.format(tbl=table_name)))
                conn.execute(text(f"CREATE UNIQUE INDEX IF NOT EXISTS uq_{tbl}_dedup ON {table_name} (_batch_id,_source_row_hash)"))
                conn.commit()

            count = 0
            with engine.connect() as conn:
                for rec in records:
                    rhash = hashlib.sha256(json.dumps(rec,sort_keys=True,ensure_ascii=False,default=str).encode()).hexdigest()[:16]
                    conn.execute(text(INSERT_SQL.format(tbl=table_name)), {
                        "bid": BATCH_ID,"sys":SYS,"obj":short,"hash":rhash,
                        "url":endpoint,"params":json.dumps(body),
                        "rat":datetime.now(timezone.utc),"iat":datetime.now(timezone.utc),
                        "p":json.dumps(rec,ensure_ascii=False,default=str),
                    })
                    count += 1
                conn.commit()

            if count > 0:
                total_records += count
                print(f"  {day.strftime('%m-%d')} {name_cn:20s} {count:5d} rows")

            time.sleep(0.08)  # ~10 QPS

        except Exception as e:
            pass  # skip individual failures

    day_count += 1
    if day_count % 10 == 0:
        print(f"  --- day {day_count}/{TOTAL_DAYS} ({day.strftime('%m-%d')}), {total_records} total ---")

print(f"\n{'='*60}")
print(f"Backfill complete: {TOTAL_DAYS} days, {total_records} total records")
print(f"Batch: {BATCH_ID[:8]}")

# Summary by interface
with engine.connect() as conn:
    r = conn.execute(text(
        "SELECT _source_object, count(*) FROM raw.mes_light_03_procedure_report WHERE _batch_id=:bid GROUP BY 1 ORDER BY 2 DESC"
    ), {"bid": BATCH_ID})
    print("\nSample breakdown (procedure_report):")
    for row in r:
        print(f"  {row[0]}: {row[1]}")
