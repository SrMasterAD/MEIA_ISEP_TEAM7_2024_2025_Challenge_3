from pydantic import BaseModel

class UserConfigurationsRequest(BaseModel):
    area: float
    plantation_cost: float
    expected_profit: float
    expected_yield: float
