from django.urls import path, include

from . import views

urlpatterns = [
    path('api/', include('users.api.urls')),
    #path('register/', views.register, name='register'),
    #path('', include('django.contrib.auth.urls')),
]