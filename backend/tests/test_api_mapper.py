import pytest
from app.modules.ingestion.connectors.api_mapper import ColumnMapper


class TestColumnMapper:
    def test_maps_scalar_to_column(self):
        mapper = ColumnMapper({"workorder_no", "plan_qty", "woid"})
        row = {"woid": 12345, "workorderNo": "WO-001", "planQty": 500}
        result = mapper.map_row(row)
        assert result["columns"] == {"woid": 12345, "workorder_no": "WO-001", "plan_qty": 500}
        assert result["jsonb_cols"] == {}

    def test_maps_nested_to_jsonb(self):
        mapper = ColumnMapper({"workorder_no"})
        row = {
            "workorderNo": "WO-001",
            "simpleProcedureVOS": [{"procedureNo": "01", "procedureName": "裁切"}],
            "customFields": [{"fieldCode": "cf1", "fieldValue": "急单"}],
        }
        result = mapper.map_row(row)
        assert result["columns"] == {"workorder_no": "WO-001"}
        assert len(result["jsonb_cols"]) == 2
        assert "simple_procedures" in result["jsonb_cols"]
        assert "custom_fields" in result["jsonb_cols"]

    def test_ignores_unknown_scalar(self):
        mapper = ColumnMapper({"workorder_no"})
        row = {"workorderNo": "WO-001", "unknownField": "should-be-ignored"}
        result = mapper.map_row(row)
        assert result["columns"] == {"workorder_no": "WO-001"}
        assert "unknown_field" not in result["columns"]
        assert "unknown_field" not in result["jsonb_cols"]

    def test_camel_to_snake(self):
        assert ColumnMapper._to_snake("workorderNo") == "workorder_no"
        assert ColumnMapper._to_snake("planQty") == "plan_qty"
        assert ColumnMapper._to_snake("woid") == "woid"
        assert ColumnMapper._to_snake("multipleWordsHere") == "multiple_words_here"
        assert ColumnMapper._to_snake("simpleProcedureVOS") == "simple_procedures"
        assert ColumnMapper._to_snake("productSpecificationQtyVOS") == "product_specification_qties"
