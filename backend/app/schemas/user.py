from pydantic import BaseModel


class UpdateProfile(BaseModel):

    display_name: str | None = None

    bio: str | None = None

    gender: str | None = None

    avatar: str | None = None