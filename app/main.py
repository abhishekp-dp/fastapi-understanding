from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.models import users
from app.routers import users
from app.routers import company,roles
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs#")

app.include_router(users.router)
app.include_router(company.router)
app.include_router(roles.router)

