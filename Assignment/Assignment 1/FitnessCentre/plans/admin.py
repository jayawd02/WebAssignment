from django.contrib import admin
from plans.models import Goal, DietPlan,WorkoutPlan,Meal, Exercise
# Register your models here.

class WorkoutPlanInLine(admin.TabularInline):
    model = WorkoutPlan
    exclude = ['date_created','status','created_by']
    extra = 5

class DietPlanInLine (admin.TabularInline):
    model=DietPlan
    exclude = ['date_created', 'created_by','status']
    extra = 7

class GoalAdmin(admin.ModelAdmin):
    #fields = ['author','content', 'image']
    list_display = ('member','type','status','date_created','created_by')
    list_filter = ['member', 'status']
    search_fields = ['member']

    inlines =[WorkoutPlanInLine,DietPlanInLine]

class MealAdmin(admin.ModelAdmin):
    fields = ['name','type', 'category','calories', 'description','created_by']
    list_display = ('name', 'type', 'category','calories', 'date_created', 'created_by')
    list_filter = ['type', 'category','calories']
    search_fields = ['name']

class ExerciseAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'equipments', 'level',  'created_by']
    list_display = ('name', 'type', 'level', 'date_created', 'created_by')
    list_filter = ['type', 'level']
    search_fields = ['name']

class DietPlanAdmin(admin.ModelAdmin):

    list_display = ('goal', 'day', 'type', 'meal','date_created', 'created_by')
    list_filter = ['goal','day', 'type']
    search_fields = ['goal']

class WorkoutPlanAdmin(admin.ModelAdmin):

    list_display = ('goal', 'day', 'exercise','date_created', 'created_by')
    list_filter = ['goal','day']
    search_fields = ['goal']


admin.site.register(Goal,GoalAdmin)
admin.site.register(DietPlan,DietPlanAdmin)
admin.site.register(Meal,MealAdmin)
admin.site.register(WorkoutPlan,WorkoutPlanAdmin)
admin.site.register(Exercise,ExerciseAdmin)

