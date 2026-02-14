from pydantic import BaseModel, EmailStr
from datetime import datetime

class ToggleResponse(BaseModel):
    user_email: EmailStr
    role: str

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    user_email: str
    role: str
    created_at: datetime
    is_active: bool
    is_verified: bool

    class Config:
        from_attributes= True