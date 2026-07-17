from fastapi import FastAPI
from app.database.base import Base

from app.database.session import engine

Base.metadata.create_all(bind=engine)

from app.auth.router import router as auth_router

app = FastAPI(
    title="AuraWalk API",
    version="0.2.0",
)

app.include_router(auth_router)


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