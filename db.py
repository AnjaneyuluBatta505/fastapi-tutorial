db_courses = [
    {
        "name": "python",
        "type": "interpreted",
        "description": "Python is a high-level, interpreted programming language",
        "price": 500,
    },
    {
        "name": "go",
        "type": "compiled",
        "description": "Go is a statically typed, compiled programming language",
        "price": 800,
    },
    {
        "name": "javascript",
        "type": "interpreted",
        "description": "JavaScript, is a programming language that is one of the core technologies of the World Wide Web",
        "price": 300,
    },
    {
        "name": "java",
        "type": "compiled",
        "description": "Java is a high-level, class-based, object-oriented programming language",
        "price": 100,
    },
]


def get_db_course(course_name):
    course = list(filter(lambda course: course.get("name") == course_name, db_courses))
    if course:
        return course[0]
    return None
