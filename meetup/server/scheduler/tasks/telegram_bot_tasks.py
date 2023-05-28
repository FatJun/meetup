import datetime

from scheduler.celery import app
from utils import sync_send_webhook


@app.task
def send_webhook_meet_start_within_ten_minutes_notify(meet_members_telegram_chat_ids: list[int], meet_name: str):
    sync_send_webhook("meet_start_within_ten_minutes_notify",
                      meet_members_telegram_chat_ids=meet_members_telegram_chat_ids,
                      meet_name=meet_name)


@app.task
def send_webhook_meet_started_notify(meet_members_telegram_chat_ids: list[int], meet_name: str):
    sync_send_webhook("meet_started_notify",
                      meet_members_telegram_chat_ids=meet_members_telegram_chat_ids,
                      meet_name=meet_name)


@app.task
def send_webhook_meet_created_notify(meet_members_telegram_chat_ids: list[int], meet_name: str,
                                     meet_start_at: datetime.datetime):
    sync_send_webhook("meet_created_notify", meet_members_telegram_chat_ids=meet_members_telegram_chat_ids,
                      meet_name=meet_name, meet_start_at=meet_start_at)
