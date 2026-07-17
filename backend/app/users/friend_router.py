from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.security.dependencies import get_current_user

from app.schemas.friend import (
    FriendAction,
    FriendRequest,
)

from app.services.friend_service import *

router = APIRouter(
    prefix="/friends",
    tags=["Friends"],
)


@router.post("/request")
def request_friend(
    data: FriendRequest,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    return send_request(
        db,
        payload["sub"],
        data.target_user_id,
    )


@router.post("/accept")
def accept(
    data: FriendAction,
    db: Session = Depends(get_db),
):

    return accept_request(
        db,
        data.request_id,
    )


@router.post("/reject")
def reject(
    data: FriendAction,
    db: Session = Depends(get_db),
):

    return reject_request(
        db,
        data.request_id,
    )


@router.get("/list")
def list_friend(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    return my_friends(
        db,
        payload["sub"],
    )