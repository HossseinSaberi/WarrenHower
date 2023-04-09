from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from .models import Users

def get_list_of_users(db : Session):
    try:
        users_list = db.query(Users).all()
        return users_list
    except HTTPException as e:
        print(e)
        