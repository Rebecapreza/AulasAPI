from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Ursinho Pooh API')
app.include_router(api_router, prefix=settings.api_v1_str)

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='info', reload=True)