from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from members.models import Member


# Create your models here.

class Goal(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    GoalType = models.TextChoices('GoalType', 'weight-loss weight-gain maintenance other')
    type = models.CharField(blank=True, null=True, choices=GoalType.choices, max_length=12)
    target_date = models.DateField()
    start_weight = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    goal_weight = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    start_BMI = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    goal_BMI = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    daily_calorie_limit = models.PositiveIntegerField(null=True, blank=True)
    protein = models.PositiveIntegerField(null=True, blank=True)
    carbs = models.PositiveIntegerField(null=True, blank=True)
    fat = models.PositiveIntegerField(null=True, blank=True)
    StatusChoice = models.TextChoices('StatusChoice', 'Active Inactive')
    status = models.CharField(blank=True,null=True,choices=StatusChoice.choices, max_length=10, default='Active')
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.type


class Meal(models.Model):
    name = models.CharField(max_length=50)
    MealType = models.TextChoices('MealType', 'Vegan Vegetarian Seafood Meat Other')
    type = models.CharField(blank=True, null=True, choices=MealType.choices, max_length=12)
    MealCategory = models.TextChoices('MealCategory', 'Main Snack Side Soup Salad Dessert Drink Other')
    category = models.CharField(blank=True, null=True, choices=MealCategory.choices, max_length=10)
    description = models.TextField(null=True, blank=True)
    calories = models.PositiveSmallIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class DietPlan(models.Model):
    goal= models.ForeignKey(Goal,on_delete=models.SET_NULL,null=True,blank=True)
    DayChoice = models.TextChoices('DayChoice', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday')
    day = models.CharField(choices=DayChoice.choices, max_length=10)
    MealGroup = models.TextChoices('MealGroup', 'breakfast lunch dinner snack ')
    type = models.CharField(choices=MealGroup.choices, max_length=10)
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)
    serving_size = models.CharField(max_length=20)
    calories = models.PositiveSmallIntegerField()
    StatusChoice = models.TextChoices('StatusChoice', 'Active Inactive')
    status = models.CharField(blank=True, null=True, choices=StatusChoice.choices, max_length=10, default='Active')
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.day


class Exercise(models.Model):
    name = models.CharField(max_length=25)
    ExerciseType = models.TextChoices('ExerciseType', 'Cardio Strength Leg Arm Abs Full-body Other')
    type = models.CharField(choices=ExerciseType.choices, max_length=10)
    equipments = models.CharField(null=True, blank=True, max_length=30)
    LevelChoice = models.TextChoices('LevelChoice', 'Beginner Intermediate Advanced Other')
    level = models.CharField(choices=LevelChoice.choices, max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    goal= models.ForeignKey(Goal,on_delete=models.SET_NULL,null=True,blank=True)
    DayChoice = models.TextChoices('DayChoice', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday')
    day = models.CharField(choices=DayChoice.choices, max_length=10)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    mins = models.PositiveSmallIntegerField(null=True,blank=True)
    rounds = models.PositiveSmallIntegerField(null=True,blank=True)
    reps = models.PositiveSmallIntegerField(null=True,blank=True)
    weight = models.PositiveSmallIntegerField(null=True, blank=True)
    calories_burn = models.PositiveSmallIntegerField()
    StatusChoice = models.TextChoices('StatusChoice', 'Active Inactive')
    status = models.CharField(blank=True, null=True, choices=StatusChoice.choices, max_length=10, default='Active')
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.day

