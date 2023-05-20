import os

origins = [
    'http://localhost:3000', 'http://127.0.0.1:3000',
    'https://localhost:3000', 'https://127.0.0.1:3000'
]
WEBHOOK_API_TOKEN = os.getenv("WEBHOOK_API_TOKEN")
