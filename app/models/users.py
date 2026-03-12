from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
