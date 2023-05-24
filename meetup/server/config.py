import dotenv
import os
import pytz
import logging

dotenv.load_dotenv()

TZ = pytz.timezone(os.getenv("TZ"))
WEBHOOK_API_TOKEN = os.getenv("WEBHOOK_API_TOKEN")
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] [%(asctime)s] - %(message)s')