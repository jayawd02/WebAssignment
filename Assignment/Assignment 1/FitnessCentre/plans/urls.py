from django.urls import path

from plans.views import GoalListView, GoalDetailView
from plans import views as plan_views

urlpatterns = [
    path('goals/', GoalListView.as_view(), name='goal-list'),
    path ('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail')
    # path('profile/detail', user_views.profile_view, name='profile-detail'),
    # path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('posts/new/', PostCreateView.as_view(), name='post-create'),
    # path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]