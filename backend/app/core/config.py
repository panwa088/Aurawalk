from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AuraWalk"

    SECRET_KEY: str = "CHANGE_THIS_SECRET"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = "postgresql://aurawalk:aurawalk@localhost:5432/aurawalk"

    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()