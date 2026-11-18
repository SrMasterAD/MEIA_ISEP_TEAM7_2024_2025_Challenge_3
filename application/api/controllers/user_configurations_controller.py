import logging

# Set up logger
logger = logging.getLogger(__name__)

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from application.api.services import user_configurations_service
from application.api.models.user_configurations_model import UserConfigurationsModel
from application.api.models.user_configurations_request import UserConfigurationsRequest
from application.api.models.user_configurations_response import UserConfigurationsResponse
from application.api.utils.token_utils import get_current_user_id_from_token

router = APIRouter(tags=["User Configurations"])

# Mapper: domain model → response DTO
def to_response_dto(domain: UserConfigurationsModel) -> UserConfigurationsResponse:
    return UserConfigurationsResponse(**domain.dict())

@router.post("/user/configurations", response_model=UserConfigurationsResponse)
async def create_config(
    config: UserConfigurationsRequest,
    user_id: int = Depends(get_current_user_id_from_token)
):
    domain = await user_configurations_service.create_configuration(user_id, config)
    return to_response_dto(domain)

@router.post("/user/configurations/{config_id}/upload-photo")
async def upload_config_photo(
    picture: UploadFile = File(...),
    user_id: int = Depends(get_current_user_id_from_token)
):
    try:
        return await user_configurations_service.handle_photo_upload(user_id, picture)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/user/configurations", response_model=UserConfigurationsResponse)
async def get_config_by_user_id(
    user_id: int = Depends(get_current_user_id_from_token)
):
    domain = await user_configurations_service.get_configuration_by_user_id(user_id)
    if domain is None:
        logger.error("failed to get configuration for user_id: {user_id}")
        raise HTTPException(status_code=500, detail="Configuration not found")
    return to_response_dto(domain)

@router.put("/user/configurations/{config_id}", response_model=UserConfigurationsResponse)
async def update_config(
    config_id: int,
    config: UserConfigurationsRequest,
    user_id: int = Depends(get_current_user_id_from_token)
):
    domain = await user_configurations_service.update_configuration(user_id, config_id, config)
    return to_response_dto(domain)

@router.delete("/user/configurations/{config_id}")
async def delete_config(config_id: int, user_id: int = Depends(get_current_user_id_from_token)):
    return await user_configurations_service.delete_configuration(user_id, config_id)
