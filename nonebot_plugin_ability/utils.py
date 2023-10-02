import yaml
import inspect
import asyncio

from nonebot.exception import NoneBotException
from pathlib import Path
from functools import wraps
from typing import Any, Callable, TypeVar, ParamSpec, Coroutine

try:
    import ujson as json
except ImportError:
    import json

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


R = TypeVar("R")
"""返回值泛型。"""

P = ParamSpec("P")
"""参数泛型"""


class ResourceError(NoneBotException):
    """资源操作异常"""


class FileNotExistError(ResourceError, FileNotFoundError):
    """文件不存在"""


class ReadFileError(ResourceError):
    """读取文件错误"""


class WriteFileError(ResourceError):
    """写入文件错误"""


class FileTypeError(ResourceError):
    """文件类型错误"""


def get_path(file: str | Path, *, depth: int = 0) -> Path:
    """
    获取文件或目录的绝对路径
    :param file: 文件路径，如果为相对路径，则相对于当前文件的父目录
    :param depth: depth: 调用栈深度。默认为 0，即当前函数调用栈的深度
    """
    if Path(file).is_absolute():
        path = Path(file)
    else:
        path = Path(inspect.stack()[depth + 1].filename).parent / file

    return path.resolve()


def load_data(file: str | Path) -> dict[str, Any]:
    """
    读取文件数据
    支持的文件格式有：`json`、`yaml`、`toml`。

    :param file: 文件路径，如果为相对路径，则相对于当前文件的父目录
    :raise FileNotExistError: 文件不存在
    :raise FileTypeError: 文件格式不支持
    :raise ReadFileError: 文件内容为空
    :return: 解析后的数据
    """

    data_path = get_path(file, depth=1)

    if not data_path.exists():
        raise FileNotExistError(f"找不到文件: {data_path}")

    data = data_path.read_text(encoding="utf-8")
    file_type = data_path.suffix.removeprefix(".")

    if file_type == "json":
        file_data = json.loads(data)
    elif file_type in ("yml", "yaml"):
        file_data = yaml.safe_load(data)
    elif file_type == "toml":
        file_data = tomllib.loads(data)
    else:
        raise FileTypeError(f"不支持的文件类型: {file_type}, 只能是 json、yaml 或 toml")

    if file_data is None:
        raise ReadFileError(f"文件内容为空: {data_path}")

    return file_data


def is_file_path(path: str | Path) -> bool:
    """
    判断是否是一个有效的文件路径。
    :param path: 文件路径
    """
    try:
        return Path(path).is_file()
    except OSError:
        return False


def awaitable(func: Callable[P, R]) -> Callable[P, Coroutine[Any, Any, R]]:
    """同步转异步装饰器"""

    @wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return await asyncio.to_thread(func, *args, **kwargs)

    return wrapper
