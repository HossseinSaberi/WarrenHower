from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from proj_setting import settings
from sqlalchemy.orm import Session
from utils import check_user_exist_by_email
from fastapi import Depends
from Exceptions.jwtError import CredentialException
from .auth_schema import TokenData
from dependencies import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/Authenticate/token")
proj_secret_key = settings.jwt_secret_key
proj_algorythm = settings.jwt_algorithm

def verify_password(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)


def get_password_hashed(password):
    return pwd_context.hash(password)


def authenticate_user(email: str, password: str,db: Session):
    user = check_user_exist_by_email(db, email)
    hashed_pass = get_password_hashed(password)
    if not user:
        return False
    if not verify_password(password,hashed_pass):
        return False
    return user


def create_access_token(user_data: dict, expire_delta: timedelta = None):
    encode_user_data = user_data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode_user_data.update({"exp": expire})
    jwt_encode = jwt.encode(encode_user_data, proj_secret_key, algorithm=proj_algorythm)
    return jwt_encode


async def get_current_user(db: Session=Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, proj_secret_key, algorithms=[proj_algorythm])
        email: str = payload.get('sub')
        print(email)
        if email is None:
            raise  
        token_data = TokenData(email=email)
    except JWTError:
        raise CredentialException
    user =  check_user_exist_by_email(db, user_email=token_data.email)
    if user is None:
        raise CredentialException
    return user
