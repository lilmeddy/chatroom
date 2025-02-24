from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "bio", "profile_picture"]