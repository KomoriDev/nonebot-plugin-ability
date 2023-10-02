import pytest

from typing import Any
from pathlib import Path


@pytest.fixture
def temp_file(tmp_path):
    from nonebot_plugin_ability.utils import json

    file_path = tmp_path / "test_file.json"
    data = {"key": "value"}
    with open(file_path, "w") as file:
        json.dump(data, file)
    return file_path


def test_get_path():
    from nonebot_plugin_ability.utils import get_path

    current_file = Path(__file__)
    expected_path = current_file.resolve().parent / "test_file.json"

    assert get_path("test_file.json") == expected_path


def test_load_data(temp_file):
    from nonebot_plugin_ability.utils import load_data

    data = load_data(temp_file)
    assert data == {"key": "value"}


def test_is_file_path(temp_file):
    from nonebot_plugin_ability.utils import is_file_path

    assert is_file_path(temp_file) is True
    assert is_file_path("nonexistent_file.txt") is False


@pytest.mark.asyncio
async def test_awaitable():
    from nonebot_plugin_ability.utils import awaitable

    @awaitable
    def sync_func() -> Any:
        return "test"

    result = await sync_func()
    assert result == "test"
