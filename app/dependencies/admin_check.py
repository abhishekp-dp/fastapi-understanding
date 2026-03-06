from fastapi import HTTPException
from rich import status
from sqlalchemy.orm import Session

from app.models import User

def admin_check(db: Session, current_user_id: int):
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise HTTPException(
            status_code=400,
            detail="User doesn't exist"
        )
    if user.role_id == 2:
        return user
    else:
        raise HTTPException(
            status_code=400,
            detail="Only admin can create new user"
        )