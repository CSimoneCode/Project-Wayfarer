from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Posts, City, Comment
from .forms import PostsForm, ProfileForm, SignupForm, CommentForm
from django.conf import settings
from django.core.mail import send_mail
from pyuploadcare.dj.models import ImageField


# --------------------------- STATIC PAGES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# --------------------------- PROFILE 
@login_required
def profile(request):
    posts = Posts.objects.filter(author=request.user.id)
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.filter(author=request.user.id)

    context = {
        'profile': profile,
        'posts': posts,
        'comments': comments,
        'num_comments': len(comments),
        'num_posts': len(posts)
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


@login_required
def update_profile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
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
    comments = Comment.objects.filter(parent_post_id=posts_id)
    num_comments = len(comments)
    context = {
        'post': posts,
        'comments': comments,
        'num_comments': num_comments
    }
    return render(request,'posts/detail.html', context)



@login_required
def add_post(request, city_id):
    city = City.objects.get(id=city_id)
    if request.method == 'POST':
        posts_form = PostsForm(request.POST)
        if posts_form.is_valid():
            new_post = posts_form.save(commit=False)
            new_post.author_id = request.user.id
            new_post.city = city
            new_post.save()
            return redirect('posts_detail', new_post.id)
    else: 
        posts_form = PostsForm()
        context = {
            'posts_form': posts_form,
            'city': city
        }
        return render(request, 'posts/add.html', context)


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
    context = {
        'city': found_city,
        'posts': posts
    }
    return render(request, 'cities/detail.html', context)


# --------------------------- COMMENTS
@login_required
def add_comment(request, city_id, posts_id):
    city = City.objects.get(id=city_id)
    found_post = Posts.objects.get(id=posts_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author_id = request.user.id
            new_comment.parent_post_id = posts_id
            new_comment.save()
            return redirect('posts_detail', posts_id)
    else:
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'city': city,
            'post': found_post
            }
        return render(request, 'comments/add.html', context)


@login_required
def update_comment(request, city_id, posts_id, comment_id):
    comment_to_edit = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment_to_edit)
        if comment_form.is_valid():
            updated_comment = comment_form.save()
            return redirect('posts_detail', posts_id)
    else:
        comment_form = CommentForm(instance=comment_to_edit)
        context = {
            'comment_form': comment_form,
            'comment': comment_to_edit
        }
        return render(request, 'comments/edit.html', context)


@login_required
def delete_comment(request, posts_id, comment_id):
    if request.method == 'POST':
        Comment.objects.get(id=comment_id).delete()
        return redirect('posts_detail', posts_id)


# --------------------------- AUTH
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            new_email = user.email
            if User.objects.filter(email=new_email):
                error_message = 'Email already exists'
            else:
                user = form.save()
                subject = 'Welcome, Traveler.'
                message = f"Hello {user}, and welcome to Wayfarer.\nRemember to leave people and places better than you found them <3"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, email_from, recipient_list)
                login(request, user)
                return redirect('add_profile')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignupForm()
    context = {
        'form': form, 
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)


