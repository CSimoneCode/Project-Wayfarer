from django.urls import path
from . import views

urlpatterns = [
    # Static urls
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Profile/User urls
    path('profile/', views.profile, name='profile'),
    path('profile/add_profile/', views.add_profile, name='add_profile'),
    path('profile/update_profile/', views.update_profile, name='update_profile'),
    # Posts
    # path('profile/', views.profile, name='profile'),
    # Cities
    # path('profile/', views.profile, name='profile'),
    # Auth
    path('registration/signup/', views.signup, name='signup'),
    # Post urls
    path('posts/<int:posts_id>', views.posts_detail, name='posts_detail') ### route tbd...may change dependent on other routes. 
]
