import os
import dotenv
import pytz
import datetime

dotenv.load_dotenv()

TZ = pytz.timezone(os.getenv("TZ"))