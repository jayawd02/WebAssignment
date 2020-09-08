from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView

from plans.models import Goal, DietPlan, WorkoutPlan, Meal, Exercise


class GoalListView(ListView):
    model = Goal
    ordering = ['-date_created']  # order the posts newest at top

class GoalDetailView(DetailView):
    model=Goal


class DietPlanListView(ListView):
    model = DietPlan

class DietPlanDetailView(DetailView):
    model = DietPlan


class WorkoutPlanListView(ListView):
    model = WorkoutPlan


class WorkoutPlanDetailView(DetailView):
    model = WorkoutPlan

# class WorkoutPlanCreateView(LoginRequiredMixin, CreateView)  :
#     model=WorkoutPlan
#     fields = ['goal', 'day','exercise', 'mins','rounds','reps','weight','calories_burn']
#
#     def form_valid(self, form):  # pass the current logged in user as author to the model
#         form.instance.author = self.request.user
#         return super(WorkoutPlanCreateView, self).form_valid(form)
#


class MealListView(ListView):
    model = Meal


class MealDetailView(DetailView):
    model = Meal

class ExerciseListView(ListView):
    model = Exercise


class ExerciseDetailView(DetailView):
    model = Meal