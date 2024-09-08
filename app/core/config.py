from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MindMaple"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./mindmaple.db"

    class Config:
        env_file = ".env"

settings = Settings()
