import uvicorn
from fastapi import FastAPI

from . import dependencies as dp
from . import webhooks

app = FastAPI()


@app.post("/webhook", dependencies=[dp.validate_webhook_api_token])
async def webhook_handler(action: dict) -> None:
    match action["action"]:
        case {"type": webhooks.MeetCreated.type, "payload": payload}:
            webhook = webhooks.MeetCreated(**payload)
        case {"type": webhooks.MeetStarted.type, "payload": payload}:
            webhook = webhooks.MeetStarted(**payload)
        case {"type": webhooks.MeetStartWithinTenMinutes.type, "payload": payload}:
            webhook = webhooks.MeetStartWithinTenMinutes(**payload)
        case _:
            return
    webhook: webhooks.WebHook
    await webhook.execute()


def main():
    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == '__main__':
    main()
