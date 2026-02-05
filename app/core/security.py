from datetime import timedelta, timezone, datetime
from typing import Optional
from passlib.context import CryptContext
from app.core.config import ALGORITHM, SECRET_KEY, ACCESS_TIME
from jose import jwt, JWTError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_hash_pwd(password: str) -> str:
    return pwd_context.hash(password)


def verify_hash_pwd(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)


def create_access_token(subject: str, role: str, expire_delta: Optional[timedelta] = None) -> str:
    to_encode = {
        "sub" : subject,
        "role" : role,
    }
    expire = datetime.now(timezone.utc) + (expire_delta or timedelta(minutes=ACCESS_TIME))
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None