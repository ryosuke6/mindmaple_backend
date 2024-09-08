from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from typing import Generator

# データベースエンジンの作成
def create_db_engine(db_url: str):
    return create_engine(db_url, pool_pre_ping=True)

# セッションファクトリの作成
def create_session_factory(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベースエンジンとセッションファクトリの初期化
engine = create_db_engine(settings.DATABASE_URL)
DatabaseSession = create_session_factory(engine)

# モデルの基底クラス
Base = declarative_base()

# データベースセッションの依存性
def get_db() -> Generator:
    db = DatabaseSession()
    try:
        yield db
    finally:
        db.close()
