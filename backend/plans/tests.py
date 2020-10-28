from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from members.models import Member
from plans.models import Goal, Meal, DietPlan, Exercise, WorkoutPlan


class TestModels(TestCase):
    fixtures = ["goal.json", "meal.json","dietplan.json","exercise.json","workoutplan.json", "member.json","user.json"]

    def setUp(self):
        member = Member.objects.get(pk=1)
        user= User.objects.get(pk=7)


    def test_should_create_goal(self):
        goal = Goal.objects.get(pk=1)
        self.assertEqual(goal.type, "weight-loss")

    def test_should_create_meal(self):
        meal = Meal.objects.get(pk=1)
        self.assertEqual(meal.name, "Rice and curry")

    def test_should_create_dietplan(self):
        dietplan = DietPlan.objects.get(pk=1)
        self.assertEqual(dietplan.day, "Monday")

    def test_should_create_exercise(self):
        exercise = Exercise.objects.get(pk=1)
        self.assertEqual(exercise.name, "Cardio")

    def test_should_create_workoutplan(self):
        workoutplan = WorkoutPlan.objects.get(pk=1)
        self.assertEqual(workoutplan.day, "Monday")
