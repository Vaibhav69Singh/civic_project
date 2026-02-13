from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_service import (create_new_user,
                                       UserAlreadyExistError,
                                       UserDoesNotExistError,
                                       login_user_service,
                                       WrongPasswordError)
from app.schemas.auth import UserCreate, AuthResponse
from app.core.database import get_db


router = APIRouter()


@router.post("/register", response_model=AuthResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_new_user(db, user)
    except UserAlreadyExistError as e:
        raise HTTPException(status_code=409, detail=str(e))



@router.post("/login", response_model=AuthResponse)
async def login_user(form_data : OAuth2PasswordRequestForm = Depends(),
                     db: Session = Depends(get_db)
                     ):
    try:

        # here form_data.username is just the user_email
        # To make the login OAuth correct we added this feature
        return login_user_service(db, form_data.username, form_data.password)

    except (UserDoesNotExistError, WrongPasswordError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )