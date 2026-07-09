"""通用全量回溯引擎 — 读 DB 配置驱动，不绑定任何系统。"""
import hashlib, json, time as tm, uuid
from datetime import datetime, timedelta, timezone
import httpx
from sqlalchemy import create_engine, text
from app.core.config import settings


class BackfillEngine:
    def __init__(self):
        self._db = create_engine(settings.DATABASE_URL_SYNC)

    def run_system(self, system, credentials=None):
        """全量回溯。credentials = {auth_credentials, auth_credentials_2}（凭据由调用方传入）。"""
        creds = credentials or {}
        cfg = self._sys_cfg(system)
        if not cfg: return
        batch = str(uuid.uuid4())[:12]
        start = cfg["start_date"]
        ifaces = self._ifaces(system)
        non_t = [i for i in ifaces if not i["is_time_based"]]
        time_t = [i for i in ifaces if i["is_time_based"]]
        now = datetime.now()

        if non_t:
            print("Phase A: Non-time (%s)" % datetime.now().strftime("%H:%M:%S"))
            for i in non_t: self._pull_non_time(system, i, batch, creds)

        if time_t:
            td = (now - start).days
            print("\nPhase B: Time-based (%s)" % datetime.now().strftime("%H:%M:%S"))
            print("  Span: %s -> %s (%d days)\n" % (start.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d"), td))
            for i in time_t: self._pull_time(system, i, start, now, batch, creds)

        self._update_registry(system, ifaces)

    # ── DB ────────────────────────────────────

    def _sys_cfg(self, system):
        with self._db.connect() as c:
            r = c.execute(text(
                "SELECT history_start_date,time_window_days,time_param_start,time_param_end,time_format,time_field_day_only"
                " FROM sync_source_config WHERE source_system=:s"), {"s": system}).fetchone()
            if not r: return None
            r = dict(r._mapping)
            return {"start_date": r["history_start_date"] or datetime(2020,1,1),
                    "time_param_start": r["time_param_start"], "time_param_end": r["time_param_end"],
                    "time_format": r["time_format"]}

    def _ifaces(self, system):
        rows = []
        with self._db.connect() as c:
            for row in c.execute(text(
                "SELECT interface_num,interface_name,short_name,endpoint,is_time_based,time_config_key,request_body"
                " FROM sync_interface_config WHERE source_system=:s AND is_active=TRUE ORDER BY interface_num"
            ), {"s": system}):
                row = dict(row._mapping)
                body = row["request_body"] or {}
                if isinstance(body, str): body = json.loads(body)
                rows.append({"num": row["interface_num"], "name": row["interface_name"],
                             "short": row["short_name"], "endpoint": row["endpoint"],
                             "is_time_based": row["is_time_based"], "time_config_key": row["time_config_key"],
                             "request_body": body})
        return rows

    def _conn_info(self, system, creds):
        with self._db.connect() as c:
            r = c.execute(text(
                "SELECT cc.host, cc.extra_config FROM connector_configs cc"
                " JOIN data_sources ds ON cc.data_source_id=ds.id"
                " WHERE ds.code=:s AND cc.config_type='api_config'"
            ), {"s": system}).fetchone()
            if not r: raise ValueError("No connector for %s" % system)
            r = dict(r._mapping)
            extra = r["extra_config"] or {}
            if isinstance(extra, str): extra = json.loads(extra)
            base_url = r["host"]
            headers = {"Content-Type": "application/json"}

            # Apply dual_key auth
            auth_type = extra.get("auth_type")
            if auth_type == "dual_key" and creds.get("auth_credentials"):
                headers[extra.get("auth_header_name", "AccessKeyId")] = creds["auth_credentials"]
                headers[extra.get("auth_header_name_2", "AccessKeySecret")] = creds.get("auth_credentials_2", "")
            return base_url, headers

    def _res_time_cfg(self, key, fallback):
        if not key: return fallback
        cfg = self._sys_cfg(key)
        return cfg or fallback

    # ── Pull ──────────────────────────────────

    def _post(self, base_url, headers, endpoint, body, retries=3):
        for a in range(retries):
            try: return httpx.post(base_url + endpoint, headers=headers, json=body, timeout=30, verify=False)
            except Exception:
                if a == retries - 1: raise
                tm.sleep(2 ** a)

    def _table(self, system, num, short):
        return "raw.%s_%s_%s" % (system, num, short)

    def _ensure(self, tn):
        t = tn.split(".")[1]
        with self._db.begin() as c:
            c.execute(text("CREATE TABLE IF NOT EXISTS %s (_raw_id BIGSERIAL PRIMARY KEY,_batch_id VARCHAR(64) NOT NULL,_source_system VARCHAR(64) NOT NULL,_source_object VARCHAR(256) NOT NULL,_source_row_hash VARCHAR(64) NOT NULL,_api_url VARCHAR(512) NOT NULL,_api_request_params JSONB,_api_response_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),_ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),_is_deleted BOOLEAN NOT NULL DEFAULT FALSE,payload JSONB NOT NULL)" % tn))
            c.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS uq_%s_dedup ON %s (_batch_id,_source_row_hash)" % (t, tn)))

    def _insert(self, tn, system, short, endpoint, body, recs, batch):
        c = 0
        with self._db.begin() as conn:
            for rec in recs:
                rh = hashlib.sha256(json.dumps(rec, sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()[:16]
                conn.execute(text("INSERT INTO %s (_batch_id,_source_system,_source_object,_source_row_hash,_api_url,_api_request_params,_api_response_at,_ingested_at,payload) VALUES (:bid,:sys,:obj,:hash,:url,:params,:rat,:iat,:p) ON CONFLICT (_batch_id,_source_row_hash) DO NOTHING" % tn),
                    {"bid": batch, "sys": system, "obj": short, "hash": rh, "url": endpoint, "params": json.dumps(body),
                     "rat": datetime.now(timezone.utc), "iat": datetime.now(timezone.utc), "p": json.dumps(rec, ensure_ascii=False, default=str)})
                c += 1
        return c

    def _pull_non_time(self, system, iface, batch, creds):
        base_url, headers = self._conn_info(system, creds)
        tn = self._table(system, iface["num"], iface["short"]); self._ensure(tn)
        count = 0; page = 1
        while True:
            body = {**iface["request_body"], "pageNum": page, "pageSize": 100}
            r = self._post(base_url, headers, iface["endpoint"], body); d = r.json()
            if not d.get("success"): break
            recs = d.get("data")
            if isinstance(recs, dict): recs = recs.get("list", recs.get("records", []))
            if not recs: break
            count += self._insert(tn, system, iface["short"], iface["endpoint"], body, recs, batch)
            if len(recs) < 100: break
            page += 1; tm.sleep(0.1)
        print("  [+] %s %-25s %6d" % (iface["num"], iface["short"], count))

    def _pull_time(self, system, iface, start, now, batch, creds):
        base_url, headers = self._conn_info(system, creds)
        tn = self._table(system, iface["num"], iface["short"]); self._ensure(tn)
        tc_key = iface["time_config_key"] or system
        tc = self._res_time_cfg(tc_key, self._sys_cfg(system))
        ps, pe, fmt = tc["time_param_start"], tc["time_param_end"], tc["time_format"]

        count = 0; cur = start; es = 0; days = 0; td = (now - start).days
        while cur <= now:
            we = cur + timedelta(days=1)
            body = {**iface["request_body"], "pageNum": 1, "pageSize": 100, ps: cur.strftime(fmt)}
            if pe: body[pe] = we.strftime(fmt)
            try:
                r = self._post(base_url, headers, iface["endpoint"], body); d = r.json()
                if d.get("success"):
                    recs = d.get("data")
                    if isinstance(recs, dict): recs = recs.get("list", recs.get("records", []))
                    if recs: es = 0; count += self._insert(tn, system, iface["short"], iface["endpoint"], body, recs, batch)
                    else: es += 1
                else: es += 1
            except Exception: es += 1
            if es >= 400: break
            days += 1; cur += timedelta(days=1)
            if days % 5 == 0 or (count > 0 and cur.day == 1):
                pct = min(99, days * 100 // td) if td > 0 else 99
                bar = "#" * (pct // 4) + "." * (25 - pct // 4)
                hit = " last=%s" % cur.strftime("%Y-%m-%d") if es == 0 else ""
                print("\r  %s %s [%s] %3d%%  day %s  rows %d%s   " % (iface["num"], iface["short"], bar, pct, cur.strftime("%Y-%m-%d"), count, hit), end="")
            tm.sleep(0.05)
        mark = "+" if count > 0 else "-"
        print("\r  [%s] %s %-25s %6d (%dd)%s" % (mark, iface["num"], iface["short"], count, days, " " * 40))

    def _update_registry(self, system, ifaces):
        with self._db.begin() as c:
            for i in ifaces:
                tn = self._table(system, i["num"], i["short"])
                c.execute(text("INSERT INTO raw_table_registry (raw_table_name,source_system,interface_num,interface_name,endpoint,http_method,doc_source,description) VALUES (:tbl,:sys,:num,:name,:ep,'POST','',:desc) ON CONFLICT (raw_table_name) DO UPDATE SET description=EXCLUDED.description"),
                    {"tbl": tn, "sys": system, "num": i["num"], "name": i["name"], "ep": i["endpoint"], "desc": "%s %s" % (system, i["name"])})
