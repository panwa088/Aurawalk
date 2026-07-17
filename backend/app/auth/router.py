from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.auth import RegisterRequest

from app.auth.service import register

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