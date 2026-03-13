from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import company as crud_company
from app.schemas import company as schemas
from app.database import get_db  # your DB session function under database
from app.crud.company import get_all_company, get_company_by_id, create_company, delete_company, crud_get_users_by_company
from app.models import Company,User
from app.schemas.company import CompanyCreate
from app.schemas.auth_schema import LoginRequest
from app.crud.crud_auth import get_user_by_email
from app.core.security import verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(logindata: LoginRequest, db: Session = Depends(get_db)):

    user = get_user_by_email(db, logindata.email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(logindata.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "user_id": user.id,
        "role_id": user.role_id,
        "company_id": user.company_id
    }

