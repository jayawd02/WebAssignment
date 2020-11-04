from django.urls import path,include
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, UpdatePostVote
from .views import VideoListView, VideoDetailView,VideoCreateView,VideoUpdateView, VideoDeleteView
from .views import RecipeListView, RecipeDetailView,RecipeCreateView, RecipeUpdateView, RecipeDeleteView
from . import views as gallery_views


urlpatterns = [
    path('api/', include('gallery.api.urls')),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', gallery_views.post_detail, name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/<str:opinion>/', UpdatePostVote.as_view(), name='post-vote'),
    #path('posts/<int:post_id>/comment/',gallery_views.postcomment_create,name='post-comment'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('videos/new/', VideoCreateView.as_view(), name='video-create'),
    path('videos/<int:pk>/update/', VideoUpdateView.as_view(), name='video-update'),
    path('videos/<int:pk>/delete/', VideoDeleteView.as_view(), name='video-delete'),
    path('recipe/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),

]