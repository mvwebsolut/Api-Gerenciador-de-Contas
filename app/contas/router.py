from fastapi import APIRouter

api_router = APIRouter(prefix='/contas')

from .routes import *