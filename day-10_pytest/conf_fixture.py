from conftest import config_dict
from typing import Iterable

def test_config_dict_type() -> None:
    sample: config_dict = {
        "username": "admin",
        "timeout": 30,
        "threshold": 0.75,
        "is_enabled": False
    }
    assert isinstance(sample, dict)
    assert isinstance(sample["username"], str)
    assert isinstance(sample["timeout"], int)
    assert isinstance(sample["threshold"], float)
    assert isinstance(sample["is_enabled"], bool)
    
def test_sample_data_fixture(sample_data: Iterable[config_dict]) -> None:
    for data in sample_data:
        assert "name" in data
        assert "age" in data
        assert "height" in data
        assert "is_active" in data