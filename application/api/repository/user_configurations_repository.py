from typing import List, Optional
from application.api.infrastructure.database_connection import database
from application.api.schemas.user_configurations_schema import user_configurations
from application.api.models.user_configurations_model import UserConfigurationsModel


async def create_user_configuration(user_id: int, area: float, plantation_cost: float, expected_profit: float, expected_yield: float) -> UserConfigurationsModel:
    query = user_configurations.insert().values(
        user_id=user_id,
        area=area,
        plantation_cost=plantation_cost,
        expected_profit=expected_profit,
        expected_yield=expected_yield
    )
    record_id = await database.execute(query)
    return UserConfigurationsModel(
        id=record_id,
        user_id=user_id,
        area=area,
        plantation_cost=plantation_cost,
        expected_profit=expected_profit,
        expected_yield=expected_yield
    )


async def get_configuration_by_user_id(user_id: int) -> Optional[UserConfigurationsModel]:
    query = user_configurations.select().where(user_configurations.c.user_id == user_id)

    row = await database.fetch_one(query)
    return UserConfigurationsModel(**row) if row else None


async def get_all_user_configurations(user_id: int) -> List[UserConfigurationsModel]:
    query = user_configurations.select().where(user_configurations.c.user_id == user_id)
    rows = await database.fetch_all(query)
    return [UserConfigurationsModel(**row) for row in rows]


async def update_user_configuration(config_id: int, user_id: int, area: float, plantation_cost: float, expected_profit: float, expected_yield: float) -> UserConfigurationsModel:
    query = user_configurations.update().where(
        (user_configurations.c.id == config_id) & (user_configurations.c.user_id == user_id)
    ).values(
        area=area,
        plantation_cost=plantation_cost,
        expected_profit=expected_profit,
        expected_yield=expected_yield
    )
    await database.execute(query)
    return UserConfigurationsModel(
        id=config_id,
        user_id=user_id,
        area=area,
        plantation_cost=plantation_cost,
        expected_profit=expected_profit,
        expected_yield=expected_yield
    )


async def delete_user_configuration(config_id: int, user_id: int) -> dict:
    query = user_configurations.delete().where(
        (user_configurations.c.id == config_id) & (user_configurations.c.user_id == user_id)
    )
    await database.execute(query)
    return {"message": f"User configuration with id {config_id} has been deleted"}
