from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    user_email: EmailStr
    password: str = Field(min_length=8, max_length=24)

class UserCreateResponse(BaseModel):
    user_id: int
    user_email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True