from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Users import models


def check_item_exist(item, item_id):
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Item With id {item_id} Does Not Exists!')


def check_user_exists_by_id(db: Session, user_id, int):
    user_details = db.query(models.Users).filter(
        models.Users.uid == user_id).first()
    if user_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User With Id {user_id} Does Not Exists!')
    return user_details


def check_user_exist_by_email(db: Session, user_email: str):
    user = db.query(models.Users).filter(models.Users.email == user_email).first()
    print(user)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User With Email " {user_email} " Does Not Exists!')
    return user
