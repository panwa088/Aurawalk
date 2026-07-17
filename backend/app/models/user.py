import uuid

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.sql import func

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    username = Column(String(50), unique=True, nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    display_name = Column(String(120))

    avatar = Column(String(255))

    status = Column(String(30), default="public")

    role = Column(String(30), default="member")

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())