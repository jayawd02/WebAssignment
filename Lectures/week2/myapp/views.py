from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

# Create your views here.
from myapp.models import Course, TimeTable, Student


def index(request):
    course_list = Course.objects.all()
    context = { 'course_list': course_list}
    return render(request, 'myapp/index.html', context)

def detail (request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'myapp/detail.html', {'course': course})


def timetable(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'myapp/timetable.html', {'course': course})


def enrollments (request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.enrollment
    return render(request, 'myapp/enrollments.html', {'course': course,'students': students})
