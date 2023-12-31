from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from db.session import engine
from db.base import Base
from db.config import settings


SQLALCHEMY_DATABASE_URL = settings.DB_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def create_tables():
    """create database tables"""
    Base.metadata.create_all(bind=engine)
