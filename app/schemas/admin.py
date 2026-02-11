from pydantic import BaseModel, EmailStr


class ToggleResponse(BaseModel):
    user_email: EmailStr
    role: str

    class Config:
        from_attributes = True