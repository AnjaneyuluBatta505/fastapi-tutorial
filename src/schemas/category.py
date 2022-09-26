from pydantic import BaseModel, constr


class CategoryModel(BaseModel):
    name: constr(min_length=1, max_length=30)
    description: constr(min_length=1, max_length=255)


class CategoryResponseModel(CategoryModel):
    id: int

    class Config:
        orm_mode = True
