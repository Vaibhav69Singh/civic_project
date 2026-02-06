from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.auth_service import (create_new_user,
                                       UserAlreadyExistError,
                                       UserDoesNotExistError,
                                       login_user_service,
                                       WrongPasswordError)
from app.schemas.auth import UserCreate, UserLogin, AuthResponse
from app.core.database import get_db


router = APIRouter()


@router.post("/register", response_model=AuthResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_new_user(db, user)
    except UserAlreadyExistError as e:
        raise HTTPException(status_code=409, detail=str(e))



@router.post("/login", response_model=AuthResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    try:
        return login_user_service(db, user.user_email, user.password)
    except UserDoesNotExistError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except WrongPasswordError as e:
        raise HTTPException(status_code=409, detail=str(e))
