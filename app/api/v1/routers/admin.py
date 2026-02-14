from fastapi import APIRouter, HTTPException, Depends
from app.schemas.admin import ToggleResponse, UserListResponse
from app.core.database import get_db
from app.services.admin_service import toggle_user_role_service, get_all_non_admin_service
from sqlalchemy.orm import Session
from app.utils.helper_functions import admin_check



router = APIRouter(tags=["Admin"], dependencies=[Depends(admin_check)])


@router.patch("/toggle_role", response_model=ToggleResponse)
async def toggle_role_route(target_email: str, db: Session = Depends(get_db)):
    try:
        return toggle_user_role_service(db, target_email)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"{str(e)}")


@router.get("/non_admin_accounts", response_model=list[UserListResponse])
async def get_all_non_admin_accounts(db: Session = Depends(get_db)):
    try:
        return get_all_non_admin_service(db)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"{str(e)}")