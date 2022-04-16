from fastapi import FastAPI

import dependency


async def startup(app: FastAPI):
    dependency.inject()


async def shutdown(app: FastAPI):
    pass