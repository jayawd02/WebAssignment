from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/timetable/', views.timetable, name='timetable'),
    path('<int:course_id>/enrollments/', views.enrollments, name='enrollments'),
]