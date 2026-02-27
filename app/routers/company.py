from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db  # your DB session function under database
from fastapi import APIRouter

from app.crud import company as crud_company
from app.schemas import company as schemas
from app.database import get_db  # your DB session function under database
from app.crud.company import get_all_company

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
