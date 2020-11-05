from django import forms
from .models import Profile, Posts, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'current_city',
            'past_cities',
            'pic'
        ]

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'content'
        ]


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = [
            'title',
            'content'
        ]


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
