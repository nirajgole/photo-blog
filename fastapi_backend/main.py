"""entrypoint"""
from fastapi import FastAPI,APIRouter, Depends,HTTPException,status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from config import settings
from db.session import create_tables

from user.routes import user_route

# from routers.user_routes import user

# SECRET_KEY=''
# ALGORITHM='HS256'
# ACCESS_TOKEN_EXPIRE_MINUTES= 30


def start_application():
    create_tables()
    return FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://127.0.0.1:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_route)

FAVICON_PATH = './favicon.ico'
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """favicon"""
    return FileResponse(FAVICON_PATH)


# oauth_2_scheme=OAuth2PasswordBearer(tokenUrl='token')



# @app.get('/')
# async def index(token:str=Depends(oauth_2_scheme)):
#     return {'the_token':token}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)