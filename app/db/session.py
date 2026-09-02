from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine_async=create_async_engine(url=settings.SQLALCHEMY_DATABASE_URI_ASYNC)
session_async=async_sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    bind=engine_async,
    autocommit=False
)


engine=create_engine(url=settings.SQLALCHEMY_DATABASE_URI)
session=sessionmaker(    
    autoflush=False,
    expire_on_commit=False,
    bind=engine_async,
)
