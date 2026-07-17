import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(String(36), nullable=False)

    token = Column(String(500), unique=True)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )