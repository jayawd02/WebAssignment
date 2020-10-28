from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import permissions
from django.views.generic import ListView, DetailView, CreateView
from plans.forms import GoalUpdateForm, WorkoutPlanUpdateForm
from plans.models import Goal, DietPlan, WorkoutPlan, Meal, Exercise
from .serializers import GoalSerializer,MealSerializer,DietPlanSerializer,ExerciseSerializer,WorkoutPlanSerializer
from .permissions import IsOwnerOrReadOnly
from sentry_sdk import capture_exception


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)





# class WorkoutPlanListView(ListView):
#     model = WorkoutPlan
#     template_name = 'plans/goalworkoutplan_list.html'
#
#     def get_queryset(self):
#         try:
#             goal_set = Goal.objects.filter(status='Active', member=self.request.user.member)
#         except Exception as e:
#             goal_set = None
#             capture_exception(e)
#
#         if goal_set != None:
#             return WorkoutPlan.objects.select_related('exercise').filter(goal=goal_set.last()).order_by('day')
#
#
# def workoutplan_create(request, goal_id):
#     goal = get_object_or_404(Goal, pk=goal_id)
#
#     if request.method == "POST":
#         workoutplan_update_form = WorkoutPlanUpdateForm(request.POST,
#                                                         instance=request.user)  # todo workout save not working.
#         if workoutplan_update_form.is_valid():
#             workoutplan_update_form.save()
#             messages.success(request, f'Your workout plan has been updated!')
#             return redirect('goal-list')
#     else:
#         workoutplan_update_form = WorkoutPlanUpdateForm(instance=request.user.member.goal_set.get(pk=goal.id))
#
#         context = {
#             'form': workoutplan_update_form,
#
#         }
#     return render(request, 'plans/workoutplan_form.html', context)


