from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField('date of birth')

    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    lecturer_name = models.CharField(max_length=250)
    course_Description = models.TextField()
    credits = models.IntegerField()
    enrollment = models.ManyToManyField(Student)
    def __str__(self):
        return self.course_name


class TimeTable(models.Model):
    class_date = models.DateField()
    class_startTime = models.TimeField()
    class_endTime = models.TimeField()
    class_room = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)


