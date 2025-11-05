from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()




# A7
class Greetings(BaseModel):
    hello: str

class GradeEntry(BaseModel):
    name: str
    course: str
    grade: float
    date: datetime

fake_db: list[GradeEntry] = [
    GradeEntry(name="Alice", course="Math", grade=1.7, date=datetime(2024, 4, 10)),
    GradeEntry(name="Bob", course="Physics", grade=2.3, date=datetime(2024, 4, 12)),
    GradeEntry(name="Charlie", course="Physics", grade=1.3, date=datetime(2024, 4, 15)),
    GradeEntry(name="Bob", course="Math", grade=2.0, date=datetime(2024, 4, 18)),
    GradeEntry(name="Alice", course="Physics", grade=1.0, date=datetime(2024, 4, 20)),
]

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello, World!"}

@app.get("/hello")
def hello(hello):
    return Greetings(hello=hello)

@app.get("/grades")
def read_grades():
    return fake_db

@app.get("/students")
def read_students() -> set[str]:
    return set([i.name for i in fake_db])

@app.get("/courses")
def read_courses() -> set[str]:
    return set([i.course for i in fake_db])

@app.get("/students/{name}")
def read_grades_of_student(name: str):
        return [i for i in fake_db if i.name == name]


@app.get("/courses/{name}")
def read_grades_of_course(name: str):
        return [i for i in fake_db if i.course == name]