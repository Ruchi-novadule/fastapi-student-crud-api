from fastapi import FastAPI

app = FastAPI()

# Dummy database
students = {
    1: {"name": "Ruchi", "course": "BCA"},
    2: {"name": "Aman", "course": "B.Tech"}
}

# GET - all students
@app.get("/students")
def get_students():
    return students

# GET - single student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    return {"error": "Student not found"}

# POST - add student
@app.post("/students")
def add_student(student_id: int, name: str, course: str):
    students[student_id] = {"name": name, "course": course}
    return {"message": "Student added successfully"}

# PUT - update student
@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, course: str):
    if student_id in students:
        students[student_id] = {"name": name, "course": course}
        return {"message": "Student updated"}
    return {"error": "Student not found"}

# DELETE - delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted"}
    return {"error": "Student not found"}