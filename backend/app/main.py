from fastapi import FastAPI
from app.database.base import Base
from app.users.router import router as users_router
from app.database.session import engine
from app.models.refresh_token import RefreshToken
from app.models.friend import Friend
from app.models.block import BlockUser
from app.users.friend_router import router as friend_router

Base.metadata.create_all(bind=engine)

from app.auth.router import router as auth_router

app = FastAPI(
    title="AuraWalk API",
    version="0.2.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(friend_router)

@app.get("/")
def root():
    return {
        "project": "AuraWalk",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }