from fastapi import APIRouter , Depends , HTTPException , status
from .auth_schema import Token
from sqlalchemy.orm import Session
from dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm
from .auth_utils import authenticate_user , create_access_token , get_password_hashed
from datetime import timedelta
from proj_setting import settings

router = APIRouter()
access_token_expire_mitunte = settings.jwt_access_token_expire_minutes

@router.post('/token' , response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends() , db:Session=Depends(get_db)):
    user = authenticate_user(form_data.username , form_data.password,db)
    print(user)
    if not user :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expire = timedelta(minutes=access_token_expire_mitunte)
    access_token = create_access_token(user_data={"sub":user.email} , expire_delta=access_token_expire)
    return {"access_token": access_token, "token_type": "bearer"}
