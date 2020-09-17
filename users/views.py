from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, MemberUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required # check if login or not if not redirect to login URL set in settings
def profile(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES , instance=request.user.profile)
        member_update_form = MemberUpdateForm(request.POST,instance=request.user.member)
        if user_update_form.is_valid() and profile_update_form.is_valid() and member_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            member_update_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile-detail')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
        member_update_form = MemberUpdateForm(instance=request.user.member)

    context = {
        'u_form': user_update_form,
        'p_form': profile_update_form,
        'm_form' : member_update_form,
    }

    return render(request, 'users/profile.html',context)

def profile_view (request):
    #user = get_object_or_404(User, pk=request.user.id)
    return render(request, 'users/profile_detail.html')