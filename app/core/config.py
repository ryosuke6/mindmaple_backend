from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MindMaple"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
