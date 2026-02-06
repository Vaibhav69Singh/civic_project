from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    user_email: EmailStr
    password: str = Field(min_length=8, max_length=24)



class UserLogin(BaseModel):
    user_email: EmailStr
    password: str = Field(min_length=8, max_length=24)


class AuthResponse(BaseModel):
    user_id: int
    user_email: str
    access_token: str
    token_type: str

    class Config:
        from_attributes = True