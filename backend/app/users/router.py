from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from fastapi import Depends

from app.database.session import get_db

from app.schemas.user import UpdateProfile

from app.users.service import (
    get_user,
    update_profile,
)
from app.security.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.patch("/me")
def update_me(
    data: UpdateProfile,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    user = get_user(
        db,
        payload["sub"],
    )

    return update_profile(
        db,
        user,
        data,
    )
@router.get("/me")
def me(
    user=Depends(get_current_user),
):


    return user