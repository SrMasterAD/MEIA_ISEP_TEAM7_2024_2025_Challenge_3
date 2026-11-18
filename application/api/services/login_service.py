import logging

# Set up logger
logger = logging.getLogger(__name__)

from fastapi import HTTPException
from application.api.models.login_request import LoginRequest
from application.api.repository import user_repository
from application.api.utils.security_utils import verify_password
from application.api.utils.token_utils import create_access_token

async def login_user(user: LoginRequest) -> dict:
    found = await user_repository.get_user_by_email(user.email)
    if not found or not verify_password(user.password, found["password"]):
        logger.warning(f"Failed login attempt for email: {user.email}")
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(data={"sub": str(found["id"])})
    return {"access_token": token, "token_type": "bearer"}
