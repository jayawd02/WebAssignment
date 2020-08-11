from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Genre, Video


# Create your views here.

def index(request):
    #return HttpResponse('welcome to beta netflix')
    genres =Genre.objects.all()
    videos= Video.objects.all()

   # return render(request,'index.html',{'video': video })
    return render(request,'index.html',{'videos': videos, 'genres': genres})

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    genres=video.genres
    return render(request,'detail.html',{'video': video, 'genres':genres})