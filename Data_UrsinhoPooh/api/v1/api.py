from fastapi import APIRouter

from api.v1.endpoints import Pooh

api_router = APIRouter()

api_router.include_router(Pooh.router, prefix='/Pooh', tags=["Pooh"])