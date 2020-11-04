from django.urls import path,include

from . import views

urlpatterns = [
    path('api/', include('members.api.urls')),
    path('', views.index, name='index'),
]