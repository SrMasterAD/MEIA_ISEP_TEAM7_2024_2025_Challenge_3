from sqlalchemy import Table, Column, Integer, Float, ForeignKey
from application.api.infrastructure.database_connection import metadata

user_configurations = Table(
    "user_configurations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), unique=True, nullable=False),
    Column("area", Float, nullable=False),
    Column("plantation_cost", Float, nullable=False),
    Column("expected_profit", Float, nullable=False),
    Column("expected_yield", Float, nullable=False)
)
