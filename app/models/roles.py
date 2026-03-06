from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)