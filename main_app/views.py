from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile, Posts
# from .forms import PostsForm 
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

    user = User.objects.filter(id=request.user.id)
    if len(Profile.objects.filter(user=request.user)) == 0:
        context = {
            'user': user
        }
    else:
        profile = Profile.objects.filter(user=request.user)[0]    
        context = {
            'profile': profile,
            'user': user
        }
    return render(request, 'profiles/index.html', context)

@login_required
def add_profile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user_id = request.user.id
            new_profile.save()
            return redirect('profile')
        else:
            error_message = 'Something went wrong - try again'
    else:
        profile_form = ProfileForm()
        context = {'profile_form': profile_form, 'error_message': error_message}
        return render(request, 'profiles/add.html', context)

##update profile currently incomplete

@login_required
def update_profile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile) ######################CHECK Here
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            return redirect('profile')
        else:
            error_message = 'Something went wrong - try again'
    else:
        # if len(Profile.objects.filter(user=request.user)) != 0:
        profile_form = ProfileForm(instance=request.user.profile)
        # else:
        # profile_form = ProfileForm()

        context = {'profile_form': profile_form, 'error_message': error_message}
        return render(request, 'profiles/edit.html', context)


# --------------------------- Auth
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_profile')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



# --------------------------- POSTS
@login_required
def posts_index(request):                       ### We don't have a City model yet or have the Profile yet so we'll refactor this when we have that
    posts = Posts.objects.filter(profile=request.profile) 
    pass

def posts_detail(request, posts_id):
    posts = Posts.object.get(id=posts_id)
    context = { 'post': posts } #Transition to singular post! For semantics.
    return render(request,'posts/detail.html', context)
