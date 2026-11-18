from sqlalchemy import Table, Column, Integer, String
from application.api.infrastructure.database_connection import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(50), unique=True, nullable=False),
    Column("name", String(255), nullable=False),
    Column("password", String(255), nullable=False)
)
