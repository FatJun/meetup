import tortoise
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.utils import init_db, close_db_connections
from database.config import TORTOISE_ORM
from .config import origins
from .services import routers


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
    config=TORTOISE_ORM,
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
