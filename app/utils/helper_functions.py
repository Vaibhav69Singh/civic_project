from fastapi import Depends, HTTPException, status
from app.core.security import create_access_token
from app.core.security import decode_token
from fastapi.security import OAuth2PasswordBearer



def build_auth_response(user):
    return {
        "user_id": user.user_id,
        "user_email": user.user_email,
        "role": user.role,
        "access_token": create_access_token(
            subject=str(user.user_id),
            role=user.role
        ),
        "token_type": "bearer"
    }

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def admin_check(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
       raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token"
        )

    role = payload.get("role")
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin permission required"
        )
    return True