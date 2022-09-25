from sqlalchemy import select
from ..db.async_base import async_session
from ..models.category import Category


@async_session
async def async_fetch_categories(async_session):
    stmt = select(Category).filter()
    result = await async_session.execute(stmt)
    return result.scalars().all()
