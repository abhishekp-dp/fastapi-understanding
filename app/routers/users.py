from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import users as crud_user
from app.schemas import users as schemas
from app.database import get_db  # your DB session function under database
from app.crud.users import create_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    """
    Read all users from the database
    """
    return crud_user.get_all_users(db)


@router.post("/createuser/")
def createusers(name: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, name, email)