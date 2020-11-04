from django.urls import path,include

from .views import GoalListView, GoalDetailView, WorkoutPlanListView
from . import views as plan_views


urlpatterns = [
    path('api/', include('plans.api.urls')),
    path('goals/', GoalListView.as_view(), name='goal-list'),
    path ('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path ('goals/<int:goal_id>/workoutplan/new',plan_views.workoutplan_create,name='workoutplan-create'),
    path ('goals/workoutplan/',WorkoutPlanListView.as_view(), name='workoutplan-list'),

]