from django.urls import path, include
from .views import  UpdatePostVote
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet,RecipeViewSet, PostViewSet
from gallery import views

router = DefaultRouter()
router.register(r'videos', views.VideoViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# recipe_list = RecipeViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# recipe_detail = RecipeViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# video_list = VideoViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# video_detail = VideoViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# post_list = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# post_detail = PostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = [
#     path('posts/', post_list, name='post-list'),
#     path('posts/<int:pk>/', post_detail, name='post-detail'),
#     path('posts/new/', post_list, name='post-create'),
#     path('posts/<int:pk>/update/', post_detail, name='post-update'),
#     path('posts/<int:pk>/delete/', post_detail, name='post-delete'),
#     #path('posts/<int:pk>/<str:opinion>/', UpdatePostVote.as_view(), name='post-vote'),
#     path('videos/', video_list, name='video-list'),
#     path('videos/<int:pk>/', video_detail, name='video-detail'),
#     path('videos/new/', video_list, name='video-create'),
#     path('videos/<int:pk>/update/', video_detail, name='video-update'),
#     path('videos/<int:pk>/delete/', video_detail, name='video-delete'),
#     path('recipe/', recipe_list, name='recipe-list'),
#     path('recipe/<int:pk>/', recipe_detail, name='recipe-detail'),
#     path('recipe/new/', recipe_list, name='recipe-create'),
#     path('recipe/<int:pk>/update/', recipe_detail, name='recipe-update'),
#     path('recipe/<int:pk>/delete/', recipe_detail, name='recipe-delete'),
# ]