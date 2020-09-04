from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import VideoListView
from .views import RecipeListView

urlpatterns = [
    #path('posts/', views.posts, name='posts'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('recipe/', RecipeListView.as_view(), name='recipe-list'),

]