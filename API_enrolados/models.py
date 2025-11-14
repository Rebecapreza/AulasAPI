from typing import Optional
from pydantic import BaseModel

class personagensEnrolados(BaseModel):
    nome: str
    personalidade: str
    foto: str
    
class personagemEnrolados(personagensEnrolados):
    pass 

class personagem(personagensEnrolados):
    id:int