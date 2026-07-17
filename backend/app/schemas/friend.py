from pydantic import BaseModel


class FriendRequest(BaseModel):
    target_user_id: str


class FriendAction(BaseModel):
    request_id: str