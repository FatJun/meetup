import asyncio

import tortoise
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from database.utils import init_db, close_db_connections
from .services import routers
from .config import origins
from database.config import DATABASE_URL, MODULES


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules=MODULES,
    generate_schemas=True,
    add_exception_handlers=True
)

for router in routers:
    if hasattr(router, "router"):
        prefix = router.prefix if hasattr(router, "prefix") else ""
        tags = router.tags if hasattr(router, "tags") else []
        app.include_router(router.router, prefix=prefix, tags=tags)


def main():
    tortoise.run_async(init_db())
    uvicorn.run(app, host="0.0.0.0", port=8000)
    tortoise.run_async(close_db_connections())


if __name__ == '__main__':
    main()
