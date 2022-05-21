from fastapi import FastAPI, Query, Path

app = FastAPI()


db_courses = [
    {
        "name": "python",
        "type": "interpreted",
        "description": "Python is a high-level, interpreted programming language",
        "price": 500
    },
    {
        "name": "go",
        "type": "compiled",
        "description": "Go is a statically typed, compiled programming language",
        "price": 800
    },
    {
        "name": "javascript",
        "type": "interpreted",
        "description": "JavaScript, is a programming language that is one of the core technologies of the World Wide Web",
        "price": 300
    },
    {
        "name": "java",
        "type": "compiled",
        "description": "Java is a high-level, class-based, object-oriented programming language",
        "price": 100
    },
]


@app.get('/courses')
def list_courses(
    min_price: int = Query(None, description="minimum price"),
    max_price: int = Query(None, description="maximum price price")
):
    courses = [*db_courses]

    if(min_price is not None):
        courses = filter(lambda course: course.get("price") >= min_price, courses)

    if(max_price is not None):
        courses = filter(lambda course: course.get("price") <= max_price, courses)

    return {"data": list(courses)}


@app.get('/courses/{course_name}')
def get_course(course_name: str = Path(description="Name of the course")):
    courses = list(filter(lambda course: course.get("name") == course_name, db_courses))
    course = None
    if(len(courses) > 0):
        course = courses[0]
    else:
        course = {'404': 'Not found'}
    return course
