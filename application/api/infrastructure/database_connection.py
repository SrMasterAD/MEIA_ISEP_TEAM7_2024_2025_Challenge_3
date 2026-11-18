import databases
import sqlalchemy

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/deepwheatdb"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)

def create_all_tables():
    from application.api.schemas.users_schema import users
    metadata.create_all(engine)

async def connect():
    await database.connect()

async def disconnect():
    await database.disconnect()
