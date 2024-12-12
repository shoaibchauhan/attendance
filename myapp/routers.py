from typing import List
from fastapi import APIRouter, HTTPException
from myapp.models import AttendanceLog, Course, Department, Student, User
from myapp.schema import AttendanceLogSchema, CourseSchema, DepartmentSchema, StudentSchema, UserSchema

router = APIRouter()

# Department Endpoints
@router.get("/departments", response_model=List[DepartmentSchema])
def list_departments():
    departments = Department.objects.all()  # Django ORM: Use .all()
    return list(departments)

@router.post("/departments", response_model=DepartmentSchema)
def create_department(department: DepartmentSchema):
    try:
        new_department = Department.objects.create(
            department_name=department.department_name,
            submitted_by=department.submitted_by
        )
        return new_department
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating department: {e}")

@router.put("/departments/{department_id}", response_model=DepartmentSchema)
def update_department(department_id: int, department: DepartmentSchema):
    try:
        existing_department = Department.objects.get(id=department_id)  # Django ORM: Use .get() for retrieving by id
        existing_department.department_name = department.department_name
        existing_department.submitted_by = department.submitted_by
        existing_department.save()  # Save changes
        return existing_department
    except Department.DoesNotExist:
        raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating department: {e}")

# Student Endpoints
@router.get("/students", response_model=List[StudentSchema])
def list_students():
    students = Student.objects.all()  # Django ORM: Use .all()
    return list(students)

@router.post("/students", response_model=StudentSchema)
def create_student(student: StudentSchema):
    try:
        department = Department.objects.get(id=student.department_id)  # Get related department by id
        new_student = Student.objects.create(
            full_name=student.full_name,
            department=department,
            class_name=student.class_name,
            submitted_by=student.submitted_by
        )
        return new_student
    except Department.DoesNotExist:
        raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating student: {e}")

@router.put("/students/{student_id}", response_model=StudentSchema)
def update_student(student_id: int, student: StudentSchema):
    try:
        existing_student = Student.objects.get(id=student_id)  # Retrieve student by id
        department = Department.objects.get(id=student.department_id)  # Get department by id
        existing_student.full_name = student.full_name
        existing_student.department = department
        existing_student.class_name = student.class_name
        existing_student.submitted_by = student.submitted_by
        existing_student.save()  # Save the updated student
        return existing_student
    except Student.DoesNotExist:
        raise HTTPException(status_code=404, detail="Student not found")
    except Department.DoesNotExist:
        raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating student: {e}")

# Course Endpoints
@router.get("/courses", response_model=List[CourseSchema])
def list_courses():
    courses = Course.objects.all()  # Django ORM: Use .all()
    return list(courses)

@router.post("/courses", response_model=CourseSchema)
def create_course(course: CourseSchema):
    try:
        department = Department.objects.get(id=course.department_id)  # Get department by id
        new_course = Course.objects.create(
            course_name=course.course_name,
            department=department,
            semester=course.semester,
            class_name=course.class_name,
            lecture_hours=course.lecture_hours,
            submitted_by=course.submitted_by
        )
        return new_course
    except Department.DoesNotExist:
        raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating course: {e}")

@router.put("/courses/{course_id}", response_model=CourseSchema)
def update_course(course_id: int, course: CourseSchema):
    try:
        existing_course = Course.objects.get(id=course_id)  
        department = Department.objects.get(id=course.department_id)  
        existing_course.course_name = course.course_name
        existing_course.department = department
        existing_course.semester = course.semester
        existing_course.class_name = course.class_name
        existing_course.lecture_hours = course.lecture_hours
        existing_course.submitted_by = course.submitted_by
        existing_course.save()  
        return existing_course
    except Course.DoesNotExist:
        raise HTTPException(status_code=404, detail="Course not found")
    except Department.DoesNotExist:
        raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating course: {e}")

# User Endpoints
@router.get("/users", response_model=List[UserSchema])
def list_users():
    users = User.objects.all()  # Django ORM: Use .all()
    return list(users)

@router.post("/users", response_model=UserSchema)
def create_user(user: UserSchema):
    try:
        new_user = User.objects.create(
            type=user.type,
            full_name=user.full_name,
            username=user.username,
            email=user.email,
            submitted_by=user.submitted_by
        )
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating user: {e}")

@router.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema):
    try:
        existing_user = User.objects.get(id=user_id)  # Retrieve user by id
        existing_user.type = user.type
        existing_user.full_name = user.full_name
        existing_user.username = user.username
        existing_user.email = user.email
        existing_user.submitted_by = user.submitted_by
        existing_user.save()  # Save updated user
        return existing_user
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating user: {e}")

# AttendanceLog Endpoints
@router.get("/attendance", response_model=List[AttendanceLogSchema])
def list_attendance_logs():
    attendance_logs = AttendanceLog.objects.all()  # Django ORM: Use .all()
    return list(attendance_logs)

@router.post("/attendance", response_model=AttendanceLogSchema)
def create_attendance_log(attendance: AttendanceLogSchema):
    try:
        student = Student.objects.get(id=attendance.student_id)
        course = Course.objects.get(id=attendance.course_id)
        submitted_by = User.objects.get(id=attendance.submitted_by_id)
        new_attendance = AttendanceLog.objects.create(
            student=student,
            course=course,
            present=attendance.present,
            submitted_by=submitted_by
        )
        return new_attendance
    except Student.DoesNotExist:
        raise HTTPException(status_code=404, detail="Student not found")
    except Course.DoesNotExist:
        raise HTTPException(status_code=404, detail="Course not found")
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating attendance log: {e}")

@router.put("/attendance/{attendance_id}", response_model=AttendanceLogSchema)
def update_attendance_log(attendance_id: int, attendance: AttendanceLogSchema):
    try:
        existing_attendance = AttendanceLog.objects.get(id=attendance_id)  # Retrieve by id
        student = Student.objects.get(id=attendance.student_id)
        course = Course.objects.get(id=attendance.course_id)
        submitted_by = User.objects.get(id=attendance.submitted_by_id)
        existing_attendance.student = student
        existing_attendance.course = course
        existing_attendance.present = attendance.present
        existing_attendance.submitted_by = submitted_by
        existing_attendance.save()  # Save changes
        return existing_attendance
    except AttendanceLog.DoesNotExist:
        raise HTTPException(status_code=404, detail="Attendance log not found")
    except Student.DoesNotExist:
        raise HTTPException(status_code=404, detail="Student not found")
    except Course.DoesNotExist:
        raise HTTPException(status_code=404, detail="Course not found")
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating attendance log: {e}")
