from sqlalchemy import Column, Integer, String, Date
from database import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    district = Column(String, nullable=False)
    mob = Column(String, nullable=False)
