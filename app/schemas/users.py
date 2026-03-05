from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    company_id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    company_id: int

    class Config:
        from_attributes = True