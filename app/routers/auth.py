from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db  # your DB session function under database
from app.schemas.auth_schema import LoginRequest
from app.crud.crud_auth import get_user_by_email
from app.core.security import verify_password
from app.core.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(logindata: LoginRequest, db: Session = Depends(get_db)):

    user = get_user_by_email(db, logindata.email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(logindata.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token(
        {
            "user_id": user.id,
            "role_id": user.role_id,
            "company_id": user.company_id
        }
    )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "role_id": user.role_id,
        "company_id": user.company_id,
        "access_token": token,
        "token_type": "bearer"
    }


