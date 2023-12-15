from fastapi import APIRouter

router = APIRouter(prefix='/conta-pagar-receber')

from .routes import *