from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from gallery import views as gallery_views
from rest_framework.authtoken import views

urlpatterns = [
    path('members/', include('members.urls')),
    path('users/', include('users.urls')),
    path('gallery/', include('gallery.urls')),
    path('plans/', include('plans.urls')),
    path('profile/', user_views.profile, name='profile'),
    path('profile/detail', user_views.profile_view, name='profile-detail'),
    path('register/', user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('users/', include('django.contrib.auth.urls')),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='members/home.html'), name='home'),
    path('api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)