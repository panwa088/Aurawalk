from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from app.security.jwt import decode_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
):

    payload = decode_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token",
        )

    return payload