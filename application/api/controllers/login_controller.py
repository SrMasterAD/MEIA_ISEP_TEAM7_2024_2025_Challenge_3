from fastapi import APIRouter, Depends

from application.api.models.login_request import LoginRequest
from application.api.services.login_service import login_user

router = APIRouter(tags=["Login"])

@router.post("/login")
async def request_login(request: LoginRequest):
    return await login_user(request)
