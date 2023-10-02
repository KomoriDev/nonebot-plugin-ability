from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")

from .text import md5 as md5
from .text import indent as indent
from .text import random_string as random_string

from .message import extract_at_users as extract_at_users
from .message import extract_image_urls as extract_image_urls
from .message import extract_plain_text as extract_plain_text

from .utils import get_path as get_path
from .utils import load_data as load_data
from .utils import is_file_path as is_file_path
from .utils import awaitable as awaitable

from .requests import Requests as Requests

__plugin_meta__ = PluginMetadata(
    name="聚能环",
    description="NoneBot 外置电池",
    usage="详见文档",
    type="library",
    homepage="https://github.com/KomoriDev/nonebot-plugin-ability",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
)
