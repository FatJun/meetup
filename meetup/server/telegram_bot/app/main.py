import uvicorn
from fastapi import FastAPI
from . import dependencies as dp

from .webhooks import WebHook, MeetCreated, MeetStarted, MeetStartWithinTenMinutes

app = FastAPI()


@app.post("/webhook", dependencies=[dp.validate_webhook_api_token])
async def webhook_handler(action: dict) -> None:
    match action["action"]:
        case {"type": MeetCreated.type, "payload": payload}:
            webhook = MeetCreated(**payload)
        case {"type": MeetStarted.type, "payload": payload}:
            webhook = MeetStarted(**payload)
        case {"type": MeetStartWithinTenMinutes.type, "payload": payload}:
            webhook = MeetStartWithinTenMinutes(**payload)
        case _:
            return
    webhook: WebHook
    await webhook.execute()


def main():
    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == '__main__':
    main()
