import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

db_url = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(db_url)

LocalSession = sessionmaker(bind=engine)


@contextmanager
def get_session():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()


def session(func):
    def wrapper(*args, **kwargs):
        with get_session() as session:
            return func(session, *args, **kwargs)
    return wrapper
