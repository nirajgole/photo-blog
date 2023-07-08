"""users"""
from db.base_class import Base
from sqlalchemy import Column, Integer, String # pylint: disable=import-error

class User(Base):
    """user"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255),unique=True)
    password = Column(String(255))