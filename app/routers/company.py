from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db  # your DB session function under database
from fastapi import APIRouter

from app.crud import company as crud_company
from app.schemas import company as schemas
from app.database import get_db  # your DB session function under database
from app.crud.company import get_all_company, get_company_by_id, create_company, delete_company, crud_get_users_by_company
from app.models import Company,User
from app.schemas.company import CompanyCreate
from app.dependencies.auth_dependency import get_current_user

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

@router.get("/", response_model=schemas.CompanyPaginationResponse)
def read_company(page: int=1,limit: int=10,sort_by: str="id",order:str="asc" ,db: Session = Depends(get_db)):
    """
    Read all company from the database
    """
    companies, total = crud_company.get_all_company(db,page,limit,sort_by,order)
    return {
        "page": page,
        "limit": limit,
        "data": companies,
        "total": total

    }

@router.get("/{company_id}", response_model=schemas.CompanyResponse)
def get_company_id(company_id : int , db: Session = Depends(get_db)):
    company = get_company_by_id(db,company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.post("/createcompany/")
def createcompany(company: CompanyCreate, db: Session = Depends(get_db),current_user=Depends(get_current_user)):

    if current_user["role_id"] != 2:
        raise HTTPException(status_code=403, detail="Only Admin can Create Company")

    existing_company= db.query(Company).filter(Company.company_name==company.company_name, Company.location==company.location).first()
    if existing_company:
        raise HTTPException(
            status_code=400,
            detail="Company already exist at provided location"
        )
    return create_company(db,company)


@router.delete("/{company_id}/")
def deletecompany(company_id: int,db: Session = Depends(get_db),current_user=Depends(get_current_user)):

    if current_user["role_id"] != 2:
        raise HTTPException(status_code=403, detail="Only Admin can Delete Company")

    company_exist = db.query(Company).filter(Company.id == company_id).first()
    if not company_exist:
        raise HTTPException(status_code=404, detail="Company doesn't exist")

    user_exist = db.query(User).filter(User.company_id == company_id).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="User already exists")

    delete_company(db, company_id)
    return {"Company Deleted Successfully"}

@router.get("/{company_id}/users/", response_model=schemas.CompanyUsersResponse)
def get_users_by_company(company_id : int , db: Session = Depends(get_db)):
    company = get_company_by_id(db,company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    company_users = crud_get_users_by_company(db,company.id)
    return {
        "total_users": len(company_users),
        "users": company_users
    }


