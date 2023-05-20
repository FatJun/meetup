import requests


def sync_send_webhook(action_type: str, **payload):
    url = "http://telegram-bot:8001/webhook"
    json = {"action": {"type": action_type, "payload": payload}}
    requests.post(url, json=json)
