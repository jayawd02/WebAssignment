from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date of birth')

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    lecturer_name = models.CharField(max_length=250)
    course_Description = models.TextField()
    credits = models.IntegerField()
    enrollment = models.ManyToManyField(Student)

class TimeTable(models.Model):
    class_date = models.DateTimeField()
    class_startTime = models.DateTimeField()
    class_endTime = models.DateTimeField()
    class_room = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
