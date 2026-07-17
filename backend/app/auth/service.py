from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.auth import RegisterRequest

from app.security.password import hash_password

from app.services.user_service import get_by_email
from app.services.user_service import get_by_username
from app.services.user_service import create_user


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

    return create_user(db, user)