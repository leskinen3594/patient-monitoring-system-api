from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import partial

from .handlers.events import startup, shutdown
from .controllers import (
    test_endpoint, role_endpoint,
)


origins = ["api-pms-dev.herokuapp.com"]


def create_app():
    fast_app = FastAPI(title='Patient Monitoring System', description="API ระบบติดตามผลการตรวจของแพทย์ (Demo)")
    fast_app.add_event_handler('startup', func=partial(startup, app=fast_app))
    fast_app.add_event_handler('shutdown', func=partial(shutdown, app=fast_app))
    fast_app.include_router(test_endpoint.router, prefix='/v1/ping', tags=['Ping'])
    fast_app.include_router(role_endpoint.router, prefix='/v1/roles', tags=['Role'])
    return fast_app

app = create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Run with cli
# uvicorn api.main:app --reload --host 0.0.0.0 --port 5000
# web: uvicorn api.main:app --host=0.0.0.0 --port=${PORT:-5000}