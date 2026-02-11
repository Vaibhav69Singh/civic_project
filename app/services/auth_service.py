from app.crud.user import get_user_by_email, get_user_by_id, create_user
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate
from app.core.security import create_hash_pwd, verify_hash_pwd
from app.utils.helper_functions import build_auth_response


#************************ Helper Exception classes ************************

class UserAlreadyExistError(Exception): pass
class UserDoesNotExistError(Exception): pass
class WrongPasswordError(Exception): pass


#************************ Helper functions ************************

def get_user_by_email_service(db: Session, user_email: str):
    return get_user_by_email(db, user_email)

def get_user_by_id_service(db: Session, user_id: int):
    return get_user_by_id(db, user_id)


#************************ Main Auth functions ************************

def create_new_user(db: Session, user: UserCreate):
    existing_user =get_user_by_email(db, user.user_email)
    if existing_user:
        raise UserAlreadyExistError("Email already used")

    hashed_pwd = create_hash_pwd(user.password)
    new_user = create_user(db, user.user_email, hashed_pwd)

    return build_auth_response(new_user)

def login_user_service(db: Session, user_email: str, password: str):
    existing_user = get_user_by_email_service(db, user_email)
    if not existing_user:
        raise UserDoesNotExistError("No user with this email")

    if not verify_hash_pwd(plain_pwd=password, hashed_pwd= existing_user.hashed_password):
        raise WrongPasswordError("Password does not match")

    return build_auth_response(existing_user)