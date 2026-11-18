from pydantic import BaseModel

class UserConfigurationsModel(BaseModel):
    id: int
    user_id: int
    area: float
    plantation_cost: float
    expected_profit: float
    expected_yield: float
