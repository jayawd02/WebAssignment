from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from members.models import Member
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "email",  "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['address_line1','address_line2','contact_no1','contact_no2','email','date_of_birth',
                  'health_problems','allergies','meal_preference','height','gender']
