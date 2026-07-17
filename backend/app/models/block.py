from sqlalchemy.orm import Mapped

from app.models.base import BaseModel


class BlockUser(BaseModel):

    __tablename__ = "blocks"

    owner_id: Mapped[str]

    target_id: Mapped[str]