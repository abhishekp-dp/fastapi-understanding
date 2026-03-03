from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db  # your DB session function under database
from fastapi import APIRouter

from app.crud import company as crud_company
from app.schemas import company as schemas
from app.database import get_db  # your DB session function under database
from app.crud.company import get_all_company, get_company_by_id, create_company
from app.models import Company

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

@router.get("/", response_model=list[schemas.CompanyResponse])
def read_company(db: Session = Depends(get_db)):
    """
    Read all company from the database
    """
    return crud_company.get_all_company(db)

@router.get("/{company_id}", response_model=schemas.CompanyResponse)
def get_company_id(company_id : int , db: Session = Depends(get_db)):
    company = get_company_by_id(db,company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.post("/createcompany/")
def createcompany(id: int, company_name: str, location: str, db: Session = Depends(get_db)):
    company= db.query(Company).filter(Company.id==id).first()
    if company:
        raise HTTPException(
            status_code=400,
            detail="Company already exist"
        )
    return create_company(db,id,company_name,location)



