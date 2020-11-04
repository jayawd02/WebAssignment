from rest_framework import serializers
from plans.models import Goal, Meal, DietPlan, Exercise, WorkoutPlan


class GoalSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.first_name')

    class Meta:
        model = Goal
        exclude = ['date_created']


class MealSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.first_name')

    class Meta:
        model = Meal
        exclude = ['date_created']


class DietPlanSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.first_name')

    class Meta:
        model = DietPlan
        exclude = ['date_created']


class ExerciseSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.first_name')

    class Meta:
        model = Exercise
        exclude = ['date_created']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.first_name')

    class Meta:
        model = WorkoutPlan
        exclude = ['date_created']
