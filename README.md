# FastAPI Student CRUD API

This is a simple CRUD API built using FastAPI for managing student data.

## Features
- Create Student
- Get All Students
- Get Student by ID
- Update Student
- Delete Student

## Tech Stack
- Python
- FastAPI
- Uvicorn

## Installation

Clone the repository

git clone https://github.com/Ruchi-novadule/fastapi-student-crud-api.git

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn main:app --reload

## API Endpoints

GET /students -> Get all students  
GET /students/{id} -> Get student by ID  
POST /students -> Create new student  
PUT /students/{id} -> Update student  
DELETE /students/{id} -> Delete student

## API Testing

You can test the API using Swagger UI.

http://127.0.0.1:8000/docs