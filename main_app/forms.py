from django import forms
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'date_of_birth',
            'photo',
            'location',
            'bio',
            'account_type',
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'photo',
            'public'
        ]


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=240)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    