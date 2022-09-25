# async sqlalchemy queries

## pre-requisites

- **asyncio** module - https://docs.python.org/3/library/asyncio.html
  - asyncio is a library to write concurrent code using the async/await syntax.
  - asyncio is often a perfect fit for IO-bound and high-level structured network code.


- **asyncpg** - https://magicstack.github.io/asyncpg/current/
  - `pip install asyncpg`
- **greenlet** - https://greenlet.readthedocs.io/en/latest/
  - `pip install greenlet`


## steps

- update database url to support async

```
postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}
```

- create async database connection

```python
from sqlalchemy.ext.asyncio import create_async_engine

db_url = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(db_url, echo=True, future=True)
```

- create async session

```python
from sqlalchemy.orm import sessionmaker
LocalAsyncSession = sessionmaker(engine, class_=AsyncSession)
```

Use async session to query the database.
