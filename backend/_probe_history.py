"""MES 历史数据探底 — 找到真实最早数据点，确定回溯起点。"""
import httpx, json
from datetime import datetime, timedelta

BASE = "https://a.lightmes.cn"
HEADERS = {
    "Content-Type": "application/json",
    "AccessKeyId": "AABD820E8F78B30735DBCBC119C29D92",
    "AccessKeySecret": "8DD80B9CD20900A528D21E21AF83F220",
}

def post(endpoint, body):
    r = httpx.post(BASE + endpoint, headers=HEADERS, json=body, timeout=30, verify=False)
    return r.json()

# ── 策略1: 用工单表精准探底 ─────────────────
print("=" * 60)
print("Phase 1a: 工单全覆盖拉取，找最早 createTime")
print("=" * 60)

all_wo = []
page = 1
while True:
    data = post("/lightmesapi/open/workorderController/filterWorkorder",
                {"pageNum": page, "pageSize": 200, "workOrderStatus": [1,2,3,4,5,6]})
    if not data.get("success"):
        break
    records = data.get("data", [])
    if isinstance(records, dict):
        records = records.get("list", records.get("records", []))
    if not records:
        break
    all_wo.extend(records)
    print(f"  page {page}: {len(records)} records, total so far: {len(all_wo)}")
    if len(records) < 200:
        break
    page += 1

if all_wo:
    times = [r.get("createTime") for r in all_wo if r.get("createTime")]
    times.sort()
    earliest_wo = times[0] if times else None
    latest_wo = times[-1] if times else None
    print(f"\n  Earliest workorder: {earliest_wo}")
    print(f"  Latest workorder:   {latest_wo}")
    print(f"  Total workorders:   {len(all_wo)}")
else:
    earliest_wo = None
    print("  No workorders found!")

# ── 策略2: 时间接口二分探底 ─────────────────
print("\n" + "=" * 60)
print("Phase 1b: 时间接口二分探底")
print("=" * 60)

NOW = datetime.now()
T_FMT = "%Y-%m-%d %H:%M:%S"

# 用报工接口作为探针（数据量最大的时间接口）
PROBE_ENDPOINT = "/lightmesapi/open/workorderController/selectWorkorderReportDataByTime"

def has_data(days_ago):
    """检查 N 天前那天是否有数据。"""
    d = NOW - timedelta(days=days_ago)
    body = {
        "pageNum": 1, "pageSize": 1,
        "startTime": d.strftime(T_FMT),
        "endTime": (d + timedelta(days=1)).strftime(T_FMT),
    }
    data = post(PROBE_ENDPOINT, body)
    records = data.get("data", [])
    if isinstance(records, dict):
        records = records.get("list", [])
    return len(records) > 0 if isinstance(records, list) else False

# 二分找最早有数据的天数
lo, hi = 1, 365 * 3  # 3 年范围
found_any = False
while lo < hi:
    mid = (lo + hi) // 2
    if has_data(mid):
        lo = mid + 1
        found_any = True
        print(f"  day -{mid}: has data, probing deeper...")
    else:
        hi = mid
        print(f"  day -{mid}: no data, narrowing...")

earliest_day = lo - 1 if found_any else 0
earliest_probe_date = (NOW - timedelta(days=earliest_day)).strftime("%Y-%m-%d") if found_any else "N/A"
print(f"\n  Earliest day with data: -{earliest_day} days ({earliest_probe_date})")

# ── 结论 ───────────────────────────────────
print("\n" + "=" * 60)
print("结论")
print("=" * 60)

# 取两者中更早的
if earliest_wo:
    try:
        wo_date = datetime.strptime(earliest_wo[:10], "%Y-%m-%d")
    except:
        wo_date = None
else:
    wo_date = None

if wo_date and earliest_day:
    start_date = min(wo_date, NOW - timedelta(days=earliest_day))
elif wo_date:
    start_date = wo_date
elif earliest_day:
    start_date = NOW - timedelta(days=earliest_day)
else:
    start_date = NOW - timedelta(days=180)  # fallback

lookback = (NOW - start_date).days
print(f"  回溯起点: {start_date.strftime('%Y-%m-%d')}")
print(f"  回溯天数: {lookback} 天")
print(f"  建议切片: {lookback} 天 × 12 个时间接口 = ~{lookback * 12} 次请求")
print(f"  预估耗时: ~{lookback * 12 / 10 / 60:.1f} 分钟 @ 10 QPS")
