from sqlalchemy.orm import Session

from app.models.user import User


def get_user(
    db: Session,
    user_id: str,
):

    return (
        db.query(User)
        .filter(
            User.id == user_id,
            User.deleted == False,
        )
        .first()
    )


def update_profile(
    db: Session,
    user: User,
    data,
):

    payload = data.model_dump(
        exclude_none=True
    )

    for k, v in payload.items():

        setattr(user, k, v)

    db.commit()

    db.refresh(user)

    return user