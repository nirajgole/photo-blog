from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status,Response,Request,Security
from user.schema import User as UserSchema,UserOut,UserInDB,Token,TokenData,LogInUser
from db.session import get_session
from user.model import User
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm,SecurityScopes
from jose import JWTError, jwt
import os
from security.authSecurity import create_access_token
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from pydantic import ValidationError

oauth_2_scheme=OAuth2PasswordBearer(tokenUrl='login')

#replace opensssl secret key
JWT_SECRET=os.getenv('JWT_SECRET')
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
ALGORITHM = "HS256"
user_route = APIRouter()

# @user_route.post('/testing')
# async def fetch_users(user:UserInDB):
#     print(user.username,user.password)
#     return user.username


@user_route.post('/login',response_model=Token)
async def get_token(user:LogInUser,session:Session=Depends(get_session)):
    # username,password=UserSchema.as_dict(form_user)
    username,password=dict(user).values()
    print(username,password)

    user=await authenticate_user(username,password,session)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # user_obj= UserSchema.as_dict(user)

    # access_token = jwt.encode(user_obj,JWT_SECRET)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username},
        expires_delta=access_token_expires)
    print(access_token)
    # return {'access_token':access_token,'token_type':'bearer'}
    content={'message':'Logged in successfully.'}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    response=JSONResponse(content=content,headers=headers)
    cookie_params={
        'httponly':True,
        'secure':True,
        'samesite':'none'
    }
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", **cookie_params)
    return response

async def get_current_user(security_scopes: SecurityScopes,token:str=Depends(oauth_2_scheme),session:Session=Depends(get_session)):
    #check security scopes
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    #decode jwt token
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception

    #get user
    # user = get_user(fake_users_db, username=token_data.username)
    user = await session.query(User).get(username)
    if user is None:
        raise credentials_exception

    #check scopes
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value}
            )
    # try:
    #     user=jwt.decode(token,JWT_SECRET,algorithms=['HS256'])
    #     print(user)
    # except Exception as exc:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail='Invalid username or password.'
    #     ) from exc

    return user

# @user_route.post('/is_logged_in')
async def get_current_active_user(
    current_user:UserSchema=Security(get_current_user, scopes=["me"])
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@user_route.get('/users')
async def fetch_users(session: Session = Depends(get_session)):
    data = session.query(User).all()
    return data

@user_route.get('/user/me',response_model=UserSchema)
async def get_user(current_user: UserSchema=Depends(get_current_active_user)):
    return current_user


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


@user_route.delete('/user/{username}')
async def delete_user(username: str, session: Session = Depends(get_session)):
    item = session.query(User).get(username)
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


# @user_route.get('/login',response_model=UserSchema)
# async def do_login(user:UserSchema=Depends(get_current_user)):
#     return user

# @user_route.post("/cookie/")
# def create_cookie():
#     content = {"message": "Come to the dark side, we have cookies"}
#     response = JSONResponse(content=content)
#     cookie_params={
#         'httponly':True,
#         'secure':True,
#         'samesite':'lax'
#     }
#     response.set_cookie(key='token_name', value='token_value',**cookie_params )
#     return response

