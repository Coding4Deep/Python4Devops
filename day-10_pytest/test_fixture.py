import pytest
import tempfile
from pathlib import Path
from typing import Iterable



@pytest.fixture
def temp_config_file() -> Iterable[Path]:
    temp_file = tempfile.NamedTemporaryFile(
        mode="w+t",
        encoding="utf-8",
        suffix=".yaml",
        delete=False,
    )
    temp_file_path = Path(temp_file.name)
    print(
        f"\n   [FIXTURE SETUP]: temp_config_file created at {temp_file_path}"
    )
    temp_file.write("setting1: value1\nsetting2: value2\n")
    temp_file.close()
    yield temp_file_path
    print(
        f"\n   [FIXTURE TEARDOWN]: temp_config_file deleting {temp_file_path}"
    )
    if temp_file_path.exists():
        temp_file_path.unlink()

def test_read_from_temp_file(temp_config_file: Path):
    print("  [TEST] test_read_from_temp_file running...")
    assert temp_config_file.exists()
    content = temp_config_file.read_text(encoding="utf-8")
    assert "setting1: value1" in content
    assert "setting2: value2" in content