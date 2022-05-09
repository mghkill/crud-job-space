from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass

@dataclass
class Leads(db.Model):
    
    id: int
    name: str
    email: str
    phone: str
    cep: str
    number: str
    placeLog: str
    complement: str
    district: str
    localityCity: str
    uf: str
    ibge: str
    gia: str
    ddd: str
    siafi: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "leads_user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    cep = Column(String, nullable=False)
    number = Column(String, nullable=False)
    placeLog = Column(String, nullable=False)
    complement = Column(String, nullable=False)
    district = Column(String, nullable=False)
    localityCity = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    ibge = Column(String, nullable=False)
    gia = Column(String, nullable=False)
    ddd = Column(String, nullable=False)
    siafi = Column(String, nullable=False)
    creation_date = Column(DateTime)
    last_visit = Column(DateTime)
    visits = Column(Integer, default=1)

