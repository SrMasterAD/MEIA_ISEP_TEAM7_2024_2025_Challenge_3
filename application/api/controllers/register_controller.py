from fastapi import APIRouter

from application.api.models.register_request import RegisterRequest
from application.api.models.register_response import RegisterResponse
from application.api.services.register_service import register_user

router = APIRouter(tags=["Register"])

@router.post("/register", response_model=RegisterResponse)
async def request_register(request: RegisterRequest):
    return await register_user(request)