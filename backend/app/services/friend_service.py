from sqlalchemy.orm import Session

from app.models.friend import Friend


def send_request(
    db: Session,
    owner: str,
    target: str,
):

    exists = (
        db.query(Friend)
        .filter(
            Friend.requester_id == owner,
            Friend.receiver_id == target,
            Friend.deleted == False,
        )
        .first()
    )

    if exists:
        return exists

    obj = Friend(
        requester_id=owner,
        receiver_id=target,
        status="pending",
    )

    db.add(obj)

    db.commit()

    db.refresh(obj)

    return obj


def accept_request(
    db: Session,
    request_id: str,
):

    obj = (
        db.query(Friend)
        .filter(
            Friend.id == request_id,
            Friend.deleted == False,
        )
        .first()
    )

    if obj:

        obj.status = "accepted"

        db.commit()

        db.refresh(obj)

    return obj


def reject_request(
    db: Session,
    request_id: str,
):

    obj = (
        db.query(Friend)
        .filter(
            Friend.id == request_id,
            Friend.deleted == False,
        )
        .first()
    )

    if obj:

        obj.status = "rejected"

        db.commit()

        db.refresh(obj)

    return obj


def my_friends(
    db: Session,
    user_id: str,
):

    return (
        db.query(Friend)
        .filter(
            (
                (Friend.requester_id == user_id)
                |
                (Friend.receiver_id == user_id)
            ),
            Friend.status == "accepted",
            Friend.deleted == False,
        )
        .all()
    )