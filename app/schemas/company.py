from tokenize import String

from pydantic import BaseModel
from app.schemas.users import UserResponse

class CompanyResponse(BaseModel):
    id : int
    company_name : str
    location : str


    class Config:
        from_attributes = True

class CompanyCreate(BaseModel):
    id : int
    company_name: str
    location : str

    class Config:
        from_attributes = True

class CompanyUsersResponse(BaseModel):
    total_users : int
    users : list[UserResponse]

    class Config:
        from_attributes = True