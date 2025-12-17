from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "CareerFlow"
    DEBUG: bool = False

    DATABASE_URL: str = ""
    REDIS_URL: str = ""

    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRES_DAYS: int = 7

    TELEGRAM_BOT_TOKEN: str = ""
    OPENAI_API_KEY: str = ""

    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "https://localhost:8000"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
