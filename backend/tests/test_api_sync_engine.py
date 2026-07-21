"""Tests for ApiSyncEngine — config loading, day slicing."""
import pytest
from datetime import date
from app.modules.ingestion.engines.api_sync_engine import load_config, slice_days


class TestSliceDays:
    def test_single_day(self):
        start = date(2026, 7, 1)
        end = date(2026, 7, 1)
        slices = list(slice_days(start, end))
        assert len(slices) == 1
        assert slices[0] == (date(2026, 7, 1), date(2026, 7, 2))

    def test_multi_day(self):
        start = date(2026, 7, 1)
        end = date(2026, 7, 3)
        slices = list(slice_days(start, end))
        assert len(slices) == 3

    def test_no_reverse_range(self):
        with pytest.raises(ValueError):
            list(slice_days(date(2026, 7, 5), date(2026, 7, 1)))


class TestLoadConfig:
    def test_loads_valid_yaml(self, tmp_path):
        import yaml
        cfg = tmp_path / "test.yaml"
        cfg.write_text(
            yaml.dump({
                "name": "test",
                "connection": {"base_url": "http://example.com", "auth_type": "none"},
                "interfaces": [{"name": "if1", "endpoint": "/api/test", "target_table": "raw.test"}],
            }),
            encoding="utf-8",
        )
        loaded = load_config(str(cfg))
        assert loaded["name"] == "test"
        assert len(loaded["interfaces"]) == 1

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            load_config("/nonexistent/config.yaml")
