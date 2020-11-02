from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


# --------------------------- STATIC PAGES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# --------------------------- PROFILE 
@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user)[0]
    user = User.objects.filter(id=request.user.id)
    context = {
        'profile': profile,
        'user': user
    }
    return render(request, 'profiles/index.html', context)


@login_required
def update_profile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
        else:
            error_message = 'Something went wrong - try again'
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        context = {'profile_form': profile_form, 'error_message': error_message}
        return render(request, 'profiles/edit.html', context)


# --------------------------- POSTS
@login_required
def posts_index(request):
    pass


# --------------------------- Auth
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


