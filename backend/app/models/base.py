import uuid

from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

from app.database.base import Base


class BaseModel(Base):

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )