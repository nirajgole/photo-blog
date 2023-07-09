from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi_backend.schemas.user import UserInDB

# pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth_2_scheme=OAuth2PasswordBearer(tokenUrl='token')



# def verify_password(plain_password,hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db,username:str):
#     if username in db:
#         user_data=db['username']
#         return UserInDB(**user_data)

# def authenticate_user(db,username:str,password:str):
#     user=get_user(db,username)
#     if not user:
#         return False
#     if not verify_password(password,user.hashed_password):
#         return False
#     return user

# def create_access_token(data:dict,expires_delta:timedelta or None=None):
#     to_encode=data.copy()