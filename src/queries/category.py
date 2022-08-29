from sqlalchemy import insert, select
from ..db.base import session
from ..schemas.category import CategoryModel
from ..models.category import Category


@session
def insert_category(session, model: CategoryModel):
    stmt = insert(Category).values(**model.dict())
    result = session.execute(stmt)
    session.commit()
    (pk,) = result.inserted_primary_key
    return pk


@session
def fetch_category_by_name(session, name):
    stmt = select(Category).where(Category.name == name)
    result = session.execute(stmt)
    return result.scalars().one_or_none()


@session
def fetch_category_by_id(session, pk):
    stmt = select(Category).where(Category.id == pk)
    result = session.execute(stmt)
    return result.scalars().one_or_none()
