from pydantic import BaseModel
from pydantic import EmailStr


class UserResponse(BaseModel):

    id: str

    username: str

    email: EmailStr

    display_name: str | None = None

    avatar: str | None = None

    role: str

    status: str

    class Config:
        from_attributes = True