from django.contrib import admin
from plans.models import Goal, DietPlan,WorkoutPlan,Meal, Exercise
# Register your models here.


admin.site.register(Goal)
admin.site.register(DietPlan)
admin.site.register(Meal)
admin.site.register(WorkoutPlan)
admin.site.register(Exercise)