from typing import List

from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    company_id: int
    role_id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    company_id: int
    role_id: int

    class Config:
        from_attributes = True

class UserPaginationResponse(BaseModel):
    total: int
    page: int
    limit: int
    data: List[UserResponse]

    class Config:
        from_attributes = True