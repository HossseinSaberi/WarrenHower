from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .models import Users, Profile
from utils import check_item_exist , check_user_exists_by_id
from Authenticate import auth_utils


def get_list_of_users(db: Session):
    try:
        users_list = db.query(Users).all()
        return users_list
    except HTTPException as e:
        print(e)


def get_user_detail(user_id, db):
    user_details = db.query(Users).filter(Users.uid == user_id).join(
        Profile, Profile.user_id == Users.uid, isouter=True).first()
    check_item_exist(user_details, user_id)
    return user_details


def create_new_user(user_detail, db):
    hashed_pass = auth_utils.get_password_hashed(user_detail.password)
    user_detail.password = hashed_pass
    try:
        new_user = Users(**user_detail.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        return e


def update_user_detail(user_detail, db):
    hashed_pass = user_detail.password
    user_detail.password = hashed_pass
    oath_detail = auth_utils.get_current_user()
    user = check_user_exists_by_id(db, oath_detail.user_id)
    user.update(user_detail.dict(), synchronize_session=False)
    db.commit()
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,
                        detail=f'User With Id {oath_detail.user_id} , Was Updated!')
