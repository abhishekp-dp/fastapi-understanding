from fastapi import FastAPI
from app.models import users
from app.routers import users
from app.routers import company
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(company.router)

