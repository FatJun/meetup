from typing import Type

from tortoise.expressions import Q
from tortoise.signals import post_save

from database.meets.models import Meet
from utils import async_send_webhook


@post_save(Meet)
async def send_meet_created_webhook(_: Type[Meet], instance: Meet, *args):
    telegram_chat_ids = await instance.members.filter(~Q(telegram_chat_id=None)).values_list("telegram_chat_id",
                                                                                             flat=True)
    if len(telegram_chat_ids) >= 1:
        await async_send_webhook("meet_created", meet_members_telegram_chat_ids=telegram_chat_ids,
                                 meet_name=instance.name, meet_start_at=instance.start_at.isoformat())
