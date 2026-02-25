from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True