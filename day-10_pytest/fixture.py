import tempfile
import pytest
from pathlib import Path
from typing import Iterable,Iterator

@pytest.fixture
def temp_file() -> Iterator[Path]:
    temp_file = tempfile.NamedTemporaryFile(
        mode="w+t",
        encoding="utf-8",
        suffix=".txt",
        delete=False,
        suffix=".yaml",
    )
    temp_file_path = Path(temp_file.name)
    print(f"\n   [FIXTURE SETUP]: temp_file created at {temp_file_path}")
    temp_file.write("Hello, World!\nThis is a TEMPORARY file.\n")
    temp_file.close()
    yield temp_file_path
    print(f"\n   [FIXTURE TEARDOWN]: temp_file deleting {temp_file_path}")
    if temp_file_path.exists():
        temp_file_path.unlink()


def test_read_temp_file(temp_file: Path):
    print("  [TEST] test_read_temp_file running...")
    assert temp_file.exists()
    content = temp_file.read_text(encoding="utf-8").lower()
    print(f"  [TEST] Content of temp_file:\n{content}")
    assert "hello" in content
    assert "temporary" in content