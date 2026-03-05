from sqlalchemy.orm import Session
from app.models.company import Company  # ✅ correct model import
from app.models.users import User


def get_all_company(db: Session):
    return db.query(Company).all()

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def create_company(db: Session, company_name: str, location: str):
    # Step 1: Create object
    new_company = Company(company_name=company_name,location=location)

    # Step 2: Add to session
    db.add(new_company)

    # Step 3: Commit to database
    db.commit()

    # Step 4: Refresh (to get auto-generated ID)
    db.refresh(new_company)

    # Step 5: Return inserted user
    return new_company

def delete_company(db: Session, company_id: int):
    company_delete = db.query(Company).filter(Company.id == company_id).first()
    db.delete(company_delete)
    db.commit()


def crud_get_users_by_company(db: Session, company_id: int):
    return db.query(User).filter(User.company_id == company_id).all()