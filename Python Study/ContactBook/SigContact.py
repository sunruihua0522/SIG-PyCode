from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
class SigContact(declarative_base(())):
    __tablename__ = 'SigContact'
    id = Column(Integer,primary_key=True)
    firstName = Column(String(100))
    middleName = Column(String(100))
    lastName = Column(String(100))
    company = Column(String(100))
    department = Column(String(100))
    jobTitle = Column(String(100))
    city = Column(String(100))
    account = Column(String(50))
    businessPhone = Column(String(50))
    mobile = Column(String(30))
    email = Column(String(100))
