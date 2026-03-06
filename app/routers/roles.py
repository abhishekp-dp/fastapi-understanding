from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.roles import create_role
from app.database import get_db

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud
from app.crud import roles as crud_roles
from app.schemas import roles as schemas
from app.database import get_db  # your DB session function under database
from app.models import roles


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@router.post("/createroles")
def createroles(id: int, name: str, db: Session = Depends(get_db)):

    return create_role(db,id,name)