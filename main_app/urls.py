from django.urls import path
from . import views

urlpatterns = [
    # Static urls
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Profile/User urls
    path('profile/', views.profile, name='profile'),
    path('profile/new/', views.add_profile, name='add_profile'),
    path('registration/signup/', views.signup, name='signup'),
    
]