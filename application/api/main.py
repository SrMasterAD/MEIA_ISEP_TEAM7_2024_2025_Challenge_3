import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from application.api.controllers.login_controller import router as login_router
from application.api.controllers.register_controller import router as register_router
from application.api.controllers.user_configurations_controller import router as user_config_router
from application.api.controllers.report_controller import router as report_router

from application.api.infrastructure.database_connection import database, create_all_tables, connect

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers
app.include_router(login_router)
app.include_router(register_router)
app.include_router(user_config_router)
app.include_router(report_router)

@app.on_event("startup")
async def startup():
    create_all_tables()
    await connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
