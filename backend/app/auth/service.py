from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.auth import RegisterRequest

from app.security.password import hash_password

from app.services.user_service import get_by_email
from app.services.user_service import get_by_username
from app.services.user_service import create_user

from app.security.password import verify_password
from app.security.jwt import create_access_token

from app.security.jwt import create_refresh_token

from app.services.token_service import save_refresh_token

def register(db: Session, data: RegisterRequest):

    if get_by_username(db, data.username):
        raise Exception("Username already exists")

    if get_by_email(db, data.email):
        raise Exception("Email already exists")

    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        display_name=data.username,
    )

def login(db: Session, username: str, password: str):

    user = get_by_username(db, username)

    if user is None:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token(
        user.id,
        user.username,
    )

    refresh = create_refresh_token(
    user.id
    )

    save_refresh_token(
        db,
        user.id,
        refresh,
    )

    return {
        "access_token": token,
        "refresh_token": refresh,
        "token_type": "bearer",
    }

    return create_user(db, user)