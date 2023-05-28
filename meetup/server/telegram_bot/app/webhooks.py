import asyncio
import datetime
from abc import ABC, abstractmethod

from asyncio_throttle import Throttler

from config import TZ
from telegram_bot.config import bot, TELEGRAM_MESSAGES_PER_SECOND_LIMIT
from scheduler.tasks import telegram_bot_tasks


class Webhook(ABC):
    type: str

    @abstractmethod
    async def execute(self):
        pass


class NotifyTelegramWebhook(Webhook, ABC):
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, telegram_chat_ids: list[int]):
        self.users_telegram_chat_ids = telegram_chat_ids

    async def execute(self):
        await self.notify_users_in_telegram()

    async def notify_users_in_telegram(self):
        tasks = []
        for telegram_chat_id in self.users_telegram_chat_ids:
            coro = self.notify_user_by_chat_id(telegram_chat_id)
            tasks.append(asyncio.create_task(coro))
        await asyncio.gather(*tasks)

    async def notify_user_by_chat_id(self, chat_id: int):
        async with self.throttler:
            await bot.send_message(chat_id, self.notification)

    @property
    @abstractmethod
    def notification(self) -> str:
        pass


class MeetStartedNotify(NotifyTelegramWebhook):
    type = "meet_started_notify"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_name: str):
        super(MeetStartedNotify, self).__init__(meet_members_telegram_chat_ids)
        self.meet_name = meet_name

    @property
    def notification(self):
        return f'Встреча "{self.meet_name}" началась, поторопись!'


class MeetStartWithinTenMinutesNotify(NotifyTelegramWebhook):
    type = "meet_start_within_ten_minutes_notify"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_name: str):
        super(MeetStartWithinTenMinutesNotify, self).__init__(meet_members_telegram_chat_ids)
        self.meet_name = meet_name

    @property
    def notification(self):
        return f'Встреча "{self.meet_name}" начнется в течение 10 минут, будь готов!'


class MeetCreatedNotify(NotifyTelegramWebhook):
    type = "meet_created_notify"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_start_at: str, meet_name: str):
        super(MeetCreatedNotify, self).__init__(meet_members_telegram_chat_ids)
        self.meet_start_at = datetime.datetime.fromisoformat(meet_start_at).astimezone(TZ)
        self.meet_name = meet_name

    @property
    def notification(self) -> str:
        meet_start_at_formatted = self.meet_start_at.strftime('%d.%m.%Y / %H:%M')
        meet_created_notification = 'Вы были приглашены на встречу "{0}", которая начнется {1}. (отказаться нельзя! :3)'
        return meet_created_notification.format(self.meet_name, meet_start_at_formatted)


class MeetCreated(Webhook):
    type = "meet_created"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_start_at: str, meet_name: str):
        self.meet_members_telegram_chat_ids = meet_members_telegram_chat_ids
        self.meet_start_at = datetime.datetime.fromisoformat(meet_start_at).astimezone(TZ)
        self.meet_name = meet_name

    async def execute(self):
        telegram_bot_tasks.send_webhook_meet_created_notify.delay(self.meet_members_telegram_chat_ids,
                                                                  self.meet_name, self.meet_start_at)
        telegram_bot_tasks.send_webhook_meet_start_within_ten_minutes_notify.apply_async(
            eta=self.meet_start_at - datetime.timedelta(minutes=10),
            args=(self.meet_members_telegram_chat_ids, self.meet_name))
        telegram_bot_tasks.send_webhook_meet_started_notify.apply_async(
            eta=self.meet_start_at,
            args=(self.meet_members_telegram_chat_ids, self.meet_name))
