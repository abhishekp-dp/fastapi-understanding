from pydantic import BaseModel,validate_email

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True