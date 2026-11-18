from pydantic import BaseModel

class UserRegisterModel(BaseModel):
    id: int
    name: str