import pytest
from typing import Iterable, Dict

config_dict = Dict[str, str | int | float | bool]

@pytest.fixture
def sample_data() -> Iterable[config_dict]:
    print("Setting up sample data")
    yield [{
        "name": "Test User",
        "age": 30,
        "height": 5.9,
        "is_active": True
    }]
    print("Tearing down sample data")