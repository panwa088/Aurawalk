from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.auth import RegisterRequest

from app.auth.service import register
from app.schemas.auth import LoginRequest
from app.auth.service import login

from app.schemas.auth import RefreshRequest

from app.security.jwt import decode_token

from app.services.token_service import (
    get_refresh_token,
)

from app.security.jwt import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register_api(
    data: RegisterRequest,
    db: Session = Depends(get_db),
):

    try:

        user = register(db, data)

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

@router.post("/login")

def login_api(
    data: LoginRequest,
    db: Session = Depends(get_db),
):

    token = login(
        db,
        data.username,
        data.password,
    )

    if token is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )
@router.post("/refresh")
def refresh(
    data: RefreshRequest,
    db: Session = Depends(get_db),
):

    db_token = get_refresh_token(
        db,
        data.refresh_token,
    )

    if db_token is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token",
        )

    payload = decode_token(
        data.refresh_token
    )

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Token expired",
        )

    access = create_access_token(
        payload["sub"],
        "",
    )

    return {
        "access_token": access,
    }

    return token