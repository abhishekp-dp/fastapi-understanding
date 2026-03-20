import offset
from sqlalchemy import column, desc, or_
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from app.models.users import User  # ✅ correct model import
from app.models.company import Company
from app.schemas.users import UserCreate
from app.core.security import hash_password


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session,page: int,limit: int,sort_by: str,order: str,search: str,current_user_role: int | None,current_user_company: int | None):

    skip = (page-1) * limit

    if current_user_role != 2: #role_id=2 is admin
        query=db.query(User).join(Company, User.company_id == Company.id).filter(Company.id == current_user_company)
    else:
        query = db.query(User).join(Company, User.company_id == Company.id)

    if search:
        query = query.filter(
                or_(User.name.ilike(f"%{search}%"),
                 User.email.ilike(f"%{search}%"),
                        Company.company_name.ilike(f"%{search}%")
                 )
        )

    # ✅ Allowed columns (important)
    allowed_field =["id","name"]

    if sort_by not in allowed_field:
        sort_by = "id"

    # ✅ Convert string → column
    columns = getattr(User,sort_by)
    if order == "desc":
        query=query.order_by(columns.desc())
    else:
        query = query.order_by(columns.asc())

    users = (query
             .offset(skip)
             .limit(limit)
             .all())
    total = query.count()
    return users , total


def create_user(db: Session, usercreate: UserCreate):

    # password will be hashed before storing
    hashed_password = hash_password(str(usercreate.password))
    # Step 1: Create object
    new_user = User(name=usercreate.name,
                    email=usercreate.email,
                    company_id=usercreate.company_id,
                    role_id=usercreate.role_id,
                    password=hashed_password)

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
