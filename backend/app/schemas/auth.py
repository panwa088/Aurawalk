from pydantic import BaseModel
from pydantic import EmailStr


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    
class RefreshRequest(BaseModel):

    refresh_token: str    