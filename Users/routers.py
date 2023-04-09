from fastapi import APIRouter , Depends
from dependencies import get_db
from sqlalchemy.orm import Session
from typing import List
from .schemas import UserResponseList
from .crud import get_list_of_users

router = APIRouter()

@router.get('/Users' , response_model=List[UserResponseList])
def list_of_users(db:Session = Depends(get_db)):
    user_list = get_list_of_users(db)
    return user_list