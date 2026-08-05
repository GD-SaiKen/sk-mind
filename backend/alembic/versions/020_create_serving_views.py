"""create serving schema + 8 serving views + UNIQUE constraint on semantic_properties

Revision ID: 020
Revises: 019
Create Date: 2026-07-30

Phase 1: 数据同步策略 — serving 视图层 + loader upsert 支持。
"""

from typing import Sequence, Union

from alembic import op

revision: str = "020"
down_revision: Union[str, None] = "019"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── 1. UNIQUE constraint for loader upsert ──
    op.execute("""
        ALTER TABLE semantic_properties
        ADD CONSTRAINT uq_semantic_properties_object_code
        UNIQUE (semantic_object_id, code)
    """)

    # ── 2. Create serving schema ──
    op.execute("CREATE SCHEMA IF NOT EXISTS serving")

    # ──────────────────────────────────────────────────────
    # 3. 8 Serving Views (in dependency order)
    # ──────────────────────────────────────────────────────

    # 3.1 machine_dim_v1 — 设备维度表
    op.execute("""
        CREATE OR REPLACE VIEW serving.machine_dim_v1 AS
        SELECT
            mid,
            REPLACE(machine_no, '～', '~') AS machine_no,
            machine_name,
            sim,
            status,
            department_name,
            CASE department_name
                WHEN '装配一车间' THEN 'workshop_1'
                WHEN '装配二车间' THEN 'workshop_2'
                WHEN '机加车间' THEN 'machining'
                WHEN '钣金车间' THEN 'sheet_metal'
                WHEN '涂装车间' THEN 'painting'
                WHEN '总装车间' THEN 'final_assembly'
                ELSE department_name
            END AS workshop,
            _ingested_at
        FROM raw.mes_get_machine_list
    """)
    op.execute("""
        COMMENT ON VIEW serving.machine_dim_v1 IS
        '设备维度视图。来源: raw.mes_get_machine_list。
         车间映射规则: department_name → workshop (装配一车间→workshop_1, 装配二车间→workshop_2, 机加车间→machining, 钣金车间→sheet_metal, 涂装车间→painting, 总装车间→final_assembly, 其他保持原值)。
         machine_no 中的全角波浪号 ～ 替换为半角 ~。'
    """)

    # 3.2 andon_v1 — Andon 事件视图
    op.execute("""
        CREATE OR REPLACE VIEW serving.andon_v1 AS
        SELECT
            ar_id,
            machine_no,
            to_timestamp(create_date::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' AS create_date,
            andon_title,
            to_timestamp(receive_date::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' AS receive_date,
            receive_time / 60.0 AS response_minutes,
            finish_time / 60.0 AS processing_minutes,
            all_time / 60.0 AS total_minutes,
            submit_name,
            finish_name,
            mes_explain,
            remark,
            note,
            andon_status,
            standard_duration,
            standard_response_time / 60.0 AS standard_response_minutes,
            standard_processing_time / 60.0 AS standard_processing_minutes,
            (receive_time > standard_response_time) AS is_response_timeout,
            (finish_time > standard_processing_time) AS is_processing_timeout,
            -- Shift inference from create_date
            CASE
                WHEN EXTRACT(HOUR FROM to_timestamp(create_date::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai') BETWEEN 6 AND 13 THEN '白班'
                WHEN EXTRACT(HOUR FROM to_timestamp(create_date::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai') BETWEEN 14 AND 21 THEN '中班'
                ELSE '夜班'
            END AS shift,
            NULL::VARCHAR(64) AS product_code,    -- placeholder: 需从 JSONB 提取，v2 处理
            NULL::VARCHAR(128) AS product_name,   -- placeholder: 需从 JSONB 提取，v2 处理
            NULL::VARCHAR(64) AS mould_no,        -- placeholder: 需从 JSONB 提取，v2 处理
            _ingested_at
        FROM raw.mes_andon_api_controller
        WHERE create_date ~ '^\\d+$'
          AND COALESCE(receive_date::text, '0') ~ '^\\d+$'
    """)
    op.execute("""
        COMMENT ON VIEW serving.andon_v1 IS
        'Andon 事件视图。来源: raw.mes_andon_api_controller。
         create_date/receive_date 存 BIGINT 毫秒时间戳，用 to_timestamp(col::bigint/1000.0) AT TIME ZONE ''Asia/Shanghai'' 转换。
         response_minutes/processing_minutes/total_minutes: 秒 → 分钟。
         is_response_timeout / is_processing_timeout: 超时判断。
         shift: 根据 create_date 小时推断 (6-13白班, 14-21中班, 其他夜班)。
         product_code/product_name/mould_no: NULL 占位，需从 JSONB 提取，v2 处理。'
    """)

    # 3.3 error_report_v1 — 故障报告视图 (依赖 machine_dim_v1)
    op.execute("""
        CREATE OR REPLACE VIEW serving.error_report_v1 AS
        SELECT
            e.lwl_id,
            e.machine_no,
            e.machine_name,
            e.machine_status_name,
            e.work_date,
            e.shift_name,
            e.shift_start_date,
            e.shift_end_date,
            CASE e.color
                WHEN 'green' THEN '绿'
                WHEN 'yellow' THEN '黄'
                WHEN 'red' THEN '红'
                WHEN 'gray' THEN '灰(关机)'
                ELSE e.color
            END AS color,
            e.reason_code,
            e.wait_reason,
            e.reason_classification,
            e.wait_start_time,
            e.wait_end_time,
            e.duration,
            e.workorder_no,
            e.material_no,
            e.user_name,
            e.description,
            m.workshop,
            e._ingested_at
        FROM raw.mes_select_error_report e
        LEFT JOIN serving.machine_dim_v1 m ON REPLACE(e.machine_no, '～', '~') = m.machine_no
    """)
    op.execute("""
        COMMENT ON VIEW serving.error_report_v1 IS
        '故障报告视图。来源: raw.mes_select_error_report + LEFT JOIN machine_dim_v1。
         color: 英文字符串 → 中文映射 (green→绿, yellow→黄, red→红, gray→灰(关机))。
         workshop: 通过 machine_dim_v1 JOIN 获取车间映射。'
    """)

    # 3.4 oee_v1 — OEE 报告视图 (依赖 machine_dim_v1)
    op.execute("""
        CREATE OR REPLACE VIEW serving.oee_v1 AS
        SELECT
            o.mid,
            o.department_name,
            o.machine_no,
            o.machine_name,
            o.sim_date,
            o.shift_name,
            o.start_time,
            o.end_time,
            o.red_time / 60.0 AS red_minutes,
            o.green_time / 60.0 AS green_minutes,
            o.yellow_time / 60.0 AS yellow_minutes,
            o.close_time / 60.0 AS close_minutes,
            o.green_total_time / 60.0 AS green_total_minutes,
            -- green_rate 重算：灰灯(关机)放分母
            CASE
                WHEN (o.green_time + o.red_time + o.yellow_time + o.close_time) > 0
                THEN o.green_time / (o.green_time + o.red_time + o.yellow_time + o.close_time)
                ELSE 0
            END AS green_rate,
            o.red_rate,
            o.yellow_rate,
            o.close_rate,
            o.actual_rate,
            o.effective_yellow_time / 60.0 AS effective_yellow_minutes,
            o.effective_green_rate,
            o.actual_yellow_rate,
            o.performance_rate,
            o.oee_rate,
            o.run_oee_rate,
            o.standard_rate,
            o.user_name,
            o.green_compensation,
            o.wait_count,
            o.fault_count,
            o.good_qty,
            o.stop_time / 60.0 AS stop_minutes,
            o.stop_green / 60.0 AS stop_green_minutes,
            o.stop_free / 60.0 AS stop_free_minutes,
            o.andon_time / 60.0 AS andon_minutes,
            o.andon_rate,
            o.red_hour,
            o.green_hour,
            o.yellow_hour,
            o.close_hour,
            o.green_total_hour,
            o.shift_green_rate,
            o.shift_green_time / 60.0 AS shift_green_minutes,
            o.online_time / 60.0 AS online_minutes,
            -- is_low_efficiency: oee_rate < 0.6
            (COALESCE(o.oee_rate, 0) < 0.6) AS is_low_efficiency,
            m.workshop,
            o._ingested_at
        FROM raw.mes_select_oee_report o
        LEFT JOIN serving.machine_dim_v1 m ON REPLACE(o.machine_no, '～', '~') = m.machine_no
    """)
    op.execute("""
        COMMENT ON VIEW serving.oee_v1 IS
        'OEE 报告视图。来源: raw.mes_select_oee_report + LEFT JOIN machine_dim_v1。
         秒 → 分钟转换: red/green/yellow/close/stop/andon/online/shift_green 时间字段除以 60。
         green_rate 重算: 灰灯(关机时间)放入分母统计。
         is_low_efficiency: oee_rate < 0.6 标记低效。
         workshop: 通过 machine_dim_v1 JOIN 获取。'
    """)

    # 3.5 reporting_v1 — 生产报工视图 (依赖 machine_dim_v1)
    op.execute("""
        CREATE OR REPLACE VIEW serving.reporting_v1 AS
        SELECT
            r.wtaid,
            r.wtid,
            r.woid,
            r.workorder_no,
            r.workorder_type,
            r.task_no,
            r.rpid,
            r.procedure_no,
            r.procedure_name,
            r.procedure_remark,
            r.mtid,
            r.material_no,
            r.material_desc,
            r.material_spec,
            r.unit,
            r.routings_material_no,
            r.mid,
            r.machine_no,
            r.machine_name,
            r.workcenter_no,
            r.workcenter_name,
            r.department_name,
            r.plan_qty,
            r.workorder_plan_qty,
            r.production_qty,
            r.good_qty,
            r.bad_qty_manufacturing,
            r.bad_qty_incoming,
            r.isolation_bad_qty,
            -- total_qty = yield + defect
            COALESCE(r.good_qty, 0) + COALESCE(r.bad_qty_manufacturing, 0) + COALESCE(r.bad_qty_incoming, 0) AS total_qty,
            -- yield_rate
            CASE
                WHEN COALESCE(r.good_qty, 0) + COALESCE(r.bad_qty_manufacturing, 0) + COALESCE(r.bad_qty_incoming, 0) > 0
                THEN r.good_qty / (COALESCE(r.good_qty, 0) + COALESCE(r.bad_qty_manufacturing, 0) + COALESCE(r.bad_qty_incoming, 0))
                ELSE 0
            END AS yield_rate,
            r.in_stock_qty,
            r.in_stock_rate,
            r.total_complete_qty,
            r.check_qty,
            r.produce_hours,
            r.machine_hours,
            r.people_hours,
            r.earned_hours,
            r.compensate_hours,
            r.actual_people_hours,
            r.compensate_work_hours,
            r.plan_work_time,
            r.start_time,
            r.end_time,
            r.green_duration / 60.0 AS green_minutes,
            r.yellow_duration / 60.0 AS yellow_minutes,
            r.red_duration / 60.0 AS red_minutes,
            r.close_duration / 60.0 AS close_minutes,
            r.andon_duration / 60.0 AS andon_minutes,
            r.effective_duration / 60.0 AS effective_minutes,
            r.free_time / 60.0 AS free_time_minutes,
            r.theoretical_duration / 60.0 AS theoretical_minutes,
            r.plan_complete_rate,
            r.standard_complete_rate,
            r.production_rate,
            r.green_rate,
            r.good_rate,
            r.oee_rate,
            r.man_output_rate,
            r.utilization_rate,
            r.mould_list,
            r.time_mould_change,
            r.actual_time_mould_change,
            r.single_trip_qty,
            r.actual_single_trip_qty,
            r.single_trip_qty_rate,
            r.single_trip_time,
            r.actual_single_trip_time,
            r.unit_price,
            r.amount,
            r.operator_list,
            r.operation_count,
            r.user_name,
            r.conversion_coefficient,
            r.coefficient,
            r.second_coefficient,
            r.main_coefficient,
            r.material_batch_no,
            r.production_batch_no,
            r.shift_time_name,
            r.shift_capacity,
            r.task_count,
            r.task_action_remark,
            r.workorder_remark,
            r.plan_follow_word_no,
            r.salesorder_no,
            r.customization_no,
            -- is_empty: no production (good_qty + bad = 0)
            (COALESCE(r.good_qty, 0) + COALESCE(r.bad_qty_manufacturing, 0) + COALESCE(r.bad_qty_incoming, 0) = 0) AS is_empty,
            -- shift inference from start_time
            CASE
                WHEN EXTRACT(HOUR FROM r.start_time) BETWEEN 6 AND 13 THEN '白班'
                WHEN EXTRACT(HOUR FROM r.start_time) BETWEEN 14 AND 21 THEN '中班'
                ELSE '夜班'
            END AS shift,
            m.workshop,
            r._ingested_at
        FROM raw.mes_select_workorder_task_action_statistics r
        LEFT JOIN serving.machine_dim_v1 m ON REPLACE(r.machine_no, '～', '~') = m.machine_no
    """)
    op.execute("""
        COMMENT ON VIEW serving.reporting_v1 IS
        '生产报工视图。来源: raw.mes_select_workorder_task_action_statistics + LEFT JOIN machine_dim_v1。
         total_qty: good_qty + bad_qty_manufacturing + bad_qty_incoming。
         yield_rate: good_qty / total_qty。
         is_empty: good_qty + bad = 0 时标记为空班次。
         shift: 根据 start_time 小时推断 (6-13白班, 14-21中班, 其他夜班)。
         workshop: 通过 machine_dim_v1 JOIN 获取。'
    """)

    # 3.6 workorder_v1 — 工单视图
    op.execute("""
        CREATE OR REPLACE VIEW serving.workorder_v1 AS
        WITH t AS (
            SELECT *,
                CASE WHEN create_time IS NOT NULL AND create_time <> '' AND create_time ~ '^[0-9]+$'
                     THEN to_timestamp(create_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _create_dt,
                CASE WHEN start_time IS NOT NULL AND start_time <> '' AND start_time ~ '^[0-9]+$'
                     THEN to_timestamp(start_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _start_dt,
                CASE WHEN end_time IS NOT NULL AND end_time <> '' AND end_time ~ '^[0-9]+$'
                     THEN to_timestamp(end_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _end_dt,
                CASE WHEN require_end_time IS NOT NULL AND require_end_time <> '' AND require_end_time ~ '^[0-9]+$'
                     THEN to_timestamp(require_end_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _require_dt,
                CASE WHEN estimated_start_time IS NOT NULL AND estimated_start_time <> '' AND estimated_start_time ~ '^[0-9]+$'
                     THEN to_timestamp(estimated_start_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _estimated_start_dt,
                CASE WHEN estimated_end_time IS NOT NULL AND estimated_end_time <> '' AND estimated_end_time ~ '^[0-9]+$'
                     THEN to_timestamp(estimated_end_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _estimated_end_dt,
                CASE WHEN actual_complete_time IS NOT NULL AND actual_complete_time <> '' AND actual_complete_time ~ '^[0-9]+$'
                     THEN to_timestamp(actual_complete_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _actual_dt,
                CASE WHEN close_time IS NOT NULL AND close_time <> '' AND close_time ~ '^[0-9]+$'
                     THEN to_timestamp(close_time::bigint / 1000.0) AT TIME ZONE 'Asia/Shanghai' END AS _close_dt
            FROM raw.mes_filter_workorder
        )
        SELECT
            woid,
            workorder_no,
            workorder_type,
            urgent_level,
            mtid,
            material_no,
            material_desc,
            material_spec,
            unit,
            (plan_qty)::numeric AS plan_qty,
            (completed_qty)::numeric AS completed_qty,
            (surplus_qty)::numeric AS surplus_qty,
            (order_qty)::numeric AS order_qty,
            (portion_qty)::numeric AS portion_qty,
            (arranged_qty)::numeric AS arranged_qty,
            (complete_progress)::numeric AS complete_progress,
            CASE (status)::integer
                WHEN 1 THEN '待确认'
                WHEN 2 THEN '异常'
                WHEN 3 THEN '已确认'
                WHEN 5 THEN '部分确认'
                WHEN 9 THEN '已结产'
                ELSE ('状态' || status)
            END AS status,
            CASE
                WHEN COALESCE((plan_qty)::numeric, 0) > 0
                THEN COALESCE((completed_qty)::numeric, 0) / (plan_qty)::numeric * 100
                ELSE 0
            END AS progress_pct,
            (_require_dt IS NOT NULL AND _require_dt < NOW() AND (status)::integer <> 9) AS is_overdue,
            CASE
                WHEN _require_dt IS NOT NULL AND _require_dt < NOW() AND (status)::integer <> 9
                THEN EXTRACT(DAY FROM NOW() - _require_dt)::int
                ELSE 0
            END AS overdue_days,
            _create_dt AS create_time,
            _start_dt AS start_time,
            _end_dt AS end_time,
            _require_dt AS require_end_time,
            _estimated_start_dt AS estimated_start_time,
            _estimated_end_dt AS estimated_end_time,
            _actual_dt AS actual_complete_time,
            _close_dt AS close_time,
            customer_no,
            customization_no,
            customer_requirement,
            customer_material_code,
            customer_material_name,
            sales,
            salesorder_no,
            plan_follow_word_no,
            order_master,
            project_number,
            order_number,
            current_procedure,
            next_procedure,
            all_procedure,
            routings_material_no,
            material_status,
            create_tuid,
            create_user_name,
            close_uid,
            close_user_name,
            (material_price)::numeric AS material_price,
            (material_total_price)::numeric AS material_total_price,
            (standard_work_hours)::numeric AS standard_work_hours,
            error_info,
            notes,
            remark,
            close_remark,
            (overdue_count)::numeric AS overdue_count,
            (print_number)::numeric AS print_number,
            material_ledger_desc,
            material_ledger_spec,
            supplier,
            NULL::character varying(128) AS workshop,
            _ingested_at
        FROM t
    
    """)
    op.execute("""
        COMMENT ON VIEW serving.workorder_v1 IS
        '工单视图。来源: raw.mes_filter_workorder。
         status 映射(MES 枚举): 1→待确认, 2→异常, 3→已确认, 5→部分确认, 9→已结产。
         progress_pct: completed_qty/plan_qty * 100。
         is_overdue: require_end_time < NOW() 且未完工/未关闭时标记超期。
         overdue_days: 超期天数。
         workshop: NULL 占位 (工单表无 machine 字段，需通过其他方式关联)。
         时间列: raw 层存 BIGINT 毫秒时间戳(text)，用 to_timestamp(col::bigint/1000.0) AT TIME ZONE ''Asia/Shanghai'' 转换，空/非法值返回 NULL。'
    
    """)

    # 3.7 schedule_v1 — 排产任务视图
    op.execute("""
        CREATE OR REPLACE VIEW serving.schedule_v1 AS
        SELECT
            wopid,
            workorder_no,
            salesorder_no,
            material_no,
            material_desc,
            material_spec,
            procedure_no,
            procedure_name,
            plan_follow_word_no,
            plan_qty,
            pending_qty,
            arranged_qty,
            completed_qty,
            procedure_order,
            completion_stage,
            -- completion_rate
            CASE
                WHEN COALESCE(plan_qty, 0) > 0 THEN COALESCE(completed_qty, 0) / plan_qty
                ELSE 0
            END AS completion_rate,
            -- progress_status
            CASE
                WHEN COALESCE(completed_qty, 0) <= 0 THEN '未开工'
                WHEN completed_qty < plan_qty THEN '进行中'
                ELSE '已完工'
            END AS progress_status,
            production_back_workcenters,
            _ingested_at
        FROM raw.mes_select_production_back_params_by_time
    """)
    op.execute("""
        COMMENT ON VIEW serving.schedule_v1 IS
        '排产任务视图。来源: raw.mes_select_production_back_params_by_time。
         completion_rate: completed_qty / plan_qty。
         progress_status: 0→未开工, <plan→进行中, >=plan→已完工。'
    """)

    # 3.8 craft_hours_v1 — 工艺工时视图
    op.execute("""
        CREATE OR REPLACE VIEW serving.craft_hours_v1 AS
        SELECT
            mtid,
            material_no,
            material_desc,
            material_spec,
            unit,
            auxiliary_unit,
            conversion_coefficient,
            create_time,
            update_time,
            update_user_name,
            create_user_name,
            material_nature,
            confirm,
            material_ledger_desc,
            material_ledger_spec,
            update_qty,
            gantt_color,
            bind_sop,
            bind_first_inspect_scheme,
            bind_self_inspect_scheme,
            bind_final_inspect_scheme,
            bind_process_supervision_scheme,
            NULL::VARCHAR(128) AS workshop,  -- NULL placeholder: no workshop mapping
            procedure_names,
            procedure_name,
            _ingested_at
        FROM raw.mes_query_craft_hours
    """)
    op.execute("""
        COMMENT ON VIEW serving.craft_hours_v1 IS
        '工艺工时视图。来源: raw.mes_query_craft_hours。
         workshop: NULL 占位 (该接口无车间信息)。'
    """)


def downgrade() -> None:
    # Drop views
    op.execute("DROP VIEW IF EXISTS serving.craft_hours_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.schedule_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.workorder_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.reporting_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.oee_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.error_report_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.andon_v1 CASCADE")
    op.execute("DROP VIEW IF EXISTS serving.machine_dim_v1 CASCADE")

    # Drop UNIQUE constraint
    op.execute("ALTER TABLE semantic_properties DROP CONSTRAINT IF EXISTS uq_semantic_properties_object_code")

    # Drop serving schema
    op.execute("DROP SCHEMA IF EXISTS serving CASCADE")
