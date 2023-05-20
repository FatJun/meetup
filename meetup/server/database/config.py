from tortoise import Tortoise

from . import models

DATABASE_URL = "postgres://postgres:Qwerty12345@db:5432/postgresDB"
MODULES = {"models": models}
Tortoise.init_models(models, "models")
pre_init_database = "Database pre-init"
