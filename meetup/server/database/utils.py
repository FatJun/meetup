from tortoise import Tortoise

from .config import DATABASE_URL, MODULES


async def init_db():
    await Tortoise.init(
        modules=MODULES,
        db_url=DATABASE_URL,
    )
    await Tortoise.generate_schemas()


async def close_db_connections():
    await Tortoise.close_connections()

