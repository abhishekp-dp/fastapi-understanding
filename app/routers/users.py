from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from app.crud import users as crud_user
from app.schemas import users as schemas
from app.database import get_db  # your DB session function under database
from app.crud.users import create_user, get_user_by_company, delete_user
from app.crud.users import get_user_by_id
from app.crud.company import get_all_company
from app.models import Company,User
from app.crud.users import delete_user
from app.dependencies.admin_check import admin_check
from app.schemas.users import UserCreate

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
def createusers( usercreate: UserCreate,db: Session = Depends(get_db)):
    company= db.query(Company).filter(Company.id==usercreate.company_id).first()
    email_exists = db.query(User).filter(User.email==usercreate.email).first()
    if not company:
        raise HTTPException(
            status_code=400,
            detail="Company does not exist"
        )
    if email_exists:
        raise HTTPException(
            status_code=400,
            detail="Email already exist"
        )

    #admin_check(db,current_user_id)

    return create_user(db,usercreate)

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


@router.delete("/{user_id}/")
def deleteuser(user_id: int,  current_user_id: int=1 , db: Session = Depends(get_db)):
    user_exist = db.query(User).filter(User.id == user_id).first()
    if not user_exist:
        raise HTTPException(status_code=404, detail="User doesn't exist")

    #admin_check(db, current_user_id)
    delete_user(db, user_id)
    return {"User Deleted Successfully"}


