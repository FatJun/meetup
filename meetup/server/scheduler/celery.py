from celery import Celery


app = Celery("scheduler", broker="redis://redis:6379/0", include=["scheduler.tasks.telegram_bot_tasks"])
