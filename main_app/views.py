from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Posts, City
from .forms import PostsForm, ProfileForm


# --------------------------- STATIC PAGES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# --------------------------- PROFILE 
@login_required
def profile(request):
    found_user = User.objects.filter(id=request.user.id)
    posts = Posts.objects.filter(author=request.user.id)
    profile = Profile.objects.filter(user=request.user)[0]    
    context = {
        'profile': profile,
        'found_user': found_user,
        'posts': posts
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
        context = {
            'profile_form': profile_form, 
            'error_message': error_message
        }
        return render(request, 'profiles/add.html', context)

##update profile currently incomplete

@login_required
def update_profile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            return redirect('profile')
        else:
            error_message = 'Something went wrong - try again'
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'profile_form': profile_form, 
            'error_message': error_message
        }
        return render(request, 'profiles/edit.html', context)


# --------------------------- POSTS
def posts_detail(request, posts_id):
    posts = Posts.objects.get(id=posts_id)
    context = { 'post': posts } #Transition to singular post! For semantics.
    return render(request,'posts/detail.html', context)


@login_required
def delete_post(request, posts_id):
    if request.method == 'POST':
        Posts.objects.get(id=posts_id).delete()

        # Will probably want to redirect to the cities page once those are up
        return redirect('profile')


@login_required
def edit_post(request, posts_id):
    found_post = Posts.objects.get(id=posts_id)
    if request.method == 'POST':
        post_form = PostsForm(request.POST, instance=found_post)
        if post_form.is_valid():
            updated_post = post_form.save()
            return redirect('posts_detail', updated_post.id)
    else:
        post_form = PostsForm(instance=found_post)
        context = {
            'post': found_post,
            'post_form': post_form
        }
        return render(request, 'posts/edit.html', context)
            

# --------------------------- CITIES

def cities_index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'cities/index.html', context)


def cities_detail(request, city_id):
    found_city = City.objects.get(id=city_id)
    posts = Posts.objects.filter(city = found_city.id).order_by('-post_date')
    print(f'city {found_city} posts {posts}')
    context = {
        'city': found_city,
        'posts': posts
    }
    return render(request, 'cities/detail.html', context)


# --------------------------- AUTH
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
    context = {
        'form': form, 
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)


