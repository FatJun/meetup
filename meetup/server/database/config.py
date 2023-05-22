import os
import dotenv

dotenv.load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
TZ = os.getenv("TZ")

USERS_APP_MODELS = "database.users.models"
MEETS_APP_MODELS = "database.meets.models"

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "db",
                "port": "5432",
                "user": POSTGRES_USER,
                "password": POSTGRES_PASSWORD,
                "database": POSTGRES_DB
            }
        }
    },
    "apps": {
        "models": {
            "models": ("aerich.models", MEETS_APP_MODELS, USERS_APP_MODELS,),
            "default_connection": "default"
        },
    },
    "use_tz": False,
    "timezone": TZ,
}
