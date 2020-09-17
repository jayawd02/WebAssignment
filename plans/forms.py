from django import forms

from plans.models import WorkoutPlan, Goal


class WorkoutPlanUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        exclude = ['date_created', 'status','created_by']


class GoalUpdateForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ['date_created', 'status','created_by']
