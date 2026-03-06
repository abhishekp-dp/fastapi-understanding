from pydantic import BaseModel


class RolesCreate(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True