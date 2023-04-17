from fastapi import APIRouter, Depends, status
from dependencies import get_db
from sqlalchemy.orm import Session
from typing import List
from .schemas import UserResponseList, UserDetails, ProfileResponse, UserCreation , UserEdition
from .crud import get_list_of_users, get_user_detail, create_new_user , update_user_detail
from Authenticate import auth_utils
from jose import JWTError
from Exceptions import jwtError
router = APIRouter()


@router.get('/', response_model=List[UserResponseList])
def list_of_users(db: Session = Depends(get_db) , token: str=Depends(auth_utils.oauth2_scheme)):
    try:
        user_list = get_list_of_users(db)
        return user_list
    except JWTError :
        raise jwtError.CredentialException


@router.post('/',  status_code=status.HTTP_201_CREATED, response_model=UserResponseList)
def user_creation(user_detail: UserCreation, db: Session=(Depends(get_db)) , token: str=Depends(auth_utils.oauth2_scheme)):
    user_creation_resp = create_new_user(user_detail, db)
    return user_creation_resp


@router.get('/{user_id}', response_model=UserDetails)
def user_details(user_id: int, db: Session = Depends(get_db), token: str=Depends(auth_utils.oauth2_scheme)):
    user_detail = get_user_detail(user_id, db)
    return user_detail

@router.put('/{user_id}', response_model=UserDetails)
def user_details(user_detail : UserEdition , db: Session = Depends(get_db), token: str=Depends(auth_utils.oauth2_scheme)):
    user_detail = update_user_detail(user_detail, db)
    return user_detail

@router.delete('/{user_id}', response_model=None)
def user_details(user_id: int, db: Session = Depends(get_db), token: str=Depends(auth_utils.oauth2_scheme)):
    user_detail = get_user_detail(user_id, db)
    return user_detail

