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

# class UserInDB(User):
#     hashed_password: str