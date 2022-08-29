from fastapi import APIRouter, HTTPException
from ..schemas.category import CategoryModel, CategoryResponseModel
from ..services.category import create_category, get_category

router = APIRouter()


@router.post('/categories', status_code=201, response_model=CategoryResponseModel)
def create_new_category(model: CategoryModel):
    try:
        pk = create_category(model)
        obj = get_category(pk)
        return obj
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
