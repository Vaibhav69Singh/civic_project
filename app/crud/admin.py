from sqlalchemy.orm import Session
from app.models.user import User

def change_role(db: Session, user_email: str, role: str):
    user_data = db.query(User).filter(User.user_email == user_email).first()
    if not user_data: return None

    user_data.role = role
    db.commit()
    db.refresh(user_data)
    return user_data

def all_non_admin(db: Session):
    return (
        db.query(User)
        .filter(User.role != 'admin')
        .all()
    )