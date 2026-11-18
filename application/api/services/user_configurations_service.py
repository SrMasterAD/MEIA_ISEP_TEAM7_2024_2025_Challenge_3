from typing import Optional

from fastapi import UploadFile

from application.api.models.user_configurations_model import UserConfigurationsModel
from application.api.models.user_configurations_request import UserConfigurationsRequest
from application.api.repository import user_configurations_repository

from fastapi import HTTPException


async def create_configuration(user_id: int, config: UserConfigurationsRequest) -> UserConfigurationsModel:
    existing = await user_configurations_repository.get_configuration_by_user_id(user_id)
    if existing:
        raise HTTPException(status_code=400, detail="User already has a configuration.")

    return await user_configurations_repository.create_user_configuration(
        user_id=user_id,
        area=config.area,
        plantation_cost=config.plantation_cost,
        expected_profit=config.expected_profit,
        expected_yield=config.expected_yield
    )


async def get_configuration_by_user_id(user_id: int) -> Optional[UserConfigurationsModel]:
    return await user_configurations_repository.get_configuration_by_user_id(user_id)

async def update_configuration(user_id: int, config_id: int, config: UserConfigurationsRequest) -> UserConfigurationsModel:
    return await user_configurations_repository.update_user_configuration(
        config_id=config_id,
        user_id=user_id,
        area=config.area,
        plantation_cost=config.plantation_cost,
        expected_profit=config.expected_profit,
        expected_yield=config.expected_yield
    )


async def delete_configuration(user_id: int, config_id: int) -> dict:
    return await user_configurations_repository.delete_user_configuration(config_id, user_id)

async def handle_photo_upload(user_id:int, picture: UploadFile) -> dict:
    image_data = await picture.read()
    print(f"Received photo: {picture.filename} (size: {len(image_data)} bytes)")

    return {
        "filename": picture.filename,
        "content_type": picture.content_type,
        "size": len(image_data)
    }
