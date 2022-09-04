from fastapi import APIRouter, HTTPException, Response

from ..schemas.category import CategoryModel, CategoryResponseModel
from ..services.category import create_category, get_category, update_category, delete_category
from ..queries.category import fetch_categories
from ..errors.base import AlreadyExistsError, NotFoundError


router = APIRouter()


@router.post('/categories', status_code=201, response_model=CategoryResponseModel)
def create_new_category(model: CategoryModel):
    try:
        pk = create_category(model)
        obj = get_category(pk)
        return obj
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/categories', status_code=200, response_model=list[CategoryResponseModel])
def list_categories():
    return fetch_categories()


@router.get('/categories/<pk>', status_code=200, response_model=CategoryResponseModel)
def get_category_by_id(pk: int):
    try:
        return get_category(pk)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put('/categories/<pk>', status_code=200, response_model=CategoryResponseModel)
def update_category_by_id(pk: int, model: CategoryModel):
    try:
        pk = update_category(pk, model)
        return get_category(pk)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/categories/<pk>', status_code=204)
def delete_category_by_id(pk: int):
    try:
        delete_category(pk)
        return Response('', status_code=204)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
