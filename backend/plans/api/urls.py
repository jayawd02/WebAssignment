from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'goals', views.GoalViewSet)
router.register(r'meals', views.MealViewSet)
router.register(r'dietplans', views.DietPlanViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'api/workoutplans', views.WorkoutPlanViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

