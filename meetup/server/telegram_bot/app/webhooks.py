import asyncio
import datetime
from abc import ABC, abstractmethod

from config import TZ
from telegram_bot.config import bot, TELEGRAM_MESSAGES_PER_SECOND_LIMIT
from asyncio_throttle import Throttler
from scheduler.tasks.telegram_bot_tasks import send_webhook_meet_start_within_ten_minutes, send_webhook_meet_started


class WebHook(ABC):
    type: str

    @abstractmethod
    async def execute(self):
        pass


class NotifyTelegramWebHook(WebHook, ABC):
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


class MeetStarted(NotifyTelegramWebHook):
    type = "meet_started"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_name: str):
        super(MeetStarted, self).__init__(meet_members_telegram_chat_ids)
        self.meet_name = meet_name

    @property
    def notification(self):
        return f'Встреча "{self.meet_name}" началась, поторопись!'


class MeetStartWithinTenMinutes(NotifyTelegramWebHook):
    type = "meet_start_within_ten_minutes"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_name: str):
        super(MeetStartWithinTenMinutes, self).__init__(meet_members_telegram_chat_ids)
        self.meet_name = meet_name

    @property
    def notification(self):
        return f'Встреча "{self.meet_name}" начнется в течение 10 минут, будь готов!'


class MeetCreated(NotifyTelegramWebHook):
    type = "meet_created"
    throttler = Throttler(rate_limit=TELEGRAM_MESSAGES_PER_SECOND_LIMIT)

    def __init__(self, meet_members_telegram_chat_ids: list[int], meet_start_at: str, meet_name: str):
        super(MeetCreated, self).__init__(meet_members_telegram_chat_ids)
        self.meet_start_at = datetime.datetime.fromisoformat(meet_start_at).astimezone(TZ)
        self.meet_name = meet_name

    async def execute(self):
        await super(MeetCreated, self).execute()
        send_webhook_meet_start_within_ten_minutes.apply_async(
            eta=self.meet_start_at - datetime.timedelta(minutes=10), args=(
                self.users_telegram_chat_ids, self.meet_name))
        send_webhook_meet_started.apply_async(eta=self.meet_start_at, args=(
            self.users_telegram_chat_ids, self.meet_name))

    @property
    def notification(self) -> str:
        meet_start_at_formatted = self.meet_start_at.strftime('%d.%m.%Y / %H:%M')
        meet_created_notification = ('Вы были приглашены на встречу "%s", которая начнется %s.  '
                                     '(отказаться нельзя! :3)')
        return meet_created_notification % (self.meet_name, meet_start_at_formatted)
