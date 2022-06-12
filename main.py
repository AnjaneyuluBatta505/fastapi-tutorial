from fastapi import FastAPI, Query, Path, HTTPException, Response
from schemas import CourseModel, CourseUpdateModel
from db import get_db_course, db_courses

app = FastAPI()


@app.get("/courses")
def list_courses(
    min_price: int = Query(None, description="minimum price"),
    max_price: int = Query(None, description="maximum price price"),
):
    courses = [*db_courses]

    if min_price is not None:
        courses = filter(lambda course: course.get("price") >= min_price, courses)

    if max_price is not None:
        courses = filter(lambda course: course.get("price") <= max_price, courses)

    return {"data": list(courses)}


@app.get("/courses/{course_name}")
def get_course(course_name: str = Path(description="Name of the course")):
    course = get_db_course(course_name)
    if not course:
        raise HTTPException(status_code=404, detail="not found")
    return course


@app.post("/courses", status_code=201)
def create_course(model: CourseModel):
    course = model.dict()
    # add to database
    db_courses.append(course)
    return course


@app.put("/courses/{course_name}", status_code=200)
def update_course(course_name, model: CourseUpdateModel):
    course = get_db_course(course_name)
    if not course:
        raise HTTPException(status_code=404, detail="not found")
    if model.description is not None:
        course["description"] = model.description
    if model.price is not None:
        course["price"] = model.price
    return course


@app.delete("/courses/{course_name}", status_code=204, response_class=Response)
def delete_course(course_name):
    course = get_db_course(course_name)
    if not course:
        raise HTTPException(status_code=404, detail="not found")
    course_index = db_courses.index(course)
    db_courses.pop(course_index)
    return None
