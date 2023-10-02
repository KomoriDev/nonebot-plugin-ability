import string
import random
import hashlib
import inspect

from typing import Literal


def indent(s: str) -> str:
    """
    删除多行字符串额外缩进
    :param s: 文本
    :return: 文本
    """
    return inspect.cleandoc(s)


def md5(s: str) -> str:
    """
    对字符串进行 md5 加密
    :param s: 需要加密的字符串
    :return: md5加密后的文本
    """
    md5_ = hashlib.md5()
    md5_.update(s.encode())
    return md5_.hexdigest()


def escape(s: str, *, escape_comma: bool = True) -> str:
    """
    对字符串进行 CQ 码转义。
    :param s: 需要转义的字符串
    :param escape_comma: 是否转义逗号（`,`）。
    """
    s = s.replace("&", "&amp;").replace("[", "&#91;").replace("]", "&#93;")
    if escape_comma:
        s = s.replace(",", "&#44;")
    return s


def unescape(s: str) -> str:
    """
    对字符串进行 CQ 码去转义。

    :param s: 需要转义的字符串
    """
    return (
        s.replace("&#44;", ",")
        .replace("&#91;", "[")
        .replace("&#93;", "]")
        .replace("&amp;", "&")
    )


def random_string(
    length: int,
    prefix: str | None = None,
    type: Literal["numeric", "alpha", "alphanumeric"] = "alpha",
    charset: str | None = None,
    num_strings: int = 1,
    seed: int | None = None,
    start_index: int | None = None,
    end_index: int | None = None,
) -> str | list[str]:
    """
    随机字符串
    :param length: 生成的字符串的长度。
    :param prefix: 生成的字符串的前缀。
    :param type: 生成字符串的类型。
    :param charset: 自定义字符集。如果未提供自定义字符集，则根据 type 参数选择默认字符集。
    :param num_strings: 生成字符串的数量。默认为1，即生成单个字符串。如果大于1，则生成字符串列表。
    :param seed: 随机数生成器的种子。默认为None，即不使用种子。
    :param start_index: 用于指定生成字符串的子串范围。默认为 None，即生成整个字符串。
    :param end_index: 用于指定生成字符串的子串范围。默认为 None，即生成整个字符串。

    """
    if seed is not None:
        random.seed(seed)

    if charset is None:
        if type == "numeric":
            charset = string.digits
        elif type == "alpha":
            charset = string.ascii_lowercase
        elif type == "alphanumeric":
            charset = string.ascii_lowercase + string.digits
        else:
            raise ValueError(
                "Invalid type. Must be one of 'numeric', 'alpha', 'alphanumeric'."
            )

    if start_index is not None and end_index is not None:
        if (
            start_index < 0
            or start_index >= length
            or end_index < 0
            or end_index >= length
            or start_index > end_index
        ):
            raise ValueError("Invalid start_index or end_index values.")
        length = end_index - start_index + 1

    if num_strings == 1:
        result = "".join(random.choices(charset, k=length))
    else:
        result = [
            "".join(random.choices(charset, k=length)) for _ in range(num_strings)
        ]

    if prefix is not None:
        if num_strings == 1:
            result = prefix + result[len(prefix) :]
        else:
            result = [prefix + s[len(prefix) :] for s in result]

    return result
