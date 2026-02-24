from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Company(Base):
    __tablename__ = "Company"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), unique=True, index=True)