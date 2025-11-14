from core.configs import settings
from sqlalchemy import Column, Integer, String

class PersonagensModel (settings.dbBaseModel):
    __tablename__ = 'Personagens'
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    personalidade: str = Column(String(100))
    cor: str = Column(String(100))
    