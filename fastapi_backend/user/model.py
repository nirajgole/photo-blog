"""users"""
from db.base_class import Base
from sqlalchemy import Column, Integer, String # pylint: disable=import-error
from passlib.hash import bcrypt

class User(Base):
    """user"""
    __tablename__ = 'users'
    # id = Column(Integer, primary_key=True)
    username=Column(String(255),primary_key=True)
    name = Column(String(255))
    email = Column(String(255),unique=True)
    password = Column(String(255))
    disabled=0

    def verify_password(self,pwd):
        return bcrypt.verify(pwd,self.password)



