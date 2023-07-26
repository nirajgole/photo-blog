"""schemas"""
from pydantic import BaseModel


class User(BaseModel):
    username:str
    name: str or None = None
    email: str or None = None
    password:str
    disabled:bool or None = None

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class UserInDB(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str