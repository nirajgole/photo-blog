"""entrypoint"""
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from db.session import engine
from db.base import Base

from routers.user_routes import user

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    create_tables()
    return FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user)

FAVICON_PATH = './favicon.ico'
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """favicon"""
    return FileResponse(FAVICON_PATH)
