import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates

from pos_api.utils.app import  (
    catch_exceptions_middleware,
    jwt_middleware,
    security_headers_middleware,
)

from pos_api.mongodb import connect_db, close_db

from pos_pkg import config
from pos_pkg.config import WEBHOST

def create_app():
    app = FastAPI(docs_url=None, redoc_url=None)
    connect_db()
    app.add_event_handler("shutdown", close_db)
    app.middleware("http")(catch_exceptions_middleware)
    app.middleware("http")(security_headers_middleware)
    app.middleware("http")(jwt_middleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[WEBHOST],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    from pos_api.dependencies.users import create_users_app

    app.users = create_users_app()
    return app

app = create_app()

@app.on_event("startup")
def register_routes():
    from pos_api.endpoints import (
        users,
    )
    users.register_routes(app)

    app.include_router(users.router)


def run_dev_server():
    uvicorn.run(
        app="galileo_forms_api.app:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        workers=4,
        reload_dirs=[
            config.PROJECT_DIR / "api",
            config.PROJECT_DIR / "pkg",
        ],
    )


if __name__ == "__main__":
    run_dev_server()