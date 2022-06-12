from typing import Literal, Optional
from pydantic import BaseModel, conint, constr


class CourseModel(BaseModel):
    name: constr(max_length=50)
    type: Literal["interpreted", "compiled"]
    description: constr(max_length=500)
    price: conint(lt=1000)


class CourseUpdateModel(BaseModel):
    description: Optional[constr(max_length=500)]
    price: Optional[conint(lt=1000)]
