from app.crud.admin import change_role, all_non_admin
from sqlalchemy.orm import Session
from app.crud.user import get_user_by_email


class UserNotFoundError(Exception): pass


def toggle_user_role_service(db: Session, target_user_email: str):
    user = get_user_by_email(db, target_user_email)
    if not user: raise UserNotFoundError("User not found")

    if user.role == "user":
        new_role = "authority"
    else:
        new_role = "user"

    return change_role(db, target_user_email, new_role)


def get_all_non_admin_service(db: Session):
    return all_non_admin(db)