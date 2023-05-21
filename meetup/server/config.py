import dotenv
import os
import pytz

dotenv.load_dotenv()

TZ = pytz.timezone(os.getenv("TZ"))
WEBHOOK_API_TOKEN = os.getenv("WEBHOOK_API_TOKEN")
