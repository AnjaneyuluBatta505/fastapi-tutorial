from curses import echo
import os

from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

db_url = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

async_engine = create_async_engine(db_url, echo=True)

AsyncLocalSession = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


@asynccontextmanager
async def get_async_session():
    session = AsyncLocalSession()
    try:
        yield session
    except Exception as e:
        print(e)
        await session.rollback()
    finally:
        await session.close()


def async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper
