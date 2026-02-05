from app.crud.user import get_user_by_email, get_user_by_id, create_user
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate
from app.core.security import create_hash_pwd, create_access_token


class UserAlreadyExistError(Exception): pass


def get_user_using_email(db: Session, user_email: str):
    return get_user_by_email(db, user_email)

def get_user_using_id(db: Session, user_id: int):
    return get_user_by_id(db, user_id)


def create_new_user(db: Session, user: UserCreate):
    existing_user =get_user_by_email(db, user.user_email)
    if existing_user:
        raise UserAlreadyExistError("Email already used")

    hashed_pwd = create_hash_pwd(user.password)
    new_user = create_user(db, user.user_email, hashed_pwd)

    access_token = create_access_token(
        subject=str(new_user.user_id),
        role="user"
    )

    return {
        "user_id": new_user.user_id,
        "user_email": new_user.user_email,
        "token": access_token,
        "created_at": new_user.created_at
    }