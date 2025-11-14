from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings (BaseSettings):
    API_v1_str: str = "/api/v1"
    # API_v2_str: str = "/api/v2"
    
    db_url: str = "mysql+asyncmy://root@127.0.0.1:3306/bandas"
    
    dbBaseModel = declarative_base()
    
class config:
    case_sensitive = False
    env_file = "env"
    
settings = Settings()