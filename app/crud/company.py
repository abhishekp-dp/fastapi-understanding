from sqlalchemy.orm import Session
from app.models.company import Company  # ✅ correct model import


def get_all_company(db: Session):
    return db.query(Company).all()