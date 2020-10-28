from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'goals', views.GoalViewSet)
router.register(r'meals', views.MealViewSet)
router.register(r'dietplans', views.DietPlanViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'workoutplans', views.WorkoutPlanViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('goals/', GoalListView.as_view(), name='goal-list'),
#     path ('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
#     path ('goals/<int:goal_id>/workoutplan/new',plan_views.workoutplan_create,name='workoutplan-create'),
#     path ('goals/workoutplan/',WorkoutPlanListView.as_view(), name='workoutplan-list'),
#
# ]