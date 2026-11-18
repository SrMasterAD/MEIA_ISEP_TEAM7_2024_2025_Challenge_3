from passlib.context import CryptContext
from application.api.infrastructure.database_connection import database
from application.api.models.register_request import RegisterRequest
from application.api.models.user_register_model import UserRegisterModel
from application.api.schemas.users_schema import users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def create_user(user: RegisterRequest):
    query = users.insert().values(
        email=user.email,
        name=user.name,
        password=user.password  # already hashed!
    )
    user_id = await database.execute(query)
    return UserRegisterModel(id=user_id, name=user.name)



async def get_user_by_email(user_email: str):
    query = users.select().where(users.c.email == user_email)
    return await database.fetch_one(query)