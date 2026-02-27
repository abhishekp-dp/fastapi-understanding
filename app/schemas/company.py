from tokenize import String

from pydantic import BaseModel

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