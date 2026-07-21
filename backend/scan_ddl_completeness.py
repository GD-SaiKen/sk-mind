"""Comprehensive scan v2: test all 25 MES interfaces with correct params, compare DDL."""
import ssl, sys, json
sys.path.insert(0, '.')
from datetime import date
from sqlalchemy import text
from app.modules.ingestion.connectors.api_mapper import ColumnMapper
from app.modules.ingestion.engines.api_sync_engine import load_config
from app.modules.ingestion.services.sync_database import get_sync_db
import httpx

config = load_config('config/data_sources/mes_light.yaml')
CREDS_ID = 'AABD820E8F78B30735DBCBC119C29D92'
CREDS_SECRET = '8DD80B9CD20900A528D21E21AF83F220'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
client = httpx.Client(base_url='https://a.lightmes.cn', timeout=30, verify=ctx,
    headers={'AccessKeyId': CREDS_ID, 'AccessKeySecret': CREDS_SECRET})
db = get_sync_db()

# Known good params for each interface
PARAMS = {
    'filterWorkorder': {'pageNum':1,'pageSize':1,'startDate':'2026-07-20','endDate':'2026-07-21','workOrderStatus':[]},
    'selectComplishReport': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20','endTime':'2026-07-21','status':1},
    'selectProceduresReportDataByTime': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'selectProductionBackParamsByTime': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'selectTaskUseMaterial': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'selectWorkorderProcedure': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'selectWorkorderReportDataByTime': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'selectWorkorderTaskActionStatistics': {'pageNum':1,'pageSize':1},
    'andonApiController': {'pageNum':1,'pageSize':1,'statusList':[]},
    'getTimecountMessagesByTimeSim': {'pageNum':1,'pageSize':1,'sim':'','startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'getTrilightCountByTimeSim': {'pageNum':1,'pageSize':1,'sim':'','startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'getTrilightCurrentColor': {'sim':''},
    'getTrilightCurrentColorList': {'simList':['']},
    'getTrilightEfficiencyDurationTime': {'pageNum':1,'pageSize':1,'sim':'','startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'getTrilightEfficiencyOneDay': {'sim':'','date':'2026-07-20'},
    'getTrilightSummaryDurationTime': {'pageNum':1,'pageSize':1,'startTime':'2026-07-20 00:00:00','endTime':'2026-07-20 23:59:59'},
    'selectOeeReport': {'pageNum':1,'pageSize':1,'startDate':'2026-07-20','endDate':'2026-07-21'},
    'getMachineCount': {'tid':0},
    'getMachineDetailById': {'mid':0},
    'getMachineList': {'pageNum':1,'pageSize':1},
    'listDefs': {'pageNum':1,'pageSize':1,'entityType':'WORKORDER','enabledOnly':1},
    'listOptionalCustomFieldCodes': {'pageNum':1,'pageSize':1,'entityType':'WORKORDER','enabledOnly':1},
    'queryCraftHours': {'pageNum':1,'pageSize':1},
    'queryCraftHoursDetails': {'mtid':0},
    'selectErrorReport': {'pageNum':1,'pageSize':1,'date':'2026-07-20 00:00:00'},
}

problems = []
ok = []
ddl_issues = []

for idx, iface in enumerate(config['interfaces'], 1):
    name = iface['name']
    tbl = iface['target_table']
    endpoint = iface['endpoint']

    body = PARAMS.get(name, {'pageNum':1,'pageSize':1})

    try:
        r = client.post(endpoint, json=body)
        data = r.json()
    except Exception as e:
        problems.append((idx, name, tbl, f'CONNECT: {e}'))
        continue

    code = data.get('code')
    if code != 1000:
        problems.append((idx, name, tbl, f'API code={code} msg={data.get("message","")[:40]}'))
        continue

    dd = data.get('data')
    if dd is None:
        problems.append((idx, name, tbl, 'data is None'))
        continue

    # Extract records
    if isinstance(dd, list):
        recs = dd
    elif isinstance(dd, dict):
        recs = dd.get('list') or dd.get('data') or []
    elif isinstance(dd, int):
        # getMachineCount returns raw int
        recs = [{'data': dd}]
    else:
        problems.append((idx, name, tbl, f'unexpected data: {type(dd).__name__}'))
        continue

    if not recs:
        ok.append((idx, name, tbl, 'empty'))
        continue

    api_fields = set(recs[0].keys())
    schema, table_name = tbl.split('.', 1)

    ddl_rows = db.execute(text(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_schema = :schema AND table_name = :table "
        "AND column_name NOT LIKE '_\\_%' ESCAPE '\\'"
    ), {'schema': schema, 'table': table_name}).fetchall()
    ddl_cols = {r.column_name for r in ddl_rows}

    if not ddl_cols:
        problems.append((idx, name, tbl, 'TABLE NOT FOUND'))
        continue

    mapper = ColumnMapper(ddl_cols)
    api_snake = {mapper._to_snake(f) for f in api_fields}
    missing = api_snake - ddl_cols
    extra_biz = {e for e in (ddl_cols - api_snake) if not e.startswith('_')}

    if missing or extra_biz:
        ddl_issues.append((idx, name, tbl, missing, extra_biz))
    else:
        ok.append((idx, name, tbl, f'{len(recs)} record(s)'))

client.close()
db.close()

# Report
sep = '=' * 80
print(sep)
print(f'ALL 25 MES INTERFACES — DDL COMPLETENESS SCAN')
print(sep)

if problems:
    print(f'\n--- API PROBLEMS ({len(problems)}) ---')
    for idx, name, tbl, msg in problems:
        print(f'  [{idx}] {name}: {msg}')

if ddl_issues:
    print(f'\n--- DDL FIELD ISSUES ({len(ddl_issues)}) ---')
    for idx, name, tbl, missing, extra in ddl_issues:
        print(f'  [{idx}] {name} -> {tbl}')
        if missing:
            print(f'    MISSING: {", ".join(sorted(missing))}')
        if extra:
            print(f'    EXTRA:   {", ".join(sorted(extra))}')

print(f'\n--- OK ({len(ok)}) ---')
for idx, name, tbl, detail in ok:
    print(f'  [{idx}] {name}: {detail}')

print(f'\n{sep}')
print(f'Summary: {len(ok)} OK | {len(ddl_issues)} DDL issues | {len(problems)} API problems')
print(sep)
