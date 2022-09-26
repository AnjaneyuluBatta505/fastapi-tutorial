from sqlalchemy import insert, select, update, delete
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
    print(stmt)
    result = session.execute(stmt)
    return result.scalars().one_or_none()


@session
def fetch_categories(session):
    stmt = select(Category).filter()
    print(stmt)
    result = session.execute(stmt)
    return result.scalars().all()


@session
def update_category_by_id(session, pk: int, model: CategoryModel):
    stmt = update(Category).where(Category.id == pk).values(**model.dict())
    result = session.execute(stmt)
    is_updated = result.rowcount > 0
    if is_updated:
        session.commit()
    return is_updated


@session
def delete_category_by_id(session, pk: int):
    stmt = delete(Category).where(Category.id == pk)
    print(stmt)
    result = session.execute(stmt)
    is_deleted = result.rowcount > 0
    if is_deleted:
        session.commit()
    return is_deleted
