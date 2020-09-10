from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView

from plans.forms import GoalUpdateForm, WorkoutPlanUpdateForm
from plans.models import Goal, DietPlan, WorkoutPlan, Meal, Exercise


class GoalListView(ListView):
    model = Goal
    ordering = ['-date_created']  # order the posts newest at top


class GoalDetailView(DetailView):
    model = Goal


# @login_required
# def goal_create(request):
#     if request.method == "POST":
#         goal_update_form = GoalUpdateForm(request.POST, instance=request.user.member)
#         workoutplan_update_form = WorkoutPlanUpdateForm(request.POST, instance=request.user.member)
#
#         if goal_update_form.is_valid() and workoutplan_update_form.is_valid() :
#             goal_update_form.save()
#             workoutplan_update_form.save()
#
#             messages.success(request, f'Your goal and workout plan has been updated!')
#             return redirect('goal-detail')
#     else:
#         goal_update_form = GoalUpdateForm(instance=request.user.member)
#         workoutplan_update_form = WorkoutPlanUpdateForm(instance=request.user.member)
#
#
#     context = {
#         'g_form': goal_update_form,
#         'w_form': workoutplan_update_form,
#
#     }
#
#     return render(request, 'plans/goal_form.html',context)


class DietPlanListView(ListView):
    model = DietPlan


class DietPlanDetailView(DetailView):
    model = DietPlan


class WorkoutPlanListView(ListView):
    model = WorkoutPlan
    template_name = 'plans\goalworkoutplan_list.html'

    def get_queryset(self):
        goal = get_object_or_404(Goal, id= self.kwargs.get('goal_id'))
        return WorkoutPlan.objects.filter(goal=goal).order_by('day')


class WorkoutPlanDetailView(DetailView):
    model = WorkoutPlan


def workoutplan_create(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)

    if request.method == "POST":
        workoutplan_update_form = WorkoutPlanUpdateForm(request.POST,
                                                        instance=request.user)  # todo workout save not working.
        if workoutplan_update_form.is_valid():
            workoutplan_update_form.save()
            messages.success(request, f'Your workout plan has been updated!')
            return redirect('goal-list')
    else:
        workoutplan_update_form = WorkoutPlanUpdateForm(instance=request.user.member.goal_set.get(pk=goal.id))

        context = {
            'form': workoutplan_update_form,

        }
    return render(request, 'plans/workoutplan_form.html', context)


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
