import uvicorn
from fastapi import FastAPI
from app.views import api


def init_app():
    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        pass

    @app.on_event("shutdown")
    async def shutdown():
        pass

    app.include_router(api)

    return app


app = init_app()