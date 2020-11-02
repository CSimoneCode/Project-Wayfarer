from django import forms
from .models import Profile, Posts


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'current_city',
            'past_cities'
        ]

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            # 'author',
            'content'
        ]


        