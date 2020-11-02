from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile, Posts
from .forms import PostsForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# --------------------------- STATIC PAGES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# --------------------------- PROFILE 
@login_required
def profile(request):

    return render(request, 'profile.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# --------------------------- POSTS
@login_required
def posts_index(request):                       ### We don't have a City model yet so we'll refactor this when we have that
    posts = Posts.objects.filter(profile=request.profile) 
    pass
