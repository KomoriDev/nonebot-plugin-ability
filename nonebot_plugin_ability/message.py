from nonebot.internal.adapter import Bot, Event, Message
from nonebot_plugin_alconna import At, Image, UniMessage


async def extract_plain_text(message: Message) -> str:
    """
    提取消息中纯文本消息。
    """
    return message.extract_plain_text().strip()


async def extract_image_urls(bot: Bot, event: Event) -> list[str | None]:
    """
    提取消息中的图片链接。
    :return: 图片链接列表
    """
    unimsg = await UniMessage.generate(event, bot)
    return [image.url for image in unimsg[Image]]


async def extract_at_users(bot: Bot, event: Event) -> list[str]:
    """
    提取消息中提及的用户。
    :return: 提及用户列表
    """
    unimsg = await UniMessage.generate(event, bot)
    return [at.target for at in unimsg[At]]
