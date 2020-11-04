from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterAPIView, LoginAPIView

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
   ## path('logout', LogoutView.as_view(), name='knox_logout') #todo logout url

]