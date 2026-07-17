from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class User(BaseModel):

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)

    email: Mapped[str] = mapped_column(unique=True)

    password: Mapped[str]

    display_name: Mapped[str]

    avatar: Mapped[str | None]

    bio: Mapped[str | None]

    gender: Mapped[str | None]

    role: Mapped[str] = mapped_column(default="member")

    status: Mapped[str] = mapped_column(default="public")

    is_active: Mapped[bool] = mapped_column(default=True)