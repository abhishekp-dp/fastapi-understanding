from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from app.models.users import User  # ✅ correct model import
from app.models.company import Company


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session):
    print("Abhishek")
    return db.query(User).all()


def create_user(db: Session, name: str, email: str, company_id: int,role_id: int=1):
    # Step 1: Create object
    new_user = User(name=name, email=email,company_id=company_id,role_id=role_id)

    # Step 2: Add to session
    db.add(new_user)

    # Step 3: Commit to database
    db.commit()

    # Step 4: Refresh (to get auto-generated ID)
    db.refresh(new_user)

    # Step 5: Return inserted user
    return new_user

def get_user_by_company (db: Session, company_id: int):
    companyusers = (
        db.query(User)
        .join(Company, User.company_id == Company.id)
        .filter(Company.id == company_id)
        .all()
    )

    return companyusers

def delete_user(db: Session, user_id: int):
    user_delete = db.query(User).filter(User.id == user_id).first()
    db.delete(user_delete)
    db.commit()
