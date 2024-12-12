from django.db import models  

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    lecture_hours = models.IntegerField()
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

class AttendanceLog(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    present = models.BooleanField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)