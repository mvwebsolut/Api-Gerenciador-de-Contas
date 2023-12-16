import sys, asyncio

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from app.contas import api_router

app = FastAPI()
app.include_router(api_router)
