from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , scoped_session
from functools import lru_cache
from proj_setting import settings

SQL_ALCHEMY_POSTGRES_ADDR = "postgresql://{}:{}@{}:{}/{}".format(settings.db_username , settings.db_password , settings.db_ip , settings.db_port , settings.db_name)
engine = create_engine(SQL_ALCHEMY_POSTGRES_ADDR)
Base = declarative_base()

@lru_cache
def create_session() -> scoped_session:
    SessionLocal = scoped_session(sessionmaker(autoflush=False , bind=engine))
    return SessionLocal


