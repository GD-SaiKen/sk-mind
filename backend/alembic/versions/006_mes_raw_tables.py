"""add MES raw tables (16 tables)

Revision ID: 006
Revises: 005
Create Date: 2026-07-20
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = '006'
down_revision: Union[str, None] = '005'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 3.1 raw.mes_workorders — 工单
    op.execute("""
    CREATE TABLE raw.mes_workorders (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        woid                BIGINT NOT NULL,
        workorder_no        VARCHAR(64),
        workorder_type      VARCHAR(32),
        urgent_level        INTEGER,
        mtid                BIGINT,
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        unit                VARCHAR(16),
        rid                 BIGINT,
        plan_qty            NUMERIC,
        completed_qty       NUMERIC,
        surplus_qty         NUMERIC,
        order_qty           NUMERIC,
        portion_qty         NUMERIC,
        arranged_qty        NUMERIC,
        progress            VARCHAR(32),
        complete_progress   NUMERIC,
        create_time         TIMESTAMPTZ,
        start_time          TIMESTAMPTZ,
        end_time            TIMESTAMPTZ,
        require_end_time    TIMESTAMPTZ,
        estimated_start_time TIMESTAMPTZ,
        estimated_end_time  TIMESTAMPTZ,
        actual_complete_time TIMESTAMPTZ,
        close_time          TIMESTAMPTZ,
        customer_no         VARCHAR(32),
        customization_no    VARCHAR(64),
        customer_requirement TEXT,
        customer_material_code VARCHAR(64),
        customer_material_name VARCHAR(128),
        sales               VARCHAR(64),
        salesorder_no       VARCHAR(64),
        plan_follow_word_no VARCHAR(64),
        order_master        VARCHAR(64),
        project_number      VARCHAR(64),
        order_number        VARCHAR(64),
        current_procedure   VARCHAR(128),
        next_procedure      VARCHAR(128),
        all_procedure       TEXT,
        routings_material_no VARCHAR(64),
        status              INTEGER,
        material_status     INTEGER,
        create_tuid         BIGINT,
        create_user_name    VARCHAR(64),
        close_uid           BIGINT,
        close_user_name     VARCHAR(64),
        material_price      NUMERIC,
        material_total_price NUMERIC,
        standard_work_hours NUMERIC,
        error_info          TEXT,
        notes               TEXT,
        remark              TEXT,
        close_remark        TEXT,
        overdue_count       BIGINT,
        print_number        INTEGER,
        material_ledger_desc VARCHAR(256),
        material_ledger_spec VARCHAR(256),
        supplier            VARCHAR(128),

        simple_procedures   JSONB,
        custom_fields       JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mwo_woid      ON raw.mes_workorders (woid)")
    op.execute("CREATE INDEX idx_mwo_no        ON raw.mes_workorders (workorder_no)")
    op.execute("CREATE INDEX idx_mwo_material  ON raw.mes_workorders (material_no)")
    op.execute("CREATE INDEX idx_mwo_customer  ON raw.mes_workorders (customer_no)")
    op.execute("CREATE INDEX idx_mwo_status    ON raw.mes_workorders (status)")
    op.execute("CREATE INDEX idx_mwo_ctime     ON raw.mes_workorders (create_time)")
    op.execute("CREATE UNIQUE INDEX uq_mwo_dedup ON raw.mes_workorders (_batch_id, _row_hash)")

    # 3.2 raw.mes_procedure_reports — 工序报工
    op.execute("""
    CREATE TABLE raw.mes_procedure_reports (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        woid                BIGINT,
        workorder_no        VARCHAR(64),
        workorder_type      VARCHAR(32),
        salesorder_no       VARCHAR(64),
        plan_follow_word_no VARCHAR(64),
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        material_code       VARCHAR(64),
        unit                VARCHAR(16),
        wtaid               BIGINT,
        tid                 BIGINT,
        procedure_no        VARCHAR(32),
        procedure_order     INTEGER,
        procedure_name      VARCHAR(128),
        procedure_remark    TEXT,
        good_qty            NUMERIC,
        bad_qty             NUMERIC,
        bad_qty_manufacturing NUMERIC,
        bad_qty_incoming    NUMERIC,
        in_stock_qty        NUMERIC,
        workorder_plan_qty  NUMERIC,
        plan_qty            NUMERIC,
        single_trip_qty     NUMERIC,
        actual_time         NUMERIC,
        earned_hours        NUMERIC,
        single_trip_time    NUMERIC,
        frequency_size      INTEGER,
        machine_no          VARCHAR(64),
        machine_name        VARCHAR(128),
        workcenter_no       VARCHAR(64),
        workcenter_name     VARCHAR(128),
        workshop_name       VARCHAR(128),
        product_line        VARCHAR(128),
        mould_no            VARCHAR(64),
        mould_name          VARCHAR(128),
        user_names          VARCHAR(512),
        employee_nos        VARCHAR(256),
        approver_name       VARCHAR(64),
        one_level_reason    VARCHAR(256),
        two_level_reason    VARCHAR(256),
        three_level_reason  VARCHAR(256),
        approver_time       TIMESTAMPTZ,
        task_start_time     TIMESTAMPTZ,
        task_end_time       TIMESTAMPTZ,
        work_date           DATE,
        create_time         TIMESTAMPTZ,
        warehouse           VARCHAR(128),
        production_batch_no VARCHAR(64),
        material_batch_no   VARCHAR(64),
        material_qty        NUMERIC,
        weight              NUMERIC,
        material_unit       VARCHAR(16),
        knife_weight        NUMERIC,
        material_weight     NUMERIC,
        piece_weight        NUMERIC,
        scrap_weight        NUMERIC,
        task_action_remark  TEXT,
        transfer_card_no    VARCHAR(64),
        component           VARCHAR(128),
        shift_name          VARCHAR(64),
        note                TEXT,
        completion_stage    INTEGER,
        chassis_no          VARCHAR(64),
        rear_outrigger_code VARCHAR(64)
    )
    """)
    op.execute("CREATE INDEX idx_mpr_woid     ON raw.mes_procedure_reports (woid)")
    op.execute("CREATE INDEX idx_mpr_wno      ON raw.mes_procedure_reports (workorder_no)")
    op.execute("CREATE INDEX idx_mpr_pno      ON raw.mes_procedure_reports (procedure_no)")
    op.execute("CREATE UNIQUE INDEX uq_mpr_dedup ON raw.mes_procedure_reports (_batch_id, _row_hash)")

    # 3.3 raw.mes_production_schedules — 工序排产
    op.execute("""
    CREATE TABLE raw.mes_production_schedules (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        wopid               VARCHAR(64) NOT NULL,
        workorder_no        VARCHAR(64),
        salesorder_no       VARCHAR(64),
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        procedure_no        VARCHAR(32),
        procedure_name      VARCHAR(128),
        plan_follow_word_no VARCHAR(64),
        plan_qty            NUMERIC,
        pending_qty         NUMERIC,
        arranged_qty        NUMERIC,
        completed_qty       NUMERIC,
        procedure_order     INTEGER,
        completion_stage    INTEGER,

        production_back_workcenters JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mps_wopid    ON raw.mes_production_schedules (wopid)")
    op.execute("CREATE INDEX idx_mps_wno      ON raw.mes_production_schedules (workorder_no)")
    op.execute("CREATE UNIQUE INDEX uq_mps_dedup ON raw.mes_production_schedules (_batch_id, _row_hash)")

    # 3.4 raw.mes_task_actions — 报工明细
    op.execute("""
    CREATE TABLE raw.mes_task_actions (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        wtaid               BIGINT NOT NULL,
        wtid                BIGINT,
        woid                BIGINT,
        sid                 BIGINT,
        workorder_no        VARCHAR(64),
        workorder_type      VARCHAR(32),
        task_no             VARCHAR(64),
        rpid                BIGINT,
        procedure_no        VARCHAR(32),
        procedure_name      VARCHAR(128),
        procedure_remark    TEXT,
        mtid                BIGINT,
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        unit                VARCHAR(16),
        routings_material_no VARCHAR(64),
        mid                 BIGINT,
        machine_no          VARCHAR(64),
        machine_name        VARCHAR(128),
        pulse               INTEGER,
        workcenter_no       VARCHAR(64),
        workcenter_name     VARCHAR(128),
        department_name     VARCHAR(128),
        plan_qty            NUMERIC,
        workorder_plan_qty  NUMERIC,
        production_qty      NUMERIC,
        good_qty            NUMERIC,
        theoretical_qty     NUMERIC,
        per_hour_output     NUMERIC,
        bad_qty_manufacturing NUMERIC,
        bad_qty_incoming    NUMERIC,
        isolation_bad_qty   NUMERIC,
        in_stock_qty        NUMERIC,
        in_stock_rate       NUMERIC,
        total_complete_qty  NUMERIC,
        check_qty           NUMERIC,
        produce_hours       NUMERIC,
        machine_hours       NUMERIC,
        people_hours        NUMERIC,
        earned_hours        NUMERIC,
        compensate_hours    NUMERIC,
        actual_people_hours NUMERIC,
        compensate_work_hours NUMERIC,
        plan_work_time      NUMERIC,
        start_time          TIMESTAMPTZ,
        end_time            TIMESTAMPTZ,
        mould_start_time    TIMESTAMPTZ,
        mould_end_time      TIMESTAMPTZ,
        start_mould_time    TIMESTAMPTZ,
        end_mould_time      TIMESTAMPTZ,
        green_duration      NUMERIC,
        yellow_duration     NUMERIC,
        red_duration        NUMERIC,
        close_duration      NUMERIC,
        andon_duration      NUMERIC,
        effective_duration  NUMERIC,
        free_time           NUMERIC,
        theoretical_duration NUMERIC,
        plan_complete_rate  NUMERIC,
        standard_complete_rate NUMERIC,
        production_rate     NUMERIC,
        green_rate          NUMERIC,
        good_rate           NUMERIC,
        oee_rate            NUMERIC,
        man_output_rate     NUMERIC,
        utilization_rate    NUMERIC,
        mould_list          VARCHAR(512),
        time_mould_change   NUMERIC,
        actual_time_mould_change NUMERIC,
        actual_mold_cavity  NUMERIC,
        single_trip_qty     NUMERIC,
        actual_single_trip_qty NUMERIC,
        single_trip_qty_rate NUMERIC,
        mold_cavity_rate    NUMERIC,
        single_trip_time    NUMERIC,
        actual_single_trip_time NUMERIC,
        unit_price          NUMERIC,
        amount              NUMERIC,
        operator_list       VARCHAR(512),
        operation_count     INTEGER,
        user_name           VARCHAR(64),
        conversion_coefficient NUMERIC,
        coefficient         VARCHAR(32),
        second_coefficient  NUMERIC,
        main_coefficient    NUMERIC,
        material_batch_no   VARCHAR(64),
        production_batch_no VARCHAR(64),
        shift_time_name     VARCHAR(128),
        shift_capacity      NUMERIC,
        task_count          BIGINT,
        task_action_remark  TEXT,
        workorder_remark    TEXT,
        plan_follow_word_no VARCHAR(64),
        salesorder_no       VARCHAR(64),
        customization_no    VARCHAR(64),
        customer_requirement TEXT,
        transfer_card_no    VARCHAR(64),
        auxiliary_unit      VARCHAR(16),
        auxiliary_qty       NUMERIC,
        auxiliary_report    INTEGER,
        material_ledger_desc VARCHAR(256),
        material_ledger_spec VARCHAR(256),
        material_ledger_weight NUMERIC,
        supplier            VARCHAR(128),
        order_qty           NUMERIC,
        approve_status      VARCHAR(32),
        compensate_notes    TEXT,
        actual_single_output_time NUMERIC,
        theoretical_scrap_weight NUMERIC,
        material_qty        NUMERIC,
        weight              NUMERIC,
        material_unit       VARCHAR(16),
        knife_weight        NUMERIC,
        material_weight     NUMERIC,
        piece_weight        NUMERIC,
        scrap_weight        NUMERIC,
        chassis_no          VARCHAR(64),
        rear_outrigger_code VARCHAR(64),
        box_qty             NUMERIC,
        error_remark        TEXT,
        main_bad_qty        NUMERIC,
        second_bad_qty      NUMERIC,
        has_media           VARCHAR(32),
        output_rate         NUMERIC,
        auxiliary_metering  NUMERIC,
        pic_url             TEXT,
        pic_type            INTEGER,

        product_specifications JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mta_wtaid    ON raw.mes_task_actions (wtaid)")
    op.execute("CREATE INDEX idx_mta_woid     ON raw.mes_task_actions (woid)")
    op.execute("CREATE INDEX idx_mta_wno      ON raw.mes_task_actions (workorder_no)")
    op.execute("CREATE UNIQUE INDEX uq_mta_dedup ON raw.mes_task_actions (_batch_id, _row_hash)")

    # 3.5 raw.mes_material_usages — 投料明细
    op.execute("""
    CREATE TABLE raw.mes_material_usages (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        workorder_no        VARCHAR(64),
        task_no             VARCHAR(64),
        did                 BIGINT,
        work_shop           VARCHAR(128),
        product_line        VARCHAR(128),
        wcid                BIGINT,
        workcenter_no       VARCHAR(64),
        workcenter_name     VARCHAR(128),
        procedure_no        VARCHAR(32),
        procedure_name      VARCHAR(128),
        use_material        VARCHAR(64),
        use_material_desc   VARCHAR(256),
        material_batch_no   VARCHAR(64),
        use_qty             NUMERIC,
        use_unit            VARCHAR(16),
        quantity            NUMERIC,
        use_time            TIMESTAMPTZ,
        uid                 BIGINT,
        user_name           VARCHAR(64),
        url_str             TEXT,

        urls                JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mmu_wno      ON raw.mes_material_usages (workorder_no)")
    op.execute("CREATE INDEX idx_mmu_material ON raw.mes_material_usages (use_material)")

    # 3.6 raw.mes_materials — 物料主数据
    op.execute("""
    CREATE TABLE raw.mes_materials (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        mtid                BIGINT NOT NULL,
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        unit                VARCHAR(16),
        auxiliary_unit      VARCHAR(16),
        conversion_coefficient NUMERIC,
        create_time         TIMESTAMPTZ,
        update_time         TIMESTAMPTZ,
        update_user_name    VARCHAR(64),
        create_user_name    VARCHAR(64),
        material_nature     INTEGER,
        confirm             INTEGER,
        material_ledger_desc VARCHAR(256),
        material_ledger_spec VARCHAR(256),
        update_qty          INTEGER,
        gantt_color         VARCHAR(32),
        bind_sop            INTEGER,
        bind_first_inspect_scheme  INTEGER,
        bind_self_inspect_scheme   INTEGER,
        bind_final_inspect_scheme  INTEGER,
        bind_process_supervision_scheme INTEGER,

        procedure_names     JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mmat_mtid    ON raw.mes_materials (mtid)")
    op.execute("CREATE INDEX idx_mmat_no      ON raw.mes_materials (material_no)")

    # 3.7 raw.mes_machines — 设备主数据
    op.execute("""
    CREATE TABLE raw.mes_machines (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        mid                 BIGINT NOT NULL,
        machine_no          VARCHAR(64),
        machine_name        VARCHAR(128),
        sim                 VARCHAR(64),
        status              INTEGER,
        machine_brand       VARCHAR(128),
        machine_model       VARCHAR(128),
        machine_function    TEXT,
        machine_image       TEXT,
        serial_number       VARCHAR(128),
        fixed_assets_code   VARCHAR(128),
        supplier            VARCHAR(128),
        manufacturer        VARCHAR(128),
        production_date     DATE,
        receive_date        DATE,
        first_date          DATE,
        documents           TEXT,
        use_time            VARCHAR(64),
        department_name     VARCHAR(128)
    )
    """)
    op.execute("CREATE INDEX idx_mmc_mid     ON raw.mes_machines (mid)")
    op.execute("CREATE INDEX idx_mmc_no      ON raw.mes_machines (machine_no)")
    op.execute("CREATE INDEX idx_mmc_sim     ON raw.mes_machines (sim)")

    # 3.8 raw.mes_oee_reports — 设备 OEE
    op.execute("""
    CREATE TABLE raw.mes_oee_reports (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        mid                 BIGINT NOT NULL,
        department_name     VARCHAR(128),
        machine_no          VARCHAR(64),
        machine_name        VARCHAR(128),
        sim_date            DATE,
        shift_name          VARCHAR(64),
        start_time          TIMESTAMPTZ,
        end_time            TIMESTAMPTZ,
        red_time            NUMERIC,
        green_time          NUMERIC,
        yellow_time         NUMERIC,
        close_time          NUMERIC,
        green_total_time    NUMERIC,
        red_rate            NUMERIC,
        green_rate          NUMERIC,
        yellow_rate         NUMERIC,
        close_rate          NUMERIC,
        actual_rate         NUMERIC,
        effective_yellow_time NUMERIC,
        effective_green_rate NUMERIC,
        actual_yellow_rate  NUMERIC,
        performance_rate    NUMERIC,
        oee_rate            NUMERIC,
        run_oee_rate        NUMERIC,
        standard_rate       NUMERIC,
        user_name           VARCHAR(64),
        green_compensation  NUMERIC,
        wait_count          BIGINT,
        fault_count         BIGINT,
        good_qty            NUMERIC,
        stop_time           NUMERIC,
        stop_green          NUMERIC,
        stop_free           NUMERIC,
        andon_time          NUMERIC,
        andon_rate          NUMERIC,
        red_hour            NUMERIC,
        green_hour          NUMERIC,
        yellow_hour         NUMERIC,
        close_hour          NUMERIC,
        green_total_hour    NUMERIC,
        green_compensation_hour NUMERIC,
        effective_yellow_hour NUMERIC,
        stop_hour           NUMERIC,
        andon_hour          NUMERIC,
        online_time         NUMERIC,
        shift_green_rate    NUMERIC,
        shift_green_time    NUMERIC
    )
    """)
    op.execute("CREATE INDEX idx_moee_mid    ON raw.mes_oee_reports (mid)")
    op.execute("CREATE INDEX idx_moee_date   ON raw.mes_oee_reports (sim_date)")

    # 3.9 raw.mes_andon_records — 安灯记录
    op.execute("""
    CREATE TABLE raw.mes_andon_records (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        ar_id               BIGINT NOT NULL,
        machine_no          VARCHAR(64),
        create_date         TIMESTAMPTZ,
        andon_title         VARCHAR(128),
        receive_date        TIMESTAMPTZ,
        receive_time        NUMERIC,
        finish_date         TIMESTAMPTZ,
        finish_time         NUMERIC,
        all_time            NUMERIC,
        submit_name         VARCHAR(64),
        finish_name         VARCHAR(64),
        mes_explain         TEXT,
        remark              TEXT,
        mes_url             TEXT,
        url_type            INTEGER,
        note                TEXT,
        note_url            TEXT,
        note_type           INTEGER,
        task_remark         TEXT,
        andon_status        INTEGER,
        standard_duration   NUMERIC,
        standard_response_time NUMERIC,
        standard_processing_time NUMERIC,
        response_timeout    NUMERIC,
        processing_timeout  NUMERIC,
        can_print_oa        INTEGER,

        user_names           JSONB,
        finish_url_list      JSONB,
        supplement_url_list  JSONB,
        andon_record_log_list JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mar_arid    ON raw.mes_andon_records (ar_id)")
    op.execute("CREATE INDEX idx_mar_machine ON raw.mes_andon_records (machine_no)")

    # 3.10 raw.mes_error_reports — 异常上报
    op.execute("""
    CREATE TABLE raw.mes_error_reports (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        lwl_id              BIGINT NOT NULL,
        mid                 BIGINT,
        machine_no          VARCHAR(64),
        machine_name        VARCHAR(128),
        machine_status_name VARCHAR(128),
        work_date           DATE,
        shift_name          VARCHAR(64),
        shift_start_date    TIMESTAMPTZ,
        shift_end_date      TIMESTAMPTZ,
        color               VARCHAR(16),
        reason_code         VARCHAR(64),
        wait_reason         VARCHAR(256),
        reason_classification VARCHAR(128),
        wait_start_time     TIMESTAMPTZ,
        wait_end_time       TIMESTAMPTZ,
        duration            NUMERIC,
        workorder_no        VARCHAR(64),
        material_no         VARCHAR(64),
        user_name           VARCHAR(64),
        description         TEXT,
        open_user_name      VARCHAR(64),
        update_time         TIMESTAMPTZ,

        pic_urls            JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mer_mid     ON raw.mes_error_reports (mid)")
    op.execute("CREATE INDEX idx_mer_machine ON raw.mes_error_reports (machine_no)")

    # 3.11a raw.mes_trilight_statuses — 三色灯实时状态
    op.execute("""
    CREATE TABLE raw.mes_trilight_statuses (
        _raw_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _batch_id    UUID NOT NULL,
        _pulled_at   TIMESTAMP NOT NULL,
        _row_hash    TEXT,
        _ingested_at TIMESTAMP DEFAULT now(),

        sim          VARCHAR(64) NOT NULL,
        current_state VARCHAR(8),
        update_date  TIMESTAMPTZ,
        on_line_status BOOLEAN
    )
    """)
    op.execute("CREATE INDEX idx_mts_sim ON raw.mes_trilight_statuses (sim)")

    # 3.11b raw.mes_trilight_efficiencies — 三色灯效率汇总
    op.execute("""
    CREATE TABLE raw.mes_trilight_efficiencies (
        _raw_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _batch_id    UUID NOT NULL,
        _pulled_at   TIMESTAMP NOT NULL,
        _row_hash    TEXT,
        _ingested_at TIMESTAMP DEFAULT now(),

        sim          VARCHAR(64) NOT NULL,
        red_time     BIGINT,
        green_time   BIGINT,
        yellow_time  BIGINT,
        close_time   BIGINT,
        query_date   DATE
    )
    """)
    op.execute("CREATE INDEX idx_mte_sim ON raw.mes_trilight_efficiencies (sim)")

    # 3.11c raw.mes_trilight_color_changes — 三色灯颜色变化明细
    op.execute("""
    CREATE TABLE raw.mes_trilight_color_changes (
        _raw_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _batch_id    UUID NOT NULL,
        _pulled_at   TIMESTAMP NOT NULL,
        _row_hash    TEXT,
        _ingested_at TIMESTAMP DEFAULT now(),

        sim          VARCHAR(64) NOT NULL,
        start_time   TIMESTAMPTZ,
        end_time     TIMESTAMPTZ,
        color        VARCHAR(8)
    )
    """)
    op.execute("CREATE INDEX idx_mtcc_sim ON raw.mes_trilight_color_changes (sim)")

    # 3.11d raw.mes_trilight_counts — 三色灯脉冲计数
    op.execute("""
    CREATE TABLE raw.mes_trilight_counts (
        _raw_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _batch_id    UUID NOT NULL,
        _pulled_at   TIMESTAMP NOT NULL,
        _row_hash    TEXT,
        _ingested_at TIMESTAMP DEFAULT now(),

        sim          VARCHAR(64) NOT NULL,
        count_size   BIGINT,
        count_messages JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mtcnt_sim ON raw.mes_trilight_counts (sim)")

    # 3.12 raw.mes_completion_reports — 达成率报表
    op.execute("""
    CREATE TABLE raw.mes_completion_reports (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sid                 BIGINT,
        shift_name          VARCHAR(64),
        work_date           DATE,
        department_name     VARCHAR(128),
        task_count          INTEGER,
        completed_task_count INTEGER,
        un_completed_task_count INTEGER,
        task_qty            NUMERIC,
        completed_task_qty  NUMERIC,
        un_completed_task_qty NUMERIC,
        complete_rate       NUMERIC,
        qty_complete_rate   NUMERIC
    )
    """)
    op.execute("CREATE INDEX idx_mcr_date ON raw.mes_completion_reports (work_date)")

    # 3.13 raw.mes_custom_field_defs — 自定义字段定义
    op.execute("""
    CREATE TABLE raw.mes_custom_field_defs (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        ecfd_id             BIGINT NOT NULL,
        entity_type         VARCHAR(64),
        web_id              BIGINT,
        field_code          VARCHAR(64),
        field_label         VARCHAR(128),
        field_type          VARCHAR(32),
        required            INTEGER,
        sort_no             INTEGER,
        max_length          INTEGER,
        options_json        TEXT,
        enabled             INTEGER
    )
    """)
    op.execute("CREATE INDEX idx_mcfd_entity ON raw.mes_custom_field_defs (entity_type)")


def downgrade() -> None:
    # Drop in reverse order of creation
    op.execute("DROP TABLE IF EXISTS raw.mes_custom_field_defs CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_completion_reports CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_trilight_counts CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_trilight_color_changes CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_trilight_efficiencies CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_trilight_statuses CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_error_reports CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_andon_records CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_oee_reports CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_machines CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_materials CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_material_usages CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_task_actions CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_production_schedules CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_procedure_reports CASCADE")
    op.execute("DROP TABLE IF EXISTS raw.mes_workorders CASCADE")
