from sqlalchemy.orm import Session
from app.models.users import User   # ✅ correct model import

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    print("Abhishek")
    return db.query(User).all()