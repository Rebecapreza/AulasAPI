from typing import Optional
from pydantic import BaseModel as SCBaseModel

class PersonagensSchemas(SCBaseModel):
    id: Optional[int] = None
    nome: str
    personalidade: str
    cor: str
    
    class Config:
        orm_mode = True