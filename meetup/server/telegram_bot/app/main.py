import uvicorn
from fastapi import FastAPI

from . import dependencies as dp
from . import webhooks

app = FastAPI()


@app.post("/webhook", dependencies=[dp.validate_webhook_api_token])
async def webhook_handler(action: dict) -> None:
    match action["action"]:
        case {"type": webhooks.MeetCreatedNotify.type, "payload": payload}:
            webhook = webhooks.MeetCreatedNotify(**payload)
        case {"type": webhooks.MeetCreatedNotify.type, "payload": payload}:
            webhook = webhooks.MeetCreatedNotify(**payload)
        case {"type": webhooks.MeetStartedNotify.type, "payload": payload}:
            webhook = webhooks.MeetStartedNotify(**payload)
        case {"type": webhooks.MeetStartWithinTenMinutesNotify.type, "payload": payload}:
            webhook = webhooks.MeetStartWithinTenMinutesNotify(**payload)
        case _:
            return
    webhook: webhooks.Webhook
    await webhook.execute()


def main():
    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == '__main__':
    main()
