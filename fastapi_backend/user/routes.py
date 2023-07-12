from fastapi import APIRouter, Depends, HTTPException, status
from user.schema import User as UserSchema,UserOut
from db.session import get_session
from user.model import User
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import os

oauth_2_scheme=OAuth2PasswordBearer(tokenUrl='token')

#replace opensssl secret key
JWT_SECRET=os.getenv('JWT_SECRET')

user_route = APIRouter()

@user_route.post('/token')
async def get_token(form_data:OAuth2PasswordRequestForm=Depends(),session: Session = Depends(get_session)):
    """"""
    user=await authenticate_user(form_data.username,form_data.password,session)
    if not user:
        return {'error':'Invalid Credentials'}

    user_obj= UserSchema.as_dict(user)

    tkn = jwt.encode(user_obj,JWT_SECRET)

    return {'access_token':tkn,'token_type':'bearer'}

async def get_current_user(token:str=Depends(oauth_2_scheme)):
    try:
        user=jwt.decode(token,JWT_SECRET,algorithms=['HS256'])
        print(user)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password.'
        ) from exc

    return user

@user_route.get('/users')
async def fetch_users(session: Session = Depends(get_session)):
    data = session.query(User).all()
    return data

@user_route.get('/user/{username}',response_model=UserSchema)
async def get_user(username: str, session: Session = Depends(get_session)):
    return session.query(User).get(username)


@user_route.post('/register')
async def create_user(user: UserSchema, session: Session = Depends(get_session)):
    # implement email already exists
    item = User(email=user.email, password=bcrypt.hash(user.password), name=user.name,username=user.username)
    session.add(item)
    session.commit()
    session.refresh(item)
    return f'{item.name} user added successfully!'


@user_route.put('/user/{username}',response_model=UserOut)
async def update_user(username: str, user:UserSchema, session: Session = Depends(get_session)):
    item = session.query(User).get(username)
    # item=UserSchema.as_dict(item)
    item.name = user.name
    # implement email already exists
    item.email = user.email
    item.password = user.password
    session.commit()
    return item


@user_route.delete('/user/{id}')
async def delete_user(id: int, session: Session = Depends(get_session)):
    item = session.query(User).get(id)
    session.delete(item)
    session.commit()
    session.close()
    return 'Item was deleted.'

async def authenticate_user(username:str,password:str,session:Session):
    user=session.query(User).get(username)
    print(user)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


@user_route.get('/login',response_model=UserSchema)
async def do_login(user:UserSchema=Depends(get_current_user)):
    return user

