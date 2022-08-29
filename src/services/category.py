from ..schemas.category import CategoryModel
from ..queries.category import insert_category, fetch_category_by_name, fetch_category_by_id


def create_category(model: CategoryModel):
    # validate category exists
    if fetch_category_by_name(model.name) is not None:
        raise Exception("Category is already exists")
    # create category
    pk = insert_category(model)
    return pk


def get_category(pk):
    return fetch_category_by_id(pk)