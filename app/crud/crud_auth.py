from pydantic.v1 import EmailStr
from sqlalchemy.orm import Session
from app.models.company import Company  # ✅ correct model import
from app.models.users import User
from app.schemas.company import CompanyCreate


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()