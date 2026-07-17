from sqlalchemy.orm import Session

from app.models.refresh_token import RefreshToken


def save_refresh_token(
    db: Session,
    user_id: str,
    token: str,
):

    obj = RefreshToken(
        user_id=user_id,
        token=token,
    )

    db.add(obj)

    db.commit()

    return obj


def get_refresh_token(
    db: Session,
    token: str,
):

    return (
        db.query(RefreshToken)
        .filter(
            RefreshToken.token == token
        )
        .first()
    )


def delete_refresh_token(
    db: Session,
    token: str,
):

    obj = get_refresh_token(
        db,
        token,
    )

    if obj:

        db.delete(obj)

        db.commit()