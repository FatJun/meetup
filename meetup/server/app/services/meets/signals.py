from typing import Type

from tortoise.expressions import Q
from tortoise.signals import post_save

from database.meets.models import Meet
from utils import async_send_webhook


@post_save(Meet)
async def send_meet_created_webhook(_: Type[Meet], instance: Meet, created: bool, *args):
    registered_in_telegram_members = instance.members.filter(Q(registered_in_telegram=True))
    telegram_chat_ids: list[int] = await registered_in_telegram_members.values_list("telegram_chat_id", flat=True)
    if created:
        telegram_chat_ids.append(instance.creator.telegram_chat_id)
    webhook_payload = {
        "meet_members_telegram_chat_ids": telegram_chat_ids, "meet_start_at": instance.start_at.isoformat(),
        "meet_name": instance.name,
    }
    await async_send_webhook("meet_created", **webhook_payload)
