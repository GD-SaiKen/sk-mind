"""add MES raw tables — 25 tables, one per API endpoint (v2)

Revision ID: 006
Revises: 005
Create Date: 2026-07-21
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
    # ── Step 1: Drop old 16 tables (if they exist) ──
    old_tables = [
        "raw.mes_workorders",
        "raw.mes_procedure_reports",
        "raw.mes_production_schedules",
        "raw.mes_task_actions",
        "raw.mes_material_usages",
        "raw.mes_materials",
        "raw.mes_machines",
        "raw.mes_oee_reports",
        "raw.mes_andon_records",
        "raw.mes_error_reports",
        "raw.mes_trilight_statuses",
        "raw.mes_trilight_efficiencies",
        "raw.mes_trilight_color_changes",
        "raw.mes_trilight_counts",
        "raw.mes_completion_reports",
        "raw.mes_custom_field_defs",
    ]
    for tbl in old_tables:
        op.execute(f"DROP TABLE IF EXISTS {tbl} CASCADE")

    # ── Step 2: Create 25 new tables ──

    # 3.1 raw.mes_filter_workorder (interface #1)
    op.execute("""
    CREATE TABLE raw.mes_filter_workorder (
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
    op.execute("CREATE INDEX idx_mfwo_woid      ON raw.mes_filter_workorder (woid)")
    op.execute("CREATE INDEX idx_mfwo_no        ON raw.mes_filter_workorder (workorder_no)")
    op.execute("CREATE INDEX idx_mfwo_material  ON raw.mes_filter_workorder (material_no)")
    op.execute("CREATE INDEX idx_mfwo_customer  ON raw.mes_filter_workorder (customer_no)")
    op.execute("CREATE INDEX idx_mfwo_status    ON raw.mes_filter_workorder (status)")
    op.execute("CREATE INDEX idx_mfwo_ctime     ON raw.mes_filter_workorder (create_time)")
    op.execute("CREATE UNIQUE INDEX uq_mfwo_dedup ON raw.mes_filter_workorder (_batch_id, _row_hash)")

    # 3.2 raw.mes_select_complish_report (interface #2)
    op.execute("""
    CREATE TABLE raw.mes_select_complish_report (
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
    op.execute("CREATE INDEX idx_mscr_date ON raw.mes_select_complish_report (work_date)")
    op.execute("CREATE UNIQUE INDEX uq_mscr_dedup ON raw.mes_select_complish_report (_batch_id, _row_hash)")

    # 3.3 raw.mes_select_procedures_report_data_by_time (interface #3)
    op.execute("""
    CREATE TABLE raw.mes_select_procedures_report_data_by_time (
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
    op.execute("CREATE INDEX idx_msprd_woid     ON raw.mes_select_procedures_report_data_by_time (woid)")
    op.execute("CREATE INDEX idx_msprd_wno      ON raw.mes_select_procedures_report_data_by_time (workorder_no)")
    op.execute("CREATE INDEX idx_msprd_pno      ON raw.mes_select_procedures_report_data_by_time (procedure_no)")
    op.execute("CREATE UNIQUE INDEX uq_msprd_dedup ON raw.mes_select_procedures_report_data_by_time (_batch_id, _row_hash)")

    # 3.4 raw.mes_select_production_back_params_by_time (interface #4)
    op.execute("""
    CREATE TABLE raw.mes_select_production_back_params_by_time (
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
    op.execute("CREATE INDEX idx_mspbp_wopid    ON raw.mes_select_production_back_params_by_time (wopid)")
    op.execute("CREATE INDEX idx_mspbp_wno      ON raw.mes_select_production_back_params_by_time (workorder_no)")
    op.execute("CREATE UNIQUE INDEX uq_mspbp_dedup ON raw.mes_select_production_back_params_by_time (_batch_id, _row_hash)")

    # 3.5 raw.mes_select_task_use_material (interface #5)
    op.execute("""
    CREATE TABLE raw.mes_select_task_use_material (
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
    op.execute("CREATE INDEX idx_mstum_wno      ON raw.mes_select_task_use_material (workorder_no)")
    op.execute("CREATE INDEX idx_mstum_material ON raw.mes_select_task_use_material (use_material)")
    op.execute("CREATE UNIQUE INDEX uq_mstum_dedup ON raw.mes_select_task_use_material (_batch_id, _row_hash)")

    # 3.6 raw.mes_select_workorder_procedure (interface #6) — NEW
    op.execute("""
    CREATE TABLE raw.mes_select_workorder_procedure (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        wopid               BIGINT NOT NULL,
        workorder_no        VARCHAR(64),
        salesorder_no       VARCHAR(64),
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        plan_follow_word_no VARCHAR(64),
        procedure_no        VARCHAR(32),
        procedure_name      VARCHAR(128),
        plan_qty            NUMERIC,
        pending_qty         NUMERIC,
        arranged_qty        NUMERIC,
        completed_qty       NUMERIC
    )
    """)
    op.execute("CREATE INDEX idx_mswp_wopid ON raw.mes_select_workorder_procedure (wopid)")
    op.execute("CREATE INDEX idx_mswp_wno   ON raw.mes_select_workorder_procedure (workorder_no)")
    op.execute("CREATE UNIQUE INDEX uq_mswp_dedup ON raw.mes_select_workorder_procedure (_batch_id, _row_hash)")

    # 3.7 raw.mes_select_workorder_report_data_by_time (interface #7)
    op.execute("""
    CREATE TABLE raw.mes_select_workorder_report_data_by_time (
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
    op.execute("CREATE INDEX idx_mswrd_woid     ON raw.mes_select_workorder_report_data_by_time (woid)")
    op.execute("CREATE INDEX idx_mswrd_wno      ON raw.mes_select_workorder_report_data_by_time (workorder_no)")
    op.execute("CREATE INDEX idx_mswrd_pno      ON raw.mes_select_workorder_report_data_by_time (procedure_no)")
    op.execute("CREATE UNIQUE INDEX uq_mswrd_dedup ON raw.mes_select_workorder_report_data_by_time (_batch_id, _row_hash)")

    # 3.8 raw.mes_select_workorder_task_action_statistics (interface #8)
    op.execute("""
    CREATE TABLE raw.mes_select_workorder_task_action_statistics (
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
    op.execute("CREATE INDEX idx_mswtas_wtaid    ON raw.mes_select_workorder_task_action_statistics (wtaid)")
    op.execute("CREATE INDEX idx_mswtas_woid     ON raw.mes_select_workorder_task_action_statistics (woid)")
    op.execute("CREATE INDEX idx_mswtas_wno      ON raw.mes_select_workorder_task_action_statistics (workorder_no)")
    op.execute("CREATE UNIQUE INDEX uq_mswtas_dedup ON raw.mes_select_workorder_task_action_statistics (_batch_id, _row_hash)")

    # 3.9 raw.mes_andon_api_controller (interface #9)
    op.execute("""
    CREATE TABLE raw.mes_andon_api_controller (
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

        user_names           JSONB
    )
    """)
    op.execute("CREATE INDEX idx_maac_arid    ON raw.mes_andon_api_controller (ar_id)")
    op.execute("CREATE INDEX idx_maac_machine ON raw.mes_andon_api_controller (machine_no)")
    op.execute("CREATE UNIQUE INDEX uq_maac_dedup ON raw.mes_andon_api_controller (_batch_id, _row_hash)")

    # 3.10 raw.mes_get_timecount_messages_by_time_sim (interface #10)
    op.execute("""
    CREATE TABLE raw.mes_get_timecount_messages_by_time_sim (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        count_messages      JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mgtm_sim ON raw.mes_get_timecount_messages_by_time_sim (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgtm_dedup ON raw.mes_get_timecount_messages_by_time_sim (_batch_id, _row_hash)")

    # 3.11 raw.mes_get_trilight_count_by_time_sim (interface #11) — NEW
    op.execute("""
    CREATE TABLE raw.mes_get_trilight_count_by_time_sim (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        count_size          BIGINT
    )
    """)
    op.execute("CREATE INDEX idx_mgtc_sim ON raw.mes_get_trilight_count_by_time_sim (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgtc_dedup ON raw.mes_get_trilight_count_by_time_sim (_batch_id, _row_hash)")

    # 3.12 raw.mes_get_trilight_current_color (interface #12)
    op.execute("""
    CREATE TABLE raw.mes_get_trilight_current_color (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        current_state       VARCHAR(8),
        update_date         TIMESTAMPTZ,
        on_line_status      BOOLEAN
    )
    """)
    op.execute("CREATE INDEX idx_mgtcc_sim ON raw.mes_get_trilight_current_color (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgtcc_dedup ON raw.mes_get_trilight_current_color (_batch_id, _row_hash)")

    # 3.13 raw.mes_get_trilight_current_color_list (interface #13)
    op.execute("""
    CREATE TABLE raw.mes_get_trilight_current_color_list (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        current_state       VARCHAR(8),
        update_date         TIMESTAMPTZ,
        on_line_status      BOOLEAN
    )
    """)
    op.execute("CREATE INDEX idx_mgtccl_sim ON raw.mes_get_trilight_current_color_list (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgtccl_dedup ON raw.mes_get_trilight_current_color_list (_batch_id, _row_hash)")

    # 3.14 raw.mes_get_trilight_efficiency_duration_time (interface #14)
    op.execute("""
    CREATE TABLE raw.mes_get_trilight_efficiency_duration_time (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        red_time            BIGINT,
        green_time          BIGINT,
        yellow_time         BIGINT,
        close_time          BIGINT
    )
    """)
    op.execute("CREATE INDEX idx_mgtedt_sim ON raw.mes_get_trilight_efficiency_duration_time (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgtedt_dedup ON raw.mes_get_trilight_efficiency_duration_time (_batch_id, _row_hash)")

    # 3.15 raw.mes_get_trilight_efficiency_one_day (interface #15)
    op.execute("""
    CREATE TABLE raw.mes_get_trilight_efficiency_one_day (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        red_time            BIGINT,
        green_time          BIGINT,
        yellow_time         BIGINT,
        close_time          BIGINT
    )
    """)
    op.execute("CREATE INDEX idx_mgteod_sim ON raw.mes_get_trilight_efficiency_one_day (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgteod_dedup ON raw.mes_get_trilight_efficiency_one_day (_batch_id, _row_hash)")

    # 3.16 raw.mes_get_trilight_summary_duration_time (interface #16)
    op.execute("""
    CREATE TABLE raw.mes_get_trilight_summary_duration_time (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        sim                 VARCHAR(64) NOT NULL,
        start_time          TIMESTAMPTZ,
        end_time            TIMESTAMPTZ,
        color               VARCHAR(8)
    )
    """)
    op.execute("CREATE INDEX idx_mgtsdt_sim ON raw.mes_get_trilight_summary_duration_time (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgtsdt_dedup ON raw.mes_get_trilight_summary_duration_time (_batch_id, _row_hash)")

    # 3.17 raw.mes_select_oee_report (interface #17)
    op.execute("""
    CREATE TABLE raw.mes_select_oee_report (
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
    op.execute("CREATE INDEX idx_msoer_mid    ON raw.mes_select_oee_report (mid)")
    op.execute("CREATE INDEX idx_msoer_date   ON raw.mes_select_oee_report (sim_date)")
    op.execute("CREATE UNIQUE INDEX uq_msoer_dedup ON raw.mes_select_oee_report (_batch_id, _row_hash)")

    # 3.18 raw.mes_get_machine_count (interface #18) — NEW
    op.execute("""
    CREATE TABLE raw.mes_get_machine_count (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        data                INTEGER
    )
    """)

    # 3.19 raw.mes_get_machine_detail_by_id (interface #19)
    op.execute("""
    CREATE TABLE raw.mes_get_machine_detail_by_id (
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
    op.execute("CREATE INDEX idx_mgmdbi_mid     ON raw.mes_get_machine_detail_by_id (mid)")
    op.execute("CREATE INDEX idx_mgmdbi_no      ON raw.mes_get_machine_detail_by_id (machine_no)")
    op.execute("CREATE INDEX idx_mgmdbi_sim     ON raw.mes_get_machine_detail_by_id (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgmdbi_dedup ON raw.mes_get_machine_detail_by_id (_batch_id, _row_hash)")

    # 3.20 raw.mes_get_machine_list (interface #20)
    op.execute("""
    CREATE TABLE raw.mes_get_machine_list (
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
        department_name     VARCHAR(128)
    )
    """)
    op.execute("CREATE INDEX idx_mgml_mid     ON raw.mes_get_machine_list (mid)")
    op.execute("CREATE INDEX idx_mgml_no      ON raw.mes_get_machine_list (machine_no)")
    op.execute("CREATE INDEX idx_mgml_sim     ON raw.mes_get_machine_list (sim)")
    op.execute("CREATE UNIQUE INDEX uq_mgml_dedup ON raw.mes_get_machine_list (_batch_id, _row_hash)")

    # 3.21 raw.mes_list_defs (interface #21)
    op.execute("""
    CREATE TABLE raw.mes_list_defs (
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
    op.execute("CREATE INDEX idx_mld_entity ON raw.mes_list_defs (entity_type)")
    op.execute("CREATE UNIQUE INDEX uq_mld_dedup ON raw.mes_list_defs (_batch_id, _row_hash)")

    # 3.22 raw.mes_list_optional_custom_field_codes (interface #22) — NEW
    op.execute("""
    CREATE TABLE raw.mes_list_optional_custom_field_codes (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        field_code          VARCHAR(64),
        field_label         VARCHAR(128)
    )
    """)
    op.execute("CREATE UNIQUE INDEX uq_mlocfc_dedup ON raw.mes_list_optional_custom_field_codes (_batch_id, _row_hash)")

    # 3.23 raw.mes_query_craft_hours (interface #23)
    op.execute("""
    CREATE TABLE raw.mes_query_craft_hours (
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
    op.execute("CREATE INDEX idx_mqch_mtid    ON raw.mes_query_craft_hours (mtid)")
    op.execute("CREATE INDEX idx_mqch_no      ON raw.mes_query_craft_hours (material_no)")
    op.execute("CREATE UNIQUE INDEX uq_mqch_dedup ON raw.mes_query_craft_hours (_batch_id, _row_hash)")

    # 3.24 raw.mes_query_craft_hours_details (interface #24) — NEW
    op.execute("""
    CREATE TABLE raw.mes_query_craft_hours_details (
        _raw_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        _source_id          UUID NOT NULL,
        _batch_id           UUID NOT NULL,
        _pulled_at          TIMESTAMP NOT NULL,
        _source_signature   TEXT,
        _row_hash           TEXT,
        _quality_flags      JSONB DEFAULT '[]',
        _ingested_at        TIMESTAMP DEFAULT now(),

        rid                 BIGINT NOT NULL,
        material_no         VARCHAR(64),
        material_desc       VARCHAR(256),
        material_spec       VARCHAR(256),
        unit                VARCHAR(16),
        material_ledger_desc VARCHAR(256),
        material_ledger_spec VARCHAR(256),
        material_ledger_brand VARCHAR(128),
        remark              TEXT,
        conversion_coefficient NUMERIC,
        auxiliary_unit      VARCHAR(16),
        material_weight     NUMERIC,
        material_price      NUMERIC,
        routings_name       VARCHAR(128),
        customization_no    VARCHAR(64),
        customization_name  VARCHAR(128),
        customer_requirement TEXT,
        completion_stage    INTEGER,
        file_url            TEXT,
        gantt_color         VARCHAR(32),
        utilization_rate    NUMERIC,
        customer_material_no VARCHAR(64),
        material_nature     INTEGER,
        psf_id              BIGINT,
        series_name         VARCHAR(128),
        series_code         VARCHAR(64),

        sop_path_list               JSONB,
        routings_procedure_msg_list JSONB
    )
    """)
    op.execute("CREATE INDEX idx_mqchd_rid    ON raw.mes_query_craft_hours_details (rid)")
    op.execute("CREATE INDEX idx_mqchd_no     ON raw.mes_query_craft_hours_details (material_no)")
    op.execute("CREATE UNIQUE INDEX uq_mqchd_dedup ON raw.mes_query_craft_hours_details (_batch_id, _row_hash)")

    # 3.25 raw.mes_select_error_report (interface #25)
    op.execute("""
    CREATE TABLE raw.mes_select_error_report (
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
    op.execute("CREATE INDEX idx_mser_mid     ON raw.mes_select_error_report (mid)")
    op.execute("CREATE INDEX idx_mser_machine ON raw.mes_select_error_report (machine_no)")
    op.execute("CREATE UNIQUE INDEX uq_mser_dedup ON raw.mes_select_error_report (_batch_id, _row_hash)")


def downgrade() -> None:
    # Drop all 25 tables in reverse order
    tables = [
        "raw.mes_select_error_report",
        "raw.mes_query_craft_hours_details",
        "raw.mes_query_craft_hours",
        "raw.mes_list_optional_custom_field_codes",
        "raw.mes_list_defs",
        "raw.mes_get_machine_list",
        "raw.mes_get_machine_detail_by_id",
        "raw.mes_get_machine_count",
        "raw.mes_select_oee_report",
        "raw.mes_get_trilight_summary_duration_time",
        "raw.mes_get_trilight_efficiency_one_day",
        "raw.mes_get_trilight_efficiency_duration_time",
        "raw.mes_get_trilight_current_color_list",
        "raw.mes_get_trilight_current_color",
        "raw.mes_get_trilight_count_by_time_sim",
        "raw.mes_get_timecount_messages_by_time_sim",
        "raw.mes_andon_api_controller",
        "raw.mes_select_workorder_task_action_statistics",
        "raw.mes_select_workorder_report_data_by_time",
        "raw.mes_select_workorder_procedure",
        "raw.mes_select_task_use_material",
        "raw.mes_select_production_back_params_by_time",
        "raw.mes_select_procedures_report_data_by_time",
        "raw.mes_select_complish_report",
        "raw.mes_filter_workorder",
    ]
    for tbl in tables:
        op.execute(f"DROP TABLE IF EXISTS {tbl} CASCADE")
