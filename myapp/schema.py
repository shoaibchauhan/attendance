from typing import Optional
from pydantic import BaseModel


class DepartmentSchema(BaseModel):
    department_name: str
    submitted_by: str

    class Config:
        orm_mode = True

class StudentSchema(BaseModel):
    full_name: str
    department_id: int
    class_name: str
    submitted_by: str

    class Config:
        orm_mode = True

class CourseSchema(BaseModel):
    course_name: str
    department_id: int
    semester: str
    class_name: str
    lecture_hours: int
    submitted_by: str

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    type: str
    full_name: str
    username: str
    email: str
    submitted_by: str

    class Config:
        orm_mode = True

class AttendanceLogSchema(BaseModel):
    student_id: int
    course_id: int
    present: bool
    submitted_by_id: int

    class Config:
        orm_mode = True