from sqlalchemy.orm import Session
from app.models.company import Company  # ✅ correct model import
from app.models.users import User
from app.schemas.company import CompanyCreate


def get_all_company(db: Session,page: int,limit: int,sort_by: str,order: str):

    skip = (page-1) * limit

    query=db.query(Company)

    # ✅ Allowed columns (important)
    allowed_field =["id","name"]

    if sort_by not in allowed_field:
        sort_by = "id"

    # ✅ Convert string → column
    columns = getattr(Company,sort_by)
    if order == "desc":
        query=query.order_by(columns.desc())
    else:
        query = query.order_by(columns.asc())

    total = query.count()
    companies = (query
             .offset(skip)
             .limit(limit)
             .all())
    return companies , total

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def create_company(db: Session, company: CompanyCreate):
    # Step 1: Create object
    new_company = Company(company_name=company.company_name,location=company.location)

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