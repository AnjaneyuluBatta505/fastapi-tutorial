from ..schemas.category import CategoryModel
from ..queries.category import insert_category, fetch_category_by_name, fetch_category_by_id, update_category_by_id, delete_category_by_id
from ..errors.base import NotFoundError, AlreadyExistsError, UpdateFailedError, DeleteFailedError


def create_category(model: CategoryModel):
    # validate category exists
    if fetch_category_by_name(model.name) is not None:
        raise Exception("Category is already exists")
    # create category
    pk = insert_category(model)
    return pk


def get_category(pk):
    obj = fetch_category_by_id(pk)
    if obj is None:
        raise NotFoundError(f'Category with id={pk} does not exist')
    return obj


def update_category(pk: int, model: CategoryModel):
    # pk exists or not in the database
    get_category(pk)
    # name already exists
    obj = fetch_category_by_name(model.name)
    if obj is not None and obj.id != pk:
        raise AlreadyExistsError(f'Category with name "{model.name}" already exist.')
    is_updated = update_category_by_id(pk, model)
    if not is_updated:
        raise UpdateFailedError('Failed to update the category')
    return pk


def delete_category(pk: int):
    get_category(pk)
    is_deleted = delete_category_by_id(pk)
    if not is_deleted:
        raise DeleteFailedError(f'Failed to delete category with id={pk}')
    return pk
