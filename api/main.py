from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import partial
from .handlers.events import startup, shutdown
from .controllers import (
    test_endpoint, role_endpoint, prefix_endpoint,
    user_endpoint, doctor_endpoint, patient_endpoint,
    log_endpoint, ptl_endpoint
)
from message_broker import connectMQTT, publish


origins = ["https://api-pms-dev.herokuapp.com"]


def create_app():
    fast_app = FastAPI(title='Patient Monitoring System', description="API ระบบติดตามผลการตรวจของแพทย์ (Demo)")
    fast_app.add_event_handler('startup', func=partial(startup, app=fast_app))
    fast_app.add_event_handler('shutdown', func=partial(shutdown, app=fast_app))
    fast_app.include_router(test_endpoint.router, prefix='/v1/ping', tags=['Ping'])
    fast_app.include_router(role_endpoint.router, prefix='/v1/roles', tags=['Role'])
    fast_app.include_router(prefix_endpoint.router, prefix='/v1/prefixs', tags=['Prefix Name'])
    fast_app.include_router(user_endpoint.router, prefix='/v1/users', tags=['User'])
    fast_app.include_router(doctor_endpoint.router, prefix='/v1/doctors', tags=['Doctor'])
    fast_app.include_router(patient_endpoint.router, prefix='/v1/patients', tags=['Patient'])
    fast_app.include_router(ptl_endpoint.router, prefix='/v1/patients-list', tags=['Patient List'])
    fast_app.include_router(log_endpoint.router, prefix='/v1/estimate-log', tags=['Estimate Log'])
    return fast_app

connectMQTT()
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