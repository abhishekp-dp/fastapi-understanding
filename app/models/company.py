from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(100), nullable=False)
    location = Column(String(100), unique=True, index=True)