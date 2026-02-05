from sqlalchemy.orm import Session
from app.models.user import User


def get_user_by_email(db: Session, email: str) -> User | None:
    return (
        db.query(User)
        .filter(User.user_email == email)
        .first()
    )


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )


def create_user(db: Session, user_email: str, hashed_password: str) -> User:
    new_user = User(
        user_email= user_email,
        hashed_password= hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user