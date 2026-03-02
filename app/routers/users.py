from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from app.crud import users as crud_user
from app.schemas import users as schemas
from app.database import get_db  # your DB session function under database
from app.crud.users import create_user, get_user_by_company
from app.crud.users import get_user_by_id


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

@router.get("/{user_id}", response_model=schemas.UserResponse)
def getuser(user_id : int , db: Session = Depends(get_db)):
    user = get_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/{company_id}/")
def getusers_company(company_id: int,db: Session = Depends(get_db)):
    user_company=get_user_by_company(db, company_id)
    if not user_company:
        raise HTTPException(status_code=404, detail="User with this company not found")
    return user_company