from tortoise import Tortoise

from .config import TORTOISE_ORM, USERS_APP_MODELS, MEETS_APP_MODELS


async def init_db():
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    await Tortoise.generate_schemas()


async def close_db_connections():
    await Tortoise.close_connections()


Tortoise.init_models((USERS_APP_MODELS, MEETS_APP_MODELS), "models")
