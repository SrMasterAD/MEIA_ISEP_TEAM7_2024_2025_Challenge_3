from pydantic import BaseModel

class UserConfigurationsResponse(BaseModel):
    id: int
    user_id: int
    area: float
    plantation_cost: float
    expected_profit: float
    expected_yield: float
