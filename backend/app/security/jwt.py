from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from app.core.config import settings

ALGORITHM = "HS256"


def create_access_token(user_id: str, username: str):

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": user_id,
        "username": username,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )

def create_refresh_token(user_id: str):

    expire = datetime.now(timezone.utc) + timedelta(days=30)

    payload = {
        "sub": user_id,
        "type": "refresh",
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )

def decode_token(token: str):

    try:

        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM],
        )

    except JWTError:

        return None