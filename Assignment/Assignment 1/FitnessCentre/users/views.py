from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "users/register.html", {"form": form})


@login_required # check if login or not if not redirect to login URL set in settings
def profile(request):
    return render(request, 'users/profile.html')
