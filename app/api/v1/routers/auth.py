from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.auth_service import create_new_user, UserAlreadyExistError
from app.schemas.auth import UserCreate
from app.core.database import get_db


router = APIRouter()


@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_new_user(db, user)
    except UserAlreadyExistError as e:
        raise HTTPException(status_code=409, detail=str(e))