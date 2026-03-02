from sqlalchemy.orm import Session
from app.models.company import Company  # ✅ correct model import


def get_all_company(db: Session):
    return db.query(Company).all()

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()