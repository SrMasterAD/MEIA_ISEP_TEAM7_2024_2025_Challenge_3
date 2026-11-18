from fastapi import HTTPException
from application.api.models.register_request import RegisterRequest
from application.api.models.register_response import RegisterResponse
from application.api.repository import user_repository
from application.api.utils.security_utils import hash_password
from application.api.utils.token_utils import create_access_token
import logging

logger = logging.getLogger(__name__)

async def register_user(user: RegisterRequest) -> RegisterResponse:
    existing = await user_repository.get_user_by_email(user.email)
    if existing:
        logger.error(f"User with email {user.email} already exists")
        raise HTTPException(status_code=400, detail="User already registered")

    user.password = hash_password(user.password)
    created_user = await user_repository.create_user(user)

    access_token = create_access_token(data={"sub": str(created_user.id)})

    return RegisterResponse(
        id=created_user.id,
        name=created_user.name,
        access_token=access_token
    )
