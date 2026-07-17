from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Friend(BaseModel):

    __tablename__ = "friends"

    requester_id: Mapped[str]

    receiver_id: Mapped[str]

    status: Mapped[str] = mapped_column(
        default="pending"
    )